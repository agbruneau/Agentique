# Consolidation de l'audit du 17 août 2026

Dix agents ont audité et corrigé le dépôt en cinq morceaux, deux tours chacun. Il
leur était **interdit** de toucher `docs/PRD.md` et `docs/decisions.md` ; ils ont
donc consigné dans leurs rapports ce qui oblige à les corriger. Ce document est
la passe qui consolide, et il est le **verdict du banc** : le §0 du PRD se met à
jour à la fin d'un banc, cette campagne en est un, et son enregistrement est au
§0.2.

**Périmètre édité** : `docs/PRD.md`, `docs/decisions.md`, `CLAUDE.md`,
`docs/README.md`, `docs/SPEC.md`, `docs/architecture.md`,
`docs/DEVELOPPEMENT.md`, `README.md`, et les **commentaires** de `clippy.toml`.
Aucun fichier `.rs` n'est touché : un second agent lisse le code en parallèle et
écrit dans `crates/`.

**Condition de mesure.** `cargo` n'est pas dans le `PATH` et l'édition de liens
échoue dans le `target/` du dépôt, dont le chemin contient un « é ». ✎ *Motif faux, corrigé le
22 août 2026 : ce n'est pas l'accent du chemin mais la **synchronisation OneDrive** du
`target/` qui casse l'édition de liens — un workspace d'essai sous `…/3 - Traité/`, même
accent et même espace, s'édite sans un mot hors de OneDrive. Le déroutement reste le bon
remède ; seul son motif était mal attribué. Mesure à l'appui à
[`docs/DEVELOPPEMENT.md`](../../docs/DEVELOPPEMENT.md).* Toutes les
mesures ci-dessous ont été prises ainsi, et chacune porte son heure parce que
`crates/` bougeait pendant :

```powershell
$env:PATH = "$env:USERPROFILE\.cargo\bin;$env:LOCALAPPDATA\Microsoft\WinGet\Packages\BrechtSanders.WinLibs.POSIX.UCRT_Microsoft.Winget.Source_8wekyb3d8bbwe\mingw64\bin;$env:PATH"
$env:CARGO_TARGET_DIR = "C:\Users\agbru\AppData\Local\Temp\cargo-conso"
```

---

## L'état mesuré, et la ligne qui le refait

| Ce qui est mesuré | Valeur | Ligne | Heure |
|---|---|---|---|
| Suite complète | **465 tests, 0 échec**, exit 0 | `cargo test --workspace --release` | 09 h 49 |
| — dont unitaires | **422** : 253 `sim-agents`, 96 `sim-core`, 68 `sim-milieu`, 5 `sim-viz` | même sortie, par binaire de test | 09 h 49 |
| — dont intégration | **43** : 4 `determinisme` + 11 `scenario_b` + 5 + 4 + 5 + 3 + 11 `sortie_phase_2..6` | idem | 09 h 49 |
| Interdictions structurelles | **0**, exit 0 | `cargo clippy --workspace --all-targets --release` | 09 h 50 |
| Renvois rustdoc | **0**, exit 0 | `cargo doc --workspace --no-deps` | 09 h 50 |
| Pages du `Traité.pdf` | **143** | `python -c "import pymupdf; print(pymupdf.open('Traité.pdf').page_count)"` | 09 h 46 |
| Édition | **3ᵉ, 15 août 2026** | `head -6 Traité.md` → `date: "15 août 2026 — troisième édition, revue sur sa propre mesure"` | 09 h 46 |
| Notices | **123** | `awk 'NR>1749' Traité.md \| grep -cE '^[0-9]+\. '` | 09 h 46 |
| Sections | **24** | `grep -c '^### ' Traité.md` | 09 h 46 |
| `sim_agents::hors_perimetre()` | **20** | `awk '/pub fn hors_perimetre/,/^}/' crates/sim-agents/src/lib.rs \| grep -cE '^\s*"'` | 10 h 21 |
| `sim_milieu::hors_perimetre()` | **13** | même ligne sur `crates/sim-milieu/src/lib.rs` | 10 h 21 |
| `ModeleFaute::hors_modele()` | **5** entrées, la première énumérant **neuf** mécanismes sans appelant | lecture de `crates/sim-core/src/faute.rs:489` | 10 h 05 |
| Modules `sim-agents` | **31** (32 fichiers moins `lib.rs`) | `ls crates/sim-agents/src/*.rs \| wc -l` | 10 h 21 |
| Termes du glossaire | **32** dans `glossaire()` | lecture de `crates/sim-agents/src/glossaire.rs:48` | 10 h 02 |
| Énoncés en dur, onglet « Limites » | **22** = 8 + 11 + 3, sur trois des six listes | lecture de `crates/sim-viz/src/lib.rs`, `limites()` | 10 h 03 |
| Lignes du PRD | **2 340** après consolidation | `wc -l docs/PRD.md` | 10 h 15 |
| Réserves au §0 du PRD | **22** lignes de tableau | `awk 'NR>=147 && NR<=180' docs/PRD.md \| grep -c '^\| \*\*'` | 10 h 21 |

