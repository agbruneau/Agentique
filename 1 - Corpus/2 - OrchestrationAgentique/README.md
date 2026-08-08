# Volume II — « L'autonomie encadrée »

📖 **Lire :** [`Monographie.pdf`](Monographie.pdf) (387 p.) dans ce dossier. *(Le volume n'a plus de
page de présentation ni de publication GitHub Pages — voir « Structure du dossier ».)*

> **Où vous êtes.** Ce dossier est le **deuxième des trois volumes** du corpus, dans le dépôt
> [*Agentique*](../../README.md). Il **présuppose le volume I**
> ([`1 - InteroperabiliteAgentique/`](../1%20-%20InteroperabiliteAgentique/)) pour la théorie du
> découplage, l'ingénierie des agents LLM et l'anatomie des protocoles : le volume I illustre
> mondialement ce que celui-ci instruit au grain du droit canadien.

**Monographie exhaustive** sur l'interopérabilité et l'orchestration agentique en écosystème d'entreprise de services financiers au Canada — protocoles ouverts (MCP, A2A, AP2, AGNTCY), cadre réglementaire canadien (E-23, AMF, ACVM, cadre bancaire) et blueprint d'intégration d'entreprise. État des lieux 2024-2026.

| Champ | Valeur |
|---|---|
| Livrable | millésime **`mono-v1.0`** — publiée le 17 juillet 2026 (⚠ millésime éditorial : l'**étiquette git n'a pas été posée**) |
| Volumétrie | **92 059 mots**, 29 pièces (24 chapitres, avant-propos, annexes A-D) |
| Rendu | `Monographie.pdf` **387 p.** (article de synthèse retiré du dossier le 22 juillet 2026) |
| Gel de l'information | 16 juillet 2026 (22 pièces) · 17 juillet 2026 (7 pièces) |
| Socle factuel | **46 entrées** F-01 à F-48 (F-12 à F-14 non attribués ; F-23b) |
| Conformité | CA-1 à CA-8 |

☑ **Re-mesuré sur pièce le 29 juillet 2026**, à la passe de dépôt final du dépôt, et **inchangé** :
`Monographie.pdf` **387 p.** (`pypdf`), **29 pièces** sous `monographie/` (plus le registre des gels).
⚠ **Un point n'a pas bougé non plus, et il reste dû** : l'**étiquette git `mono-v1.0` n'est toujours pas
posée** alors que quatre documents de gouvernance l'annoncent comme telle — *un millésime éditorial n'est
pas un point de restauration*. Poser le tag ou corriger ces mentions est une décision d'auteur.

**Contribution la plus citable — un résultat négatif :** en croisant trois protocoles (MCP, A2A, AP2) et cinq corpus de textes canadiens, **aucun lien documenté par source primaire** — quinze croisements, zéro lien. D'où la thèse : sous exigence réglementaire stricte, le cadre déterministe invoque les agents, jamais l'inverse.

## Par où commencer

- **Lire la monographie** → [`monographie/README.md`](monographie/README.md) : index de lecture ordonné, à commencer par l'[avant-propos](monographie/00-avant-propos.md). Le [chapitre 13](monographie/03-partie-III/ch-13-pont-frames.md) en est le pivot.
- **PDF assemblé** → [`Monographie.pdf`](Monographie.pdf) (les 29 pièces reliées en un volume).

## Structure du dossier

| Chemin | Contenu |
|---|---|
| `monographie/` | Les 29 pièces, un fichier par chapitre (parties I-VII, annexes `90-annexes/`, registre des gels `99-registre-gel.md`) + son [index de lecture](monographie/README.md) |
| `prd/` | Documents de gouvernance et sources — [`PRD.md`](prd/PRD.md), [`PRDPlan.md`](prd/PRDPlan.md), [`TOC.md`](prd/TOC.md), [`audit.md`](prd/audit.md), et les deux PDF académiques du socle (F-36, F-37) |
| `verification/` | Rapports de revalidation ([16](verification/revalidation-2026-07-16.md), [17](verification/revalidation-2026-07-17.md) juillet 2026) et grille de conformité [CA-1..CA-8](verification/relecture-CA.md) |
| `build/` | Pipeline de rendu PDF (assemblage + Pandoc → Typst) |
| `Monographie.md` / `Monographie.pdf` | Assemblage versionné des 29 pièces et son rendu (387 p.) |

