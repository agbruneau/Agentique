# CLAUDE.md — dépôt *Agentique*

Guide pour Claude Code (claude.ai/code) à la **racine** du dépôt.

⚠ **Le dépôt s'appelle `Agentique`** (`github.com/agbruneau/Agentique`), pas « Monographies ». Ce
nom-là survit dans du contenu gelé — les références [217] et [218] de la veille, les URL des deux
`index.html` — et **il n'est pas corrigé en silence** : la veille est publiée, les `index.html` sont
un reliquat consigné au [`README.md`](README.md).

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
| Vol. III — *L'entreprise agentique* (cadrage, gouvernance PRD) | [`1 - Corpus Agentique/3 - EntrepriseAgentique/CLAUDE.md`](1%20-%20Corpus%20Agentique/3%20-%20EntrepriseAgentique/CLAUDE.md) |
| Vol. IV — *La somme agentique* | pas de `CLAUDE.md` — son `TOC.md` tient lieu de spécification |

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
l'autre.** La veille, elle, n'utilise ni l'un ni l'autre (voir plus bas). Le Vol. III n'a **aucun
pipeline** : en créer un serait une troisième copie — le savoir avant de le faire.

Le Vol. III prolonge l'appareil du Vol. II mais s'en écarte sur quatre points (motifs de balayage,
commande de décompte, escalade de gouvernance, numérotation des garde-fous). Ces écarts sont
consignés et motivés dans [son propre `CLAUDE.md`](1%20-%20Corpus%20Agentique/3%20-%20EntrepriseAgentique/CLAUDE.md) —
**les y lire avant d'appliquer une règle du Vol. II de mémoire.**

## Veille technologique — le livrable de la racine

`Veille Technologique.md` → `Veille Technologique.pdf` (**140 p.**, 14 sections numérotées,
**244 références**, 14 tableaux — **édition intégrale du 18 juillet 2026**). Document **autonome** :
il n'est repris dans aucune monographie, et il est le seul à citer les volumes du dépôt.

⚠ **Depuis l'édition intégrale, la veille cite les quatre volumes — mais à deux régimes distincts,
et l'écart est la règle qui compte.** Les Vol. I et II sont **rédigés** et fournissent des faits :
§4.12 pour le démonstrateur `Borealis-Go` (réf. [217]), §8.4 pour le croisement canadien
(réf. [218]). Les Vol. III et IV sont des **cadrages** — zéro chapitre, zéro entrée de socle propre
— et ne fournissent **aucun fait** : ils prêtent des instruments d'analyse (la grille des cinq
questions, les décisions de fusion), marqués comme constructions d'auteur, et leurs entrées
bibliographiques [219] et [220] portent cette réserve en toutes lettres. **Ne jamais élever un
cadrage au rang de source de fait** en le citant à l'appui d'un énoncé : c'est la faute que ces deux
cadrages prennent eux-mêmes pour objet. Le régime est posé en §13.1 et tenu à chaque occurrence.

⚠ **La section 13 porte une date propre.** Elle est passée sur la **v0.3 du `TOC.md` du Vol. IV,
datée du 19 juillet 2026** — soit le lendemain de la date d'édition de la veille. L'écart est
assumé et déclaré dans le texte (§13.5 et §2.2) ; les sections 1 à 12 restent à leur date d'état.
Ne pas « harmoniser » cette date : un cadrage qui se révise plus vite que la revue ne se gèle est
un constat de la §10, pas une incohérence à lisser.

