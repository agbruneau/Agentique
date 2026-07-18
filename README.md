# Interopérabilité, orchestration et entreprise agentiques — un triptyque, sa veille et sa somme

Travaux d'André-Guy Bruneau sur les agents d'IA en écosystème d'entreprise, et plus
particulièrement en services financiers. Le dépôt réunit **trois monographies** conçues en
progression — les protocoles, puis les cadres réglementaires, puis l'organisation qui doit les
faire tenir ensemble —, **une veille technologique autonome** qui les traverse et les tient à jour,
et **un compendium** qui projette de les refondre en un seul ouvrage.

> **Où entrer.** Le lecteur pressé lit la [veille technologique](Veille%20Technologique.md) : c'est
> l'état de l'art le plus récent (18 juillet 2026), et le seul document publié qui cite les volumes
> du dépôt. Le lecteur méthodique suit l'ordre des volumes, du général au spécifique. Le compendium
> n'est encore qu'un plan : il ne se lit pas.

## Les cinq livrables

Les trois volumes vivent sous [`1 - Corpus Agentique/`](1%20-%20Corpus%20Agentique/) ; la veille est
à la racine ; le compendium a son propre dossier.

| | **Veille technologique** | **Vol. I — Interopérabilité** | **Vol. II — Orchestration** | **Vol. III — Entreprise** | **Vol. IV — Compendium** |
|---|---|---|---|---|---|
| **Dossier** | racine du dépôt | [`1 - Corpus Agentique/1 - InteroperabiliteAgentique/`](1%20-%20Corpus%20Agentique/1%20-%20InteroperabiliteAgentique/) | [`1 - Corpus Agentique/2 - OrchestrationAgentique/`](1%20-%20Corpus%20Agentique/2%20-%20OrchestrationAgentique/) | [`1 - Corpus Agentique/3 - EntrepriseAgentique/`](1%20-%20Corpus%20Agentique/3%20-%20EntrepriseAgentique/) | [`2 - Compendium Agentique/`](2%20-%20Compendium%20Agentique/) |
| **Titre** | Interopérabilité agentique et orchestration des processus d'affaires en entreprise | Interopérabilité agentique en entreprise dans le domaine des services financiers | L'autonomie encadrée | L'entreprise agentique — la fabrique de confiance | La somme agentique |
| **Rôle** | État de l'art vérifié, mis à jour par éditions | Cadre général, mondial et théorique | Cas canadien réglementé, instruit au grain du droit | Le verrou commun : identité, maillage, exploitation | Omnibus terminal : absorbe et remplace les trois volumes |
| **Portée** | Mondiale | Mondiale (UE / É.-U. / R.-U. / Asie) | Canada-Québec (E-23, AMF, Loi 25, ACVM, Lynx/RTR) | Organisation et cycle de vie (NHI, *agent mesh*, AgentOps) | Les trois portées réunies (2024-2032) |
| **Thèse** | « L'agent d'entreprise fiable de 2026 est un agent *enveloppé* » | « Autonomie graduée sous contrôle de finalité » | « Autonomie encadrée » (*framed autonomy*) | « La confiance ne se décrète pas, elle se fabrique » | Les trois thèses sont trois coupes d'un même objet |
| **Méthode** | Revue structurée, vérification adverse à trois votants | Formalisme d'ingénierie (ArchiMate 4, ADS « Boréalis ») | Socle factuel F-01…F-48, niveaux de preuve [A]/[B]/[C] | Reconduction des deux méthodes (annoncée) | Méthode unifiée, gel unique (annoncée) |
| **Gel de l'information** | 18 juillet 2026 | Juin 2026 | 16-17 juillet 2026 | — (proposition) | — (à fixer au lancement) |
| **État** | Publiée (107 p., 218 références) | Rédaction terminée (569 p. + synthèse 69 p.) | Publiée, millésime `mono-v1.0` (387 p. + synthèse 66 p.) | **Cadrage seul** — table des matières v0.4 | **Cadrage seul** — table des matières v0.2 |

## Veille technologique — le document transversal

[`Veille Technologique.md`](Veille%20Technologique.md) → `Veille Technologique.pdf` (**107 p.**,
13 sections numérotées, **218 références**). Revue vérifiée où chaque énoncé factuel est adossé à
une source primaire consultée et soumis à contradiction — vérificateurs indépendants chargés de
*réfuter*, contre-vérification directe sinon. Elle couvre les trois protocoles structurants (MCP,
A2A, ANP), leur gouvernance, l'adoption documentée, la sécurité, et **six couches** que la pile
protocolaire laisse implicites : événementielle, de contrôle, transactionnelle, sémantique, de
confiance et d'orchestration des processus d'affaires.

