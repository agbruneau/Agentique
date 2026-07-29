# CLAUDE.md — volume I (Interopérabilité agentique)

Guide pour Claude Code (claude.ai/code) **dans ce dossier**.

## Périmètre de ce fichier

Ce `CLAUDE.md` ne régit que le **volume I**, sous `1 - Corpus/1 - InteroperabiliteAgentique/`
(dossier parent renommé le 25 juillet 2026, `1 - Corpus Agentique/` auparavant). Il ne dit rien des
autres livrables du dépôt *Agentique* :

| Ce que vous cherchez | Où |
|---|---|
| Place du volume I dans le corpus, ordre de lecture, divergences entre volumes | [README du dépôt](../../README.md) |
| Conventions communes et **conventions de la veille technologique** (à la racine) | [`CLAUDE.md` du dépôt](../../CLAUDE.md) |
| Volume II — *L'autonomie encadrée* (cas canadien) | [`2 - OrchestrationAgentique/CLAUDE.md`](../2%20-%20OrchestrationAgentique/CLAUDE.md) |
| Volume III — *L'entreprise agentique* (rédigé, non publiable) | [`3 - EntrepriseAgentique/CLAUDE.md`](../3%20-%20EntrepriseAgentique/CLAUDE.md) — et son [`README.md`](../3%20-%20EntrepriseAgentique/README.md) |
| Volume IV — *La somme agentique* (compendium, **50 chapitres rédigés hors portes, arrêté en révision finale, non publiable**) | [`2 - Compendium/`](../../2%20-%20Compendium/) |

⚠ **Le dépôt s'appelle `Agentique`** (`github.com/agbruneau/Agentique`), pas « Monographies ». Ce
nom-là ne survit que dans du contenu gelé (les références [217]-[218] de la veille) ; partout
ailleurs il se corrige.

## Nature du volume

Projet d'**écriture** en **français canadien** autour de l'**interopérabilité agentique** : **deux livrables rédigés**, rendus dans un même PDF, et rien d'autre depuis le 25 juillet 2026 :

1. **Monographie** de science et génie informatique, à double public — **recherche** (modèles, formalismes, état de l'art) et **praticien-architecte** (normes, protocoles, mises en œuvre). Sept chapitres en spirale du général au spécifique ; **socle des sources arrêté à juin 2026** ; invariant transversal rappelé à chaque couche : *découplage, contrat, évolution*.
2. **Architecture détaillée de solution (ADS)**, intégrée comme **Annexe B** de la monographie — source [`Chapitres/Annexe B - Architecture de Solutions.md`](Chapitres/Annexe%20B%20-%20Architecture%20de%20Solutions.md). Elle projette la monographie (surtout ch. 5-6) sur une entreprise fictive (*Coopérative financière Boréalis*) et une pile **IBM** consolidée : livrable d'ingénierie *prêt au déploiement* (diagrammes, contrats, NFR, topologie, runbooks), de nature distincte du corps doctrinal mais rendu dans le même PDF.

### ⚠ Le démonstrateur `Borealis-Go/` a été retiré du dépôt le 25 juillet 2026 — fait daté, consigné et non corrigé

**Constat sur le dépôt.** Le commit **`60f57f6`** (« restructuration du repo ») supprime le dossier
`Borealis-Go/` en entier — code Go des 5 agents A2A et 4 serveurs MCP, 12 ADR, PRD et plan
d'exécution, journaux de vérification, présentation PDF. Il ne se lit plus que dans l'historique
git : `git show 60f57f6~1:'1 - Corpus Agentique/1 - InteroperabiliteAgentique/Borealis-Go/…'`
(chemin de l'arbre **avant** le renommage du dossier parent, opéré au même commit).

**Trois conséquences pour qui édite ici.**

- Ne **pas** rétablir de renvoi vers `Borealis-Go/`, ni de chaîne d'outillage Go (`make check`, gate
  de couverture) : il n'y a plus qu'une chaîne dans ce dossier, le pipeline FESP.
- Le **`CLAUDE.md` du démonstrateur est parti avec lui.** La règle « il prime dans son répertoire »
  n'a plus d'objet ; ce fichier est désormais le seul du dossier.
- Les renvois **entrants** perdent leur cible : la **référence [217] de la veille** (§4.12, « De la
  spécification au code ») et les mentions du Vol. III (ch. 28, PRD, TOC, confrontation des thèses).
  *Un renvoi exact vers un fichier absent reste exact ; il cesse d'être opposable.* **Les corriger
  relève des documents émetteurs, pas d'ici** — et la veille, publiée, ne se corrige pas après coup.

⚠ **L'article de synthèse et la page `index.html` ne sont plus dans ce dossier.** `Synthese Monographie.md`, son PDF (69 p.) et `index.html` ont été retirés — **suppression committée le 22 juillet 2026** (commit `fd8f1be`), arbre de travail propre. Deux conséquences pour qui édite ici :

- ne pas rétablir de renvoi vers ces fichiers ni de chaîne de rendu qui les vise ;
- les renvois **entrants** des volumes aval qui résolvaient contre `Synthese Monographie.md` (§10, §11.5 et tableau 15 — voir [`Chapitres/TOC.md`](Chapitres/TOC.md) §Filiation) n'ont plus de cible dans le dépôt. Les corriger relève des volumes émetteurs, pas d'ici.

⚠ **La veille technologique n'est plus un livrable de ce dossier.** Elle a été déplacée à la racine du dépôt (`Veille Technologique.md`), couvre désormais les quatre volumes et porte sa propre édition (**édition d'août 2026**, faits gelés au 29 juillet 2026, **161 p., 269 références**) : ses conventions et sa chaîne de rendu sont au [`CLAUDE.md` du dépôt](../../CLAUDE.md). Ne pas la traiter ici.

