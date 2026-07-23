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
| **État** | Publiée (145 p., 256 références) | Rédaction terminée (569 p. ; synthèse retirée le 22 juillet 2026) | Publiée, millésime `mono-v1.0` (387 p. ; synthèse retirée le 22 juillet 2026) | **Rédigé, non publié** — 34 pièces rédigées et relues (≈ 160 400 mots), gouvernance PRD v1.3 / TOC v0.8 / PRDPlan v0.5 ; finalisation P5 en cours ; **PDF assemblé le 23 juillet 2026** (428 p., gabarit FESP), non publiable en l'état | **Cadrage seul** — TOC v0.14 (+ conspectus) |

## Veille technologique — le document transversal

[`Veille Technologique.md`](Veille%20Technologique.md) → `Veille Technologique.pdf` (**145 p.**,
14 sections numérotées, **256 références**, 15 tableaux). Revue vérifiée où chaque énoncé factuel
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
- **Article de synthèse** — *retiré du dossier le 22 juillet 2026* (`Synthese Monographie.md` / `.pdf`,
  69 p.). La monographie et son Annexe B restent les seuls livrables rédigés du volume.
- **Démonstrateur `Borealis-Go/`** — code Go exécutable matérialisant l'ADS : **5 agents A2A** et
  **4 serveurs MCP** orchestrant une pré-qualification de crédit (jamais un octroi ferme), sur les
  SDK officiels des deux protocoles. **12 ADR**, journal d'audit à chaîne de hachage, vérification
  adverse à chaque phase, invariants critiques prouvés par mutation ; couverture déclarée 96,2 %
  au rapport final. C'est ce démonstrateur qui fournit la §4.12 de la veille.

## Vol. II — L'autonomie encadrée

Monographie sur l'interopérabilité et l'orchestration agentique en services financiers canadiens,
publiée sous le millésime `mono-v1.0`. **92 059 mots** en 29 pièces (24 chapitres, avant-propos,
annexes A-D) selon son README ; `Monographie.pdf` **387 p.** (article de synthèse, 66 p., retiré du
dossier le 22 juillet 2026).

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

