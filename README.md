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
| **Méthode** | Revue structurée, vérification adverse à trois votants | Formalisme d'ingénierie (ArchiMate 4, ADS « Boréalis ») | Socle factuel F-01…F-48, niveaux de preuve [A]/[B]/[C] | Double héritage codifié : entrées du Vol. II à niveau conservé, du Vol. I en [C] | Méthode unifiée, gel unique (annoncée) |
| **Gel de l'information** | 18 juillet 2026 | Juin 2026 | 16-17 juillet 2026 | — (hérite de deux gels : juin et 16-17 juillet 2026) | — (à fixer au lancement) |
| **État** | Publiée (140 p., 244 références) | Rédaction terminée (569 p. + synthèse 69 p.) | Publiée, millésime `mono-v1.0` (387 p. + synthèse 66 p.) | **Cadrage seul** — gouvernance complète (PRD v0.1, TOC v0.4, PRDPlan v0.1), 0 chapitre | **Cadrage seul** — table des matières v0.2 |

## Veille technologique — le document transversal

[`Veille Technologique.md`](Veille%20Technologique.md) → `Veille Technologique.pdf` (**140 p.**,
14 sections numérotées, **244 références**, 14 tableaux). Revue vérifiée où chaque énoncé factuel
est adossé à une source primaire consultée et soumis à contradiction — vérificateurs indépendants
chargés de *réfuter*, contre-vérification directe sinon. Elle couvre les trois protocoles
structurants (MCP, A2A, ANP), leur gouvernance, l'adoption documentée, la sécurité, et **sept
couches** que la pile protocolaire laisse implicites : événementielle, de contrôle,
transactionnelle, sémantique, de confiance, d'orchestration des processus d'affaires et —
depuis l'édition intégrale — d'**exploitation** (observabilité agentique, évaluation continue,
révocation).

**Elle est aussi le point d'articulation du corpus.** L'**édition intégrale du 18 juillet 2026**
rend compte des **quatre** volumes, dans une section 13 qui leur est consacrée — mais à deux
régimes strictement distincts, et c'est l'écart qui compte :

- les **Vol. I et II sont rédigés** et fournissent des faits — **§4.12 — « De la spécification au
  code »** confronte le corpus documentaire à l'épreuve du démonstrateur `Borealis-Go`
  (référence [217]) ; **§8.4 — « L'instruction sectorielle canadienne »** reprend le croisement
  systématique entre trajectoire protocolaire et textes canadiens (référence [218]) ;
- les **Vol. III et IV sont des cadrages** — zéro chapitre, zéro entrée de socle propre — et ne
  fournissent **aucun fait** (références [219] et [220], qui portent la réserve en toutes lettres).
  Ils prêtent des *instruments* : la grille des cinq questions du Vol. III organise les §7.6 à 7.10,
  les décisions de fusion du Vol. IV servent de contrôle de couverture. Traiter un plan comme un
  corpus serait la faute que ces deux cadrages prennent eux-mêmes pour objet.

L'échange est bidirectionnel : la veille rend au corpus deux corrections de datation, referme une
lacune que le Vol. II déclarait ouverte (les dépôts ACP d'AGNTCY, archivés le 11 avril 2026) — et
**rétracte la certitude d'une de ses propres datations** (voir « Divergences factuelles » plus bas).
L'auto-citation est assumée et divulguée ; ses limites (circularité possible, implémentation
unique, chiffres institutionnels auto-déclarés, deux volumes non rédigés) sont exposées en
section 10 de la veille.

*Historique des éditions : 2, 4, 7, 12, 13, 15, 18 juillet 2026, puis l'édition intégrale du
18 juillet 2026. Chaque édition ajoute une couche ou un corpus et revérifie les faits périssables.*

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