**Le compte de tests a bougé trois fois le même jour** — 428 à 08 h 10 avant
toute modification, 447 à 08 h 32, 465 à 09 h 49 — parce que cinq agents
écrivaient en parallèle. C'est le fait de méthode le plus utile de cette
campagne, et il est écrit tel quel dans les documents : **un chiffre écrit sans
la commande qui le produit se périme sans que rien ne le signale.** Onze minutes
ont suffi à périmer un compte de pages ; douze, à périmer une mesure
d'empaquetage.

---

## Point par point

### 1 — L'édition du traité

**Vérifié.** `Traité.pdf` est à la racine, 143 pages, table des matières donnant
le ch. 8 p. 117 et les Références p. 130 ; `Traité.md` porte
« 15 août 2026 — troisième édition ». `docs/` ne contient aucun PDF. Le PRD
désignait la **deuxième** édition en trois endroits (en-tête, F2, §7) et
`decisions.md` en un (DT5). `CLAUDE.md` était déjà corrigé par l'audit — 143
pages et le chemin racine — avant cette passe.

**Écrit.**

- `docs/PRD.md`, en-tête « Source normative » : troisième édition, 15 août 2026,
  143 pages, 123 notices, avec la mention que la révision 3.0 a été écrite contre
  la deuxième et que **les 56 renvois de page ne sont pas migrés**.
- `docs/PRD.md`, **F2** : la clause de 3.0 passe à la troisième édition, avec le
  motif — le seul traité que le dépôt contienne — et, au même rang, **ce que la
  correction ne fait pas** : migrer les renvois. Cinq mesures y établissent que
  les 56 `p. N` sont ceux de la deuxième, et le protocole `pymupdf` de remesure y
  est écrit.
- `docs/PRD.md` §0.0 : un chapeau ⚠ qui dit que la sous-section est de l'histoire
  et que **sa pagination l'est aussi**, avec renvoi au §0.2. L'histoire des six
  phases n'est pas réécrite.
- `docs/PRD.md` §7, chapeau des scénarios : « les pages citées sont celles de la
  **troisième** édition », avec l'avertissement que la section n'y est pas encore
  migrée et que la thèse du scénario M est la seule vérifiée à la ligne.
- `docs/decisions.md`, **DT5** : amendé « en appliquant la clause à elle-même »,
  avec la ligne de mesure du nombre de pages, le compte des 56 renvois et les
  cinq mesures qui établissent qu'ils sont de la deuxième édition.
- `docs/README.md` : la ligne du `Traité.pdf` ne dit plus « le PRD, figé à la
  deuxième, en cite encore une autre » mais « l'édition est tranchée, la
  migration ne l'est pas » ; la ligne du PRD nomme les trois sous-sections du §0 ;
  la table « Par où entrer » gagne une entrée vers le §0.2.
- `CLAUDE.md` : le §0.0 est présenté comme de l'histoire à pagination de deuxième
  édition, et le §0.2 est nommé.