**État : rédaction terminée.** Le travail courant est la finalisation et la maintenance — corrections, vérification adverse des citations, régénération du PDF. Outillage : `git` et le pipeline de rendu (voir *Commandes*) — plus de chaîne Go dans ce dossier.

## Organisation

Contenu rédigé dans [`Chapitres/`](Chapitres/), deux fichiers par chapitre, plus l'ADS :

| Fichier | Rôle |
|---|---|
| `Chapitre N - {Sujet}.md` | chapitre rédigé (corps) |
| `Chapitre N - Bibliographie - {Sujet}.md` | références vérifiées du chapitre |
| `Annexe B - Architecture de Solutions.md` | corps de l'ADS, repris tel quel dans `Monographie.md` |
| `TOC.md` | table des matières commentée, **v1.0 du 18 juillet 2026** — rétro-documentation relevée sur le texte livré, non spécification d'un ouvrage à écrire (à la différence des `TOC.md` des Vol. III et IV) |

Assemblage et livrable à la racine :

- [`Monographie.md`](Monographie.md) → `Monographie.pdf` (**569 p.**) — **source unique** du PDF : liminaires (page titre Typst, résumé, table des matières, abréviations) + 7 chapitres + Bibliographie générale + **Annexe A** (documents d'accompagnement) + **Annexe B** (l'ADS : 18 sections + vues *blueprint* §0.1-0.2, 6 sous-annexes, 28 diagrammes Mermaid). Rendu FESP (Pandoc → Typst), diagrammes pré-rendus.

⚠ **Plus de page de présentation ni de publication GitHub Pages pour ce volume** : `index.html` a été retiré (voir *Nature du volume*). Les adresses `https://agbruneau.github.io/Monographies/…` qui circulaient étaient de toute façon fausses — le dépôt s'appelle `Agentique`. Ne pas réintroduire de renvoi « Lire en ligne » sans avoir d'abord constaté que Pages est activé sur le bon dépôt.

Progression de la monographie (chaque chapitre suppose les précédents) :

