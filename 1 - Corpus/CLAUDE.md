# CLAUDE.md — dossier `1 - Corpus/` (le triptyque)

Guide pour Claude Code (claude.ai/code) **dans ce dossier**.

## Périmètre de ce fichier

Ce `CLAUDE.md` régit le **dossier `1 - Corpus/`** lui-même : son [`README.md`](README.md) (la synthèse consolidée des trois monographies) et les arbitrages de cohérence entre volumes. Il ne régit **aucun des trois volumes** — chacun a son propre `CLAUDE.md`, qui prime dans son périmètre.

| Ce que vous cherchez | Où |
|---|---|
| Conventions communes du dépôt et conventions de la veille technologique | [`CLAUDE.md` du dépôt](../CLAUDE.md) |
| Place du corpus dans le dépôt, ordre de lecture, divergences factuelles entre volumes | [README du dépôt](../README.md) |
| Synthèse consolidée des trois monographies | [`README.md` de ce dossier](README.md) |
| Vol. I — *Interopérabilité agentique* | [`1 - InteroperabiliteAgentique/CLAUDE.md`](1%20-%20InteroperabiliteAgentique/CLAUDE.md) |
| Vol. II — *L'autonomie encadrée* | [`2 - OrchestrationAgentique/CLAUDE.md`](2%20-%20OrchestrationAgentique/CLAUDE.md) |
| Vol. III — *L'entreprise agentique* | [`3 - EntrepriseAgentique/CLAUDE.md`](3%20-%20EntrepriseAgentique/CLAUDE.md) — et son [`README.md`](3%20-%20EntrepriseAgentique/README.md) au lecteur, déposé le 29 juillet 2026 |
| Vol. IV — *La somme agentique* (compendium, **50 chapitres rédigés hors portes, arrêté en révision finale**) | [`../2 - Compendium/CLAUDE.md`](../2%20-%20Compendium/CLAUDE.md) |

> [!IMPORTANT]
> **Le fichier le plus spécifique gagne.** En travaillant dans un volume, appliquer son `CLAUDE.md`, pas celui-ci. Ce fichier n'intervient que pour le `README.md` du dossier et pour les questions qui touchent **plusieurs volumes à la fois**.

---

## Ce que ce dossier contient — et ne contient pas

Le dossier `1 - Corpus/` est un **conteneur** : il ne porte aucun chapitre, aucun socle factuel, aucun pipeline de rendu. Il contient :

- **Trois sous-dossiers** — un par volume du triptyque (`1 - InteroperabiliteAgentique/`, `2 - OrchestrationAgentique/`, `3 - EntrepriseAgentique/`) ;
- **Un `README.md`** — la synthèse consolidée des trois monographies ;
- **Ce `CLAUDE.md`** — les conventions du conteneur.

Aucun livrable rédigé ne vit à ce niveau. Le `README.md` est un **document dérivé** : il synthétise les trois monographies mais ne leur ajoute aucun fait, aucune thèse ni aucune recommandation qui ne figure déjà dans au moins un volume.

---

## Le `README.md` — synthèse consolidée

### Nature

Le `README.md` de ce dossier est une **synthèse consolidée** des trois monographies, destinée au lecteur qui souhaite comprendre le corpus dans son ensemble avant d'entrer dans un volume. Il articule les trois thèses, les concepts transversaux, les protocoles et standards, les recommandations consolidées et les parcours de lecture.

### Règles de rédaction

- **Document dérivé, jamais source.** Le `README.md` ne crée pas de faits : il les extrait des trois monographies. Toute affirmation qui y figure doit être traçable à au moins un volume. Ne jamais y ajouter une thèse, un concept ou une recommandation sans siège dans un volume.
- **Cohérence avec les volumes.** Les décomptes (pages, pièces, mots, entrées de socle) sont ceux annoncés par chaque volume dans son propre `README.md` ou `CLAUDE.md`. En cas de divergence, le chiffre du volume source fait foi — corriger le `README.md` du corpus, pas celui du volume.
- **Cohérence avec le `README.md` du dépôt.** Le [`README.md` du dépôt](../README.md) porte ses propres décomptes, re-mesurés sur pièce. Les deux fichiers peuvent diverger de formulation mais pas de chiffres : si un décompte change dans un volume, le reporter dans les deux `README.md` (dépôt et corpus).
- **Pas de doublon avec le `README.md` du dépôt.** Le `README.md` du dépôt situe les volumes, traite les divergences factuelles, l'ordre de lecture, les pipelines de rendu et la maintenance. Le `README.md` du corpus se concentre sur le **contenu intellectuel** : thèses, concepts, protocoles, recommandations. Ne pas y dupliquer les sections de maintenance, de construction PDF ou de divergences factuelles.
- **Langue.** Français canadien soutenu, ton professionnel et neutre — mêmes conventions que le reste du dépôt. Terminologie technique anglaise entre parenthèses à la première occurrence.
- **Diagrammes Mermaid.** Le `README.md` contient des diagrammes Mermaid pour visualiser les relations entre volumes et le flux identitaire. Ils sont rendus nativement par GitHub ; aucun pré-rendu n'est nécessaire.

