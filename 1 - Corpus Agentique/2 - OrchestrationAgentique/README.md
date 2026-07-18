# Volume II — « L'autonomie encadrée »

📖 **Lire en ligne :** <https://agbruneau.github.io/Monographies/1%20-%20Corpus%20Agentique/2%20-%20OrchestrationAgentique/>

> **Où vous êtes.** Ce dossier est le **deuxième des trois volumes** du dépôt
> [*Monographies*](../../README.md). Il **présuppose le volume I**
> ([`1 - InteroperabiliteAgentique/`](../1%20-%20InteroperabiliteAgentique/)) pour la théorie du
> découplage, l'ingénierie des agents LLM et l'anatomie des protocoles : le volume I illustre
> mondialement ce que celui-ci instruit au grain du droit canadien.

**Monographie exhaustive** sur l'interopérabilité et l'orchestration agentique en écosystème d'entreprise de services financiers au Canada — protocoles ouverts (MCP, A2A, AP2, AGNTCY), cadre réglementaire canadien (E-23, AMF, ACVM, cadre bancaire) et blueprint d'intégration d'entreprise. État des lieux 2024-2026.

| Champ | Valeur |
|---|---|
| Livrable | millésime **`mono-v1.0`** — publiée le 17 juillet 2026 (⚠ millésime éditorial : l'**étiquette git n'a pas été posée**) |
| Volumétrie | **92 059 mots**, 29 pièces (24 chapitres, avant-propos, annexes A-D) |
| Rendus | `Monographie.pdf` **387 p.** · `Synthese Monographie.pdf` **66 p.** |
| Gel de l'information | 16 juillet 2026 (22 pièces) · 17 juillet 2026 (7 pièces) |
| Socle factuel | **46 entrées** F-01 à F-48 (F-12 à F-14 non attribués ; F-23b) |
| Conformité | CA-1 à CA-8 |

**Contribution la plus citable — un résultat négatif :** en croisant trois protocoles (MCP, A2A, AP2) et cinq corpus de textes canadiens, **aucun lien documenté par source primaire** — quinze croisements, zéro lien. D'où la thèse : sous exigence réglementaire stricte, le cadre déterministe invoque les agents, jamais l'inverse.

## Par où commencer

- **Lire la monographie** → [`monographie/README.md`](monographie/README.md) : index de lecture ordonné, à commencer par l'[avant-propos](monographie/00-avant-propos.md). Le [chapitre 13](monographie/03-partie-III/ch-13-pont-frames.md) en est le pivot.
- **PDF assemblé** → [`Monographie.pdf`](Monographie.pdf) (les 29 pièces reliées en un volume).
- **Contribuer / reprendre** → [`CLAUDE.md`](CLAUDE.md) : conventions, garde-fous et procédure de reprise.

## Structure du dossier

| Chemin | Contenu |
|---|---|
| `monographie/` | Les 29 pièces, un fichier par chapitre (parties I-VII, annexes `90-annexes/`, registre des gels `99-registre-gel.md`) + son [index de lecture](monographie/README.md) |
| `doc/` | Documents de gouvernance et sources — [`PRD.md`](doc/PRD.md), [`PRDPlan.md`](doc/PRDPlan.md), [`TOC.md`](doc/TOC.md), [`audit.md`](doc/audit.md), et les deux PDF académiques du socle (F-36, F-37) |
| `verification/` | Rapports de revalidation ([16](verification/revalidation-2026-07-16.md), [17](verification/revalidation-2026-07-17.md) juillet 2026) et grille de conformité [CA-1..CA-8](verification/relecture-CA.md) |
| `build/` | Pipeline de rendu PDF (assemblage + Pandoc → Typst) |
| `index.html` | Page de présentation du volume (GitHub Pages) |
| `Monographie.md` / `Monographie.pdf` | Assemblage versionné des 29 pièces et son rendu (387 p.) |
| `Synthese Monographie.md` / `.pdf` | Article de synthèse autonome (12 sections, 19 tableaux, ~26 500 mots ; 66 p.) tiré de la monographie — même pipeline de rendu |

## Gouvernance

Documents par ordre d'autorité — **en cas de conflit, le PRD prime** :

1. [`PRD.md`](doc/PRD.md) — contenu, socle factuel, garde-fous (R-1..R-8), critères d'acceptation ;
2. [`PRDPlan.md`](doc/PRDPlan.md) — plan d'exécution et boucle qualité par chapitre (§4.2) ;
3. [`TOC.md`](doc/TOC.md) — titre, abstract, table des matières commentée.

Toute affirmation factuelle centrale est tracée à une entrée du socle F-xx avec son niveau de preuve — **[A]** vote adversarial 3-0 > **[B]** source primaire extraite > **[C]** repérage à confirmer.

## Régénérer le PDF

Après toute modification des chapitres, **depuis ce dossier** :

```bash
python build/assemble.py            # concatène monographie/ → Monographie.md
bash   build/build-pdf.sh Monographie.md   # → Monographie.pdf (US-letter, gabarit build/fesp.template)
```

⚠ `build/assemble.py` cherche encore `TOC.md` à la racine du volume alors qu'il vit dans `doc/` depuis le 17 juillet 2026 : **l'assemblage échoue en l'état**. Ce reliquat et les autres liens cassés par ce déplacement sont inventoriés dans [`CLAUDE.md`](CLAUDE.md).

## Avertissements

- **Aucun avis juridique ni conseil d'investissement** : l'ouvrage rapporte des textes et en propose des lectures d'architecture qui engagent l'auteur seul.
- **Aucune recommandation de fournisseur** : la Partie VII instancie le blueprint sur le portefeuille d'IBM à titre de cas documenté, pas de verdict comparatif.
- **L'ouvrage se périme par morceaux** : chaque pièce porte sa date de gel ; les échéances de revalidation sont suivies dans [`CLAUDE.md`](CLAUDE.md) et au [chapitre 24](monographie/07-partie-VII/ch-24-lacunes-revalidation.md).
- **Onze lacunes ouvertes** sont exposées plutôt que comblées ([chapitre 21](monographie/06-partie-VI/ch-21-frontiere.md)).
