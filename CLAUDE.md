# CLAUDE.md — dépôt *Monographies*

Guide pour Claude Code (claude.ai/code) à la **racine** du dépôt.

## Ce que ce fichier régit — et ce qu'il ne régit pas

Ce dépôt réunit cinq livrables de périmètres distincts (voir le [`README.md`](README.md)). Les
règles ne sont **pas communes** d'un dossier à l'autre : chacun a ses conventions, et elles
divergent volontairement. Ce fichier régit deux choses seulement — la **racine du dépôt** et la
**veille technologique** qui y vit.

| Périmètre | Fichier qui fait autorité |
|---|---|
| Racine, veille technologique, arbitrages inter-volumes | **ce fichier** |
| Vol. I — *Interopérabilité agentique* (rédaction) | [`1 - Corpus Agentique/1 - InteroperabiliteAgentique/CLAUDE.md`](1%20-%20Corpus%20Agentique/1%20-%20InteroperabiliteAgentique/CLAUDE.md) |
| Démonstrateur Go du Vol. I (code) | [`…/1 - InteroperabiliteAgentique/Borealis-Go/CLAUDE.md`](1%20-%20Corpus%20Agentique/1%20-%20InteroperabiliteAgentique/Borealis-Go/CLAUDE.md) — **prime dans son répertoire** |
| Vol. II — *L'autonomie encadrée* (rédaction, gouvernance PRD) | [`1 - Corpus Agentique/2 - OrchestrationAgentique/CLAUDE.md`](1%20-%20Corpus%20Agentique/2%20-%20OrchestrationAgentique/CLAUDE.md) |
| Vol. III et Vol. IV | pas de `CLAUDE.md` — leur `TOC.md` tient lieu de spécification |

**Le fichier le plus spécifique gagne.** En travaillant dans un dossier de volume, appliquer son
`CLAUDE.md`, pas celui-ci.

## Divergences de conventions entre volumes — à ne pas uniformiser

Ces écarts sont **délibérés** ; les corriger « pour la cohérence » casserait des références
croisées ou l'historique d'un volume.

| | Vol. I | Vol. II |
|---|---|---|
| Messages de commit | courts, **en français**, par livrable (`Chapitre 5`, `Annexe B`) | **Conventional Commits en anglais** (`docs(mono): …`) |
| Autorité de contenu | les conventions de chapitres du `CLAUDE.md` | le **PRD** (`doc/PRD.md`), qui prime sur tout |
| Traçabilité des faits | vérification adverse des citations, bilan par bibliographie | socle factuel **F-xx** avec niveaux **[A]/[B]/[C]** |
| Pipeline PDF | FESP (Mermaid → Pandoc → Typst) | **copie** du FESP + `assemble.py` en amont |

Les deux pipelines PDF sont des copies indépendantes : **un correctif à l'un ne se propage pas à
l'autre.** La veille, elle, n'utilise ni l'un ni l'autre (voir plus bas).

## Veille technologique — le livrable de la racine

`Veille Technologique.md` → `Veille Technologique.pdf` (**107 p.**, 13 sections numérotées,
**218 références**, édition du 18 juillet 2026). Document **autonome** : il n'est repris dans aucune
monographie, et il est le seul à citer les volumes du dépôt — §4.12 pour le démonstrateur
`Borealis-Go` du Vol. I (réf. [217]), §8.4 pour le croisement canadien du Vol. II (réf. [218]).
Il en cite **deux, pas trois** : le Vol. III n'y apparaît sous aucune forme, et la veille parle
elle-même de « deux corpus compagnons ». L'auto-citation est assumée et divulguée ; ses limites
sont exposées en section 10.

### Rendu

Invocation Pandoc **directe**, gabarit Typst *par défaut* — jamais `build/build-pdf.sh` :

```bash
pandoc "Veille Technologique.md" --pdf-engine=typst --toc -o "Veille Technologique.pdf"
```

