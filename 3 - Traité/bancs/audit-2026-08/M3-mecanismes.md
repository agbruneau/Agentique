# M3 — les mécanismes du traité (`crates/sim-agents/src/`)

Périmètre : `accord.rs`, `adhesion.rs`, `agregation.rs`, `agregat_fenetre.rs`,
`alignement.rs`, `allocation.rs`, `arbitrage.rs`, `cascade.rs`, `causalite.rs`,
`consensus_lineaire.rs`, `cycle_de_vie.rs`, `deliberation.rs`, `directive.rs`,
`echantillonnage.rs`, `elasticite.rs`, `pair_a_pair.rs`, `propagation.rs`,
`reconfiguration.rs`, `soupcon.rs`, `stigmergie.rs`, `taux_de_base.rs`,
`usl.rs` — **11 167 lignes** (`wc -l`, état livré au tour 2 ; 10 846 à la fin du
tour 1, et le chiffre de 10 611 initialement porté ici était antérieur aux
corrections du tour 1 — cf. Tour 2, G-g).

**Tous les `fichier:ligne` de ce rapport désignent le code livré**, recalés à la
fin du tour 2. Seule exception, signalée sur place : le tableau « Code hors de
mon morceau », dont les fichiers sont corrigés en parallèle par une autre passe.

## Le banc de provenance

Toute provenance de page a été localisée dans `Traité.pdf`, et non supposée.
Protocole : extraction du texte page par page, normalisation (apostrophes
typographiques, césures, blancs), puis recherche de la phrase citée.

```python
import pymupdf, re
d = pymupdf.open('Traité.pdf')
norm = lambda s: re.sub(r'\s+', ' ', re.sub(r'-\n', '', s.replace('’', "'")))
txt = [norm(d[i].get_text()) for i in range(d.page_count)]
find = lambda s: [i + 1 for i, t in enumerate(txt) if norm(s) in t]
```

**Le numéro imprimé coïncide avec l'index physique** — vérifié sur les pages 2,
3, 4, 5, 11, 16, 59, 143, dont la dernière ligne porte son propre numéro. Une
page trouvée par ce banc est donc la page à citer, sans décalage de liminaires.

### Mesure

| Grandeur | Valeur |
|---|---|
| `Traité.pdf`, 3ᵉ édition, horodaté 15 août 2026 | **143 pages** |
| Table des matières intégrée | 8 chapitres, 24 sections |
| Dernière notice de la bibliographie | **123** (p. 143, « 123. Commission européenne… »), sans trou |

Le fichier est à la **racine** du dépôt, non dans `docs/`.

### Conséquence

`CLAUDE.md` déclare « **116 pages** » et le chemin `docs/Traité.pdf`. Les deux
sont faux contre le fichier. C'est la cause racine de l'anomalie A1 : la
pagination citée dans le code ne pouvait pas être juste, puisque la référence
qui devait la contraindre annonce un autre document.

---

## Anomalies corrigées

### A1 — Toutes les provenances de page du morceau désignent une autre édition

**Où** — 18 sites dans 9 fichiers.

**Preuve** — chaque phrase citée a été localisée par le banc ci-dessus. Aucune
ne se trouve à la page annoncée ; l'écart va de 2 à 37 pages.

