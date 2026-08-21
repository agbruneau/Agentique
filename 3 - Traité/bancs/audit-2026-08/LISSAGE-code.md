# Lissage du code — ce que le découpage en cinq morceaux a laissé aux coutures

Passe de lissage sur le dépôt tel que les dix agents de `bancs/audit-2026-08/`
l'ont laissé : 465 tests, clippy 0, rustdoc 0. Aucun arbitrage déjà tranché n'est
rouvert, aucun test n'est retiré ni affaibli, aucun périmètre n'est réduit.
`docs/`, `CLAUDE.md`, `README.md` et `clippy.toml` ne sont pas touchés — ce qui
s'y règle est consigné au § « Ce que le lissage laisse ouvert ».

État livré : **466 tests**, clippy 0, rustdoc 0. Un test ajouté, aucun retiré ;
deux tests changent de nom ou de portée en gagnant des cas, jamais en en perdant.

Les `fichier:ligne` de ce rapport désignent **le code livré**.

---

## Le motif commun

Les cinq morceaux ne se voyaient pas travailler, et les coutures ont produit
trois formes de défaut, toujours la même mécanique :

1. **Une règle établie dans un morceau, appliquée à ce seul morceau.** M2 a
   interdit le balisage Markdown dans sa liste d'absences et l'a tenu par un
   test ; `sim-core` et `sim-agents` n'ont rien reçu, et M1 a *ajouté* des
   astérisques dans la sienne pendant ce temps. M5 a qualifié les renvois `§X.Y`
   ambigus de `sim-viz` ; les chaînes que `sim-viz` affiche et qui viennent des
   trois autres crates sont restées nues. M4 a exigé que la page d'un bloc PD8
   nomme son édition et l'a écrit pour cinq blocs sur dix — les cinq autres
   vivent dans les modules de M3.
2. **Un obstacle levé par un morceau pendant qu'un autre s'y arrêtait.** M2 a
   refusé de renuméroter ses pages du traité parce que « `CLAUDE.md` fixe la
   pagination normative à 116 pages » et qu'arbitrer quel rendu fait foi
   n'était pas de son ressort. M5 a corrigé `CLAUDE.md` à 143 pages dans la même
   campagne. Le motif de non-correction de M2 avait cessé d'exister au moment où
   il l'écrivait.
3. **Un constat vu par un morceau, corrigible seulement depuis un autre.** M4 a
   relevé que `cycle_de_vie` est un module sans appelant absent de
   `hors_perimetre()`, et s'est arrêté au motif que le module est hors de son
   périmètre — alors que c'est la **liste** qui est fautive, pas le module. M3 a
   relevé un chemin de panique non documenté et l'a signalé plutôt que de le
   corriger, son mandat portant sur les treize entrées du juge.

---

## Ce que j'ai changé

### 1 — `crates/sim-core/src/faute.rs:497` — `hors_modele()` portait du balisage Markdown (PD6)

**Le défaut.** Quatre paires d'astérisques d'emphase dans la première entrée :
`**ce modèle-ci**`, `**aucun appelant**`, `**règle**`, `**neuf**`. Trois d'entre
elles ont été **écrites par le correctif A2 de M1**.

`crates/sim-viz/src/lib.rs:906` passe cette liste à `section()` → `puce()`, qui
pose un `egui::RichText` sans analyseur Markdown. Les astérisques s'affichent
donc littéralement, dans l'onglet « Limites », à côté de deux listes qui n'en
portent pas. C'est exactement le défaut D3 que le critique de M2 a relevé côté
`sim-milieu` et que M2 a fermé par un test (`sim-milieu/src/lib.rs:108`) — la
règle existait, écrite, testée, dans la crate d'à côté.

**Changé.** Les astérisques retirées ; le sens ne bouge pas (« Le scénario B,
lui, **règle** » devient « règle bien »). Le rustdoc de `hors_modele()` porte
désormais la règle et dit qu'elle vaut pour les trois listes.

### 2 — `crates/sim-viz/src/lib.rs:1052` — la garde ne couvrait qu'une des trois listes

**Le défaut.** L'onglet « Limites » réunit trois listes écrites dans trois
crates. Une seule était tenue par un test. Le défaut 1 est revenu par la seule
qui ne l'était pas.