### 2 — L'épissure de `docs/PRD.md:1539` et `:401`

**Vérifié par mesure sur le PDF**, et l'épissure est plus large que le rapport M4
ne l'annonçait dans le code : la **proposition principale entière** — « un milieu
qui rend la coordination bon marché rend du même geste bon marché ce que le
concepteur ne veut pas » — est **p. 5**, à la fin de l'avant-propos, dans son
libellé exact ; l'**énumération** des trois conséquences est **p. 127**, au §8.3,
où elle s'introduit par « la mesure **ajoute** qu'il rend tout aussi bon
marché… ». La p. 94 n'est celle d'aucune des deux.

**Écrit.** La thèse du scénario M (§7) porte les **deux** provenances, chacune
avec sa page et sa mention d'édition, suivie d'un ⚠ qui nomme le défaut : une
provenance unique pour deux sources, et une page qui n'est celle d'aucune — « le
défaut que F2 nomme, commis par la règle qui le nomme ». `docs/PRD.md:401`
(§2.4) porte la même correction. Deux autres occurrences de « p. 94 », trouvées
au passage et qui citaient un **autre** passage, sont corrigées sur mesure :
« il tombera d'un coup, partout à la fois » est **p. 127** (§8.3), et « le critère
de réussite est vérifiable sans goût » est **p. 119** (§8.1).

### 3 — EX-M26, prix croissant

**Vérifié, et le constat est négatif : le PRD ne chiffre pas cette grandeur.**
`grep -n 'prix croissant\|pente\|preneur' docs/*.md` ne rend que des énoncés
qualitatifs — EX-M26 exige « prix croissant **avec le nombre de preneurs** »
(§6.2), et le §7 liste la politique parmi les positions d'un curseur. Aucune
formule, aucun chiffre : rien à corriger dans le PRD, dont le libellé est
compatible avec le code corrigé. Le code, lui, lit maintenant
`1 + pente × (k − 1)` pour le k-ième preneur distinct, **soumissionnaire
compris** (`crates/sim-milieu/src/quota.rs:151`), et la doc du champ avait raison
contre lui.

**Écrit.** La formule entre au `docs/SPEC.md` §13 — le document qui dit ce que le
code garantit —, avec le fait qu'elle n'a pas d'autre domicile normatif, le test
qui la tient (`le_prix_monte_des_le_deuxieme_preneur`) et la valeur réfutable :
prix cumulé **10** à pente 1 sur quatre preneurs distincts, non 7.

### 4 — `sim-core` n'a aucune `hors_perimetre()`

**Vérifié.** `grep -rn 'fn hors_perimetre' crates/` ne rend que
`sim-agents/src/lib.rs:74` et `sim-milieu/src/lib.rs:55`. La première entrée de
`ModeleFaute::hors_modele()` énumère **neuf** mécanismes sans appelant —
`tirer_pannes`, `Moteur::avancer_partition`, `message_perdu`, `injection_echec`,
`injection_retard`, `injection_valeur`, `retard_message`, `ecriture_corrompue`,
`avertissements` —, dont six n'ont aucun rapport avec le modèle de faute pris
comme modèle ; le plancher mémoire d'EX-C17, EX-C08 et EX-C16 y logent aussi, ou
nulle part.

