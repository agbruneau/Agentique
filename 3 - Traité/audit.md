# Audit intégral du dossier `3 - Traité` et plan d'exécution des correctifs

*Audit conduit le 2 septembre 2026 sur l'arbre de travail du dépôt (branche `main`, dernier commit `7f0d810`). Périmètre : le dossier `3 - Traité/` en totalité — le traité (`Traité.md` / `Traité.pdf`, 19 figures), le simulateur `stigmergie-lab` (quatre crates, deux bancs, un binaire de campagne), ses six documents de gouvernance sous `docs/`, ses trois verdicts de banc, son appareil de contrôle (`Python/check-traite.py`, `build/build-pdf.sh`, `figures/`), ses deux fichiers d'accueil (`README.md`, `CLAUDE.md`) et l'empaquetage web. Le dossier est entré au dépôt le 14 août 2026 ; il vivait auparavant comme dépôt autonome.*

---

## 1. Résumé

**Ce dossier tient ce qu'il déclare, et c'est le premier résultat de l'audit.** Sa règle centrale — *tout chiffre affiché doit être retrouvé par la mesure, ou l'écart doit être consigné* (NF-15) — a été appliquée à ses propres cardinaux, et **ils se reproduisent** :

| Ce que le dossier déclare | Ce que la mesure rend | Verdict |
|---|---|---|
| 467 tests, 0 échec — 254 / 96 / 68 / 6 unitaires, 43 d'intégration | `cargo test --workspace --release` : **467 passés, 0 échec**, ventilation identique | ☑ |
| `clippy` 0, `cargo doc` 0 | sorties **0** et **0** | ☑ |
| `Traité.pdf` : 143 pages, 3ᵉ édition du 15 août 2026 | 143 pages ; **le PDF refait depuis `Traité.md` est identique, page à page, texte à texte** | ☑ |
| 123 notices, toutes citées, contiguës | 123, 123 citées, aucune orpheline ni pendante | ☑ |
| 19 figures | 19 citées, 19 présentes, **regravées identiques à l'octet** par `figures/contenu.py` | ☑ |
| 24 sections, 22 tableaux, 21 blocs de code, 10 algorithmes légendés | 24, 22, 21, 10 | ☑ |
| `hors_perimetre()` : 20 et 13 ; `hors_modele()` : 5 ; 31 modules ; 22 énoncés en dur de l'onglet « Limites » ; 15 oracles ; 14 DT ; 22 réserves ouvertes | 20, 13, 5, 31, 22 (= 8 + 11 + 3), 15, 14, 22 | ☑ |
| Empaquetage web : 3 669 337 octets bruts, 1 447 624 compressés | 3 669 337, 1 447 624 | ☑ *sur le fichier présent — mais voir T-04* |

*C'est l'inverse du constat fait sur le compendium le même jour : ici, les rendus sont ceux de leur source et les chiffres ont leur ligne de mesure.*

Ce que l'audit trouve est de trois ordres, et aucun n'est bloquant :

