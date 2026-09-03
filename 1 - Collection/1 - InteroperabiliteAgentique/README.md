# Volume I — Interopérabilité agentique en entreprise dans le domaine des services financiers

📖 **Lire :** [`Monographie.pdf`](Monographie.pdf) (569 p.) dans ce dossier. *(Le volume n'a plus de
page de présentation ni de publication GitHub Pages — voir « Structure du dossier ».)*

> ⚠ **Dépôt clos et final — clôture portée au 1er septembre 2026** — décision d'auteur **D-13**, prise le 8 août 2026
> ([`2 - Compendium/PRD/PRD.md`](../../2%20-%20Compendium/PRD/PRD.md) v0.17 §16). Aucune passe
> n'est plus prévue, sur ce volume ni sur aucun autre du dépôt : ce qui suit décrit un état
> **définitif**. ⚠ *Clore n'est ni terminer ni publier* — rien n'est levé, rien n'est soldé, et
> ce qui restait dû devient un **manque définitif, daté et écrit**.
>
> ⚠ **La date de clôture a porté « 8 août 2026 » jusqu'au 3 septembre 2026, et elle confondait deux choses** : *une décision se date de sa prise, une clôture de l'état qu'elle arrête.* **D-13 reste prise le 8 août 2026** ; **la clôture court du 1er septembre 2026**, dernier jour où une pièce est entrée au dépôt — l'article de `6 - Article/`, commit `da6255b`. ⚠ *La passe d'audit et de fond du 2 septembre 2026 (D-15, D-16) lui est postérieure d'un jour : elle porte sur l'appareil, le plan et le domaine de livraison du Vol. IV, et **aucune pièce n'y entre ni n'en sort**.* Motif complet au **PRD §16.5**.

> **Où vous êtes.** Ce dossier est le **premier des trois volumes** du corpus, dans le dépôt
> [*Agentique*](../../README.md) — le cadre général et mondial, dont le volume II tire le cas
> canadien réglementé et le volume III le verrou identitaire ; un quatrième livrable, le compendium
> (Vol. IV), projette de les absorber. Pour l'ordre de lecture, les renvois entre volumes et la
> veille technologique qui les recoupe, commencer par le [README du dépôt](../../README.md).

