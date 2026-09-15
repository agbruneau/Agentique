# Journal — `1 - Collection/2 - OrchestrationAgentique/`

Ce fichier reçoit, sans un mot changé, les deux pages d'accueil de ce dossier et de ses sous-dossiers non numérotés telles qu'elles étaient écrites au commit `5cdb5bb` du
15 septembre 2026 : la chronique datée — clôtures, réouvertures, redatations, corrections de corrections — et tout ce qui
l'entourait, tables et cartes comprises. Un chiffre y vaut à la date qui l'accompagne ; un présent, au jour où il a été écrit ;
un « ci-dessous » ou un « en tête », à la page d'où il vient.

Seules les cibles de lien ont bougé, et seulement celles qui seraient mortes : elles visent ce qui existe depuis ce dossier.
Le texte d'origine se relit par `git show 5cdb5bb:"1 - Collection/2 - OrchestrationAgentique/<page>"`, `<page>` étant le chemin que la table ci-dessous donne. Trois dossiers ont changé de nom le 5 septembre 2026 — `3 - Traité/` est
`4 - Essais/1 - Traité/`, `4 - Veille/` est `3 - Veille/`, `6 - Article/` est `4 - Essais/2 - Article/` — et un chemin écrit
avant cette date garde son ancien nom. L'état courant est à [`README.md`](README.md) et aux pages qu'il nomme ; une passe nouvelle s'ajoute à la fin de ce fichier,
datée, et rien de ce qui précède ne s'y corrige.

