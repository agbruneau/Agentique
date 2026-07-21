# Chapitre 24 — L'observabilité agentique : voir ce que fait un agent identifié

| Champ | Valeur |
|---|---|
| Statut | **Gabarit** — aucune rédaction. Valeurs admises : Gabarit / Rédigé (premier jet) / Rédigé et relu adversarialement |
| Date de gel de l'information | — (à renseigner à la rédaction, et reportée au registre `99-registre-gel.md` au **même commit**) |
| Socle mobilisé (PRD §7) | H-14, H-27 |
| Garde-fous à surveiller (PRD §8) | **R-03 — siège de la définition d'auteur d'« AgentOps » (§24.1)** ; **R-07** — Instana : degré 3 (socle muet) ; watsonx.governance : degré 2 (fait négatif établi) — **ne pas généraliser** ; R-06 (§24.3) |
| Volumétrie cible | ~3400 mots |

> **Thèse ([TOC.md](../../doc/TOC.md))** : l'AgentOps commence par l'observabilité, et l'observabilité agentique a trouvé son socle de standardisation dans les conventions sémantiques GenAI/agents d'OpenTelemetry — mais tracer un *appel* n'est pas tracer une *délégation* : la corrélation entre trace d'exécution et chaîne de mandat est le chaînon manquant que l'ouvrage documente.

---

<!-- GOUVERNANCE — bloc à supprimer à la rédaction ; hors décompte de volumétrie (PRDPlan §1.5)
Lot d'instruction : L-14
Règle cardinale (PRD §7.0) : ne rien rédiger avant la clôture du lot ci-dessus.
Boucle qualité obligatoire : PRDPlan §5.2 — sept étapes, dont la relecture adversariale
  par un relecteur distinct du rédacteur (CA-14), et l'amendement du socle en premier
  lorsque la faute y siège.
Formulations imposées : PRDPlan §5.5. Motifs de balayage : PRD §A.6.
Escalade : un rédacteur ne corrige jamais le PRD, le TOC ni ce plan — il remonte (PRDPlan §5.3).
-->