**Changé.** Un test, `aucune_liste_dabsences_ne_porte_de_balisage_markdown`, sur
les trois. Il vit dans `sim-viz` et non à trois exemplaires dans les trois
crates, parce que la contrainte appartient au **rendu** : c'est `egui` qui n'a
pas d'analyseur, et trois copies de la même assertion seraient précisément le
doublon que cette passe cherche. `sim-milieu` garde la sienne, locale et
antérieure ; elle n'est pas retirée (retirer un test est une décision
d'inventaire, et elle tourne sans la chaîne de compilation de `sim-viz`).

**Contre-épreuve.** Astérisques remises dans `faute.rs`, `cargo test -p sim-viz
--release --lib` :

```
test tests::aucune_liste_dabsences_ne_porte_de_balisage_markdown ... FAILED
thread ... panicked at crates\sim-viz\src\lib.rs:1060:17:
sim-core — astérisque d'emphase : **ce modèle-ci**, dans les scénarios livrés : …
test result: FAILED. 5 passed; 1 failed; 0 ignored; 0 measured; 0 filtered out
```

Restaurées : les six passent.

### 3 — Deux renvois `§X.Y` ambigus, affichés sur l'écran même où M5 en a qualifié un troisième

**Le défaut.** M5 (E4, E5) a appliqué la règle de `CLAUDE.md` — « un renvoi qui
peut se lire des deux côtés se qualifie » — à `sim-viz`, y compris au rustdoc de
`limites()`, qui écrit désormais « §8.3 **du PRD** — ce que le produit ne mesure
pas ». Deux chaînes affichées par la **même** fonction, venues des deux autres
crates, portaient un `§` nu :

| Où | Renvoi | Ce qu'il désigne |
|---|---|---|
| `crates/sim-core/src/faute.rs:527` | « adversité endogène (§8.3) » | le **traité** — « Buts incompatibles », p. 124 |
| `crates/sim-agents/src/lib.rs:98` | « oracles du §5.1 au registre » | le **traité** — « Mécanismes de consensus », p. 73 |

Un lecteur de l'onglet lisait donc « §8.3 du PRD » en tête de page et « §8.3 »
nu, désignant l'autre document, quatre puces plus bas.

**Changé.** « §8.3 du traité — celui du PRD porte sur ce que le produit ne mesure
pas » et « oracles du §5.1 du traité ». Les sections sont celles de la table des
matières mesurée du PDF livré (`get_toc()` : §5.1 p. 73, §8.3 p. 124).

### 4 — `crates/sim-agents/src/lib.rs:110` — `hors_perimetre()` déclarait six mécanismes sans appelant, il y en a sept

**Le défaut.** Vérification de la liste **dans l'autre sens** — ce qui est absent
y figure-t-il ? `cycle_de_vie` (EX-A26 sondes, EX-A48 ordre de chute, EX-A27
budget de perturbation) n'a **aucune** référence hors de son propre fichier
sauf `gouvernance.rs:332`, qui est un `mod tests` :

```
$ grep -rn "crate::cycle_de_vie\|sim_agents::cycle_de_vie" crates/ --include=*.rs
crates/sim-agents/src/gouvernance.rs:332:    use crate::cycle_de_vie::{BudgetPerturbation, Perturbation};
```

C'est exactement le statut des six déjà déclarés — adhésion, alignement,
causalité, consensus linéaire, directive, reconfiguration —, vérifiés un à un
par le même balayage. Le critique de M4 l'avait vu (« Le seul manque est
`cycle_de_vie` ») et M4 s'était arrêté au motif que « le fichier du mécanisme est
hors périmètre » : c'est la liste qui est en cause, et elle était dans son
périmètre.

**Changé.** L'entrée passe à **sept** et nomme le mécanisme avec ses trois codes
d'exigence et sa seule référence.

**Conséquence.** `CLAUDE.md` et le §0 du PRD comptent six ; ils divergent
maintenant du code d'une unité. Consigné plus bas — la correction leur appartient.

### 5 — Cinq blocs PD8 sur dix ne nommaient pas leur édition (F2)