| Page reçue | Lignes | Sections |
|---|---|---|
| [`README.md`](#page-readme) | 142 | [Par où commencer](#par-où-commencer) · [Structure du dossier](#structure-du-dossier) · [Gouvernance](#gouvernance) · [Régénérer le PDF](#régénérer-le-pdf) · [Avertissements](#avertissements) |
| [`monographie/README.md`](#page-monographie) | 92 | [Ordre de lecture](#ordre-de-lecture) · [Avertissements](#avertissements-1) · [Comment cet ouvrage a été vérifié](#comment-cet-ouvrage-a-été-vérifié) · [Gouvernance](#gouvernance-1) |

<a id="page-readme"></a>

---

*Page reçue : `README.md`, 142 lignes au commit `5cdb5bb`.*

# Volume II — « Orchestration agentique »

📖 **Lire :** [`Monographie.pdf`](Monographie.pdf) (387 p.) dans ce dossier. *(Le volume n'a plus de
page de présentation ni de publication GitHub Pages — voir « Structure du dossier ».)*

> **Livrable** — un des sept que fixe la décision d'auteur [**D-18**](../../2%20-%20Compendium/PRD/PRD.md#d-18) du 15 septembre 2026 ([registre](../../README.md#les-sept-livrables)) ; dépôt **rouvert** le même jour par [D-17](../../2%20-%20Compendium/PRD/PRD.md#d-17), re-clôture prévue vers le 8 décembre 2026. *Le bandeau de clôture plus bas reste à sa date.*

> ⚠ **Le volume a été renommé le 8 août 2026** : *« L'autonomie encadrée »* du 17 juillet au 8 août
> 2026, **« Orchestration agentique »** depuis. ⚠ *Le titre change, la thèse ne change pas* :
> l'**autonomie encadrée** (*framed autonomy*) reste la thèse centrale de l'ouvrage, exposée au
> chapitre 6 et instruite au chapitre 13 — elle cesse seulement d'en être l'intitulé. Le nouveau
> titre est celui du dossier depuis l'origine. ⚠ *La proximité de dénomination signalée ici visait le
> **Vol. IV**, dont le titre a été, du 9 au 21 août 2026, **exactement** celui de la veille
> technologique : citer l'un des deux par son seul intitulé ne désignait alors rien.* ☑ **L'homonymie
> est levée en deux temps, et aucun des deux ne touche ce volume-ci** : l'**échange titre/sous-titre
> du 21 août 2026** donne à la veille « Veille technologique en entreprise » pour titre et renvoie le
> nom commun au sous-titre de série ; la **révision du 25 août 2026** porte le Vol. IV à
> « Interopérabilité et Orchestration en Entreprise Agentique ». *Les deux se citent désormais par
> leur seul intitulé.*

> ✎ *Rouvert le 15 septembre 2026 par D-17 — voir le statut en tête ; ce bandeau reste à sa date.*
> ⚠ **Dépôt clos et final — clôture portée au 1er septembre 2026** — décision d'auteur **D-13**, prise le 8 août 2026
> ([`2 - Compendium/PRD/PRD.md`](../../2%20-%20Compendium/PRD/PRD.md) v0.17 §16). Aucune passe
> n'est plus prévue, sur ce volume ni sur aucun autre du dépôt : ce qui suit décrit un état
> **définitif**. ⚠ *Clore n'est ni terminer ni publier* — rien n'est levé, rien n'est soldé, et
> ce qui restait dû devient un **manque définitif, daté et écrit**.
>
> ⚠ **La date de clôture a porté « 8 août 2026 » jusqu'au 3 septembre 2026, et elle confondait deux choses** : *une décision se date de sa prise, une clôture de l'état qu'elle arrête.* **D-13 reste prise le 8 août 2026** ; **la clôture court du 1er septembre 2026**, dernier jour où une pièce est entrée au dépôt — l'article entré au commit `da6255b` dans `6 - Article/`, *dossier porté sous `4 - Essais/2 - Article/` par la réorganisation du 5 septembre 2026 (commit `daacbec`)*. ⚠ *La passe d'audit et de fond du 2 septembre 2026 (D-15, D-16) lui est postérieure d'un jour : elle porte sur l'appareil, le plan et le domaine de livraison du Vol. IV, et **aucune pièce n'y entre ni n'en sort**.* Motif complet au **PRD §16.5**.

> **Où vous êtes.** Ce dossier est le **deuxième des trois volumes** du corpus, dans le dépôt
> [*Agentique*](../../README.md). Il **présuppose le volume I**
> ([`1 - InteroperabiliteAgentique/`](../1%20-%20InteroperabiliteAgentique/)) pour la théorie du
> découplage, l'ingénierie des agents LLM et l'anatomie des protocoles : le volume I illustre
> mondialement ce que celui-ci instruit au grain du droit canadien.

**Monographie exhaustive** sur l'interopérabilité et l'orchestration agentique en écosystème d'entreprise de services financiers au Canada — protocoles ouverts (MCP, A2A, AP2, AGNTCY), cadre réglementaire canadien (E-23, AMF, ACVM, cadre bancaire) et blueprint d'intégration d'entreprise. État des lieux 2024-2026.

| Champ | Valeur |
|---|---|
| Livrable | millésime **`mono-v1.0`** — publiée le 17 juillet 2026 ; ☑ **l'étiquette git `mono-v1.0` est posée le 8 août 2026, au commit où D-13 est prise** (décision d'auteur, passe D-13). ⚠ *Elle l'a été vingt-deux jours après le millésime éditorial qu'elle nomme, et elle marque donc l'arbre du 8 août, non l'arbre du 17 juillet : `git show mono-v1.0` le montre.* ⚠⚠ **Et elle ne marque pas davantage l'arbre clos** : *la clôture est portée au 1er septembre 2026* — l'étiquette est restée sur l'arbre de la prise, et **aucune étiquette ne porte l'état arrêté**. Les documents de gouvernance du volume qui l'annonçaient posée depuis juillet **cessent d'être faux sans devenir exacts pour autant** |
| Volumétrie | **92 056 mots**, 29 pièces (24 chapitres, avant-propos, annexes A-D) — commande de référence [PRDPlan §4.2](prd/PRDPlan.md) (corps borné, jetons alphanumériques, locale C), rejouée sur les 29 pièces le 10 août 2026. ⚠ **92 059 au 17 juillet 2026**, chiffre que l'[index de lecture](monographie/README.md) porte encore à sa date : le commit `659241b` a retiré **trois jetons du corps** de trois pièces (§ 6.2, § 13.2, glossaire de l'annexe D) au renommage du volume — *l'écart touche les deux commandes de décompte, non la seule `decompte.sh`* |
| Rendu | `Monographie.pdf` **387 p.** (article de synthèse retiré du dossier le 22 juillet 2026) |
| Gel de l'information | 16 juillet 2026 (22 pièces) · 17 juillet 2026 (7 pièces) |
| Socle factuel | **46 entrées** F-01 à F-48 (F-12 à F-14 non attribués ; F-23b) |
| Conformité | CA-1 à CA-8 |

