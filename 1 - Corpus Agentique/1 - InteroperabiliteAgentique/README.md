# Volume I — Interopérabilité agentique en entreprise dans le domaine des services financiers

📖 **Lire en ligne :** <https://agbruneau.github.io/Monographies/1%20-%20Corpus%20Agentique/1%20-%20InteroperabiliteAgentique/>

> **Où vous êtes.** Ce dossier est le **premier des trois volumes** du dépôt
> [*Monographies*](../../README.md) — le cadre général et mondial, dont le volume II tire le cas
> canadien réglementé et le volume III le verrou identitaire. Pour l'ordre de lecture, les renvois
> entre volumes et la veille technologique qui les recoupe, commencer par le
> [README du dépôt](../../README.md).

Monographie de science et génie informatique, rédigée en **français canadien**. L'ouvrage construit, **en spirale du général au spécifique**, une lecture unifiée de l'interopérabilité à l'ère des agents d'IA, pour un **double public** : recherche (modèles, formalismes, état de l'art) et praticien-architecte (normes, protocoles, mises en œuvre). Invariant transversal : *découplage, contrat, évolution*. Socle documentaire arrêté à **juin 2026**.

**Auteur :** André-Guy Bruneau, M. Sc. IT — Juin 2026

Le volume réunit **trois livrables rédigés** — la monographie (7 chapitres), l'**architecture détaillée de solution** (Annexe B) et un **article de synthèse** autonome — **accompagnés d'un démonstrateur de code** ([`Borealis-Go/`](Borealis-Go/)). Les deux PDF sont publiés sur GitHub Pages.

## Les sept chapitres

Chaque chapitre suppose les précédents.

| # | Chapitre | Objet |
|---|----------|-------|
| 1 | Interopérabilité des SI | Fondements et intégration d'entreprise |
| 2 | IA agentique | Ingénierie des systèmes agentiques fondés sur les LLM |
| 3 | Interopérabilité agentique | Convergence : MCP, A2A, ANP ; découverte, sémantique, identité, sécurité |
| 4 | … en entreprise | Déploiement à l'échelle (héritage applicatif, identités non humaines, gouvernance) |
| 5 | … dans le domaine financier | Cinq sous-domaines, sous le patron « autonomie graduée sous contrôle de finalité » |
| 6 | Blueprint ArchiMate | Formalisation des ch. 1-5 en architecture d'entreprise |
| 7 | Horizon 2027-2032 | Chapitre prospectif (*capstone*) : PROGRAMMÉ / PROJETÉ / SPÉCULATIF |

## Architecture détaillée de solution (ADS) — Annexe B

L'**Annexe B** de la monographie ([`Chapitres/Annexe B - Architecture de Solutions.md`](Chapitres/Annexe%20B%20-%20Architecture%20de%20Solutions.md)) applique la monographie (surtout ch. 5-6) à une entreprise fictive — la *Coopérative financière Boréalis* — sous forme d'**architecture détaillée de solution prête au déploiement**, consolidée sur la pile **IBM** (watsonx Orchestrate/governance, API Connect + DataPower, Confluent, MQ, z/OS Connect, Sovereign Core).

Le document (~20 000 mots ; **18 sections, 6 sous-annexes, 28 diagrammes Mermaid**) couvre : vues *blueprint* d'ouverture (§0.1, figures A-B ; §0.2, 10 vues ArchiMate, figures C-L), architecture logique et physique, contrats d'interface, sécurité, NFR/SLO, modèle opérationnel, stratégie de test, plan de déploiement par plateaux, ADR et registre des risques. Les diagrammes sont rendus nativement sur GitHub ; le tout est intégré au PDF de la monographie (`Monographie.pdf`).

## Article de synthèse

Une **revue de synthèse** autonome (69 p.) condense la monographie au format académique : douze sections (introduction, méthode, fondements, ingénierie agentique, couche d'interopérabilité, entreprise, finance, ArchiMate, horizon 2027-2032, validation par l'ADS, discussion, conclusion) suivies d'une bibliographie thématique propre. Source [`Synthese Monographie.md`](Synthese%20Monographie.md) ; rendu `Synthese Monographie.pdf` (même pipeline FESP, sans diagramme). Publiée sur GitHub Pages.

## Veille technologique — déplacée à la racine du dépôt

La veille n'est **plus un livrable de ce dossier**. Elle vit désormais à la racine du dépôt
([`Veille Technologique.md`](../../Veille%20Technologique.md)), recoupe les trois volumes et porte sa
propre édition — **18 juillet 2026, 107 p., 218 références**, dont deux (§4.12 et §8.4) citent
explicitement ce volume et le volume II. Les mentions « 7 juillet 2026, 48 p., 116 références »
qui figuraient ici décrivaient une édition antérieure.

## Démonstrateur Borealis (code)

Un **démonstrateur Go** exécutable — [`Borealis-Go/`](Borealis-Go/) — matérialise l'Annexe B (surtout le ch. 6) : **5 agents A2A** et **4 serveurs MCP** orchestrant une **pré-qualification de crédit** (jamais un octroi ferme), au calibre d'un projet-étalon d'ingénierie interne (couverture ≥ 90 %, tests golden immuables, **12 ADR**, gate local). Livrable de nature distincte, régi par son propre [`Borealis-Go/CLAUDE.md`](Borealis-Go/CLAUDE.md) et documenté dans [`Borealis-Go/README.md`](Borealis-Go/README.md). Présentation synthèse : [`Borealis-Go/Présentation Borealis-Go.pdf`](Borealis-Go/Pr%C3%A9sentation%20Borealis-Go.pdf). C'est lui qui fournit la §4.12 de la veille.

## Structure du dossier

```
Chapitres/
  Chapitre N - {Sujet}.md                  chapitre rédigé (7)
  Chapitre N - Bibliographie - {Sujet}.md  références vérifiées (7)
  Annexe B - Architecture de Solutions.md  ADS (épine IBM) — corps de l'Annexe B
Monographie.md / .pdf                      assemblage : 7 chapitres + liminaires + Annexes A et B (569 p.)
Synthese Monographie.md / .pdf             article de synthèse (revue condensée, 69 p.)
index.html                                 page de présentation (landing page, GitHub Pages)
build/                                     pipeline de rendu PDF (Mermaid → Pandoc → Typst)
Borealis-Go/                               démonstrateur Go (MCP + A2A) — livrable de code distinct
```

## Construire les PDF

Pipeline FESP, à lancer **depuis ce dossier** :

```bash
bash build/build-pdf.sh                              # Monographie.pdf (défaut)
bash build/build-pdf.sh "Synthese Monographie.md"    # Synthese Monographie.pdf (article de synthèse)
```

Le script prend un `.md` source en argument (défaut `Monographie.md`). Il pré-rend chaque bloc ` ```mermaid ` (les 28 diagrammes de l'Annexe B) en SVG avant Pandoc→Typst ; si `mermaid-cli` est absent, les diagrammes restent en bloc de code (mode dégradé, sans échec).

**Prérequis :** Pandoc ≥ 3.1.7, Typst ≥ 0.12, `python3` + `pypdf`, polices Liberation Sans et DejaVu Sans. Pour le rendu des diagrammes : Node ≥ 18 + [`@mermaid-js/mermaid-cli`](https://github.com/mermaid-js/mermaid-cli) (`mmdc`) et un Chromium. Le script exporte lui-même `PYTHONUTF8=1` (nécessaire sous Windows).

La chaîne de la veille (racine) et celle du volume II sont **distinctes** de celle-ci : voir le [README du dépôt](../../README.md).

## État

**Rédaction terminée.** Les sept chapitres sont rédigés et assemblés ; l'ADS, intégrée en Annexe B, est rendue dans `Monographie.pdf` ; la synthèse est publiée. Le travail courant est la finalisation — corrections, vérification adverse des citations, régénération des PDF.

**Vérifié par passes adverses successives :**

- **2026-06-24 → 06-30** — double puis triple passe de vérification adverse du contenu et des sept bibliographies (dates, versions, statuts GA/*preview*) ; ajout du *blueprint* d'ouverture de l'Annexe B (§0.1-0.2) ; corrections propagées dans le corps, `Monographie.md` et l'article de synthèse.
- **2026-07** — cycle de révision (audit et correctifs, PDF régénérés) ; rédaction de la **veille technologique**, depuis détachée de ce dossier et portée à la racine du dépôt.
- **2026-07-14** — audit intégral de l'**article de synthèse** (bibliographie portée à 211 entrées, terminologie harmonisée) puis de la **monographie** : 3 054 renvois vérifiés (aucun brisé), bilans des sept bibliographies recomptés, fidélité source ↔ PDF contrôlée. Correctifs : terminologie et typographie du corps, **143 identifiants stables ajoutés** aux bibliographies des ch. 1, 3 et 4 (URL de source primaire vérifiées sur le web), entrée ISO/IEC 27001:2022 créée. PDF régénérés (**569 p.**).

Les ressources marquées ⚠ (*preview*, specs versionnées, acquisitions annoncées) restent à re-confirmer à la date exacte de citation avant toute diffusion formelle.

Conventions de rédaction et règles de travail détaillées : voir [`CLAUDE.md`](CLAUDE.md).