**Le défaut.** M4 a établi qu'« une page citée sans son édition est une
provenance fausse, pas imprécise », a porté `(3ᵉ éd.)` sur les blocs A, B, D, K,
M et l'a tenu par un test. Les cinq autres — E, F, G, J, L — vivent dans les
modules de mécanismes, morceau de M3. La documentation du test le dit
elle-même : « les y ajouter demanderait de toucher à cinq modules de mécanismes,
pas d'écrire une ligne ici ». Les pages, elles, sont justes : M3 les avait
remesurées et le critique de M4 les a revérifiées indépendamment.

**Changé.** Les cinq `source` portent `(3ᵉ éd.)` :

| Bloc | Fichier:ligne | Source livrée |
|---|---|---|
| E | `adhesion.rs:24` | §1.3, algorithme 3 du ch. 1, p. 21-22 (3ᵉ éd.) |
| F | `allocation.rs:22` | §5.2, figure 5.2 p. 80, tableau 15 p. 81 (3ᵉ éd.) |
| G | `agregat_fenetre.rs:27` | §7.1, p. 104 (3ᵉ éd.) |
| J | `cascade.rs:25` | §6.1, p. 90 (3ᵉ éd.) |
| L | `taux_de_base.rs:20` | §7.2, figure 7.2 p. 107, tableau 19 p. 110 (3ᵉ éd.) |

**Et la clause porte maintenant sur les dix.** `scenario.rs:583` extrait
`tous_les_blocs()`, la liste des dix qui n'existait qu'en littéral local dans un
test ; `les_dix_blocs_portent_leur_section_et_leur_page` (`:602`) et
`les_blocs_verifies_nomment_leur_edition`, renommé
`les_dix_blocs_nomment_leur_edition` (`:652`), la partagent. Le test **gagne**
cinq blocs et n'en perd aucun ; sa documentation dit pourquoi les cinq nouveaux
restent hors de `blocs_verifies()` (deux de leurs thèses sont des reformulations
du produit, pas des citations, donc la vérification mot pour mot du test suivant
ne s'y applique pas — c'est le constat N7 de M3).

**Contre-épreuve.** `(3ᵉ éd.)` retirée de `BLOC_E` :

```
test scenario::tests::les_dix_blocs_nomment_leur_edition ... FAILED
thread ... panicked at crates\sim-agents\src\scenario.rs:654:13:
bloc E : page citée sans son édition — §1.3, algorithme 3 du ch. 1, p. 21-22
test result: FAILED. 252 passed; 1 failed
```

### 6 — `Bornes::LEGENDE` et `SOURCE_BORNES` ne nommaient pas la leur, à côté d'un bloc qui la nomme

**Le défaut.** Le panneau « Ce que le traité démontre » du scénario B affiche la
provenance des deux bornes (`SOURCE_BORNES`, recopiée de `Bornes::LEGENDE`) et,
plus bas dans le même écran, `BLOC_B.source`. Les deux citent **la même page** —
§1.2, p. 16 — et une seule nommait son édition. C'est la forme atténuée du défaut
que M5 avait corrigé sur ce panneau (deux pages pour une source dans un seul
cadre) : deux régimes de provenance pour une seule.

**Changé.** `crates/sim-agents/src/stigmergie.rs:431` et
`crates/sim-viz/src/scenario_b.rs:74` portent « §1.2, p. 16, 3ᵉ éd. ». Le test
`la_provenance_des_bornes_suit_encore_sim_agents` tient les deux accordés — il
échoue si l'une change sans l'autre — et le rustdoc de `LEGENDE` dit désormais
pourquoi la mention y est.

### 7 — Les pages du traité que M2 avait parquées sur un obstacle levé depuis

**Le défaut.** M2 (§B1) a mesuré cinq provenances fausses dans `sim-milieu` et
a refusé de les corriger, au motif que la référence normative annonçait 116 pages
alors que le PDF en fait 143, et qu'arbitrer lequel fait foi n'était pas de son
ressort. M5 (§6-7) a corrigé `CLAUDE.md` à **143 pages, mesurées**. L'arbitrage
est donc rendu, et M2 l'appelait de ses vœux : « soit `Traité.pdf` (143 pages)
fait foi et les cinq citations de cette crate — plus leurs homologues dans les
trois autres — se renumérotent en une passe ».