☑ **Re-mesuré sur pièce le 29 juillet 2026**, à la passe de dépôt final du dépôt, et **inchangé** :
`Monographie.pdf` **387 p.** (`pypdf`), **29 pièces** sous `monographie/` (plus le registre des gels).
⚠ **Un point n'avait pas bougé non plus et restait dû à cette date** : l'**étiquette git `mono-v1.0`
n'était alors pas posée** alors que quatre documents de gouvernance l'annonçaient comme telle — *un
millésime éditorial n'est pas un point de restauration*. ☑ **Le constat est dépassé depuis le 8 août
2026** : l'étiquette est posée au commit où D-13 est prise (`git tag -l` la rend), et la ligne
« Livrable » ci-dessus porte la réserve qui subsiste — *elle marque l'arbre du 8 août, ni celui du
17 juillet, ni l'arbre clos : la clôture est portée au 1er septembre 2026, et **aucune étiquette ne
porte l'état arrêté**.*

**Contribution la plus citable — un résultat négatif :** en croisant trois protocoles (MCP, A2A, AP2) et cinq corpus de textes canadiens, **aucun lien documenté par source primaire** — quinze croisements, zéro lien. D'où la thèse : sous exigence réglementaire stricte, le cadre déterministe invoque les agents, jamais l'inverse.

## Par où commencer

- **Lire la monographie** → [`monographie/README.md`](monographie/README.md) : index de lecture ordonné, à commencer par l'[avant-propos](monographie/00-avant-propos.md). Le [chapitre 13](monographie/03-partie-III/ch-13-pont-frames.md) en est le pivot.
- **PDF assemblé** → [`Monographie.pdf`](Monographie.pdf) (les 29 pièces reliées en un volume).

## Structure du dossier

| Chemin | Contenu |
|---|---|
| `README.md` | ce fichier — présentation du volume |
| `monographie/` | Les 29 pièces, un fichier par chapitre (parties I-VII, annexes `90-annexes/`, registre des gels `99-registre-gel.md`) + son [index de lecture](monographie/README.md) |
| `prd/` | Documents de gouvernance et sources — [`PRD.md`](prd/PRD.md), [`PRDPlan.md`](prd/PRDPlan.md), [`TOC.md`](prd/TOC.md), [le rapport de vérification globale](prd/audit.md), et les deux PDF académiques du socle (F-36, F-37) |
| `verification/` | Rapports de revalidation ([16](verification/revalidation-2026-07-16.md), [17](verification/revalidation-2026-07-17.md) juillet 2026) et grille de conformité [CA-1..CA-8](verification/relecture-CA.md) |
| `build/` | Pipeline de rendu PDF (assemblage + Pandoc → Typst) |
| `Monographie.md` / `Monographie.pdf` | Assemblage versionné des 29 pièces et son rendu (387 p.) |
| `.gitignore` | — |

⚠ **`doc/` s'appelle désormais `prd/`** (renommage du 22 juillet 2026). Les deux déplacements du
dossier de gouvernance — racine → `doc/` le 17 juillet, `doc/` → `prd/` le 22 — avaient laissé des
renvois relatifs cassés dans tout le volume. ☑ **Repointés le 8 août 2026**, et re-vérifiés en
résolvant chaque cible sur disque : **48 dans `monographie/`** (bandeaux de thèse et renvois de corps
vers `TOC.md`, portés à `../../prd/TOC.md`), **seize dans
`prd/audit.md`** (locateurs `fichier.md:ligne` préfixés `../` et convertis en ancres `#Lnnn`) et
**quatre dans `verification/relecture-CA.md`** (`../PRD.md`, `../PRDPlan.md`, `../audit.md` → `../prd/…`),
soit **68 renvois markdown**. ⚠ **Ce que ce cardinal compte, faute de quoi il ne se reproduit pas** :
des **occurrences de lien markdown `[…](cible)` dont la cible est relative**, et non des cibles
distinctes — `relecture-CA.md` vise `../prd/audit.md` deux fois, ce qui fait quatre occurrences pour
trois fichiers visés. Sont **hors décompte** les liens de même répertoire, qui n'ont jamais eu de
préfixe à corriger : `prd/audit.md` en porte un vers `TOC.md#L155`, et le compter donnerait dix-sept.
L'index de lecture est hors décompte lui aussi, pour la raison datée plus bas. ⚠ *Le chemin corrigé dans `build/assemble.py` — `ROOT / "TOC.md"` porté à
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