**Rédigé de bout en bout, non encore publié.** Les **34 pièces** — avant-propos, 28 chapitres en
9 parties, 5 annexes — sont **rédigées, relues adversarialement et corrigées** (statut constaté sur
pièce le 22 juillet 2026), pour **≈ 160 400 mots réels** au regard d'une cible indicative de
**≈ 102 500**. Le socle factuel propre compte **98 entrées** (F-01 à F-98), sur **33 entrées
héritées** (H-01 à H-33) ; les **15 lots d'instruction sont clos**. Le volume s'organise autour de
trois capacités — *émettre* une identité opposable (le passeport d'agent), l'*appliquer* au
maillage d'agents, l'*exploiter* dans la durée (AgentOps) — sous l'horloge post-quantique.

⚠ **Rédigé ne vaut pas publiable.** La phase de finalisation (**P5**) est en cours : revalidation
temporelle finale, rejeu des motifs de balayage sur les 34 pièces ; le pipeline de rendu a été
créé le 23 juillet 2026 (copie du FESP du Vol. II) et **quinze remontées de gouvernance demeurent
ouvertes** (R-G-43 à R-G-57), dont plusieurs relèvent de l'auteur. **Le PDF est assemblé
(428 p., gabarit FESP) ; rédigé ne vaut pas publiable.**

Le dossier porte trois répertoires — la gouvernance dans `prd/`, la rédaction dans `monographie/`,
les rapports de vérification dans `verification/` —, plus un
[`CLAUDE.md`](1%20-%20Corpus%20Agentique/3%20-%20EntrepriseAgentique/CLAUDE.md) à l'agent qui
édite. Documents de gouvernance, par ordre d'autorité :

1. [`prd/PRD.md`](1%20-%20Corpus%20Agentique/3%20-%20EntrepriseAgentique/prd/PRD.md) **v1.3** —
   contenu, héritage du socle, quatorze garde-fous, critères d'acceptation ; **prime en cas de
   conflit**, y compris sur le TOC ;
2. [`prd/TOC.md`](1%20-%20Corpus%20Agentique/3%20-%20EntrepriseAgentique/prd/TOC.md) **v0.8** —
   autorité sur le découpage (28 chapitres, 9 parties, 34 pièces) ;
3. [`prd/PRDPlan.md`](1%20-%20Corpus%20Agentique/3%20-%20EntrepriseAgentique/prd/PRDPlan.md)
   **v0.5** — plan d'exécution (phases P0 à P5).

Le volume naît des lacunes des deux précédents : identité non humaine et délégation multi-saut
(verrou identifié au Vol. I), mécanique des attaques et valeur cryptographique des Agent Cards
(questions ouvertes du Vol. II).

## Vol. IV — La somme agentique (compendium)

**Au stade du cadrage seul, lui aussi.** Le dossier
[`2 - Compendium Agentique/`](2%20-%20Compendium%20Agentique/) porte une table des matières
commentée ([`TOC.md`](2%20-%20Compendium%20Agentique/TOC.md), **v0.14 du 23 juillet 2026**), son
**PRD de gouvernance de la rédaction** ([`PRD.md`](2%20-%20Compendium%20Agentique/PRD.md), v0.1 du
23 juillet 2026 — portes de lancement, régimes de preuve, critères d'acceptation, jalons), sa vue
synoptique dérivée ([`README.md`](2%20-%20Compendium%20Agentique/README.md)), son exécutable
de contrôle ([`check-toc.py`](2%20-%20Compendium%20Agentique/check-toc.py), avec son harnais de
validation par mutation) et un
[`CLAUDE.md`](2%20-%20Compendium%20Agentique/CLAUDE.md) de conventions —
**aucun chapitre rédigé : c'est un plan de refonte, pas une nouvelle thèse.**

Sa nature le distingue des trois autres : ce n'est ni un quatrième panneau ni un méta-index, mais
un **omnibus qui absorbe les Vol. I, II et III** en un seul ouvrage réordonné et dédoublonné, à
numérotation continue — 57 chapitres en 10 livres, ≈ 369 000 à 394 000 mots projetés. Une fois
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
├── Veille Technologique.md / .pdf         ← veille autonome, 18 juillet 2026, passe du 23 juillet 2026 (145 p., 256 réf.)
├── 1 - Corpus Agentique/                  ← le triptyque
│   ├── 1 - InteroperabiliteAgentique/       Vol. I
│   │   ├── Chapitres/                         7 chapitres + 7 bibliographies + Annexe B (ADS)
│   │   ├── Monographie.md / .pdf              assemblage (569 p.)
│   │   ├── Borealis-Go/                       démonstrateur Go (MCP + A2A), 12 ADR
│   │   └── build/                             pipeline FESP (Mermaid → Pandoc → Typst)
│   ├── 2 - OrchestrationAgentique/          Vol. II
│   │   ├── monographie/                       29 pièces (parties I-VII, annexes, registre des gels)
│   │   ├── prd/                               PRD, PRDPlan, TOC, audit + 2 PDF sources — gouvernance
│   │   ├── verification/                      revalidations et grille de conformité CA-1..CA-8
│   │   ├── build/                             assemblage + pipeline Pandoc → Typst
│   │   └── Monographie.md / .pdf              assemblage (387 p.)
│   └── 3 - EntrepriseAgentique/             Vol. III
│       ├── CLAUDE.md                          conventions du volume
│       ├── prd/                               PRD v1.3, TOC v0.8, PRDPlan v0.5 — gouvernance
│       ├── monographie/                       34 pièces rédigées + registre des gels
│       ├── verification/                      29 rapports (lots, relectures, revalidations)
│       ├── build/                             pipeline FESP (copie du Vol. II) + assemble.py
│       └── Monographie.md / .pdf              assemblage (428 p., gabarit FESP) — non publiable
└── 2 - Compendium Agentique/              ← Vol. IV
    ├── CLAUDE.md                            conventions du volume
    ├── TOC.md                               table des matières commentée (v0.14) — spécification
    └── README.md                            vue synoptique dérivée du TOC (le « conspectus » du volume)
```

**Où sont les `CLAUDE.md`.** Un par périmètre, sans recouvrement : la racine porte les conventions
communes et celles de la veille ; les Vol. I, II, III et IV portent chacun les siennes ; le
démonstrateur Go a les siennes, qui priment dans son répertoire. Le `CLAUDE.md` du Vol. IV renvoie à
son `TOC.md` comme spécification de contenu.

## Construire les PDF

Quatre chaînes distinctes, à lancer depuis le dossier concerné.

**Veille technologique** (racine) — invocation Pandoc directe, gabarit Typst par défaut :

```bash
pandoc "Veille Technologique.md" --pdf-engine=typst --toc -o "Veille Technologique.pdf"
```

**Vol. I** — pipeline FESP, avec pré-rendu des 28 diagrammes Mermaid ; depuis
`1 - Corpus Agentique/1 - InteroperabiliteAgentique/` :

```bash
bash build/build-pdf.sh                              # Monographie.pdf
```

**Vol. II** — assemblage des 29 pièces, puis une **copie** du même pipeline ; depuis
`1 - Corpus Agentique/2 - OrchestrationAgentique/` :

```bash
python build/assemble.py                    # monographie/ → Monographie.md
bash   build/build-pdf.sh Monographie.md    # → Monographie.pdf
```

⚠ `build/assemble.py` cherche encore `TOC.md` à la racine du volume alors qu'il vit dans `prd/` :
**l'assemblage du Vol. II échoue en l'état.** Les deux copies du pipeline évoluent séparément ;
un correctif au Vol. I ne se propage pas au Vol. II.

**Vol. III** — assemblage des 34 pièces, puis une **troisième copie** du même pipeline
(créée le 23 juillet 2026, au gabarit des monographies) ; depuis
`1 - Corpus Agentique/3 - EntrepriseAgentique/` :

```bash
python build/assemble.py                    # monographie/ → Monographie.md
bash   build/build-pdf.sh Monographie.md    # → Monographie.pdf (428 p.)
```

Les trois copies du pipeline évoluent séparément. Le PDF porte une **note d'état** en tête :
rédigé, **non publiable** tant que les quinze remontées ouvertes (R-G-43 à R-G-57) ne sont pas
tranchées.

**Prérequis :** Pandoc ≥ 3.1.7, Typst ≥ 0.12, `python3` + `pypdf` ; polices Liberation Sans et
DejaVu Sans (pipeline FESP), New Computer Modern (veille) ; pour les diagrammes, Node ≥ 18 +
[`@mermaid-js/mermaid-cli`](https://github.com/mermaid-js/mermaid-cli) et un Chromium. Les trois
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
`doc/`) et sur les décomptes **re-mesurés** — veille 142 p. / 244 réf. / 14 sections, Vol. I
569 p. / 69 p. / 28 diagrammes / 12 ADR, Vol. II 387 p. / 66 p. / 29 pièces / 46 entrées de socle,
tous inchangés. Le 23 juillet 2026, la passe complémentaire de la veille (sous-section 12.4,
l'après-agentique en préimpression) porte ses décomptes à **144 p. / 256 réf.**, re-mesurés sur le
PDF régénéré ; les chiffres du 18 juillet ci-dessus décrivent l'état de cette date-là. La passe de
révision du même 23 juillet (corrections vérifiées et aération des sections 4.10 et 10, en vue de
la publication arXiv) porte la pagination à **145 p.**, références inchangées.

Le même 23 juillet 2026, une passe de cohérence a réaligné les `README.md` et `CLAUDE.md` sur l'état
réel du dépôt : Vol. IV porté à **TOC v0.11** (57 chapitres, 10 livres, ≈ 369 000–394 000 mots
projetés) avec son `README.md` et son `CLAUDE.md` ; renommage `doc/` → `prd/` (Vol. II) et
suppressions des articles de synthèse et des `index.html` (Vol. I et II) constatés **committés**
(commit `fd8f1be`, arbre de travail propre) ; création du pipeline FESP du Vol. III (troisième copie
indépendante) enregistrée ; nom du dépôt corrigé de « Monographies » en `Agentique` dans les
fichiers du démonstrateur `Borealis-Go`.

⚠ Le décompte des diagrammes du Vol. I se mesure avec un motif **ancré** :
`grep -c '^```mermaid'` donne 28. Le motif non ancré en retourne 29 — il attrape une ligne de prose
de la note de production qui cite la balise.

**Restent ouverts, signalés et non corrigés** — ce sont des fichiers de code ou de contenu, hors du
périmètre de cette passe documentaire :

| Fichier | Reliquat |
|---|---|
| `1 - Corpus Agentique/2 - OrchestrationAgentique/build/assemble.py` | lit `TOC.md` à la racine du volume ; il vit dans `prd/` — **assemblage hors service** |
| `…/2 - OrchestrationAgentique/prd/PRDPlan.md` | renvoi `](CLAUDE.md)` → `../CLAUDE.md` |
| `…/2 - OrchestrationAgentique/prd/audit.md` | renvois `](monographie/…)` → `../monographie/…` |
| `…/2 - OrchestrationAgentique/verification/relecture-CA.md` | renvois `](../PRD.md)`, `](../PRDPlan.md)`, `](../audit.md)` → `../prd/…` |
| `…/1 - InteroperabiliteAgentique/Borealis-Go/docs/ARCHITECTURE.md` | ligne 906 : annonce « les 11 ADR » ; le dossier `docs/adr/` en compte 12 (0001-0012, hors gabarit) |
| `…/2 - OrchestrationAgentique/build/__pycache__/` | bytecode Python (`.pyc`) versionné par mégarde — à retirer du suivi et à ignorer |

Le `monographie/` du Vol. II concentre à lui seul **48 de ces renvois cassés**, sur 28 de ses
29 pièces : voir le tableau et la commande de contrôle du [`CLAUDE.md`](1%20-%20Corpus%20Agentique/2%20-%20OrchestrationAgentique/CLAUDE.md) du volume.

⚠ **Plus de pages de présentation ni de publication GitHub Pages pour les volumes.** Les deux
`index.html` (Vol. I et Vol. II) ont été supprimés le 22 juillet 2026 (commit `fd8f1be`). Ils
annonçaient « Lire en ligne » sous `https://agbruneau.github.io/Monographies/…`, et leurs balises
`canonical`, `og:url` et liens « Dépôt GitHub » nommaient tous `Monographies` — adresses fausses de
toute façon, le dépôt s'appelant `Agentique` (`github.com/agbruneau/Agentique`), et cause des 404
relevés. Rétablir une publication en ligne supposerait de repartir de la bonne base
(`https://agbruneau.github.io/Agentique/`) et de vérifier que Pages est bien activé pour ce dépôt.

Conventions de rédaction et règles de travail : voir le [`CLAUDE.md`](CLAUDE.md) du dépôt, puis
celui de chaque volume.