### Décomptes à tenir synchronisés

Les chiffres suivants sont annoncés dans le `README.md` du corpus et doivent être **re-mesurés** (jamais recopiés) à chaque modification d'un volume. Sources de vérité, par ordre :

| Décompte | Source de vérité | Sièges dérivés |
|---|---|---|
| Pages du Vol. I (569 p.) | `Monographie.pdf` du Vol. I | README corpus, README dépôt |
| Pages du Vol. II (387 p.) | `Monographie.pdf` du Vol. II | README corpus, README dépôt |
| Pages du Vol. III (427 p.) | `Monographie.pdf` du Vol. III | README corpus, README dépôt |
| Mots du Vol. I (≈ 263 600) | `Monographie.md` du Vol. I (re-mesuré, aucun `CLAUDE.md` ne le porte) | README corpus, README dépôt |
| Mots du Vol. II (92 059) | `CLAUDE.md` du Vol. II | README corpus, README dépôt |
| Mots du Vol. III (≈ 160 900) | `CLAUDE.md` du Vol. III | README corpus, README dépôt |
| Pièces du Vol. II (29) | `monographie/` du Vol. II | README corpus, README dépôt |
| Pièces du Vol. III (34) | `monographie/` du Vol. III | README corpus, README dépôt |
| Entrées de socle Vol. II (46) | `prd/PRD.md` du Vol. II (F-01 à F-48, F-12–F-14 non attribués, + F-23b) | README corpus, README dépôt |
| Entrées de socle Vol. III (98 propres + 33 héritées) | `prd/PRD.md` du Vol. III (F-01 à F-98 propres + H-01 à H-33) | README corpus, README dépôt |
| Diagrammes Mermaid Vol. I (28) | `grep -c '^```mermaid' Monographie.md` (motif **ancré**) | README corpus, README dépôt |
| **Total du corpus (1 383 p. / ≈ 516 500 mots / 70 pièces / 144 entrées codifiées)** | Re-mesure combinée | README corpus, README dépôt |

> [!NOTE]
> **Règle de comptage des diagrammes**
> Le décompte des diagrammes du Vol. I se mesure avec un motif ancré : `grep -c '^```mermaid'` donne 28. Le motif non ancré en retourne 29 (il attrape une ligne de prose qui cite la balise dans la note de production).

---

## Les trois volumes — statuts et conventions

### Divergences de conventions entre volumes — ne pas uniformiser

Les volumes portent des conventions qui **divergent volontairement**. Les corriger « pour la cohérence » casserait des références croisées ou l'historique d'un volume. Voir le [`CLAUDE.md` du dépôt](../CLAUDE.md) pour le tableau complet.

| | Vol. I | Vol. II | Vol. III |
|---|---|---|---|
| **Commits** | courts, en français | Conventional Commits en anglais | Conventional Commits en anglais |
| **Autorité de contenu** | conventions de chapitres du `CLAUDE.md` | le **PRD** (`prd/PRD.md`) | le **PRD** (`prd/PRD.md`) |
| **Traçabilité des faits** | vérification adverse des citations | socle F-xx, niveaux [A]/[B]/[C] | socle F-xx + héritage codifié |
| **Garde-fous** | — | R-1 à R-8 (un chiffre) | R-01 à R-14 (deux chiffres) |
| **Pipeline PDF** | FESP (Mermaid → Pandoc → Typst) | copie FESP + `assemble.py` | copie FESP + `assemble.py` |

> [!NOTE]
> **Indépendance des pipelines PDF**
> Les trois pipelines PDF sont des copies indépendantes : un correctif apporté à l'un ne se propage pas automatiquement aux autres.

### États au dépôt final — re-mesurés sur pièce le 29 juillet 2026

| Volume | État | Pages | Mots |
|---|---|---|---|
| **Vol. I** | Rédaction terminée, PDF final | **569 p.** | **≈ 263 600** |
| **Vol. II** | Publié (millésime éditorial `mono-v1.0`, étiquette git **non posée**) | **387 p.** | **92 059** |
| **Vol. III** | Rédigé, **non publiable** — 15 remontées ouvertes (R-G-43 à R-G-57) | **427 p.** | **≈ 160 900** |

☑ **Les trois paginations ont été re-mesurées à cette date (`pypdf`) et sont inchangées depuis le
25 juillet 2026** ; les trois états sont inchangés eux aussi. ⚠ **Une re-mesure qui confirme n'est pas un
changement d'état** : le Vol. II reste sans étiquette git, et *rédigé ne vaut toujours pas publiable*
pour le Vol. III. **Le Vol. III porte désormais son propre [`README.md`](3%20-%20EntrepriseAgentique/README.md)**
— déposé le 29 juillet 2026, document dérivé sans fait neuf : c'est un **siège de décomptes
supplémentaire**, à mettre à jour avec ceux de la table ci-dessus.

