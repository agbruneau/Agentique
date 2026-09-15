# Volume I — Interopérabilité agentique en entreprise dans le domaine des services financiers

**Lire :** [`Monographie.pdf`](Monographie.pdf) (571 p.) — sept chapitres et l'Annexe B, rendus en un seul volume.

Le premier des trois volumes du [corpus](../README.md) : le cadre général et mondial, dont le Vol. II tire le cas canadien
réglementé et le Vol. III le verrou identitaire. Thèse : les systèmes agentiques ne rendent pas obsolètes les principes
d'intégration, ils les réinstancient — *découplage, contrat, évolution* — et l'autonomie des agents se gradue sous contrôle
de finalité. L'Annexe B projette l'ouvrage sur une coopérative fictive, Boréalis, en architecture détaillée de solution sur la
pile IBM : 18 sections, 6 sous-annexes, 28 diagrammes Mermaid. Socle documentaire arrêté à juin 2026.

**Statut :** livrable — fixé le 15 septembre 2026 par la décision [D-18](../../2%20-%20Compendium/PRD/PRD.md#d-18) ; dépôt rouvert le
même jour par [D-17](../../2%20-%20Compendium/PRD/PRD.md#d-17). Aucun relecteur humain nommé.

| Chapitre | Objet |
|---|---|
| 1 — Interopérabilité des SI | fondements et intégration d'entreprise |
| 2 — IA agentique | ingénierie des systèmes agentiques fondés sur les LLM |
| 3 — Interopérabilité agentique | MCP, A2A, ANP ; découverte, sémantique, identité, sécurité |
| 4 — … en entreprise | déploiement à l'échelle : héritage applicatif, identités non humaines, gouvernance |
| 5 — … dans le domaine financier | cinq sous-domaines sous le patron de l'autonomie graduée |
| 6 — Blueprint ArchiMate | formalisation des chapitres 1 à 5 en architecture d'entreprise |
| 7 — Horizon 2027-2032 | chapitre prospectif : programmé, projeté, spéculatif |
| Annexe B | architecture détaillée de solution |

**Par où entrer :** [`Chapitres/TOC.md`](Chapitres/TOC.md), la table des matières commentée ; chaque chapitre suppose les
précédents. Les sources des chapitres et leurs sept bibliographies sont sous [`Chapitres/`](Chapitres/).

**Refaire :** depuis ce dossier, `bash build/build-pdf.sh` recompose `Monographie.pdf` depuis `Monographie.md`, l'Abstract anglais tenu par `build/inject-pagination.py` — Pandoc, Typst, `mermaid-cli`
pour les diagrammes, polices du poste d'auteur. `python Python/check-vol1.py` oppose la pagination du PDF à la ligne « Lire »
ci-dessus, apparie les notices des bibliographies au corps et vérifie la parité du rendu ; son harnais est
`python Python/check-vol1-mutations.py`.

**Journal :** [`JOURNAL.md`](JOURNAL.md) — retraits de l'article de synthèse et du démonstrateur Borealis-Go, déplacements de la
veille, passes de vérification de juin à septembre 2026, clôture et réouverture. Licence propre au volume : [`LICENSE`](LICENSE),
mêmes termes que celle de la racine.