**Écrit — comme décision, pas comme fonction.** Une entrée au registre
(`docs/decisions.md`, « Les décisions ouvertes par l'audit du 17 août 2026 »)
qui pose les deux branches et leur coût : ouvrir `sim_core::hors_perimetre()`
touche le PRD, `SPEC.md`, `CLAUDE.md` et l'onglet « Limites », qui gagnerait une
septième section ; ou écrire que `hors_modele()` est **par convention** la liste
du cœur, ce qui coûte une phrase et laisse le nom mentir. Une ligne au tableau
des réserves du §0 du PRD, une mention dans `docs/SPEC.md` §11, une dans
`docs/architecture.md` (PD6) et une dans `CLAUDE.md`, chacune portant
« **ne pas créer la fonction sans la décision** ». **Aucun `.rs` n'est touché.**

### 5 — Quatre oracles annoncés, six mesurés

**Vérifié, et c'est bien `CLAUDE.md` qui avait tort.**
`sim_agents::hors_perimetre()` déclare depuis l'audit « **six** des quinze
oracles du catalogue ne sont armés par aucune exécution — `CONSERVATION`,
`ACCORD_LOCAL`, `D1`, `D2`, `UN_SEUL_PROPRIETAIRE` et
`TOUTE_PARTITION_A_UN_PROPRIETAIRE` », et `docs/SPEC.md` §3.3 dit six lui aussi,
avec le détail utile : **deux ne sont armés nulle part, pas même par un test** —
`PushPull::armer_oracle` et `Alignement::armer_oracles` n'ont aucun appelant —,
les quatre autres n'ont d'appelant que dans les tests de leur propre module, et
**neuf tournent**. Le catalogue reste à quinze.

**Écrit.** `CLAUDE.md` et le tableau des réserves du §0 du PRD passent à six, avec
les six noms et la distinction « armé nulle part / armé par son seul test ».
`docs/SPEC.md` §11 corrige « quatre oracles » en « six ». La ligne du PRD porte
la marque *(audit du 17 août)* et dit que le compte du code avait raison.

### 6 — `clippy.toml`, le motif de `mul_add`

**Vérifié contre `bancs/dt1-flottant/VERDICT.md`.** Le verdict porte
`| f64::mul_add | constat | **instable — voir ci-dessous** |`, puis : au premier
passage elle divergeait, au second — après installation de mingw-w64 — elle
**coïncide**, rien du code n'ayant changé ; « une opération dont le résultat
dépend de l'outillage présent sur la machine de build est exactement ce que NF-02
ne peut pas tolérer », et « l'interdiction en sort **renforcée, pas affaiblie** ».
Le commentaire de `clippy.toml:8-10` écrivait l'inverse : « `mul_add` diverge pour
une autre raison — arrondi unique matériel contre double arrondi en WASM ».

**Écrit.** Le commentaire porte le motif du verdict : verdict changé entre deux
passages, dépendance à la machine de construction, `libm::fma` identique aux deux
passages. Le `reason` de la ligne 18 portait la même erreur (« diverge
natif/WASM ») et porte désormais le motif exact. **Aucune interdiction n'est
touchée** : les sept méthodes et les deux types restent, dans le même ordre, avec
les mêmes chemins. `cargo clippy --workspace --all-targets --release` reste à 0.
`docs/DEVELOPPEMENT.md` sépare les deux motifs dans la même passe.

### 7 — Les écarts au traité que la campagne a produits

C'est le point où la campagne a rendu le plus, et le tri compte plus que le
compte. **Le total reste cinq, et la troisième édition le confirme** : sa
conclusion écrit « Cinq écarts entre le livre et sa transposition y sont
consignés, dont trois contre l'ouvrage » et cite ce dépôt en notice 120
(`Traité.md:1743`, `Traité.pdf` p. 129). Ce qui change est le **statut** de trois
lignes, mesuré ligne à ligne contre l'édition livrée :

| Écart | Statut d'avant | Statut mesuré le 17 août | Marque |
|---|---|---|---|
| Budget de retard du mode « moyeu » | contre le traité (2ᵉ éd.) | **Absorbé.** §3.1, `Traité.md:736`, p. 42 : « à n = 100, **7,933 × 10⁻³** […] un arrondi présenté comme une borne stricte est un énoncé faux, non une imprécision ». La mesure est écrite dans la source | **[M]** |
| Dérive de la somme sans relance | contre le traité (2ᵉ éd.) | **Absorbé.** §4.1, `Traité.md:981`, p. 58 : « Sans relance, l'erreur ne croît pas sans borne : **elle se fige** […] La relance de la ligne 11 **ne plafonne donc pas** l'erreur » | **[M]** |
| Contrôleur d'élasticité | « constat de mesure, ne contredit rien » | **Contredit le §7.3 de la 3ᵉ édition**, `Traité.md:1576`, p. 114 : « Le comportement par défaut n'est donc **pas** une oscillation, c'est un dépassement en escalier suivi d'une descente filtrée — et qui cherche une oscillation ne trouve rien à corriger. » **Non tranché** | **[M]**, ouvert |
| `mul_add` | constat de mesure | inchangé — porte sur la machine de construction, pas sur le traité | **[M]** |
| Φ_c | contre le §8.1 et contre le PRD | inchangé, et **cité par la conclusion de la 3ᵉ édition** avec les valeurs mesurées ici (0,173 ; 0,228) | **[M]** |

**Pourquoi le troisième n'est pas tranché, et ce qu'il faudrait.** La même page du
traité publie quatre réglages : fenêtre de stabilisation de 300 s à la baisse,
**nulle à la hausse**, et deux politiques de montée bornant le pas (100 % ou
4 répliques par tranche de 15 s, la plus permissive l'emportant). **Le produit
transpose la première et aucune des trois autres** — le budget de churn ⌊β·T⌋ du
§2.2 les remplace —, et ce sont précisément elles que le traité invoque pour
conclure à l'escalier. L'écart peut donc venir de la transposition incomplète
autant que du traité. Ce qu'il faudrait : transposer les deux politiques de
montée, rejouer
`cargo run -p sim-agents --example diagnostic_elasticite --release`, reclasser.

**Trois citations du PRD que la troisième édition retire ou inverse**, trouvées
en vérifiant les précédentes. Ce ne sont pas des écarts au sens de NF-15 —
aucune mesure n'est en cause — mais des **provenances devenues fausses**, ce que
F2 traite comme un défaut bloquant. Les trois sont corrigées sur place au PRD et
consignées au registre :

1. §1 du PRD citait *« Le livre a donc échangé une ignorance contre une dette »*
   (p. 96). La 3ᵉ édition écrit le contraire, p. 129 : « Le livre n'a donc **pas**
   échangé une ignorance contre une dette : il a proposé, l'auteur a mesuré, et
   la mesure lui est revenue contre. » Ce qui a produit le retournement est la
   phase 6 de ce dépôt.
2. §2.3 du PRD donnait le troisième reste pour *« inchangé par la deuxième
   édition »*, sur l'absence d'estimateur de corrélation ne demandant pas la vue
   globale. La 3ᵉ édition écrit « **la phrase ne tient plus** » et lui oppose
   φ = 0,916 sur 18 000 missions (`Traité.md:1737`, notice 121). Le périmètre du
   produit ne change pas — la corrélation des **fautes** reste une entrée —, mais
   le reste est **rétréci**, pas comblé, et le PRD le dit maintenant.
3. §1 du PRD décrivait l'ouvrage comme « **100 pages**, dont 95 d'argument, les
   Références commençant p. 96 ». Mesuré : 143 pages, conclusion p. 128-129,
   Références p. 130, 24 sections, 123 notices.

Une quatrième provenance, corrigée au passage : le tableau 14 est **p. 77** dans
la troisième édition, non p. 58 (§0, critère de sortie de la phase 3).

### 8 — Les décisions laissées ouvertes par les bâtisseurs

Consignées au registre, section **« Les décisions ouvertes par l'audit du 17 août
2026 »**, chacune avec ce que la mesure établit et ce qu'il faudrait pour
trancher — **comme décisions ouvertes, pas comme faits**. Les quatre touchent une
interface publique ou une liste normative, ce qu'un audit de crate ne doit pas
trancher seul.

1. **Fermer `Proprietes` par le type** (M1, C1). `#[non_exhaustive]` interdit le
   littéral, pas l'affectation de champ ; la structure est `Copy` à quatre champs
   `pub`. Fermer casse `crates/sim-agents/src/pair_a_pair.rs`. Ce que PD12 tient
   quand même est plus étroit qu'annoncé, et la doc porte la mesure depuis
   l'audit. Ligne ajoutée aux réserves du §0.
2. **Remonter dans `sim-agents` les neuf valeurs transcrites dans `sim-viz`**
   (M5, E6). Six dans `VueA::default`, trois dans `VueB::default` ; leur
   provenance réelle est le **§7 du PRD**, pas rien — la vue *transcrit* faute
   d'accesseur, et rien ne tient la transcription en accord. Ligne ajoutée aux
   réserves du §0, avec le renvoi aux lignes du §7 qui font foi.
3. **`ModeleFaute::avertissements` sans appelant** (M1, C4 et D2). La moitié
   `[U]` d'EX-C06 n'est tenue par personne, et l'avertissement de crash corrélé
   **ajouté** par l'audit hérite de la réserve. Ligne ajoutée aux réserves du §0.
4. **Ouvrir ou non `sim_core::hors_perimetre()`** — voir le point 4 ci-dessus.

### 9 — `docs/README.md` et `gauntlet-log.md`

**Vérifié.** `git log --oneline -1 -- gauntlet-log.md` → `4dfc0dc menage` : le
journal de la revue 2.0 a bien été retiré. `git ls-files gauntlet-log.md` ne rend
**rien** et `git status --short` porte `?? gauntlet-log.md` : le fichier présent
à la racine n'est pas suivi, et `head -1` le donne pour « Journal de la boucle —
audit complet du code ». Les deux énoncés sont vrais, chacun sur son objet.

**Écrit.** L'entrée porte le commit du retrait, et l'avertissement ⚠ qui la suit
— déjà posé par l'audit — gagne la différence de statut qui lève réellement
l'ambiguïté : **le premier a été supprimé du dépôt, le second n'y a jamais été
ajouté**, avec la ligne `git ls-files` qui l'établit. Renvoi vers
`bancs/audit-2026-08/`, ce document, le §0.2 du PRD et le registre — c'est là
qu'est ce que la campagne produit de durable, pas dans le journal de session.

### 10 — Les comptes vérifiables

Tous remesurés ; voir le tableau en tête. Corrigés :

| Document | Ce qui était écrit | Mesuré |
|---|---|---|
| `CLAUDE.md`, `README.md` ×2, `docs/SPEC.md` ×3, `docs/DEVELOPPEMENT.md` ×2, `docs/PRD.md` | 447 tests (428 au PRD) | **465** |
| mêmes fichiers | 404 unitaires ; 247 / 91 / 61 / 5 | **422** ; **253 / 96 / 68 / 5** |
| `docs/SPEC.md` §11 | `sim_agents::hors_perimetre()` 19 entrées | **20** |
| `docs/SPEC.md` §11 | `sim_milieu::hors_perimetre()` 9 entrées | **13** |
| `docs/SPEC.md` §11, `CLAUDE.md`, `docs/PRD.md` §0 | quatre oracles non armés | **six** |
| `CLAUDE.md` | réserves du §0 : dix-huit entrées | **22** (quatre ajoutées ici) |
| `CLAUDE.md`, `docs/README.md` | PRD ~2 200 lignes | **2 340** |
| `docs/PRD.md` §1 | traité de 100 pages, Références p. 96 | **143 pages**, Références **p. 130** |

Vérifiés et **exacts, non touchés** : 31 modules de `sim-agents`
(`docs/architecture.md` ×3, `CLAUDE.md`) ; 22 énoncés en dur de l'onglet
« Limites » (`docs/architecture.md`) ; 32 termes de glossaire (`README.md`) ;
quinze oracles au catalogue (`docs/SPEC.md`, `docs/README.md`) ; quatorze DT
(`docs/README.md`) ; quatre mécanismes du ch. 8 sans appelant — EX-A57, EX-M25,
EX-M26, EX-A59 — répartis entre les deux `hors_perimetre()` ; seize `EX-V*` sans
point d'appel sur vingt-trois ; 123 notices, 24 sections, 143 pages.

**Non touchés délibérément : les octets d'empaquetage WASM.** Une construction
finale les fixera. Ils sont à `README.md:114-115` et `CLAUDE.md:284-285`
(1 447 267 compressés / 3 668 599 bruts, construction de 09 h 09), et il en
existe une **troisième** occurrence, périmée et différente, au §0 du PRD
(3 663 058 / 1 445 293, remesure du 13 août). Les trois nombres sont laissés tels
quels ; le §0 du PRD gagne en revanche un ⚠ qui **le renvoie aux deux lignes de
commande du `README.md`** comme seule autorité et donne son couple pour de
l'historique, de sorte qu'un troisième chiffre ne se lise plus comme un troisième
état. *Reste à faire par qui construira.*

---

## Ce que la consolidation laisse ouvert

Au même rang que le reste, parce qu'une liste d'absences périmée est le mensonge
symétrique (PD6).

1. **La migration des 56 renvois de page du PRD n'est pas faite.** La clause
   d'édition est corrigée, les renvois ne le sont pas — sept l'ont été, ceux qui
   étaient mesurés en le corrigeant. Les autres sont ceux de la deuxième édition
   et ne résolvent pas dans le PDF livré. C'est le plus gros reste de cette
   passe, et il est nommé dans F2, dans DT5 et dans `docs/README.md` avec son
   protocole de remesure. Une page du PRD ne se cite pas sans être revérifiée.
2. **La migration des renvois du code n'est pas finie non plus.**
   `grep -rhoE '§[0-9]+(\.[0-9]+)?, p\. [0-9]+' crates/ | sort | uniq -c | sort -rn`
   rendait quatre pages différentes pour le seul §1.2 le 17 août à 08 h 32, et le
   compte bougeait d'une heure à l'autre. Le code n'est pas mon périmètre ; je
   n'ai pas remesuré cette ligne après la passe du second agent, et **le compte
   écrit dans `CLAUDE.md` et `docs/SPEC.md` est celui de 08 h 32**, avec son
   heure.
3. **Le contrôleur d'élasticité n'est pas tranché** contre le §7.3 de la
   troisième édition. Il faut transposer la fenêtre nulle à la hausse et les deux
   politiques de montée avant de savoir si l'écart est du produit ou du traité.
   Consigné comme ouvert, pas comme verdict.
4. **Les quatre décisions de conception restent ouvertes** : `Proprietes` par le
   type, les neuf valeurs de `sim-viz`, `ModeleFaute::avertissements` sans
   appelant, `sim_core::hors_perimetre()`. Aucune n'est tranchée ici, et aucune
   ne peut l'être sans toucher `crates/`.
5. **Les octets d'empaquetage WASM sont périmés en trois endroits**, dont deux
   volontairement laissés et un — le §0 du PRD — laissé aussi mais désamorcé par
   un renvoi. Une construction et deux lignes de `printf` referment le point.
6. **Le §12 A du PRD n'a pas été revérifié.** Sa table de correspondance porte
   des mentions « (2ᵉ éd.) » sur des **sections**, non des pages ; elles restent
   justes comme attribution de section, et je ne les ai pas confrontées une à une
   au sommaire de la troisième édition. Ce qui trancherait : rejouer
   `d.get_toc()` contre les 24 lignes de la table.
7. **Rien n'a été vérifié à l'écran.** Aucun correctif d'interface de cette
   campagne n'a été vu rendu ; les six listes de l'onglet « Limites » sont
   établies par le code et par `cargo test`, pas par un œil. NF-07 reste non
   mesurée, pour la raison du §0.
8. **La suite n'a pas été rejouée après mes dernières écritures**, ni après
   celles du second agent postérieures à 10 h 21. Les mesures de 09 h 49 et
   09 h 50 portent sur l'arbre de cette heure-là ; elles ne portent sur aucune
   autre, et c'est pourquoi elles sont horodatées. Aucun `.rs` n'a été touché par
   cette passe, donc aucun de mes changements ne peut avoir cassé un test — mais
   ce n'est pas la même chose que de l'avoir mesuré.