Toute affirmation factuelle centrale est tracée à une entrée du socle F-xx avec son niveau de preuve — **[A]** vote adversarial 3-0 > **[B]** source primaire extraite > **[C]** repérage à confirmer. *Échelle réformée le 15 septembre 2026 : **[H]**, lu et non réfuté par un relecteur humain nommé, prend la tête — aucune entrée ne le porte — et « [A] » se lit **[A-i]**, réfutation tentée par trois instances de modèle ([PRD §7](prd/PRD.md), annexe A §A.9 de la monographie).*

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

<a id="page-monographie"></a>

---

*Page reçue : `monographie/README.md`, 92 lignes au commit `5cdb5bb`.*

# Orchestration agentique

> **Livrable** (Vol. II) — un des sept que fixe la décision d'auteur [**D-18**](../../2%20-%20Compendium/PRD/PRD.md#d-18) du 15 septembre 2026 ([registre](../../README.md#les-sept-livrables)) ; dépôt **rouvert** le même jour par [D-17](../../2%20-%20Compendium/PRD/PRD.md#d-17), re-clôture prévue vers le 8 décembre 2026. *Le bandeau de clôture qui suit reste à sa date.*

> ⚠ **Dépôt clos et final — clôture portée au 1er septembre 2026** — décision d'auteur **D-13**, prise le 8 août 2026
> ([`2 - Compendium/PRD/PRD.md`](../../2%20-%20Compendium/PRD/PRD.md) v0.17 §16). Aucune passe
> n'est plus prévue : ce qui suit décrit un état **définitif**.
>
> ⚠ **La date de clôture a porté « 8 août 2026 » jusqu'au 3 septembre 2026, et elle confondait deux choses** : *une décision se date de sa prise, une clôture de l'état qu'elle arrête.* **D-13 reste prise le 8 août 2026** ; **la clôture court du 1er septembre 2026**, dernier jour où une pièce est entrée au dépôt — l'article entré au commit `da6255b` dans `6 - Article/`, *dossier porté sous `4 - Essais/2 - Article/` par la réorganisation du 5 septembre 2026 (commit `daacbec`)*. ⚠ *La passe d'audit et de fond du 2 septembre 2026 (D-15, D-16) lui est postérieure d'un jour : elle porte sur l'appareil, le plan et le domaine de livraison du Vol. IV, et **aucune pièce n'y entre ni n'en sort**.* Motif complet au **PRD §16.5**.

**Interopérabilité et orchestration agentique dans les services financiers canadiens — protocoles ouverts, cadre réglementaire et blueprint d'intégration d'entreprise (état des lieux 2024-2026)**

| Champ | Valeur |
|---|---|
| Version | millésime **`mono-v1.0`** — millésime éditorial du 17 juillet 2026 ; ☑ **l'étiquette git du même nom est posée le 8 août 2026**, au commit où D-13 est prise. ⚠ *Elle marque donc l'arbre du 8 août, non celui du 17 juillet — ni l'arbre clos, la clôture étant portée au 1er septembre 2026* |
| Date de publication | 17 juillet 2026 |
| Dates de gel | 16 juillet 2026 (22 pièces) ; 17 juillet 2026 (7 pièces) — registre : [`99-registre-gel.md`](monographie/99-registre-gel.md) |
| Volumétrie | **92 059 mots** sur 29 pièces — mesure du 17 juillet 2026, après la passe corrective de l'[audit global](prd/audit.md) (méthode et commande de référence : [PRDPlan §4.2](prd/PRDPlan.md), dont le défaut connu y est documenté) |
| Socle factuel | **46 entrées** F-01 à F-48 ([PRD §7](prd/PRD.md)) |
| Conformité | **CA-1 à CA-8 : 8/8** — ⚠ **partiellement démenti** par la vérification du 17 juillet 2026 (CA-1 et CA-7 portaient des écarts, depuis corrigés) : voir l'addendum de [`verification/relecture-CA.md`](verification/relecture-CA.md) |
| Revalidation | 17 juillet 2026 ([`verification/revalidation-2026-07-17.md`](verification/revalidation-2026-07-17.md)) |

**Commencer par l'[avant-propos](monographie/00-avant-propos.md).** Il expose la méthode, les niveaux de preuve, la convention de datation et les avertissements — sans lesquels les chapitres se lisent mal. Le **[chapitre 13](monographie/03-partie-III/ch-13-pont-frames.md)** est le pivot de l'ouvrage : c'est le chapitre à contester en premier.