**Au stade du cadrage seul, mais désormais gouverné.** Aucun chapitre n'est rédigé et **aucun socle
factuel propre n'est constitué** — 0 entrée propre, 33 entrées héritées (H-01 à H-33), 15 lots
d'instruction ouverts, 0 clos. Cadrage annoncé : 28 chapitres en 9 parties, ≈ 100 000 mots, autour
de trois capacités — *émettre* une identité opposable (le passeport d'agent), l'*appliquer* au
maillage d'agents, l'*exploiter* dans la durée (AgentOps) — sous l'horloge post-quantique.

Le dossier porte quatre fichiers, et rien d'autre : trois documents de gouvernance dans `doc/`,
plus un [`CLAUDE.md`](1%20-%20Corpus%20Agentique/3%20-%20EntrepriseAgentique/CLAUDE.md) à l'agent
qui édite. Par ordre d'autorité :

1. [`doc/PRD.md`](1%20-%20Corpus%20Agentique/3%20-%20EntrepriseAgentique/doc/PRD.md) **v0.1** —
   contenu, héritage du socle, quatorze garde-fous, critères d'acceptation ; **prime en cas de
   conflit**, y compris sur le TOC ;
2. [`doc/TOC.md`](1%20-%20Corpus%20Agentique/3%20-%20EntrepriseAgentique/doc/TOC.md) **v0.4** du
   18 juillet 2026, statut *proposition* — autorité sur le découpage ;
3. [`doc/PRDPlan.md`](1%20-%20Corpus%20Agentique/3%20-%20EntrepriseAgentique/doc/PRDPlan.md)
   **v0.1** — plan d'exécution (phases P0 à P5).

⚠ **Règle cardinale : aucun chapitre n'est rédigeable aujourd'hui** (PRD §7.0) — aucun ne s'écrit
avant la clôture du lot d'instruction dont il dépend. Deux décisions de cadrage restent à l'auteur
et bloquent la suite ; l'une d'elles, le dépôt d'un corpus d'appui de trois ouvrages annoncés
« déposés » mais **absents du dépôt**, bloque à elle seule sept sections et une annexe entière.

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
- **La veille les cite tous les quatre, à deux régimes distincts.** Les volumes *rédigés*
  fournissent des faits : §4.12 pour le Vol. I (réf. [217]), §8.4 pour le Vol. II (réf. [218]).
  Les volumes de *cadrage* ne fournissent aucun fait et ne prêtent que des instruments d'analyse :
  Vol. III (réf. [219], grille des cinq questions, §7.6 à 7.10), Vol. IV (réf. [220], décisions de
  fusion). Sa section 13 est le siège de ce rendu de compte, et son §13.1 pose la règle : un volume
  sans chapitre rédigé ni socle propre ne porte aucun fait.
- **Vol. IV les absorbe** : ses renvois inter-volumes deviennent des renvois internes.
- Un lecteur pressé côté canadien peut entrer directement par le **chapitre 13** du Vol. II
  (« le pont : des contraintes réglementaires aux frames déterministes »), son pivot.

## Divergences factuelles entre volumes

Deux faits datés divergent d'un corpus à l'autre. Ils sont **signalés, non arbitrés** — la veille
les expose en §8.4, et le lecteur doit les trancher à sa date de citation :

| Objet | Vol. II (gel 16-17 juill.) | Veille (édition intégrale, 18 juill.) | État après revalidation |
|---|---|---|---|
| Ligne directrice IA de l'AMF — version finale | 30 mars 2026, avec **dette de vérification déclarée** (`lautorite.qc.ca` renvoie 403 aux outils) | 7 avril 2026 | **divergence ouverte** — la revalidation du 18 juillet a buté sur le **même 403** (sept tentatives, cinq adresses) ; aucune des deux dates n'est établie sur une source primaire directement consultée |
| Gouvernance d'AP2 | aucun transfert documenté au socle | don à la FIDO Alliance, **28 avril 2026** | **résolue** — source primaire datée, accessible et antérieure au gel du Vol. II ; frontière de socle, non désaccord |

L'entrée en vigueur du 1er mai 2027 est, elle, concordante entre les corpus, et ne l'a jamais cessé.

Les deux cas portent la même leçon sous deux formes. Sur AP2, deux corpus vérifiés de bonne foi
divergent parce que **leurs périmètres de sources diffèrent** — argument pour le millésimage
systématique. Sur l'AMF, ils divergent parce que **la source elle-même est inaccessible aux
outils** : c'est l'accessibilité de la source qui est mesurée, non la rigueur inégale des corpus,
et aucune discipline de veille ne corrige cela. ⚠ **L'édition intégrale de la veille rétracte en
conséquence la certitude de sa propre datation** (§13.6) : sa date du 7 avril repose sur des
sources secondaires, et n'est donc pas mieux étayée que celle du Vol. II.

⚠ **Le cadrage du Vol. IV tranche ces deux divergences en faveur du Vol. II** — ligne directrice
AMF finale au 30 mars 2026 (ch. 31), aucun transfert de gouvernance d'AP2 documenté (ch. 10) —
donc *contre* les lectures de la veille. L'arbitrage est consigné à son Annexe C. Sur AP2 il est
**périmé par une source primaire datée** ; sur l'AMF il n'est **ni confirmé ni infirmé**. Et de
toute manière, tant que le compendium n'est pas rédigé, **cet arbitrage n'a aucune autorité** : les
volumes sources font foi et la divergence reste ouverte — le cadrage le dit lui-même.

> ⚠ Le fichier `commun/faits-partages.md`, évoqué par le cadrage du Vol. III comme source unique
> de vérité pour les faits partagés, **n'existe pas et ne sera pas créé** : son PRD §7.5 a tranché
> de porter lui-même ces divergences. Chaque volume porte donc ses propres faits datés.

## Structure du dépôt

```
.
├── README.md                              ← ce fichier (avant-propos croisé)
├── CLAUDE.md                              ← conventions du dépôt + conventions de la veille
├── Veille Technologique.md / .pdf         ← veille autonome, 18 juillet 2026 (140 p., 244 réf.)
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
│       ├── CLAUDE.md                          conventions du volume
│       └── doc/                               PRD v0.1, TOC v0.4, PRDPlan v0.1 — gouvernance seule
└── 2 - Compendium Agentique/              ← Vol. IV
    └── TOC.md                               table des matières commentée (v0.2) — seul livrable
```

**Où sont les `CLAUDE.md`.** Un par périmètre, sans recouvrement : la racine porte les conventions
communes et celles de la veille ; les Vol. I, II et III portent chacun les siennes ; le
démonstrateur Go a les siennes, qui priment dans son répertoire. Seul le Vol. IV n'en a pas — son
`TOC.md` tient lieu de spécification.

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

Les `README.md` et `CLAUDE.md` de la racine ont été resynchronisés le 18 juillet 2026 sur
l'arborescence réelle, sur l'accession du Vol. III à une gouvernance complète (`CLAUDE.md` +
`doc/`) et sur les décomptes **re-mesurés** — veille 140 p. / 244 réf. / 14 sections, Vol. I
569 p. / 69 p. / 28 diagrammes / 12 ADR, Vol. II 387 p. / 66 p. / 29 pièces / 46 entrées de socle,
tous inchangés.

⚠ Le décompte des diagrammes du Vol. I se mesure avec un motif **ancré** :
`grep -c '^```mermaid'` donne 28. Le motif non ancré en retourne 29 — il attrape une ligne de prose
de la note de production qui cite la balise.

**Restent ouverts, signalés et non corrigés** — ce sont des fichiers de code ou de contenu, hors du
périmètre de cette passe documentaire :

| Fichier | Reliquat |
|---|---|
| `1 - Corpus Agentique/2 - OrchestrationAgentique/build/assemble.py` | lit `TOC.md` à la racine du volume ; il vit dans `doc/` — **assemblage hors service** |
| `…/2 - OrchestrationAgentique/doc/PRDPlan.md` | renvoi `](CLAUDE.md)` → `../CLAUDE.md` |
| `…/2 - OrchestrationAgentique/doc/audit.md` | renvois `](monographie/…)` → `../monographie/…` |
| `…/2 - OrchestrationAgentique/verification/relecture-CA.md` | renvois `](../PRD.md)`, `](../PRDPlan.md)`, `](../audit.md)` → `../doc/…` |
| `…/1 - InteroperabiliteAgentique/Borealis-Go/docs/ARCHITECTURE.md` | ligne 906 : annonce « les 11 ADR » ; le dossier `docs/adr/` en compte 12 (0001-0012, hors gabarit) |
| `…/3 - EntrepriseAgentique/doc/PRDPlan.md` | deux renvois cassés par le déplacement vers `doc/` : `](../../CLAUDE.md)` → `../../../CLAUDE.md`, et `](../../TOC.md)` → `../../doc/TOC.md` |
| `…/2 - OrchestrationAgentique/build/__pycache__/` | bytecode Python (`.pyc`) versionné par mégarde — à retirer du suivi et à ignorer |

Le `monographie/` du Vol. II concentre à lui seul **48 de ces renvois cassés**, sur 28 de ses
29 pièces : voir le tableau et la commande de contrôle du [`CLAUDE.md`](1%20-%20Corpus%20Agentique/2%20-%20OrchestrationAgentique/CLAUDE.md) du volume.

⚠ **Le second renvoi du Vol. III est le plus coûteux du dépôt, et il ne coûte encore rien.** Il vit
dans le *gabarit de pièce* que les 34 pièces à venir recopieront : non corrigé, il reproduit
mécaniquement le gisement du Vol. II. Le corriger aujourd'hui coûte un caractère ; après rédaction,
34 éditions.

⚠ **Publication GitHub Pages : les adresses annoncées sont fausses.** Les deux volumes annoncent
« Lire en ligne » sous `https://agbruneau.github.io/Monographies/…`, et leurs balises `canonical`,
`og:url` et liens « Dépôt GitHub » nomment tous `Monographies`. **Le dépôt s'appelle `Agentique`**
(`github.com/agbruneau/Agentique`) : la base correcte est `https://agbruneau.github.io/Agentique/`.
C'est la cause des 404 relevés, et non un simple défaut d'activation — reste à vérifier, une fois
les URL rectifiées, que Pages est bien activé pour ce dépôt.

Conventions de rédaction et règles de travail : voir le [`CLAUDE.md`](CLAUDE.md) du dépôt, puis
celui de chaque volume.