**Mesure.** Refaite ici, `pymupdf` sur `Traité.pdf` du dépôt (143 pages, folio
imprimé = index physique), recherche verbatim page par page après normalisation
des apostrophes et des blancs :

| Fichier:ligne | Ancre cherchée | Annoncé | Mesuré |
|---|---|---|---|
| `sim-milieu/src/journal.rs:700-703` | les quatre énoncés M1 à M4 | §1.2, p. 13 | **p. 14** (les quatre) |
| `sim-milieu/src/journal.rs:82` | « la traçabilité distribuée répond » | §6.2, p. 71 | **p. 96** |
| `sim-milieu/src/replication.rs:7` | « Le nombre de disparitions auquel » | §2.1, p. 22 | **p. 26** |
| `sim-milieu/src/replication.rs:181` | « tout enregistrement accusé au producteur » | §2.1, p. 21 | **p. 26** |
| `sim-milieu/src/controle.rs:4` | « Le plan de données évite l'accord » | §4.2, p. 49 | **p. 65** |
| `sim-core/src/faute.rs:4` | « sont exactement les fautes que la campagne » | §3.3, p. 41 | **p. 50** |

Les six sites renumérotés **portent leur édition**, sans quoi le prochain lecteur
ne saurait pas si le nombre est d'avant ou d'après la migration — `CLAUDE.md`
pose que « un renvoi qui porte son édition est le seul qui se relise sans le
refaire ».

Le cas de `journal.rs:82` est le seul qui demandait une précaution : la table des
matières donne §6.2 = p. 91-95 et §6.3 à p. 96, mais la page 96 porte **la fin du
§6.2** — la phrase qui fonde le renvoi y est, le titre du §6.3 vient plus bas sur
la même page. La provenance livrée le dit.

**Deux mesures d'autres rapports sont corrigées au passage**, sans effet sur le
code : `usl.rs:3` cite « conclusion, p. 130 » et M4 le rangeait parmi les renvois
hors section (« conclusion = p. 128-129 ») ; la phrase « L'ouvrage n'a pas dit
comment » est bien **p. 130**, page qui porte la fin de la conclusion et le début
des Références. Le renvoi était juste. De même `allocation.rs:117` (§5.2, p. 78)
et `consensus_lineaire.rs:91` (§3.1, p. 42), revérifiés justes.