---

## Ordre de lecture

| # | Pièce | Fichier |
|---|---|---|
| — | **Avant-propos et note méthodologique** | [`00-avant-propos.md`](monographie/00-avant-propos.md) |
| | **Partie I — Fondements : les protocoles d'interopérabilité agentique** | |
| 1 | Généalogie et gouvernance : des projets propriétaires aux standards ouverts | [`ch-01`](monographie/01-partie-I/ch-01-genealogie-gouvernance.md) |
| 2 | Anatomie technique : MCP et A2A v1.0, une complémentarité déclarée | [`ch-02`](monographie/01-partie-I/ch-02-anatomie-mcp-a2a.md) |
| 3 | La transaction agentique et la couche d'infrastructure : AP2 et AGNTCY | [`ch-03`](monographie/01-partie-I/ch-03-ap2-agntcy-acp.md) |
| 4 | Taxonomie des risques protocolaires | [`ch-04`](monographie/01-partie-I/ch-04-risques-protocolaires.md) |
| | **Partie II — L'orchestration multi-agents en entreprise** | |
| 5 | Les options d'orchestration : la taxonomie OO1–OO4 | [`ch-05`](monographie/02-partie-II/ch-05-options-orchestration.md) |
| 6 | L'autonomie encadrée : le paradigme APM | [`ch-06`](monographie/02-partie-II/ch-06-autonomie-encadree.md) |
| 7 | Réalisations : les frameworks d'orchestration d'entreprise | [`ch-07`](monographie/02-partie-II/ch-07-frameworks.md) |
| 8 | L'identité et les registres d'agents | [`ch-08`](monographie/02-partie-II/ch-08-identite-registres.md) |
| | **Partie III — Le cadre réglementaire canadien** | |
| 9 | E-23 : le risque de modèle à l'ère de l'IA | [`ch-09`](monographie/03-partie-III/ch-09-e23-risque-modele.md) |
| 10 | Le vide fédéral : de C-27 à C-36 | [`ch-10`](monographie/03-partie-III/ch-10-vide-federal-c36.md) |
| 11 | Québec : la ligne directrice IA de l'AMF et l'article 12.1 de la Loi 25 | [`ch-11`](monographie/03-partie-III/ch-11-quebec-amf-loi25.md) |
| 12 | Valeurs mobilières : l'avis ACVM 11-348 | [`ch-12`](monographie/03-partie-III/ch-12-acvm-11-348.md) |
| **13** | **Le pont : des contraintes réglementaires aux frames déterministes** *(pivot)* | [`ch-13`](monographie/03-partie-III/ch-13-pont-frames.md) |
| | **Partie IV — L'interopérabilité financière canadienne** | |
| 14 | Le cadre des services bancaires axés sur le consommateur | [`ch-14`](monographie/04-partie-IV/ch-14-cadre-bancaire.md) |
| 15 | ISO 20022 : Lynx accompli, RTR imminent | [`ch-15`](monographie/04-partie-IV/ch-15-iso20022-lynx-rtr.md) |
| 16 | Prospective : AP2 sur les rails canadiens ? | [`ch-16`](monographie/04-partie-IV/ch-16-ap2-rails.md) |
| | **Partie V — L'adoption par les institutions financières canadiennes** | |
| 17 | Études de cas : la production agentique canadienne (2025-2026) | [`ch-17`](monographie/05-partie-V/ch-17-etudes-de-cas.md) |
| | **Partie VI — Synthèse : l'architecture de référence** | |
| 18 | La matrice protocoles × exigences réglementaires | [`ch-18`](monographie/06-partie-VI/ch-18-matrice.md) |
| 19 | L'architecture de référence par couches | [`ch-19`](monographie/06-partie-VI/ch-19-architecture-reference.md) |
| 20 | Instrumentation et feuille de route vers le 1er mai 2027 | [`ch-20`](monographie/06-partie-VI/ch-20-instrumentation-feuille-route.md) |
| 21 | La frontière de la connaissance vérifiable | [`ch-21`](monographie/06-partie-VI/ch-21-frontiere.md) |
| | **Partie VII — Le blueprint : plateforme d'intégration d'entreprise (instanciation IBM)** | |
| 22 | Principes directeurs et vue en couches (C1–C8) | [`ch-22`](monographie/07-partie-VII/ch-22-principes-couches.md) |
| 23 | Correspondance réglementaire et flux illustratifs | [`ch-23`](monographie/07-partie-VII/ch-23-correspondance-flux.md) |
| 24 | Lacunes du blueprint et conditions de revalidation | [`ch-24`](monographie/07-partie-VII/ch-24-lacunes-revalidation.md) |
| | **Annexes** | |
| A | Méthodologie de constitution du socle | [`annexe-a`](monographie/90-annexes/annexe-a-methodologie.md) |
| B | Matrice détaillée protocoles × réglementation | [`annexe-b`](monographie/90-annexes/annexe-b-matrice.md) |
| C | Chronologie réglementaire et normative 2023-2027 | [`annexe-c`](monographie/90-annexes/annexe-c-chronologie.md) |
| D | Glossaire bilingue — **§D.1 et §D.7 font autorité** | [`annexe-d`](monographie/90-annexes/annexe-d-glossaire.md) |

