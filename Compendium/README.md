# Compendium de l'entreprise agentique (`Compendium`)

[Retour à l'index principal](../README.md) · [Suite intégrale (`Corpus/`)](../Corpus/README.md) · [Éditions structurées (`Tomes/`)](../Tomes/README.md) · [Cartographie (`Tomes/Cartographie/`)](../Tomes/Cartographie/README.md) · [PRD maître (`prd.md`)](prd.md) · [Plan directeur (`plan.md`)](plan.md)

Ce répertoire accueille la production du **Compendium** fondé sur le référentiel directeur [`prd.md`](prd.md) et orchestré par le plan directeur [`plan.md`](plan.md). L'infrastructure de cartographie et de traçabilité rattachée réside dans [`Tomes/Cartographie/`](../Tomes/Cartographie/README.md).

## Contenu actuel

- [`prd.md`](prd.md) : référentiel directeur d'exigences produit, d'architecture et d'homologation (`12` domaines `D01–D12`, `36` chapitres, `71` familles, `260` thèmes, `5` annexes `A–E`, `115` schémas de vulgarisation raccordés aux `319` diagrammes des Tomes 1 à 8).
- [`plan.md`](plan.md) : plan directeur exécutable de production, d'illustration et d'homologation vérifiable `G0`–`G5` (`6` sections, `9` tâches `Task 1`–`Task 9`, `12` parties `D01`–`D12`, `36` fiches chapitres `CH-01`–`CH-36`, `5` annexes `A`–`E` et `22` critères `CA-01`–`CA-22`, vérifié par [`Tomes/Cartographie/tests/test_plan.py`](../Tomes/Cartographie/tests/test_plan.py)).
- [`dashboard/`](dashboard/server.py) : tableau de bord web local en direct fondé sur [`plan.md`](plan.md) et sondant `Compendium/ouvrage/` (`python -B Compendium/dashboard/server.py --port 8765`, vérifié par [`dashboard/test_dashboard.py`](dashboard/test_dashboard.py)).
- [`Tomes/Cartographie/`](../Tomes/Cartographie/README.md) : cartographie thématique et structurelle complète du corpus (outillage Python, données JSON, suites `pytest` et deux applications HTML autonomes hors ligne) :
  - [`MindMap - Cartographie thématique du Corpus.html`](../Tomes/Cartographie/MindMap%20-%20Cartographie%20th%C3%A9matique%20du%20Corpus.html) (5 vues dynamiques incluant la Vue 5 `PRD Maître`)
  - [`PRD - Référentiel directeur de l'entreprise agentique.html`](../Tomes/Cartographie/PRD%20-%20R%C3%A9f%C3%A9rentiel%20directeur%20de%20l%27entreprise%20agentique.html) (lecteur web autonome du PRD avec pont vers la MindMap et le Graphe)