**Elle est aussi le point d'articulation du corpus.** L'édition du 18 juillet 2026 intègre les
**deux** corpus compagnons rédigés du dépôt — le Vol. III, non écrit, n'y figure pas — et en fait
des sections à part entière :

- **§4.12 — « De la spécification au code »** confronte le corpus documentaire à l'épreuve d'une
  implémentation de référence : le démonstrateur `Borealis-Go` du Vol. I (référence [217]) ;
- **§8.4 — « L'instruction sectorielle canadienne »** reprend le croisement systématique entre
  trajectoire protocolaire et textes canadiens établi par le Vol. II (référence [218]).

L'auto-citation est assumée et divulguée ; ses limites (circularité possible, implémentation
unique, chiffres institutionnels auto-déclarés) sont exposées en section 10 de la veille.

*Historique des éditions : 2, 4, 7, 12, 13, 15 puis 18 juillet 2026. Chaque édition ajoute une
couche ou un corpus et revérifie les faits périssables.*

## Vol. I — Interopérabilité agentique

Monographie de science et génie informatique, construite **en spirale du général au spécifique**,
pour un double public (recherche et praticien-architecte). Invariant transversal : *découplage,
contrat, évolution*.

- **Monographie** (`Monographie.pdf`, **569 p.**) — 7 chapitres : interopérabilité des SI, IA
  agentique, interopérabilité agentique, en entreprise, dans le domaine financier, blueprint
  ArchiMate, horizon 2027-2032.
- **Architecture détaillée de solution** (Annexe B) — la monographie projetée sur une entreprise
  fictive, la *Coopérative financière Boréalis*, consolidée sur la pile IBM ; 18 sections,
  6 sous-annexes, 28 diagrammes Mermaid, rendus dans le PDF principal.
- **Article de synthèse** (`Synthese Monographie.pdf`, **69 p.**) — la monographie condensée au
  format académique, avec bibliographie propre.
- **Démonstrateur `Borealis-Go/`** — code Go exécutable matérialisant l'ADS : **5 agents A2A** et
  **4 serveurs MCP** orchestrant une pré-qualification de crédit (jamais un octroi ferme), sur les
  SDK officiels des deux protocoles. **12 ADR**, journal d'audit à chaîne de hachage, vérification
  adverse à chaque phase, invariants critiques prouvés par mutation ; couverture déclarée 96,2 %
  au rapport final. C'est ce démonstrateur qui fournit la §4.12 de la veille.

## Vol. II — L'autonomie encadrée

Monographie sur l'interopérabilité et l'orchestration agentique en services financiers canadiens,
publiée sous le millésime `mono-v1.0`. **92 059 mots** en 29 pièces (24 chapitres, avant-propos,
annexes A-D) selon son README ; `Monographie.pdf` **387 p.** ; article de synthèse **66 p.**

⚠ `mono-v1.0` est un **millésime éditorial, pas une étiquette git** : aucune référence de ce nom
n'existe dans le dépôt, ni en local ni sur le distant (vérifié le 18 juillet 2026). Plusieurs
documents de gouvernance du Vol. II l'annoncent pourtant comme posée.

Sa contribution la plus citable est un **résultat négatif** : en croisant trois protocoles
(MCP, A2A, AP2) et cinq corpus de textes canadiens, **aucun lien documenté par source primaire** —
quinze croisements, zéro lien. D'où sa thèse probatoire : sous exigence réglementaire stricte, le
cadre déterministe invoque les agents, jamais l'inverse, parce que le cadre est la seule pièce
dont l'exploitant puisse démontrer la teneur devant un tiers.

Sa méthode est son autre apport : socle factuel de **46 entrées** (F-01 à F-48) cotées par niveau
de preuve — **[A]** vote adversarial 3-0 > **[B]** source primaire extraite > **[C]** repérage —,
huit garde-fous de formulation, onze lacunes exposées plutôt que comblées.

## Vol. III — L'entreprise agentique