1. **Un périmé, et un faux périmé.** Le champ `Date` du PRD porte le 13 août pour un document dont la source normative est du 15 et le dernier banc du 17 (T-01) — celui-là est réel. L'empaquetage web, lui, est périmé **de date** par la règle que le `README` énonce, ⚠ *mais la phase 2 a mesuré que le module refait est **identique à l'octet** : les chiffres publiés n'ont jamais été faux* (T-04, corrigé en cours d'exécution).
2. **Une dette déclarée, mesurée, et pas finie : la migration des renvois de page vers la 3ᵉ édition.** 107 renvois `§X.Y, p. N` ont été jugés contre la carte des pages du PDF livré ; 93 tombent dans la plage de leur section, 11 à sa frontière, et **3 sont faux — mais les 3 sont déjà déclarés comme tels dans le code, avec la page réelle**. ⚠ *Ce constat annonçait « 45 renvois nus » ; la mesure de la phase 1 en trouve **zéro de vivant** — 52 des 61 nomment leur édition, et les 9 autres sont de la prose sur la question d'édition elle-même.* **La migration est finie au code** ; ce qui restait dû était l'ablation de deux ventilations chiffrées et périmées (T-03, corrigé en cours d'exécution).
3. **Trois contradictions entre le PRD et la source qu'il nomme**, héritées de la 2ᵉ édition et déclarées seulement pour le §0 quand elles vivent aussi au §6, au §7 et au §12 (T-02) ; un contrôle de rendu qui ne voit un PDF périmé que par horodatage, donc aveugle après tout `git clone` (T-06) ; et une source dont la numérotation des algorithmes n'est pas unique (T-07).

**Le plan est en trois phases** — appareil, métadonnées et renvois, source — dont la troisième n'est pas exécutable sans une quatrième édition du traité, et le dit.

---

## 2. Méthode

- **Rejeu de tout l'appareil**, depuis le dossier, avec `CARGO_TARGET_DIR` dérouté hors de OneDrive comme le `README` l'exige : `cargo test`, `cargo clippy`, `cargo doc`, `python Python/check-traite.py`, `python figures/contenu.py` (regravure en place, puis `git status`), `bash build/build-pdf.sh` vers un chemin de scratch.
- **Parité stricte du rendu** : le PDF refait est comparé au PDF versionné page à page, sur le texte extrait — pas seulement sur le compte de pages.
- **Carte des pages de la 3ᵉ édition**, construite en cherchant le titre de chacune des 24 sections dans le texte du PDF ; chaque renvoi `§X.Y, p. N` du code et des documents est jugé contre elle. Les cas de frontière sont tranchés sur le texte de la page — la fin de section occupe-t-elle le haut de la page citée ?
- **Chaque cardinal que `CLAUDE.md` ou le PRD déclare « remesurable »** a été remesuré par la ligne qu'il donne.
- **Non rejoués, et c'est déclaré** : les trois bancs (`dt1-flottant`, `parite-wasm`, `nf05-debit`), qui exigent une construction WASM et Node ; l'interface native et la campagne. Leurs verdicts sont lus, non refaits.
- Les mesures sont celles du 2 septembre 2026. Le dossier a l'honnêteté de dater les siennes ; cet audit fait de même.

---

## 3. Constats

Sévérité : **B** bloquant (le dossier ment sur lui-même) · **M** majeur (une règle du dossier est violée, ou une déclaration est fausse) · **m** mineur.

### 3.1 Appareil et rendus

| # | Sév. | Constat | Où |
|---|---|---|---|
| T-04 | ~~M~~ → **m** | ⚠ **CE CONSTAT ÉTAIT SUR-ÉVALUÉ, et la phase 2 l'a démenti le jour même — la correction est ici plutôt qu'effacée.** **Le constat, tel qu'il a été porté** : `web/sim_viz_bg.wasm` date du 17 août 2026 à 11 h 14, `crates/sim-viz/` a été édité au commit `7a1b7f2` du 25 août, et le `README` (l. 162) comme `CLAUDE.md` (l. 299) publient un couple de chiffres NF-08 *« valide jusqu'à la prochaine édition de `crates/sim-viz/` »*. **Ce que la mesure a rendu** : le module refait est **identique à l'octet**, et le commit incriminé ne portait que **deux lignes de commentaire de documentation** — zéro code. ⚠ *L'audit annonçait « 81 lignes de code dans `scenario_a.rs` et `scenario_b.rs` » : ce chiffre venait d'un `git diff` pris depuis `3dced78`, base qui englobe des commits déjà contenus dans le module. Il est retiré.* ☑ **Les chiffres publiés n'ont jamais été faux.** **Ce qui reste vrai, et justifie le contrôle 0.3** : rien ne garantissait la concordance, et le module était périmé **de date**. *Une date postérieure dit qu'on ne SAIT pas ; elle ne dit pas qu'on a tort — et le contrôle écrit en phase 0 a fait exactement cette confusion à sa mise en service, ce qui a conduit à lui ajouter un mode par contenu.* | `README.md:162`, `CLAUDE.md:299`, `git show 7a1b7f2 -- crates/sim-viz` |
| T-06 | M | **`check-traite.py` [1] ne voit un PDF périmé que par horodatage** (`src.stat().st_mtime > pdf.stat().st_mtime`). Après un `git clone` ou un `checkout`, les deux fichiers portent la date du checkout et le contrôle est **aveugle** ; il l'est aussi si le `.md` est repris dans la même seconde que le rendu, ou si le rendu est refait sans reprise du `.md` après une régression du gabarit. **Le contrôle qui manque est la parité stricte** — refaire le rendu et comparer —, que cet audit a exécutée à la main : elle passe aujourd'hui. | `Python/check-traite.py`, fonction `pagination()` |
| T-05 | m | `check-traite.py` porte encore **« les 119 notices »** dans sa docstring (l. 18) et `REFS = 119` (l. 35) comme repli si le front-matter ne se lit pas ; le traité en compte 123 et le front-matter le dit. Le contrôle passe parce que le front-matter se lit ; **le jour où il ne se lira pas, le repli exigera 119 et échouera à tort**. Le commentaire de la l. 187 explique pourquoi le compte ne se code plus en dur — et laisse la constante. | `Python/check-traite.py:18`, `:35` |
| T-14 | m | `check-traite.py` [2] rapporte **« +366 mots-équivalents depuis la référence du 15 août »** alors que le PDF est identique au rendu du `.md` courant : la constante de référence de l'étalonnage précède le dernier état du 15 août. La croissance rapportée est mesurée contre une ligne de base périmée d'un demi-jour. | `Python/check-traite.py`, bloc d'étalonnage |
| T-11 | m | **77 des 126 fichiers suivis sont en CRLF dans l'arbre de travail** alors que le `.gitattributes` de la racine impose `eol=lf`. Les quatre scripts (`.sh`, `.py`) sont en LF et se lancent ; les 19 SVG se regravent identiques après normalisation par git. **Rien ne casse ici**, contrairement au compendium — mais c'est la même condition, et elle est du dépôt, non du dossier. | `git ls-files --eol -- "3 - Traité"` |
| T-12 | m | `bancs/audit-2026-08/` est un **répertoire vide** laissé sur le disque après le retrait de ses douze rapports au commit `7a1b7f2` ; git ne le suit pas, le `README` racine le nomme comme retiré. Cosmétique. | `ls bancs/` |
| T-16 | info | Les trois bancs ne sont **pas rejoués** par cet audit. Leurs verdicts datent des 12, 13 et 17 août 2026. Après T-04, **le banc de parité doit être rejoué sur la construction neuve** — c'est la seule mesure qui prouve que le WASM refait rend les mêmes bits que le natif. | `bancs/*/VERDICT.md` |

### 3.2 Métadonnées, renvois et cohérence documentaire

| # | Sév. | Constat | Où |
|---|---|---|---|
| T-01 | M | **PRD : `Date \| 13 août 2026`** pour un document dont la rangée `Source normative` nomme la 3ᵉ édition du **15 août**, dont le §0.2 enregistre le banc du **17 août**, et dont la révision 3.0 est celle qui « fait passer la clause d'édition ». *Une estampille de version et sa date se lisent ensemble ou pas du tout* — c'est la faute exacte trouvée le même jour au compendium. | `docs/PRD.md:9` |
| T-02 | M | **Le corps du PRD contredit la 3ᵉ édition en trois sites, et la divergence n'est déclarée que pour le §0.** La 3ᵉ édition écrit **7,933 × 10⁻³** (§3.1, p. 42) et qualifie 7,9 × 10⁻³ d'« énoncé faux » ; elle écrit **« elle se fige »** (§4.1, p. 58). Le PRD porte encore **« moins de 7,9 × 10⁻³ »** aux l. 1051 (§6, exigence) et 2160 (§12 A, correspondance traité → implantation) et **« elle dérive sans borne »** à la l. 1435 (§7, scénario). `decisions.md` déclare que le PRD « écrit encore » ces valeurs **« au §0 »** — le §0 les porte en histoire, mais les trois sites ci-dessus sont des **exigences et des correspondances**, c'est-à-dire ce que le code cite. | `docs/PRD.md:1051`, `:1435`, `:2160` ; `docs/decisions.md` (« Reclassement du 17 août ») |
| T-03 | M | **La migration des renvois de page vers la 3ᵉ édition n'est pas finie, et elle se mesure.** Sur **107** renvois `§X.Y, p. N` du code et des documents : **93** tombent dans la plage de leur section ; **11** à sa frontière — tranchés sur le texte de la page, tous plausibles (la fin de section occupe le haut de la page citée) ; **3 sont faux** — `§8.3, p. 94` (la page appartient au §6.2), `§5.3, p. 63` (§4.2), `§1.3, p. 4` (sommaire) — plus `§2.1, p. 22` (dernière page du §1.3). ☑ **Les quatre sont déclarés comme faux dans le code**, avec la page réelle, dans une table d'auto-déclaration (`scenario.rs:624-630`) : *ce sont des pièces d'histoire conservées, non des erreurs vivantes.* ⚠ **Le « ce qui reste dû » de ce constat était FAUX, et la phase 1 l'a mesuré** : il annonçait *« 45 renvois nus contre 22 qui portent `(3ᵉ éd.)` »*, arithmétique tirée de 61 − 22 sans voir *(a)* qu'un seul marqueur qualifie plusieurs pages d'une même ligne, ni *(b)* que d'autres formes qualifient — « troisième édition », « 3ᵉ édition ». ☑ **Mesure du 2 septembre 2026** : sur **61** renvois, **50** nomment leur édition sur leur propre ligne, **2** dans les deux qui l'encadrent, et **les 9 restants vivent tous dans une prose qui porte sur la question d'édition** — la table d'histoire de `scenario.rs`, qui énumère les pages fausses avec leur remplaçante. ***Aucun renvoi vivant n'est nu : la migration est finie au code.*** ☐ **Ce qui restait vraiment dû** : les deux ventilations chiffrées et périmées de `CLAUDE.md` et de `SPEC.md`, retirées en phase 1 au profit de leur seule ligne de mesure. Et la ventilation qu'il donne pour le §1.2 — *p. 16 dix fois, p. 13 quatre fois, p. 14 deux fois* — est celle du 17 août ; aujourd'hui **p. 14 six fois, p. 13 une fois** : le compte a bougé, comme il l'annonce. | `grep -rhoE '§[0-9]+(\.[0-9]+)?, p\. [0-9]+' crates/`, `crates/sim-agents/src/scenario.rs:618-634` |
| T-08 | m | **La conclusion du traité dit « cinq écarts, dont trois contre l'ouvrage »** (l. 1743, p. 129) ; le reclassement du 17 août en compte **deux contre le traité**, deux absorbés par la 3ᵉ édition, un hors traité. `decisions.md` le déclare et l'explique. Mais `CLAUDE.md` et le `README` écrivent que la 3ᵉ édition **« confirme le compte en citant ce dépôt »** — vrai du cardinal cinq, **faux de la répartition**, que seule une 4ᵉ édition peut corriger. *Une confirmation partielle citée comme confirmation est une provenance qui déborde sa source.* | `Traité.md:1743`, `CLAUDE.md` (NF-15), `README.md` |
| T-09 | m | `decisions.md` situe la **notice 120** à `Traité.md:1743` (×2) et p. 129. La ligne 1743 est la **phrase de la conclusion qui cite [120]** ; la notice elle-même est à la **l. 1871, p. 143**. Le renvoi de ligne pointe la citation, le texte annonce la notice. Imprécision de libellé, pas d'erreur de fait. | `docs/decisions.md` (« Reclassement du 17 août ») |
| T-10 | info | La notice 120 du traité cite **« 428 tests, dépôt au 15 août 2026 »** ; le dossier en mesure 467. **Aucun défaut** : la citation est datée, vraie à sa date, et la source est gelée par édition. À savoir quand le `README` racine et le traité sont lus côte à côte. | `Traité.md:1871` |

### 3.3 La source elle-même

| # | Sév. | Constat | Où |
|---|---|---|---|
| T-07 | m | **La numérotation des algorithmes du traité n'est pas unique** : « Algorithme 1 », « 2 » et « 3 » existent **trois fois chacun** — ch. 1 (l. 313, 378, 466), ch. 3 (l. 693, 779, 861), ch. 4 (l. 954, 1016, 1080) —, et le ch. 8 emploie un **autre schéma**, « Algorithme 8.1 » (l. 1656). Conséquence mesurée sur les citations : **126 renvois « algorithme 1/2/3 »**, dont **25 seulement qualifiés par leur chapitre** — 9 sur 23 dans `crates/`, 16 sur 58 dans `docs/`, 0 sur 45 dans le traité, où le chapitre courant désambiguïse. *Une source qui nomme trois objets du même nom rend chaque citation nue équivoque.* Les tableaux, eux, sont numérotés **au rendu** (« Tableau 16. – Leviers de gouvernance », p. 84) et non dans la source ; les 184 citations « tableau N » du code et du PRD résolvent, **mais toute insertion d'un tableau renumérote ceux qui suivent** sans qu'aucun contrôle ne le signale. | `Traité.md`, `grep -rhoiE 'algorithme [1-3]' crates/ docs/` |
| T-13 | m | **Figure 2.1b précède Figure 2.1a** dans le texte (l. 515 puis 519) : les lettres suivent l'ordre des fichiers (`f-02-1a-calm`, `1b-usl`, `1c-isr`), non l'ordre de lecture. Cosmétique, et de la source : ne se corrige qu'à une nouvelle édition. | `Traité.md:515`, `:519` |

### 3.4 Ce que l'audit a écarté, et pourquoi le dire

Trois constats ont été instruits puis **retirés parce que la mesure les a démentis** — et un audit qui tairait ses fausses pistes ferait croire à une sûreté qu'il n'a pas.

- **« Les tableaux cités par leur numéro n'existent nulle part »** : `pypdf` n'extrayait aucun libellé « Tableau N » du PDF. `pymupdf` les lit — *« Tableau 3. – »*, *« Tableau 16. – »* — et un rendu de la page 84 le montre. **L'extracteur était aveugle, pas le document.**
- **« `fontsize: 10pt` contredit le corps de 11 pt »** : le YAML dit 10, le corps mesuré est 11 — **et la source l'écrit elle-même** (l. 41 et 264 : *« `fontsize` vaut 10 pt et le corps vaut 11 pt »*), avec le motif. Déclaré, donc pas un constat.
- **« Trois renvois de page sont faux »** : ils le sont, **et le code les déclare tels** dans une table qui donne la page réelle (T-03). Une erreur déclarée avec sa correction est une pièce d'histoire, pas un défaut.

---

## 4. Plan d'exécution

### 4.1 Cadre

- **Aucune phase ne touche `Traité.md` ni `Traité.pdf`** : la 3ᵉ édition est gelée, et ce qui relève de la source (T-07, T-08, T-13) est nommé pour une 4ᵉ édition, non exécuté.
- **Toute passe qui touche `crates/sim-viz/` refait l'empaquetage web et rejoue le banc de parité dans le même commit** — c'est la règle du `README`, rendue opposable par la phase 1.
- Chaque phase se clôt par le rejeu de la batterie du §6 et **sortie 0**.
- **Un chiffre corrigé garde l'ancien à côté de lui, daté** — la discipline du §0.2 du PRD, étendue aux corrections de cet audit.

### 4.2 Phase 0 : appareil (un commit)

| Tâche | Constats | Geste |
|---|---|---|
| 0.1 | T-06 | Ajouter à `check-traite.py` un contrôle **[4] parité** : refaire le rendu vers un fichier temporaire (`OUT_PDF=…`), comparer au PDF versionné **page à page sur le texte extrait**, échouer à la première divergence. Garder [1] pour l'arbre de pages. Éprouver par mutation : un mot changé dans le `.md`, un PDF d'une autre construction. |
| 0.2 | T-05, T-14 | `check-traite.py` : docstring et repli à **123** ; re-baser l'étalonnage [2] sur l'état rendu (72 110 mots, 19 figures, 143 pages), et dater la ligne de base dans le commentaire. |
| 0.3 | T-04 | Ajouter à `build/` (ou à `DEVELOPPEMENT.md` comme commande, avec un contrôle qui la vérifie) un test de **fraîcheur de l'empaquetage** : échec si un fichier de `crates/sim-viz/src/` est postérieur à `web/sim_viz_bg.wasm`. *C'est le défaut que le banc du 17 août a décrit et que rien n'attrape.* |
| 0.4 | T-12 | Retirer le répertoire vide `bancs/audit-2026-08/`. |

Critère de sortie : `check-traite.py` à quatre contrôles, sortie 0 ; le contrôle [4] démontré par mutation ; le contrôle de fraîcheur en échec **avant** la phase 2 (il doit voir T-04) et en succès après.

### 4.3 Phase 1 : métadonnées et renvois (un commit)

| Tâche | Constats | Geste |
|---|---|---|
| 1.1 | T-01 | PRD : `Date` à la date de la dernière révision de fond (17 août 2026, banc §0.2) — ou, si la version 3.0 doit rester datée du 13, ajouter une rangée `Dernière mise à jour` et l'expliquer. *Une seule des deux, et dire laquelle.* |
| 1.2 | T-02 | PRD : aux l. 1051, 1435 et 2160, porter la valeur de la **3ᵉ édition** avec renvoi de page et d'édition, et garder l'ancienne en note datée (« 2ᵉ éd. écrivait … ») ; étendre la déclaration de `decisions.md` du « §0 » aux trois sites. |
| 1.3 | T-03 | Qualifier les **45 renvois `p. N` nus** du code par `(3ᵉ éd.)` après vérification de chacun contre la carte des pages (§3.2 de cet audit) ; les quatre déclarés faux restent dans leur table d'histoire. Mettre à jour la ventilation du §1.2 dans `CLAUDE.md` ou — mieux — **retirer les chiffres et ne garder que la commande**, comme le dossier le fait ailleurs. |
| 1.4 | T-08, T-09 | `CLAUDE.md` et `README` : « la 3ᵉ édition confirme le **cardinal** de cinq ; sa répartition — trois contre l'ouvrage — est **antérieure au reclassement du 17 août** ». `decisions.md` : « l'énoncé de la conclusion (l. 1743, p. 129) cite la notice 120 (l. 1871, p. 143) ». |

Critère de sortie : `grep -rhoE '§[0-9]+(\.[0-9]+)?, p\. [0-9]+' crates/` **vide** — tout renvoi porte son édition — ; PRD sans valeur de 2ᵉ édition hors du §0.

### 4.4 Phase 2 : l'empaquetage et sa parité (un commit)

| Tâche | Constats | Geste |
|---|---|---|
| 2.1 | T-04 | Refaire l'empaquetage par les deux lignes du `README` § « 2. L'interface web » ; mesurer brut et compressé ; **reporter les deux chiffres, datés, à `README.md` et `CLAUDE.md`**, l'ancien couple à côté. |
| 2.2 | T-16 | Rejouer `bancs/parite-wasm` sur la construction neuve ; si le verdict tient, le dater ; sinon, c'est un écart NF-02 à consigner au registre **avant** toute autre chose. |
| 2.3 | T-11 | Ne rien faire ici : la normalisation des fins de ligne est un chantier du **dépôt**, déjà nommé à l'audit du compendium, et elle invalide des empreintes ailleurs. Le dossier n'en souffre pas. |

Critère de sortie : contrôle de fraîcheur (0.3) en succès ; NF-08 re-mesurée et datée.

### 4.5 Phase 3 : la source — pour une quatrième édition, non pour ce dépôt

| Tâche | Constats | Ce que la prochaine édition devrait trancher |
|---|---|---|
| 3.1 | T-07 | **Un seul schéma de numérotation des algorithmes** — `N.k` par chapitre partout, comme le ch. 8 le fait déjà —, ou une numérotation continue 1-10. Dans l'attente, **qualifier par le chapitre** les 101 citations nues du code et des documents. |
| 3.2 | T-08 | Une conclusion qui porte la répartition **du reclassement** (deux contre, deux absorbés, un hors traité), ou qui date la sienne. |
| 3.3 | T-13 | Lettres des figures 2.1 dans l'ordre de lecture, ou ordre de lecture dans celui des lettres. |
| 3.4 | T-07 | **Numéroter les tableaux dans la source** (« Tableau 16 — ») plutôt que de laisser le rendu le faire : 184 citations en dépendent, et une insertion les décale toutes sans bruit. |

*Cette phase n'a pas de critère de sortie dans ce dépôt : elle relève de l'auteur du traité, et le dossier ne corrige pas sa source normative — il remonte.*

### 4.6 Séquence et effort

Phase 0 puis 1 puis 2, dans l'ordre : **le contrôle de fraîcheur (0.3) doit exister avant que l'empaquetage soit refait (2.1)**, pour qu'on le voie mordre une fois. Effort : la phase 0 et la phase 1 tiennent dans une passe ; la phase 2 dépend d'une construction WASM et de Node, et son banc de parité prend le temps qu'il prend. La phase 3 ne se planifie pas ici.

---

## 5. Limites de cet audit

- **Les bancs ne sont pas rejoués.** DT1, NF-05 et la parité sont des verdicts lus, non refaits ; le dossier lui-même dit que le débit (NF-05) varie d'un passage à l'autre.
- **La carte des pages est reconstruite par recherche de titres dans le texte extrait**, et les onze cas de frontière sont jugés sur la position du titre suivant dans la page. C'est une mesure, mais indirecte : un renvoi jugé « plausible » n'a pas été relu dans le PDF.
- **L'audit ne porte pas sur le fond du traité ni sur la justesse des mécanismes** : il porte sur la concordance entre ce que le dossier déclare et ce qu'il contient. Les cinq écarts NF-15 et les vingt-deux réserves sont lus comme déclarés, non instruits.
- Un extracteur de texte a failli produire un faux constat majeur (§3.4). **Deux outils ont été employés là où un seul mentait** ; là où un seul a été employé, la réserve vaut.

---

## 6. Commandes de rejeu

```bash
cd "3 - Traité"
export PYTHONUTF8=1
export PATH="$LOCALAPPDATA/Microsoft/WinGet/Packages/BrechtSanders.WinLibs.POSIX.UCRT_Microsoft.Winget.Source_8wekyb3d8bbwe/mingw64/bin:$HOME/.cargo/bin:$PATH"
export CARGO_TARGET_DIR="C:/Users/agbru/AppData/Local/Temp/cargo-conso"   # hors de OneDrive, exigé
cargo test --workspace --release
cargo clippy --workspace --all-targets --release
cargo doc --workspace --no-deps
python Python/check-traite.py         # 4 contrôles, dont [4] parité : refait le rendu et compare les octets
python Python/check-empaquetage.py    # refait le module WASM et compare les octets
python figures/contenu.py && git status --short figures/          # vide = figures reproductibles
```

Les sondes qui ont conduit les constats :

```bash
grep -rhoE '§[0-9]+(\.[0-9]+)?, p\. [0-9]+' crates/ | sort | uniq -c | sort -rn   # T-03 : 45 renvois nus
grep -rhoE '\(3ᵉ éd\.\)' crates/ | wc -l                                          # 22 qualifiés
git log --oneline --since=2026-08-17 -- crates/sim-viz                            # T-04 : 7a1b7f2
grep -n -E "7,9 × 10⁻³|dérive sans borne" docs/PRD.md                             # T-02 : l. 1051, 1435, 2160
grep -n -oE '^(\*\*)?Algorithme [0-9.]+' Traité.md                                # T-07 : dix lignes, trois « 1 »
git ls-files --eol -- . | awk '{print $2}' | sort | uniq -c                       # T-11
```

---

## 7. Exécution des phases 0 à 2 — journal du 2 septembre 2026

*Sur instruction d'auteur, les phases 0 à 2 ont été exécutées le jour même de l'audit. La phase 3
relève d'une quatrième édition du traité et n'est pas entamée.*

### 7.1 Ce qui a été fait

| Phase | État | Ce qu'elle laisse derrière |
|---|---|---|
| **0 — appareil** | ☑ close, sauf 0.4 | **Contrôle [4] parité** dans `check-traite.py`, éprouvé par mutation ; **`Python/check-empaquetage.py`**, neuf, à deux modes, éprouvé par deux mutations ; repli des notices et étalonnage recalés ; cinq commandes d'avant-commit déclarées à trois endroits |
| **1 — métadonnées et renvois** | ☑ close | `Date` du PRD ; **trois sites d'exigence** alignés sur la 3ᵉ édition ; deux ventilations périmées retirées au profit de leur ligne de mesure ; portée de la « confirmation » du traité précisée ; notice 120 distinguée de l'énoncé qui la cite |
| **2 — empaquetage et parité** | ☑ close | Module refait et **mesuré identique** ; NF-08 re-daté ; **banc `parite-wasm` rejoué, six cas tenus** ; verdict daté |
| **3 — la source** | ☑ **close le même jour** — quatrième édition | Numérotation des algorithmes, répartition de la conclusion, ordre des figures 2.1, numérotation des tableaux : *tout cela s'écrit dans le traité, et le dossier ne corrige pas sa source normative — il remonte* |

**Batterie complète, sorties 0** : `cargo test` (23 suites, 467 tests), `cargo clippy`, `cargo doc`,
`check-traite.py` (quatre contrôles), `check-empaquetage.py`, `figures/contenu.py` (regravure sans
diff), `bancs/parite-wasm` (six cas).

### 7.2 Ce que l'exécution a appris contre l'audit

**Deux constats sur quatorze étaient faux, et les deux dans le même sens — ils accusaient à tort.**

1. ⚠ **T-04 était un faux positif en substance.** L'empaquetage était périmé **de date**, pas de
   contenu : refait, le module est sorti **identique à l'octet**, et le commit incriminé ne portait
   que **deux lignes de commentaire de documentation**. *Mon « 81 lignes de code » venait d'un
   `git diff` pris sur une base trop ancienne, qui englobait des commits déjà contenus dans le
   module.* ☑ **Les chiffres NF-08 publiés n'ont jamais été faux**, et la règle du `README` n'avait
   pas encore été enfreinte.
2. ⚠ **T-03 sur-comptait d'un facteur cinq.** Il annonçait « 45 renvois nus » ; la mesure en trouve
   **zéro de vivant**. L'arithmétique fautive était 61 − 22, qui ignore qu'un seul marqueur
   `(3ᵉ éd.)` qualifie plusieurs pages d'une même ligne et que d'autres formes qualifient aussi.
   **La migration des renvois était finie**, et ce qui restait dû n'était pas un travail de
   qualification mais l'**ablation de deux ventilations chiffrées et périmées**.

☑ **Un troisième constat s'est confirmé exactement, et c'est celui qui portait** : T-06. La mutation
qui l'éprouve est celle d'un `git clone` — source reprise, horodatages égalisés — et elle montre
**[1] au vert pendant que [4] mord**. *Le contrôle qui manquait manquait bien.*

### 7.3 Ce que l'exécution a appris contre elle-même

⚠ **Le contrôle de fraîcheur écrit en phase 0 a crié au loup à sa mise en service**, sur le faux
positif T-04 : il comparait des dates et concluait « périmé » là où le contenu était juste. **Il a
donc reçu un second mode**, qui refait le module et compare les octets — possible parce que la
phase 2 a mesuré, au passage, que **la construction WASM est reproductible à l'octet**, ce que le
dossier n'avait jamais établi.

⚠ **Puis une seconde mutation a trouvé un trou dans ce correctif** : le mode par contenu était placé
*derrière* le mode par dates, si bien qu'un module **altéré à la main** passait — écrire dedans met
sa date à jour, donc plus aucune source ne lui est postérieure, donc on ne comparait rien.
***Un contrôle qu'on satisfait en touchant le fichier qu'il surveille ne surveille pas ce fichier.***
Le contenu est devenu le verdict, les dates un simple indice, et les deux mutations passent.

☑ **Le contrôle de parité du rendu s'est révélé plus fort que prévu.** Le plan projetait une
comparaison **page à page sur le texte extrait** ; la mesure a montré que la chaîne rend le PDF
**reproductible à l'octet** aux seuls horodatages près — quatre champs, tous volatils par
construction. Le contrôle compare donc les **octets**, ce qui ne dépend d'aucun extracteur : *l'audit
lui-même avait manqué de conclure faux parce que deux extracteurs du dépôt lisent différemment le
même PDF* (§3.4).

### 7.4 Ce qui n'a pas été fait

☐ **Tâche 0.4 — le répertoire vide `bancs/audit-2026-08/`.** La suppression a été **refusée par la
couche de permissions**, deux fois et sous deux formes. Le répertoire est vide, non suivi par git, et
nommé comme retiré au `README` de la racine ; il se retire par :

```bash
rmdir "3 - Traité/bancs/audit-2026-08"
```

☐ **Phase 3 en entier**, qui relève de l'auteur du traité.

☐ **Les bancs `dt1-flottant` et `nf05-debit` restent non rejoués.** Seul `parite-wasm` l'a été,
parce que la phase 2 touchait ce qu'il mesure. *Un verdict qu'on ne rejoue pas se lit à sa date.*

---

## 8. Exécution de la phase 3 — journal du 2 septembre 2026

*Sur instruction d'auteur, la phase 3 a été exécutée le jour même. Elle touchait la source
normative : elle est donc traitée comme une **quatrième édition**, faute de quoi changer la
numérotation d'un document publié sans changer son édition eût été la provenance fausse que **F2**
proscrit. Le registre la consigne à [`docs/decisions.md`](docs/decisions.md).*

### 8.1 Les quatre tâches

| Tâche | État | Ce qu'elle laisse derrière |
|---|---|---|
| **3.1** — numérotation des algorithmes | ☑ | **`N.k` partout** : 1.1-1.3, 2.1-2.3, 3.1-3.3, 4.1-4.3, 8.1. **Trois légendes posées au chapitre 2**, qui n'en avait aucune. **Zéro citation nue** dans le traité, le code et les documents — 31 dans la source, 25 qualifiées, 41 résolues par contexte, 13 à la main |
| **3.2** — la conclusion | ☑ | La répartition « trois contre l'ouvrage » **porte sa date** et nomme le reclassement qui l'a portée à deux |
| **3.3** — figures §2.1 | ☑ | Les lettres suivent l'**ordre de lecture** ; les deux SVG renommés, le graveur réordonné, les orphelins retirés |
| **3.4** — numérotation des tableaux | ☑ | **22 tableaux numérotés dans la source**, comme les figures ; la numérotation automatique de Typst est coupée pour les deux espèces |

### 8.2 Ce que la mesure a permis, et qui n'était pas acquis

☑ **La pagination est préservée : 143 pages avant, 143 après.** Les vingt-quatre sections ouvrent
aux mêmes pages **à une exception près** — le §2.3 passe de la p. 34 à la p. 35, les trois légendes
neuves du chapitre 2 l'ayant repoussé. ⚠ **C'est cette mesure, et elle seule, qui a autorisé la
migration des 141 marqueurs de `(3ᵉ éd.)` à `(4ᵉ éd.)`** : sans elle, chaque page citée aurait dû
être revérifiée une à une. *Les 107 renvois `§X.Y, p. N` retombent exactement là où ils étaient — 93
dans leur plage, 14 hors, les mêmes qu'avant et tous déjà déclarés.*

### 8.3 Ce que l'exécution a appris

1. ⚠ **Le traité ne comptait pas dix algorithmes, mais treize — et trois n'avaient pas de nom.**
   Les blocs du chapitre 2 étaient cités « l'algorithme 1/2/3 » dans la prose **sans porter aucune
   légende** : le numéro ne désignait rien, et une citation extérieure était irrésoluble. *L'audit
   avait compté « 10 algorithmes légendés » et coché la case ; le mot « légendés » faisait tout le
   travail, et personne ne l'avait remarqué.*
2. ⚠ **Le chapitre 5 n'a pas d'algorithmes du tout — il a des procédures nommées.**
   `DÉCISION-PAR-SEUIL`, `MOYENNE-LOCALE`, `ENCHÈRE-ε` : leur prose les appelait « algorithme 1/2/3 »
   par habitude. *Leur imposer une numérotation aurait uniformisé contre le texte plutôt qu'avec
   lui* — la prose les nomme désormais, et le chapitre garde sa convention.
3. ☑ **Un contrôle écrit le matin a exigé du travail le soir.** `check-empaquetage.py` a refusé le
   module WASM après la migration des marqueurs : *ceux-ci ne vivent pas que dans les commentaires,
   ils vivent dans les chaînes `source:` que l'interface affiche.* Le module a changé de contenu —
   **+80 octets compressés** — et le banc de parité a été rejoué sur la construction neuve.
   **Le mode par dates n'aurait rien vu** : le module était plus récent que la plupart des sources.

### 8.4 Ce qui n'a pas été fait

☐ **Le répertoire vide `bancs/audit-2026-08/`** — la suppression reste refusée par la couche de
permissions. Elle se fait par `rmdir "3 - Traité/bancs/audit-2026-08"`.

☐ **Les bancs `dt1-flottant` et `nf05-debit`** ne sont toujours pas rejoués : la phase 3 ne touche ni
l'arithmétique ni le débit. *Un verdict qu'on ne rejoue pas se lit à sa date.*

☐ **Rien du fond.** Les cinq écarts de NF-15 restent cinq et gardent leur classement, les
vingt-deux réserves restent vingt-deux, les six phases restent closes. **La quatrième édition
n'ajoute ni chapitre, ni thèse, ni mesure.**
