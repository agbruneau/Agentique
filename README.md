# Agentique

[![appareil](https://github.com/agbruneau/Agentique/actions/workflows/appareil.yml/badge.svg)](https://github.com/agbruneau/Agentique/actions/workflows/appareil.yml)

Un corpus de recherche en français sur une seule question : *comment une entreprise de services financiers canadienne déploie, gouverne et exploite des agents d'IA
autonomes sous contrainte réglementaire ?* Sept documents livrables l'instruisent, un simulateur Rust transpose l'un d'eux. André-Guy Bruneau en répond ; la rédaction est assistée par des agents de modèle, déclarés pièce par pièce à [`CONTRIBUTIONS.md`](CONTRIBUTIONS.md).

**État :** rouvert le 15 septembre 2026 par la décision [D-17](<2%20-%20Compendium/PRD/PRD.md#d-17>) pour exécuter le [plan](<Plan%20d%27ex%C3%A9cution%20%E2%80%94%20%C3%A9valuation%20acad%C3%A9mique.md>) tiré de
l'[évaluation académique](<%C3%89valuation%20acad%C3%A9mique.md>) du même jour — 75,5 / 100, corrections majeures requises, rendue par un modèle de langage ;
re-clôture prévue vers le 8 décembre 2026. La forme est vérifiée par un appareil rejoué à chaque poussée ; le fond ne l'est par aucun humain
autre que l'auteur : aucun relecteur nommé, relecture préparée à [`RELECTURE.md`](RELECTURE.md). Licence CC BY 4.0 ([`LICENSE`](LICENSE)).

| Temps | Par où entrer |
|---|---|
| cinq minutes | [*Cinq schémas*](<5%20-%20Recension/Cinq%20sch%C3%A9mas%20%E2%80%94%20%C3%A9tat%20de%20l%27art%20en%20services%20financiers.pdf>), 7 p. — les figures de l'état de l'art, commentées |
| trois quarts d'heure | [*Note de synthèse*](<3%20-%20Veille/Note%20de%20synth%C3%A8se.pdf>), 21 p. — veille, revue et état de l'art condensés, chaque affirmation renvoyée à sa section |
| le fond | les trois monographies de [`1 - Collection/`](<1%20-%20Collection/>), dans l'ordre ; la veille, 144 p., pour l'état du champ déployé |
| du code | [`4 - Essais/1 - Traité/`](<4%20-%20Essais/1%20-%20Trait%C3%A9/>) — le simulateur d'essaims, 470 tests |

## Les sept livrables

Compte et statuts fixés par la décision [D-18](<2%20-%20Compendium/PRD/PRD.md#d-18>) du 15 septembre 2026 ; toute entrée ou sortie passe par une décision. Réserve commune aux sept : aucun relecteur humain nommé.

| Vol. | Document | Dossier | Rendu | Statut |
|---|---|---|---|---|
| I | *Interopérabilité agentique en entreprise dans le domaine des services financiers* | [`1 - Collection/1 - InteroperabiliteAgentique/`](<1%20-%20Collection/1%20-%20InteroperabiliteAgentique/>) | 570 p. | livrable |
| II | *Orchestration agentique* | [`1 - Collection/2 - OrchestrationAgentique/`](<1%20-%20Collection/2%20-%20OrchestrationAgentique/>) | 387 p. | livrable |
| III | *L'entreprise agentique — la fabrique de confiance* | [`1 - Collection/3 - EntrepriseAgentique/`](<1%20-%20Collection/3%20-%20EntrepriseAgentique/>) | 427 p. | livrable sous réserve déclarée : quinze remontées ouvertes, une dette de vote |
| V | *Traité sur les systèmes multiagents en essaim* | [`4 - Essais/1 - Traité/`](<4%20-%20Essais/1%20-%20Trait%C3%A9/>) | 143 p. | livrable |
| VI | *Veille technologique en entreprise* | [`3 - Veille/`](<3%20-%20Veille/>) | 144 p. | livrable |
| VII | *Revue de la littérature académique* | [`3 - Veille/`](<3%20-%20Veille/>) | 59 p. | livrable |
| VIII | *État de l'art en services financiers*, et sa planche | [`5 - Recension/`](<5%20-%20Recension/>) | 186 p. et 7 p. | livrable |

Hors compte, par la même décision : le Vol. IV, [`2 - Compendium/`](<2%20-%20Compendium/>), 1 000 p., archive de travail ; quatre documents publiés — la note de veille SDLC (49 p.)
et la note de synthèse (21 p.) sous `3 - Veille/`, l'article HPC-QPU (38 p.) sous `4 - Essais/2 - Article/`, [`NiveauMaturité.html`](NiveauMaturit%C3%A9.html) (7 diapositives) ; l'appareil — évaluation, gabarit, plan ; le mémoire de maîtrise de l'auteur (1997), pièce déposée.

**Refaire et vérifier :** [`APPAREIL.md`](APPAREIL.md) donne chaque point d'entrée, son dossier et sa dernière sortie ; [`appareil.yml`](.github/workflows/appareil.yml) les rejoue sous Linux et Windows ; chaque `README` dit ce qui se refait dans son dossier.

**Journal :** [`JOURNAL.md`](JOURNAL.md) reçoit la chronique de cette page — clôtures, réouvertures, rangements, relevés de l'arbre, carte du dépôt — ; chaque dossier
numéroté tient la sienne. Le 5 septembre 2026, `3 - Traité/` est devenu `4 - Essais/1 - Traité/`, `4 - Veille/` `3 - Veille/`, et `6 - Article/` `4 - Essais/2 - Article/`.