1. Interopérabilité des SI (fondements, intégration d'entreprise)
2. IA agentique
3. Interopérabilité agentique (MCP, A2A…)
4. … en entreprise
5. … dans le domaine financier
6. Blueprint d'architecture d'entreprise ArchiMate (formalise les ch. 1-5)
7. Horizon 2027-2032 (chapitre prospectif / *capstone* projetant les ch. 1-6)

## Commandes

Une seule chaîne de rendu dans ce dossier : le **pipeline FESP** (`build/build-pdf.sh`). Se lance depuis `1 - Corpus/1 - InteroperabiliteAgentique/`.

```bash
bash build/build-pdf.sh                            # Monographie.pdf (défaut ; pré-rend les 28 diagrammes Mermaid)
```

Le script prend un `.md` source en argument (défaut `Monographie.md`) et en déduit le `.pdf` ; depuis le retrait de l'article de synthèse, `Monographie.md` est la **seule** source de ce dossier. Les blocs ` ```mermaid ` sont pré-rendus en SVG (mermaid-cli) puis injectés avant Pandoc→Typst ; si `mmdc` est absent, ils restent en bloc de code (mode dégradé, sans échec). La pagination liminaire romaine→arabe ne s'applique qu'à `Monographie.md`. Gabarit : `build/fesp.template` (police Liberation Sans, repli Arial).

Les volumes II et III possèdent chacun une **copie** de ce pipeline, précédée d'une étape d'assemblage qui leur est propre (`build/assemble.py`) — celle du Vol. III créée le 23 juillet 2026, en troisième copie. Les trois évoluent séparément : ne pas présumer qu'un correctif ici s'y propage. La veille de la racine, elle, n'utilise **pas** FESP (voir le [`CLAUDE.md` du dépôt](../../CLAUDE.md)).

**Prérequis :** Pandoc ≥ 3.1.7, Typst ≥ 0.12, `python3` + `pypdf`, polices Liberation Sans + DejaVu Sans (repli déclaré dans le gabarit FESP : Arial + Segoe UI Symbol). Diagrammes : Node ≥ 18 + `@mermaid-js/mermaid-cli` (`mmdc`) + un Chromium (surcharges `MMDC=…`, `PUPPETEER_CONFIG=…`).

**Notes d'environnement :** `build/build-pdf.sh` exporte lui-même `PYTHONUTF8=1` (ligne 16) — inutile de le faire à la main sous Windows. `DIAGCACHE` **n'est pas un cache écrit par le script** : c'est un répertoire de SVG `diagram-NN.svg` **fournis par l'appelant**, lus tels quels ; les SVG que le script rend vont dans un `$TMP` détruit à la sortie (`trap … EXIT`). Pour réutiliser des diagrammes d'un build à l'autre, il faut les y déposer soi-même.

## Convention des chapitres rédigés

- **Sections numérotées, préfixées du numéro de chapitre** : sections `N.0, N.1, N.2…` (`##`) ; sous-sections `N.1.1` (`###`) ; items feuilles `N.1.1.1` (`####`). Le premier nombre est **toujours** le numéro du chapitre (ch. 1 → `1.6.3.1`, ch. 3 → `3.2.1`). *Exception documentée :* les ch. 2 et 4 ouvrent à `N.1` (pas de section `N.0`) — ne pas renuméroter.
- **En-tête de chapitre** : titre `#`, bloc `> **Résumé.**`, puis ligne *Public visé / Fil conducteur / dates*.
- **Renvois inter-sections** en clair : intra-chapitre `(voir §1.1.1)`, `(détaillé en 1.6.2)` ; inter-chapitres avec le numéro du **chapitre cible** `(cf. ch.1 §1.6.3.1)`, `(renvoi ch. 7)`. Tout renvoi doit pointer vers une cible existante.
- **Invariant transversal** rappelé à chaque couche : *découplage, contrat, évolution*.

## Convention de l'ADS (Annexe B)

- **Numérotation native conservée, décalée d'un niveau sous `# Annexe B`** : sections `## 0…17` (plus `## 0.1`-`0.2`, vues *blueprint* d'ouverture) + `## Annexe A…F` internes ; sous-sections `### N.x`. Ne pas confondre : le `§6` de l'ADS (sécurité) ≠ ch. 6 de la monographie ; l'`## Annexe B` interne (matrice de traçabilité) ≠ l'**Annexe B** de la monographie (= l'ADS entière). Les renvois à la monographie restent explicites (`cf. Monographie ch.6 §6.1.3`).
- **Diagrammes Mermaid *inline*** (aucun fichier image séparé), légendés `**Figure N — …**`. Toute syntaxe doit passer `mmdc` (séquences : pas de `;` ni `{}` dans les messages ; libellés d'arête sans parenthèses nues).
- **Vues d'entreprise en ArchiMate 4** (stéréotypes du registre Monographie ch.6 §6.1.9), équivalent 3.2 noté si requis.
- **Extraits de configuration *illustratifs*** (jamais de secret réel) ; statuts vivants marqués ⚠ ; valeurs chiffrées (SLO, RPO/RTO, débits) = hypothèses à calibrer.

## Convention des fichiers Bibliographie

- **Format de citation** : `Auteurs/Organisme (Année). *Titre*. Support/éditeur. Identifiant stable (DOI / RFC / ISO/IEC / W3C / URL).`
- **Catégories** thématiques ; ordre alphabétique par auteur/organisme (normes ISO/IEC et RFC par numéro croissant). Exceptions déclarées en tête de fichier : le ch. 1 classe les RFC au rang alphabétique de leur auteur/éditeur ; les textes réglementaires des ch. 4-5 suivent l'ordre chronologique.
- **Marqueur ⚠** = *ressource vivante* (doc produit, spec versionnée par date, travail en cours) dont la version/ancre doit être fixée au moment de citer. Ne pas le retirer sans avoir figé la version.
- `cf. §X` relie une entrée aux sections qui s'en servent ; `à re-vérifier à la rédaction` = contrôle à refaire avant publication (conserver tel quel).
- **Accents des chaînes de citation** : préservés *verbatim* même fautifs (`fevrier`), pour ne pas altérer les métadonnées sources. Ne pas « corriger » au fil de l'eau.

## Règles de travail

- **Vérification adverse des citations.** Toute référence ajoutée ou modifiée est vérifiée sur le web (existence, auteurs, année, numéro de norme/RFC/recommandation) avant d'être affirmée exacte. Chaque bibliographie de chapitre porte un bilan (`N références vérifiées → M entrées…`) ; le mettre à jour si on touche au compte.
- **Dates et statut prospectif.** Signaler toute nouveauté postérieure à juin 2026 — c'est le gel du volume. Le **ch. 7** projette l'avenir et trie chaque énoncé en **PROGRAMMÉ / PROJETÉ / SPÉCULATIF** (faits datés / prévisions millésimées / paris) — ne jamais présenter du spéculatif comme acquis. Dans l'ADS, ne jamais présenter un statut *preview* (⚠) comme GA.
- **Synchronisation et publication.** Après toute édition d'un chapitre : reporter le changement dans `Monographie.md`, régénérer le PDF **et le pousser avec la source** — jamais la source seule. Si la pagination change, reporter le nouveau compte dans ce `CLAUDE.md`, dans le [`README.md`](README.md) du volume **et dans le [README du dépôt](../../README.md)**, qui affiche lui aussi les paginations de tous les livrables.
- **Registre et ton.** Qualité rédactionnelle soutenue ; **ton professionnel et neutre** (pas de marketing, pas de 1ʳᵉ personne). Gloses, titres et notes en français.
- **Longueur.** Chaque **chapitre de la monographie** fait au moins **10 000 mots** ; préserver ce seuil lors des révisions.
- **Messages de commit** : courts, en français, nommés par livrable touché — `Chapitre 5`, `Chapitre 3 et 4`, `Annexe B`. ⚠ Convention **propre au volume I** : le volume II emploie des Conventional Commits en anglais (`docs(mono): …`). Vérifier dans quel dossier on travaille avant de rédiger le message.