| Fichier:ligne | Citation | Page annoncée | Page mesurée | Ancre localisée |
|---|---|---|---|---|
| `stigmergie.rs:7`, `:426`, `:688`, `:689`, `:951` | §1.2 | 13 | **16** | « il campe à distance bornée » |
| `agregation.rs:3` | §4.1 | 47 | **58** | « Le résultat n'est pas en retard, il est faux » (corps ; reprise en exergue p. 59) |
| `usl.rs:3` | conclusion | 93 | **130** | « L'ouvrage n'a pas dit comment » |
| `adhesion.rs:24` | §1.3, algorithme 3 | 17 | **21-22** | bloc « Algorithme 3 — » p. 21 ; « deux propriétaires distincts pour la même clé » p. 22 |
| `adhesion.rs:35` | conclusion | 94 | **129** | « le seul recours reste l'idempotence de l'effet » |
| `agregat_fenetre.rs:27` | §7.1 | 75 | **104** | « esquisses fusionnables » ; Tableau 18 p. 104 |
| `alignement.rs:12` | §1.2 | 10 | **12** | Vicsek, « β ≈ 0,45 » |
| `allocation.rs:22` | §5.2, tableau 15 | 61 | **80 / 81** | Figure 5.2 p. 80 (« c'est la borne à battre », « 2,61 », « 5,43 ») ; Tableau 15 p. 81 |
| `allocation.rs:117` | §5.2 | 63-64 | **78** | « sans modèle des arrivées futures », « 3-compétitif », « aucun allocateur » |
| `allocation.rs:213` | §7.3 | 93 | **116** | « décider combien d'agents viser […] jamais lequel » |
| `cascade.rs:3` | §6.1 | 73 | **91** | la thèse est le **titre de la figure 6.1** : « AUCUN AGENT N'EST TOMBÉ, ET L'ESSAIM S'EFFONDRE » |
| `cascade.rs:25` | §6.1 | 73 | **90** (corps) **/ 91** (figure) | « la cascade est complète en trois générations » |
| `taux_de_base.rs:20` | figure 7.2 / tableau 19 | 79 / 82 | **107 / 110** | « une sonde presque parfaite […] presque toutes fausses » p. 107 |
| `taux_de_base.rs:201` | figure 5.1 | 60 | **73** | Figure 5.1 |

**Changé** — les 18 sites portent la page mesurée. `cascade.rs:3` cite désormais
la figure, puisque la phrase est son titre et non une phrase du corps.

**Conséquence** — F2 est rétablie sur le morceau. Une page fausse n'est pas une
imprécision : elle envoie le lecteur sur un autre texte, et c'est le seul contrôle
qui permet de vérifier qu'un chiffre du code vient bien du traité.

---

### A2 — `agregation.rs` affirme que la relance plafonne l'erreur ; le traité affirme le contraire

**Où** — `agregation.rs:33` (variante `Ligne11Relance`), `:53-58` (libellé
affiché), `:236` (commentaire de `PushPull::cycle`), `:638-645` et `:696-701`
(documentation du critère 3 et son assertion).

**Preuve** — §4.1, p. 58 :

> Sans relance, l'erreur ne croît pas sans borne : elle se fige. […] **La relance
> de la ligne 11 ne plafonne donc pas l'erreur** : elle réinjecte de la
> dispersion à chaque période, de sorte que son maximum croît avec la durée
> d'observation là où l'erreur sans relance est acquise une fois pour toutes.

Le code écrivait, dans le texte que l'interface affiche :

> ligne 11 — la relance **plafonne** l'erreur accumulée

La documentation du test était en outre en contradiction avec ses propres
assertions : elle annonçait « avec C = ∞, elle dérive sans borne » au-dessus de
trois lignes qui vérifient que la dérive **se fige**.

**Changé** — les cinq sites portent l'énoncé du traité. Le test est renommé
`critere_3_la_relance_ne_plafonne_pas_lerreur_elle_la_fait_croitre`, et il gagne
l'assertion qui manquait — celle qui rend l'énoncé réfutable :

```rust
let avec_court = executer(Some(50), 300).derive_max;
assert!(avec.derive_max > avec_court, …);
```

**Mesure** — l'assertion passe : `derive_max` sous relance croît de 300 à
1 200 cycles. L'énoncé de la 3ᵉ édition est donc **retrouvé** et non cité
(NF-15). Aucune assertion n'a été retirée ni relâchée.

---

### A3 — `consensus_lineaire.rs` affiche une borne que le traité qualifie d'énoncé faux

**Où** — `consensus_lineaire.rs:86-93` (`Mode::Moyeu::avertissement`, texte
d'interface) et `:377-386` (documentation du test).

**Preuve** — §3.1, p. 42 :

> la borne suffisante devient τ < π/(4(n − 1)) — à n = 100, **7,933 × 10⁻³**
> unité de temps du protocole […]. L'arrondi de π/(4n) donnerait 7,9 × 10⁻³, que
> la borne réellement écrite dépasse de 0,42 % : **un arrondi présenté comme une
> borne stricte est un énoncé faux**, non une imprécision.

L'avertissement du produit affichait « moins de 7,9 × 10⁻³ ». Le test du même
fichier prouvait déjà que c'est faux (`assert!(moyeu_a_100 > 7.9e-3)`) et
présentait l'écart comme ouvert contre le PRD — la 3ᵉ édition l'a tranché.

**Changé** — l'avertissement porte 7,933 × 10⁻³ et la raison. La documentation du
test cite la résolution du traité au lieu de rouvrir l'écart. Assertion ajoutée
sur le dépassement de 0,42 %, et l'assertion `contains("7,9")` — que « 7,9 × 10⁻³ »
seul satisfaisait — est resserrée en `contains("7,933")`.

**Conséquence** — le seul texte du morceau qui contredisait frontalement le traité
sur un chiffre a disparu, et le test ne peut plus passer si l'arrondi revient.

---

### A4 — `elasticite.rs` déclare absente une provenance que le traité publie

**Où** — `elasticite.rs:128-140` (`Params::FENETRE_STABILISATION` et sa
documentation), `:78-81` (commentaire des défauts), `:443` (test).

**Preuve** — §7.3, p. 114 :

> Le paramètre qui l'empêche est la fenêtre de stabilisation, et **la même page
> en publie les valeurs par défaut : 300 s à la baisse, 0 s à la hausse**.

Le code déclarait :

```rust
pub const FENETRE_STABILISATION: &'static str =
    "provenance absente — la page qui documente le mécanisme ne publie pas ce défaut (F1)";
```

et rangeait `fenetre_descente_s: 300.0` parmi « les quatre valeurs […] **décisions
du produit sans provenance dans le traité** (F1) ». La valeur du code **est** celle
du traité — 300,0 — et son commentaire dit qu'elle n'en vient pas.

**Changé** — la constante porte la provenance (§7.3, p. 114) **et** ce qui n'est
pas transposé : la fenêtre nulle à la hausse et les deux politiques de montée
(100 % ou 4 répliques par tranche de 15 s), que le budget de churn ⌊β·T⌋ du §2.2
remplace. Le commentaire des défauts ne range plus que trois valeurs sous F1. Le
test `la_fenetre_de_stabilisation_declare_son_absence_de_provenance` devient
`la_fenetre_de_stabilisation_porte_sa_provenance_et_ce_quelle_omet` et vérifie
quatre choses au lieu d'une : la valeur du défaut, sa section, sa page, et la
déclaration de ce qui manque (PD6).

**Conséquence** — F1 déclarait une absence là où il y avait une source ; c'est le
mensonge symétrique de PD6, et il faisait passer une valeur documentée pour un
choix arbitraire.

---

### A5 — `elasticite.rs` : τ « mesuré, jamais saisi » recopiait la valeur saisie

**Où** — la mesure est en `elasticite.rs:258-261`, et la visée datée qui la
fonde en `:215-223`. Le code fautif était à l'ancienne ligne 275-276.

**Preuve** — `docs/PRD.md:838`, EX-A25 :

> et **τ, délai entre une correction et son effet mesurable**, mesuré par le
> simulateur et jamais saisi.

Le code écrivait :

```rust
// τ est **mesuré** : c'est l'écart entre l'instant de la correction
// et celui où elle contribue à la mesure.
self.delais_mesures.push(self.params.disponibilite_initiale_s);
```

`disponibilite_initiale_s` est le champ **saisi** T_a. `tau_mesure_s()` rendait
donc l'entrée sous l'étiquette d'une sortie. Le test ne pouvait pas le voir :
aux défauts, T_a = 30 s est un multiple de la période de 15 s, donc la valeur
mesurée et la valeur saisie coïncident.

**Changé** — la mesure est faite. `Controleur::visee_visible()` rend la visée
datée dont l'effet entre dans la métrique ; à chaque période où cette visée
change, `horloge_s − instant_de_pose` est enregistré. L'entrée initiale `(0, n₀)`
est exclue : ce n'est pas une correction. Champ `derniere_visible_s` ajouté pour
ne compter chaque correction qu'une fois.

**Mesure** — le test gagne le cas qui sépare les deux grandeurs :

| Réglage | T_a saisi | τ mesuré |
|---|---|---|
| défauts (P = 15 s) | 30 s | 30 s |
| P = 15 s, T_a = 20 s | 20 s | **30 s** |

La quantification par la période porte le délai réel à deux périodes. Une
implantation qui recopie T_a échoue désormais sur le second cas.

---

### A6 — `soupcon.rs` attribue au §4.3 une dérivation qui est au §7.3

**Où** — `soupcon.rs:184-202`.

**Preuve** — le §4.3 (**p. 70**) ne donne que le majorant :

> leurs valeurs par défaut, période 10 s, expiration 1 s, seuil d'échec 3,
> fixent à **30 s** le délai avant qu'un agent muet ne soit retiré

L'encadrement 21–31 s que la fonction implante est au §7.3, p. 112 :

> entre 0 et 10 s plus tard, puis exige deux échecs supplémentaires à 10 s
> d'intervalle, plus 1 s de délai d'expiration, d'où une détection comprise
> **entre 21 s et 31 s**.

**Changé** — citation corrigée en §7.3, p. 112, avec l'extrait qui la fonde et la
mention explicite que le §4.3 ne donne pas cet encadrement.

**Conséquence** — la seule fonction du morceau dont NF-15 exige qu'elle retrouve
un chiffre du traité renvoyait à la section qui ne le contient pas.

---

### A7 — Trois chemins de panique atteignables depuis l'API publique

`SPEC §7, clause 4` — « une configuration invalide est un refus rendu à
l'appelant, jamais un abandon » — et le dépôt applique déjà cette règle
(`adhesion::proprietaire`, `propagation::Rumeur::nouvelle`,
`pair_a_pair::Maille::nouvelle`, `soupcon::cout_nominal`).

| Où (état livré) | Déclencheur | Effet |
|---|---|---|
| `soupcon.rs:203` | `completude(_, _, 0)` | `seuil as u64 - 1` déborde : panique en debug, encadrement absurde en release |
| `cycle_de_vie.rs:174` | `retirer(_, ReglagesSonde { seuil_echec: 0, .. })` | idem ; les champs de `ReglagesSonde` sont publics |
| `echantillonnage.rs:261` | `TriDeVue::scission_silencieuse()` sur population vide | `tri[n / 2]` hors bornes |
| `echantillonnage.rs:211`, `:227` | `TriDeVue::attribut` était public : l'agrandir portait `attribut.len()` au-delà de `vues.len()` | `cycle` puis `vue` indexaient hors bornes |
| `accord.rs:413`, `:424`, `:470` | `MoyenneLocale::x` était public : l'agrandir désalignait `fige` et `sous_epsilon` | `figer`, `tour`, `arret_local` indexaient hors bornes |

**Changé** — `saturating_sub(1)` sur les deux seuils ; garde de population vide
dans `scission_silencieuse` ; `TriDeVue::cycle` et `MoyenneLocale::tour` étendent
leurs tables auxiliaires à la population courante ; `TriDeVue::vue` rend
`Option<&[u32]>` (précédent : `adhesion::proprietaire`) ; `MoyenneLocale::figer`
et `arret_local` sont bornés. **Trois** tests ajoutés — `soupcon.rs`,
`cycle_de_vie.rs`, `echantillonnage.rs` —, et non cinq : les chemins d'`accord.rs`
sont corrigés sans test (G-c).

**Deux moitiés de cette correction ne tiennent pas, et le tour 2 les reprend** :
elle couvre l'agrandissement d'un champ public et pas le rétrécissement (G-d), et
le `saturating_sub(1)` est une coercition, pas le refus qu'invoque la clause
(G-e). Voir Tour 2.

**Conséquence** — `release` ne pose pas `overflow-checks` dans ce dépôt : le
débordement des deux seuils n'aurait pas paniqué en release, il aurait rendu un
encadrement de l'ordre de 1,8 × 10¹⁹ tics sans qu'aucun oracle ne s'en aperçoive.

---

### A8 — `cascade.rs` : le test du critère (2) documente un effet que le modèle ne produit pas

**Où** — `cascade.rs:466-476` (documentation) et `:490-494` (assertion ajoutée).

**Preuve** — la documentation annonçait : « Il retarde la première mort déclarée
et allonge la détection vraie. » Or `Cascade::pas` calcule

```rust
let l99 = if utilisation < 1.0 { … } else { f64::INFINITY };
```

et le préréglage par défaut est saturé (`charge_par_s = 3 400` contre une
capacité de 16 × 1 000 / 5 = 3 200). `l99` vaut donc `INFINITY` **dès le premier
pas**, et `l99 > timeout_s` est vrai pour toute valeur finie de `timeout_s` : un
délai plus généreux ne retarde rien.

**Changé** — la documentation dit ce que le modèle produit, et l'assertion qui le
rend réfutable est ajoutée :

```rust
assert_eq!(
    (genereux.redemarrages, genereux.generations),
    (serre.redemarrages, serre.generations),
    "sous saturation la latence diverge : le réglage ne retarde rien du tout"
);
```

**Conséquence** — le critère est plus fort qu'avant : il n'établissait que
« la cascade survit à un timeout de 30 s », il établit maintenant qu'elle est
**identique**, ce qui est l'énoncé du traité — « le remède n'est pas un réglage
plus généreux » — et non un affaiblissement de celui-ci.

---

### A9 — Deux constantes de `accord.rs` sans nom ni provenance

**Où** — les deux constantes sont en `accord.rs:49` (`TAILLE_ECHANTILLON_QUORUM`)
et `:57` (`EPSILON_ARRET`) ; les littéraux qu'elles remplacent étaient aux
anciennes lignes 269 et 370.

**Preuve** — F2 : « une grandeur sans provenance est traitée comme une faute de
rédaction ». Le `8` était écrit deux fois — une fois comme taille d'échantillon
dans `SeuilDeQuorum::tour`, une fois comme `quorum.k + 8` dans le coût affiché par
`grille` — sans lien entre les deux : modifier l'un laissait l'autre mentir sur
le coût. Le `1e-3` est l'ε de la condition d'arrêt que `grille` affiche en toutes
lettres (« |Δx_i| ≤ ε pendant T tours ») sans jamais donner sa valeur ; le §5.1
pose la condition et ne chiffre ni ε ni T.

**Changé** — `TAILLE_ECHANTILLON_QUORUM` et `EPSILON_ARRET`, tous deux déclarés
**décisions d'implantation sans provenance dans le traité (F1)**, employés aux
deux sites chacun. La ligne de grille affiche désormais la valeur de ε et son
statut.

---

## Anomalies identifiées, non corrigées

### N1 — `elasticite.rs:15-30` : le constat de mesure du module porte contre le §7.3

Le module écrit que le contrôleur « ne converge pas » aux valeurs documentées et
que la différence entre le régime nominal et le préréglage « oscillation » est
« de degré, pas de nature ». Le §7.3, p. 114, conclut l'inverse sur le
comportement par défaut :

> Le comportement par défaut n'est donc pas une oscillation, c'est un dépassement
> en escalier suivi d'une descente filtrée — **et qui cherche une oscillation ne
> trouve rien à corriger**.

**Motif de non-correction** — c'est l'un des cinq écarts consignés au registre
`docs/decisions.md` et au §0 du PRD, et la 3ᵉ édition l'a manifestement absorbé
au §7.3. Trancher demande de rejouer le banc du contrôleur avec les deux
politiques de montée transposées (elles ne le sont pas, cf. A4), puis de mettre à
jour `docs/decisions.md` et le §0 du PRD — trois documents normatifs hors de mon
périmètre. Le texte du module reste tel quel ; A4 a corrigé la seule partie
factuellement fausse, la provenance.

### N2 — `cascade.rs:148-156` : `pannes_reelles` ne peut pas ne pas valoir zéro

Aucun chemin ne l'incrémente. Les assertions `pannes_reelles == 0` de
`critere_1a`, `critere_1b` et du bandeau EX-V16 ne peuvent donc pas échouer.

**Motif** — le fichier le déclare déjà, en toutes lettres et au bon endroit :
« Les assertions `pannes_reelles == 0` ne peuvent donc pas échouer — ce qu'elles
établissent est la lecture du code, pas une mesure. » Le rendre réfutable exige de
brancher `sim_core::ModeleFaute` sur le scénario J, ce qui est un livrable et non
une correction d'audit. Même situation pour `Controleur::pannes` en `elasticite.rs`.

### N3 — `deliberation.rs:97`, `:192` : `bloque_par_un_lent` ne bloque rien

Sous `Mode::AttendreTousLesEcrivains`, le drapeau est levé mais le tour se déroule
exactement comme en nominal — mêmes dépôts, mêmes lectures, même décision. La
documentation du champ dit « a fait attendre la population », ce que le modèle ne
produit pas.

**Motif** — `DepotAveugle` n'a pas d'axe temporel : il compte des tours de journal,
pas des instants. Représenter l'attente demande de porter le mécanisme sur le
moteur à événements, ce qui dépasse une correction. Le mécanisme n'a par ailleurs
aucun appelant (EX-A57, réserve ouverte du §0), donc l'écart n'affecte aucun
résultat.

### N4 — `elasticite.rs:365` : `arreter` ne gèle rien et prend `&mut self`

La méthode rend `self.population` sans rien modifier, et son `&mut self` annonce
une mutation qui n'existe pas. Ce que le test vérifie est qu'appeler `periode`
**après** `arreter` continue de bouger la population — ce qui contredit le mot
« gèle ».

**Motif** — corriger le nom ou la signature est un changement d'API publique dont
le sens dépend de ce qu'EX-A46 attend d'un « arrêt », et EX-A46 est un énoncé de
sûreté du PRD que je ne peux pas modifier pour l'accorder. Signalé, non touché.

### N5 — `stigmergie.rs:255-270` : `Params::depot()` écrête γ à 0,999 999 sans le dire

> **Levée au tour 2** — le motif de non-correction ci-dessous ne tient qu'à
> moitié : l'écrêtage ne borne que par le haut, et la moitié basse du domaine
> exclu produit `+∞` ou `NaN`. Voir Tour 2, G-f.

Hors du domaine (0, 1), la calibration retombe silencieusement sur γ = 0,999 999.
Aucun commentaire ne le signale, alors que γ = 1 est un préréglage exposé exprès
(EX-A11a) et que `Params::verrouillage()` contourne justement ce chemin en fixant
`depot_unitaire`.

**Motif** — l'écrêtage est inoffensif tant que `verrouillage()` reste le seul
chemin vers γ ≥ 1, ce qui est le cas aujourd'hui ; le corriger sans changer le
comportement ne serait qu'un commentaire, et le corriger en changeant le
comportement déplacerait la calibration du préréglage. À trancher avec le §0.

### N6 — `alignement.rs:81` : le voisinage tiré peut être plus petit que `degre`

`tirer_voisinage` saute les tirages qui retombent sur l'agent lui-même ou sur un
voisin déjà pris, sans retirer. La documentation annonce « chaque agent reçoit
`degre` voisins ». À `degre = 6` sur 64 agents l'écart est marginal ; à faible
population il ne l'est pas.

**Motif** — la boucle de rejet change la consommation d'aléa, donc la trajectoire
de tous les tests du fichier et des critères de sortie qui en dépendent. Un
changement de trajectoire est une décision de banc, pas une correction d'audit.

### N7 — Deux thèses de `Bloc` sont présentées en exergue sans être des citations

`adhesion.rs:4` (« Borner cette fenêtre reviendrait à faire terminer un accord en
asynchrone ») et `agregat_fenetre.rs:3` (« Une réponse fausse d'une quantité
inconnue, que rien dans le résultat ne trahit ») sont formatées `//! > … (§X.Y)`,
c'est-à-dire comme les citations verbatim des autres modules. Le banc de
provenance ne les trouve nulle part dans le traité : ce sont des reformulations du
produit.

**Motif** — la convention `Bloc::these` **est** une reformulation par
construction, et le champ `en_clair` voisin l'assume. Le défaut est dans le
balisage `> `, uniforme sur les onze modules, pas dans le contenu. Uniformiser
demande une décision sur la convention, qui vaut aussi pour les fichiers du
morceau voisin.

---

## Écarts hors périmètre, à porter à la passe de consolidation

### Documents normatifs

| Document | Énoncé | Mesure |
|---|---|---|
| `CLAUDE.md` | « troisième édition […] **116 pages** » | 143 pages |
| `CLAUDE.md` | « `docs/Traité.pdf` — source normative » | le fichier est à la racine ; `docs/` ne le contient pas |

Tant que `CLAUDE.md` annonce 116 pages, aucune page citée dans le dépôt ne peut
être vérifiée contre le fichier réel — c'est ce qui a laissé passer A1.

### Code hors de mon morceau, même défaut qu'A1

**Les lignes de ce seul tableau sont celles de l'état trouvé.** Ces fichiers sont
corrigés en parallèle par une autre passe : tout numéro que j'y écrirais serait
périmé avant d'être lu. Les ancres textuelles, elles, restent valides.

| Fichier:ligne | Annoncé | Mesuré |
|---|---|---|
| `sim-agents/src/glossaire.rs:150`, `:175`, `:184` | §1.2, p. 13 — algorithme 2 | **p. 14** (bloc « Algorithme 2 — renforcement ») |
| `sim-agents/src/glossaire.rs:159`, `:167`, `:292`, `:301`, `:309` | §1.2, p. 13 | **p. 14** (M1–M4) ou **p. 16** (plancher) selon la notice |
| `sim-agents/src/glossaire.rs:72`, `:80`, `:124` | §1.3, p. 21 — tableau 3 / figure 0 | **tableau 3 p. 18** ; **figure 0 p. 4** |
| `sim-agents/src/glossaire.rs:318` | conclusion p. 94 | **p. 129** |
| `sim-agents/src/scenario.rs:53` | §1.3, p. 21 — figure 0, tableau 3 | **figure 0 p. 4 ; tableau 3 p. 18** |
| `sim-agents/src/scenario.rs:206` | §1.2, p. 13 — algorithme 2 | **p. 14** |
| `sim-agents/src/scenario_d.rs:25`, `:390` | §2.1, p. 22 — figure 2.1c | **figure 2.1c p. 28** |
| `sim-agents/src/scenario_m.rs:7`, `:41` | §8.3, p. 94 | **p. 127** ; l'incise « du même geste » est bien p. 5 |
| `sim-milieu/src/journal.rs:628-631` | §1.2, p. 13 (M1–M4) | **p. 14** |
| `sim-viz/src/scenario_b.rs:549`, `:555` | §1.2, p. 13 | **p. 16** |

`scenario_d.rs:390` assère `BLOC_D.source.contains("p. 22")` : corriger la source
sans corriger le test le fait échouer.

---

## Commandes exécutées

Répertoire de sortie dérouté (`CARGO_TARGET_DIR`) : un autre agent compile la même
`target/` en parallèle, et l'édition de liens échouait sur des `.rlib` disparus en
cours de route.

```
cargo clippy -p sim-agents --all-targets --release
    Checking sim-agents v0.1.0 (…\crates\sim-agents)
    Finished `release` profile [optimized] target(s) in 1.72s
```

```
cargo test -p sim-agents --release
test result: ok. 247 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out   (lib)
test result: ok.   0 passed; …                                                 (bin campagne)
test result: ok.   4 passed; …                                                 (determinisme)
test result: ok.  11 passed; …                                                 (scenario_b)
test result: ok.   5 passed; …                                                 (sortie_phase_2)
test result: ok.   4 passed; …                                                 (sortie_phase_3)
test result: ok.   5 passed; …                                                 (sortie_phase_4)
test result: ok.   3 passed; …                                                 (sortie_phase_5)
test result: ok.  11 passed; …                                                 (sortie_phase_6)
test result: ok.   0 passed; …                                                 (doc-tests)
```

**290 tests, 0 échec.** Trois tests ajoutés (un par chemin de panique) et dix-huit
assertions ajoutées à des tests existants. Trois assertions ont disparu : celle
qui exigeait « provenance absente » (A4) et celle qui acceptait « 7,9 » (A3)
étaient fausses ou trop lâches, et chacune est remplacée par une ou plusieurs
assertions plus fortes ; la troisième (`alignement.rs`) est reprise mot pour mot
dans un bloc de trois. Aucun test retiré, aucune assertion relâchée.

```
cargo doc -p sim-agents --no-deps
 Documenting sim-agents v0.1.0 (…\crates\sim-agents)
    Finished `dev` profile [unoptimized + debuginfo] target(s) in 2.36s
   Generated …\doc\sim_agents\index.html and 1 other file
```

```
cargo check -p sim-viz --release
    Finished `release` profile [optimized] target(s) in 10.68s
```

`sim-viz` est le seul consommateur de `sim-agents` ; il est vérifié parce que
`TriDeVue::vue` change de signature.

---

# Tour 2 — reprise sur le jugement `M3-critique.md`

Contexte neuf. Chaque preuve du critique a été **rejouée avant correctif**, dans
un crate de reproduction hors arbre (`catch_unwind`, `CARGO_TARGET_DIR` dérouté),
puis rejouée après. Aucun fichier hors du morceau des mécanismes n'est touché ;
`docs/PRD.md` et `docs/decisions.md` ne le sont pas non plus.

## La reproduction, avant correctif

Sortie brute du banc, sur le dépôt tel que le tour 1 l'a laissé. Le crochet de
panique imprime le site.

```
   ↳ …\crates\sim-agents\src\accord.rs:272
[PANIQUE ] G1 SeuilDeQuorum::n agrandi : index out of bounds: the len is 16 but the index is 63
[PANIQUE ] G2 SeuilDeQuorum::qualites vidé : index out of bounds: the len is 0 but the index is 0
   ↳ …\crates\sim-agents\src\accord.rs:272
   ↳ …\crates\sim-agents\src\propagation.rs:113
[PANIQUE ] G3 Rumeur::n agrandi : index out of bounds: the len is 8 but the index is 25
[MESURE  ] G4 ecart_a_la_validite() population vide = NaN
   ↳ …\crates\sim-agents\src\echantillonnage.rs:228
[PANIQUE ] G5 TriDeVue::attribut rétréci → cycle : index out of bounds: the len is 4 but the index is 28
   ↳ …\crates\sim-agents\src\echantillonnage.rs:264
[PANIQUE ] G6 TriDeVue::attribut rétréci → scission : index out of bounds: the len is 4 but the index is 4
[PANIQUE ] G7 MoyenneLocale::x rétréci → tour : index out of bounds: the len is 2 but the index is 3
   ↳ …\crates\sim-agents\src\accord.rs:393
[MESURE  ] G-e completude(10, 1, 0) = (1, 11)
[MESURE  ] G-e retirer(seuil_echec = 0) → mise à mort en 11 s
[MESURE  ] G-f gamma =   0.9 -> depot() = 8.231290285767679e-5   avertissements = 0
[MESURE  ] G-f gamma =     1 -> depot() = 7.812503906477259e-10  avertissements = 1
[MESURE  ] G-f gamma =     0 -> depot() = inf                    avertissements = 0
[MESURE  ] G-f gamma =  -0.5 -> depot() = NaN                    avertissements = 0
[MESURE  ] G-f tri partial_cmp/unwrap_or(Equal) sur [3, NaN, 1, 2] = [3.0, NaN, 1.0, 2.0]
[MESURE  ] G-f tri partial_cmp/unwrap_or(Equal) sur [1, NaN, 3, 2] = [1.0, NaN, 2.0, 3.0]
```

Les treize points du jugement sont donc tous reproduits, sans exception ni
approximation. **Les deux dernières lignes sont la mesure la plus lourde du
lot** : la même multiplicité de valeurs, présentée dans deux ordres différents,
sort dans deux ordres différents — l'un totalement dé-trié. La comparaison
`partial_cmp(…).unwrap_or(Equal)` n'est pas transitive, donc le résultat du tri
dépend du parcours de l'algorithme, ce qui est la définition de ce que PD1
interdit.

### Ce que le banc a trouvé en plus, et qui change le diagnostic

Le même banc, exécuté **sans mutation d'aucun champ**, panique quatre fois :

```
[PANIQUE ] B1 MoyenneLocale plus petite que le service : len is 2 but the index is 39   ← accord.rs:393
[PANIQUE ] B2 TriDeVue plus petit que le service       : len is 2 but the index is 39   ← echantillonnage.rs:228
[PANIQUE ] B3 SeuilDeQuorum plus petit que le service  : len is 4 but the index is 38   ← accord.rs:272
[PANIQUE ] B4 Rumeur plus petite que le service        : len is 4 but the index is 39   ← propagation.rs:113
```

`MoyenneLocale::nouvelle(vec![1.0, 2.0])` avec un `ServiceDePairs::nouveau(64, …)`
suffit. Aucun champ public n'est touché : c'est de l'API nominale.

## Le remède, et pourquoi il n'y en a pas cinq

Le critique nomme le motif : « un champ public dimensionne des tables construites
une fois, et rien ne lie les deux ». Le banc B montre que la formulation exacte
est **plus large** : *deux objets portent la population, et rien ne les lie*. Le
champ public est une des deux façons de les séparer ; le service de pairs, qui a
sa propre population, en est l'autre, et elle ne demande aucune mutation. Un tour
qui ne traiterait que la première laisserait quatre paniques debout — c'est
exactement l'erreur de forme du tour 1, à un cran de généralité près.

D'où **deux remèdes, chacun unique de sa sorte**, et non cinq gardes :

**(1) La dimension cesse d'exister en double.** Là où un champ `n` doublait la
table qu'il dimensionnait, le champ est **supprimé** et remplacé par une méthode
qui lit la table ; là où le champ *était* la dimension, il devient privé avec un
accesseur en lecture. Il n'y a plus rien à désaligner — pas une garde à
l'exécution, une impossibilité à la compilation.

| Champ | Devient | Accesseur |
|---|---|---|
| `SeuilDeQuorum::n` | **supprimé** — `opinion` porte la population | `accord.rs:270` `pub fn n(&self) -> u32` |
| `SeuilDeQuorum::qualites` | privé (`accord.rs:183`) | `accord.rs:275` `pub fn qualites(&self) -> &[f64]` |
| `Rumeur::n` | **supprimé** — `etat` porte la population | `propagation.rs:80` `pub fn n(&self) -> u32` |
| `TriDeVue::attribut` | privé (`echantillonnage.rs:186`) | `echantillonnage.rs:203` `pub fn attribut(&self) -> &[f64]` |
| `MoyenneLocale::x` | privé (`accord.rs:382`) | `accord.rs:405` `pub fn x(&self) -> &[f64]` |

**(2) Un identifiant de pair est borné là où il entre**, et non là où il indexe.
Chaque mécanisme consomme `ServiceDePairs::tirer`, qui rend déjà un `Option` :
un identifiant hors de la population du mécanisme est traité comme un tirage sans
réponse, ce qui est sa lecture juste — un pair qu'on n'a pas n'est pas
observable. Quatre sites de tirage, pas douze sites d'indexation :

- `accord.rs:297` et `:320` — `SeuilDeQuorum::tour`, les deux tirages ;
- `accord.rs:435` — `MoyenneLocale::tour` ;
- `echantillonnage.rs:230` — `TriDeVue::cycle` ;
- `propagation.rs:170` — `Rumeur::tirer`, **le seul point d'entrée** du module,
  d'où une seule ligne pour la rumeur *et* l'anti-entropie.

Cette borne pose au passage l'invariant qui manquait : toute entrée de
`TriDeVue::vues` est désormais un agent de la population, ce qui rend
`scission_silencieuse` indexable sans garde — G6 disparaît sans qu'on ait à
l'attraper.

Les tables auxiliaires ne sont plus redimensionnées à chaque tour
(`MoyenneLocale::tour`, `TriDeVue::cycle`, `MoyenneLocale::figer`) : ces `resize`
étaient la moitié de correction que le critique désigne, et ils n'ont plus
d'objet.

**Vérification que la mutation n'est plus exprimable** — le banc de reproduction,
inchangé, ne compile plus :

```
error[E0615]: attempted to take value of method `n` on type `sim_agents::accord::SeuilDeQuorum`
error[E0616]: field `qualites` of struct `sim_agents::accord::SeuilDeQuorum` is private
error[E0615]: attempted to take value of method `n` on type `Rumeur`
error[E0616]: field `attribut` of struct `TriDeVue` is private   (×2)
error[E0616]: field `x` of struct `MoyenneLocale` is private
```

**Vérification que ce qui reste atteignable ne panique plus** — même banc, réduit
à ce qui compile :

```
[MESURE  ] G4 ecart_a_la_validite() population vide = None
[OK      ] B1 MoyenneLocale plus petite que le service
[OK      ] B2 TriDeVue plus petit que le service
[OK      ] B3 SeuilDeQuorum plus petit que le service
[OK      ] B4 Rumeur plus petite que le service
```

Cinq tests portent la preuve dans la suite du dépôt :
`accord.rs:764` (`un_service_plus_grand_que_la_population_ne_panique_pas`),
`accord.rs:787` (`une_population_vide_est_refusee_ou_declaree_sans_mesure`),
`accord.rs:805` (`figer_hors_population_na_aucun_effet`),
`echantillonnage.rs:408`
(`une_population_vide_ou_plus_petite_que_le_service_ne_panique_pas`) et
`propagation.rs:376` (même nom, côté rumeur).

---

## Les sept affirmations prises en défaut

### G-a — « dernière notice : 120 » : **corrigée dans ce rapport**

Le critique a raison, et c'est un retour de bâton : la section qui reprochait à
`CLAUDE.md` ses chiffres faux en portait un. Revérifié :

```
pages 143
page 143, notices trouvées : ['120', '121', '122', '123']
… « 123. Commission européenne. « Guidelines on the implementation of the
transparency obligations … » »
```

Le tableau *Mesure* porte désormais **123, sans trou**. `CLAUDE.md` disait vrai
sur ce point et n'est pas touché ; ce qu'il continue d'annoncer faussement — 116
pages, chemin `docs/Traité.pdf` — reste au tableau des écarts hors périmètre.

### G-b — « §4.3, p. 71-72 » : **corrigée**, dans le rapport et dans le code

Localisation refaite par le banc de provenance :

```
« période 10 s, expiration 1 s, seuil d'échec 3 »  -> [70]
« fixent à 30 s le délai »                          -> [70]
« entre 21 s et 31 s »                              -> [112]
« puis exige deux échecs supplémentaires »          -> [112]
```

La contre-preuve d'A6 est **p. 70**, et A6 le dit maintenant. Le code, lui, citait
le §4.3 **sans page** : `soupcon.rs:187` la porte désormais (« §4.3 (p. 70) »),
puisqu'un majorant de 30 s est une grandeur, et qu'une grandeur sans provenance
est une faute de rédaction (F2). La page portée pour l'encadrement — §7.3,
p. 112 — est confirmée juste.

### G-c — « cinq tests ajoutés » : **corrigée**, et le chemin sans test en a un

Trois, pas cinq, et le rapport se contredisait 200 lignes plus loin. A7 porte
désormais **trois**, et nomme le chemin corrigé sans test : celui d'`accord.rs`.
Ce chemin a maintenant les siens — `accord.rs:764`, `:787`, `:805` —, et c'est
bien celui dont la correction était incomplète (G-d, G7).

### G-d, G5, G6, G7 — **corrigées** par les remèdes (1) et (2) ci-dessus

Le critique note en outre que dans `MoyenneLocale::tour` « les `resize` traitent
les tables auxiliaires pendant que la cause reste — `anciens[j as usize]` où `j`
est borné par la population du **service**, jamais par `x.len()` ». C'est exact,
et c'est la cause que le banc B isole : elle est traitée à la racine par le
remède (2), pas au symptôme.

### G-e — arbitrage : **le code s'aligne sur la clause**

`docs/SPEC.md:668` pose la clause juste sous les *points d'entrée exécutables*,
ce qui autorise à lire qu'elle ne vise que ceux-là. **Je tranche dans l'autre
sens, sur trois appuis :**

1. **Le dépôt applique déjà la clause hors des points d'entrée**, et le tour 1
   l'a lui-même invoquée ainsi. `SeuilDeQuorum::nouveau` refuse `k = 0` par un
   `Result` en expliquant qu'à zéro « la règle est vraie par vacuité, ce qui n'est
   pas un accord unanime ». `seuil_echec = 0` est **le même énoncé** : zéro échec
   toléré n'est pas un seuil serré, c'est l'absence de politique de sonde.
   Traiter deux invalidités identiques de deux façons dans la même crate est
   l'incohérence, pas la clause.
2. **La coercition produit un nombre d'allure juste.** `completude(10, 1, 0)`
   rendait `(1 s, 11 s)` : un encadrement plausible, du bon ordre de grandeur, que
   **rien ne distingue d'une mesure**. C'est précisément le risque que la
   « Conséquence » d'A7 identifiait pour le débordement en release, en plus petit
   et en plus discret.
3. **Le coût est nul**, ce qui prive l'argument inverse de son seul appui
   pratique : quatre sites d'appel, tous dans le périmètre.

`completude` rend `Result<(Duree, Duree), String>` (`soupcon.rs:203`), `retirer`
rend `Result<Retrait, String>` (`cycle_de_vie.rs:174`). Les `saturating_sub(1)`
disparaissent au profit de `seuil - 1` sur un domaine désormais garanti.

```
[MESURE  ] G-e completude(10, 1, 0) = Err("seuil d'échec nul refusé : … à zéro
           échec il n'y a pas de détection à encadrer. Le délai rendu serait une
           valeur d'allure plausible sans mesure derrière.")
[MESURE  ] G-e completude(10, 1, 3) = Ok((21, 31))
[MESURE  ] G-e retirer(seuil_echec = 0) = Err("seuil d'échec nul refusé : … à
           zéro échec il n'y a pas de politique de sonde à simuler …")
```

Les deux tests correspondants vérifient **le refus et le voisin qui passe**, pour
que la garde ne mange pas le domaine utile :
`soupcon.rs:623` (`un_seuil_dechec_nul_est_refuse_au_lieu_detre_ecrete`) et
`cycle_de_vie.rs:355` (même nom). NF-15 tient : `completude(10, 1, 3)` retrouve
toujours 21–31 s.

### G-f — arbitrage : **l'ordre total d'abord**, le domaine ensuite

Le critique a raison sur les deux moitiés : `min(0.999_999)` ne borne que par le
haut, `avertissements()` ne signalait que γ ≥ 1, et le `NaN` qui en sort détruit
l'ordre déterministe. **Je tranche pour l'ordre total comme remède principal**,
et non pour la seule garde de domaine, parce que c'est celui qui protège **toute**
source de `NaN` et pas seulement γ :

- PD1 est une contrainte non négociable ; γ n'est qu'un des chemins par lesquels
  un `NaN` peut atteindre un tri. Fermer le chemin laisse le tri fragile ; rendre
  le tri total le met hors d'atteinte quel que soit le chemin.
- `f64::total_cmp` est du stdlib, exactement spécifié sur les bits, donc
  **identique entre cibles** — NF-02 tient, et il n'est pas des sept méthodes
  interdites.
- La garde de domaine, elle, ne peut pas être un refus : γ = 1 est un préréglage
  exposé exprès (EX-A11a, `Params::verrouillage`). Elle ne peut donc être qu'un
  écrêtage déclaré — ce qui la rend insuffisante à elle seule, et confirme l'ordre
  des deux.

Les cinq comparaisons `partial_cmp(…).unwrap_or(Equal)` du périmètre passent à
`total_cmp` : `echantillonnage.rs:246` et `:273`, `stigmergie.rs:980` et `:1144`,
`usl.rs:200`.

En second, le domaine cesse d'être silencieux à son bord bas. `Params::GAMMA_MIN`
(`stigmergie.rs:225`) et `Params::GAMMA_MAX` (`:233`) nomment l'écrêtage et le
déclarent F1 ; `depot()` (`:255`) écrête **aux deux bords**, `NaN` traité à part
parce que `f64::clamp` le propage ; `actualiser_phi` (`:854`) et
`compter_incomparabilite` (`:994`) écrêtent le bord bas, là où le `NaN` naissait
avant de descendre dans φ puis dans les poids ; `avertissements()` (`:204`)
signale γ ≤ 0 et `NaN` ; `bornes_applicables()` (`:362`) efface la borne sur le
domaine complet, la forme négative `!(0 < γ < 1)` attrapant `NaN` par
construction.

Après :

```
[MESURE  ] G-f gamma =   0.9 -> depot() = 8.231290285767679e-5   avert. = 0   borne = applicable
[MESURE  ] G-f gamma =     1 -> depot() = 7.812503906477259e-10  avert. = 1   borne = effacée
[MESURE  ] G-f gamma =     0 -> depot() = 1.079336762340959e-2   avert. = 1   borne = effacée
[MESURE  ] G-f gamma =  -0.5 -> depot() = 1.079336762340959e-2   avert. = 1   borne = effacée
[MESURE  ] G-f gamma =   NaN -> depot() = 1.079336762340959e-2   avert. = 1   borne = effacée
[MESURE  ] [3.0, NaN, 1.0, 2.0] → partial_cmp [3.0, NaN, 1.0, 2.0] | total_cmp [1.0, 2.0, 3.0, NaN]
[MESURE  ] [1.0, NaN, 3.0, 2.0] → partial_cmp [1.0, NaN, 2.0, 3.0] | total_cmp [1.0, 2.0, 3.0, NaN]
```

Les deux valeurs **dans le domaine** sont inchangées au dernier bit — γ = 0,9 rend
`8.231290285767679e-5` avant comme après, γ = 1 rend `7.812503906477259e-10` : la
garde ne déplace aucune trajectoire existante. Deux tests l'établissent :
`stigmergie.rs:1207` (`les_deux_bords_du_domaine_de_gamma_sont_ecretes_et_signales`,
qui vérifie aussi que `Params::scenario_b()` n'émet **aucun** avertissement) et
`stigmergie.rs:1228` (`lordre_des_poids_ne_depend_pas_de_la_position_dun_nan`,
qui rejoue exactement la mesure ci-dessus). Trois lignes s'ajoutent au portail de
`bornes_applicables` : γ = 0, γ < 0, γ = NaN.

**N5 est donc levée**, et son motif de non-correction du tour 1 est faux dans sa
seconde moitié : corriger ne demandait pas de déplacer la calibration du
préréglage — le bord haut ne bouge pas d'un bit.

### G-g — 10 846 lignes, non 10 611 : **corrigée**

Le chiffre porté était antérieur aux corrections du tour 1. L'en-tête du rapport
donne maintenant le compte de l'état **livré**, 11 167 lignes, avec la date de
mesure et la valeur intermédiaire.

---

## Les sept anomalies que le tour 1 n'avait pas vues

| Réf. | État | Où, dans le code livré |
|---|---|---|
| G1 — `SeuilDeQuorum::n` public | **corrigée** — champ supprimé | `accord.rs:178`, `:270` |
| G2 — `SeuilDeQuorum::qualites` public | **corrigée** — champ privé | `accord.rs:183`, `:275` |
| G3 — `Rumeur::n` public | **corrigée** — champ supprimé | `propagation.rs:36`, `:80` |
| G4 — `ecart_a_la_validite()` rend `NaN` | **corrigée** — rend `Option<f64>` | `accord.rs:458` |
| G5 — `echantillonnage.rs:228` | **corrigée** — remèdes (1) et (2) | `echantillonnage.rs:230` |
| G6 — `echantillonnage.rs:264` | **corrigée** — l'invariant de vue la rend inatteignable | `echantillonnage.rs:261-273` |
| G7 — `accord.rs:393` | **corrigée** — remèdes (1) et (2) | `accord.rs:435` |

**G4, en détail.** C'est l'oracle armé d'EX-A51, et « rendre une valeur au lieu
d'un refus » y est plus grave qu'ailleurs : `NaN` comparé à un seuil est faux dans
les deux sens, donc un oracle qui rend `NaN` **se lit comme un oracle satisfait**
— l'argument que le tour 1 avait déjà écrit pour `bornes_applicables` et qu'il
n'avait pas appliqué ici. La signature passe à `Option<f64>`, et `grille`
(`accord.rs:599-607`) porte la conséquence : sans population, la case « validité »
reste `Case::NonLivree` — non mesurée —, jamais `Case::Tenue`. C'est PD6 : une
absence se déclare au même rang qu'une présence, elle ne se maquille pas en
« tenue ».

Deux sources de `0/0` existaient dans le même fichier. La seconde,
`SeuilDeQuorum::fraction_engagee`, est traitée à la racine plutôt que par un
second `Option` : le constructeur rend déjà un `Result` et refuse déjà deux
réglages, il refuse maintenant `n = 0` (`accord.rs:249`). `MoyenneLocale::nouvelle`
n'a pas de constructeur faillible et ne peut pas en gagner un sans casser
`tests/sortie_phase_3.rs`, hors périmètre : d'où l'`Option` pour elle et le refus
pour l'autre.

---

## Ce qui n'est **pas** corrigé, et pourquoi

Rien du jugement. Les treize entrées sont traitées. Restent, inchangées, les sept
réserves N1 à N7 du tour 1 **moins N5**, qui est levée ci-dessus ; leurs motifs de
non-correction sont ceux déjà écrits, et le critique ne les conteste pas.

Deux remarques de portée, pour le juge suivant :

- **`Rumeur::etat(i)` panique hors population** (`propagation.rs:85`). C'est la
  même classe que `TriDeVue::vue`, que le tour 1 a passé en `Option`. Non touché :
  ce n'est aucune des treize entrées, la méthode n'a aucun appelant dans le dépôt,
  et le mandat de ce tour est explicite sur la portée. Signalé plutôt que corrigé
  en silence.
- **Le tableau « Code hors de mon morceau »** garde les lignes de l'état trouvé,
  et le dit sur place : ces fichiers sont repris en parallèle par une autre passe.

---

## Commandes exécutées, tour 2

Même déroutement de `CARGO_TARGET_DIR` qu'au tour 1, pour la même raison.

```
cargo clippy -p sim-agents --all-targets --release
    Checking sim-agents v0.1.0 (…\crates\sim-agents)
    Finished `release` profile [optimized] target(s) in 1.34s
```

Aucun avertissement. Un `manual_clamp` était apparu sur une première rédaction de
l'écrêtage de γ en `max().min()` ; il est levé en traitant `NaN` par une branche
explicite plutôt qu'en le contournant par un `allow`.

```
cargo test -p sim-agents --release
test result: ok. 253 passed; 0 failed; …   (lib)
test result: ok.   0 passed; …             (bin campagne)
test result: ok.   4 passed; …             (determinisme)
test result: ok.  11 passed; …             (scenario_b)
test result: ok.   5 passed; …             (sortie_phase_2)
test result: ok.   4 passed; …             (sortie_phase_3)
test result: ok.   5 passed; …             (sortie_phase_4)
test result: ok.   3 passed; …             (sortie_phase_5)
test result: ok.  11 passed; …             (sortie_phase_6)
test result: ok.   0 passed; …             (doc-tests)
```

**296 tests, 0 échec** — 290 à la mesure du critique. **Cinq** sont ajoutés ici
(`accord.rs` ×3, `stigmergie.rs` ×2) ; le sixième vient d'un module hors de mon
périmètre, modifié en parallèle par une autre passe — je le compte sans me
l'attribuer. Aucun test retiré, aucune assertion relâchée. Deux tests changent de nom parce que le cas qu'ils
couvraient n'existe plus et qu'un cas plus large le remplace :
`une_population_vide_ou_agrandie_ne_panique_pas` →
`une_population_vide_ou_plus_petite_que_le_service_ne_panique_pas`
(`echantillonnage.rs:408`), et son homologue de `propagation.rs:376`. Dans les
deux cas, l'agrandissement testé n'est plus **exprimable** — le compilateur le
refuse, ce qui est strictement plus fort qu'une assertion —, et le nouveau cas
couvre une panique que l'ancien ne voyait pas. Deux autres changent de nom pour la
même raison côté G-e (`…_ne_deborde_pas` → `…_est_refuse_au_lieu_detre_ecrete`),
et chacun vérifie une chose de plus qu'avant : le motif du refus, et le réglage
voisin qui doit continuer de passer.

```
cargo doc -p sim-agents --no-deps
 Documenting sim-agents v0.1.0 (…\crates\sim-agents)
    Finished `dev` profile [unoptimized + debuginfo] target(s) in 1.79s
   Generated …\doc\sim_agents\index.html and 1 other file
```

```
cargo check -p sim-viz --release
    Checking sim-viz v0.1.0 (…\crates\sim-viz)
    Finished `release` profile [optimized] target(s) in 1.01s
```

`sim-viz` est vérifié parce que cinq champs publics disparaissent de l'API. Il
n'en consommait aucun : les seuls usages hors module sont dans
`tests/sortie_phase_3.rs`, qui ne lit ni n'écrit aucun des cinq et compile sans
retouche — vérifié, pas supposé, ce fichier étant hors de mon périmètre.

## Contraintes structurelles

Aucune des sept méthodes de `f64` interdites n'est introduite. `f64::total_cmp`,
`f64::clamp`, `f64::max`, `f64::min` et `f64::is_nan` n'en font pas partie et
n'évaluent aucune transcendante : `total_cmp` est une comparaison sur les bits,
exactement spécifiée, donc identique entre cibles (NF-02). Aucun `HashMap` ni
`HashSet` (PD1). `clippy` est muet sur le paquet complet, cibles de test
comprises.