**Effet mesurable.** La ligne de diagnostic de `CLAUDE.md` rend maintenant, pour
le §1.2 : `p. 16` dix fois, `p. 14` six fois, `p. 12` une fois — trois ancres
distinctes et toutes exactes (l'énoncé des bornes, l'algorithme 2 et les quatre
invariants, l'ouverture de la section). Les cinq `p. 13` vivants ont disparu ; la
seule occurrence restante est dans le tableau de mesure d'un rustdoc de test, qui
enregistre l'**état trouvé** et doit le garder.

### 8 — `crates/sim-agents/src/propagation.rs:88` — le chemin de panique que M3 a signalé sans le documenter

**Le défaut.** `Rumeur::etat(i)` indexe sans borner. M3 l'a relevé au tour 2 et
l'a laissé — à juste titre : le rendre faillible est un changement de signature,
et son mandat était fermé. Mais M1 et M2 ont passé leur campagne à ajouter des
sections `# Panics` (deux dans `sim-core`, huit dans `sim-milieu`), au motif
qu'un abandon non documenté est une faute de rédaction. `sim-agents` sort de la
campagne avec un chemin de panique connu, nommé dans un rapport, muet dans le
code. Le `///` de la méthode était en outre une paraphrase de son nom, ce que les
conventions du dépôt traitent comme une doc vide.

**Changé.** Une section `# Panics` qui dit la condition, pourquoi elle est
atteignable ici et nulle part ailleurs dans le module (les identifiants venus du
service de pairs sont écartés à l'entrée, remède (2) de M3), et ce que coûterait
le correctif par le type. Le `///` dit désormais ce que le nom ne dit pas : `i`
est un indice de population, pas un identifiant de pair. **Aucun comportement
n'est modifié**, et l'anomalie de fond reste ouverte, ci-dessous.

---

## Vérifications faites, sans défaut à signaler

Ce qui a été repris et tenait compte autant que ce qui ne tenait pas.

- **`sim_milieu::hors_perimetre()`, les treize entrées, dans les deux sens.**
  Toutes exactes. Rien de ce que M2, M3 ou M4 ont corrigé ne branche ni ne
  débranche un mécanisme : `Groupe` n'est instancié nulle part hors crate,
  `Historique` et `Quotas` ne le sont que par `tests/sortie_phase_6.rs`, le
  module `format` et `Milieu::partition_de` n'ont toujours aucun appelant.
- **`ModeleFaute::hors_modele()`, les neuf mécanismes sans appelant.** Balayage
  refait, `bancs/` compris : `tirer_pannes`, `Moteur::avancer_partition`,
  `message_perdu`, `injection_echec`, `injection_retard`, `injection_valeur`,
  `retard_message`, `ecriture_corrompue` et `avertissements` n'ont d'appelant que
  leurs propres tests, quand ils en ont un — `ecriture_corrompue` et
  `avancer_partition` n'en ont aucun. `gigue` est bien appelé
  (`moteur.rs:250`). `Moteur::installer_fautes` reste sans appelant.
- **Les quatre signatures qui ont changé de part et d'autre d'une frontière.**
  `completude` et `retirer` rendent `Result` : les cinq appelants sont des tests
  qui le déplient par `expect`, aucun `let _ =`. `ecart_a_la_validite` et
  `TriDeVue::vue` rendent `Option` : aucun `unwrap_or` n'en fabrique une valeur —
  `grille` (`accord.rs:605`) traduit le `None` en `Case::NonLivree`, ce qui est
  la lecture PD6. `Compte::fiabilite` rend `Result` : `sortie_phase_6.rs:249-252`
  distingue bien le refus de régime de l'absence d'issue. `Groupe::nouveau` prend
  sa date de création et n'a aucun appelant hors crate. Les champs supprimés
  (`SeuilDeQuorum::n`, `Rumeur::n`, `Groupe::p`, le paramètre `octets` de
  `Partition::ajouter`) ne sont décrits nulle part sous leur ancienne forme : les
  docs qui les nomment renvoient aux accesseurs, et `cargo doc` le vérifie.
- **Aucune doc d'appelant ne décrit une forme périmée.** Les dix-huit renvois
  `crate::hors_perimetre()` / `hors_modele()` répartis dans les quatre crates
  disent tous ce que la liste dit effectivement.
- **`sim-core` n'a toujours pas de `hors_perimetre()`**, et n'en reçoit pas : la
  décision est consignée pour la consolidation documentaire, pas prise ici.
- **Les registres de langue des accesseurs neufs.** `SeuilDeQuorum::n`,
  `Rumeur::n`, `qualites`, `x`, `attribut`, `Groupe::p` : chacun dit l'invariant
  — la dimension est dérivée de la table, jamais rangée en double — et non la
  paraphrase de son nom.

---

## Ce que le lissage laisse ouvert

Au même rang que le reste, avec le motif de chacun.

### A — Les accents graves des trois listes d'absences (≈ 40 entrées)

M5 (§4) a jugé que `` `sim-agents::partage` `` s'affichait littéralement dans
l'onglet « Limites » et l'a remplacé par des guillemets dans **sa** liste, au
motif que « les accents graves ne sont pas plus analysés que les astérisques ».
Les trois listes importées en portent des dizaines, sur le même écran, par le
même `RichText`. La règle codifiée par le test de M2 — reprise telle quelle par
le test ajouté ici — ne couvre que les astérisques et les retours à la ligne.

**Motif.** Trancher demande de choisir entre deux régimes typographiques pour une
quarantaine d'entrées de trois crates, et de réécrire chacune. C'est une décision
de convention d'affichage, pas un lissage ; la faire à moitié — quelques entrées
converties — laisserait l'écran plus incohérent qu'il ne l'est. Le rustdoc du
test ajouté dit explicitement que la règle s'arrête là et pourquoi.

### B — Les renvois `§X.Y` nus des commentaires publiés des trois autres crates

M5 a appliqué la règle de `CLAUDE.md` à tout `sim-viz`, commentaires compris, en
notant que `cargo doc --workspace --no-deps` les publie. Le même balayage sur les
trois autres crates rend une soixantaine de `§5.1` et `§8.3` nus — dont
`sim-agents/src/lib.rs:6` (« Aucun d'eux ne dessine quoi que ce soit (§5.1) »,
qui vise le **PRD**) et `sim-agents/src/accord.rs:7` (« Chaque mécanisme du
§5.1 », qui vise le **traité**), à quatre-vingt-douze lignes l'un de l'autre.

**Motif.** Seuls les deux renvois **affichés** ont été traités ici, parce qu'ils
tombent sur l'écran où la règle est déjà écrite. Les autres demandent de
déterminer, un par un, lequel des deux documents chaque site vise — un travail de
relecture de soixante sites, dont la sortie est du texte et non du code, et qui
appartient à la passe qui consolide déjà les documents normatifs.

### C — Les pages **justes** qui ne nomment pas leur édition (17 sites)

Après le §7, tous les `p. N` vivants du code sont exacts contre le PDF livré.
Dix-sept ne portent pas `(3ᵉ éd.)` : `agregation.rs` ×3, `alignement.rs:12`,
`allocation.rs:117` et `:213`, `cascade.rs:474`, `consensus_lineaire.rs:91`,
`elasticite.rs:138` et `:437`, `scenario_m.rs:51`, `soupcon.rs:184` et `:611`,
`stigmergie.rs:7`, `:693`, `:694`, `:956`. F2 les qualifie de provenances fausses
et non imprécises.

**Motif.** Ce n'est pas un lissage mais l'achèvement de la migration, que
`CLAUDE.md` décrit comme en cours et fait mesurer par une commande. La faire
entière suppose de fixer la forme — `(3ᵉ éd.)` après la page, `, 3ᵉ éd.` dans une
chaîne de provenance, les deux coexistent déjà — et de décider si un renvoi de
section sans page la porte aussi. Décision de convention, à prendre avec le
document qui l'énonce.

### D — La dérivation du §7.3 (21–31 s) est implantée trois fois, avec trois arbitrages différents

- `sim_core::detecteur::Detecteur::completude` — `saturating_mul`, et
  `Detecteur::nouveau` **panique** sur un seuil nul, avec sa section `# Panics`
  (arbitrage de M1, C6) ;
- `sim_agents::soupcon::DetecteurInfectieux::completude` — **refuse** le seuil
  nul par un `Result`, au titre de la clause 4 du §7 de `docs/SPEC.md`
  (arbitrage de M3, G-e) ;
- `sim_agents::cycle_de_vie::retirer` — recalcule la borne haute
  (`période × (seuil − 1) + expiration + période`) à la main, refuse le seuil nul
  par un `Result`, et **ne sature pas** le produit.

Deux tests portent le même nom dans deux crates
(`la_completude_retrouve_les_21_a_31_secondes`) et vérifient le même chiffre du
traité sur deux implantations.

**Motif.** Unifier suppose de rouvrir l'arbitrage `assert!` contre `Result` que
M1 a tranché et documenté, ou de faire dépendre `sim-core` de `sim-agents` — la
chaîne va dans l'autre sens. Faire appeler `completude` par `retirer` est
possible et supprimerait la troisième copie ; c'est une refonte de mécanisme, pas
un lissage, et NF-15 exige que le chiffre reste retrouvé par une mesure. Signalé
plutôt que corrigé à moitié.

### E — `Rumeur::etat` panique toujours hors population

Le §8 en documente le chemin ; il ne le ferme pas. Le remède est celui de
`TriDeVue::vue` — rendre `Option` —, c'est-à-dire un changement de signature
publique. La méthode n'a aucun appelant dans le dépôt.

### F — Deux tests subsumés, laissés en place

`scenario.rs:773` (`chaque_scenario_porte_son_bloc_de_trois`, relevé par M4 au
constat C) et `scenario_d.rs:393`, qui assère que `BLOC_D` nomme son édition —
clause désormais tenue pour les dix par `les_dix_blocs_nomment_leur_edition`.
Retirer un test est une décision d'inventaire, pas un correctif ; la consigne
interdit d'affaiblir la suite et je m'y tiens.

### G — Ce que ces changements rendent faux dans les documents normatifs

Rien n'a été édité dans `docs/`, `CLAUDE.md` ni `README.md`. À porter :

1. **`CLAUDE.md`, « Six mécanismes des phases 1 à 5 n'ont aucun appelant »** —
   sept depuis le §4, `cycle_de_vie` compris. Même énoncé au §0 du PRD.
2. **`CLAUDE.md`, « Quatre des quinze oracles du catalogue ne sont armés par
   aucune exécution »** — le code en déclare **six** depuis la campagne
   (`CONSERVATION`, `ACCORD_LOCAL`, `D1`, `D2`, `UN_SEUL_PROPRIETAIRE`,
   `TOUTE_PARTITION_A_UN_PROPRIETAIRE`), dont deux ne sont armés nulle part, pas
   même par un test. Divergence relevée par M4 et non résorbée.
3. **Le compte de tests** passe de 465 à **466**.
4. **Quatre commentaires de code citent la « deuxième édition »** du traité comme
   source d'un mécanisme livré : `sim-milieu/src/lib.rs:18` (ch. 8),
   `sim-core/src/famille.rs:4` (§1.1), `sim-core/src/faute.rs:516` (§8.3,
   EX-C20), `sim-agents/src/stigmergie.rs:357`. Le dépôt ne contient que la
   troisième. Les sections existent dans les deux, et la phrase se lit comme de
   l'histoire (« ce que la deuxième édition a introduit ») autant que comme une
   provenance. Décider laquelle des deux lectures fait foi appartient à la clause
   d'édition que la consolidation est en train de reprendre.
5. **`docs/SPEC.md` et `docs/architecture.md`** annoncent les comptes des listes
   d'absences (19, 9 et 5 énoncés). Le premier reste à 20 entrées ; sa quinzième
   a changé de contenu, pas de rang. À revérifier à la consolidation.

---

## Preuves

Commandes lancées à la racine du dépôt, `CARGO_TARGET_DIR` dérouté vers un chemin
ASCII : l'éditeur de liens de mingw échoue dans le `target/` du dépôt, dont le
chemin porte un « é ».

```
$ cargo clippy --workspace --all-targets --release
    Finished `release` profile [optimized] target(s) in 1.81s
clippy exit=0
```

```
$ cargo test --workspace --release
test result: ok. 253 passed  (sim-agents lib)
test result: ok.   4 passed  (determinisme)
test result: ok.  11 passed  (scenario_b)
test result: ok.   5 passed  (sortie_phase_2)
test result: ok.   4 passed  (sortie_phase_3)
test result: ok.   5 passed  (sortie_phase_4)
test result: ok.   3 passed  (sortie_phase_5)
test result: ok.  11 passed  (sortie_phase_6)
test result: ok.  96 passed  (sim-core)
test result: ok.  68 passed  (sim-milieu)
test result: ok.   6 passed  (sim-viz)
test exit=0
```

**466 tests, 0 échec** — 465 à la ligne de base. Un ajouté
(`aucune_liste_dabsences_ne_porte_de_balisage_markdown`), aucun retiré, aucune
assertion relâchée ; `les_dix_blocs_nomment_leur_edition` couvre cinq blocs de
plus qu'avant sous son ancien nom.

```
$ cargo doc --workspace --no-deps
    Finished `dev` profile [unoptimized + debuginfo] target(s) in 3.05s
   Generated …\doc\banc_dt1\index.html and 9 other files
doc exit=0
```

Aucun avertissement sur les trois commandes.

La mesure des pages se refait ainsi :

```python
import pymupdf, re
d = pymupdf.open("Traité.pdf")
norm = lambda s: re.sub(r"\s+", " ", s.replace("’", "'"))
txt = [norm(p.get_text()) for p in d]
find = lambda s: [i + 1 for i, t in enumerate(txt) if norm(s) in t]
print(d.page_count, find("l'ordre est total à l'intérieur"))   # 143 [14]
```
