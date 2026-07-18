# CLAUDE.md — Borealis (code)

Démonstrateur Go d'interopérabilité agentique (**MCP + A2A**), cas de pré-qualification de crédit.
Vit sous `1 - Corpus Agentique/1 - InteroperabiliteAgentique/Borealis-Go/` dans le dépôt d'écriture
*Monographies* : c'est le livrable **de code** du volume I. Matérialise le PRD (`PRD-Borealis.md`) et
son plan d'exécution (`PRDPlan-Borealis.md`). **Source de vérité = le PRD.**

Ce fichier prime dans ce répertoire : le `CLAUDE.md` du volume I régit la **rédaction**, celui-ci le
**code**. Rien ici ne concerne la monographie, ses bibliographies ou son pipeline PDF.

## Règles non négociables (PRDPlan §2)

- **Jamais d'octroi ferme.** Aucun chemin de code d'octroi ; le e2e s'arrête à la pré-évaluation (FR-25, invariant 1).
- **Déterminisme.** Le fake `Reasoner` est le défaut ; `make e2e` × 3 → **sorties canoniques** identiques (horloge/IDs injectables, champs volatils exclus). Aucun LLM réel dans le gate.
- **Golden immuables** dès la clôture de la phase qui les couvre ; modification ultérieure ⇒ ADR.
- **Aucun PII réel** ; générateur de données seedé et déterministe.
- **TDD** : test d'acceptation qui échoue d'abord, puis on le fait passer.
- **Couverture > 90 %** (directive utilisateur, 2026-07-07 ; relève NFR-11 de 80 → 90 % global) : plancher du gate à 90 % dès M0 ; `main()` gardés **minces** (logique en `run(ctx)` testable) pour l'atteindre ; unitaire ≥ 95 % sur `internal/*`.
- **Écarts au PRD** : jamais de déviation silencieuse ⇒ ADR d'écart (`docs/adr/`) + rapport de phase.
- **Pas de CI distante** : rigueur locale via `scripts/check.{sh,ps1}`.

## Commandes

```bash
make check          # gate complet (build, vet, test[+race si CGO], vuln, lint, couverture)
make test           # tests ; make race (requiert CGO/gcc) ; make coverage ; make bench
make build          # binaires cmd/ → ./build ; make e2e ; make audit-export
bash scripts/check.sh   # plancher de couverture 90 % par défaut (directive utilisateur > 90 %)
```

## Contraintes d'hôte connues (voir docs/verification-p01.md)

- **Docker absent** → `docker compose` / build reproductible non vérifiables localement (hôte CGO/Linux + Docker requis).
- **CGO/gcc absent** → `-race` sauté avec avertissement ; requis sur hôte CGO.

## Conventions

- Commits **conventionnels, en français**, par exigence/tâche (`feat(mcp): …`, `test(a2a): …`).
- ADR au format PRD §14 (avec *Reversal condition*). Raccourcis délibérés marqués `// ponytail:`.
- Dépendances externes ajoutées à leur premier usage. Versions épinglées (P0.1).