**Au stade du cadrage seul.** Le dossier ne contient à ce jour qu'une table des matières commentée
([`TOC.md`](1%20-%20Corpus%20Agentique/3%20-%20EntrepriseAgentique/TOC.md), v0.4 du 18 juillet 2026,
statut *proposition*) : aucun chapitre rédigé, **aucun socle factuel constitué** — les « socles
candidats » y sont des repérages [C] à instruire. Cadrage annoncé : 28 chapitres en 9 parties,
≈ 100 000 mots, autour de trois capacités — *émettre* une identité opposable (le passeport
d'agent), l'*appliquer* au maillage d'agents, l'*exploiter* dans la durée (AgentOps) — sous
l'horloge post-quantique.

Le volume naît des lacunes des deux précédents : identité non humaine et délégation multi-saut
(verrou identifié au Vol. I), mécanique des attaques et valeur cryptographique des Agent Cards
(questions ouvertes du Vol. II).

## Vol. IV — La somme agentique (compendium)

**Au stade du cadrage seul, lui aussi.** Le dossier
[`2 - Compendium Agentique/`](2%20-%20Compendium%20Agentique/) ne contient qu'une table des matières
commentée ([`TOC.md`](2%20-%20Compendium%20Agentique/TOC.md), v0.2 du 18 juillet 2026) —
**aucun contenu neuf rédigé : c'est un plan de refonte, pas une nouvelle thèse.**

Sa nature le distingue des trois autres : ce n'est ni un quatrième panneau ni un méta-index, mais
un **omnibus qui absorbe les Vol. I, II et III** en un seul ouvrage réordonné et dédoublonné, à
numérotation continue — 54 chapitres en 12 livres, ≈ 260 000 à 320 000 mots projetés. Une fois
rédigé, il se substitue à la lecture des trois volumes ; **jusque-là, les trois volumes sources
font foi.** Ses décisions structurantes : numérotation continue, déduplication tracée sous chaque
entrée, divergences héritées tranchées (et non plus signalées), méthode et gel unifiés, couverture
totale tracée — chaque section des sources est affectée à un chapitre d'arrivée ou marquée « coupe
assumée ».

⚠ Sa volumétrie est explicitement **indicative et non normative** : elle agrège des décomptes pris
par des commandes différentes, non comparables entre eux. La première tâche de sa rédaction est de
re-mesurer les trois corpus par une commande de référence unique.

## Ordre de lecture et renvois

**Vol. I → Vol. II → Vol. III**, la veille servant d'entrée rapide ou de mise à jour ; le Vol. IV
les remplacera tous les trois une fois écrit.

- **Vol. II présuppose Vol. I** pour la théorie du découplage, l'ingénierie des agents LLM,
  l'anatomie des protocoles, la sécurité de la couche agentique et la cryptographie post-quantique.
- **Vol. I illustre mondialement** ce que **Vol. II instruit au grain du droit canadien**.
- **Vol. III prolonge les deux** sur leur verrou commun, l'identité et son exploitation.
- **La veille recoupe les trois**, mais n'en cite que **deux** : §4.12 pour le Vol. I (réf. [217])
  et §8.4 pour le Vol. II (réf. [218]). Le Vol. III n'y figure sous aucune forme — la veille parle
  d'ailleurs de « deux corpus compagnons », pas de trois.
- **Vol. IV les absorbe** : ses renvois inter-volumes deviennent des renvois internes.
- Un lecteur pressé côté canadien peut entrer directement par le **chapitre 13** du Vol. II
  (« le pont : des contraintes réglementaires aux frames déterministes »), son pivot.

## Divergences factuelles entre volumes

Deux faits datés divergent d'un corpus à l'autre. Ils sont **signalés, non arbitrés** — la veille
les expose en §8.4, et le lecteur doit les trancher à sa date de citation :

| Objet | Vol. II (gel 16-17 juill.) | Veille (18 juill.) |
|---|---|---|
| Ligne directrice IA de l'AMF — version finale | 30 mars 2026, avec dette de vérification déclarée (`lautorite.qc.ca` renvoie 403 aux outils) | 7 avril 2026 |
| Gouvernance d'AP2 | aucun transfert documenté au socle | don à la FIDO Alliance, 28 avril 2026 |

L'entrée en vigueur du 1er mai 2027 est, elle, concordante entre les corpus. La divergence tient à
une frontière de socle plus qu'à un désaccord : deux corpus vérifiés de bonne foi peuvent diverger
sur un fait daté selon leurs périmètres de sources — argument pour le millésimage systématique.

⚠ **Le cadrage du Vol. IV tranche ces deux divergences en faveur du Vol. II** — ligne directrice
AMF finale au 30 mars 2026 (ch. 31), aucun transfert de gouvernance d'AP2 documenté (ch. 10) —
donc *contre* les lectures de la veille, pourtant postérieures de deux jours. L'arbitrage est
consigné à son Annexe C. Tant que le compendium n'est pas rédigé, **cet arbitrage n'a pas
d'autorité** : les volumes sources font foi et la divergence reste ouverte.

> ⚠ Le fichier `commun/faits-partages.md`, évoqué par le cadrage du Vol. III comme source unique
> de vérité pour les faits partagés, **n'existe pas encore** (marqué « à créer » dans sa TOC).
> En son absence, chaque volume porte ses propres faits datés.

## Structure du dépôt

```
.
├── README.md                              ← ce fichier (avant-propos croisé)
├── CLAUDE.md                              ← conventions du dépôt + conventions de la veille
├── Veille Technologique.md / .pdf         ← veille autonome, 18 juillet 2026 (107 p., 218 réf.)
├── 1 - Corpus Agentique/                  ← le triptyque
│   ├── 1 - InteroperabiliteAgentique/       Vol. I
│   │   ├── Chapitres/                         7 chapitres + 7 bibliographies + Annexe B (ADS)
│   │   ├── Monographie.md / .pdf              assemblage (569 p.)
│   │   ├── Synthese Monographie.md / .pdf     article de synthèse (69 p.)
│   │   ├── Borealis-Go/                       démonstrateur Go (MCP + A2A), 12 ADR
│   │   ├── build/                             pipeline FESP (Mermaid → Pandoc → Typst)
│   │   └── index.html                         page de présentation (GitHub Pages)
│   ├── 2 - OrchestrationAgentique/          Vol. II
│   │   ├── monographie/                       29 pièces (parties I-VII, annexes, registre des gels)
│   │   ├── doc/                               PRD, PRDPlan, TOC, audit — gouvernance
│   │   ├── verification/                      revalidations et grille de conformité CA-1..CA-8
│   │   ├── build/                             assemblage + pipeline Pandoc → Typst
│   │   ├── Monographie.md / .pdf              assemblage (387 p.)
│   │   ├── Synthese Monographie.md / .pdf     article de synthèse (66 p.)
│   │   └── index.html                         page de présentation (GitHub Pages)
│   └── 3 - EntrepriseAgentique/             Vol. III
│       └── TOC.md                             table des matières commentée (v0.4) — seul livrable
└── 2 - Compendium Agentique/              ← Vol. IV
    └── TOC.md                               table des matières commentée (v0.2) — seul livrable
```

**Où sont les `CLAUDE.md`.** Un par périmètre, sans recouvrement : la racine porte les conventions
communes et celles de la veille ; chaque volume rédigé porte les siennes ; le démonstrateur Go a
les siennes, qui priment dans son répertoire. Les Vol. III et IV, à l'état de cadrage, n'en ont pas
— leur `TOC.md` tient lieu de spécification.

## Construire les PDF

Trois chaînes distinctes, à lancer depuis le dossier concerné.

**Veille technologique** (racine) — invocation Pandoc directe, gabarit Typst par défaut :

```bash
pandoc "Veille Technologique.md" --pdf-engine=typst --toc -o "Veille Technologique.pdf"
```

**Vol. I** — pipeline FESP, avec pré-rendu des 28 diagrammes Mermaid ; depuis
`1 - Corpus Agentique/1 - InteroperabiliteAgentique/` :

```bash
bash build/build-pdf.sh                              # Monographie.pdf
bash build/build-pdf.sh "Synthese Monographie.md"    # Synthese Monographie.pdf
```

**Vol. II** — assemblage des 29 pièces, puis une **copie** du même pipeline ; depuis
`1 - Corpus Agentique/2 - OrchestrationAgentique/` :

```bash
python build/assemble.py                    # monographie/ → Monographie.md
bash   build/build-pdf.sh Monographie.md    # → Monographie.pdf
```

⚠ `build/assemble.py` cherche encore `TOC.md` à la racine du volume alors qu'il vit dans `doc/` :
**l'assemblage du Vol. II échoue en l'état.** Les deux copies du pipeline évoluent séparément ;
un correctif au Vol. I ne se propage pas au Vol. II.

**Prérequis :** Pandoc ≥ 3.1.7, Typst ≥ 0.12, `python3` + `pypdf` ; polices Liberation Sans et
DejaVu Sans (pipeline FESP), New Computer Modern (veille) ; pour les diagrammes, Node ≥ 18 +
[`@mermaid-js/mermaid-cli`](https://github.com/mermaid-js/mermaid-cli) et un Chromium. Les deux
`build-pdf.sh` exportent eux-mêmes `PYTHONUTF8=1` — inutile de le faire à la main sous Windows.
**Règle permanente :** régénérer et versionner le PDF avec sa source — jamais la source seule.

## Ce qui reste vivant

Le domaine se périme par trimestres, et ces corpus par morceaux. Échéances datées à revalider
avant toute réutilisation ou publication :

| Échéance | Objet | Documents touchés |
|---|---|---|
| 28 juillet 2026 | Révision de la spécification MCP (protocole sans état) | Veille §4.1 ; Vol. I ch. 3 ; Vol. II ch. 1, 2, 7 |
| après le 26 août 2026 | Texte final du règlement du cadre bancaire canadien ; arrêté désignant l'organisme de normalisation | Veille §8.4 ; Vol. II ch. 14, 15, 24 |
| cible T4 2026 | Lancement effectif du RTR — cible précédée de quatre cibles abandonnées depuis 2019 | Veille §8.4 ; Vol. II ch. 15, 24 |
| 2 décembre 2026 | Marquage des contenus générés (règlement européen sur l'IA) | Veille §8.1, §12 |
| **1er mai 2027** | Entrée en vigueur simultanée d'E-23 (BSIF) et de la ligne directrice IA de l'AMF | Veille §4.11.5, §8.4 ; Vol. I ch. 5 à 7 ; Vol. II ch. 9, 11, 20 |
| continue | Trajectoire du projet de loi C-36 | Veille §8.4 ; Vol. II ch. 10 |

## Avertissements

- **Aucun avis juridique ni conseil d'investissement.** Ces ouvrages rapportent des textes et en
  proposent des lectures d'architecture qui engagent leur auteur seul.
- **Aucune recommandation de fournisseur.** Les instanciations sur une pile d'éditeur (IBM
  notamment) sont des cas documentés, pas des verdicts comparatifs.
- **Statuts et chiffres.** Les métriques d'adoption sont, sauf mention contraire, auto-déclarées
  par les acteurs et attribuées comme telles ; les statuts *preview* ne sont jamais présentés comme
  *disponibilité générale* ; les projections d'analystes portent leur millésime.
- **Lacunes exposées, non comblées.** Le Vol. II en recense onze ; la veille, seize questions
  ouvertes. Aucune n'est comblée par une source de moindre qualité.
- **Assistance par agents.** Ces travaux ont été produits avec l'assistance de pipelines de
  recherche multi-agents, selon les méthodes de vérification décrites dans chaque document ; la
  responsabilité éditoriale est celle de l'auteur.

## Notes de maintenance

Les `README.md` et `CLAUDE.md` du dépôt ont été resynchronisés sur l'arborescence réelle
(`1 - Corpus Agentique/`, `2 - Compendium Agentique/`), sur le déplacement de la veille à la racine
et sur les décomptes vérifiés. **Restent ouverts, signalés et non corrigés** — ce sont des fichiers
de code ou de contenu, hors du périmètre de cette passe documentaire :

| Fichier | Reliquat |
|---|---|
| `1 - Corpus Agentique/2 - OrchestrationAgentique/build/assemble.py` | lit `TOC.md` à la racine du volume ; il vit dans `doc/` — **assemblage hors service** |
| `…/2 - OrchestrationAgentique/doc/PRDPlan.md` | renvoi `](CLAUDE.md)` → `../CLAUDE.md` |
| `…/2 - OrchestrationAgentique/doc/audit.md` | renvois `](monographie/…)` → `../monographie/…` |
| `…/2 - OrchestrationAgentique/verification/relecture-CA.md` | renvois `](../PRD.md)`, `](../PRDPlan.md)`, `](../audit.md)` → `../doc/…` |
| `…/1 - InteroperabiliteAgentique/Borealis-Go/docs/ARCHITECTURE.md` | annonce « les 11 ADR » ; le dossier `docs/adr/` en compte 12 (0001-0012) |

Le `monographie/` du Vol. II concentre à lui seul **48 de ces renvois cassés**, sur 28 de ses
29 pièces : voir le tableau et la commande de contrôle du [`CLAUDE.md`](1%20-%20Corpus%20Agentique/2%20-%20OrchestrationAgentique/CLAUDE.md) du volume.

⚠ `…/1 - InteroperabiliteAgentique/index.html` porte une **modification non committée** qui a
résorbé ses propres reliquats (liens vers la veille déplacée, URL de l'ancien dépôt). Elle n'a pas
été produite par cette passe documentaire : **la relire avant de committer.**

⚠ **Publication GitHub Pages non confirmée.** Les deux volumes annoncent une adresse « Lire en
ligne » sous `https://agbruneau.github.io/Monographies/…`, forme déduite du nom du dépôt et des
balises `canonical` des pages. Les sondages effectués depuis cet environnement ont retourné 404,
tant sur ces adresses que sur la racine du site : **à vérifier depuis un navigateur**, et à activer
si Pages ne l'est pas encore pour ce dépôt.

Conventions de rédaction et règles de travail : voir le [`CLAUDE.md`](CLAUDE.md) du dépôt, puis
celui de chaque volume.