La section 13 (« Le corpus compagnon : quatre volumes, un même objet ») est le siège de ce rendu
de compte ; la Conclusion est devenue la section **14**. L'auto-citation est assumée et divulguée ;
ses limites — dont le risque de circularité, quatre volumes partageant un auteur — sont exposées
en section 10.

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
- **Sections `#` numérotées automatiquement** par Pandoc (Introduction = 1 … Conclusion = **14**) ;
  ⚠ **le corps cite ses sections en clair** (« section 4.11.5 », « section 9.6 ») : insérer une
  section de tête au milieu décale toute la numérotation aval et casse ces renvois. Ajouter en
  **sous-section** (l'ajout en queue ne décale rien) ou, si une section de tête est nécessaire,
  l'insérer juste avant la Conclusion et corriger les renvois. Même piège pour les **tableaux**,
  numérotés automatiquement : une table insérée en amont décale les « tableau N » cités en aval.
  Ces deux pièges sont couverts par `check-veille.py` (voir plus bas). Les sous-sections `##` deviennent `N.1` ; les
  sections liminaires ou finales sans numéro portent `{-}` (`# Sommaire exécutif {-}`,
  `# Divulgation {-}`, `# Références {-}`). **Toute table porte une légende** (ligne `: …`) : une
  table sans légende consomme quand même un numéro et creuse un trou dans la série.
- **Décomptes annoncés en toutes lettres.** Le corps annonce ses propres cardinaux — « dix
  constats », « quatorze contributions », « vingt questions ouvertes ». ⚠ **Ils ne se mettent pas à
  jour tout seuls** : ajouter un item sans re-mesurer produit une contradiction interne que la
  relecture attrape mais que le rendu ne signale pas. Le piège n'est pas le nombre posé au titre de
  la liste — c'est celui qui la **cite à distance** (sommaire exécutif, conclusion, divulgation).
  Couvert par `check-veille.py`.
- **Tri épistémique** : la section 12 (*Horizon prospectif 2027-2030*) trie ses sous-sections en
  **PROGRAMMÉ / PROJETÉ / SPÉCULATIF** — même logique que le ch. 7 du Vol. I. Ne jamais présenter
  du spéculatif comme acquis.
- **Références manuelles** : liste numérotée sous `# Références {-}`, dans un bloc
  `::: {#refs} … :::`. Le corps cite par crochets **littéraux** `[N]` — **pas** de champ
  `bibliography` Pandoc, **pas** de clés `@…`. Toucher au compte oblige à reporter le nouveau total
  ici, dans le [`README.md`](README.md) et dans le bilan de vérification de la veille.
- **Ressources vivantes** : les références précédées de ⚠ sont des pages sans version datée stable ;
  ne pas retirer le marqueur sans avoir figé une version. ⚠ **Le marqueur ne sert qu'à cela.** Une
  réserve portant sur le *contenu* d'une source (« non adopté », « errata publiés après parution »,
  « aucun chapitre rédigé ») s'écrit **`**Réserve —**`**, jamais avec ⚠ : surcharger le marqueur
  rend indistinguables une page qui bouge et un fait qu'il faut nuancer.
- **Pas deux entrées pour un même document.** Avant d'ajouter une référence, vérifier qu'aucune
  entrée ne porte déjà la même URL, le même DOI ou le même identifiant arXiv — l'édition intégrale
  a dû en fusionner deux paires. Couvert par `check-veille.py`, qui normalise les URL (`http`/`https`,
  `www`, barre finale, `/abs/` vs `/pdf/`, suffixe de version) : deux formes différentes du même
  document ne se voient pas à l'œil.

### Contrôles de publication — `check-veille.py`

```bash
python check-veille.py    # sortie 0 si tout passe, 1 sinon
```

**À exécuter avant chaque `pandoc`.** Couvre les quatre défauts que le rendu ne signale jamais :
renvois de section et de tableau non résolus (y compris `§N.M` et `QO n`), tables sans légende,
cardinaux en toutes lettres périmés, doublons bibliographiques, références pendantes ou orphelines.

⚠ **Ce script est du contenu : il se vérifie comme le reste.** Trois faux positifs y sont déjà
neutralisés, et les réintroduire en « simplifiant » un motif rendrait le contrôle bruyant donc
ignoré : `(8.9)` et `(2.0)` sont des **numéros de version**, pas des renvois ; « quatre-vingt-dix »
contient « vingt-dix », qui n'est pas un nombre ; « constats » et « questions » servent aussi à des
énumérations **locales** légitimes (« Trois constats se dégagent », la grille des « cinq questions »
de la §7.6) — d'où l'ancrage des cardinaux sur la tournure d'annonce et non sur le nom nu. Avant de
publier une modification du script, la valider par mutation : introduire chacune des fautes dans une
copie et vérifier que le script **échoue**, après avoir constaté qu'il **passe** sur le document
intact — sans cette seconde vérification, un script cassé « détecte » tout.
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