Son identité visuelle (police New Computer Modern, mise en page) vient du gabarit par défaut, pas
d'un `.template` du dépôt. **Prérequis :** Pandoc ≥ 3.1.7, Typst ≥ 0.12, police New Computer Modern.

### Conventions de rédaction

- **En-tête YAML complet** : titre, auteur (avec la date d'édition), résumé,
  `mainfont: "New Computer Modern"`, `section-numbering: "1.1.1"`.
- **Sections `#` numérotées automatiquement** par Pandoc (Introduction = 1 … Conclusion = 13) ;
  sous-sections `##` → `N.1`. Les sections liminaires ou finales sans numéro portent `{-}`
  (`# Sommaire exécutif {-}`, `# Divulgation {-}`, `# Références {-}`).
- **Tri épistémique** : la section 12 (*Horizon prospectif 2027-2030*) trie ses sous-sections en
  **PROGRAMMÉ / PROJETÉ / SPÉCULATIF** — même logique que le ch. 7 du Vol. I. Ne jamais présenter
  du spéculatif comme acquis.
- **Références manuelles** : liste numérotée sous `# Références {-}`, dans un bloc
  `::: {#refs} … :::`. Le corps cite par crochets **littéraux** `[N]` — **pas** de champ
  `bibliography` Pandoc, **pas** de clés `@…`. Toucher au compte oblige à reporter le nouveau total
  ici, dans le [`README.md`](README.md) et dans le bilan de vérification de la veille.
- **Ressources vivantes** : les références précédées de ⚠ sont des pages sans version datée stable ;
  ne pas retirer le marqueur sans avoir figé une version.
- **Sauts de page** via blocs Typst bruts ` ```{=typst} #pagebreak(weak: true) ``` ` ; le saut avant
  la table des matières passe par `header-includes`
  (`#show outline: it => [#pagebreak(weak: true) #it]`).

### Méthode

Revue **structurée et vérifiée** : chaque énoncé factuel est adossé à une source primaire consultée
et soumis à contradiction — vérificateurs indépendants chargés de *réfuter*, contre-vérification
directe sinon. Les métriques d'adoption auto-déclarées sont attribuées à leur source à chaque
occurrence ; un statut *preview* n'est jamais présenté comme une disponibilité générale.

## Règles valant pour tout le dépôt

- **Langue.** Livrables et prose en **français canadien** soutenu ; ton professionnel et neutre
  (pas de marketing, pas de première personne). Terminologie technique anglaise entre parenthèses à
  la première occurrence ; citations verbatim en langue originale.
- **PDF versionné avec sa source.** Régénérer et pousser le `.pdf` avec le `.md` — jamais la source
  seule. Vaut pour la veille comme pour les deux monographies.
- **Décomptes.** Toute pagination, tout compte de références, de chapitres ou de pièces annoncé
  dans un `README.md` ou un `CLAUDE.md` doit être **re-mesuré** avant d'être modifié, jamais
  recopié d'un autre document. Un même chiffre vit souvent à plusieurs endroits (README du dépôt,
  README du volume, `CLAUDE.md`, JSON-LD et compteur `data-count` de l'`index.html`) : les mettre à
  jour ensemble.
- **Faits datés.** Le domaine se périme par trimestres. Les échéances à revalider sont tenues dans
  la section « Ce qui reste vivant » du [`README.md`](README.md) ; chaque volume porte en plus ses
  propres dates de gel. Deux faits datés divergent entre la veille et le Vol. II : ils sont
  **signalés, non arbitrés** — ne pas les uniformiser en silence.
- **Lacunes exposées, non comblées.** Aucune lacune déclarée d'un volume ne se comble par une
  source de moindre qualité.
- **Périmètre des fichiers de doc.** Un `README.md` s'adresse au lecteur, un `CLAUDE.md` à l'agent
  qui édite. Ne pas dupliquer d'un niveau à l'autre : le niveau supérieur situe et renvoie, le
  niveau inférieur détaille.
