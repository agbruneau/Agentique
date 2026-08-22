# Journal de la boucle — audit complet du code

Technique : gauntlet loop (bâtisseur / critique, comparaison à l'aveugle).
Objectif : *auditer le code en totalité et corriger toutes les anomalies identifiées.*

**Barre** — `bancs/dt1-flottant/VERDICT.md`. Un rapport d'audit tient la barre s'il
mesure au lieu de raconter, cite sa provenance, et tire la conséquence de ce qu'il
a mesuré.

**Budget fixé avant lancement** : deux vagues + une passe de lissage, plafond
≈ 31 agents. La boucle s'arrête au budget, sur victoire à l'aveugle, ou sur deux
tours consécutifs sans gain.

**Ligne de base, 17 août 2026** — `cargo clippy --workspace --all-targets --release`
sort à 0, sans avertissement. Les anomalies restantes ne sont donc pas de niveau
lint.

**Limite connue de l'aveuglement** : la barre est un document interne au dépôt et
porte sur un autre sujet que les rapports d'audit. Retirer les étiquettes cache
*lequel des deux on cherche à promouvoir*, pas *lequel est lequel*. Le juge tranche
sur la rigueur probatoire, seul axe où les deux documents sont réellement
comparables. C'est consigné plutôt que masqué.

## Découpage — cinq morceaux, disjoints par fichier

| # | Morceau | Portée |
|---|---|---|
| M1 | `crates/sim-core/` | moteur, horloge, aléa, oracles, faute, détecteur, familles, registre, vérification |
| M2 | `crates/sim-milieu/` | journal partitionné, réplication, latence, groupe, plan de contrôle, historique, quota |
| M3 | `crates/sim-agents/` — mécanismes | les modules du traité : stigmergie, propagation, accord, cascade, élasticité, soupçon… |
| M4 | `crates/sim-agents/` — scénarios & preuves | essaim, scénarios, gouvernance, conformité, dettes, `bin/`, `examples/`, `tests/` |
| M5 | `crates/sim-viz/` + cohérence documentaire | interface, et concordance `README.md` / `docs/*.md` avec le code |

---

## Vague 1 — tour 1

### M1 · `sim-core` — bâtisseur

12 anomalies corrigées, 6 identifiées et laissées ouvertes avec motif. Suite
`sim-core` : 86 → 91 tests, aucun retiré ni relâché. Les quatre correctifs à
conséquence mesurable sont exécutés contre le code de `HEAD` dans le rapport,
sorties de panique citées.

Les deux qui changent un résultat numérique :

- `famille.rs:100` — `i * nb` en `u32` déborde à n ≥ 65 536 : l'agent 99 999
  était rangé dans la famille 7 049 au lieu de 49 999. Touche EX-C19, donc Φ_c.
- `faute.rs:292` — `crash_baie` / `crash_centre` tirés par membre : une baie de
  20 machines n'en frappait que 18, et tombait avec p = 1,00 là où le réglage
  déclarait 0,50. Mesuré : 400 chutes sur 400 tirages avant, 204 après.

**Trouvaille d'environnement, hors code** : `cargo test` échoue à l'édition de
liens dans le `target/` du dépôt — `ld.exe` ne retrouve aucun des `.o` qu'il
vient de produire, parce que le chemin contient un « é » (`3 - Traité`). Toutes
les mesures ont donc été prises avec `CARGO_TARGET_DIR` sur un chemin ASCII. ✎ *Motif faux, corrigé le
22 août 2026 : ce n'est pas l'accent du chemin mais la **synchronisation OneDrive** du
`target/` qui casse l'édition de liens — un workspace d'essai sous `…/3 - Traité/`, même
accent et même espace, s'édite sans un mot hors de OneDrive. Le déroutement reste le bon
remède ; seul son motif était mal attribué. Mesure à l'appui à
[`docs/DEVELOPPEMENT.md`](docs/DEVELOPPEMENT.md).* La
commande que `CLAUDE.md` donne comme *la* commande de suite complète ne passe
pas telle quelle sur cette machine.

Coût : ~254 k jetons, 80 appels d'outil, 19 min.

### M2 · `sim-milieu` — bâtisseur

16 anomalies corrigées, 3 laissées ouvertes. Suite `sim-milieu` : 56 → 61 tests.

- `groupe.rs:92` — `Protocole::tours()` comptait des aller-retours (2/4) là où
  EX-M22 impose l'unité de l'annexe B.1, qui chiffre 4 et 8.
- `groupe.rs:381` — `suivre_vivacite` ouvrait une attente par sondage et
  `satisfaire` n'en retirait qu'une : les autres échoyaient en violations
  fabriquées par la seule fréquence d'appel.
- `journal.rs:730` — l'oracle EX-M10, écrit pour un défaut mesuré sur 36,5 %
  des compactages, n'avait aucun test. Contre-épreuve exécutée : frontière
  retirée → le nouveau test échoue.
- `lib.rs:55` — `hors_perimetre()` taisait quatre absences, dont le module
  `format` entier.

### M3 · mécanismes de `sim-agents` — bâtisseur

23 anomalies corrigées, 8 laissées ouvertes. Suite `sim-agents` : 290 tests.

**Trouvaille qui déborde le morceau, confirmée indépendamment par M2 et par
moi-même** : `Traité.pdf` est à la **racine**, pas dans `docs/`, et fait
**143 pages** — `CLAUDE.md` en annonçait 116 et donnait un chemin qui n'existe
pas. Toutes les provenances de page du dépôt pointaient donc sur une autre
édition. M3 a relocalisé les siennes par recherche de la phrase citée dans le
PDF, protocole donné au rapport, et signale 18 pages également périmées dans
les morceaux voisins.

Deux correctifs de fond :

- `elasticite.rs:275` — τ, déclaré « mesuré, jamais saisi » par EX-A25,
  recopiait en fait `disponibilite_initiale_s`. Mesure réelle livrée, plus un
  test qui sépare les deux.
- `echantillonnage.rs:205,215,250` — trois indexations hors bornes atteignables
  depuis des champs publics.

Et deux endroits où le code **affichait un énoncé que la 3ᵉ édition qualifie de
faux** : la relance de la ligne 11 (`agregation.rs`) et le seuil de
`consensus_lineaire.rs:86`.

### M5 · `sim-viz` + concordance documentaire — bâtisseur

15 anomalies corrigées, 3 laissées ouvertes.

Le compte de tests annoncé partout dans la documentation était périmé sur six
chiffres à la fois : **428/385/239/86/56/4 annoncés, 447/404/247/91/61/5
mesurés**. `CLAUDE.md` corrigé sur le chemin du PDF et sur les 143 pages.
NF-08 remesurée sur un empaquetage refait : 1 445 512 octets compressés.

- `sim-viz/src/lib.rs:902` — EX-V23 absente de la liste d'absences alors que le
  §0 du PRD écrit que l'onglet la déclare (PD6).
- `sim-viz/src/scenario_b.rs:29-32` — le `//!` promet de ne jamais choisir une
  valeur ; `VueB::default` imposait n = 16 contre 64.

Coût cumulé des trois : ~1,04 M jetons.

### M4 · scénarios & preuves de `sim-agents` — bâtisseur

17 anomalies corrigées, 5 laissées ouvertes. Suite `sim-agents` : 282 → 290.

Le morceau était mandaté sur les **tests qui ne peuvent pas échouer**, et il en
a trouvé :

- `conformite.rs:261` — un `clamp(0,1)` contredisait la doc du champ **et**
  rendait vrai par construction le test du zéro de Φ_c. Valeur brute réelle :
  **−0,2**. Le clamp masquait un signe négatif que le test était censé
  surveiller. Touche directement le résultat de la phase 6.
- `tests/sortie_phase_2.rs:130` — le critère de sortie (5) reposait sur
  `assert_eq!(pannes, 0)`, vrai par construction du type. Volet réfutable ajouté.
- `gouvernance.rs:349` — assertion impliquée par les deux lignes qui la
  précèdent.
- `partage.rs:33` — encodage `{:.9}` : le dépôt unitaire de
  `Params::verrouillage()` traversait le lien EX-V09 en 5 chiffres significatifs
  sur 17, sans refus.

Laissée ouverte, et c'est la plus lourde : `dettes.rs:186` — `verdicts` efface
**7** bornes là où le réglage n'en invalide que **4**. Corriger déplace le
critère de sortie de la phase 6 ; consigné pour arbitrage.

M4 relève aussi que `CLAUDE.md` annonçait **quatre** oracles non armés alors
qu'il y en a **six**, et que le PRD désigne comme source la **deuxième** édition
alors que le dépôt ne contient que la troisième.

Coût : ~335 k jetons.

### Vague 1 — bilan des bâtisseurs

**69 anomalies corrigées, 23 identifiées et laissées ouvertes** avec motif.
Suite complète : 428 → **447 tests**, aucun retiré ni relâché. Clippy et
rustdoc restent à zéro sur les quatre crates.

Coût de la vague : ~1,62 M jetons, 549 appels d'outil.

Les cinq critiques sont lancés : contexte neuf, choix forcé A/B écrit **avant**
d'ouvrir le dépôt, puis vérification indépendante — contre-épreuve exigée sur
les tests déclarés renforcés, réétalonnage exigé sur les pages relocalisées.

### M1 · `sim-core` — critique, tour 1

**Verdict : A — le rapport d'audit bat le verdict DT1.** Jugement écrit avant
ouverture du dépôt. Motif : le rapport porte la provenance sur chaque
affirmation prise une par une et range huit choses non établies au même rang que
les douze établies ; le verdict DT1, lui, publie un seul des hachages qui
fondent son tableau de parité et étend une donnée montrée à six données non
montrées.

**Écart retenu sur le perdant** (le verdict DT1) : « le lecteur ne peut ni
vérifier ligne à ligne ni repérer laquelle des lignes serait fausse ; il ne peut
que refaire le banc en entier ou croire. » — C'est la barre qui se fait
observer, pas le produit. Consigné, non actionné : le mandat porte sur le code.

**Vérification** — les quatre sorties citées se reproduisent au caractère près,
graine et paramètres compris. Aucune régression en aval. Deux affirmations
accessoires prises en défaut, et **six anomalies que le bâtisseur n'avait pas
vues**, dont trois de fond :

- `detecteur.rs:59-61` — la doc affirme que `#[non_exhaustive]` tient PD12 « par
  le type ». Il interdit le littéral, pas l'affectation de champ : `Proprietes`
  est `Copy` à quatre champs `pub`. Exactitude fabriquée depuis une crate
  externe, mesurée.
- `verification.rs:160-187` — à δ ≥ 2 ou δ = NaN, `N` sature à 0 et
  `Campagne::conclure()` rend un verdict EX-C18 complet, avec son autorité, sur
  **zéro exécution**.
- `moteur.rs:281-304` — le commentaire promet que la violation précède le
  budget. Elle précède `BudgetEvenements`, mais pas `Demande` ni `BudgetTemps` :
  une violation **déjà au registre** est enterrée par l'arrêt.
- `faute.rs:452-458` — le correctif A1 du bâtisseur a changé le dénominateur de
  deux taux et laissé le seuil d'avertissement calibré sur l'ancien. Sous-avertit
  dans le sens grave.

Détail complet : [`bancs/audit-2026-08/M1-critique.md`](bancs/audit-2026-08/M1-critique.md).

Coût : ~237 k jetons.

### M2 · `sim-milieu` — critique, tour 1

**Verdict : A — le rapport d'audit bat le verdict DT1.** Motif : le rapport
pousse jusqu'à la contre-épreuve — retirer le correctif, montrer le test qui
tombe —, « seule forme qui établit qu'un test garde quelque chose ».

**Écart retenu sur le perdant** (le verdict DT1) : le fait pivot du document —
`mul_add` divergeait au premier passage, coïncide au second — est le seul dont
aucune sortie n'est reproduite. L'interdiction la mieux argumentée repose sur la
mesure la moins vérifiable.

**Vérification** — contre-épreuve reproduite à l'identique ; les cinq pages
réétalonnées reproduites indépendamment par `pypdf` (14, 26, 26, 65, 96) ; page
de titre lue : « 15 août 2026 — troisième édition ». Deux affirmations prises en
défaut, dont un cardinal faux (« dix entrées existantes » — il y en avait neuf).

**Cinq anomalies neuves**, dont trois de fond :

- `groupe.rs:358` — l'oracle de sûreté EX-M23 a une **branche de violation
  morte** : aucune suite d'appels publics ne peut laisser un non-membre
  propriétaire. Et son test `une_partition_na_quun_proprietaire` passerait avec
  un corps vide. La crate sait nommer ce cas ailleurs (`journal.rs:694`) ; ici
  la doc affirme le contraire.
- `historique.rs:75` — le refus « non négociable » du régime `NonVerifiable` se
  contourne par `Compte::fiabilite`, publique, qui rend le même rapport sans
  refus **et sans payer la consultation**.
- `journal.rs:457` — `valider` appelé deux fois sur la même écriture facture
  deux tours et pousse un doublon dans `latences_durabilite` : biaise le ℓ₉₉
  d'EX-M09.

Détail : [`bancs/audit-2026-08/M2-critique.md`](bancs/audit-2026-08/M2-critique.md).

Coût : ~217 k jetons.

### M5 · `sim-viz` + docs — critique, tour 1

**Verdict : B — le rapport d'audit.** Ordre inversé par rapport à M1 et M2 ;
même issue. Motif : « A raisonne juste et tire bien ses conséquences, mais il
livre un tableau de verdicts là où B livre des sorties. »

**Écart retenu sur le perdant** (le verdict DT1) : « le document qui exige
ailleurs qu'une grandeur porte sa provenance imprime ici sa déduction dans la
même typographie que ses mesures. »

**Vérification** — 447 = 404 + 43, réparti 247/91/61/5, reproduit chiffre pour
chiffre. Empaquetage reproduit à l'octet près. 143 pages, 123 notices, 19 SVG,
16 `EX-V*`, 17 filtres de `README` : tous exacts. Deux défauts, et le second est
le plus instructif de la vague :

- `CLAUDE.md:245` porte encore `1 445 293`, le chiffre que le rapport lui-même
  déclare périmé, dans un fichier qu'il a édité trois fois. Correction annoncée
  sur deux occurrences, faite sur une.
- **Le chiffre installé est déjà périmé par les propres correctifs de
  l'auteur** : reconstruit à l'instant, l'empaquetage rend 1 446 247, pas
  1 445 512 — la construction datait de 08 h 13, `lib.rs` a été édité à 08 h 25.
  Le défaut diagnostiqué (« l'empaquetage était vieux de deux révisions »)
  reproduit à une révision.

**Quatre anomalies neuves**, dont deux qui contredisent la table du SPEC :

- `docs/SPEC.md:681` — « zéro définition de scénario » est faux :
  `scenario_a.rs:104-112` pose six valeurs de paramètre qui ne viennent d'aucun
  `sim-agents`.
- `docs/SPEC.md:680` — « zéro logique de simulation » est contredit par
  `scenario_b.rs:1340-1353`, dont le rustdoc l'avoue en propres termes et que
  l'onglet « Limites » ne déclare pas.

Détail : [`bancs/audit-2026-08/M5-critique.md`](bancs/audit-2026-08/M5-critique.md).

Coût : ~222 k jetons.

### M4 · scénarios & preuves — critique, tour 1

**Verdict : B — le rapport d'audit.** Quatre sur quatre.

**Écart retenu sur le perdant** : identique aux trois autres — un seul couple de
bits publié pour un tableau de quatorze lignes. Quatre critiques en contextes
séparés, sans concertation possible, ont désigné le même défaut de la barre.

**Contre-épreuves faites sur les cinq tests renforcés : tous échouent quand on
casse le mécanisme.** Le plus net : `critere_5_loscillation_diverge_sans_aucune_panne`
tombe au volet ajouté, alors que les trois assertions d'origine passent encore —
l'ancien test aurait laissé passer. Quatorze pages réétalonnées indépendamment,
aucune fausse.

**Quatre anomalies neuves, plus une provenance sous-déclarée** :

- `tests/sortie_phase_6.rs:136-139` — le repli présenté comme « la seule chose
  que ce point garde de réfutable » est **vide** : mesure remplacée par une
  constante, le test passe. `test … ok`, contre-épreuve citée.
- `scenario.rs:468,532` — le test ajouté *contre les provenances fausses* se
  compare à lui-même : une page fausse portant la bonne mention d'édition passe.
- `scenario_m.rs:41` — la provenance certifiée sous-déclare l'épissure : ce qui
  vient de la p. 5 n'est pas une incise, c'est toute la proposition principale.

Le critique a restauré le dépôt à l'octet près et l'a établi par empreinte
SHA-256 du `git diff` contre sa ligne de base — vérification qui a rattrapé un
premier restaure incomplet.

Détail : [`bancs/audit-2026-08/M4-critique.md`](bancs/audit-2026-08/M4-critique.md).

Coût : ~239 k jetons.

### M3 · mécanismes — critique, tour 1

**Verdict : B — le rapport d'audit.** Cinq sur cinq.

**Vérification** — le folio imprimé recoupé à l'index physique sur 15 pages ; les
**14 relocalisations sont toutes justes**, dont huit revérifiées par ancre
textuelle. 290 tests, clippy muet, rustdoc propre.

**Sept affirmations prises en défaut**, dont trois qui comptent :

- « Cinq tests ajoutés, un par chemin » — il y en a **trois**, et le chemin sans
  test est précisément celui dont la correction est incomplète.
- **Trois des cinq correctifs ne couvrent qu'un sens.** Ils gardent
  l'agrandissement d'un champ public, pas le rétrécissement. Trois paniques
  mesurées : `echantillonnage.rs:228`, `:264`, `accord.rs:393`.
- La clause de SPEC invoquée n'est pas celle appliquée : `saturating_sub(1)` est
  une coercition silencieuse, pas « un refus rendu à l'appelant ».
- Et un joli retour de bâton : le rapport reproche à `CLAUDE.md` un chiffre faux
  (« dernière notice 120 ») alors que c'est **`CLAUDE.md` qui a raison — 123**.

**Sept anomalies neuves.** La plus lourde :

- `stigmergie.rs` — γ ≤ 0 n'est ni écrêté, ni averti, ni refusé : `depot()` rend
  `inf` puis `NaN`, et **le `NaN` se propage dans les `partial_cmp().unwrap_or(Equal)`
  du tri des traces, où il détruit l'ordre déterministe — contre PD1.**
- `accord.rs:272` et `propagation.rs:113` — trois paniques de plus par champ
  public, dont une à 120 lignes du site que le rapport venait de corriger.

Détail : [`bancs/audit-2026-08/M3-critique.md`](bancs/audit-2026-08/M3-critique.md).

Coût : ~184 k jetons.

---

## Vague 1 — verdict d'ensemble

**Cinq morceaux, cinq victoires à l'aveugle.** Le rapport d'audit l'emporte sur
le verdict DT1 aux cinq tours, dans les deux ordres de présentation (A pour M1
et M2, B pour M3, M4 et M5).

**Les cinq critiques ont désigné le même écart chez le perdant**, en contextes
séparés et sans concertation possible : le verdict DT1 publie **un seul
hachage** — `f4ec27f3f92a91ac` — pour un tableau de quatorze lignes, et étend
« même constat pour les six autres » à six données jamais montrées. Sa
conclusion la plus lourde, le retournement de `mul_add` entre deux passages, ne
cite aucun artefact d'aucun des deux. C'est une observation sur la barre, pas
sur le produit ; elle est consignée et non actionnée, le mandat portant sur le
code.

**Ce que les critiques ont rapporté sur le produit** : les correctifs de la
vague 1 tiennent — sorties reproduites au caractère près, contre-épreuves
concluantes sur les cinq tests renforcés, 28 pages réétalonnées indépendamment
sans une seule fausse. Mais ils ont pris les bâtisseurs en défaut sur
**onze affirmations** et trouvé **vingt-six anomalies neuves**, dont au moins
quatre de premier ordre :

1. `stigmergie.rs` — γ ≤ 0 produit un `NaN` qui détruit l'ordre déterministe du
   tri des traces (PD1).
2. `verification.rs` — un verdict EX-C18 complet rendu sur **zéro exécution**.
3. `groupe.rs:358` — l'oracle de sûreté EX-M23 a une branche de violation morte,
   et son test passerait avec un corps vide.
4. `tests/sortie_phase_6.rs` — le repli « réfutable » du critère est vide :
   mesure remplacée par une constante, le test passe.

Coût de la vague : ~1,10 M jetons pour les critiques, ~2,72 M au total.
Dix agents dépensés sur un plafond de trente et un.

**La boucle a atteint sa condition de sortie sur la qualité** — victoire à
l'aveugle partout. Elle ne l'a pas atteinte sur le mandat : vingt-six anomalies
sont identifiées et non corrigées. La vague 2 les prend.

## Vague 2 — tour 2

Chaque bâtisseur a reçu le jugement de son critique comme liste de travail, avec
mandat de reproduire chaque preuve **avant** de corriger, puis d'établir que le
correctif la fait disparaître.

**Les vingt-six anomalies neuves sont traitées. Aucune n'a été écartée.**

Trois tours méritent d'être lus, parce que le bâtisseur y a fait mieux que
d'exécuter la consigne.

### M1 — un arbitrage rendu contre le diagnostic du critique, sur mesure

Le critique tenait que le correctif du tour 1 avait changé le dénominateur de
`crash_baie` et `crash_centre` en laissant le seuil calibré sur l'ancien. La
mesure dit autre chose : le taux **par acteur** est identique dans les trois
régimes — 0,0928 / 0,0905 / 0,0903 pour un réglage de 0,09 —, donc la somme
reste le majorant par union qu'elle a toujours été. Ce que le tour 1 a changé
est la **corrélation** : 928 vidages complets de la population contre **zéro**,
à espérance égale. D'où un avertissement de *régime*, sans seuil, plutôt qu'un
chiffre que ni le §3.3 ni le PRD ne donnent. Le cas grave du critique déclenche
maintenant.

`sim-core` : 91 → 96 tests.

### M3 — le diagnostic du critique était un cran trop étroit

Le critique voyait cinq champs publics mal gardés. Le banc de reproduction du
bâtisseur montre **deux objets qui portent la population sans rien qui les
lie** : quatre paniques de plus se déclenchent sans mutation d'aucun champ,
simplement en donnant à un mécanisme un `ServiceDePairs` plus grand que lui.

D'où deux remèdes, chacun unique de sa sorte, au lieu de cinq gardes :
la dimension cesse d'exister en double — `SeuilDeQuorum::n` et `Rumeur::n`
**supprimés**, dérivés de leur table ; et l'identifiant de pair est borné **là
où il entre**, aux 4 sites de tirage plutôt qu'aux 12 sites d'indexation. Le
banc de reproduction du critique, inchangé, **ne compile plus**.

Le `NaN` qui détruisait l'ordre déterministe (PD1) est traité par l'ordre total
— cinq `partial_cmp(…).unwrap_or(Equal)` deviennent `total_cmp`, qui couvre
toutes les sources de `NaN` et pas seulement γ, en stdlib, bit-exact, compatible
NF-02. γ=0,9 et γ=1 restent identiques au dernier bit.

### M2 — deux correctifs qui rendent le défaut inexprimable

Le contournement du refus `NonVerifiable` est fermé **à la racine** : le refus
quitte `poids` pour `Compte::fiabilite`, par où passent les trois voies
publiques. Et le champ `p` de `groupe.rs` est **supprimé**, dérivé de
`attribution.len()` : le désaccord entre `parallelisme_utile` et
`debit_instantane` n'est plus représentable, la reproduction du critique ne
compile plus.

Constat de mesure honnête, porté au rapport : une sonde qui panique sur toute
re-validation n'a **jamais** déclenché sur les sept binaires d'intégration. Le
biais du ℓ₉₉ d'EX-M09 était **latent, non actif** — le correctif ne déplace
aucune mesure publiée.

### M4 et M5

M4 a renforcé les deux tests qui ne pouvaient pas échouer, chacun établi par
contre-épreuve. Le test des provenances interroge maintenant `Traité.md` et
retrouve la thèse mot pour mot ; trois contre-épreuves le font tomber. Le repli
du critère de sortie de phase 6 est remplacé par deux clauses dont l'une réfute
*toute* constante — la grandeur dépend de l'exécution, trois graines donnant
trois valeurs distinctes. La mesure a d'ailleurs écarté une troisième clause
envisagée : la grandeur n'est pas monotone en la part.

M5 a corrigé les sept entrées, et relevé au passage que les neuf valeurs de
paramètre posées dans `sim-viz` **ne sont pas sans provenance** — ce sont les
défauts des tableaux du §7 du PRD, transcrits faute d'accesseur ; seule la
graine n'en vient pas. Une sixième section de l'onglet « Limites » déclare
désormais l'hypothèse réimplantée dans la vue, comme PD6 l'exige.

### Vérification de la vague, mesurée sur la suite complète

```
cargo test --workspace --release   →  465 passed, 0 failed
cargo clippy --workspace --all-targets --release  →  exit 0, aucun diagnostic
cargo doc --workspace --no-deps    →  exit 0, aucun lien cassé
```

428 tests documentés en début de campagne, 447 mesurés à la vague 1, **465**
aujourd'hui. Aucun test retiré ni relâché sur les deux vagues.

Coût de la vague : ~1,13 M jetons. Quinze agents dépensés sur trente et un.

---

## Phase 5 — lissage

Deux agents neufs, jeux de fichiers disjoints. L'un recoud les coutures du code
— registres qui divergent, doublons, appelants qui compilent mais ont perdu le
sens, registres de langue. L'autre consolide `docs/PRD.md` et
`docs/decisions.md`, que les dix agents avaient interdiction de toucher et où
ils ont donc empilé ce qu'ils y renvoyaient.

Aucun des deux ne rouvre un arbitrage déjà tranché ; la liste des huit
arbitrages fermés leur est donnée avec leur motif.