Monographie de science et génie informatique, rédigée en **français canadien**. L'ouvrage construit, **en spirale du général au spécifique**, une lecture unifiée de l'interopérabilité à l'ère des agents d'IA, pour un **double public** : recherche (modèles, formalismes, état de l'art) et praticien-architecte (normes, protocoles, mises en œuvre). Invariant transversal : *découplage, contrat, évolution*. Socle documentaire arrêté à **juin 2026**.

**Auteur :** André-Guy Bruneau, M. Sc. IT — Juin 2026

Le volume réunit **deux livrables**, rendus dans un même PDF : la monographie (7 chapitres) et l'**architecture détaillée de solution** (Annexe B). *(Le démonstrateur de code qui les accompagnait a été retiré du dépôt le 25 juillet 2026 — voir plus bas.)*

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

## Article de synthèse — retiré du dossier

L'article de synthèse autonome (12 sections, 69 p.) **ne fait plus partie de ce dossier** :
`Synthese Monographie.md` et son PDF ont été retirés le 22 juillet 2026. La monographie et son
Annexe B restent les seuls livrables rédigés du volume.

⚠ Les volumes aval qui citaient le Vol. I **contre la numérotation de la synthèse** (renvois §10,
§11.5 et tableau 15 — cf. [`Chapitres/TOC.md`](Chapitres/TOC.md), §Filiation) n'ont plus de cible
dans le dépôt ; les renvois §7.x, eux, résolvent contre `Monographie.md` et restent valides.

## Veille technologique — déplacée hors de ce dossier

La veille n'est **plus un livrable de ce dossier**. Elle vit désormais sous
[`4 - Veille/`](../../4%20-%20Veille/)
([`Veille Technologique.md`](../../4%20-%20Veille/Veille%20Technologique.md)) — ⚠ *à la
racine du dépôt du détachement jusqu'au 15 août 2026, puis sous `4 - Revue et Veille/` le même jour,
**dossier renommé `4 - Veille/` dans la journée** (commit `71d5388`)* —, recoupe les quatre volumes et porte sa
propre édition — **édition du 15 août 2026 (faits gelés à cette date), 144 p., 342 références**, dont deux (§4.12 et §8.4)
citent explicitement ce volume et le volume II, et dont la section 13 rend compte des quatre volumes. Les mentions « 7 juillet 2026, 48 p., 116 références »
qui figuraient ici décrivaient une édition antérieure, comme les « 100 p., 303 références » de l'édition
du 8 août 2026 que ce paragraphe a portées jusqu'au 17 août 2026.

## Démonstrateur Borealis (code) — retiré du dépôt

Un **démonstrateur Go** exécutable — `Borealis-Go/` — matérialisait l'Annexe B (surtout le ch. 6) :
**5 agents A2A** et **4 serveurs MCP** orchestrant une **pré-qualification de crédit** (jamais un
octroi ferme), au calibre d'un projet-étalon d'ingénierie interne (couverture déclarée 96,2 %,
tests golden immuables, **12 ADR**, gate local). Il a été **retiré du dépôt le 25 juillet 2026**
(commit `60f57f6`) et ne se lit plus que dans l'historique git.

⚠ C'est lui qui fournissait la **§4.12 de la veille** (référence [217]) : la citation reste exacte,
elle cesse d'être vérifiable sur l'arbre courant. La veille est publiée et **n'est pas corrigée
après coup** ; le Vol. III, qui le cite lui aussi, relève de sa propre charge éditoriale.

## Structure du dossier

```
README.md                                  ← ce fichier (présentation du volume)
Chapitres/
  Chapitre N - {Sujet}.md                  chapitre rédigé (7)
  Chapitre N - Bibliographie - {Sujet}.md  références vérifiées (7)
  Annexe B - Architecture de Solutions.md  ADS (épine IBM) — corps de l'Annexe B
  TOC.md                                   table des matières commentée (v1.0, rétro-documentation)
Monographie.md / .pdf                      assemblage : 7 chapitres + liminaires + Annexes A et B (569 p.)
build/                                     pipeline de rendu PDF (Mermaid → Pandoc → Typst)
                                           build-pdf.sh, fesp.template, inject-pagination.py
LICENSE                                    seul `LICENSE` du dépôt — il ne vaut que pour ce volume
.gitignore
```

⚠ **Ni `index.html` ni publication GitHub Pages.** La page de présentation a été retirée le
22 juillet 2026. Les adresses `https://agbruneau.github.io/Monographies/…` annoncées auparavant
étaient fausses de toute façon : le dépôt s'appelle [`Agentique`](https://github.com/agbruneau/Agentique).

## Construire les PDF

Pipeline FESP, à lancer **depuis ce dossier** :

```bash
bash build/build-pdf.sh                              # Monographie.pdf (défaut)
```

Le script prend un `.md` source en argument (défaut `Monographie.md`, désormais la seule source du dossier). Il pré-rend chaque bloc ` ```mermaid ` (les 28 diagrammes de l'Annexe B) en SVG avant Pandoc→Typst ; si `mermaid-cli` est absent, les diagrammes restent en bloc de code (mode dégradé, sans échec).

**Prérequis :** Pandoc ≥ 3.1.7, Typst ≥ 0.12, `python3` + `pypdf`, polices Liberation Sans et DejaVu Sans. Pour le rendu des diagrammes : Node ≥ 18 + [`@mermaid-js/mermaid-cli`](https://github.com/mermaid-js/mermaid-cli) (`mmdc`) et un Chromium. Le script exporte lui-même `PYTHONUTF8=1` (nécessaire sous Windows).

La chaîne de la veille (depuis [`4 - Veille/`](../../4%20-%20Veille/) — *la racine du dépôt jusqu'au 15 août 2026*) et celle du volume II sont **distinctes** de celle-ci : voir le [README du dépôt](../../README.md).

## État

**Rédaction terminée.** Les sept chapitres sont rédigés et assemblés ; l'ADS, intégrée en Annexe B, est rendue dans `Monographie.pdf` (569 p., vérifié le 22 juillet 2026, re-mesuré le 29 juillet et inchangé). ⚠ **Il n'y a plus de travail courant** : la finalisation qu'annonçait ce paragraphe — corrections, vérification adverse des citations, régénération du PDF — **ne sera pas conduite**, le dépôt étant clos depuis le 8 août 2026 (D-13, bandeau en tête). *Ce qui restait à faire devient un manque daté, non une conformité.*

**Vérifié par passes adverses successives :**

- **2026-06-24 → 06-30** — double puis triple passe de vérification adverse du contenu et des sept bibliographies (dates, versions, statuts GA/*preview*) ; ajout du *blueprint* d'ouverture de l'Annexe B (§0.1-0.2) ; corrections propagées dans le corps, `Monographie.md` et l'article de synthèse.
- **2026-07** — cycle de révision (vérification et correctifs, PDF régénérés) ; rédaction de la **veille technologique**, depuis détachée de ce dossier et portée à la racine du dépôt *(⚠ puis sous `4 - Revue et Veille/` le 15 août 2026, dossier renommé **`4 - Veille/`** le jour même)*.
- **2026-07-14** — vérification intégrale de l'**article de synthèse** (bibliographie portée à 211 entrées, terminologie harmonisée ; article depuis retiré du dossier) puis de la **monographie** : 3 054 renvois vérifiés (aucun brisé), bilans des sept bibliographies recomptés, fidélité source ↔ PDF contrôlée. Correctifs : terminologie et typographie du corps, **143 identifiants stables ajoutés** aux bibliographies des ch. 1, 3 et 4 (URL de source primaire vérifiées sur le web), entrée ISO/IEC 27001:2022 créée. PDF régénérés (**569 p.**).
- **2026-07-18** — `Chapitres/TOC.md` v1.0 : rétro-documentation du volume achevé (thèses, sections et décomptes relevés sur le texte livré, non projetés).
- **2026-07-22** — retrait de l'article de synthèse et de la page `index.html` ; `README.md` resynchronisé sur l'arborescence réelle (569 p. et 28 diagrammes re-mesurés, 12 ADR).
- **2026-07-25** — **retrait du démonstrateur `Borealis-Go/`** et renommage du dossier parent (`1 - Corpus Agentique/` → `1 - Corpus/`), commit `60f57f6` ; `README.md` resynchronisé. Décomptes re-mesurés sur pièce et **inchangés** : `Monographie.pdf` **569 p.**, **28 diagrammes** (motif ancré `grep -c '^```mermaid'`).
- **2026-07-29** — **passe de dépôt final du dépôt** : `README.md` relu, décomptes re-mesurés sur pièce et **inchangés** — `Monographie.pdf` **569 p.** (`pypdf`), **28 diagrammes** (motif ancré). Deux mises à jour de renvoi seulement : le Vol. IV cesse d'être décrit comme un « cadrage » — il porte **cinquante chapitres rédigés hors portes** et il est **arrêté en révision finale, non publiable** depuis le 29 juillet 2026 —, et le Vol. III porte désormais son propre `README.md`. ⚠ **Rien de ce volume n'est touché** : ni chapitre, ni bibliographie, ni PDF.

Les ressources marquées ⚠ (*preview*, specs versionnées, acquisitions annoncées) restent à re-confirmer à la date exacte de citation avant toute diffusion formelle.