⚠ **`doc/` s'appelle désormais `prd/`** (renommage du 22 juillet 2026). Les deux déplacements du
dossier de gouvernance — racine → `doc/` le 17 juillet, `doc/` → `prd/` le 22 — avaient laissé des
renvois relatifs cassés dans tout le volume. ☑ **Repointés le 8 août 2026**, et re-vérifiés en
résolvant chaque cible sur disque : **48 dans `monographie/`** (bandeaux de thèse et renvois de corps
vers `TOC.md`, portés à `../../prd/TOC.md`), **dix-sept dans
`prd/audit.md`** (locateurs `fichier.md:ligne` préfixés `../` et convertis en ancres `#Lnnn`) et
**quatre dans `verification/relecture-CA.md`** (`../PRD.md`, `../PRDPlan.md`, `../audit.md` → `../prd/…`),
soit **69 renvois markdown**. ⚠ *Le chemin corrigé dans `build/assemble.py` — `ROOT / "TOC.md"` porté à
`ROOT / "prd" / "TOC.md"` — **n'est pas un renvoi** mais un chemin de système de fichiers : il est compté
à part, et ce fichier ne porte aucune cible de lien markdown.* ⚠ **Deux limites des ancres
`#Lnnn`** : elles portent le lecteur sur le bon fichier, mais GitHub n'honore le numéro de ligne que sur
la vue source (`?plain=1#Lnnn`), pas sur un `.md` rendu — *le renvoi cesse d'être mort sans redevenir
exact à la ligne.*
*(L'index de lecture [`monographie/README.md`](monographie/README.md) avait déjà été repointé le
25 juillet 2026.)*

⚠ **Un renvoi mort subsiste et il est hors de portée d'un correctif de lien** : `prd/PRDPlan.md`
renvoie à un `CLAUDE.md` (« conventions du dépôt ») **qui n'existe nulle part dans le dépôt**. Le
corriger demanderait de choisir une cible, ce qui n'est pas une opération de lien — décision d'auteur.

⚠ **Ni `index.html`, ni article de synthèse, ni publication GitHub Pages.** La page de présentation
et `Synthese Monographie.md` / `.pdf` (12 sections, 19 tableaux, ~26 500 mots ; 66 p.) ont été
retirés du dossier le 22 juillet 2026. Les adresses `https://agbruneau.github.io/Monographies/…`
annoncées auparavant étaient fausses de toute façon : le dépôt s'appelle
[`Agentique`](https://github.com/agbruneau/Agentique).

## Gouvernance

Documents par ordre d'autorité — **en cas de conflit, le PRD prime** :

1. [`PRD.md`](prd/PRD.md) — contenu, socle factuel, garde-fous (R-1..R-8), critères d'acceptation ;
2. [`PRDPlan.md`](prd/PRDPlan.md) — plan d'exécution et boucle qualité par chapitre (§4.2) ;
3. [`TOC.md`](prd/TOC.md) — titre, abstract, table des matières commentée.

Toute affirmation factuelle centrale est tracée à une entrée du socle F-xx avec son niveau de preuve — **[A]** vote adversarial 3-0 > **[B]** source primaire extraite > **[C]** repérage à confirmer.

## Régénérer le PDF

Après toute modification des chapitres, **depuis ce dossier** :

```bash
python build/assemble.py            # concatène monographie/ → Monographie.md
bash   build/build-pdf.sh Monographie.md   # → Monographie.pdf (US-letter, gabarit build/fesp.template)
```

☑ **L'assemblage remarche** (8 août 2026). `build/assemble.py` cherchait `TOC.md` à la racine du volume
alors qu'il vit dans `prd/` depuis le 22 juillet 2026 : il levait un `FileNotFoundError` avant d'écrire
une ligne. Il lit désormais `prd/TOC.md`, comme l'assembleur du Vol. III. **Réexécuté : `38 blocs, 853 Ko`,
et la sortie reproduit `Monographie.md` à l'octet près** — la panne était dans le chemin seul, pas dans le
contenu produit.

⚠ **L'assembleur rebase désormais les liens relatifs des pièces.** Une pièce de
`monographie/03-partie-III/` renvoie à `../../prd/TOC.md` ; concaténée dans `Monographie.md`, à la racine
du volume, cette cible ne résolvait plus. Le script réécrit chaque cible relative depuis le répertoire de
la pièce — **12 renvois morts de moins dans `Monographie.md`**, et aucune ligne de prose touchée.

## Avertissements

- **Aucun avis juridique ni conseil d'investissement** : l'ouvrage rapporte des textes et en propose des lectures d'architecture qui engagent l'auteur seul.
- **Aucune recommandation de fournisseur** : la Partie VII instancie le blueprint sur le portefeuille d'IBM à titre de cas documenté, pas de verdict comparatif.
- **L'ouvrage se périme par morceaux** : chaque pièce porte sa date de gel ; les échéances de revalidation sont suivies au [chapitre 24](monographie/07-partie-VII/ch-24-lacunes-revalidation.md).
- **Onze lacunes ouvertes** sont exposées plutôt que comblées ([chapitre 21](monographie/06-partie-VI/ch-21-frontiere.md)).