### Filiation et héritage entre volumes

Le Vol. III hérite du socle des deux précédents, à deux régimes distincts :

- **Du Vol. II** : 16 entrées, à niveau conservé (même méthode de vérification).
- **Du Vol. I** : 17 entrées, abaissées à [C] (la vérification du Vol. I porte sur les références, non sur le contenu des affirmations).

⚠ **Ne pas confondre les deux régimes d'héritage** : une entrée du Vol. II conserve son [A]/[B]/[C] ; une entrée du Vol. I entre systématiquement en [C].

---

## Règles transversales

Ces règles valent pour le dossier `1 - Corpus/` et son `README.md`. Les règles communes à **tout le dépôt** sont au [`CLAUDE.md` du dépôt](../CLAUDE.md) ; celles de chaque volume, dans son propre `CLAUDE.md`.

- **PDF versionné avec sa source.** Vaut pour les trois volumes : régénérer et pousser le `.pdf` avec le `.md` — jamais la source seule.
- **Décomptes re-mesurés, jamais recopiés.** Un même chiffre vit à plusieurs endroits (README du dépôt, README du corpus, README et CLAUDE.md du volume, PRD, TOC). Les mettre à jour ensemble.
- **Divergences factuelles signalées, non arbitrées.** Deux faits datés divergent entre la veille et le Vol. II (date de la ligne directrice IA de l'AMF, gouvernance d'AP2) : le [`README.md` du dépôt](../README.md) les documente. **Ne pas les uniformiser en silence** ici.
- **Lacunes exposées, non comblées.** Aucune lacune déclarée d'un volume ne se comble par une source de moindre qualité — dans aucun document, y compris le `README.md` du corpus.
- **Langue.** Français canadien soutenu ; ton professionnel et neutre. Terminologie technique anglaise entre parenthèses à la première occurrence ; citations verbatim en langue originale.

---

## Fichiers retirés du dépôt — fait consigné, non corrigé

Trois catégories de fichiers ont été retirées du dépôt et restent citées par les volumes :

| Fichier | Date de retrait | Commit | Volumes citant |
|---|---|---|---|
| `Synthese Monographie.md` / `.pdf` (Vol. I et II) | 22 juillet 2026 | `fd8f1be` | Vol. III (100 occurrences sur 26 fichiers) |
| `index.html` (Vol. I et II) | 22 juillet 2026 | `fd8f1be` | — |
| `Borealis-Go/` (Vol. I) | 25 juillet 2026 | `60f57f6` | Veille (réf. [217]), Vol. III (6 occurrences sur 5 fichiers) |

> [!WARNING]
> **Règle relative aux fichiers retirés**
> Ne pas restaurer ces fichiers, ne pas réécrire les citations. Un renvoi exact vers un fichier absent reste exact ; il cesse seulement d'être opposable. Chaque volume porte la consignation détaillée dans son propre `CLAUDE.md`.

---

## Commandes utiles — vérifications inter-volumes

Depuis le dossier `1 - Corpus/` :

```bash
# Vérifier les paginations des trois PDF (Python cross-platform)
python -c "import pypdf; [print(f'{f}: {len(pypdf.PdfReader(f).pages)} p.') for f in ['1 - InteroperabiliteAgentique/Monographie.pdf', '2 - OrchestrationAgentique/Monographie.pdf', '3 - EntrepriseAgentique/Monographie.pdf']]"

# Compter les diagrammes Mermaid du Vol. I (motif ancré)
# En Bash / Linux / macOS :
grep -c '^```mermaid' "1 - InteroperabiliteAgentique/Monographie.md"

# En Python (cross-platform Windows PowerShell / Linux / macOS) :
python -c "import sys; sys.stdout.reconfigure(encoding='utf-8'); print(sum(1 for line in open('1 - InteroperabiliteAgentique/Monographie.md', encoding='utf-8') if line.startswith(chr(96)*3 + 'mermaid')))"

# Compter les pièces des Vol. II (29) et Vol. III (34)
python -c "import glob, os; print('Vol. II pièces:', sum(1 for f in glob.glob('2 - OrchestrationAgentique/monographie/**/*.md', recursive=True) if not os.path.basename(f).startswith(('README', '99-')))); print('Vol. III pièces:', sum(1 for f in glob.glob('3 - EntrepriseAgentique/monographie/**/*.md', recursive=True) if not os.path.basename(f).startswith(('README', '99-'))))"

# Mesurer le nombre total de mots du corpus (Python cross-platform)
python -c "import glob, re, os; print('Vol. I mots:', len(re.findall(r'\w+', open('1 - InteroperabiliteAgentique/Monographie.md', encoding='utf-8').read())))"
```