---

## Avertissements

Ils sont développés dans l'[avant-propos](monographie/00-avant-propos.md) ; en voici la substance.

- **Aucun avis juridique, aucun conseil d'investissement.** L'ouvrage rapporte des textes et en propose des lectures d'architecture. Ces lectures engagent l'auteur, jamais le régulateur.
- **Aucune recommandation de fournisseur.** La Partie VII instancie un blueprint sur le portefeuille d'IBM : c'est un **cas documenté par sources primaires**, retenu parce que sa documentation publique permettait de tracer chaque composant. Ce n'est pas un verdict comparatif.
- **L'ouvrage se périme par morceaux.** Chaque pièce porte sa date de gel. Une révision majeure de la spécification MCP est confirmée pour le **28 juillet 2026** — douze jours après le gel des chapitres 1, 2 et 7, qui décrivent donc en connaissance de cause un état déjà daté. Les conditions de péremption et le protocole de revalidation sont au [chapitre 24](monographie/07-partie-VII/ch-24-lacunes-revalidation.md).
- **Onze lacunes ouvertes** sont exposées plutôt que comblées ([chapitre 21](monographie/06-partie-VI/ch-21-frontiere.md)). La plus coûteuse : le contenu de la ligne directrice sur l'IA de l'AMF n'est pas au socle, et l'ouvrage n'en dérive aucune contrainte.

## Comment cet ouvrage a été vérifié

Chaque affirmation factuelle centrale renvoie à une entrée du socle (F-xx), et chaque entrée porte son niveau de preuve : **[A]** vote adversarial 3-0, **[B]** source primaire lue et extraite sans vote, **[C]** repérage à confirmer. **[A] > [B] > [C]** — le niveau ne mesure pas la qualité de la source, mais **ce que l'affirmation a subi**. *Échelle réformée le 15 septembre 2026 : « [A] » se lit **[A-i]** — les trois votants sont des instances de modèle — et **[H]**, lu et non réfuté par un relecteur humain nommé, prend la tête sans qu'aucune entrée le porte ([annexe A, §A.9](monographie/90-annexes/annexe-a-methodologie.md)).*

Les 29 pièces ont chacune passé la boucle qualité de [PRDPlan §4.2](prd/PRDPlan.md), dont une **relecture adversariale par un relecteur distinct du rédacteur**. La grille [CA-1..CA-8](verification/relecture-CA.md) consigne les contrôles exécutés — et les écarts qu'ils ont trouvés, corrigés plutôt qu'absorbés.

Un résultat de cette vérification mérite d'être donné au lecteur, parce qu'il dit ce que vaut le reste : **tous les défauts lourds trouvés à la publication l'ont été par des relecteurs adversariaux, aucun par l'auto-contrôle de leur rédacteur.**

## Gouvernance

[`prd/PRD.md`](prd/PRD.md) (autorité de contenu — socle, garde-fous, critères) · [`prd/PRDPlan.md`](prd/PRDPlan.md) (exécution) · [`prd/TOC.md`](prd/TOC.md) (découpage, thèses, volumétrie). En cas de conflit, **le PRD prime**.

Ce fichier est l'**index de lecture** des 29 pièces, et rien d'autre : la gouvernance, le pipeline de rendu et la procédure de reprise sont au [`README.md`](README.md) du volume ; la place du volume dans le corpus est au [README du dépôt](../../README.md).
