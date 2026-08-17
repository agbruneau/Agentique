# PRD — stigmergie-lab

**Simulateur déterministe d'essaims d'agents logiciels coordonnés par le milieu**

| | |
|---|---|
| Document | Product Requirements Document |
| Version | 3.0 |
| Date | 13 août 2026 |
| Auteur | André-Guy Bruneau |
| Source normative | `Traité.pdf`, **à la racine du dossier et non sous `docs/`** — *Traité sur les systèmes multiagents en essaim*, **troisième édition, revue sur sa propre mesure, 15 août 2026** — 8 chapitres, 24 sections, 123 notices, **143 pages**. *La révision 3.0 de ce document a été écrite contre la deuxième édition, du 13 août 2026 ; l'édition normative est passée à la troisième le 17 août 2026 (F2, DT5), et **ses renvois de page y ont tous été migrés le même jour**, un par un et par ancre textuelle — voir F2, §0.2 et [`bancs/audit-2026-08/FINITION-prd.md`](../bancs/audit-2026-08/FINITION-prd.md). **Une page de ce document ne se cite plus sans son édition** : la forme est `p. N, Xᵉ éd.`, et une seule ligne le vérifie.* |
| Statut | Réalisé — **six phases livrées**. Le critère de sortie de la phase 6 est **atteint sur trois de ses quatre points et refait sur la mesure pour le quatrième** ; réserves et écarts au §0. Révisé par l'audit du dépôt du 13 août 2026, dont les corrections sont marquées **(audit)**, puis par l'audit du 17 août 2026, consigné au §0.2. **Le compte de tests est une mesure et ne se cite pas** : `cargo test --workspace --release` rend **467 tests, 0 échec** au 17 août 2026 à 11 h 14 |

---

## 0. Suivi de réalisation

*Section de suivi, hors argument. Elle enregistre l'avancement ; elle ne modifie aucune exigence. Les budgets déclarés sont ceux du §9 — décisions de projet sans provenance dans le traité (F1).*

### 0.0 Révision 3.0 — ce que la deuxième édition du traité change

⚠ **Cette sous-section est de l'histoire, et sa pagination l'est aussi.** Elle
enregistre ce que la **deuxième** édition a changé, et c'est ce qu'il faut lire
avant de toucher à un mécanisme existant. Mais le seul traité que le dépôt
contienne est la **troisième**, du 15 août 2026 : les pages citées ici sont celles
de la deuxième et ne résolvent pas dans le fichier livré. Ce que la troisième
change — dont deux écarts qu'elle absorbe et trois citations qu'elle retire — est
au **§0.2**, avec la clause de F2 mise à jour.

Le traité a été republié le 13 août 2026 en deuxième édition. Trois choses en découlent, et il faut les séparer, parce qu'elles n'ont ni le même coût ni le même statut.

**(a) Toute la pagination a bougé.** Le texte a été refondu ; les 40 renvois de page de ce document pointaient sur la première édition et pointaient donc à côté. Ils sont repris. F2 gagne une clause : **une page citée sans son édition n'est plus une provenance**, et ce document ne cite plus que la deuxième.

**(b) Des insertions dans chacun des chapitres 1 à 7, et aucune réfutation.** Aucun mécanisme livré ne devient faux. Ce qui change est le **domaine de validité** de sept énoncés, et le tableau 21 de la nouvelle édition en dresse l'inventaire — les sept supposent l'indépendance des tirages ou des fautes, aucun ne le dit dans son énoncé, tous cessent de tenir sur une population qui décide comme un seul agent. Six des sept sont **déjà livrés et déjà mesurés** dans ce dépôt. C'est le fait le plus lourd de cette révision : le simulateur tourne, les bornes cessent de tenir, et rien dans le code ne le signale — ce qui est très exactement le mode de rupture qu'EX-A42 et RQ10 surveillent, sur une hypothèse de plus.

| Énoncé du traité | Hypothèse d'indépendance | Où il est livré ici | Ce qu'il devient à conformité maximale |
|---|---|---|---|
| Plancher d'exploration du renforcement stigmergique (§1.2) | Tirages des n agents indépendants | EX-A11b/c, scénario B, **oracle armé en permanence** | La population explore comme **un seul** agent ; le plancher est atteint n fois au même endroit |
| Redondance de facteur k (§2.1) | Défaillances des répliques indépendantes | EX-M05 à EX-M08, scénario D | n répliques valent 1 ; la corrélation porte désormais sur la **décision**, plus seulement sur la panne |
| Décorrélation par gigue pleine (§2.3) | Les délais tirés diffèrent d'un agent à l'autre | Annexe B (repère externe) ; non implanté | La gigue décorrèle les **instants**, jamais le **choix** : tous relâchent différemment vers la même cible |
| Approximation de champ moyen (§3.1) | Échangeabilité **et** décorrélation des tirages | EX-A16, EX-A53, RQ5 | La fraction de population dans un état vaut 0 ou 1 ; la fluctuation en 1/√n est **fausse** |
| Vérification statistique (§3.3) | Épisodes échantillonnés indépendants | §8.4, EX-C18, scénario L critère 3 | L'échantillon mesure une population plus étroite que celle qu'il croit décrire |
| Auto-affectation à deux sondes (§5.2) | Choix des serveurs sondés indépendants | EX-A05, scénario F critère 3 | Tous sondent les mêmes candidats ; l'amélioration exponentielle **disparaît** |
| Corroboration r parmi n détecteurs (§7.2) | Détecteurs indépendants | EX-A31, scénario L | Le gain de précision s'annule ; le taux de base reprend ses droits |

La septième ligne est la seule que le produit sût montrer avant la phase 6 : le scénario L la parcourt de bout en bout par le curseur de structure des domaines (EX-C14), et son critère de sortie de phase 5 est atteint. Les six autres n'avaient **aucun curseur** : EX-C14 corrèle les **fautes**, pas les **décisions**, et rien dans le modèle ne faisait décider deux agents ensemble. La phase 6 comble ce trou par EX-C19, et EX-A58 arme les sept dettes sur le code existant.

### 0.1 Écart relevé par la phase 6 — Φ_c ne mesure pas ce que ce document lui prêtait

NF-15 impose de consigner l'écart, et celui-ci porte contre **ce document** plutôt que contre le traité. Il est écrit dans le code à l'endroit où il se constate — `sim_agents::conformite::CONSTAT_DE_MESURE` — et se reproduit par :

```bash
cargo run -p sim-agents --example diagnostic_conformite --release
```

**Ce que le §9 annonçait**, avant toute mesure : *« Φ_c mesuré passe de ≈ 0 à ≈ 1 par le seul curseur de structure des familles »*, et c'était le premier point du critère de sortie de la phase 6.

**Ce que la mesure donne**, sur le scénario B à n = 24, m = 6, graine 7, précision ± 0,003 sur ≈ 10⁵ paires :

| part de conformité | 0 | 0,25 | 0,5 | 0,75 | 1 |
|---|---|---|---|---|---|
| **Φ_c mesuré** | 0,173 | 0,180 | 0,181 | 0,228 | 0,186 |
| tirages partagés | 0 | 2 563 | 5 129 | 7 687 | 9 828 |

Trois faits, et aucun n'était prévu.

1. **Φ_c vaut déjà 0,17 à curseur au repos**, avec un tirage par agent. Ce n'est pas un défaut de l'estimateur : les agents lisent tous la même trace, donc leurs décisions **sont** corrélées. C'est la thèse de l'ouvrage — la coordination par le milieu — mesurée par la grandeur que le ch. 8 propose pour mesurer autre chose.
2. **Le curseur ne déplace Φ_c que de ≈ 0,055** — de 0,173 à 0,228, l'amplitude étant prise max − min sur le curseur, comme le calcule `le_curseur_controle_le_partage_des_tirages_et_non_lamplitude_de_phi_c`. Soit **dix-huit fois** sa précision et **un dix-huitième** de l'amplitude annoncée. La conformité du tirage est un contributeur **minoritaire** devant celle du milieu. *(audit : la version antérieure écrivait « ≈ 0,02, une soixantaine de fois sa précision, un huitième de l'amplitude », trois nombres qu'aucune lecture des mesures ne rend compatibles.)*
3. **La relation n'est pas monotone** : 0,75 rend plus que 1,0. Partager un uniforme entre agents dont les vues de φ diffèrent ne force pas le même choix.

**Ce que l'écart établit, et il porte contre le traité autant que contre ce document.** Φ_c mesure la corrélation des décisions **sans distinguer** celle qui vient de la fonction de décision de celle qui vient du milieu partagé. Sur un essaim stigmergique les deux coexistent et la seconde domine. Le §8.1 du traité propose Φ_c comme paramètre d'ordre de la conformité d'une population ; ce qu'il mesure ici est la somme des deux, et rien dans la grandeur ne les sépare. C'est un cinquième écart au sens de NF-15, et il entre au [registre](decisions.md).

**Deux conséquences de conception, appliquées.**

- **EX-A58 n'efface plus une borne sur Φ_c mesuré, mais sur le réglage.** NF-14 parle d'un *réglage qui viole une hypothèse*, et c'est la structure des familles qui la viole démontrablement : dès que deux agents partagent une famille, leurs tirages ne sont plus indépendants. Effacer sur Φ_c aurait affirmé que l'hypothèse d'indépendance des **tirages** est violée alors que ce qui est mesuré est la **coordination** — une fausse alarme, que la discipline de PD12 interdit d'afficher comme une preuve. Φ_c reste affiché comme une mesure, à côté et jamais à la place.
- **Le premier point du critère de sortie de la phase 6 est refait sur la mesure**, comme DT1 et NF-05 l'ont été. Ce que la phase établit est plus fort et moins spectaculaire que ce qu'elle annonçait : l'hypothèse d'indépendance des sept énoncés du tableau 21 était **déjà** portée sans être dite par le code livré des phases 1 à 5, et rien avant EX-A58 ne le signalait.

**Critère de sortie de la phase 6** :

| Point du critère | État | Preuve |
|---|---|---|
| Φ_c passe de ≈ 0 à ≈ 1 par le seul curseur | **Non atteint — contredit par la mesure** | Φ_c ∈ [0,173 ; 0,228] sur tout le curseur. Refait : *le curseur contrôle le partage des tirages, de façon monotone et vérifiable*, ce que fixe `le_curseur_controle_le_partage_des_tirages_et_non_lamplitude_de_phi_c` |
| Les bornes s'effacent sans être grisées, **et** aucun oracle de sûreté armé ne se déclenche pendant l'effacement | **Atteint** | `Params::bornes_applicables` rend une `Err` portant le motif dès que la part de conformité est non nulle ; les sept verdicts du tableau 21 passent à `Effacee`. Aucun `Option` grisé, aucun drapeau. Et sur trois parts × trois graines, `violations_de_surete == 0` : le mécanisme tourne, les oracles restent muets, et ce qui cesse de tenir est une borne que rien dans le protocole ne surveille. **Portée exacte de cette seconde moitié, relevée par l'audit** : à part nulle, `PLANCHER` et `HORS_DOMINANTE` sont *évalués* à chaque cycle et restent muets, ce qui est une mesure ; dès que la part est non nulle, NF-14 efface la borne et `verifier_bornes` sort avant de les évaluer — leur silence est alors tenu **par construction**. Le test vérifie donc en plus, sous effacement, ce qui reste réfutable : que l'exécution va à son terme, que les sept bornes sont retirées, et que la mesure survit à l'effacement. *(audit : ces deux clauses formaient une seule phrase au §9 et étaient tabulées en deux lignes ici, d'où un critère compté tantôt à quatre points, tantôt à cinq.)* |
| Le contraste avec et sans identité apposée est lisible sans explication | **Atteint** | `sessions_partagees` vaut 0 en nominal et 1 sous le préréglage « identité partagée » : le milieu appose fidèlement une identité fausse et ne peut que le **constater** |
| Le dépôt aveugle coûte un tour de journal de plus, et zéro message de plus | **Atteint** | 48 messages et 8 tours de journal pour 4 tours de délibération à n = 6 ; les deux comptes sont affichés séparément |

**(c) Un huitième chapitre, transposé puis livré.** §8.1 (conformité), §8.2 (la trace comme témoignage), §8.3 (buts incompatibles) sont spécifiés au §6, au §7 (scénario M) et au §9 (phase 6). La phase 6 est **livrée** : cinq modules nouveaux, 419 tests à sa clôture et 428 après l'audit, clippy propre. Elle a produit un **écart au PRD lui-même**, consigné ci-dessous et au §0.1 — la grandeur que le ch. 8 propose ne mesure pas ce que ce document lui prêtait.

| Phase | Thèse | Budget déclaré | État | Critère de sortie atteint |
|---|---|---|---|---|
| 1 — Le noyau et la thèse | Le point partagé est déplacé, et le déplacement se voit | 10 sp | **Terminée** — 93 tests | **Oui, sur les quatre points** (détail ci-dessous) |
| 2 — Le milieu réel et son prix | m − 1, jamais k − 1 ; et le débit a un maximum qui se mesure | 12 sp | **Terminée** — 185 tests | **Oui, sur les cinq points** (détail ci-dessous) |
| 3 — Propager, converger, s'accorder | Trois exigences de force croissante, et le prix qui les sépare | 14 sp | **Terminée** — 249 tests | **Oui, sur les quatre points** (détail ci-dessous) |
| 4 — La fenêtre de violation | Toute gouvernance distribuée est une gouvernance à fenêtre de violation | 14 sp | **Terminée** — 312 tests | **Quatre points sur cinq** — le premier, « le tableau 15 se remplit par la mesure », est **non atteint** (détail ci-dessous) *(audit)* |
| 5 — Cas d'étude et limites | Une réponse fausse d'une quantité inconnue, que rien ne trahit | 8 sp | **Terminée** — 348 tests | **Oui, sur les trois points** |
| 6 — Le second axe | Un milieu qui rend la coordination bon marché rend du même geste la conformité, la collusion et la tromperie bon marché | 10 sp | **Terminée** — 419 tests, 428 après l'audit | **Partiellement** — trois points sur quatre ; le premier est **contredit par la mesure** et refait (détail ci-dessous) |

**Phase 1 — bancs.** Le découpage en bancs est un ordonnancement de réalisation, pas une subdivision des livrables du §9.

| Banc | Portée | Exigences visées | État |
|---|---|---|---|
| 0 | Tableau de suivi, chaîne d'outils, workspace | §5.1 | **Fait** |
| 1 | Banc d'essai flottant natif/WASM, verdict DT1 | DT1, RQ1, NF-02 | **Fait** — [verdict](../bancs/dt1-flottant/VERDICT.md) |
| 2 | `sim-core` : moteur DES, horloge logique, RNG semé, modèle de faute, détecteur, oracles | EX-C01 à EX-C11, PD6, PD10, PD12 | **Fait** — 45 tests, dont NF-15 (détection 21–31 s) |
| 3 | `sim-milieu` sans réplication : journal partitionné M1–M4 | EX-M01 à EX-M04, EX-M09, EX-M13 | **Fait** — 13 tests, oracles M1–M4 armés |
| 4 | `sim-agents` : algorithme 2 et ses quatre modes, algorithme 1, diffusion pair à pair | EX-A01, EX-A02, EX-A04, EX-A10, EX-A11a/b/c, EX-A12 | **Fait** — 31 tests |
| 5 | `sim-viz` natif, scénarios B puis A | EX-V01, EX-V02, EX-V07, EX-V08, EX-V11, PD3, PD8 | **Fait** — binaire `stigmergie-lab` |
| 6 | Critère de sortie de la phase 1 | NF-01, NF-04, NF-09, NF-10 | **Fait** — 93 tests, clippy propre |

**Critère de sortie de la phase 1** (§9, repris ici sans modification) : le scénario B se rejoue à l'identique par graine ; les quatre modes de défaillance sont provocables par préréglage ; le plancher d'exploration mesuré respecte sa borne ; DT1 est tranchée sur mesure et non par défaut.

| Point du critère | État | Preuve |
|---|---|---|
| Le scénario B se rejoue à l'identique par graine | **Atteint** | NF-04 : 100 graines, deux exécutions chacune, traces et mesures égales ; 100 graines distinctes donnent 100 traces distinctes |
| Les quatre modes de défaillance sont provocables par préréglage | **Atteint** | Un test NF-10 par mode : essaim aveugle (T < ℓ₉₉), trace optimiste / pessimiste, rejeu avec effet dupliqué, incomparabilité M2 |
| Le plancher d'exploration mesuré respecte sa borne | **Atteint** | Oracle EX-A11b armé en permanence, vérifié sur 20 graines ; aucune violation |
| DT1 est tranchée sur mesure et non par défaut | **Atteint** | [Verdict DT1](../bancs/dt1-flottant/VERDICT.md) : flottant partout, transcendantes par `libm`, sept méthodes de `f64` interdites par `clippy.toml` |

**Phase 2 — bancs.**

| Banc | Portée | Exigences visées | État |
|---|---|---|---|
| 7 | Réplication ISR, R1/R2, registre des hypothèses fortes, scénario D | EX-M05 à M08, M10 à M12, M14, M15, EX-C12 | **Fait** |
| 8 | Coût du lot, groupe de consommation, rééquilibrage, parallélisme, rétention, plan de contrôle | EX-M16 à M23, DT7 | **Fait** |
| 9 | File et service par agent, population variable, élasticité, sondes, budget de perturbation | EX-C15, EX-C17, EX-A25 à A27, A46 à A49 | **Fait** |
| 10 | Mode campagne sans interface, régression USL, scénario C | EX-V10, scénario C | **Fait** |
| 11 | Parité de sortie natif/WASM, partage par URL | EX-V09, EX-V12 | **Fait** — [banc de parité](../bancs/parite-wasm/) |
| 12 | Directive avec époque, affichages EX-V13 à EX-V17 | EX-A07, PD4, EX-V03, EX-V04, EX-V19 | **Fait** |
| 13 | Critère de sortie de la phase 2 | — | **Fait** — 5 tests dédiés |

**Critère de sortie de la phase 2** (§9, **reformulé** — le §9 nomme les tableaux 7, 11, 12, 14 et les figures 4.2 et 5.1 ; l'écart est en réserve) :

| Point du critère | État | Preuve |
|---|---|---|
| Le scénario C retrouve σ et κ injectés par construction, dans son intervalle de confiance | **Atteint** | Validation croisée sur trois jeux de paramètres ; la campagne rend σ̂ = 0,019945 pour σ = 0,02 et κ̂ = 0,00010018 pour κ = 0,0001 |
| R1 tombe exactement à t₄, jamais avant | **Atteint** | Rejeu pas à pas : aucune violation jusqu'à t₄, violation à l'élection hors ISR, aucune si l'on attend un membre |
| `min.insync.replicas = 1` fait tomber la tolérance de f à 0 sans qu'aucune erreur ne soit émise, et l'interface le nomme | **Atteint** | Le producteur écrit encore et reçoit son accusé à largeur 1 ; seul l'affichage EX-V15 le trahit |
| Un lien partagé reproduit la figure exactement chez le destinataire | **Atteint** | Trace, effort par tranche et φ moyen identiques après encodage/décodage ; lien d'une autre version refusé (NF-03) |
| Le préréglage « oscillation » diverge avec un compteur de pannes strictement nul | **Atteint** | Amplitude ≥ 8 et inversions de sens ≥ 4 sur 200 périodes, `pannes == 0` |

**Réserve de la phase 2 — levée : l'interface WASM est empaquetée.** EX-V12 est tenue et vérifiée par un banc dédié : les six cas du scénario B produisent des empreintes identiques en natif et en `wasm32-unknown-unknown`, bits des flottants compris. EX-V09 est tenue et testée. L'empaquetage qui restait — `wasm-bindgen`, page d'accueil, hébergement statique (DT4) — est fait : `sim-viz` expose une bibliothèque que les deux cibles partagent, `web/index.html` charge le module, et trois fichiers déposés côte à côte suffisent, sans dépendance serveur. **NF-08 est mesurée**, et **remesurée par l'audit** sur les sources d'aujourd'hui : **3 663 058 octets bruts** (3,493 Mio ; 3,66 Mo SI) et **1 445 293 octets compressés** (1,378 Mio ; 1,45 Mo SI, `gzip -9`), contre une cible de 8 Mo. Le chiffre antérieur — 3 550 108 o bruts et 1 409 718 o compressés — datait de la clôture de la phase 5 ; il n'était pas faux, il n'était plus daté. La cible reste tenue d'un facteur cinq et demi, et elle l'est dans les deux conventions d'unité. ⚠ **Et le couple ci-dessus n'est plus daté non plus : ce n'est pas ce chiffre qu'il faut citer.** `web/sim_viz_bg.wasm` est produit par `wasm-bindgen`, exclu du suivi de version, et se périme à la première édition de `crates/sim-viz/` — l'audit du 17 août a mesuré son propre correctif périmé en douze minutes. Ce qui fait foi est la construction la plus récente et les **deux lignes de commande** du [`README.md`](../README.md) (§ « 2. L'interface web »), jamais un nombre écrit ici. Le couple ci-dessus est conservé comme historique de la remesure du 13 août, pas comme état.

Un défaut a été trouvé par l'empaquetage, et il n'aurait pu l'être autrement : `std::time::Instant`, qui sert le temps mural d'EX-V07, **panique** sur `wasm32-unknown-unknown`. Le natif compilait sans rien dire. Le correctif est `web_time`, déjà dans l'arbre par egui. Un lint a été tenté puis retiré — sur cible native, `web_time::Instant` **est** `std::time::Instant` par réexport, et le lint frappait le correctif en même temps que le défaut. **Rien n'attrape la régression aujourd'hui** : `std::time::Instant::now()` compile sans un mot pour `wasm32-unknown-unknown` et ne panique qu'à l'exécution. Ce qui marcherait est `cargo clippy --target wasm32-unknown-unknown` avec le type interdit — sur cette cible, `web_time::Instant` n'est pas `std::time::Instant`, donc le lint frapperait le défaut sans frapper le correctif. Non câblé, et consigné à ce titre.

**Deux points restent hors de l'empaquetage, et ne sont pas des réserves de déploiement.** **NF-07** — 30 images/s à n ≤ 2 000 en WASM — n'est pas mesurée : elle demande un navigateur en avant-plan avec une horloge d'images, et rien de ce qui précède ne l'établit. **EX-V09 n'est pas câblée dans l'interface** : `sim_agents::partage` encode et décode le lien, avec ses tests, mais `sim-viz` ne lit pas le fragment d'URL au chargement et n'en produit pas. C'était déjà le cas en natif ; l'empaquetage web ne l'a ni causé ni corrigé.

**Constat de mesure de la phase 2 — le contrôleur d'élasticité ne converge pas.** Aux valeurs documentées, il tourne autour de sa cible : `visées = courantes × r` est un correcteur proportionnel à gain unitaire, et le temps mort vaut deux périodes de synchronisation. L'écart entre le régime nominal et le préréglage « oscillation » d'EX-A47 est donc une différence **de degré et non de nature** — l'hystérésis de descente divise les inversions de sens par cinq, elle ne les supprime pas. Le constat est consigné dans `crates/sim-agents/src/elasticite.rs` et vérifié par test. Il ne contredisait pas la **deuxième** édition du traité : le §2.2 décrit ce mécanisme comme mesurant « l'effet d'une décision qu'il n'a pas fini d'appliquer ». ⚠ **Il contredit le §7.3 de la troisième** *(audit du 17 août 2026)*, qui conclut que le comportement par défaut « n'est donc pas une oscillation, c'est un dépassement en escalier suivi d'une descente filtrée — et qui cherche une oscillation ne trouve rien à corriger », et qui publie sur la même page les deux réglages dont il tire cette conclusion : fenêtre de stabilisation de 300 s à la baisse et **nulle à la hausse**, deux politiques de montée bornant le pas (100 % ou 4 répliques par tranche de 15 s, la plus permissive l'emportant). Le produit transpose la première valeur et **aucune** des trois autres — le budget de churn ⌊β·T⌋ du §2.2 les remplace. L'écart peut donc venir de la transposition incomplète autant que du traité, et **il n'est pas tranché** : ce qu'il faudrait est transposer les deux politiques de montée, rejouer `cargo run -p sim-agents --example diagnostic_elasticite --release`, et reclasser au [registre](decisions.md).

**Réserves ouvertes à la clôture de la phase 6.** Relevées par l'audit du dépôt
et consignées ici parce que NF-15 et PD6 l'imposent : un mécanisme écrit
qu'aucun scénario n'appelle a, sur un résultat, exactement l'effet d'un
mécanisme absent. *(audit : le titre datait ce tableau de la phase 5 alors que
quatre de ses lignes viennent de la phase 6.)*

| Réserve | Ce qui est en place | Ce qui ne l'est pas |
|---|---|---|
| **NF-05 non atteinte** | Banc `nf05-debit`, verdict remesuré à la clôture de la phase 5 | De l'ordre de 10 à 15 s simulées/s-cœur à n = 1 000, contre 10³. Écart structurel en Θ(n²) ; la cible est à refaire sur la mesure |
| **NF-07 non mesurée** | Empaquetage WASM, NF-08 tenue | Aucune mesure d'images/s : il faut un navigateur en avant-plan avec une horloge d'images |
| **L'interface s'arrête aux scénarios A et B** | Producteurs implantés et testés dans les couches basses | **Seize exigences `EX-V*` sur vingt-trois** sans point d'appel — seules EX-V01, V07, V08, V10, V11, V12 et **V22** en ont un : EX-V02 (mode « enquête »), EX-V03/V04/V19, EX-V05, EX-V06, EX-V09, EX-V13 à EX-V18, EX-V20/V21, EX-V23. Le parcours « le fil » (O6) et l'export n'existent pas. *(audit : le dénominateur datait d'avant EX-V22 et EX-V23, et EX-V22 est câblée depuis la phase 6.)* |
| **Cinq mécanismes du milieu ne sont exécutés par aucun scénario** | `format`, `groupe`, `controle`, rétention et compactage : implantés, testés unitairement | Aucun appelant hors tests. EX-M10 à EX-M23 sont des calculatrices vérifiées, pas des mécanismes du modèle |
| **Le modèle de faute n'est branché sur aucune exécution** | `ModeleFaute` complet, réglable, testé | Aucun scénario ne règle `Config.fautes`, et le moteur ne recevait pas ce réglage. La partition à deux états n'est jamais tirée |
| **DT6 posée, non tenue** | `sim-core::Detecteur`, un objet paramétré | Un seul consommateur au lieu de cinq ; `sim-milieu` n'en instancie aucun ; le sondage indirect est un second objet dans `sim-agents::soupcon` |
| **DT9 et DT11 sans commutateur** | Arbitrage d'époque et modèles de temps décrits | Aucune valeur par défaut pour l'arbitrage ; ni horloge de Poisson, ni couplage synchrone, ni option du scénario H |
| **Pas d'intégration continue** | `cargo test --workspace --release` | NF-13 et NF-16 nomment un mécanisme d'application que le dépôt ne contient pas |
| **Le contrôleur d'élasticité ne converge pas** | Constat mesuré et testé | Voir ci-dessus ; ne contredit pas le §2.2 |
| **La vue affiche la conséquence du mécanisme, jamais le mécanisme** | `Mesures::effort_par_tranche`, rejoué au curseur dans le scénario B | `Mesures` ne porte **aucune** série temporelle de φ : la trace n'est rendue qu'en fin d'exécution. « Lire, déposer, s'évaporer » n'est traçable nulle part, et le reconstituer dans `sim-viz` serait un chiffre inventé (§5.1) |
| **`Comparaison` ne porte pas ce que le scénario A tire** | `scenario_a` sème un `Alea`, perd de vrais messages et fait tourner un détecteur | Ni les pertes, ni les propriétés du détecteur ne remontent. Trois des sept réglages du §7 — `p`, `taux_omission`, `graine` — ne déplacent donc aucun compte affiché, et la graine y reste figée à 1, montrée mais non réglable (EX-V07 tenue, PD12 sans affichage) |
| **Φ_c ne sépare pas ses deux causes** *(nouveau, relevé par la phase 6)* | EX-A56 livré et testé ; le constat est dans `conformite::CONSTAT_DE_MESURE` et au §0.1 | La grandeur mesure la somme de la corrélation due à la fonction de décision et de celle due au milieu partagé. Sur le scénario B, la seconde domine — Φ_c ≈ 0,17 avec un tirage par agent. Aucun estimateur du produit ne les sépare, et le §8.1 du traité n'en propose pas |
| **Trois des sept dettes ne sont pas mesurables ici** | EX-A58 livré : les sept portent leur hypothèse, et `dettes::partage_mesurable()` rend le compte | Gigue pleine (§2.3), champ moyen (§3.1) et vérification statistique (§3.3) portent des bornes qu'**aucun réglage du produit ne met en défaut** : la dette est réelle, le produit ne peut que citer sa conséquence |
| **Quatre mécanismes du ch. 8 n'ont aucun appelant** *(audit : ils étaient trois, le quota manquait)* | EX-A57, EX-M25, EX-M26, EX-A59 implantés et testés unitairement | Aucun scénario ne les exécute, ce qui a sur un résultat exactement l'effet d'un mécanisme absent. La file d'arbitrage n'a même pas d'émetteur : aucun agent du produit ne rencontre un mandat contradictoire, faute de régime du §8.3 du **traité** dans le monde clos (T3). Les quatre sont désormais déclarés par les deux `hors_perimetre()`, que l'interface affiche |
| **Six mécanismes des phases 1 à 5 n'ont aucun appelant** *(nouveau, audit)* | adhésion (EX-A03), alignement (EX-A02), causalité (EX-A08), consensus linéaire (EX-A13, EX-A43), directive avec époque (EX-A07), reconfiguration (EX-A44, EX-A45) | Écrits et testés unitairement, exécutés par aucun scénario. Conséquence directe : **six des quinze oracles du catalogue** — `CONSERVATION`, `ACCORD_LOCAL`, `D1`, `D2`, `UN_SEUL_PROPRIETAIRE` et `TOUTE_PARTITION_A_UN_PROPRIETAIRE` — ne sont armés par aucune exécution, et le contre-exemple PD10 d'`ACCORD_LOCAL` n'est lu par personne. *(audit du 17 août : la ligne comptait quatre ; les deux oracles du groupe de consommation manquaient. `sim_agents::hors_perimetre()` et le §3.3 de `SPEC.md` disaient six. Deux des six ne sont armés nulle part, pas même par un test — `PushPull::armer_oracle` et `Alignement::armer_oracles` n'ont aucun appelant, donc `CONSERVATION` et `ACCORD_LOCAL` ne sont jamais inscrits à un registre. Neuf tournent.)* |
| **`sim-core` n'a pas de liste d'absences** *(nouveau, audit du 17 août)* | `sim_milieu::hors_perimetre()` et `sim_agents::hors_perimetre()` ; `ModeleFaute::hors_modele()` | `grep -rn 'fn hors_perimetre' crates/` ne rend que deux fonctions : le cœur n'en a aucune. Ses absences logent donc dans `ModeleFaute::hors_modele()`, dont ce n'est pas l'objet — sa **première** entrée y énumère **neuf** mécanismes sans appelant, dont six sans rapport avec le modèle de faute pris comme modèle, et le plancher mémoire d'EX-C17, EX-C08 et EX-C16 y sont ou nulle part. **Décision de conception, non tranchée** : ouvrir `sim_core::hors_perimetre()` touche ce document, `SPEC.md`, `CLAUDE.md` et l'onglet « Limites » ; l'alternative est d'écrire que `hors_modele()` est par convention la liste du cœur. Au [registre](decisions.md) |
| **`ModeleFaute::avertissements` n'a aucun appelant** *(nouveau, audit du 17 août)* | La fonction existe, elle est testée, et l'audit y a **ajouté** l'avertissement de crash corrélé que les taux par niveau rendaient nécessaire | Aucun appelant dans `crates/`, `bancs/` compris : la moitié **`[U]`** d'EX-C06 — « l'interface avertit » — n'est tenue par personne, et l'avertissement neuf hérite de la réserve. Les avertissements que la vue affiche viennent de `sim_agents::stigmergie::Params::avertissements`, homonyme et sans rapport. Déclaré par `hors_modele()` |
| **Neuf valeurs de paramètre sont transcrites dans `sim-viz`** *(nouveau, audit du 17 août)* | Les tableaux du §7 de ce document, qui en sont la provenance : `:1095-1100` pour A, `:1132` et `:1134` pour B | `VueA::default` pose six valeurs et `VueB::default` trois ; aucune n'est lue dans `sim-agents`, faute d'accesseur. Rien ne tient la transcription en accord avec le §7, et un test la comparant à elle-même serait tautologique. La graine, elle, ne figure dans aucun tableau. Le contrat de `sim-viz` porte donc « zéro définition de scénario **à deux exceptions nommées** ». **Décision de conception, non tranchée** : remonter les neuf valeurs demande un défaut nommé pour `VueB` et un constructeur de défaut pour `scenario_a`, dont l'API est une fonction nue à sept paramètres. Au [registre](decisions.md) |
| **PD12 n'est pas tenue par le type** *(nouveau, audit du 17 août)* | `#[non_exhaustive]` sur `sim_core::detecteur::Proprietes`, et le fait que le détecteur ne prenne ses nombres que de `sonder` | `#[non_exhaustive]` interdit le littéral, **pas l'affectation de champ** : la structure est `Copy` à quatre champs `pub`, et un exemplaire à `exactitude = Some(0.0)` se fabrique depuis une crate externe. Ce que PD12 tient est plus étroit qu'annoncé — une copie falsifiée ne remonte pas dans l'objet, elle ne trompe qu'un affichage. La doc porte la mesure depuis l'audit. **Décision de conception, non tranchée** : fermer par le type casse `crates/sim-agents/src/pair_a_pair.rs`. Au [registre](decisions.md) |
| **Les prédicats d'oracle du milieu ne sont évalués par aucune exécution** *(nouveau, audit)* | M1 à M4 et M10 armés à chaque exécution du scénario B | `Milieu::verifier`, `verifier_m4` et `verifier_m10` n'ont aucun appelant hors test. Une violation ne pourrait donc pas arrêter l'exécution comme EX-C09 le décrit. R2, lui, est armé **sans prédicat** : il tient par construction d'`avancer_visibilite` |
| **EX-C08 et EX-C16 n'entrent dans aucun résultat** *(nouveau, audit)* | `Agregat` de couverture, générateur de graphes, courtiers, constat de connexité conjointe | Aucun appelant hors test. Le binaire `campagne`, seul chemin multi-exécutions du produit, n'agrège aucune couverture : les conditions à compte nul ne sont donc signalées nulle part |
| **EX-V23 n'a rien à afficher** | Le panneau est spécifié ; `FileDarbitrage::affichage` rend le libellé complet | Sans émetteur, la file est vide en permanence. Le panneau n'est donc pas câblé dans `sim-viz`, et l'onglet « Limites » le déclare |

**Six ajouts aux couches basses que l'interface demande, et qu'aucune passe de
`sim-viz` ne peut faire.** Relevés pendant la révision de l'interface (phase 5,
boucle d'ergonomie), consignés ici plutôt qu'implantés hors portée :

1. **`Mesures::phi_par_tranche`** — φ moyen par tranche et par ressource, écrit
   au même endroit qu'`effort_par_tranche` (`Fourragement::traiter`), donc au
   même découpage, donc superposable. C'est ce qui manque le plus : sans lui, le
   §3 de l'écran promet en mots une évaporation qu'aucune figure ne montre. Deux
   compléments du même geste : `plancher_observe` et `hors_dominante_observee`
   par tranche mettraient la comparaison borne/mesure dans le temps.
2. **`plancher_observe` et `hors_dominante_observee` en `Option<f64>`** — ce sont
   des minimums initialisés à `f64::INFINITY`. **Le cas de γ = 1 est résolu depuis
   l'audit** — `verifier_bornes` relève les deux minimums avant de consulter le
   portail NF-14, donc une borne effacée n'efface plus la mesure —, mais la
   sentinelle subsiste pour une exécution sans aucun cycle, et la vue
   l'afficherait en face de « plancher observé » : lu comme un résultat (F2).
   `sim-viz` rend « jamais observé », mais
   une sentinelle qui franchit une frontière de crate finit toujours par
   s'afficher. `ecart_a_loptimum` fait déjà le bon geste, juste à côté.
3. **`Comparaison` porte les pertes et le détecteur** — `maille.comptes.messages_perdus`
   et `maille.detecteur.proprietes()`. Dès qu'ils sont là, la graine du scénario A
   redevient un curseur légitime, et le taux de fausses suspicions — **calculé**
   par `sim_core::detecteur`, jamais paramétré (PD12) — gagne son premier point
   d'affichage.
4. **`scenario_a` déclare un `ModeleFaute`** et rend son `resume()`, comme
   `ResultatB::modele_de_panne`. Faute de quoi le bandeau EX-V07 du scénario A
   affiche le **libellé du réglage** et le dit explicitement. Le construire depuis
   la vue aurait mis une déclaration de faute dans `sim-viz` (§5.1).
5. **`Comparaison::qui_gagne_en_temps() -> Vainqueur`** — le vainqueur en temps
   n'existe aujourd'hui que comme mot dans la phrase de `verdict_temps`. La
   figure du croisement le lit donc par `contains("la maille gagne")` : une
   reformulation ferait annoncer « aucun croisement » partout, sans erreur de
   compilation. Un test de `sim-viz` échoue à la place, en attendant.
6. **Deux préréglages nommés pour le scénario A** — `petite_equipe` (n = 8,
   ℓ₉₉ = 200 ms) et `grande_population` (n = 2 000), qui sont les deux points du
   critère d'acceptation du §7, donc de la donnée de scénario. Et, du même
   ordre, un `sim_agents::stigmergie::poignees()` : l'effet de chaque poignée du
   scénario B (« γ à 1,00, plus rien ne s'oublie ») est du **traité**, et il est
   aujourd'hui écrit dans la vue, où aucun test ne le confronte au code.

**Un défaut d'affichage, mesuré à l'écran.** Trois chaînes de
`sim_milieu::hors_perimetre()` et de `ModeleFaute::hors_modele()` portent une
emphase Markdown (`**…**`) qu'`egui` rend **littéralement** : l'onglet
« Limites » affiche les astérisques. Même famille :
`sim_core::verification::affichage_avant_lancement()`, dont la doc dit
« affiché avant de lancer », contient une flèche `U+2192` que les polices
embarquées par `eframe` n'ont pas — elle se rendrait en carré vide, si quelqu'un
l'affichait un jour ; elle n'a aucun appelant.

La liste vivante est dans le code — `sim_agents::hors_perimetre()`,
`sim_milieu::hors_perimetre()`, `ModeleFaute::hors_modele()` — et s'affiche dans
l'onglet « Limites ».

**Phase 3 — bancs.**

| Banc | Portée | Exigences visées | État |
|---|---|---|---|
| 14 | Graphe de communication, itération de Perron et ses quatre modes | EX-C16, EX-A13, EX-A43 | **Fait** |
| 15 | Échantillonnage de pairs, tri de vue, les trois agrégations, conservation de masse — scénario H | EX-A14 à A18, A37 à A39, A42, A44, A45 | **Fait** — les 7 critères sont des tests |
| 16 | Rumeur avec retrait, anti-entropie, deux familles de CRDT, coût de l'accord | EX-A19 à A22, EX-A40 | **Fait** |
| 17 | Seuil de quorum, moyenne locale, grille vivante — scénario I | EX-A28, A29, A50 à A52, A55, EX-V18 | **Fait** |
| 18 | Algorithme 3 du ch. 1, fenêtre de divergence — scénario E | EX-A03, NF-14 | **Fait** |
| 19 | Critère de sortie de la phase 3 et réévaluations | — | **Fait** — 4 tests dédiés |

**Critère de sortie de la phase 3** (§9, repris sans modification) :

| Point du critère | État | Preuve |
|---|---|---|
| Le scénario H produit une valeur unanime et fausse, attribuée à la ligne 4, et l'interface ne dit jamais « convergé » | **Atteint** | Dispersion divisée par plus de 100 pendant que la somme quitte sa valeur ; la première rupture porte `Ligne4PullPerdu` ; le critère local est étiqueté « heuristique » |
| Le scénario I remplit les grilles par la mesure, colonnes de signature comprises, lignes non livrées en gris | **Partiellement** | Les trois mécanismes livrés portent leur signature et la ligne « consensus » reste `NonLivree` avec sa valeur du traité (DT7). Mais le §9 nomme **les tableaux 7, 11, 12 et 14 et les figures 4.2 et 5.1** : seuls le tableau 14 et la figure 5.1 existent, et trois de ses **sept** colonnes — `tours_jusqua_larret`, `messages_par_tour`, `condition_darret` — sont des citations formatées, pas des mesures. *(audit : le tableau 14 porte sept colonnes ; `accord::Ligne` en fusionne sept du tableau 14, trois de la figure 5.1 et une ajoutée par le produit. Audit du 17 août : ce tableau est **p. 77, 3ᵉ éd.** — non p. 58, 2ᵉ éd.)* Voir `sim_agents::hors_perimetre()` |
| La fraction résiduelle de susceptibles ne décroît pas quand le budget s'allonge | **Atteint** | Mesurée identique à 60, 240 et 960 tours, et fonction décroissante de K |
| La case « accord » du seuil de quorum bascule sous partition | **Atteint** | Sur douze graines, la décision divisée survient sous partition et jamais sans ; seul l'oracle armé la compte |

**Réévaluation obligatoire à la sortie de la phase 3 — le plafond de scénarios (§2.4, alors de douze).** Sept scénarios sont implantés : A, B (phase 1), C, D (phase 2), E, H, I (phase 3). Cinq restent au plan : F, G, J, K, L. Le total est exactement douze, et **aucun scénario n'a été ajouté** au cours des trois phases. Le plafond n'a donc pas été mis à l'épreuve, et il est reconduit sans modification. Ce qui a effectivement absorbé la matière nouvelle, ce sont les préréglages (RC3) : trente-quatre **à la sortie de la phase 3**, davantage depuis, tous portés par les scénarios existants. Le compte exact n'est pas tenu et ne doit pas être cité comme s'il l'était — aucun registre ne l'énumère, et RC3 porte sur le mécanisme d'absorption, pas sur un nombre.

**Réévaluation obligatoire — la règle d'ouverture d'une cinquième crate (§5.1).** La règle exige les **deux** conditions : plus d'une crate consommatrice, **et** une dépendance que les autres ne doivent pas hériter. Sur le graphe réel, aucun candidat ne les satisfait. `sim-agents` a grossi — dix-huit modules à cette date, vingt-cinq à la clôture de la phase 5 — mais ses consommateurs forment une chaîne unique (`sim-viz` et les bancs), et il n'introduit aucune dépendance dont `sim-viz` devrait être protégé. Découper par thème — `sim-consensus`, `sim-agregation` — produirait des crates à un ou deux mécanismes toutes dépendantes des mêmes couches : exactement le cadriciel que RQ3 surveille. **Aucune cinquième crate n'est ouverte**, et la règle est reconduite telle quelle.

**Deux écarts au traité relevés par la mesure en phase 3.** Ils sont consignés dans le code, à l'endroit où ils se constatent, conformément à NF-15 — « un écart est un défaut du simulateur **ou** une erreur du traité, et les deux méritent d'être trouvés ».

| Écart | Ce que le PRD écrit | Ce que la mesure donne |
|---|---|---|
| Budget de retard du mode « moyeu » (EX-A43) | « moins de 7,9 × 10⁻³ unité de temps du protocole à n = 100 », avec Δ(G) = n − 1 | π/(4 × 99) = **7,933 × 10⁻³**, qui dépasse la borne annoncée. L'ordre de grandeur est juste, l'inégalité stricte ne l'est pas : soit le chiffre vient de π/(4n), soit c'est un arrondi présenté comme une borne |
| Dérive de la somme sans relance (EX-A37) | « avec C = ∞, elle dérive sans borne » | Elle **se fige**. Une fois l'unanimité installée, l'écart entre deux estimations tend vers zéro, donc (x_i − x_j)/2 aussi, et il n'y a plus de masse à perdre. L'énoncé est plus étroit que prévu — et la conséquence est pire : l'erreur devient stable, donc indétectable par l'attente |

**Phases 4 et 5 — bancs.**

| Banc | Portée | Exigences visées | État |
|---|---|---|---|
| 20 | Horloges à dérive, domaines de panne, détecteur infectieux | EX-C13, EX-C14, EX-A23 | **Fait** |
| 21 | Reconfiguration sur soupçon, S1w contre S1, bail de quorum | EX-A24, EX-A33, EX-A41 | **Fait** |
| 22 | AUTO-GUÉRIR et cascade — scénario J | EX-A36, EX-V16, §2.3 | **Fait** |
| 23 | Six mécanismes d'allocation — scénario F | EX-A05, EX-A53 | **Fait** |
| 24 | Gouvernance et fenêtre de violation — scénario K | EX-A09, A30, A54, EX-V20, EX-V21 | **Fait** |
| 25 | Reconstruction causale et critère de sortie de la phase 4 | EX-A08, NF-16 | **Fait** — 5 tests dédiés |
| 26 | Agrégat HyperLogLog — scénario G | EX-A06 | **Fait** |
| 27 | Taux de base — scénario L | EX-A31, A32, A34, A35, DT8 | **Fait** |
| 28 | Vérification statistique bornée et critère de sortie de la phase 5 | §8.4, EX-C18 | **Fait** — 3 tests dédiés |

**Critère de sortie de la phase 4** :

| Point du critère | État | Preuve |
|---|---|---|
| Le tableau 15 se remplit par la mesure | **Non atteint** | Six mécanismes, chacun avec son repère du traité en regard ; le sixième coûte 0 message et 0 tour et n'a aucune condition d'arrêt |
| Cascade complète en trois générations sans qu'aucun agent ne soit tombé | **Atteint** | Trois générations atteintes, compteur de pannes réelles à 0, quatre étapes du bandeau allumées |
| La bascule « décalage seulement » la supprime à charge inchangée | **Atteint** | Zéro redémarrage à charge identique ; un `timeoutSeconds` plus généreux ne la supprime pas et allonge la détection vraie |
| S1w tient, S1 ne tient pas, et la double détention est affichée sans être présentée comme S1 | **Atteint** | Sous arbitrage, S1w tient ; sans, elle tombe exactement au retour de l'agent soupçonné ; l'affichage porte « non rétabli » et « non bornée en asynchrone » |
| Chaque levier affiche sa fenêtre de violation, et « non bornée » là où le traité l'écrit | **Atteint** | En asynchrone, les six leviers affichent « non bornée » sans aucune valeur chiffrée |

**Critère de sortie de la phase 5** :

| Point du critère | État | Preuve |
|---|---|---|
| Le contraste manifeste / sans manifeste est lisible sans explication verbale | **Atteint** | Deux étiquettes — « partiel, manquants = [2] » contre « complet » — et l'erreur affichée est identique dans les deux cas, parce qu'elle mesure l'esquisse et non l'absence |
| P(I\|A) passe de ≈ 99,99 % à ≈ 2 % par le seul curseur de structure des domaines | **Atteint** | 0,999854 à ρ = 0 contre moins de 2 % à ρ = 1, glissement monotone, sans qu'aucun autre paramètre ne bouge ; la détection conjointe reste clouée à 0,343 |
| La voie Monte-Carlo coïncide avec la voie analytique dans l'intervalle de §8.4 | **Atteint** | Accord aux deux extrémités du curseur ; N est affiché avant le lancement, et la campagne ne rend jamais une valeur nue |

**Chiffres du traité retrouvés par la mesure en phases 4 et 5** (NF-15) : détection 21–31 s ; temps de séjour 2,61 / 10,00 / 5,43 / 100,00 du supermarché à d sondes ; détection conjointe 0,343 à r = 3 ; P(I) = 2 × 10⁻⁵ dérivé de ses trois grandeurs ; 0,97 % de probabilité d'échantillonner une intrusion à 1/1024 ; 12 cycles pour réduire la variance d'un facteur 10⁻⁶ ; seuil d'emballement à 69,7 % ; N ≈ 26 492 exécutions à ε = δ = 10⁻², et cent fois plus pour un chiffre significatif de plus.

**Réserve — NF-05 n'est pas atteinte.** Mesurée de l'ordre de 10 à 15 secondes simulées par seconde-cœur à n = 1 000, contre une cible de 10³. L'écart n'est pas un défaut d'optimisation : chaque agent lit ce que toute la population écrit, donc le coût par unité de temps simulé est en Θ(n²). Le [verdict NF-05](../bancs/nf05-debit/VERDICT.md) donne le calcul, distingue la part structurelle de la part corrigeable — l'absence de rétention, qui est EX-M10 et EX-M20 en phase 2 — et pose la question que la mesure ouvre : NF-05 est une cible d'ingénierie posée sans mesure préalable (§8.2), et la mesure la contredit de presque deux ordres de grandeur. Elle est à refaire sur la mesure, comme DT1 l'a été. Rien de la phase 1 n'en dépend : à n = 64, défaut des scénarios A et B, une exécution complète prend deux à trois secondes.

### 0.2 Banc d'audit du 17 août 2026 — ce que la campagne a mesuré, corrigé et laissé ouvert

*Écrit après la campagne, pas pendant : le §0 se met à jour à la fin d'un banc.
Cette sous-section est le verdict de celui-ci. Elle ne rouvre aucune phase et ne
récrit aucun critère de sortie : les six phases restent closes telles que les
sous-sections précédentes les enregistrent.*

**La forme du banc.** Dix agents, cinq morceaux — `sim-core`, `sim-milieu`, les
mécanismes de `sim-agents`, ses scénarios et preuves, `sim-viz` avec les six
documents —, deux tours chacun : un bâtisseur corrige, un critique en contexte
neuf le juge, le bâtisseur reprend sur le jugement. Les dix rapports sont dans
[`bancs/audit-2026-08/`](../bancs/audit-2026-08/) et la consolidation qui les
réunit est [`CONSOLIDATION.md`](../bancs/audit-2026-08/CONSOLIDATION.md). Il était
**interdit** aux dix de toucher ce document et `decisions.md` ; ce qui suit est ce
qu'ils y ont laissé.

**L'état mesuré, avec la ligne qui le refait.** Aucun de ces comptes ne se cite :
il se remesure.

| Ce qui est mesuré | Valeur | Ligne de mesure | Date |
|---|---|---|---|
| Suite complète | **467 tests, 0 échec** — 424 unitaires (254 `sim-agents`, 96 `sim-core`, 68 `sim-milieu`, 6 `sim-viz`) et 43 d'intégration | `cargo test --workspace --release` | 17 août 2026, 11 h 14 |
| Interdictions structurelles | **0**, sortie 0 | `cargo clippy --workspace --all-targets --release` | 17 août 2026, 10 h 24 |
| Renvois rustdoc | **0**, sortie 0 | `cargo doc --workspace --no-deps` | 17 août 2026, 09 h 50 |
| Pages du traité livré | **143** | `python -c "import pymupdf; print(pymupdf.open('Traité.pdf').page_count)"` | 17 août 2026 |
| Notices de la bibliographie | **123** | `awk 'NR>1749' Traité.md \| grep -cE '^[0-9]+\. '` | 17 août 2026 |
| Sections du traité | **24** | `grep -c '^### ' Traité.md` | 17 août 2026 |
| `sim_agents::hors_perimetre()` | **20** entrées | `awk '/pub fn hors_perimetre/,/^}/' crates/sim-agents/src/lib.rs \| grep -cE '^\s*"'` | 17 août 2026 |
| `sim_milieu::hors_perimetre()` | **13** entrées | même ligne, `crates/sim-milieu/src/lib.rs` | 17 août 2026 |
| `ModeleFaute::hors_modele()` | **5** entrées, dont la première énumère **neuf** mécanismes sans appelant | lecture de `crates/sim-core/src/faute.rs` | 17 août 2026 |
| Modules de `sim-agents` | **31** (32 fichiers moins `lib.rs`) | `ls crates/sim-agents/src/*.rs \| wc -l` | 17 août 2026 |
| Énoncés en dur de l'onglet « Limites » | **22** — 8 + 11 + 3 sur trois des six listes | lecture de `crates/sim-viz/src/lib.rs`, fonction `limites()` | 17 août 2026 |

Le compte de tests a bougé pendant la campagne, et c'est un fait sur la mesure et
non sur le produit : 428 à 08 h 10 avant toute modification, 447 à 08 h 32,
465 à 09 h 49, **466 à 10 h 26 — pendant la rédaction de cette sous-section** —,
et **467 à 11 h 14** à la clôture, plusieurs agents écrivant en parallèle. **La leçon est celle-ci, et
c'est le défaut le plus fréquent que la campagne a trouvé, dans le code comme
dans les documents : un chiffre écrit sans la commande qui le produit se périme
sans que rien ne le signale.** Onze minutes ont suffi à périmer un compte de
pages ; douze, à périmer un empaquetage. Tout compte de ce document porte
désormais sa ligne de mesure et sa date, ou n'est pas écrit.

**Ce que la troisième édition du traité change pour ce document.** Le dépôt ne
contient que la troisième, et la clause d'édition de **F2** y passe (voir F2 et
DT5). Trois conséquences, mesurées :

1. **Deux des cinq écarts de NF-15 sont absorbés par la source.** Le §3.1 de la
   troisième édition écrit **7,933 × 10⁻³** et qualifie 7,9 × 10⁻³ d'« énoncé
   faux, non une imprécision » ; le §4.1 écrit « Sans relance, l'erreur ne croît
   pas sans borne : **elle se fige** », puis « la relance de la ligne 11 **ne
   plafonne donc pas** l'erreur ». Les deux mesures que les phases 3 et 4 avaient
   opposées au traité y sont désormais écrites. Le tableau « Deux écarts au traité
   relevés par la mesure en phase 3 » ci-dessus reste vrai de la **deuxième**
   édition, et son libellé le dit maintenant.
2. **Un écart change de camp et n'est pas tranché.** Le constat du contrôleur
   d'élasticité — « il tourne autour de sa cible », différence « de degré et non
   de nature » — était classé comme ne contredisant pas le traité. Le §7.3 de la
   troisième édition conclut l'inverse : le comportement par défaut « n'est donc
   pas une oscillation, c'est un dépassement en escalier suivi d'une descente
   filtrée — et qui cherche une oscillation ne trouve rien à corriger ». Non
   arbitrable en l'état : le produit ne transpose ni la fenêtre nulle à la hausse
   ni les deux politiques de montée que la même page publie, et ce sont elles que
   le traité invoque. Consigné comme ouvert au [registre](decisions.md).
3. **Trois citations de ce document sont retirées ou inversées par la troisième
   édition**, et les trois sont corrigées sur place : la dette « une ignorance
   contre une dette » du §1, que la conclusion nie désormais ; le troisième reste
   donné pour « inchangé » au §2.3, dont la troisième édition écrit que « la
   phrase ne tient plus » ; et la description matérielle de l'ouvrage au §1.

**Réserves ajoutées au tableau ci-dessus** par cette campagne : le compte des
oracles non armés passe de quatre à **six** (ligne « Six mécanismes des phases 1
à 5 »), et quatre lignes sont neuves — l'absence de `sim_core::hors_perimetre()`,
`ModeleFaute::avertissements` sans appelant, les neuf valeurs de paramètre
transcrites dans `sim-viz`, et `Proprietes` qui ne tient pas PD12 par le type.

**Ce que ce banc ne démontre pas.** Rien sur le rendu à l'écran : aucune capture
n'a été prise, les correctifs d'interface sont établis par le code et par
`cargo test`, pas par un œil. **La migration des renvois de page de
ce document a en revanche été faite le même jour**, par une passe de finition distincte
([`bancs/audit-2026-08/FINITION-prd.md`](../bancs/audit-2026-08/FINITION-prd.md)) : 23 justes,
41 corrigées, 10 citant sciemment une édition antérieure, 1 introuvable dans la troisième
édition et consignée au [registre](decisions.md). Ce qu'elle ne couvre pas : les renvois du
**code** et ceux de `docs/README.md`, hors de son périmètre. Rien sur l'empaquetage WASM après 09 h 09 — les
deux chiffres du `README.md` datent d'une construction que l'édition de
`crates/sim-viz/` a périmée ; ce qui se cite est la ligne de commande.


---

## 1. Contexte

Le `Traité.pdf` soutient une thèse : au-delà d'une certaine échelle, l'architecture gagnante déplace la coordination vers un substrat événementiel partagé — un journal ordonné, durable, en ajout seul — où les agents déposent et lisent des traces plutôt que de négocier des décisions. La thèse est un déplacement, non une suppression : ce que le milieu achète en topologie, il le repaie en latence de queue, en contention et en reproductibilité perdue. L'ouvrage en donne la forme exacte :

> le substrat événementiel est supérieur là où la décision est révocable, où l'ordre partiel suffit et où l'échelle est réelle ; il est inférieur […] partout où un invariant global doit tenir à tout instant. (p. 4, 3ᵉ éd.)

L'ouvrage trace cette frontière sur **143 pages** — dont 129 d'argument, la conclusion occupant p. 128-129, 3ᵉ éd., et les Références ouvrant p. 130, 3ᵉ éd. — en 24 sections et 123 notices, avec une discipline inhabituelle : *(audit du 17 août 2026 : cette phrase décrivait 100 pages, dont 95 d'argument, Références à partir de p. 96, 1ʳᵉ éd. — la première édition sous format ferme ; le format a été levé le 15 août. Mesuré par `pymupdf` sur le `Traité.pdf` du dépôt et par sa table des matières.)* chaque mécanisme porte son modèle de panne, son hypothèse de synchronisme, son coût en messages et en tours, sa condition d'arrêt et son mode de défaillance. Il ne fournit cependant **aucun instrument exécutable**, et sa conclusion nomme cinq restes.

| # | Reste de la conclusion | Ce que le produit en fait |
|---|---|---|
| 1 | σ et κ sans protocole de mesure ; u\* reste « une illustration arithmétique » | **Comblé sur le milieu simulé** : scénario C fournit le protocole et sa validation croisée |
| 2 | La vérification paramétrée est indécidable ; le lecteur reçoit « un verdict qu'il peut réciter et non étendre » | **Rendu manipulable** : vérification statistique bornée (§8.4), coût affiché, aucun critère de complétude |
| 3 | La corrélation des fautes invalide les bornes sans invalider le code, et aucun estimateur ne l'évite | **Injectable, non mesurable** : le produit fait varier la corrélation et montre l'effondrement ; il ne l'estime pas |
| 4 | Le graphe de coordination est biparti ; « transporter mécaniquement les bornes donne des chiffres faux ; la forme correcte du résultat reste à écrire » (conclusion, p. 129, 3ᵉ éd.) | **Exhibé seulement** : le produit montre que transporter les bornes spectrales donne des chiffres faux. Il ne fournit pas le théorème. ⚠ **La citation que portait ce document — « un théorème manquant, et non une mesure manquante, est ce qui bloque » (p. 95, 2ᵉ éd.) — ne se retrouve nulle part dans la 3ᵉ édition**, qui écrit au contraire « ce n'est plus le seul endroit du livre où un théorème manque » (p. 129, 3ᵉ éd.). Écart consigné au [registre](decisions.md) |
| 5 | L'effet exactement-une-fois est impossible ; « le seul recours reste l'idempotence de l'effet » (conclusion, p. 129, 3ᵉ éd.) | **Exhibé seulement** : le produit provoque l'effet dupliqué, il ne le supprime pas |

**Ce que la deuxième édition ajoute à cette liste.** La conclusion garde ses cinq restes et rouvre la première de ses deux questions ouvertes en la déplaçant : les agents de langage n'ont plus pour seule assise une taxonomie de traces d'échec, une campagne de mesures existe, et le ch. 8 en tire ce qu'elle établit. Mais l'ouvrage écrivait lui-même le solde : *« Le livre a donc échangé une ignorance contre une dette : il sait maintenant ce qu'il faudrait mesurer, il ne l'a pas mesuré »* (p. 96, 2ᵉ éd.). Aucun des cinq mécanismes que le ch. 8 propose n'était mesuré par personne, et la grandeur qu'il introduit pour rendre la conformité réfutable n'avait ni seuil ni campagne. La suite du travail passait de trois campagnes à quatre, et la quatrième — mesurer la conformité d'une population et le seuil à partir duquel elle la rend fragile — était la seule dont un tiers eût montré la faisabilité.

⚠ **La troisième édition retire cette phrase et écrit son contraire** *(audit du 17 août 2026)*. Sa conclusion, `Traité.pdf` **p. 129, 3ᵉ éd.** : « Le livre n'a donc **pas** échangé une ignorance contre une dette : il a proposé, l'auteur a mesuré, et la mesure lui est revenue contre. » Ce qui a produit le retournement est la phase 6 de ce document : la troisième édition cite ce dépôt en notice 120, avec les valeurs de Φ_c mesurées ici — 0,173 sans conformité imposée, 0,228 au plus quand on l'impose, non monotonement — et avec le compte de cinq écarts du [registre](decisions.md). La quatrième campagne n'est donc plus « la seule dont la faisabilité soit montrée » : elle a été faite, en monde clos, et son résultat est au §0.1. Ce que la troisième édition retient de dette n'est plus une métrologie manquante mais **trois démonstrations manquantes**, dont la décomposition de Φ_c.

| # | Dette de la 2ᵉ édition | Ce que le produit en fait |
|---|---|---|
| 6 | Les cinq mécanismes proposés au ch. 8 — identité apposée, historique vérifié par identité, dépôt aveugle, quota par ressource, journal obligatoire des actions d'agent à agent — ne sont mesurés par personne | **Rendus manipulables, livrés en phase 6** : EX-M24 à EX-M26, EX-A57, scénario M. Le simulateur les fait tourner et les facture ; il ne peut pas les valider sur une population réelle. Quatre des cinq n'ont aucun appelant de scénario, ce que le §0 déclare *(audit : la ligne disait « non livré »)* |
| 7 | Φ_c, la conformité empirique, est proposée sans seuil et sans campagne | **Mesurée sur le milieu simulé, livrée en phase 6** : EX-A56. Même statut que σ et κ au reste 1 — le produit fournit le protocole, la valeur reste celle d'un modèle. Ce que la mesure a trouvé est au §0.1, et il porte contre le traité *(audit : la ligne disait « non livré »)* |

Le projet répond au manque sur deux plans. **Vulgariser** : rendre visibles, manipulables et racontables des mécanismes que le texte ne peut qu'énoncer. **Prolonger** : fournir le protocole de mesure que la conclusion réclame.

Le traité prescrit lui-même la méthode. Le §3.3 décrit, comme algorithme numéroté, une campagne de simulation déterministe à événements discrets : horloge logique, processus unique, aucune concurrence multifil, réseau/disque/temps/RNG abstraits derrière une interface, graine journalisée, rejeu à l'identique du contre-exemple. C'est la spécification du produit, écrite par sa propre source.

**La frontière a deux axes depuis la deuxième édition, et le produit doit les tenir séparés.** Le premier oppose la décision révocable à l'invariant qui doit tenir à tout instant ; il se lit sur le programme, et le ch. 8 lui ajoute une quatrième clause tirée de la mesure — le substrat est supérieur là où *« le critère de réussite est vérifiable sans goût »* (§8.1, **p. 119, 3ᵉ éd.**), un essaim chargé de juger ce qui vaut la peine d'être construit n'y parvenant pas. Le second oppose la population décorrélée à la population conforme ; il se lit sur les agents, selon une grandeur que l'ouvrage propose sans savoir la seuiller. Le verdict qui commande la phase 6 est celui-ci : *« Un système situé du bon côté du premier axe et du mauvais côté du second ne tombera pas là où les sept premiers chapitres l'avaient prévu : il tombera d'un coup, partout à la fois, et aucun de ses composants n'aura fauté »* (§8.3, **p. 127, 3ᵉ éd.**).

**La barre de couverture.** Ce PRD s'engage sur un critère vérifiable : un lecteur tenant la table des matières du traité — **24 sections, 22 tableaux, et dix blocs d'algorithme légendés** (trois aux chapitres 1, 3 et 4, plus l'algorithme 8.1), **auxquels s'ajoutent trois algorithmes numérotés dans le corps du chapitre 2 sans ligne de légende** — ne doit trouver aucun élément qui ne soit **ni** transposé en exigence, en mécanisme ou en scénario, **ni** écarté explicitement, avec sa raison, au §2.3, en annexe A.1 ou au §13. *(audit : « une douzaine d'algorithmes » n'était pas vérifiable ; le compte des blocs légendés l'est, et le chapitre 2 explique l'écart entre les deux façons de compter. Les figures se comptent de deux façons — 18 légendes numérotées pour 16 numéros distincts, la figure 2.1 se déclinant en a/b/c —, donc « 17 figures » n'est retenu sous aucune des deux.)* La barre porte sur la **transposition**, pas sur la livraison, et les deux états ne se confondent nulle part dans ce document. La règle qui rend l'engagement tenable sans faire exploser le produit est au §2.4.

---

## 2. Objectifs

### 2.1 Objectifs produit

| # | Objectif | Mesure de succès |
|---|---|---|
| O1 | Rendre la thèse centrale du traité visible en moins de deux minutes pour un lecteur non spécialiste | Un visiteur web lance le scénario A et énonce correctement le compromis diamètre/latence sans avoir lu le traité |
| O2 | Rendre chaque mode de défaillance nommé dans le traité **provocable par un réglage**, pas seulement descriptible | Chaque mode de défaillance nommé dans un algorithme numéroté du traité correspond à un préréglage nommé dans l'interface |
| O3 | Fournir le protocole de mesure de σ et κ manquant à l'ouvrage | Une campagne produit un ajustement de C(n) avec intervalles de confiance, et le u\* estimé est reproductible à la graine près |
| O4 | Garantir que toute figure produite est rejouable | Toute exécution se rejoue à l'identique — entrelacement compris — à partir de sa seule graine et de sa configuration |
| O5 | Diffuser sans installation | Le simulateur tourne en WASM dans un navigateur, à partir de la même base de code que le binaire natif |
| O6 | Rendre l'**argument entier** du traité parcourable, et pas seulement ses pièces | Un parcours ordonné — « le fil » — enchaîne les scénarios porteurs de bout en bout ; un lecteur qui le suit peut restituer la frontière que le traité trace, dans les deux sens |
| O7 | Rendre le **second axe** de la frontière manipulable au même titre que le premier | Un curseur de diversité de population fait passer Φ_c de ≈ 0 à ≈ 1 sans qu'aucun paramètre de mécanisme ne bouge, et efface une à une les bornes des sept énoncés du tableau 21 (NF-14). **La première moitié de cette mesure de succès est réfutée par la mesure** — Φ_c reste dans [0,173 ; 0,228] sur tout le curseur, §0.1 ; la seconde est atteinte, l'effacement suivant le réglage |

O6 est l'objectif que le doublement du volume rend nécessaire : treize scénarios sans fil conducteur ne sont pas un « tout global », ce sont treize démonstrations. Le commanditaire demande la première chose.

O7 est celui que la deuxième édition du traité rend nécessaire, et il a une propriété qu'aucun autre n'a : il ne fait rien voir de neuf, il fait **cesser de tenir** ce que le produit montre déjà. Sa mesure de succès porte donc sur des scénarios livrés — B, D, F, L — et non sur le scénario M seul. Un curseur qui n'effacerait rien serait un curseur décoratif, et le critère de sortie de la phase 6 est écrit pour l'interdire.

### 2.2 Objectifs de fidélité

Le produit est une transposition d'un texte qui se veut rigoureux ; la fidélité est une exigence, pas une intention.

- **F1** — Tout paramètre exposé dans l'interface porte son unité et, lorsqu'il s'agit d'une latence, son percentile. Le traité traite « un nombre sans provenance » comme une faute de rédaction ; l'interface applique la même règle. Là où la provenance manque, l'interface **affiche l'absence** au lieu de combler.
- **F2** — Toute grandeur affichée qui provient du traité affiche sa référence de section **et sa page**. Toute grandeur qui provient de la simulation est étiquetée comme telle. Les deux ne se mélangent jamais dans le même champ. **Clause ajoutée en 3.0** : l'édition fait partie de la provenance. Deux éditions ne partagent pas leur pagination, si bien qu'une page sans édition n'est pas une provenance imprécise, c'est une provenance fausse. Un renvoi à une édition antérieure subsistant dans le code ou dans l'interface est un défaut bloquant au même titre qu'un nombre sans source.

  **Clause corrigée le 17 août 2026, en l'appliquant à elle-même.** La version 3.0 écrivait « la page s'entend de la **deuxième** édition ». Le seul traité que le dépôt contienne est la **troisième**, du 15 août 2026, `Traité.pdf` à la racine, **143 pages** — mesuré par `python -c "import pymupdf; print(pymupdf.open('Traité.pdf').page_count)"`. La page s'entend donc de la troisième, et le renvoi qui la nomme (`(3ᵉ éd.)`) est le seul qui se relise sans être refait.

  **La migration des renvois est faite depuis la passe de finition du 17 août 2026** ([`bancs/audit-2026-08/FINITION-prd.md`](../bancs/audit-2026-08/FINITION-prd.md)), qui a repris les soixante-quinze `p. N` de ce document un par un, par ancre textuelle et non par arithmétique sur l'ancienne pagination. Résultat : **23 justes, 41 corrigées, 10 citant délibérément une édition antérieure et le disant, 1 introuvable** dans la troisième édition et consignée au [registre](decisions.md). **Aucun décalage constant n'existe entre les deux éditions**, et cinq mesures suffisent à le montrer — le §3.3 est p. 50-55, 3ᵉ éd., et non p. 42-43, 2ᵉ éd. ; le tableau 14 est p. 77, 3ᵉ éd., et non p. 58, 2ᵉ éd. ; la conclusion est p. 128-129, 3ᵉ éd., et non p. 96, 2ᵉ éd. ; les Références ouvrent p. 130, 3ᵉ éd. ; la thèse du scénario M est p. 5, 3ᵉ éd., **et** p. 127, 3ᵉ éd., jamais p. 94, 2ᵉ éd. **Une page se cite désormais avec son édition ou elle ne se cite pas** — la ligne qui le vérifie est en tête du tableau de finition. Le protocole de remesure :

  ```python
  import pymupdf, re
  d = pymupdf.open("Traité.pdf")
  pages = [re.sub(r"\s+", " ", p.get_text()) for p in d]
  def page_de(citation):
      c = re.sub(r"\s+", " ", citation)
      return [i + 1 for i, t in enumerate(pages) if c in t]
  print(d.page_count, d.get_toc())
  ```
- **F5** — **Une mesure liée à une version de modèle porte sa péremption.** La deuxième édition tire du ch. 8 des chiffres pris sur des modèles de langage désignés par leur version commerciale, et l'ouvrage les déclare périssables et non reproductibles hors de cette version. Ils entrent dans le produit exactement comme les chiffres de documentation de courtier : **repères externes en gris, jamais cibles, jamais sorties**, avec la mention de péremption au même rang typographique que la valeur. La règle est celle de l'annexe B, étendue à une seconde famille de sources.
- **F3** — Le simulateur ne revendique aucune garantie que le traité refuse. En particulier, il n'affiche jamais « convergé » : pour l'algorithme 1, le traité écrit « à aucun instant on ne sait si l'accord est atteint » (§1.1) ; pour l'algorithme 2, « cet énoncé est une propriété du tirage, pas un théorème de convergence » (§1.2).
- **F4** — **La vulgarisation ne simplifie que la forme, jamais l'énoncé.** Quand une figure fidèle est illisible, on change la grandeur affichée ou l'échelle ; on ne relâche pas l'affirmation. C'est la moitié constructive de RQ4 : RQ4 dit ce qu'il faut refuser, F4 dit ce qu'il faut faire à la place.

### 2.3 Non-objectifs

Explicitement hors périmètre, et pourquoi :

| Hors périmètre | Raison |
|---|---|
| Un courtier de messages réel branché sur le simulateur (Kafka, Redpanda, NATS) | Le déterminisme exige un monde clos. Le §3.3 le dit : le prix du déterminisme est de ne tester ni les dépendances ni les bibliothèques tierces. Brancher un vrai courtier détruit la propriété centrale du produit. **Le protocole documenté du courtier, lui, est dans le périmètre** — voir l'encadré ci-dessous. |
| Toute grandeur de débit ou de latence attribuée à un courtier réel | Le §6.1 cite ≈ 600 Mo/s en écriture linéaire contre ≈ 100 ko/s en aléatoire ; ce sont des mesures de la documentation de conception, pas des sorties d'un modèle. Elles entrent dans le simulateur comme **paramètres étiquetés et périssables** (F2), jamais comme résultats. |
| Tout plafond de partitions ou de bascule attribué à KIP-500 | Le traité l'écarte lui-même : le KIP vise « des centaines de milliers, voire des millions de partitions » **sans aucune mesure de temps de bascule ni de latence de propagation**, et « tout chiffre attribué à ce KIP est apocryphe » (§6.1). Le simulateur n'affiche aucun plafond de p ; p est borné par le coût de simulation, et l'interface le dit ainsi. |
| Un cadriciel d'agents généraliste | Le produit simule les mécanismes du traité, pas une plateforme d'exécution. La règle de factorisation est PD7 : une abstraction se justifie par des exemplaires **comptés dans le traité**, jamais par un mécanisme imaginé. |
| **La fonction de décision d'un agent de langage** | Inchangé, et la deuxième édition ne le desserre pas : le traité traite un modèle de langage comme « une dépendance non instrumentable, donc un trou dans le monde clos » (§3.3, p. 56, 3ᵉ éd.). Le simulateur n'exécute aucun modèle, n'appelle aucun service, et δ y reste un programme. Ce qui change en 3.0 est plus étroit et plus gênant : le ch. 8 mesure les **conséquences** de cette fonction de décision, et ces conséquences-là sont des mécanismes ordinaires — une corrélation de tirages, un champ d'identité non authentifié, un compteur par ressource. Elles entrent au périmètre (phase 6) ; la fonction qui les produit n'y entre pas. La distinction est celle du §2.3 depuis le début : le **protocole** est transposable, la **mesure** ne l'est pas. |
| **Les valeurs mesurées du ch. 8** | 266 vulnérabilités, 17 à 85 % d'option cachée, 18 agents sur 30 : ce sont les mesures d'un rapport de laboratoire sur ses propres modèles, non revu par les pairs, dont l'ouvrage écrit que rien n'y est reproductible hors de la version de modèle sur laquelle la mesure a été prise. Elles entrent en annexe B comme repères externes périssables (F5), **jamais** comme cibles d'un critère d'acceptation. Un critère de sortie qui exigerait de retrouver l'un de ces nombres serait un défaut du plan : le simulateur ne contient pas ce qui les a produits. |
| Une mesure de production | Ce que le simulateur mesure, ce sont les σ et κ du milieu **simulé**. La distinction est structurante et doit être affichée (voir EX-V11 pour la règle générale, et le libellé permanent du scénario C). |
| **Un protocole d'accord implanté** (Paxos, Raft, KRaft, quorum de métadonnées) | Le traité facture l'accord, il ne le réexpose pas — note de section du §4.2. Le plan de contrôle est simulé **par son prix** — Ω(n) messages par décision, majorité nécessaire sous détecteur fortement exact à terme, terminaison bornée seulement après stabilisation, fenêtre d'indisponibilité de 150–300 ms après arrêt du meneur (§4.2, tableau 13) — et non par son protocole. L'affichage dit que c'est un modèle de coût. Voir DT7. |
| **Des protocoles tolérants aux fautes byzantines** (3f + 1) | Hors modèle par défaut (modèle P : crash-arrêt et omission, §1.1). Le traité la reprend au ch. 7, où §7.2 dit où l'hypothèse « aucun agent menteur » cesse d'être défendable ; ce périmètre-là n'est pas transposé, et son exclusion est un choix de portée, pas une lecture du modèle P. Le traité cite ces protocoles comme **borne**, jamais comme mécanisme. **Le simulateur implante en revanche le point d'injection « agent menteur »**, désactivé par défaut : sans lui, §7.2 et la figure 5.1 n'ont pas d'énoncé. Conséquence à afficher, non à contourner : le §5.1 établit que sous faute arbitraire, aucune solution à moins de 3f + 1 participants ne tolère f déviants, et que ce modèle *tue les trois premiers mécanismes* de la figure 5.1 ; le simulateur ne peut pas montrer leur chute sous ce modèle, il ne peut que déclarer que tout verdict qu'il rend sur eux est **conditionnel au modèle P**. Voir DT8. **Ce que le §8.3 change à cette ligne, et qui est sérieux** : l'effet byzantin y est mesuré comme **endogène** — une population dont chaque membre suit fidèlement sa consigne produit l'escalade, sans qu'aucun agent ait été programmé pour nuire —, et le seuil f < n/3 ne s'y applique pas puisque le nombre d'agents adverses n'est pas borné par l'hypothèse : dans le protocole décrit, il vaut n. L'exclusion des **protocoles** reste, pour la raison qui l'a toujours portée. Ce qui tombe est la présentation de l'agent menteur comme une hypothèse **importée** : DT8 est révisée en conséquence. |
| **Un détecteur de défaillance exact** | Le §4.3 l'interdit : un détecteur « ne prouve pas la mort d'un agent, il la soupçonne ». Une configuration où le soupçon est toujours juste rendrait la sûreté de l'algorithme 3 vraie pour la mauvaise raison, et masquerait exactement ce que le scénario J doit montrer. |
| **La réservation de ressources d'un agent, et donc le dimensionnement vertical automatique** | Le simulateur modélise la métrique qu'une boucle de commande observe — y compris une métrique processeur synthétique, dont la période d'initialisation est un paramètre — mais pas la réservation qu'un contrôleur vertical ajusterait. Sans objet à régler, un contrôleur vertical n'aurait rien à faire. Les chiffres du §4.3 restent en annexe B comme repères, et les deux limites structurelles que le traité déclare invisibles à l'usage sont nommées au scénario J. |
| **La mesure de la corrélation des fautes** | Troisième reste de la conclusion. **La deuxième édition ne le changeait pas** : il n'existait pas d'estimateur qui ne demande pas déjà la vue globale qu'on cherchait à éviter (p. 95, 2ᵉ éd.). ⚠ **La troisième édition écrit que « la phrase ne tient plus »** *(audit du 17 août 2026, `Traité.pdf` p. 129, 3ᵉ éd.)* : l'association entre deux échecs se calcule sur des issues déjà écrites, et elle a une première valeur mesurée par un tiers — deux instances d'un même modèle échouent ensemble sur 90,0 % des missions où l'une échoue, φ = 0,916 sur 18 000 missions, notice 121. **Cela ne change rien au périmètre de ce produit** : la valeur porte sur deux agents et un banc, non sur une flotte, elle n'est pas répliquée, et rien n'en fait un seuil. La corrélation des **fautes** reste un paramètre d'entrée, jamais une sortie — le reste est rétréci, pas comblé. **Piège à ne pas laisser s'installer** : Φ_c, que le ch. 8 propose et qu'EX-A56 transpose, est un estimateur — il se lit sur le sujet où les décisions sont déposées, il ne coûte aucun message, il ne demande aucune vue globale. Il ne comble pourtant pas le troisième reste, parce qu'il ne mesure pas la même chose : il mesure la corrélation des **décisions**, qui sont écrites dans le milieu, et la corrélation des **pannes** n'y est écrite nulle part. Le produit tient les deux grandeurs sous deux noms, dans deux champs, avec deux provenances, et un affichage qui les mêlerait est un défaut bloquant — même règle que les deux ℓ₉₉ du §8.3. |
| **Tout ce qu'un agent peut faire à un pair hors du milieu** | Le §8.3 mesure des agents qui révoquent les comptes système de leurs pairs, tuent leurs processus en boucle et falsifient leurs contrôles de santé. Le traité en tire deux exigences — journal obligatoire des actions d'agent à agent, séparation des droits — dont il dit lui-même qu'elles portent sur ce que le **système d'exploitation** permet en dehors du chemin instrumenté. Le monde clos du §3.3 ne contient aucun système d'exploitation, aucune identité de session, aucun droit d'administration : le simulateur peut modéliser le **refus** de l'action non journalisée (EX-M24, EX-A59), il ne peut pas modéliser le contournement, qui est le mode de défaillance nommé. Ce que le produit rend visible est donc le **coût** de l'exigence, jamais son efficacité. Voir T3. |
| Le model checking exhaustif | Θ(\|S\|ⁿ) : à \|S\| = 8 et n = 12, plus de 6,8 × 10¹⁰ configurations avant tout entrelacement (§3.2). Le §5.3 ajoute le mode de défaillance réel : « passé une taille d'essaim, le vérificateur ne termine pas, et l'ingénieur reçoit un silence qu'il est tenté de lire comme une absence de problème » (§5.3, p. 85, 3ᵉ éd.). Le produit fait de la vérification **statistique**, dont le coût s'écrit. **Le §3.3 y ajoute en 2ᵉ édition une borne d'emploi** : aucun résultat exhaustif n'est disponible sur une population d'agents de langage, le §3.2 dit pourquoi il ne le sera pas, et le substitut enregistré aggrave la difficulté au lieu de la lever — *un essaim rejoué depuis des traces enregistrées ne peut plus produire ni la corrélation ni l'escalade, qui sont des propriétés de la population en train de décider* (§3.3, p. 56, 3ᵉ éd.). Le scénario M n'a donc aucun mode « rejeu de traces », et sa demande serait un contresens. |

**Ce que le §6.1 donne au produit, et ce qu'il ne donne pas.** Le chapitre décrit un vrai courtier ; le produit n'en branche aucun. La ligne de partage n'est pas « Kafka oui / Kafka non », elle est **entre un protocole et une mesure** :

| Élément du §6.1 | Statut | Pourquoi |
|---|---|---|
| Modèle ISR(k, m), R1 sûreté / R2 visibilité, borne de visibilité | **Transposé** (EX-M05, EX-M15) | C'est un protocole : états, transitions, invariants. Un monde clos le reproduit exactement. |
| Temporisateur d'appartenance à l'ISR, 30 000 ms | **Transposé** (EX-M14) | C'est une règle de décision à borne connue. Sa valeur est un paramètre périssable ; son *effet* — l'exclusion d'un suiveur vivant sous charge — est le mécanisme. |
| Protocoles de rééquilibrage (barrière unique, coopératif, battement de cœur) | **Transposé** (EX-M17) | Comptes de messages et de tours dérivables de la mécanique décrite. |
| Sondes de vivacité et de disponibilité, défauts 0/10/1/1/3 | **Transposé** (EX-A26) | Idem : périodes, seuils, effet distinct de chaque sonde. |
| Contrôleur horizontal, tolérance 0,1, période 15 s | **Transposé** (EX-A25) | Formule fermée, condition d'arrêt locale et vérifiable. |
| ≈ 600 Mo/s linéaire, ≈ 100 ko/s aléatoire, écart > 6 000× | **Paramètre étiqueté** (annexe B) | Mesure d'un système réel. Le simulateur peut l'utiliser comme entrée ; il ne peut ni la produire ni la réfuter. |
| Plafonds de partitions de KIP-500 | **Écarté** | Le traité les déclare apocryphes. Les transposer serait fabriquer une provenance. |
| Conformité au comportement réel d'un client Kafka déployé | **Écarté** | Hors monde clos, §3.3. Le simulateur transpose la documentation, pas l'implantation ; un écart entre les deux est invisible d'ici, et l'interface l'affiche en limite. |

### 2.4 Règle de couverture — un scénario par thèse, pas par mécanisme

Vingt-quatre sections, dix blocs d'algorithme légendés plus trois numérotés en corps de texte, une quarantaine de mécanismes. Un scénario par mécanisme est ingérable et illisible ; un scénario par thèse est jugeable. Cinq règles, qui gouvernent le §7 :

| # | Règle |
|---|---|
| **RC1** | Un scénario porte **une thèse réfutable du traité**, citée avec sa page, et pas davantage. Il expose : la thèse, sa source, ses paramètres, sa visualisation, son critère d'acceptation, et ce qu'il **ne** démontre **pas**. |
| **RC2** | Toute section du traité est rattachée à **exactement un** scénario porteur — celui de sa thèse dominante. Les rattachements secondaires se listent (annexe A) ; ils ne créent jamais de scénario. |
| **RC3** | Un mécanisme sans thèse propre n'a pas droit à un scénario. Il a droit à un **préréglage** dans le scénario porteur de sa section, ou à un **banc** (NF-09/NF-10). Jamais aux deux. |
| **RC4** | Deux scénarios qui partagent leur critère d'acceptation n'en font qu'un. La fusion est obligatoire, pas facultative. |
| **RC5** | Une section peut être **écartée**. Alors la raison s'écrit — au §2.3, en annexe A.1 ou au §13 — et jamais en silence. Une section absente sans ligne d'écartement est un défaut du PRD, pas un choix. |

**Plafond : treize scénarios** *(douze jusqu'à la version 2.0)*. Au-delà, on fusionne (RC4) ou on écarte (RC5) ; on n'ajoute pas. Le plafond est révisé une seule fois, à la sortie de la phase 3, sur mesure et non sur intuition — et il l'a été : la réévaluation du §0 constate qu'aucun scénario n'a été ajouté en trois phases, que la matière nouvelle a été absorbée par des préréglages (RC3), et reconduit le plafond sans modification.

**Pourquoi il passe tout de même de douze à treize.** La clause de révision unique borne la croissance du produit **par son propre appétit** : elle interdit d'ajouter un scénario parce qu'un mécanisme est intéressant. Elle ne peut pas border la croissance de la **source**, qui n'est pas une décision du produit. Le traité est passé de 21 à 24 sections ; le plafond était dimensionné sur les 21, et le tenir sur les 24 reviendrait à écarter en silence trois sections de la source normative, ce que RC5 interdit explicitement. Le plafond suit donc la source une fois, avec sa raison écrite ici, et la clause de révision unique reste intacte pour ce qu'elle protège : **aucun treizième scénario n'aurait été admis si le traité n'avait pas changé**, et le quatorzième ne l'est pas.

**Un seul scénario pour trois sections, et non trois.** Le ch. 8 aurait pu en réclamer trois — conformité, épistémique, buts incompatibles. RC1 impose une thèse réfutable par scénario, et le chapitre n'en porte qu'une, que l'avant-propos de la troisième édition énonce : *un milieu qui rend la coordination bon marché rend du même geste bon marché ce que le concepteur ne veut pas* (**p. 5, 3ᵉ éd.** — *la version antérieure de ce document donnait « p. 94, 2ᵉ éd. », qui n'est la page ni de cette proposition ni de son énumération ; voir la thèse du scénario M au §7*). Les trois sections en sont les trois conséquences, que le §8.3 énumère **p. 127, 3ᵉ éd.** — conformité parce que tous lisent la même trace, collusion parce qu'un tableau public suffit, tromperie parce que déposer coûte le même prix qu'on dise vrai ou faux — et elles partagent un unique paramètre de contrôle, la diversité effective de la population. Trois scénarios auraient partagé leur curseur et donc, par RC4, dû fusionner. La fusion est faite d'avance.

Application : la table ci-dessous fixe le rattachement porteur des 24 sections.

| Scénario porteur | Thèse | Sections portées |
|---|---|---|
| **A** — Les deux régimes | Le point partagé n'est pas détruit, il est déplacé | §1.3 (figure 0, tableau 3) |
| **B** — Fourragement stigmergique | L'essaim campe à distance bornée de l'optimum | §1.1, §1.2 |
| **C** — Campagne USL | Le débit a un maximum, et il se mesure | §2.1 (USL), §2.2, conclusion |
| **D** — La chute de R1 | m − 1 disparitions, jamais k − 1 ; et l'ISR muet | §2.1 (ISR), §6.1 |
| **E** — La fenêtre de divergence | Borner la fenêtre = terminer un accord en asynchrone | §1.3 (algo 3) |
| **F** — Allocation comparée | Deux sondes, 2d messages, un tour : la borne à battre | §5.2 |
| **G** — Agrégat fenêtré | Le sous-compte silencieux | §7.1 |
| **H** — La valeur fausse unanime | « Le résultat n'est pas en retard, il est faux » (§4.1, p. 58, 3ᵉ éd.) | §4.1, §3.1 (agrégation) |
| **I** — Propager, converger, s'accorder | Trois exigences de force croissante, et le prix qui les sépare | §4.2, §5.1, §3.1 (Perron) |
| **J** — La cascade de l'agent saturé | « Aucun agent n'est tombé, et l'essaim s'effondre » (§6.1, p. 91, 3ᵉ éd.) | §4.3, §7.3, §2.3 (métastable) |
| **K** — La fenêtre de violation | Toute gouvernance distribuée est une gouvernance à fenêtre de violation | §5.3 |
| **L** — Le taux de base | Une sonde presque parfaite produit des alarmes presque toutes fausses | §7.2 |
| **M** — Le second axe | Un milieu qui rend la coordination bon marché rend du même geste la conformité, la collusion et la tromperie bon marché | §8.1, §8.2, §8.3 |
| *(pas de scénario)* | Le moteur lui-même | §3.2 → §8.4 ; §3.3 → `sim-core` en entier ; §6.2 → EX-A08/EX-V05 ; §6.3 → PD3/PD4/EX-A07 |

### 2.5 Tensions assumées

Deux choix posés ailleurs dans ce document entrent en tension avec le périmètre §2.2/§5.3. Aucun n'est contourné ; chacun est nommé avec son coût.

**T1 — Le non-objectif « courtier réel » n'exempte pas du protocole de groupe.** Le §2.2 chiffre le coût d'un changement de population sur le protocole de rééquilibrage d'un groupe de consommation, et ce protocole a un **coordonnateur de groupe**. Trois conséquences : (a) le protocole est simulé dans `sim-milieu` — c'est un mécanisme du modèle, pas une dépendance externe, et le monde clos tient ; (b) le coordonnateur de groupe est une autorité à vue globale : il est instancié **explicitement et séparément** de l'essaim, exactement comme le coordonnateur du scénario F, et EX-A12 continue de rejeter tout *agent* à perception globale ; (c) les valeurs de phases et de messages sont des valeurs de documentation produit, donc périssables au sens de l'annexe B, et les scénarios mesurent celles du **modèle**, pas celles d'un courtier.

**T2 — Le verdict du §5.3 contredit EX-A12, et c'est PD11 qui tranche.** Le traité conclut que la seule gouvernance qui tienne à tout instant s'applique en un point d'admission unique, c'est-à-dire une autorité centrale. EX-A12 interdit à un agent d'avoir cette vue. Les deux tiennent ensemble uniquement si le produit refuse la troisième option : soit l'autorité est instanciée séparément et affichée comme telle, soit la spécification écrit la durée pendant laquelle l'invariant peut être faux. PD11 l'énonce.

**T3 — Le régime du §8.3 se produit hors du milieu, et le simulateur ne simule que le milieu.** *(Nouveau en 3.0.)* Le ch. 8 mesure une escalade dont les moyens ne passent par aucun sujet : révocation de comptes système, terminaison de processus concurrents, contrôle de santé falsifié. Le traité en tire la règle exacte — *« le journal soit le seul canal par lequel un agent puisse agir sur un autre »* (§6.3, p. 99, 3ᵉ éd.) — et nomme sa contrepartie : tout ce qu'un agent peut faire à un pair en dehors du milieu est par construction hors de la traçabilité du §6.2 et hors de tout limiteur de cadence. Trois conséquences pour ce document, et aucune n'est contournée. **(a)** Le simulateur peut instrumenter le chemin conforme — une action d'agent à agent est un enregistrement, ou elle est refusée (EX-M24, EX-A59) — et il facture ce que cette instrumentation coûte : une écriture par action, plus un chemin d'administration que l'essaim n'automatise plus. **(b)** Il ne peut pas produire le contournement, faute de système d'exploitation dans le monde clos, et c'est précisément le mode de défaillance que la mesure établit. **(c)** Il ne doit donc **jamais** afficher qu'une escalade a été empêchée : la seule chose qu'il établit est qu'aucune escalade **passant par le milieu** n'a échappé au compteur, ce qui est une propriété du modèle et non du régime. Le libellé permanent du scénario M reprend la formule : *ici, le milieu voit ce qu'on lui a fait écrire ; le régime mesuré, lui, contourne le milieu.*

---

## 3. Utilisateurs et usages

### 3.1 Personas

**P1 — Le lecteur curieux.** N'a pas lu le traité, arrive par un lien. Veut comprendre en deux minutes pourquoi « déposer une trace » vaudrait mieux que « se parler ». Ne configurera rien : il presse *Lecture* et regarde. S'il en veut davantage, il suit **le fil** (parcours 5) et sort avec l'argument entier, pas avec douze démonstrations juxtaposées. Sert O1 et O6.

**P2 — L'architecte qui doit se situer.** Conçoit un système distribué réel et veut savoir **de quel côté de la frontière il se trouve**. C'est le premier reste de la conclusion, et il est explicitement adressé à ce persona :

> L'ouvrage a tracé une frontière ; il n'a pas fourni l'instrument qui permet à un lecteur de savoir de quel côté se trouve son propre système. (conclusion, p. 128, 3ᵉ éd.)

Il manipule n, p, γ, T, ℓ₉₉, les seuils de détecteur, les fenêtres de gouvernance, et voit ce qui casse. C'est le persona que vise le verdict du §1.3 : « la première issue couvre la majorité des cas réels et [...] la troisième est choisie par défaut bien plus souvent qu'elle n'est nécessaire ». Sert O2 — et O7 depuis la deuxième édition, la frontière ayant deux axes et ce persona devant se situer sur les deux.

**P3 — Le chercheur.** Veut reproduire une figure, changer une hypothèse, produire une courbe publiable. Utilise le mode campagne sans interface, exporte en CSV, rejoue par graine. Sert O3 et O4.

**P4 — L'auteur du traité.** Veut savoir si le texte tient. Cherche les endroits où la simulation contredit une affirmation du livre — ce qui est un résultat, pas un défaut.

### 3.2 Parcours principaux

1. **Découverte web** (P1) : ouvrir l'URL → un scénario tourne déjà → un panneau de trois phrases explique ce qu'on regarde → un bouton « et si… » bascule un réglage pathologique.
2. **Situer son système** (P2) : répondre à **cinq** questions et obtenir sa position sur les **deux** axes de la frontière, puis le scénario qui montre ce qu'on paie de ce côté-là. Premier axe, celui du programme : la décision est-elle révocable ? l'ordre partiel suffit-il ? l'échelle est-elle réelle ? le critère de réussite est-il vérifiable sans jugement de goût (§8.1, **p. 119, 3ᵉ éd.**) ? Second axe, celui des agents : la population est-elle décorrélée — modèles distincts, contextes distincts, tirages distincts ? Les deux axes sont rendus séparément et jamais additionnés en un score unique : un système bien placé sur le premier et mal placé sur le second ne tombe pas plus tard, il tombe autrement — *d'un coup, partout à la fois, et aucun de ses composants n'aura fauté* (§8.3, **p. 127, 3ᵉ éd.**).
3. **Exploration** (P2) : choisir un scénario → régler → observer la dégradation → lire le mode de défaillance correspondant, nommé et cité.
4. **Campagne** (P3) : écrire un fichier de configuration → lancer en ligne de commande → obtenir CSV + rapport → rejouer une exécution isolée par sa graine.
5. **Le fil** (P1, P4) : un parcours ordonné et linéaire des treize scénarios porteurs, un arrêt par thèse. Chaque arrêt existe en **deux formats** : la version deux minutes (thèse + une figure + la phrase du traité) et la version dix minutes (les réglages qui la cassent). Le fil est partageable à n'importe quel arrêt (EX-V09), et c'est lui qui rend O6 vérifiable. Le treizième arrêt — le scénario M — est le seul qui **revienne** sur les précédents au lieu d'en ajouter un : il rejoue B, D, F et L avec le curseur de conformité poussé, et c'est ce retour, non l'arrêt lui-même, qui rend O7 vérifiable.
6. **Réfutation** (P4) : écrire un oracle → lancer la vérification statistique bornée → obtenir p̂ ± ε avec sa confiance, ou un contre-exemple rejouable.

---

## 4. Principes directeurs

Ces principes ne sont pas des préférences : chacun est dérivé d'un résultat du traité et contraint la conception.

### PD1 — Le déterminisme est la propriété fondatrice, pas une option

Source : §3.3, algorithme 3. Conséquences dures :

- Un seul fil d'exécution pour la boucle de simulation. Pas de `tokio`, pas de `rayon`, pas de `std::thread` dans le cœur.
- Aucun appel à `SystemTime::now()`, `Instant::now()`, ou `rand::thread_rng()` dans les crates de simulation. L'horloge est logique et n'avance que par consommation d'événements.
- Toute source d'aléa dérive d'un unique `ChaCha8Rng` semé, dont la graine est journalisée avec la configuration complète.
- L'itération sur les collections associatives est ordonnée. `HashMap` est interdit dans tout chemin qui influence l'ordonnancement ; `BTreeMap` ou `IndexMap` uniquement.
- Le parallélisme est admis **entre exécutions** (une campagne est massivement parallélisable, §3.2), jamais **à l'intérieur** d'une exécution.

### PD2 — La sûreté et la vivacité ne se confondent jamais

Source : §3.2. Le traité écrit : « Un cahier des charges qui mêle S1 et L1 sans les nommer produit des exigences dont la moitié est non testable. » Ce PRD applique la règle à lui-même : chaque exigence porte une étiquette.

| Étiquette | Nature | Ce qu'une exécution finie en dit |
|---|---|---|
| **[S]** | Sûreté | Réfutable par une trace finie ; un moniteur lève l'alerte à l'instant de la violation |
| **[L]** | Vivacité | Non réfutable par aucune exécution finie ; ne s'énonce **jamais** sans sa condition (détecteur de défaillance ou borne Δ) |
| **[M]** | Mesure | Ni sûreté ni vivacité : une grandeur à estimer, avec son unité, son percentile et son intervalle |
| **[C]** | Capacité / couverture | Ni sûreté ni vivacité : une propriété du **modèle** — ce qu'il sait produire, injecter ou refuser. Vérifiable à la construction ou au chargement, jamais réfutable par une trace d'exécution |
| **[U]** | Interface | Exigence d'interaction ou de présentation |

La cinquième étiquette `[C]` n'est pas dans le traité : c'est une décision de conception de ce document, tranchée en DT12. Sans elle, six exigences au moins portaient `[S]` sans être réfutables par aucune trace, ce qui viole PD2 par la lettre même de PD2.

### PD3 — La console est en Θ(1) par rapport à n

Source : §6.3. « Un tableau de bord qui affiche une ligne par agent est donc en Θ(n) d'attention ; à n = 12 500 ce n'est plus une console, c'est un journal d'exécution. » L'interface présente des **grandeurs de population** et n'ouvre l'individu que sur enquête explicite.

Le §4.3 donne à ce principe une seconde source, empruntée à l'auto-assemblage de mille robots et à la validation micro/macro jusqu'à 600 robots : écrire l'algorithme **pour la dispersion de la population** plutôt que pour un membre nominal, et vérifier le comportement collectif sur un modèle agrégé plutôt qu'en simulant chaque agent. PD3 en est la conséquence d'interface ; PD5 en est la conséquence de mesure.

### PD4 — La console écrit dans le journal, jamais aux agents

Source : §6.3. Toute action de l'utilisateur qui modifie le comportement de l'essaim en cours d'exécution est écrite comme **enregistrement de directive** sur un sujet de commande compacté, avec une époque strictement croissante. Aucun chemin de commande hors bande. Conséquence assumée et pédagogiquement précieuse : **le curseur de l'utilisateur subit le même retard que le travail ordinaire**, et l'interface le montre.

### PD5 — L'émergence exige un paramètre d'ordre

Source : §1.2. « Une affirmation d'émergence sans paramètre d'ordre ni seuil n'est pas réfutable, et l'ouvrage l'écrit "comportement collectif". » Tout scénario qui prétend montrer une émergence expose une fonctionnelle Φ(C) tracée en fonction d'un paramètre de contrôle, et identifie son seuil. Les autres scénarios disent « comportement collectif ».

**Réserve de fourniture.** Le paramètre d'ordre Φ, son paramètre de contrôle η, son seuil η_c et l'exposant β ≈ 0,45 appartiennent au modèle de Vicsek **avec bruit** (§1.2, p. 12, 3ᵉ éd.). L'algorithme 1 du ch. 1, sous bruit nul, ne les fournit pas (EX-A02). Aucun mécanisme du périmètre actuel ne les fournit ; le trou est nommé au §13 et n'est pas comblé par commodité.

**Le premier fournisseur, et son statut exact** *(nouveau en 3.0)*. Le §8.1 constate que la conformité d'une population satisfait les exigences que le §1.2 impose à toute affirmation d'émergence, et lui donne donc son paramètre d'ordre au lieu de la décrire : **Φ_c**, la probabilité que deux agents tirés au hasard produisent la même valeur sur une décision donnée, moins la valeur qu'aurait cette probabilité si les décisions étaient indépendantes de même loi marginale. Paramètre de contrôle : la **diversité effective** de la population. C'est le premier couple (Φ, paramètre de contrôle) que le périmètre puisse fournir, et PD5 cesse d'être un principe sans fournisseur — à trois réserves qui s'affichent avec la grandeur, jamais après :

1. **Φ_c est une proposition de l'ouvrage, pas une mesure de sa source.** Le traité l'écrit lui-même ; aucune campagne ne l'a estimée. Elle porte donc l'étiquette de provenance des grandeurs dérivées, non celle des chiffres du traité (F2).
2. **Il n'y a pas de seuil.** Le §8.1 dit n'en avoir aucune mesure et juger probable qu'il n'y en ait pas un seul. PD5 exige d'identifier le seuil d'une transition ; ici l'exigence n'est pas satisfaite, et l'interface affiche « seuil inconnu » plutôt qu'une couleur, une zone ou un mot. Un scénario qui parlerait de transition de phase sur Φ_c serait refusé en revue.
3. **Φ_c ne remplace pas Φ de Vicsek.** Les deux mesurent l'alignement d'une population, et ce sont deux grandeurs différentes : Φ porte sur l'**état** des agents et vient d'un mécanisme d'alignement, Φ_c porte sur leur **décision** et vient d'une absence de variance. Les mêler serait fabriquer la transition de phase que le périmètre ne fournit toujours pas.

### PD6 — Le simulateur est une spécification de l'environnement

Source : §3.3, p. 50, 3ᵉ éd. « Les fautes qu'il sait produire sont exactement les fautes que la campagne pourra trouver. » Le modèle de faute est donc un objet de première classe, versionné, documenté, et affiché à l'utilisateur — pas un paramètre enfoui. Un mécanisme absent du modèle a, dans tout résultat, **une probabilité de faute nulle**, ce qui est un mensonge silencieux (mode (b) de l'algorithme 2, §3.2).

**Deux entrées obligatoires au hors-modèle depuis la deuxième édition.** PD6 impose de déclarer l'absent au même rang que le présent, et le ch. 8 nomme deux régimes que le modèle de faute ne couvre pas. **(a) L'adversité endogène** (§8.3) : des agents qui ne s'arrêtent pas, ne se taisent pas, n'émettent aucune valeur arbitraire, et dont l'effet est pourtant byzantin. Le modèle P la manque par construction, et `ModeleFaute::hors_modele()` doit l'écrire — EX-C20. **(b) La décision corrélée** : jusqu'en 3.0, la seule corrélation du modèle est celle des **fautes**, par domaines nommés (EX-C14) ; une population dont les décisions sont corrélées est absente du modèle, donc de probabilité nulle dans tout résultat livré. C'est la formulation exacte de la réserve du §0, et c'est EX-C19 qui la lève.

**Extension imposée par le doublement — le détecteur fait partie du modèle de faute.** Cinq mécanismes du traité reposent sur un détecteur de défaillance : la sonde périodique (§4.3, §7.3), le sondage indirect de style infectieux (§4.3, §7.3), le temporisateur d'exclusion de l'ensemble synchronisé (§2.1, §6.1 : `replica.lag.time.max.ms` = 30 000 ms), le délai de session du groupe de consommation (§6.1 : 45 000 ms), et la détection implicite du best-of-n (§5.1). Un détecteur ne prouve pas la mort ; il la soupçonne, et son taux de fausses suspicions est **une fonction croissante de la charge** (§7.3, p. 112, 3ᵉ éd.). Ses paramètres — période, expiration, seuil, taille du sous-groupe de sondage — sont donc affichés au même titre que le taux d'omission. Un détecteur enfoui rend la moitié des modes de défaillance du traité inexplicables. Ce que PD12 ajoute est distinct : PD6 range le détecteur dans le modèle de faute et impose l'affichage de ses réglages ; PD12 dit ce qu'un détecteur a le droit d'affirmer.

### PD7 — L'échelle ponytail s'applique à l'implantation, et les exemplaires se comptent dans le traité

Aucune abstraction spéculative. Un trait à une seule implantation est un défaut. Le moteur d'événements est un `BinaryHeap` de la bibliothèque standard, pas un ordonnanceur générique. La régression de C(n) est un moindres carrés écrit à la main (~50 lignes), pas une dépendance d'optimisation. Toute simplification délibérée porte un commentaire `// ponytail:` nommant son plafond et son chemin de mise à niveau.

**Amendement — la règle du comptage.** La tension entre PD7 et RQ3 d'une part, et le doublement du volume d'autre part, se tranche ici et pas plus tard. Une factorisation est spéculative quand elle anticipe un mécanisme **imaginé**. Elle ne l'est pas quand le traité en fournit déjà les exemplaires écrits. Le compte se fait dans le texte source, avant d'écrire une ligne :

- **moins de trois exemplaires dans le traité** → écrire en dur, autant de fois qu'il le faut ;
- **trois exemplaires ou plus** → factoriser, et nommer les exemplaires dans le commentaire du module.

Deux objets seulement franchissent le seuil au jour de rédaction : le **détecteur de défaillance** (cinq exemplaires, PD6) et le **bail à époque** (quatre : §4.3 algo 3 lignes 7–10, §6.1 ensemble synchronisé, §7.2 confinement, §7.3 capacité inter-plans). Aucun autre. Une factorisation qui n'exhibe pas son compte est refusée en revue.

### PD8 — Expliquer est une exigence, pas une légende

Le traité s'impose une signature à chaque mécanisme :

> chaque chapitre expose ses mécanismes avec leur modèle de panne, leur hypothèse de synchronisme, leur coût en messages et en tours, leur condition d'arrêt et leur mode de défaillance (p. 4, 3ᵉ éd.)

Le produit s'impose la signature symétrique. **Aucun scénario ne s'ouvre sans son bloc de trois**, affiché, non repliable, et jamais généré automatiquement :

1. **La thèse** — une phrase, citée du traité, avec sa section et sa page.
2. **Le mécanisme visible** — quel réglage produit quel effet observable, et par quel chemin. Pas « le système se dégrade » : *le réglage X franchit le seuil Y, ce qui provoque Z*.
3. **Ce qu'il ne démontre pas** — la négation explicite, au même rang typographique que la thèse.

Un scénario dont le bloc 3 est vide est un scénario refusé. C'est ce qui distingue un simulateur d'une démonstration commerciale.

### PD9 — La couverture croît par thèses, jamais par mécanismes

Source : §3.3, algorithme 3, étape 7 : « L'espace de recherche étant effectivement infini, exécuter davantage de tests couvre davantage de code et trouve davantage de défauts, sans qu'aucun critère de complétude existe » (§3.3, p. 54, 3ᵉ éd.). La transposition au produit : ajouter des scénarios couvre davantage de traité, sans qu'aucun critère de complétude existe. Le produit s'arrête donc sur un **budget**, pas sur une complétude — plafond de treize scénarios (§2.4), six phases (§9), un budget chiffré et deux coupes déclarées par phase. Aucune interface, aucun document, ne suggère jamais que la couverture du traité est « complète ».

**Ce que la deuxième édition ajoute à PD9, et qui n'est pas confortable.** Le §3.3 du traité gagne une conséquence que le produit doit porter : les résultats d'une campagne sur une population d'agents s'**inversent** d'une génération de modèle à l'autre, et l'aptitude à sortir d'un conflit n'est pas monotone en capacité générale. Une campagne de validation d'essaim est donc liée à une version de modèle comme une mesure de latence est liée à une version de courtier — périssable, à revalider. Le traité en tire la phrase qui borne l'ambition de tout ce document : *ce que l'on sait valider avant déploiement, ce sont les mécanismes du milieu ; ce que l'on ne sait pas valider, c'est la population* (§3.3, p. 56, 3ᵉ éd.). Le produit valide des mécanismes de milieu. Il ne valide aucune population, et le scénario M ne doit jamais laisser croire l'inverse.

### PD10 — Un test local ne certifie jamais une propriété globale

Source : §3.1 (algorithme 1 du ch. 3, étape 4 et mode (d) ; agrégation épidémique sous partition ; politique stochastique sans condition d'arrêt locale), §4.1 (algorithme 1 du ch. 4 ; scission silencieuse), §4.2 (algorithme 2, arrêt local ; quiescence). Le traité écrit sept fois le même motif sous sept mécanismes distincts : un agent évalue un prédicat sur ce qu'il perçoit et en tire une conclusion sur l'essaim entier.

Conséquence dure : tout prédicat évalué sur la perception d'un seul agent porte, dans le code comme à l'écran, l'étiquette **local**, son contre-exemple nommé, et le réglage qui le met en défaut. Un prédicat local n'est jamais présenté comme un état de l'essaim.

| Prédicat local | Ce qu'il paraît dire | Ce qui le met en défaut | Source |
|---|---|---|---|
| écart aux voisins ≤ ε pendant R tours | « le consensus est atteint » | crash-arrêt : l'agent mort cesse de publier, ses voisins lisent un état figé, et l'étape 4 confond mort et convergence | §3.1, mode (d) |
| variation de x < seuil sur w cycles | « la moyenne est stabilisée » | un sous-ensemble mal échantillonné n'a pas encore contribué | §4.1 |
| idem, en push-sum | « c'est la moyenne globale » | partition réseau : chaque composante converge vers **sa** moyenne locale, et l'arrêt se déclenche des deux côtés | §3.1 |
| vue stable sur w cycles | « la topologie est formée » | scission silencieuse : chaque moitié croit être l'essaim entier | §4.1 |
| cpt ≥ K | « la rumeur est diffusée » | la probabilité résiduelle de rester susceptible tend vers une constante fixée par K, pas vers 0 | §4.2 |
| aucune écriture depuis d | « les répliques ont convergé » | la quiescence est une propriété globale ; aucun agent ne la vérifie localement | §4.2 |
| *(aucun)* — politique stochastique par taux | « l'allocation est atteinte » | il n'existe **aucune** condition d'arrêt locale : la politique tourne indéfiniment pendant que la population se stabilise en distribution, sans qu'aucun agent n'observe cette stabilisation | §3.1 |

PD10 ne dit pas que ces prédicats sont inutiles : ce sont les seuls dont un agent dispose. Il dit que leur nom dans l'interface est **« critère local (heuristique) »**, jamais « convergé », et que le simulateur doit livrer, pour chacun, le réglage qui le prend en défaut. La dernière ligne est le cas limite : quand il n'existe aucun critère local, le simulateur n'en fabrique pas (EX-A38).

### PD11 — Toute gouvernance distribuée s'énonce avec sa fenêtre de violation

Source : §5.3. La gouvernance n'est ni l'accord (ch. 4) ni l'allocation (§5.2) : elle ne produit rien, **elle interdit**. Le traité clôt le chapitre par un verdict qui contredit ce qu'il vient de construire : un invariant global ne peut être vérifié que là où toutes les demandes passent, et un point unique est une autorité centrale, avec son point de panne, son plafond de débit et sa latence de queue. *Il n'existe pas de troisième option.*

Conséquences dures pour le produit :

- Aucun levier de gouvernance distribuée n'est présenté comme un invariant. Chacun affiche **la durée pendant laquelle l'invariant qu'il protège peut être faux** (EX-V21).
- Un levier dont la fenêtre est non bornée l'affiche comme non bornée, et non comme « grande » — même règle que le « non borné » du §5.1.
- Le simulateur admet une autorité d'admission centrale, mais **jamais comme membre de l'essaim** : elle est instanciée séparément, son coût est compté à part, et sa présence est affichée (cohérent avec EX-A12 et avec le coordonnateur du scénario F).
- Un scénario qui prétend maintenir un invariant dur — unicité d'un attributaire, plafond de dépense, exclusion mutuelle — sans payer le prix du ch. 4 doit inscrire sa fenêtre dans son critère d'acceptation, sans quoi il est refusé en revue.

### PD12 — Un détecteur de défaillance est un mécanisme, jamais un fait

Source : §6.1, §7.3. « Un détecteur ne prouve pas la mort d'un agent : il la soupçonne, à partir d'indices temporels, et il est caractérisé par sa complétude et son exactitude. » Chandra et Toueg autorisent l'imperfection — le consensus reste soluble avec un détecteur commettant une infinité d'erreurs, et ◇W est le plus faible qui le résolve — **ils n'autorisent pas à l'ignorer**. Conséquences dures :

- Tout détecteur du simulateur est déclaré avec sa **complétude** (borne sur le délai de détection d'un agent réellement arrêté) et son **exactitude** (production de fausses suspicions). Un détecteur sans ces deux champs ne se construit pas.
- L'état d'un agent aux yeux d'un autre est **sain / suspect / retiré**, jamais « mort ». « Mort » n'est pas une observation, c'est une action.
- Le taux de fausses suspicions n'est **jamais un paramètre**. Il est calculé à partir de la latence de réponse courante et du seuil, donc fonction croissante de la charge — c'est l'énoncé du §7.3, et un paramètre le rendrait invérifiable.
- **Toute hypothèse plus forte que « Δ finie mais inconnue » est nommée à l'endroit où elle est prise.** Le §6.1 en fait sa règle d'ouverture : c'est cette hypothèse « qui casse en premier sous charge ». Le simulateur tient un registre de ces hypothèses (EX-C12) et l'interface l'affiche.

### PD13 — La variance d'une population est un composant, jamais une hypothèse

*Nouveau en 3.0.* Source : §1.1 de la deuxième édition, quatrième convention. Le traité écrit la règle et elle vaut pour tout l'ouvrage :

> le vecteur de paramètres qui distingue δᵢ de δ n'est pas un raffinement de notation, c'est la seule source de variance de la population, et un essaim qui ne l'instancie pas n'a pas n agents mais un agent exécuté n fois. (§1.1, p. 8, 3ᵉ éd.)

La transposition en robotique était gratuite : deux robots diffèrent par leur position, leur usure et le bruit de leurs capteurs, et cette différence est **fournie par le monde** sans que personne ait à la produire. En logiciel, elle ne l'est pas. Le simulateur en tire trois conséquences dures.

- **L'aléa d'exploration est un composant à fabriquer, et il porte son coût.** La ligne que le ch. 1 ajoute à sa table de transposition l'écrit ainsi : « Cassé — l'aléa d'exploration cesse d'être gratuit et devient un composant à fabriquer ». Le produit ne le reçoit donc pas de la nature du modèle ; il le déclare (EX-C19).
- **Une population décorrélée est un réglage, pas un défaut du monde.** Les agents du simulateur tirent aujourd'hui chacun leur aléa du même `Alea` semé, ce qui est l'hypothèse **la plus favorable** et la seule que le produit sache produire. Elle doit être affichée comme un réglage à sa valeur extrême, jamais comme la nature des choses — même geste que RQ10 pour l'échantillonneur de pairs, et pour la même raison.
- **Toute borne probabiliste porte désormais quatre hypothèses, pas trois.** EX-A42 en nommait trois ; la décorrélation effective de la population est la quatrième, et NF-14 s'y applique sans aménagement : à Φ_c mesuré non nul, la borne est **effacée**, y compris quand la mesure est meilleure qu'elle.

### PD14 — Une trace est un témoignage, et le milieu ne l'évalue pas

*Nouveau en 3.0.* Source : §1.2 et §8.2. La stigmergie repose sur une prémisse que ni Grassé, ni Theraulaz et Bonabeau, ni Heylighen n'ont eu à énoncer parce qu'elle est physiquement garantie : la trace est le résidu de l'action, donc elle ne peut pas la démentir. Un enregistrement de journal est un **compte rendu**. M1 à M4 garantissent l'ordre, la durabilité et la non-réécriture ; ils ne garantissent **rien du contenu**, et l'identité de l'auteur y est déclarative.

Conséquences dures, et elles sont étroites — c'est ce qui les rend applicables :

- **Le vocabulaire change avant les mécanismes.** Là où le produit écrit « trace », il écrit « témoignage » dès que le contenu de l'enregistrement est une assertion de son auteur sur ce qu'il a fait. Le §1.2 le formule exactement : rien de ce que la section démontre ne tombe — le calcul de φ reste idempotent et reste une fonction de l'intervalle lu —, mais **φ agrège désormais des déclarations, et l'ordre qu'il induit est celui des déclarations, non celui des utilités**. Le scénario B affiche cette phrase et ne change pas d'algorithme.
- **L'identité est apposée par le milieu ou elle n'est pas une identité** (EX-M24). Un identifiant d'auteur lu dans la charge utile n'établit rien, et toute la reconstruction causale du §6.2 en dépend : *la traçabilité distribuée répond à la question de savoir ce qui s'est passé, jamais à celle de savoir qui l'a fait, sauf si l'identité est portée par un mécanisme que l'agent ne peut pas écrire lui-même* (§6.2, p. 96, 3ᵉ éd.). Une trace ainsi construite n'est pas incomplète, elle est **fausse**, et EX-A08 ne le voit pas.
- **Un historique de fiabilité ne se construit que sur des issues vérifiables** (EX-M25). Le traité pose la condition d'échec et elle est sévère : là où l'issue n'est pas vérifiable — la plupart des jugements de conception —, l'historique n'enregistre que la concordance avec la majorité, donc il **récompense la conformité** et aggrave le mal qu'il devait corriger. Le produit refuse la pondération dans ce cas plutôt que de la livrer dégradée.
- **Ce que la transposition depuis la stigmergie biologique conserve ici est nul, et cela s'écrit.** Aucune des trois institutions du §8.2 — identité, réputation, dépôt aveugle — n'a d'analogue chez les termites. Le milieu logiciel doit **fabriquer** ce que le milieu physique donnait, exactement comme pour la sérialisation, la localité et l'évaporation au ch. 1. La confiance en est le quatrième poste, et le traité écrit qu'il est le plus cher.

---

## 5. Architecture

### 5.1 Vue d'ensemble

**La ligne de coupe est le niveau de la boucle, pas le thème.** Un découpage thématique — `sim-consensus`, `sim-gouvernance`, `sim-securite` — produirait des crates à un ou deux mécanismes, toutes dépendantes des trois mêmes couches inférieures : c'est exactement le cadriciel que RQ3 interdit. Le découpage retenu reste à quatre crates après doublement du volume, en chaîne linéaire sans cycle :

```
sim-core  ◄──── sim-milieu  ◄──── sim-agents  ◄──── sim-viz
moteur DES      journal M1–M4     mécanismes          rendu egui,
horloge logique réplication ISR   oracles             tracés,
RNG semé        rétention         paramètres d'ordre  onglet « Limites »
modèle de faute compactage        scénarios (données)
détecteur       plan de contrôle       ▲
                                       └── binaire `campagne` (sans dépendance graphique)
```

`A ◄── B` se lit : B dépend de A.

| Crate | Responsabilité | Ne fait pas |
|---|---|---|
| `sim-core` | Boucle à événements discrets, horloge logique, RNG semé, injection de fautes, **détecteur de défaillance paramétré**, registre des hypothèses fortes, oracles, journal d'exécution | Ne connaît ni le journal partitionné, ni les agents |
| `sim-milieu` | Le milieu : journal partitionné M1–M4, réplication ISR(k, m), rétention, compactage, latences paramétrables, groupe de consommation et rééquilibrage, **plan de contrôle (époques, baux, quorums) facturé séparément** | Ne connaît aucun algorithme d'agent ; n'implante aucun protocole d'accord |
| `sim-agents` | Algorithmes du traité (ch. 1 : §1.1–§1.3 ; ch. 2 : §2.2–§2.3 ; ch. 3 : §3.1 ; ch. 4 : §4.1–§4.3 ; ch. 5 : §5.1–§5.3 ; ch. 6 : §6.2–§6.3 ; ch. 7 : §7.1–§7.3), oracles de propriétés, paramètres d'ordre, **définition des scénarios : paramètres, plages, critères d'acceptation**, **glossaire et reformulations en langue courante** — de la donnée, comme les scénarios | Ne dessine rien |
| `sim-viz` | Interface egui/eframe, tracés, onglets « Limites » et « Repères », échelle typographique, schémas figés du mécanisme | **Ne contient aucune logique de simulation, aucune définition de scénario, ni aucun texte du traité.** Le parcours « le fil » (O6) et l'export CSV **ne sont pas livrés** |

Trois responsabilités se déplacent par rapport à la version 1.0, sans qu'aucune crate ne s'ajoute :

**(a) Le détecteur de défaillance monte dans `sim-core`.** PD6 le range dans le modèle de faute : une fausse suspicion est une faute injectée, pas un comportement d'agent. Un seul objet paramétré — `Detecteur { periode, expiration, seuil, sondage_indirect: u8, suspicion: bool }` — que `sim-milieu` instancie pour l'exclusion de l'ensemble synchronisé et le délai de session, et que `sim-agents` instancie pour le sondage indirect, pour la reconfiguration sur soupçon (§4.3) et pour l'auto-guérison (§7.3). Cinq exemplaires étaient comptés, et PD7 était réputé satisfait. **La mesure dit autre chose** : `sim-milieu` n'instancie aucun détecteur — il tient `delai_session` et le seuil de retard en propre — et le sondage indirect est un **second** objet, `sim-agents::soupcon::DetecteurInfectieux`, avec ses propres compteurs. Un seul consommateur subsiste (`pair_a_pair`). DT6 est donc posée et non tenue, et l'écart est au [registre des décisions](decisions.md).

**(b) Le plan de contrôle reste dans `sim-milieu`, mais facturé à part.** Le traité est catégorique sur les deux points. Sur le lieu : « Une reconfiguration sûre sans aucun accord exige que le milieu arbitre : il doit détenir l'époque et refuser les écritures périmées » (§4.3, p. 68, 3ᵉ éd.). Sur la facture : « Le plan de données évite l'accord ; le plan de contrôle le paie pour tout le monde » (§4.2, p. 65, 3ᵉ éd.). Conséquence d'implantation **visée** : `sim-milieu::controle` détient les époques, les baux et le quorum, expose ses propres compteurs de messages, de tours et de fenêtre d'indisponibilité, et l'interface ne les additionne jamais à ceux du plan de données. Aucune cinquième crate : la mettre ailleurs créerait un cycle (`sim-agents` acquiert un bail ; `sim-milieu` compare les époques).

**Ce qui a été réalisé est l'inverse sur le lieu.** `sim-milieu::controle` ne détient que le quorum et son modèle de coût ; le seul endroit où `sim-milieu` écrit « époque » est sa propre liste `hors_perimetre()`, pour déclarer qu'il n'en compare aucune, et `struct Bail` vit dans `sim-agents::soupcon`. La séparation des factures, elle, est tenue : les deux jeux de compteurs sont dans des structures disjointes qu'aucun code n'additionne. Le cycle redouté ne s'est pas produit parce que le milieu n'arbitre pas — ce qui est aussi la raison pour laquelle DT9 « activé par défaut » n'existe pas.

**(c) Les scénarios descendent de `sim-viz` vers `sim-agents`.** Un scénario est une configuration, des plages de paramètres et un critère d'acceptation, c'est-à-dire un oracle — de la logique de simulation, pas du rendu. La version 1.0 les logeait dans `sim-viz` tout en exigeant de `sim-viz` qu'il « ne contienne aucune logique de simulation » (contradiction interne) et qu'il produise un mode `--headless` « sans dépendance graphique » alors qu'il lie `eframe` (contradiction technique). Le déplacement supprime les deux : le binaire `campagne` dépend de `sim-agents` seul.

**(d) Le chapitre 8 n'ouvre aucune crate et n'en déplace aucune** *(nouveau en 3.0)*. Ses mécanismes se rangent sans reste dans la chaîne existante, et le tableau ci-dessous fixe le rangement avant d'écrire une ligne, parce que c'est le moment où la tentation d'un `sim-conformite` se présente.

| Mécanisme du ch. 8 | Crate | Pourquoi là et pas ailleurs |
|---|---|---|
| Familles de décision, tirage partagé (EX-C19) | `sim-core` | C'est une propriété de l'**aléa** et de l'ordonnancement, comme les domaines de panne d'EX-C14 qu'elle décalque. La mettre dans `sim-agents` obligerait chaque mécanisme à savoir qu'il est corrélé |
| Adversité endogène au hors-modèle (EX-C20) | `sim-core` | `ModeleFaute::hors_modele()` y vit déjà |
| Identité apposée (EX-M24) | `sim-milieu` | Le courtier écrit le champ à la réception. C'est une garantie du milieu, du même rang que M1–M4, et aucun agent ne doit pouvoir l'atteindre |
| Historique vérifié par identité (EX-M25) | `sim-milieu` | Projection du journal sur un sujet compacté — le mécanisme d'EX-M10, appliqué à un autre objet. Aucun composant nouveau |
| Quota et prix croissant par ressource (EX-M26) | `sim-milieu` | Un compteur par clé et un refus d'écriture : c'est une politique du milieu, et c'est précisément ce qui lui permet de border une population **sans son consentement** (§8.1) |
| Φ_c, conformité empirique (EX-A56) | `sim-agents` | Paramètre d'ordre : même rang que φ et que les bornes d'EX-A11c |
| Dépôt aveugle, algorithme 8.1 (EX-A57) | `sim-agents` | Protocole d'agent sur un sujet ; le milieu n'y fait qu'ordonner, ce qu'il fait déjà |
| Dettes d'indépendance (EX-A58) | `sim-agents` | Extension d'EX-A42, au même endroit |
| Demandes d'arbitrage (EX-A59) | `sim-agents` produit, `sim-viz` consomme | Symétrique exact de la directive d'EX-A07 : l'essaim écrit vers l'opérateur au lieu de lire depuis lui |
| Journal des actions d'agent à agent, séparation des droits | **aucune** | Hors monde clos : le simulateur n'a ni système d'exploitation, ni identité de session, ni droits. Écarté avec sa raison en A.1, et T3 en porte la conséquence |

**Règle d'ouverture d'une cinquième crate.** Un module ne devient une crate que s'il satisfait les **deux** conditions : plus d'une crate consommatrice, **et** une dépendance que les autres ne doivent pas hériter. Aucun candidat ne les satisfait aujourd'hui. La règle est réévaluée une fois, à la sortie de la phase 3, sur le graphe de dépendances réel. **Réévaluée de nouveau à la révision 3.0**, la source ayant changé et non le produit : le ch. 8 n'introduit aucune dépendance — ses mécanismes sont un compteur par clé, une projection compactée, une statistique de paires et une contrainte d'ordre de lecture —, et sa consommation reste la chaîne unique. **Aucune cinquième crate**, et la règle est reconduite telle quelle.

### 5.2 Justification de la stack

**Rust bout en bout**, pour quatre raisons dont trois sont dérivées du traité :

1. **La campagne se mesure en secondes simulées par seconde-cœur** (§3.3), pas en nombre d'exécutions. Une exécution native sans ramasse-miettes maximise cette grandeur.
2. **La pause de ramasse-miettes apparaît deux fois dans le traité, et jamais comme une faute de son modèle de simulation** : en §2.1 comme cause de retrait d'une réplique de l'ensemble synchronisé (« pause de ramasse-miettes, disque lent, gigue réseau »), et en §3.2, mode (b) de l'algorithme 2, comme exemple de mécanisme **absent** du modèle, donc de probabilité de faute nulle dans tout résultat. Le produit la fait entrer dans son modèle et l'affiche comme telle (PD6) ; simuler une pause GC depuis un runtime qui en subit une lui-même serait une confusion de niveaux, et Rust l'évite par construction.
3. **Le déterminisme strict est facile à tenir** sans runtime, sans ordonnanceur caché, sans finalisation non déterministe.
4. **WASM donne la diffusion web gratuitement**, à partir du même code que le binaire natif — condition de O5.

**Dépendances retenues** (et pourquoi chacune passe l'échelle ponytail) :

| Crate | Usage | Alternative écartée |
|---|---|---|
| `rand_chacha` + `rand_core` | RNG reproductible, portable natif/WASM | Aucune : `ChaCha8Rng` est la garantie de reproductibilité inter-plateformes |
| `serde` + `serde_json` | Sérialisation des configurations et des points de reprise | — |
| `eframe` / `egui` / `egui_plot` | Interface immédiate, natif + WASM sans code séparé | Une SPA web séparée : deux bases de code, deux vérités |
| `std::collections::BTreeMap` | Itération ordonnée | `HashMap` : ordre non déterministe, viole PD1 |
| `web-time` | Temps mural d'EX-V07 en WASM | `std::time::Instant` : **panique** à l'appel sur `wasm32-unknown-unknown` |
| `libm` | Transcendantes portables — `log`, `exp`, `pow`, `sin`, `cos`, `atan2`, `fma` | Les méthodes de `f64` : mesurées divergentes entre natif et WASM (banc DT1), ce qui viole NF-02. Une implantation maison : c'est exactement ce que `libm` est, et l'écrire nous-mêmes serait le contraire de PD7 |

Écarté explicitement : tout moteur ECS (`bevy`, `hecs`) — le nombre d'agents simulés n'est pas dans le régime où un ECS gagne, et le coût est un ordonnanceur qu'on ne contrôle plus. Toute crate d'optimisation numérique — la régression USL est un moindres carrés à deux paramètres.

**Ni `clap` ni `csv` ne sont tirés**, contrairement à ce que ce tableau retenait : les arguments de `campagne` se comptent sur une main et se lisent par `std::env::args()`, et le CSV produit n'a aucun champ à échapper. `indexmap` n'est jamais déclarée non plus — elle n'entre qu'en transitif d'egui.

Deux lignes ont été ajoutées depuis la version 2.0 : `libm`, qui vient de NF-02 et non d'un mécanisme, et `web-time`, imposée par la mesure lors de l'empaquetage WASM. Le critère de dérive ci-dessous n'est donc pas déclenché — mais la règle est que l'ajout se justifie par écrit, et c'est fait ici.

**Critère de dérive.** Le doublement du volume de mécanismes n'ajoute **aucune** dépendance : les mécanismes supplémentaires sont de l'arithmétique, des compteurs, des files et des tirages. Si la liste ci-dessus s'allonge, ce n'est pas le volume qui l'exige — c'est le produit qui dérive vers le cadriciel de RQ3. La liste est donc un indicateur de risque, pas seulement une nomenclature.

### 5.3 Modèle de domaine

```rust
// sim-core — l'événement est daté en temps logique, jamais en temps mural
struct Event { at: LogicalTime, seq: u64, target: ActorId, payload: Payload }

// sim-core — le détecteur soupçonne, il ne prouve pas (§4.3, §7.3)
struct Detecteur { periode: LogicalDuration, expiration: LogicalDuration,
                   seuil: u8, sondage_indirect: u8, suspicion: bool }

// sim-milieu — la trace est un enregistrement, le milieu est la partition.
// `producer` est APPOSÉ par le courtier à la réception (EX-M24, §8.2) : il ne
// se lit jamais dans `value`, et aucun agent ne peut l'écrire. C'est ce qui
// sépare un témoignage attribuable d'un témoignage anonyme — le milieu
// n'évalue toujours pas le contenu, il garantit seulement qui l'a déposé.
struct Record { offset: u64, key: Key, value: Vec<u8>, event_time: LogicalTime,
                producer: ProducerId, seq: u64, causal_parents: Vec<RecordRef> }

// sim-milieu::controle — le milieu arbitre : il détient l'époque (§4.3, p. 68, 3ᵉ éd.)
struct Bail { portee: Portee, epoque: u64, echeance: LogicalTime, quorum: u8 }

// sim-core — la variance d'une population est un composant (PD13, EX-C19).
// Deux agents d'une même famille tirent le MÊME aléa de décision au même
// instant logique : c'est le décalque d'EX-C14, sur la décision au lieu de
// la panne. Φ_c est dérivé de cette structure, jamais saisi.
struct FamilleDecision { nom: &'static str, membres: BTreeSet<ActorId> }

// L'agent est un quintuplet, conformément à §1.1 : Aᵢ = (Sᵢ, sᵢ⁰, Pᵢ, δᵢ, Xᵢ)
// La perception se factorise par un intervalle borné du milieu — c'est la
// définition même de l'essaim, et le simulateur la fait respecter (voir EX-A12).
```

`Bail` est l'objet factorisé du second exemplaire compté par PD7 : quatre usages écrits dans le traité — reconfiguration sur soupçon (§4.3), appartenance à l'ensemble synchronisé (§6.1), confinement de sécurité (§7.2), capacité inter-plans (§7.3). Les quatre partagent la même mécanique — époque monotone, échéance, renouvellement, expiration — et le même mode de défaillance silencieux : si la dérive d'horloge dépasse ε, « le détenteur croit son bail vivant alors que le quorum l'a réattribué, et l'invariant est violé sans qu'aucun agent ne l'observe » (§7.2, p. 110, 3ᵉ éd.). Ce mode est un oracle, pas une note.

Correspondance terme à terme, imposée par §1.2 et non négociable dans l'implantation :

| Stigmergie biologique | Objet du simulateur |
|---|---|
| Trace | `Record` — en ajout seul, durable |
| Milieu | `Partition` — ordre total à l'intérieur (M1), aucun entre partitions (M2) |
| Voisinage | Intervalle `[offset_validé, fin_courante)` |
| Évaporation | Facteur γ < 1 appliqué par le lecteur, **ou** politique de rétention du courtier |
| Gradient | **Absent.** Il n'existe aucune métrique entre deux clés. Le simulateur ne doit pas en fabriquer une par commodité. |
| Véracité de la trace | **Absente** *(ligne ajoutée en 3.0, §8.2)*. Une phéromone est le résidu d'un passage : elle ne peut pas être déposée par un insecte qui n'est pas passé, et sa quantité **est** l'action, non son compte rendu. Un `Record` est un compte rendu. Le milieu n'a aucun mécanisme de crédit, et le simulateur ne doit pas en fabriquer un par commodité — il fournit l'attribution (EX-M24) et, sous condition d'issue vérifiable, la réputation (EX-M25). Ni l'une ni l'autre n'est la véracité. |
| Variance entre individus | **Fabriquée** *(ligne ajoutée en 3.0, §1.1)*. En robotique, elle est donnée par le monde — position, usure, bruit de capteur. Ici, elle est le vecteur de paramètres qui distingue δᵢ de δ, et une population qui ne l'instancie pas n'a pas n agents mais un agent exécuté n fois (PD13, EX-C19). |

---

## 6. Exigences fonctionnelles

### 6.1 `sim-core` — moteur déterministe

| # | Exigence | Étiq. | Source |
|---|---|---|---|
| EX-C01 | La boucle extrait de la file l'événement de date minimale, avance l'horloge logique à cette date **sans attente réelle**, exécute le gestionnaire, insère les événements produits | [S] | §3.3, algo 3 étape 4 |
| EX-C02 | Deux exécutions de même graine et même configuration produisent des traces **identiques**, ordre d'entrelacement compris | [S] | §3.3, algo 3 étape 6 |
| EX-C03 | Les égalités de date sont départagées par un compteur de séquence monotone, jamais par l'ordre d'insertion dans un conteneur non ordonné | [S] | PD1 |
| EX-C04 | La granularité de l'horloge logique (1 µs ou 1 ms) est un **paramètre du modèle**, affiché, car elle décide de ce qui compte comme simultané | [C] | §3.3, p. 53, 3ᵉ éd. |
| EX-C05 | Le modèle de faute couvre : crash-arrêt et redémarrage de machine, de baie et de centre ; omission et retard de message ; partition réseau ; corruption des écritures non synchronisées au redémarrage ; dates d'événements randomisées. La partition réseau est modélisée comme un **processus à deux états**, faute de quoi elle n'est jamais tirée | [C] | §3.3, algo 3 (liste des fautes) ; §3.2, algo 2 (processus à deux états) |
| EX-C06 | La distribution des fautes est **réglable et affichée** ; l'interface avertit qu'un taux de fautes excessif réduit l'exploration au lieu de l'augmenter | [U] | §3.3 : « éviter de pousser le système dans un espace d'états restreint par un taux de fautes excessif » |
| EX-C07 | Des points d'injection de haut niveau permettent de faire échouer une opération d'ordinaire réussie, retarder une opération d'ordinaire rapide, choisir une valeur inhabituelle de paramètre | [C] | §3.3 |
| EX-C08 | Des compteurs de couverture conditionnelle mesurent combien d'exécutions distinctes ont atteint une condition donnée, et signalent celles à compte nul ou faible | [M] | §3.3 |
| EX-C09 | Sur violation d'oracle, l'exécution s'arrête (étape 5) ; la graine et la configuration complète, journalisées dès l'étape 1, suffisent au rejeu à l'identique, entrelacement compris (étape 6) | [S] | §3.3, algo 3 étapes 1, 5 et 6 |
| EX-C10a | La campagne s'arrête sur budget en secondes-cœur | [S] | §3.3, algo 3 étape 7 |
| EX-C10b | **Aucun critère de complétude n'est affiché ni suggéré**, l'espace de recherche étant effectivement infini | [U] | §3.3, algo 3 étape 7 |
| EX-C11 | Un oracle est déclaré comme sûreté ou comme vivacité bornée. Un oracle de vivacité **non bornée** est refusé à la compilation ou au chargement, avec un message citant §3.2 | [S] | §3.2, mode (d) |
| EX-C12 | **Registre des hypothèses fortes.** Tout temporisateur à borne connue est déclaré avec sa valeur, sa source documentaire et **l'affirmation qu'il encode** (ex. : `replica.lag.time.max.ms = 30 000 ms` encode « un suiveur sain rattrape le meneur en moins de 30 s » ; `timeoutSeconds = 1 s` encode « un agent sain répond en moins d'une seconde »). Le registre est affiché ; chaque entrée porte un compteur du nombre de fois où l'affirmation a été **fausse** dans l'exécution en cours | [S] | §6.1 : hypothèse « nommée là où elle est prise, parce que c'est elle qui casse en premier sous charge » |
| EX-C13 | **Horloges locales à dérive.** Chaque agent possède une horloge locale dont le facteur de dérive est tiré de la graine, borné par un ε_vrai de configuration. Ce ε_vrai est **distinct** de l'ε supposé par les mécanismes de bail (EX-A33). L'horloge reste logique : PD1 tient, la dérive est déterministe et rejouable | [S] | §7.2, §7.3 : « une borne ε sur la dérive relative des horloges […] seule hypothèse forte » |
| EX-C14 | **Domaines de panne partagés.** La corrélation des fautes s'injecte par domaine nommé — même image, même lien, même plan de contrôle — et non par un scalaire global. Un agent appartient à zéro ou plusieurs domaines ; une faute de domaine frappe tous ses membres au même instant logique. Le coefficient ρ affiché est **dérivé** de la structure des domaines, jamais saisi ; les scénarios pilotent la structure, pas ρ | [S] | §7.2 : « des détecteurs identiques appliqués à des entrées corrélées commettent des erreurs corrélées » ; §7.3 ; raccord §8.3 |
| EX-C15 | **Service et file par agent.** Chaque agent possède une file FIFO bornée et un temps de service paramétrable. Sa latence de réponse est une **sortie** du modèle, pas une entrée ; elle croît avec son arriéré. C'est la condition d'existence de la cascade du §6.1 : sans elle, la saturation est scriptée au lieu d'être produite | [M] | §6.1, figure 6.1 ; §7.3 ; voir §8.3 |
| EX-C16 | Le graphe de communication est un **objet du modèle** : orienté et asymétrique par défaut, à voisinage variable d'un tour à l'autre. Le retrait d'arêtes est **corrélé** — la saturation d'un courtier supprime d'un coup tous les liens qui le traversent. La connexité conjointe est vérifiée *a posteriori* sur une fenêtre glissante et rapportée comme constat d'exécution, **jamais** comme hypothèse satisfaite par construction | [S] | §5.1 |
| EX-C17 | La population est variable **en cours d'exécution** : création et destruction d'agents sont des événements datés du même moteur, soumis au même ordonnancement déterministe. Le coût unitaire d'un agent est un paramètre du modèle (défaut : 327 mots, soit 2 616 octets en 64 bits, dont 233 mots de tas, pile comprise), et le plancher mémoire de la population est affiché | [S] | §2.2 |
| EX-C18 | Une campagne de vérification qui épuise son budget sans violation affiche « aucune violation observée en N exécutions », et une vérification qui **ne termine pas** dans son budget est rapportée comme **absence de verdict** — jamais comme absence de problème | [U] | §5.3 |
| EX-C19 | **Familles de décision.** *(Phase 6.)* La corrélation des **décisions** s'injecte par famille nommée — même règle, même paramétrage, même contexte de lecture —, et non par un scalaire global, exactement comme EX-C14 procède pour les fautes. Un agent appartient à **exactement une** famille ; deux agents d'une même famille consomment le **même tirage** pour une même décision **au même tour de leur boucle** — *amendée par la réalisation, voir DT13 : le partage porte sur le rang de la décision, jamais sur la date, les cycles d'agents étant décalés d'un tirage dans la période* —, ce qui est la transposition littérale de « deux agents portant le même modèle, la même invite et le même contexte ne diffèrent par rien ». Le partitionnement par défaut est **une famille par agent** — la population décorrélée, hypothèse la plus favorable, affichée comme un réglage à sa valeur extrême et jamais comme la nature du modèle (PD13). Φ_c affiché est **dérivé** de la structure des familles et de la mesure des décisions déposées, jamais saisi ; les scénarios pilotent la structure, pas Φ_c. Le déterminisme n'en souffre pas : le tirage partagé descend du même `Alea` semé, et deux exécutions de même graine restent identiques (EX-C02) | [S] | §8.1 ; §1.1 (quatrième convention) ; décalque d'EX-C14 |
| EX-C20 | **L'adversité endogène est déclarée hors modèle.** `ModeleFaute::hors_modele()` porte le régime du §8.3 dans son libellé propre : des agents qui ne s'arrêtent pas, ne se taisent pas, n'émettent aucune valeur arbitraire, et dont l'effet est byzantin, sans qu'aucun ait été programmé pour nuire. La déclaration nomme aussi ce qui la distingue de DT8 — l'agent menteur est **injecté**, ce régime-ci est **produit** — et pourquoi le seuil f < n/3 n'y a pas de sens : le nombre d'agents adverses n'y est pas borné par l'hypothèse, il vaut n. Sans cette entrée, le régime a dans tout résultat une probabilité nulle, ce qui est le mensonge silencieux de PD6 | [C] | §8.3 ; PD6 |

### 6.2 `sim-milieu` — le journal partitionné

| # | Exigence | Étiq. | Source |
|---|---|---|---|
| EX-M01 | **M1** : l'ordre est total à l'intérieur d'une partition | [S] | §1.2 |
| EX-M02 | **M2** : aucun ordre n'est garanti entre partitions. Le simulateur **randomise activement** l'entrelacement inter-partitions perçu, afin qu'un agent qui suppose un ordre soit pris en défaut | [S] pour M2 ; [C] pour la randomisation | §1.2 pour M2 ; **décision du produit**, dérivée de M2 et non énoncée par le traité, pour la randomisation active de l'entrelacement |
| EX-M03 | **M3** : un enregistrement validé est durable ; l'accusé de durabilité est un événement distinct de l'écriture, séparé par une latence tirée d'une distribution | [S] | §1.2 |
| EX-M04 | **M4** : le compactage ne réordonne jamais, il ne fait que supprimer | [S] | §1.2 |
| EX-M05 | La réplication implante ISR(k, m) : k répliques assignées, m seuil d'accusé ; une écriture n'est validée que lorsque toutes les répliques de l'ensemble synchronisé l'ont reçue ; le meneur est élu parmi les membres de l'ensemble | [S] | §2.1 |
| EX-M06 | **R1** — tout enregistrement accusé **au producteur** est présent chez tout meneur ultérieur de la partition — est un oracle activable. Sa violation est un résultat attendu du scénario D, pas un défaut du simulateur | [S] | §2.1 |
| EX-M07 | Le retrait d'une réplique pour retard (pause GC, disque lent, gigue réseau) est modélisé **séparément** de la panne : il n'incrémente pas le compteur de pannes | [S] | §2.1, déroulé t₁ |
| EX-M08 | L'élection d'un non-membre de l'ensemble synchronisé est une option de configuration, avec ses deux conséquences simulées : troncature des journaux des suiveurs, destruction de l'enregistrement chez ses détenteurs. Leur survenue est constatée par l'oracle R1 (EX-M06, [S]) | [C] | §2.1 |
| EX-M09 | La latence du chemin écriture-durabilité-lecture est tirée d'une distribution paramétrable, et ℓ₉₉ en est extrait et affiché — **jamais la moyenne seule** | [M] | §2.3, §6.2 |
| EX-M10 | La rétention et le compactage par clé sont implantés ; un sujet compacté est marqué comme **impropre à la traçabilité**. Sa garantie — un consommateur partant du début du journal voit **au moins** l'état final de tous les enregistrements dans leur ordre d'écriture — est un oracle, et le mot « au moins » interdit d'en revendiquer l'unicité | [S] | §6.2, §6.1 tableau 17 |
| EX-M11 | Le surcoût de format est modélisé : 60 octets pour un message seul (contre 34 dans l'ancien format), 753 octets pour un lot de 100 (contre 3 400), soit ≈ 7 octets marginaux par message additionnel en lot | [C] | §1.3, §2.1, §7.1 |
| EX-M12 | La livraison idempotente du producteur (identifiant de producteur + numéros de séquence monotones par partition) est optionnelle et sa portée est affichée : **à l'intérieur d'une session et d'une partition** | [S] | §1.3, §7.1 |
| EX-M13 | Le milieu expose son propre coût : nombre d'écritures, d'octets lus, de tours de journal, distinctement du compte de messages point à point | [M] | §1.1, convention de comptage |
| EX-M14 | **L'appartenance à l'ISR est décidée par un temporisateur, pas par un accord.** Le retrait pour retard d'EX-M07 est déclenché par une borne connue (`replica.lag.time.max.ms`, 30 000 ms par défaut) appliquée au décalage de fin de journal du suiveur. Cette borne est inscrite au registre EX-C12 comme hypothèse **plus forte que le synchronisme partiel**, et la charge la rend fausse : sous saturation, l'exclusion frappe des suiveurs vivants | [S] | §6.1 |
| EX-M15 | **R2 est un invariant distinct de R1, et la perte de R1 est muette.** La borne de visibilité n'avance qu'après réplication à tout l'ISR ; un enregistrement n'est lisible qu'ensuite. Avec `min.insync.replicas = 1`, l'ISR peut se réduire au seul meneur pendant que les producteurs reçoivent toujours leurs accusés : la tolérance passe de f à 0 **sans qu'aucune erreur ne soit émise**. Le simulateur affiche donc en permanence, côte à côte et sans jamais les additionner, **\|ISR\| courant**, **m** et la **largeur d'accusé** du dernier enregistrement validé. Deux tolérances en découlent, chacune avec sa provenance : un enregistrement accusé à largeur w survit à **w − 1** disparitions (§2.1) ; R1 tient tant qu'un réplica de l'ISR survit, soit **\|ISR\| − 1** (§6.1). La marge d'accusé **\|ISR\| − m** — nombre de retraits que la partition supporte avant de cesser d'accuser — est une **grandeur dérivée du produit**, étiquetée comme telle : le traité ne l'écrit pas | [S] | §6.1 ; §2.1 pour w − 1 |
| EX-M16 | **Coût d'écriture d'un lot.** Le chemin en six étapes (envoi, ajout local, réponse aux k−1 requêtes de récupération en attente, requêtes suivantes portant le décalage de fin de journal, avancée de la borne de visibilité, accusé) coûte **2k messages par lot et 2 tours en série**. Le compteur affiche le coût **par enregistrement** : 0,012 message à b = 500 et k = 3. Le levier du lot est visible ou le compte n'a pas de sens | [M] | §6.1 |
| EX-M17 | **Trois protocoles de rééquilibrage commutables**, sur un groupe de n membres : barrière unique (JoinGroup/SyncGroup — **4n messages**, deux aller-retours par membre, révocation de toutes les tâches en cours à chaque changement d'appartenance) ; coopératif incrémental à deux rééquilibrages consécutifs, le premier révoquant les seules partitions qui changent de main (**8n messages**, quatre aller-retours) ; attribution côté courtier par battement de cœur, convergente membre par membre (**Θ(1) message par membre et par intervalle**, aucune barrière). Comptes de tours : voir annexe B.1. Pendant un rééquilibrage sous les deux premiers protocoles, **aucune partition n'est servie**. Le choix est un paramètre de scénario, pas une constante | [S] | §6.1, §2.2, §5.2 |
| EX-M18 | **Le nombre de rééquilibrages n'a pas de borne, et le simulateur n'en affiche aucune.** La condition d'arrêt est l'atteinte d'une génération stable ; elle n'est pas garantie. Un membre qui manque son échéance à chaque génération en déclenche 1, 2, … sans terme. L'interface affiche le compte cumulé et **jamais une estimation de fin** | [L] | §6.1 |
| EX-M19 | **Parallélisme utile min(n, p), et le point où ajouter un agent retranche du débit.** La partition étant la seule unité de parallélisme du côté consommateur, au plus p agents travaillent ; les n − p autres sont inactifs, **participent à chaque rééquilibrage et comptent dans le coût de coordination**. Le simulateur les compte dans les messages et jamais dans le débit — c'est le terme σ du §2.1 qui grossit pendant que le numérateur reste plat. Il trace en outre le point où ajouter un agent **retranche** du débit : la forme est empruntée à l'interférence de fourragement observée en robotique, la cause dans l'essaim logiciel n'est jamais une collision mais la contention sur le milieu (scénario C) et le coût de coordination du rééquilibrage. L'interface nomme la cause mesurée et le remède qui en découle — augmenter p ou refondre la clé (EX-A45) —, jamais « étaler dans l'espace ». L'élasticité de l'essaim est une décision de création du sujet, pas une propriété de son autoscaleur | [S] | §6.1, §4.1, §2.2 ; raccord §2.1 |
| EX-M20 | **La fenêtre de rétention R est une grandeur unique, à trois rôles.** Évaporation par politique du milieu (§1.2, §6.1), horizon de reconstruction causale (§6.2, EX-A08), **horizon réel de la détection** (§7.2). Elle est affichée une fois, et tout oracle dont l'horizon dépasse R est refusé au chargement avec le message : *au-delà de R, la propriété redevient invérifiable ; R, non la sensibilité du détecteur, est l'horizon réel de la détection* | [S] | §6.1, §7.2 |
| EX-M21 | **Plan de contrôle : modèle de coût du quorum de métadonnées.** k = 2f+1, appartenance et attribution des meneurs, **simulé par son prix et non par son protocole** (DT7). La condition `broadcastTime ≪ electionTimeout ≪ MTBF` est vérifiée en continu et sa **violation de gauche est provocable** : temps de diffusion tiré dans 0,5 – 20 ms selon la technologie de stockage, délai d'élection tiré uniformément dans un intervalle fixe (150 – 300 ms par défaut). Le mode de défaillance nommé est **élections perpétuelles** — panne née de la charge, manifestée comme panne d'accord. Les compteurs de ce plan ne sont jamais additionnés à ceux du plan de données | [S] | §6.1, tableau 17 ; §4.2 pour le coût |
| EX-M22 | **Coût d'un changement de population**, compté et affiché ligne à ligne selon le tableau 5 : création et destruction d'un agent **sans état**, 0 message sur le milieu, 0 tour, débit inchangé ; entrée dans un groupe, Θ(n) messages ; sortie planifiée d'un agent porteur, Θ(n) + 1 validation de décalage + 1 point de reprise ; sortie non planifiée, Θ(n) **après expiration du délai de session**. L'unité de tour est celle de l'annexe B.1 ; le compte de **phases** de rééquilibrage — 2 en protocole d'origine, 4 en coopératif — est affiché séparément et jamais dans la même colonne | [M] | §2.2, tableau 5 |
| EX-M23 | Deux oracles distincts et jamais confondus : **[S]** à tout instant, chaque partition est affectée à au plus un membre du groupe ; **[L]** toute partition finit par avoir un propriétaire, énoncé uniquement avec sa condition — l'expiration du délai de session, qui est le détecteur. Entre l'arrêt d'un porteur et cette expiration, le débit des partitions orphelines est nul, et cette durée est mesurée et affichée | [S] + [L] | §2.2, tableau 5 |
| EX-M24 | **Identité apposée par le courtier.** *(Phase 6.)* Le champ `producer` d'un enregistrement est écrit par le milieu à la réception, à partir de l'identité authentifiée de la session, et **jamais lu dans la charge utile**. Un producteur qui tente d'écrire un identifiant d'auteur dans `value` voit son enregistrement accepté et son champ ignoré — le milieu n'évalue pas le contenu (PD14), il apporte seulement l'attribution. Coût, à afficher : **0 message, 0 tour**, quelques octets par enregistrement, et une contrainte sur le format. Ce qu'elle achète : EX-A08 retrouve son attribution, et aucun agent ne peut déposer sous le nom d'un autre. **Condition d'échec, à afficher au même rang** : une identité partagée entre plusieurs processus, ou un jeton réémis à un successeur, ramène exactement au zombie du §2.1 — le point de défaillance résiduel n'est pas le processus, c'est l'identité. Un préréglage « identité partagée » la provoque (NF-10) | [S] | §8.2, tableau 22 |
| EX-M25 | **Historique vérifié par identité.** *(Phase 6.)* Projection du journal sur un sujet compacté — le mécanisme d'EX-M10 appliqué à un autre objet, aucun composant nouveau : pour chaque identité, la suite de ses assertions et, **quand elle existe**, l'issue vérifiée de chacune. Coût : 1 écriture par vérification, 1 lecture compactée par consultation. Ce qu'il achète : un poids par source, donc une pondération de φ par la fiabilité constatée plutôt que par la seule quantité déposée. **Deux refus, non négociables.** (1) Le simulateur refuse au chargement toute pondération de φ par un historique dont les issues ne sont pas déclarées vérifiables : là où elles ne le sont pas, l'historique n'enregistre que la concordance avec la majorité, donc il récompense la conformité du §8.1 et **aggrave le mal qu'il devait corriger** — le message de refus cite cette phrase. (2) Un historique n'est jamais affiché comme une mesure de véracité : il mesure une **concordance constatée entre une assertion et une issue**, et la distinction est celle de PD14 | [S] | §8.2, tableau 22 |
| EX-M26 | **Quota et prix croissant par ressource.** *(Phase 6.)* Un compteur par clé dans le milieu, et trois politiques commutables : quota dur par ressource, prix croissant avec le nombre de preneurs, refus d'écriture au-delà d'un seuil de concentration. Coût : **0 message**, un compteur par clé. C'est le seul levier structurel du §8.1 contre la conformité, et sa propriété distinctive est affichée avec lui : les leviers de gouvernance du §5.3 bornent un agent **qui accepte de l'être** et s'appliquent dans le processus même dont on suppose qu'il agit contre le système ; celui-ci borne une **ressource**, ce qui ne demande le consentement de personne. Ce qu'il ne traite pas, affiché aussi : une population qui converge sur une ressource **non médiée par le milieu** | [S] | §8.1 ; §5.3 retourné ; tableau 22 |

**Registres d'états distribués (tableau 17) — ce que le milieu implante et ce qu'il écarte.**

| Famille | Statut dans le produit | Raison |
|---|---|---|
| Sujet compacté (clé → dernière valeur) | **Implanté**, EX-M10 | Déjà au périmètre ; le tableau 17 ajoute sa signature : k = f+1, borne connue 30 s, 2k messages / 2 tours, défaillance = doublons de clés en queue non compactée. |
| Quorum de métadonnées (Raft) | **Modèle de coût**, EX-M21 | Nécessaire : c'est lui qui porte le meneur par partition, donc le coordonnateur du plan du milieu (EX-V17). Simulé par son prix, jamais implanté comme protocole (DT7). |
| CvRDT fondé sur l'état | **Déjà transposé**, EX-A06 / scénario G, et EX-A21 | L'esquisse HyperLogLog fusionnable du §7.1 **est** un treillis à jonction monotone : la fusion registre à registre par maximum est idempotente, commutative, associative. Le produit implante donc cette famille là où elle gagne sa place, sans second modèle de milieu. Son mode de défaillance propre — pierres tombales non ramassables — ne s'applique pas à l'esquisse, qui ne supprime rien. |
| CmRDT fondé sur les opérations | **Modélisé côté agent seulement**, EX-A21 | Le milieu n'offre pas de livraison causale entre partitions — c'est M2. La famille « opérations » est donc exposée comme mécanisme d'agent avec son **contrat de transport exigé**, et la configuration qui prétend le satisfaire sur le milieu inter-partitions est refusée au chargement. Écart consigné en annexe A.1. |

### 6.3 `sim-agents` — les mécanismes du traité

Chaque mécanisme implante l'algorithme du traité **tel qu'écrit**, avec sa signature complète : modèle de panne, hypothèse de synchronisme, hypothèses sur le milieu, condition d'arrêt, modes de défaillance.

**Note de lecture.** Le §4.1 ouvre sur un piège que la structure de ce tableau évite : trois problèmes distincts portent le même nom dans la littérature d'essaim, et les confondre coûte cher parce qu'ils n'ont ni le même modèle de faute, ni le même coût, ni la même condition d'arrêt. Le premier produit un **scalaire** (EX-A13 à EX-A16), le deuxième un **graphe** (EX-A17, EX-A18), le troisième une **partition du travail** (EX-A45, EX-M19). Aucune exigence de ce PRD ne couvre deux des trois.

| # | Mécanisme | Étiq. | Source | Priorité |
|---|---|---|---|---|
| EX-A01 | **Algorithme 2 (ch. 1)** — renforcement stigmergique borné sur journal : lecture d'intervalle, calcul de φ par décroissance γ sur les événements, écrêtage \[φ_min, φ_max\], tirage α/β, action, écriture, accusé, validation de décalage | [C] | §1.2 | P0 |
| EX-A02 | **Algorithme 1 (ch. 1)** — alignement par règle de plus proche voisin (Jadbabaie–Lin–Morse), sous les hypothèses exactes du traité : synchrone, **bruit nul**, famille finie de graphes de voisinage, voisinage connu au tour courant. Sert l'accord de fait sans protocole d'accord, et son mode de défaillance : sur perte de connexité conjointe, la population se scinde en composantes convergeant chacune vers sa propre limite, sans qu'aucun agent ne puisse le détecter. **Ne fournit ni paramètre d'ordre ni transition de phase** : le traité écrit que le bruit nul retire précisément la transition de phase | [C] | §1.1 | P0 |
| EX-A03 | **Algorithme 3 (ch. 1)** — adhésion et routage dans un maillage adossé au journal : ANNONCE, construction de vue, hachage cohérent, RETRAIT, fenêtre de divergence | [C] | §1.3 | P1 |
| EX-A04 | Diffusion pair à pair adressée, avec entretien de la vue d'appartenance par sondage — le terme de comparaison du scénario A | [C] | §1.3 | P0 |
| EX-A05 | Mécanismes d'allocation, **six** : centralisé, Contract Net, glouton en ligne, enchère ε de Bertsekas, auto-affectation à d sondes, et **politique stochastique par taux (champ moyen)** — où l'allocation est reformulée en optimisation sur les taux d'entrée et de sortie qui définissent ensuite des politiques individuelles. Le sixième coûte **0 message et 0 tour**, c'est sa force, et n'a **aucune condition d'arrêt** : la distribution prescrite est atteinte en espérance, asymptotiquement. Fluctuation relative ≈ 1/√n, soit ≈ 6 % à 250 agents | [C] | §5.2 ; §7.3, §3.1 pour le sixième | P2 |
| EX-A06 | Agrégat fenêtré coopératif avec esquisses HyperLogLog fusionnables, filigrane, volets, manifeste | [C] | §7.1 | P3 |
| EX-A07 | Injection de directive globale avec époque (D1 sûreté, D2 vivacité conditionnelle) + sujet d'accusés | [C] | §6.3 | P1 |
| EX-A08 | Reconstruction causale hors ligne `ANCÊTRES(e, H)` avec drapeau de troncature | [C] | §6.2 | P2 |
| EX-A09 | Étranglement adaptatif et délestage par criticité (K = 2, fenêtre 120 s, ≤ 3 tentatives, plafond 10 %) | [C] | §2.3 | P3 |
| EX-A13 | **Algorithme 1 (ch. 3)** — itération de consensus linéaire sur digraphe : $x_i(k{+}1) = x_i(k) + \alpha \sum_j a_{ij}\,(x_j(k) - x_i(k))$, pas α avec 0 < α < 1/Δ(G), arrêt à ε sur R tours. Modèle de panne **vide**, synchronisme **parfait** — les deux affichés en permanence, parce qu'ils sont l'inverse de ceux du reste du produit. La convergence est garantie **sans borne de temps** : une vivacité au sens strict, affichée comme telle et jamais convertie en délai | [C] | §3.1 | P2 |
| EX-A14 | **Algorithme 1 (ch. 4)** — agrégation par échange par paires push-pull : fil actif, fil passif, époque e, relance tous les C cycles, expiration τ < T. **Aucune condition d'arrêt.** La fonction agrégée est un paramètre — moyenne par défaut, seule traitée par le traité ; comptage, somme, produit et extrema par la même mécanique. Hypothèse posée et affichée : un agent arrêté **ne revient pas** avec un état ancien pendant l'exécution du protocole — hypothèse que le §4.3 renverse, et le contraste est le sujet du scénario J | [C] | §4.1 | P1 |
| EX-A15 | Agrégation épidémique push-sum : couple valeur-poids, pair tiré dans un échantillon de d pairs, moitié émise et retranchée, addition à la réception, estimateur = rapport des deux, arrêt à ε sur R tours. L'accusé de réception est un commutateur : il restaure la conservation de la somme **à 2 messages par échange au lieu de 1**, et le surcoût est compté — c'est le prix de la symétrie que la relation producteur-consommateur ne donne pas | [C] | §3.1 | P1 |
| EX-A16 | Politique stochastique par taux : chaîne de Markov sur les états d'agent dont la distribution stationnaire est l'allocation visée. **Zéro message.** Le coût ne se compte ni en tours ni en messages mais en **temps de mélange** de la chaîne des taux, et l'unité affichée est celle-là. Posée **par partition**, jamais sur la population entière. Deux clauses affichées avec le résultat : aucune borne sur ℓ₉₉ de la reconfiguration individuelle, qui est précisément la mesure du service ; et la conservation de la population comme hypothèse structurante — un agent qui s'arrête emporte sa part sans qu'aucun taux ne la réémette. C'est le sixième mécanisme d'EX-A05, vu du côté du mécanisme | [C] | §3.1, §4.1, §7.3 | P3 |
| EX-A17 | Service d'échantillonnage de pairs, objet de première classe : rend un pair par appel, avec biais réglable (uniforme, déséquilibré, groupé par hôte, dégénéré). Aucun mécanisme n'accède à la liste des vivants autrement que par ce service | [C] | §4.1 | P1 |
| EX-A18 | Tri de vue par distance : vue de c descripteurs, échange par cycle, conservation des c minimisant une distance sur un attribut (version de code, zone de déploiement, spécialisation déclarée) | [C] | §4.1 | P3 |
| EX-A19 | **Algorithme 2 (ch. 4)** — rumeur push-pull avec retrait par compteur : état ∈ {susceptible, infectieux, retiré}, cpt incrémenté sur rencontre redondante, retrait à cpt ≥ K | [C] | §4.2 | P1 |
| EX-A20 | Anti-entropie : épidémie simple sans état retiré, réconciliation du contenu comparé, fréquence bridée par le coût de comparaison. Activable **en parallèle** de la rumeur, comme filet | [C] | §4.2 | P2 |
| EX-A21 | Répliques sans conflit, **deux familles séparées et non interchangeables**, chacune avec son hypothèse de canal : fondée sur l'état (treillis à jonction monotone ; convergence pourvu que le système transmette la charge utile une infinité de fois, par paires, sur des canaux point à point à livraison à terme ; Θ(n) octets par message, Θ(n²) par tour d'anti-entropie complet) ; fondée sur les opérations (opérations concurrentes commutatives ; diffusion fiable en ordre causal ; duplication éliminée par conservation de l'ensemble des messages déjà livrés ; Θ(1) par opération). Confondre les deux est fatal, et c'est un préréglage (EX-A52) | [C] | §4.2, §5.1 | P2 |
| EX-A22 | Consensus réduit à son coût et à sa fenêtre : Ω(n) messages par décision, terminaison bornée **après** stabilisation seulement, indisponibilité ≈ un délai d'élection après arrêt du meneur. La classe de détecteur est un paramètre, parce qu'elle décide de la tolérance : détecteur **fort** → un nombre quelconque de défaillances ; détecteur **fortement exact à terme** → majorité de corrects exigée, et prouvée nécessaire. Inclut la linéarisabilité (propriété locale et composable) et le cycle CAP : détecter l'entrée en partition, restreindre les opérations, exécuter une récupération de cohérence à la sortie. **Aucun protocole n'est implanté** (DT7) | [C] | §4.2 | P2 |
| EX-A23 | Détecteur d'appartenance de style infectieux : ping direct d'un membre tiré au hasard ; à défaut d'acquittement avant une expiration **plus courte que la période**, demande de sondage indirect à un sous-groupe de taille **s** tiré au hasard (noté k dans la source, renommé s ici, la lettre k étant réservée au facteur de réplication) ; propagation du verdict avec le trafic ordinaire ; extension par suspicion. Deux paramètres seulement — période de protocole, taille du sous-groupe — et horloges non synchronisées. Coûts : 2 messages et 1 tour en nominal ; **au plus 2 + 4s messages et 3 tours par cycle de suspicion**. Le détecteur expose ses deux propriétés formelles, complétude et exactitude ; le mode « battement de cœur » est disponible comme terme de comparaison, sa charge croissant quadratiquement avec la taille du groupe. Le sondage indirect distingue la perte d'un lien de la mort d'un agent **si et seulement si les s pairs ne partagent pas le lien fautif** — condition que le protocole ne vérifie pas et qu'EX-C14 rend fausse à volonté | [C] | §4.3, §7.3 | P1 |
| EX-A24 | **Algorithme 3 (ch. 4)** — reconfiguration d'allocation sur soupçon, avec époque : retrait de m de la vue, incrément d'époque, diffusion par EX-A19, recalcul local des plages, relecture du point de reprise au décalage validé, demande de bail ⟨p, ε⟩ au milieu, abandon si bail d'époque supérieure, effets estampillés ε. **Légende obligatoire du mécanisme** : un robot mort reste mort et reste sur place, un agent logiciel soupçonné mort peut revenir avec son état d'avant et écrire ; l'époque et le bail des lignes 7 à 10 n'ont aucun équivalent dans les protocoles robotiques dont ils descendent, et c'est l'écart entre arrêt franc et arrêt-reprise qui les impose | [C] | §4.3 | P1 |
| EX-A25 | **Boucle de commande d'élasticité**, un seul mécanisme pour ses deux écritures dans le traité. Forme algorithmique (§2.2, algorithme 2 du ch. 2) : zone morte \|r − 1\| ≤ τ, plafond n\* ← min(n\*, p), budget de churn ⌊β·T⌋ dans les deux sens, hystérésis de descente sur la fenêtre W, retrait ordonné (cesser de lire, valider le décalage, écrire le point de reprise, quitter le groupe), attente d'au plus T_a + R. Forme de plateforme (§4.3, §6.1, §7.3) : `visées = plafond[courantes × (métrique_courante / métrique_visée)]`, tolérance 0,1, période de synchronisation 15 s, délai de disponibilité initiale 30 s, période d'initialisation de la métrique processeur 5 min. Coût : Θ(n) lectures de métriques par période et 1 tour, la boucle bloquant sur la collecte avant de décider. Deux grandeurs affichées en permanence : le **rapport 5 min / 15 s = 20**, nombre de fois où le contrôleur réévalue la même erreur avant qu'une réplique fraîche contribue à la mesure ; et **τ, délai entre une correction et son effet mesurable**, mesuré par le simulateur et jamais saisi. La **fenêtre de stabilisation** est exposée **sans valeur par défaut documentée** : *provenance absente — la page qui documente le mécanisme ne publie pas ce défaut* (F1) | [C] | §2.2 ; §4.3, §6.1, §7.3 | P1 |
| EX-A26 | **Sondes et cycle de vie.** Cycle à **cinq états** — démarrage → prêt → en traitement → en vidange → arrêté — et **trois sondes aux effets disjoints et non substituables** : démarrage (bloque les deux autres jusqu'à son succès), vivacité (redémarre le conteneur), disponibilité (retire des points d'accès sans redémarrer). Défauts documentés exposés tels quels : `initialDelaySeconds 0`, `periodSeconds 10`, `timeoutSeconds 1`, `successThreshold 1`, `failureThreshold 3`. Coût : 1 aller-retour par agent et par période, soit 2 messages, et Θ(n) messages par période pour l'essaim. Le groupe de consommation est un **troisième détecteur à seuil fixe**, avec ses propres constantes : `session.timeout.ms` = 45 000 ms pour un agent mort soupçonné, `max.poll.interval.ms` = 300 000 ms pour un agent bloqué dans son traitement | [C] | §2.2, §6.1, §7.3 | P1 |
| EX-A27 | **Budget de perturbation** : plafond distinguant les perturbations **volontaires**, qui passent par l'interface d'éviction et que le budget peut refuser, des **involontaires** — panne matérielle, panique du noyau, partition réseau, éviction pour manque de ressources —, qui **comptent contre le budget sans pouvoir être empêchées**. La suppression directe d'un membre le contourne : c'est une action offerte par le simulateur, pas un oubli d'implantation. Le budget ne limite pas non plus les mises à jour progressives. Libellé affiché : *il empêche l'essaim de s'auto-mutiler, il n'empêche pas le monde de le mutiler* | [C] | §4.3, §6.1, §7.3, §5.3 | P2 |
| EX-A28 | **Algorithme 1 (ch. 5)** — DÉCISION-PAR-SEUIL (best-of-n) : opinion échantillonnée localement, diffusion pendant une durée τ·qᵢ proportionnelle à la qualité (renforcement modulé), règle de k-unanimité, détection de quorum à une fraction locale ≥ 1 − δ | [C] | §5.1 | P2 |
| EX-A29 | **Algorithme 2 (ch. 5)** — MOYENNE-LOCALE : moyenne du voisinage du tour, i compris ; arrêt local et non concerté sur \|Δxᵢ\| ≤ ε pendant T tours. **Réutilise le noyau de mise à jour d'EX-A02** ; ce qui change n'est pas la règle mais le statut de la sortie — un choix collectif, non un paramètre d'ordre — donc les oracles armés (EX-A51) | [C] | §5.1 | P2 |
| EX-A30 | **Leviers de gouvernance du tableau 16** — étend EX-A09 sans le refaire : EX-A09 fournit l'étranglement adaptatif et le délestage par criticité ; EX-A30 ajoute les quatre classes de criticité comme taxonomie explicite (CRITICAL_PLUS, CRITICAL, SHEDDABLE_PLUS, SHEDDABLE), le quota délibérément surengagé, le budget de reprise, le renvoi au budget de perturbation (EX-A27) et le dimensionnement automatique par mesure, plus la colonne « ce qu'il ne borne pas » pour chacun | [C] | §5.3 | P3 |
| EX-A31 | **Corroboration r parmi n** sur le journal des alarmes. Modèle : crash-arrêt et omission, partiellement synchrone avec Δ inconnue, **aucune horloge synchronisée, aucun agent menteur**. (1) L'agent qui lève une alarme écrit ⟨sujet, empreinte, temps-événement⟩ : **1 message, 0 tour**. (2) Un corroborateur lit la fenêtre W et compte les **émetteurs distincts** ayant signalé la même empreinte. (3) Il escalade dès que ce compte atteint r, et abandonne à l'expiration de W. Coût : **Θ(n) messages par fenêtre** dans le pire cas, **0 tour**, condition d'arrêt explicite et bornée par W | [C] | §7.2 | P2 |
| EX-A32 | **AGRÉGER-ÉPIDÉMIQUE** — moyenne par paires par époques de γ cycles. Hypothèses reprises entières : les nœuds tombent en panne et les liens échouent, les départs volontaires sont traités comme des crashs, **les fautes byzantines sont exclues**, les délais sont imprévisibles, les horloges locales dérivent faiblement à court terme. Cycles de durée δ — **une période moyenne, pas une échéance**. Le facteur de convergence est une option de configuration, avec ce dont il ne dépend pas affiché à côté : **ni la taille du réseau, ni le temps, ni la distribution initiale des valeurs**. *Distinct d'EX-A14* : les deux sont des moyennes par paires, mais le traité les écrit dans deux chapitres avec deux signatures — EX-A14 porte la relance et la ligne 4, EX-A32 porte le facteur de convergence et l'époque. L'implantation partage le noyau de fusion et rien d'autre | [C] | §7.2 | P2 |
| EX-A33 | **Bail de quorum — un mécanisme, deux emplois.** Le confinement de sécurité (§7.2) et la capacité transférable entre plans (§7.3) sont le même mécanisme, paramétré par la taille du quorum q : q ≥ 2 pour le jeton de confinement, q = 1 pour le prêt bilatéral entre un plan sur site et un plan infonuagique. Une seule implantation, conformément à PD7. Modèle : crash-arrêt et omission **plus une borne ε sur la dérive relative des horloges pendant la durée du bail** — la seule hypothèse forte du §7.2 comme du §7.3, inscrite au registre EX-C12. Étapes : (1) demander le bail à un quorum de taille q, **2q messages et 1 tour** ; (2) l'obtenir avec échéance D et agir ; (3) renouveler avant D − ε − Δ, chaque renouvellement coûtant à nouveau 2q messages et 1 tour ; (4) cesser dès qu'un renouvellement échoue ou que l'échéance corrigée est atteinte — **condition d'arrêt locale, donc terminante sans accord**. Coût par action Θ(q) messages et 2 tours ; **coût par observation nul** | [C] | §7.2, §7.3 | P2 |
| EX-A34 | **Classification des prédicats** — stable / instable, et l'horizon R | [C] | §7.2 | P2 |
| EX-A35 | **Échantillonnage de traces** — par enregistrement ou cohérent par trace | [C] | §7.2 | P3 |
| EX-A36 | **AUTO-GUÉRIR**, tel qu'écrit : dix lignes, signature complète — crash-arrêt et omission ; partiellement synchrone, Δ inconnue ; **détecteur incomplet ET inexact** ; budget de perturbation B tenu derrière un quorum de taille q, **lu au moment de l'action et non au moment du soupçon**. Coût d'un soupçon confirmé : **2 + 4s + 2q messages et 4 tours**, dont un seul — l'acquisition du budget — bloque sur un quorum. Condition d'arrêt : le succès de la sonde de démarrage. Le délai de refroidissement T_froid empêche la boucle de se réamorcer sur son propre effet | [C] | §7.3 | P2 |

**EX-A10 [C]** — Chaque mécanisme expose ses **modes de défaillance nommés** comme préréglages activables. Pour l'algorithme 2 du ch. 1, les quatre :

| Préréglage | Réglage qui le provoque | Ce que l'utilisateur observe |
|---|---|---|
| « Essaim aveugle » | T < ℓ₉₉ | La rétroaction disparaît ; l'exploration dégénère en tirage indépendant |
| « Trace optimiste / pessimiste » | Écriture avant / après l'action | Surestimation (dépôt sans effet) ou sous-estimation puis réattaque d'une ressource déjà traitée |
| « Rejeu » | Crash entre l'action et la validation de décalage | φ inchangé (idempotent par M1+M4), mais **effet dupliqué** si l'action ne l'est pas |
| « Incomparabilité M2 » | Ressources comparées placées sur deux partitions | En asynchrone, M2 ne fournit aucune relation et l'ordre relatif de φ est sans objet ; sous synchronisme partiel, il n'est fiable que si l'écart de φ excède la décroissance sur Δ + ℓ₉₉ |

**EX-A11a [C]** — Le verrouillage prématuré est provocable : γ = 1 supprime l'oubli, φ_max/φ_min non borné fait tendre la probabilité de tirage de la dominante vers 1.

**EX-A11b [S]** — Un oracle activable en permanence vérifie que la fraction d'effort mesurée hors ressource dominante ne descend jamais sous la borne calculée, et que la probabilité de tirage mesurée de toute ressource visible ne descend jamais sous le plancher calculé. Une violation est réfutable à l'instant où elle survient, et signale soit un défaut d'implantation, soit une erreur du traité.

**EX-A11c [M]** — L'interface affiche en permanence les deux bornes, avec leurs paramètres — le **plancher d'exploration** :

$$P_{\min} = \frac{1}{m}\left(\frac{\varphi_{\min}}{\varphi_{\max}}\right)^{\alpha}\left(\frac{\eta_{\min}}{\eta_{\max}}\right)^{\beta}$$

et la **fraction d'effort permanente hors ressource dominante** :

$$\frac{m-1}{m}\left(\frac{\varphi_{\min}}{\varphi_{\max}}\right)^{\alpha}\left(\frac{\eta_{\min}}{\eta_{\max}}\right)^{\beta}$$

avec la phrase du traité en légende : *un essaim stigmergique n'atteint pas l'optimum, il campe à distance bornée de lui, et cette distance est un réglage et non un défaut à corriger*.

**EX-A12 [S]** — Le simulateur **fait respecter la définition d'essaim** (§1.1) : la perception d'un agent se factorise par un voisinage de cardinal borné ou par un intervalle borné du milieu. Un agent dont la perception prendrait la configuration entière est rejeté à la construction, avec le message : *ce n'est pas un membre de l'essaim, c'est un coordonnateur*. Le scénario F, qui compare à l'allocation centralisée, instancie le coordonnateur **explicitement et séparément** ; le coordonnateur de groupe (T1) et l'autorité d'admission (PD11) suivent la même règle.

**EX-A37 [S]** — **La conservation de masse est un oracle, et sa rupture est un scénario.** L'invariant — la somme des estimations sur la population reste égale à la somme des mesures initiales — est vérifié en continu par le moteur, hors du monde perçu par les agents. Sa violation n'arrête pas l'exécution : elle est **datée et attribuée à sa ligne**. Les quatre modes de l'algorithme 1 (ch. 4) sont des préréglages :

| Préréglage | Réglage qui le provoque | Ce que l'utilisateur observe |
|---|---|---|
| « PULL perdu » | omission sur le chemin de retour, ligne 4 | j a moyenné (ligne 10), i non ; la somme quitte sa valeur initiale de \|x_i − x_j\|/2 sur cet échange ; tous les agents convergent quand même, et s'accordent sur une valeur qui n'est la moyenne de rien |
| « Crash en cours de protocole » | crash-arrêt d'un agent entre deux cycles | la masse détenue disparaît ; le protocole converge encore, vers une autre valeur |
| « Relance seule » | C fini, omission > 0 | l'erreur accumulée est **plafonnée** par la relance de la ligne 11, jamais corrigée : le tracé remonte à chaque relance et redérive aussitôt |
| « Époque en retard » | messages réordonnés autour d'une relance | ligne 5 contre ligne 6 : l'agent en retard se réinitialise, l'agent en avance ignore — deux traitements opposés du même désaccord d'époque |

La visualisation obligatoire est la figure 4.1 rendue exécutable : quatre vignettes (i échantillonne j — j fusionne — le PULL se perd — la somme a bougé), rejouables pas à pas sur un échange isolé, avec la somme courante et la somme initiale affichées côte à côte.

**EX-A38 [S]** — **Aucune condition d'arrêt n'est fabriquée.** Deux mécanismes du périmètre n'en ont pas, et le simulateur ne leur en ajoute pas :

- l'algorithme 1 (ch. 4) est proactif et ne se termine pas ; une règle de décision locale — nombre fixe de cycles depuis la dernière relance, ou variation sous seuil sur w cycles — est disponible, obligatoirement étiquetée **heuristique**, avec en légende la raison du traité : un agent ne peut pas distinguer une estimation stabilisée d'une estimation qui n'a pas encore vu la contribution d'un sous-ensemble mal échantillonné ;
- la politique stochastique par taux (EX-A16) n'a **aucune** condition d'arrêt locale, pas même heuristique : elle tourne indéfiniment pendant que la population se stabilise en distribution, sans qu'aucun agent n'observe cette stabilisation. L'interface affiche l'état de la distribution comme grandeur de population (PD3), jamais comme un état perçu par un agent.

**EX-A39 [S]** — **Chaque test local d'une propriété globale a son réglage de mise en défaut.** Les six premières lignes du tableau de PD10 sont des préréglages livrés, un par ligne ; NF-10 s'y applique. L'interface affiche, à côté de tout critère local satisfait, le nom du contre-exemple qui n'est pas exclu. La septième ligne (politique stochastique) n'a pas de préréglage parce qu'elle n'a pas de critère : c'est EX-A38 qui la couvre.

**EX-A40 [L]** — **La couverture de la rumeur est une vivacité probabiliste, et ne s'énonce pas sans sa condition.** Le simulateur n'affiche jamais « la rumeur a atteint tous les agents ». Il affiche la fraction mesurée d'agents infectieux ou retirés, et, en regard, la fraction résiduelle de susceptibles avec le K qui la fixe. La seule formulation admise pour une couverture certaine est conditionnelle : « sous anti-entropie active (EX-A20), couverture certaine à terme, sans borne de temps ».

**EX-A41 [S] [L]** — **Il n'y a pas de troisième voie, et l'interface n'en propose pas.** L'arbitrage d'époque par le milieu est un commutateur à deux positions, et deux seulement :

- **Le milieu arbitre** — il détient l'époque du bail et rejette les écritures d'époque inférieure. La ligne 10 de l'algorithme 3 est opérante.
- **Le milieu n'arbitre pas** — la sûreté repose alors entièrement sur l'exactitude du détecteur, hypothèse que le produit refuse (§2.3). La seule issue restante est de payer un quorum sur l'appartenance, et le simulateur la facture en Ω(n) messages par décision (EX-A22).

Toute configuration hors de ces deux positions est rejetée à la construction, avec le message : *le détecteur ne prouve pas la mort, il la soupçonne*.

**Ce que l'arbitrage d'époque établit, et ce qu'il n'établit pas.** L'algorithme 3 du §4.3 ne fait qu'une chose à sa ligne 10 : « si m réapparaît, ses écritures portent une époque < ε, le milieu les rejette ». C'est une propriété d'**écriture**, et le produit la nomme comme telle, distincte de S1 :

> **S1w** *(nomenclature du produit, non un énoncé du traité)* — aucune écriture estampillée d'une époque inférieure à celle du bail courant n'est acceptée par le milieu.

**S1 au sens du glossaire — « deux agents ne détiennent jamais simultanément l'attribution de la même partition » (§3.2, p. 45, 3ᵉ éd.) — n'est pas rétabli par l'arbitrage d'époque.** Entre l'instant du soupçon et l'instant où m constate son bail périmé, deux agents détiennent l'attribution : m se croit propriétaire, i l'est devenu. C'est exactement la fenêtre de divergence du scénario E, que le traité refuse de borner. Le simulateur affiche les deux grandeurs séparément — durée de double détention (non bornée en asynchrone) et compte d'écritures rejetées pour époque périmée — et **n'écrit jamais « S1 tient »** là où seule S1w tient.

**Seconde condition, non négociable** : sans idempotence du traitement, le rejeu depuis le décalage validé produit un double effet à chaque panne ; le commutateur d'idempotence existe, et le compteur de doubles effets est affiché quand il est désactivé. **[L]** — la condition d'arrêt de l'algorithme 3 — toute plage de l'anneau a un propriétaire dont le bail porte l'époque courante — est énoncée comme **vivacité conditionnelle** : après l'instant de stabilisation, sous arbitrage d'époque. Jamais nue.

**EX-A42 [M]** — **Quatre hypothèses nommées, quatre commutateurs, quatre bornes qui s'éteignent.** *(Trois jusqu'à la version 2.0 ; la quatrième vient du §8.1.)* Toute borne du périmètre repose sur au moins une de ces quatre hypothèses ; chacune est un réglage, et le violer **efface** la borne correspondante de l'affichage (NF-14) :

| Hypothèse | Ce qu'elle conditionne | Ce que le traité en dit |
|---|---|---|
| Tirage uniforme du service de pairs | Θ(log n) cycles pour l'agrégation, O(log n) tours pour la rumeur, connexité conjointe du graphe d'échange | les implantations donnent un flux localement uniforme, mais les hypothèses usuelles sur l'aléa **ne tiennent pas globalement** (§4.1) ; un graphe conjointement connexe en espérance peut être déconnecté dans la réalisation, et la preuve ne s'en aperçoit pas (§4.2) |
| Insensibilité à l'adresse | l'optimalité Θ(n log log n) de la rumeur push-pull | un agent qui choisit son pair d'après ce qu'il sait de lui sort du modèle, et la borne cesse de s'appliquer « dans un sens comme dans l'autre » (§4.2) |
| Indépendance des fautes | toutes les garanties probabilistes de la diffusion épidémique | deux agents sur le même hôte, issus du même déploiement, derrière la même dépendance, ne tombent pas indépendamment ; la corrélation invalide le calcul **sans invalider le code** (§4.2) |
| **Décorrélation effective de la population** *(nouvelle en 3.0)* | les **sept** énoncés du tableau 21 : plancher d'exploration, redondance de facteur k, décorrélation par gigue, champ moyen, vérification statistique, auto-affectation à deux sondes, corroboration r parmi n | la condition est habituellement gratuite, parce que deux robots ne partagent pas leur source d'aléa ; elle cesse de l'être dès que la fonction de transition est partagée. Alors « la fraction d'agents dans l'état j ne vaut plus une densité mais 0 ou 1, et la fluctuation relative en 1/√n que le modèle prédit est simplement fausse » (§3.1, p. 43, 3ᵉ éd.). Le traité conclut que la condition à écrire en tête de tout modèle de champ moyen est **double** — échangeabilité **et** décorrélation effective — et que **la seconde se mesure au lieu de se supposer** |

Le troisième cas est celui que le traité désigne comme le pire mode de rupture : le protocole continue de tourner, la borne cesse de tenir, aucun signal ne le dit. Le simulateur, lui, le dit — c'est le seul endroit où il en sait plus que l'essaim, et l'affichage le déclare comme tel (F2).

Le quatrième est le même mode de rupture avec une différence qui le rend pire : les trois premières hypothèses portent sur le **milieu ou le protocole**, et le produit sait les violer depuis la phase 3. La quatrième porte sur la **population**, et jusqu'à la phase 6 le produit ne sait pas la violer du tout — il tourne en permanence du côté favorable, sans commutateur pour en sortir. Une hypothèse qu'aucun réglage ne met en défaut n'est pas une hypothèse tenue : c'est une hypothèse invisible, et EX-A58 existe pour la rendre visible avant de la rendre réglable.

**EX-A43 [S]** — **Les quatre modes de défaillance de l'algorithme 1 (ch. 3) sont des préréglages**, sur le modèle d'EX-A10 :

| Préréglage | Mode | Réglage qui le provoque | Ce que l'utilisateur observe |
|---|---|---|---|
| « Pas trop grand » | (a) | α = 1/Δ(G) | n valeurs propres sur le bord du cercle unité ; l'itération cesse de converger. Le traité note que l'erreur est répétée dans la littérature antérieure — le préréglage la reproduit |
| « Digraphe non équilibré » | (b) | poids a_ij asymétriques | la moyenne initiale n'est plus invariante : la limite est pondérée par la **topologie**, non par les données. L'interface affiche ensemble la limite atteinte, la moyenne initiale, et l'enveloppe convexe des états initiaux dans laquelle la valeur de groupe reste **indéterminée** |
| « Retard » | (c) | τ ≥ π/(2·ν_n) en temps continu | non-convergence. La condition est **nécessaire et suffisante**, pas seulement suffisante, et l'interface trace le budget τ < π/(4Δ(G)) qui en découle |
| « Mort ou convergé » | (d) | crash-arrêt d'un voisin publiant | l'agent mort cesse de publier, ses voisins lisent un état figé, et l'étape 4 confond mort et convergence. Le crash-arrêt est **hors du modèle de panne** de cet algorithme, et l'interface le rappelle au moment où le préréglage est activé |

Un cinquième préréglage, **« Moyeu »**, ne correspond à aucun mode du traité : c'est la discussion de transposition, et il est étiqueté comme telle. Topologie de sujet lu par tous, Δ(G) = n − 1, budget de retard τ < π/(4(n−1)) décroissant en 1/n — moins de 7,9 × 10⁻³ unité de temps du protocole à n = 100. Le milieu offre gratuitement l'échange non local qui accélère la convergence, et du même geste la topologie que la source déconseille ; les deux effets sont tracés sur le même graphe.

Aucun scalaire monotone de progression n'est affiché pour ce mécanisme : le traité établit par programmation semi-définie qu'il n'existe pas de fonction de Lyapunov quadratique commune pour cette classe, donc rien ne mesure « la distance restant à parcourir ». L'exception est nommée et elle est double : sur digraphes équilibrés fortement connexes commutant arbitrairement, le carré de la norme du désaccord **est** une fonction de Lyapunov commune, et la vitesse est minorée par la plus petite connectivité algébrique rencontrée. **Là seulement** une barre de progression est permise, et elle porte cette minoration comme borne.

**EX-A44 [S]** — **Le déclencheur de reconfiguration est déclaré : charge offerte ou appartenance.** Les deux classes d'événements — variation de charge (ρ = λ/µ franchit un seuil) et panne partielle (agent arrêté, partition réseau) — appellent des réponses opposées : ajouter des agents dans un cas, réaffecter le travail du disparu sans ajouter personne dans l'autre, puisque le débit total n'a pas manqué, il a été redistribué. Le simulateur **permet la confusion** — répondre à une panne partielle par une montée en charge — et en compte le prix : les agents injectés dans un système en train de se réparer, et le rééquilibrage supplémentaire qu'ils provoquent, comme coût net.

**EX-A45 [S]** — **Les deux régimes de clé, et la partition chaude qu'ils décident.** Le regroupement des tâches est le troisième des trois problèmes du §4.1, et son unité n'est pas choisie par l'essaim mais par le producteur : dans le milieu événementiel, c'est la partition du sujet. Le simulateur expose les régimes et leurs conséquences opposées, jamais un seul :

| Régime de clé | Ce qu'il achète | Ce qu'il coûte |
|---|---|---|
| Hachage de la clé | répartition uniforme sur les p partitions | **détruit toute localité** : deux événements du même client tombent dans deux partitions distinctes et perdent leur ordre relatif — c'est M2, pas un défaut |
| Clé sémantique | conserve la localité, donc l'ordre relatif par client | **importe la dissymétrie du domaine** ; son mode de défaillance dominant est la **partition chaude** |
| Hachage cohérent | rend l'affectation stable : l'arrivée ou le départ d'un agent ne déplace qu'environ 1/n des clés au lieu de la totalité | atténue le coût du premier régime, ne le supprime pas ; conçu pour des réseaux où aucun serveur ne peut connaître l'état complet |

Deux préréglages, et le simulateur exige qu'un régime soit choisi explicitement — il n'y a pas de défaut silencieux :

| Préréglage | Réglage qui le provoque | Ce que l'utilisateur observe |
|---|---|---|
| « Localité détruite » | hachage de la clé, deux événements du même client | l'ordre relatif se rompt ; le compteur d'inversions par client est non nul, et l'interface l'attribue à M2 |
| « Partition chaude » | clé sémantique + distribution de clés dissymétrique | une partition sature ; le débit utile décroche du plafond min(n, p) **avant** ce plafond, et ajouter des agents n'y change rien |

Le remède affiché est celui du traité et lui seul — augmenter p ou refondre la clé — avec sa contrepartie : refondre la clé **change de régime**, donc remplace un mode de défaillance par l'autre. Aucun rééquilibrage automatique n'est offert qui prétendrait supprimer les deux.

**EX-A46 [S]** — Le contrôleur d'élasticité (EX-A25) **n'a autorité sur aucun invariant de sûreté**. Règle de conception préalable, vérifiée par test : arrêter le contrôleur au milieu d'un cycle gèle la population sans corrompre aucun oracle armé. Un contrôleur dont l'arrêt fait tomber un oracle de sûreté est un défaut bloquant, pas un réglage.

**EX-A47 [S]** — Les trois modes de défaillance du contrôleur sont des **préréglages activables**, sur le modèle d'EX-A10 :

| Préréglage | Réglage qui le provoque | Ce que l'utilisateur observe |
|---|---|---|
| « Oscillation » | W < 2·T_a, ou fenêtre de stabilisation nulle avec un temps mort supérieur à la période | Le contrôleur mesure l'effet d'une décision qu'il n'a pas fini d'appliquer, conclut à l'insuffisance et redouble ; la population diverge en dents de scie, **compteur de pannes à zéro** |
| « Tempête de rééquilibrages » | β·R ≳ 1 (période T du même ordre que R) | L'essaim passe son temps à se réorganiser ; le débit utile s'effondre pendant que le compte de tours de rééquilibrage croît |
| « Métrique trompeuse » | Pilotage sur l'occupation processeur au lieu du décalage | La métrique sature après le goulot réel ; le point fixe \|r − 1\| ≤ τ devient inatteignable et le contrôleur ajuste sur une grandeur qui ne répond plus |

L'interface n'affiche jamais « stabilisé » : elle affiche **le point fixe atteint** (\|r − 1\| ≤ τ) ou son absence. La boucle est perpétuelle ; sa condition d'arrêt n'est pas sa terminaison.

**EX-A48 [S]** — Au retrait d'un agent, **la disponibilité chute avant la vivacité**. Aux valeurs par défaut, un agent en vidange qui échoue à trois sondes de vivacité consécutives est tué en une trentaine de secondes en pleine validation de décalage. L'ordre inverse est provocable comme préréglage, et ce qu'il produit est mesuré : chaque retrait « propre » engendre au moins un redémarrage, et chaque redémarrage rouvre un rééquilibrage.

**EX-A49 [S]** — La loi de Little sert au **dimensionnement de la cible**, jamais au pilotage. Deux conséquences implantées : (a) la boucle du contrôleur (EX-A25) n'appelle jamais n = λW/c ; (b) le calculateur de cible est un outil séparé qui affiche ses trois hypothèses — moyennes finies, processus stochastiques strictement stationnaires, processus d'arrivée métriquement transitif de moyenne non nulle — et **étiquette son résultat comme non valide** lorsqu'il est calculé sur une mesure prise en régime transitoire ou saturé, avec la phrase du traité : *un nombre arithmétiquement exact et opérationnellement faux*.

**EX-A50 [S]** — Extension de F3 aux mécanismes du §5.1. Aucun d'eux n'affiche de verdict global :

| Mécanisme | Ce que l'interface affiche | Ce qu'elle n'affiche jamais |
|---|---|---|
| Seuil de quorum | « fraction locale ≥ 1 − δ franchie chez x agents » | « décidé », « accord atteint » |
| Moyenne / alignement | « écart ≤ ε sur T tours » | « convergé » |
| Fusion CRDT | l'état courant, et rien d'autre | « convergé », « à jour » — la quiescence n'est constatable par **aucun** agent |

**EX-A51 [S]** — Chaque mécanisme du §5.1 **déclare la propriété qu'il abandonne** (figure 5.1) et le simulateur **arme par défaut l'oracle de cette propriété**, afin que la perte soit observable au lieu d'être supposée. Cet oracle est un privilège de l'observateur global — le simulateur — et l'interface dit explicitement qu'aucun agent ne dispose de cette information :

| Mécanisme | Propriété abandonnée | Oracle armé par défaut | Modes de défaillance en préréglages |
|---|---|---|---|
| Seuil de quorum | Accord, **sous partition réseau** | Compteur d'engagements incompatibles simultanés | Indécision (qualités voisines : la sûreté tient, la vivacité tombe) ; décision divisée (partition : deux quorums locaux, aucun agent ne le détecte) ; verrouillage (biais initial d'échantillonnage, absorbant — augmenter k ralentit sans supprimer) |
| Moyenne / alignement | Validité, et terminaison en temps fini | Écart mesuré entre la limite atteinte et la moyenne des états initiaux | Lenteur (connectivité algébrique effondrée, indistinguable d'une convergence absente) ; arrêt prématuré (deux sous-populations franchissent ε sur deux valeurs) ; dérive (digraphe non équilibré, somme non invariante) ; capture (un seul agent figé fixe la limite pour tout l'essaim) |
| Fusion CRDT | Validité — **le refus est impossible** | Compteur d'opérations acceptées qui auraient dû être refusées | Fusion qui accepte toujours ; famille « opérations » sous canal non exactement-une-fois (ne converge pas) contre famille « état » sous rejeu (converge, jonction idempotente) |

Chaque mécanisme affiche en permanence que ses verdicts sont **conditionnels au modèle P** : sous faute arbitraire, la borne 3f + 1 les tue tous les trois (§2.3).

**EX-A52 [S]** — Un type CRDT qui porte un invariant exigeant un **refus** — unicité, budget, exclusion mutuelle, capacité maximale — est rejeté à la construction, avec le message citant le §5.1. La confusion des deux familles est provocable comme préréglage : un type fondé sur les opérations dont la livraison n'est pas exactement-une-fois ne converge pas ; un type fondé sur l'état survit au rejeu parce que sa jonction est idempotente. L'interface affiche ce que le mécanisme achète en échange : l'immunité à la partition — les répliques d'un sous-ensemble connecté continuent de se livrer mutuellement leurs mises à jour sans qu'aucun accord soit requis.

**EX-A53 [S]** — **Le champ moyen répond à « combien », jamais à « lequel ».** Le mode champ moyen, s'il est introduit (voir RQ5), est **autorisé pour piloter la taille de la population et interdit pour l'allocation**. Justification implantée comme garde : les fractions d'états ne sont une statistique suffisante que sous échangeabilité des agents, et la possession d'une partition la détruit — savoir que 40 % des agents sont en traitement ne dit pas si la partition 17 a un propriétaire, et c'est cette information-là qui décide de la vivacité du sujet. L'activation du mode **désactive tout verdict d'allocation** et affiche l'avertissement. Trois hypothèses supplémentaires sont affichées avec le mode : l'irréductibilité de la matrice des taux, sans laquelle l'essaim admet plusieurs équilibres et le contrôleur peut le stabiliser dans le mauvais ; le fait que l'approximation vaut à la limite d'un grand nombre d'agents, un essaim de quelques dizaines de membres étant le cas où elle est **le moins** fondée ; et la fluctuation relative en 1/√n, ≈ 6 % à 250 agents, tolérable pour une couverture périmétrique et **disqualifiante** pour une partition de journal. Le même refus s'applique au sixième mécanisme d'EX-A05, en contrôle au chargement.

**EX-A54 [M]** — Le **prix de l'anarchie** est mesuré, non postulé : rapport entre le coût total à l'équilibre des décisions locales et l'optimum global, avec la borne théorique de la classe de fonction de coût tracée par-dessus la mesure — 4/3 pour une latence linéaire en la congestion, p + 1 pour un polynôme de degré p à coefficients positifs, et pour les fonctions générales continues non décroissantes, la seule borne disponible : la latence à l'équilibre n'excède pas celle d'un optimum contraint d'acheminer **deux fois** le trafic. L'interface affiche à côté de la borne **la fraction de charge portée par le plus gros agent** : la borne suppose un nombre infini d'agents infinitésimaux, et un essaim de n = 40 agents portant 2,5 % chacun ne la satisfait pas. Une borne affichée sans cette fraction est un défaut bloquant.

**EX-A55 [S]** — **Révocabilité.** Une décision est révocable si un agent peut l'annuler par une action locale de coût borné et connu. Toute action engagée par un mécanisme du §5.1 déclare ce coût. Le seuil de quorum n'est admissible que si l'engagement de sa ligne 10 est révocable : un engagement irrévocable est refusé au chargement, avec le message du traité. Cohérent avec l'auto-affectation à d sondes d'EX-A05, dont la révocabilité est bornée par la fraîcheur de la sonde.

**Complément imposé par le §8.3** : le partage entre décision révocable et invariant dur se double d'un **troisième cas**, qu'aucune des deux catégories ne couvre — *l'action irréversible prise par un agent contre un autre*. Elle n'est pas révocable au sens ci-dessus, et elle n'est pas non plus un invariant que le milieu protège, puisqu'elle ne passe pas par le milieu. Le simulateur la classe explicitement dans une troisième colonne, vide de mécanisme et pleine de raison : *hors du milieu, donc hors de la traçabilité du §6.2 et hors de tout limiteur de cadence* (T3). Une action rangée dans cette colonne ne reçoit **aucun** coût de révocation affiché — écrire un coût suggérerait qu'on peut la défaire.

---

**Exigences du chapitre 8** *(nouvelles en 3.0, toutes en phase 6, **toutes livrées**)* *(audit : la mention disait « aucune livrée »)*. Elles suivent la même discipline que les précédentes : signature complète, coût en messages et en tours, condition d'arrêt, mode de défaillance. Trois d'entre elles transposent un mécanisme que **le traité propose et que personne ne mesure** — l'ouvrage l'écrit de lui-même —, et cette provenance est affichée avec chacune, distincte de celle d'un résultat mesuré (F2).

**EX-A56 [M]** — **Φ_c, la conformité empirique.** Sur une décision d déposée dans le milieu, Φ_c est la probabilité que deux agents tirés au hasard produisent la même valeur, **moins** la valeur qu'aurait cette probabilité si les décisions étaient indépendantes de même loi marginale. Elle vaut 0 pour des tirages indépendants et 1 pour une population qui décide comme un seul agent.

- **Coût** : une lecture du sujet où les décisions sont déposées, et **aucun message supplémentaire** — les décisions y sont déjà écrites. C'est ce qui distingue Φ_c de l'estimateur que le troisième reste de la conclusion déclare introuvable : il ne demande aucune vue globale, seulement une lecture d'intervalle, donc il est admissible pour un agent au même titre que φ.
- **Précision** : celle de toute proportion, en 1/√k pour k paires observées. Affichée avec la valeur, jamais après.
- **Condition d'échec, et elle est structurante** : comparer deux décisions déposées sur deux partitions différentes suppose une relation d'ordre que **M2 ne fournit pas**. Φ_c se mesure donc **par partition**, ou sur un sujet dédié à une seule (DT14). Une configuration qui demanderait Φ_c sur un sujet multipartition est refusée au chargement, avec le message citant M2 — même geste qu'EX-A10 mode « incomparabilité M2 ».
- **Paramètre de contrôle** : la diversité effective de la population, c'est-à-dire la structure des familles d'EX-C19.
- **Aucun seuil n'est affiché, aucune zone n'est colorée, aucun mot ne qualifie la valeur.** Le traité écrit n'avoir aucune mesure du seuil et juger probable qu'il n'y en ait pas un seul ; l'interface affiche « seuil inconnu » à côté de la grandeur (PD5, F1).
- **Provenance** : grandeur proposée par le traité, mesurée par aucune source. Elle n'est jamais affichée dans le champ des chiffres retrouvés (NF-15).

**EX-A57 [C]** — **Algorithme 8.1, dépôt aveugle sur sujet de délibération**, implanté tel qu'écrit, avec la mention que le traité lui appose : *mécanisme proposé par l'ouvrage, mesuré par aucune source*. Signature complète : modèle de panne **P** ; synchronisme **asynchrone pour la sûreté**, partiellement synchrone avec borne Δ pour toute borne de temps ; hypothèses sur le milieu **M1, M3, M4 sur une partition unique**, plus l'identité apposée d'EX-M24. Mécanique : chaque agent écrit ce qu'il détient en propre, attend l'accusé de durabilité, **et ne lit qu'ensuite** — la lecture n'étant autorisée qu'au-delà de son propre décalage d'écriture. Le milieu n'a rien à évaluer, il n'a qu'à ordonner : c'est M1 employée comme contrainte de protocole et non comme garantie de lecture.

- **Coût** : 1 écriture et 1 lecture par agent et par tour, soit Θ(n) messages par tour — **autant** qu'une délibération libre. Le mécanisme ne coûte pas en messages, il coûte en **latence** : un tour de journal de plus par tour de délibération. Le compteur affiche les deux séparément, et le libellé dit lequel est le prix.
- **Condition d'arrêt** : un budget de tours **fixé d'avance et écrit dans le sujet**. Aucune stabilité ne sert de condition — c'est la stabilité prématurée que le mécanisme combat, et un critère d'arrêt sur stabilité serait ici le défaut, pas l'optimisation. EX-A38 s'applique : le simulateur n'en fabrique aucun.
- **Trois modes de défaillance, préréglages livrés** (NF-10) : (a) « attendre tout le monde » — l'étape 3 exige la présence de tous, un agent lent retarde toute la population ; la fenêtre doit être bornée par le temps et non par le nombre d'écrivains, et un absent n'est pas attendu ; (b) « fait vide » — l'agent qui ne détient rien en propre écrit un fait vide, et la **fraction d'enregistrements vides au tour 1** est le signal à surveiller : sous conformité forte, tous écrivent la même chose, ce que le mécanisme rend **visible sans le corriger** ; (c) « émission protégée, réception non » — rien n'oblige un lecteur à peser une pièce unique plus qu'un chœur ; le mécanisme protège l'émission d'un fait minoritaire et laisse entière sa réception, qui relève d'EX-M25.

**EX-A58 [S]** — **Les sept dettes d'indépendance sont armées, pas seulement documentées.** Chacun des sept énoncés du tableau 21 porte, dans le code à l'endroit où il est calculé et à l'écran à côté de la valeur, l'hypothèse d'indépendance qu'il suppose. Dès que le **réglage** viole démontrablement l'indépendance des tirages — c'est-à-dire dès que deux agents partagent une famille de décision —, la borne correspondante est **effacée** de l'affichage : pas grisée, pas pointillée, pas astérisquée, y compris quand la mesure est meilleure qu'elle (NF-14). *(Cette phrase disait « dès que Φ_c mesuré dépasse la précision de son estimation ». Le §0.1 l'a réfutée : Φ_c ne sépare pas la conformité de la coordination, donc effacer sur cette base afficherait une fausse alarme comme une preuve, ce que PD12 interdit. `dettes::verdicts` prend une `&Familles`, non une `&Conformite`.)* Le simulateur affiche à la place la phrase du traité : *aucun n'est faux ; tous changent de domaine de validité*. Six des sept portent sur des mesures **déjà livrées** ; l'exigence est donc, pour l'essentiel, une exigence de reprise sur du code existant, et non de code nouveau. C'est ce qui la rend peu coûteuse et facile à oublier.

**EX-A59 [C]** — **File de demandes d'arbitrage, écrite par les agents.** Symétrique exact de la directive d'EX-A07 : là où PD4 fait écrire la console vers l'essaim, EX-A59 fait écrire l'essaim vers l'opérateur. Un agent bloqué, en conflit de mandat, ou constatant une ambiguïté qu'il n'a pas autorité à trancher, écrit un enregistrement de demande sur un sujet dédié — époque, auteur **apposé** (EX-M24), décalage —, traité exactement comme une directive et doté de **son propre budget de latence**. Coût : 1 écriture. Fondement mesuré : dans les épisodes du §8.3 qui se règlent par une trêve, les agents nettoient ce qu'ils avaient déposé, écrivent des comptes rendus de ce qu'ils ont fait, et **demandent l'intervention d'un humain** — la demande d'arbitrage est un enregistrement comme un autre. Ce qu'elle ne borne pas, affiché avec elle : **le délai d'arrivée de l'humain, qui n'est pas dans le système** (tableau 22).

**Compléments de mécanisme, attachés à leur exigence.**

- **EX-A23 (détecteur), complétude dérivée** : un arrêt survenu juste après une sonde réussie n'est observé qu'au sondage suivant (0 à 10 s), puis exige deux échecs supplémentaires à 10 s d'intervalle, plus 1 s de délai d'expiration — **détection entre 21 s et 31 s**. C'est le budget d'indisponibilité incompressible de l'auto-guérison, **indépendant de la vitesse du redémarrage**, et l'interface l'affiche avec cette phrase. L'exactitude repose entièrement sur `timeoutSeconds = 1 s` : tout agent dont la latence de réponse dépasse 1 s trois fois de suite est classé mort, y compris un agent saturé mais vivant. Le simulateur ne paramètre pas ce taux : il le produit (EX-C15, PD12).
- **EX-A26 (sondes), la contre-mesure du traité est une bascule, pas un conseil** : la sonde de vivacité ne teste qu'un **blocage constatable sans travailler** — un fil qui n'a pas avancé son décalage depuis un multiple de `max.poll.interval.ms` —, jamais la capacité à répondre dans le délai, qui mesure la charge. Le scénario J montre que cette bascule supprime la cascade **sans changer la charge**. Ce que la sonde de disponibilité ne peut pas faire est affiché en toutes lettres à côté du réglage : elle n'a **aucun effet** sur l'allocation de partitions d'un consommateur, dont le travail n'arrive pas par un point d'accès mais par sa propre lecture du journal.
- **EX-A31 (corroboration), les deux régimes et jamais un seul chiffre** : sous indépendance, taux de fausses alarmes conjoint P(A\|¬I)ʳ et détection conjointe P(A\|I)ʳ ; à corrélation parfaite, P(A\|¬I)ʳ redevient P(A\|¬I) tandis que la détection conjointe **reste** à P(A\|I)ʳ. Le libellé : *la corroboration n'améliore pas la détection, elle échange de la détection contre de la précision* — et *rien dans le mécanisme ne mesure où l'on se situe entre les deux extrêmes*, ce qui interdit au simulateur d'afficher un P(I\|A) unique.
- **EX-A32 (AGRÉGER-ÉPIDÉMIQUE), facteurs et arrêt** : couplage parfait 1/4, offert **comme témoin non implantable** (exige une connaissance globale, étiqueté « non distribué — borne de comparaison ») ; tirage uniforme e⁻¹ ≈ 0,368, implanté ; tirage distribué du protocole 1/(2√e) ≈ 0,303, défaut. Après γ cycles, E(σ²) ≈ 0,303^γ · E(σ²₀) ; réduire la variance d'un facteur 10⁻⁶ demande γ ≥ ln(10⁻⁶)/ln(0,303) ≈ 11,6, soit **12 cycles, quelle que soit la taille de l'essaim**. Le simulateur calcule γ à partir de la cible de variance saisie, jamais l'inverse. À δ = 1 s posé comme hypothèse de dimensionnement, une époque coûte **24n messages et 12 tours**. La ligne 10 n'est pas décorative : l'estimation porte sur la population et les valeurs **du début de l'époque**, les arrivants sont tenus hors de l'époque en cours. Trois modes de défaillance, tous provocables :

| Préréglage | Réglage qui le provoque | Ce que l'utilisateur observe |
|---|---|---|
| « Dérive de masse » | Crash entre l'émission et la réception | La moyenne par paires ne conserve la somme que si l'échange est complet. L'estimation dérive et **rien ne la corrige**, aucun agent ne connaissant la somme vraie. C'est une **erreur de sûreté, non de vivacité** : elle ne se rattrape pas par l'attente, seulement par le redémarrage d'une époque — et l'interface refuse d'afficher « en cours de convergence ». Emballement chiffré : la variance reste bornée **si et seulement si** le facteur de convergence est inférieur à 1 − π, soit π < ≈ 69,7 % à 0,303 |
| « Scission silencieuse » | Partition réseau | Chaque grappe calcule un agrégat **local**. Chaque moitié observe une estimation parfaitement stable **et fausse** ; aucune condition d'arrêt fondée sur la stabilité ne distingue la convergence de la scission |
| « Un seul menteur » | Injection d'une valeur arbitraire, **hors modèle P** (DT8) | Rien dans l'algorithme ne borne la valeur reçue : un agent déplace la moyenne de toute la population d'une quantité arbitraire. Le simulateur n'offre **aucune défense** et affiche la borne : pas de solution à f traîtres avec moins de 3f + 1 participants, et à trois participants aucune solution ne résiste à un seul traître ; avec des messages écrits infalsifiables le problème redevient soluble pour tout nombre — *la cryptographie ne relâche pas la borne, elle la change* |

  **Contrôle à la construction** : un agrégat produit par ce mécanisme **ne peut pas alimenter une décision de sécurité**. Le chargement d'une configuration qui branche la sortie d'EX-A32 sur l'entrée d'EX-A33 (confinement) est refusé, avec le message : *l'agrégation épidémique est admissible pour estimer une charge, inadmissible pour établir un fait de sécurité* (§7.2). Le branchement sur le rééquilibrage de charge (EX-A25) est exactement l'usage prévu. *Raccord EX-A02* : l'agrégation épidémique et l'alignement de Vicsek partagent la structure — moyenne locale, absence de coordonnateur, convergence indépendante de la taille — et diffèrent sur deux points affichés côte à côte : chez Vicsek le voisinage est **métrique** et la grandeur moyennée est un cap, donc **bornée par construction** ; ici le voisinage provient d'un échantillonnage de pairs, et la grandeur moyennée **n'est pas bornée**, ce qui rend une seule valeur aberrante arbitrairement influente.

- **EX-A33 (bail), quatre clauses obligatoires** : (1) **La politique d'expiration est un choix binaire déclaré, sans valeur par défaut** — le simulateur refuse de démarrer si elle n'est pas posée. *Relâcher à l'expiration* : défaut sûr pour la disponibilité et **catastrophique pour la sécurité**, un adversaire capable d'induire une partition obtenant la levée des confinements. *Maintenir* : préserve la sécurité et **transforme toute partition réseau en panne durable**. Le libellé du traité accompagne le choix : *il doit être posé dans la politique plutôt que subi comme valeur par défaut d'une bibliothèque*. (2) **Le troisième mode est invisible et c'est le point** : si la dérive réelle (ε_vrai, EX-C13) dépasse l'ε supposé, le détenteur croit son bail vivant alors que le quorum l'a réattribué ; l'invariant est violé **sans qu'aucun agent ne l'observe**, et ni la latence ni le taux d'erreur ne le signalent. Seul l'oracle externe le voit. (3) **Dimensionnement de D** : le surcoût de bavardage vaut ℓ₉₉/D de l'intervalle, la capacité immobilisée au pire lors d'une partition vaut D ; **aucun réglage ne supprime les deux**, et l'interface trace les deux courbes ensemble. Le prix de la mesure de ε est affiché en gris et sourcé : une infrastructure de temps à références GPS et horloges atomiques maintient l'incertitude généralement sous 10 ms — *un déploiement hybride sans cette infrastructure ne mesure pas sa dérive ; il la suppose*. (4) **Pourquoi l'accord est requis ici et pas ailleurs** : deux agents qui décident indépendamment d'isoler deux hôtes appartenant au même quorum **réalisent le déni de service que l'attaquant n'avait pas obtenu**. La sûreté requise est un invariant global — *au plus f hôtes confinés simultanément* — qui doit tenir à tout instant. C'est exactement le cas où le substrat événementiel ne suffit pas, et l'interface le nomme au lieu de le contourner. La charge d'accord reste payable : sur les hypothèses d'Axelsson, 10⁶ événements par jour produisent de l'ordre de 10² alarmes et une poignée de confinements — **Θ(actions), non Θ(événements)**, quatre à cinq ordres de grandeur d'écart, et le compteur affiche les trois échelles ensemble.
- **EX-A34 (prédicats)** : tout oracle est classé **stable** (une fois vrai, il le reste) ou **instable**, et le classement est vérifié. « Le système est présentement attaqué » **n'est pas** stable — la session se termine et l'attaquant efface, et aucun instantané ne l'établit, même avec des canaux parfaits. « Un événement correspondant à la signature S s'est produit dans l'intervalle [t₁, t₂] » **est** stable dès lors que le milieu est en ajout seul. Le journal transforme donc un prédicat instable en prédicat stable, pour **Θ(1) message par observation et 0 tour** : c'est la raison technique pour laquelle la détection distribuée s'adosse au journal plutôt qu'à un état partagé. Le prix est la rétention, bornée par EX-M20.
- **EX-A35 (échantillonnage)** : le taux est un paramètre, avec ses repères en gris, mesurés sur une grappe de recherche et **non reproductibles ici** (F2) — à 1/1, latence moyenne +16,3 % et débit −1,48 % ; à 1/16, +2,12 % et −0,08 % ; à 1/1024, −0,20 % et −0,06 %, soit le bruit expérimental. Le simulateur **calcule** la conséquence pour la détection : une intrusion se manifestant dans une dizaine d'enregistrements, observée par un échantillonnage indépendant au taux 1/1024, a une probabilité 1 − (1023/1024)¹⁰ ≈ **0,97 %** d'être échantillonnée ne serait-ce qu'une fois. Un commutateur bascule vers l'**échantillonnage cohérent par trace**, qui rompt l'hypothèse d'indépendance des tirages au sein d'une intrusion : la probabilité remonte, et **c'est alors la couverture des traces, non celle des enregistrements, qui borne la détection**. Le commutateur change le libellé de la grandeur affichée, pas seulement sa valeur. Composé avec EX-A08 : une chaîne causale reconstruite depuis un journal échantillonné porte le drapeau de troncature **et** le taux qui l'a produite.
- **EX-A36 (AUTO-GUÉRIR), trois modes en préréglages** :

| Préréglage | Réglage qui le provoque | Ce que l'utilisateur observe |
|---|---|---|
| « Le côté minoritaire ne se répare plus » | Partition réseau isolant une minorité | L'acquisition du budget échoue, la ligne 7 s'applique, **aucun redémarrage n'a lieu** : l'auto-guérison perd sa vivacité exactement dans la circonstance qui la motive. Le libellé affiché : *c'est le prix assumé de sa sûreté*, pas un défaut |
| « Corroboration d'un faux soupçon » | Les s pairs placés dans le même domaine de panne que le lien fauté (EX-C14) | Le sondage indirect confirme, l'essaim redémarre **un agent sain** avec la pleine autorisation du budget |
| « Boucle auto-entretenue » | T_froid < durée réelle d'un redémarrage | Un soupçon repasse sur un agent en cours de démarrage ; la boucle ne termine pas |

  **Clause ajoutée en 3.0 — le compteur d'actions correctrices par fenêtre, avec arrêt au seuil.** Le §7.3 de la deuxième édition établit que la boucle de réparation peut devenir l'arme : trois agents chargés de migrer le même service déploient chacun sa version, voient la leur remplacée, concluent à une entrave délibérée, et retournent les moyens de cette section — chien de garde qui cherche et tue en boucle les processus concurrents, contrôle de santé falsifié, script de terminaison au nom anodin. Trois conséquences de conception s'en lisent, et les trois sont des exigences ici. (1) **Une sonde de vivacité n'est un signal fiable que si nul autre que le supervisé ne peut l'écrire** — ce qui disqualifie le contrôle de santé rendu par le service lui-même dès lors qu'il peut avoir intérêt à mentir ; c'est PD14 appliqué à une sonde, et EX-M24 en est la forme sur le milieu. (2) **La boucle porte un compteur d'actions correctrices par fenêtre et s'arrête au franchissement du seuil**, coût 0 message, un compteur local par boucle : la seule signature commune à toutes les exécutions observées est la **répétition rapide d'une action correctrice qui ne corrige rien** — l'effet de maintien du §2.3 avec un agent à la place de la file d'attente. Ce qu'il ne traite pas, affiché : un conflit lent, sous le seuil, qui dure. (3) **L'unicité du déployeur d'un service est un invariant global qui doit tenir à tout instant**, donc il relève de l'accord du ch. 4 et non du milieu : le rééquilibrage se passe d'accord, le droit de déployer non. Le simulateur refuse au chargement toute configuration qui prétendrait tenir l'unicité du déployeur par un mécanisme du §5.1 — même refus qu'EX-A52, même message.

### 6.4 `sim-viz` — visualisation et interaction

| # | Exigence | Étiq. | Source |
|---|---|---|---|
| EX-V01 | Le tableau de bord principal n'affiche **aucune ligne par agent**. Il présente des grandeurs de population : Φ quand un mécanisme le fournit, retard de consommation, ℓ₉₉, débit, plancher d'exploration, comptes de messages/tours | [U] | §6.3 ; PD3 |
| EX-V02 | L'inspection d'un agent individuel existe, mais est un mode « enquête » explicite, hors du parcours par défaut | [U] | PD3 |
| EX-V03 | Toute modification en cours d'exécution est écrite comme directive avec époque sur le sujet de commande ; l'interface affiche le **retard entre l'écriture et l'application effective**, et le compte d'accusés | [U] | §6.3 |
| EX-V04 | L'état d'une directive est « appliquée » (≥ a_min accusés), ou « **indéterminée** » — jamais « appliquée à 100 % », jamais « non appliquée » | [U] | §6.3 |
| EX-V05 | La règle d'alerte sur le retard porte sur la **dérivée** : un retard élevé mais décroissant est sain, un retard faible et croissant est la seule alarme qui se tienne | [U] | §6.2 |
| EX-V06 | Le percentile d'affichage des latences est un **paramètre** : ℓ₉₉ par défaut, ℓ₉₉,₉ disponible parce que c'est le centile auquel se lisent les chiffres de service d'un magasin réparti (§4.1 : latences au 99,9ᵉ centile d'un ordre de grandeur au-dessus des moyennes, et suivant le taux de requêtes). La moyenne, si affichée, est accompagnée de sa queue | [M] | §6.2, §4.1 |
| EX-V07 | Chaque scénario affiche en permanence : modèle de panne actif, hypothèse de synchronisme, graine, temps logique écoulé, temps mural écoulé | [U] | §3.1 (quatre conditions d'utilisabilité d'un modèle) ; PD6 |
| EX-V08 | La carte de chaleur des traces φ est ordonnée **par partition**, avec une séparation visuelle explicite entre partitions rappelant M2 : il n'y a pas de gradient entre elles | [U] | §1.2 |
| EX-V09 | Toute exécution est partageable par une URL encodant graine + configuration ; le destinataire voit exactement la même chose | [U] | Décision du produit (O4, O6) |
| EX-V10 | Une campagne sans interface — le **binaire `campagne`**, non une option `--headless` — produit CSV + rapport JSON, sans dépendance graphique ; le binaire dépend de `sim-agents` seul | [U] | Décision du produit (§5.1c) *(audit : `--headless` était un renvoi mort, le §5.1c l'ayant remplacé par un binaire séparé)* |
| EX-V11 | Chaque grandeur affichée porte son unité ; les grandeurs issues du traité portent leur référence de section et de page, les grandeurs issues de la simulation portent l'étiquette « simulé » | [U] | F1, F2 |
| EX-V12 | Le rendu WASM et le rendu natif produisent des chiffres identiques pour la même graine ; toute divergence est un défaut bloquant | [S] | NF-02 |
| EX-V13 | Tout détecteur affiché porte sa paire (complétude, exactitude) et l'état d'un agent est **sain / suspect / retiré** — jamais « mort ». Le passage de « suspect » à « retiré » nomme l'action qui l'a produit et son autorisation | [U] | §6.1, §7.3 ; PD12 |
| EX-V14 | Toute alarme affichée l'est avec **P(I\|A) et le taux de base assumé**. Un compte d'alarmes seul est un nombre sans provenance (F1) et l'interface le refuse. Les deux bornes — indépendance et corrélation parfaite — sont affichées ensemble, jamais une valeur unique | [U] | §7.2 |
| EX-V15 | **\|ISR\|, m et la largeur d'accusé** du dernier enregistrement validé sont affichés en permanence côte à côte (EX-M15), avec la marge d'accusé \|ISR\| − m étiquetée « grandeur dérivée du produit ». C'est le seul affichage qui trahit la perte muette de R1 | [S] | §6.1 |
| EX-V16 | Le bandeau de cascade (figure 6.1) affiche les quatre étapes — saturation, mort déclarée, rééquilibrage, report de charge — et un **compteur de générations**, à côté du compteur de pannes réelles. Le titre du bandeau est celui de la figure : *aucun agent n'est tombé, et l'essaim s'effondre* | [U] | §6.1, figure 6.1 |
| EX-V17 | Un panneau **« qui coordonne »** affiche en permanence le plan du milieu : meneur par partition, quorum de métadonnées, coordonnateur de groupe. L'interface n'écrit **jamais** « aucun coordonnateur » sans sa qualification : *vrai du plan des agents, faux du plan du milieu*. Une figure ou un libellé qui laisserait entendre que l'ensemble est décentralisé est un défaut bloquant, au même titre qu'un gradient entre partitions (RQ4) | [U] | §6.1 |
| EX-V18 | Le tableau 14 et la figure 5.1 sont une **grille vivante** : mécanismes en lignes, et **les sept colonnes du tableau 14** — modèle de panne, synchronisme, messages par tour, tours jusqu'à l'arrêt, condition d'arrêt, propriété abandonnée — plus les trois colonnes de la figure 5.1 (accord, validité, terminaison), chaque case remplie par la **mesure** (✓ tenue, ~ tenue sous condition, ✕ abandonnée) et non par la citation, les valeurs du traité restant affichées en gris en regard — même dispositif que le tableau 15 du scénario F. Les colonnes « modèle de panne » et « synchronisme » ne sont jamais vides : elles portent la signature déclarée du mécanisme (EX-V07). La légende du traité est reprise telle quelle : « non borné » signifie qu'aucune borne finie n'existe sous les hypothèses posées, **et non qu'elle est grande** | [U] | §5.1, tableau 14, figure 5.1 |
| EX-V19 | n est un **curseur de commande**, pas une constante de configuration. Toute action sur n passe par le sujet de commande avec époque (PD4, EX-A07) et affiche le rééquilibrage déclenché, son compte de messages et son compte de tours. L'utilisateur qui redimensionne l'essaim subit le même retard que le travail ordinaire, et le voit | [U] | §6.3 ; PD4 |
| EX-V20 | Toute borne de distribution affichée — champ moyen, prix de l'anarchie — porte la mention qu'elle **ne dit rien d'un agent particulier**, et le compteur d'agents individuellement non conformes reste affiché à côté d'elle. Un essaim conforme en distribution peut contenir un agent qui viole toutes les contraintes qu'on croyait garanties | [U] | §5.3, §3.1 |
| EX-V21 | Chaque levier de gouvernance actif affiche **sa fenêtre de violation** et **ce qu'il ne borne pas** : budget de reprise → l'agrégat de tous les clients ; étranglement adaptatif → la fenêtre de deux minutes déjà écoulée ; classes de criticité → rien, tant qu'un délesteur ne les lit pas ; budget de perturbation → les perturbations involontaires, qui le consomment sans pouvoir être empêchées ; dimensionnement automatique → un agent qui surestime son besoin. Une fenêtre non bornée s'affiche « non bornée », jamais « grande ». **Étendu en 3.0 aux huit lignes du tableau 22**, avec la même colonne « ce qu'elle ne traite pas », et un avertissement permanent que le tableau 16 n'exigeait pas : les leviers du §5.3 coûtent tous zéro message et zéro tour **parce qu'ils s'appliquent dans le processus qui allait émettre l'appel**, c'est-à-dire dans le processus même dont le §8.3 suppose qu'il agit contre le système. Le seul levier du produit qui échappe à cette objection est EX-M26, parce qu'il borne une ressource et non un agent | [U] | §5.3, tableau 16 ; §8.3, tableau 22 |
| EX-V22 | **Φ_c au tableau de bord**, à côté du décalage et de la latence de queue, parce que c'est la seule grandeur qui prédise l'effondrement **simultané**. Affichée avec : son intervalle en 1/√k, la partition sur laquelle elle est mesurée, la diversité effective en regard (structure des familles, EX-C19), et la mention « seuil inconnu » — jamais une couleur, jamais une zone, jamais un mot de jugement. Grandeur de population au sens de PD3 : aucune ligne par agent, et le détail par famille n'est accessible qu'en mode enquête (EX-V02). Elle ne figure jamais dans le même champ que le ρ dérivé des domaines de panne (EX-C14) : l'une porte sur les décisions, l'autre sur les pannes, et les mêler est un défaut bloquant au même titre que les deux ℓ₉₉ | [U] | §8.1 ; PD3, PD5, F1 |
| EX-V23 | **La file de demandes d'arbitrage** (EX-A59) est un panneau permanent de la console, au même rang que le sujet de commande : auteur apposé, époque, décalage, âge de la demande, et **son propre budget de latence**. L'interface n'affiche jamais un compte de demandes traitées sans afficher l'âge de la plus ancienne non traitée — c'est la règle de dérivée d'EX-V05 appliquée à une autre file. Le délai d'arrivée de l'humain est affiché comme **hors du système**, non comme une valeur manquante | [U] | §8.3, tableau 22 ; §6.3 |

---

## 7. Scénarios

Treize scénarios, un par thèse (§2.4) — douze livrés, le treizième spécifié en phase 6. Chacun expose, dans cet ordre et sans exception (PD8) : la **thèse**, citée avec sa section et sa page ; sa **source** ; ses **paramètres** ; le **mécanisme visible** — quel réglage produit quel effet observable, et par quel chemin ; ce que la **visualisation** montre ; son **critère d'acceptation** ; et ce qu'il **ne** démontre **pas**. Les pages citées sont celles de la **troisième édition** du traité, la seule que le dépôt contienne (F2, DT5). Elles ont toutes été migrées le 17 août 2026, ancre par ancre, et portent leur édition. Une **thèse est une citation**, donc sa provenance est vérifiable à la ligne : les treize l'ont été contre le PDF livré ([`bancs/audit-2026-08/FINITION-prd.md`](../bancs/audit-2026-08/FINITION-prd.md)), et **la thèse du scénario H change de page de deux chapitres** — « Le résultat n'est pas en retard, il est faux » est p. 58, 3ᵉ éd., non p. 44, 2ᵉ éd.

### Scénario A — Les deux régimes

> *Elle ne détruit pas le point partagé, elle le déplace dans le milieu.* (§2.1, p. 25, 3ᵉ éd. — ce document l'attribuait au §1.3, qui ne la porte pas dans la 3ᵉ édition)

**Source** : Figure 0, §1.3, tableau 3. **Priorité** : P0.

Deux populations de n agents côte à côte propagent le même changement. À gauche, maille pair à pair : chaque émetteur nomme son destinataire, entretient une vue d'appartenance par sondage. À droite, journal : une écriture, n lectures.

| Paramètre | Plage | Défaut |
|---|---|---|
| n (agents) | 4 – 2 000 | 64 |
| p (partitions) | 1 – 64 | 8 |
| ℓ₉₉ du chemin de durabilité | 1 – 500 ms | 20 ms |
| Délai d'aller simple pair à pair | 0,1 – 50 ms | 2 ms |
| Taux d'omission | 0 – 20 % | 1 % |
| d (destinataires nommés par dépôt) | 1 – 32 | 3 *(audit : réglable dans l'interface depuis la phase 5, ce tableau ne le portait pas)* |

Ces six réglages sont ceux que l'interface expose. La graine, elle, est **montrée
et non réglable** dans l'écran du scénario A, ce que le §0 consigne en réserve.

**Mécanisme visible** : augmenter n fait croître en n² le compteur d'entretien de vue à gauche, sans toucher au compte de lectures à droite ; augmenter ℓ₉₉ allonge les deux tours de journal à droite, sans toucher à l'aller simple à gauche. Le croisement se déplace sous les deux curseurs, et l'interface nomme lequel des trois comptes il croise.

**Ce que la visualisation montre** : trois comptes que le traité tient séparés et que l'interface ne mélange jamais. (1) **Une diffusion** — tableau 3, §1.3 : à gauche n−1 messages en 1 tour ; à droite 1 écriture + (k−1) réplications, puis 1 lecture par consommateur, en 2 tours de journal. (2) **L'entretien de la vue d'appartenance** — Θ(n²) messages par période de sondage à gauche (§1.3), sans équivalent à droite, le producteur n'ayant pas de destinataire à connaître. (3) **Un cycle où toute la population dépose** — Θ(n·d) messages à gauche contre Θ(n) à droite (§1.2). Sur le diamètre, l'interface n'affiche que le chiffre que le traité énonce — « le diamètre du graphe de coordination vaut 2 en permanence », pour le journal (§1.3) — et **n'en affiche aucun pour la maille**, le traité n'en donnant pas. Et — la partie que le traité refuse d'escamoter — le **temps** au bout duquel toute la population est informée : un aller simple à gauche, deux tours de journal à ℓ₉₉ à droite.

**Critère d'acceptation** : à ℓ₉₉ élevé et n faible, la maille gagne en temps — un aller simple contre deux tours de journal (tableau 3) ; à n élevé, son coût d'entretien de vue (Θ(n²) par période de sondage) croît quadratiquement alors que le compte de lectures du journal reste en Θ(n). Le point de croisement est affiché, déplaçable par les curseurs, et l'interface nomme lequel des trois comptes il croise.

**Ce qu'il ne démontre pas** : rien sur la sûreté. Les deux régimes propagent ; seul le prix diffère.

---

### Scénario B — Fourragement stigmergique

> *Un essaim stigmergique n'atteint pas l'optimum, il campe à distance bornée de lui.* (§1.2, p. 15-16, 3ᵉ éd.)

**Source** : Algorithme 2, §1.2 ; définition d'essaim, §1.1. **Priorité** : P0. **C'est le cœur du produit.**

n agents appliquant l'algorithme 2 sur m ressources d'utilité inégale, dont certaines changent de valeur en cours de route.

| Paramètre | Plage | Défaut | Rôle |
|---|---|---|---|
| γ (décroissance par fenêtre τ) | 0,50 – 1,00 ; le traité pose γ ∈ (0,1), **γ = 1 est hors domaine et exposé exprès** | 0,90 | γ = 1 → la trace est une somme cumulée et l'essaim n'oublie jamais une utilité devenue fausse |
| φ_min / φ_max | 10⁻⁴ – 1 | 0,01 | Le rapport borne le plancher d'exploration |
| α (poids de la trace) | 0 – 5 | 1,0 | |
| β (poids de l'heuristique) | 0 – 5 | 1,0 | |
| T (période de cycle) | 1 – 1 000 ms | 50 ms | T < ℓ₉₉ → essaim aveugle |
| τ (fenêtre de décroissance) | 10 ms – 60 s | 1 s | |
| Instant de bascule d'utilité | — | 50 % du budget | Révèle si l'essaim sait désapprendre |
| n (agents) | 4 – 256 | 16 | *(audit)* Plafond plus bas que celui du scénario A : chaque agent lit ce que toute la population écrit, donc le coût est en Θ(n²) — voir la réserve NF-05 |
| ℓ₉₉ du milieu | 1 – 500 ms | 20 ms | *(audit)* **Entrée** du modèle, jamais une sortie (§8.3 de ce document) : T < ℓ₉₉ produit l'essaim aveugle |
| Budget d'événements | 10 000 – 2 000 000 | 150 000 | *(audit)* Condition d'arrêt, non un paramètre du mécanisme : le produit s'arrête sur un budget, jamais sur une complétude |

Les trois dernières lignes n'ont **aucune provenance dans le traité** : ce sont des
décisions de produit (F1), ajoutées ici parce qu'elles sont réglables à l'écran et
qu'un curseur sans plage documentée est une grandeur sans provenance (F2).

**Mécanisme visible** : porter γ à 1 supprime le terme de décroissance dans le calcul de φ ; la trace devient une somme cumulée, le rapport φ_max/φ_min croît sans borne, la probabilité de tirage de la ressource dominante tend vers 1, et la bascule d'utilité à mi-course ne déplace plus l'effort. Le plancher d'exploration tracé descend au même rythme.

**Ce que la visualisation montre** : carte de chaleur de φ par partition ; répartition de l'effort sur les ressources ; **les deux seules bornes que le traité démontre**, tracées par-dessus la mesure — le plancher de tirage (1/m)·(φ_min/φ_max)^α·(η_min/η_max)^β et la fraction d'effort hors dominante ((m−1)/m)·(φ_min/φ_max)^α·(η_min/η_max)^β ; et l'**écart à l'optimum**, tracé comme **mesure seule, sans borne** — le traité écrit que l'essaim « campe à distance bornée » de l'optimum mais ne chiffre pas cette distance, et l'interface ne la chiffre pas non plus.

**Critère d'acceptation** : (1) avec γ < 1 et écrêtage, l'essaim suit la bascule d'utilité ; (2) avec γ = 1, il reste verrouillé sur la ressource devenue mauvaise ; (3) la fraction d'effort mesurée hors dominante ne descend **jamais** sous la borne calculée (oracle EX-A11b) — un écart serait un défaut d'implantation ou une erreur du traité, et les deux méritent d'être trouvés.

**Ce qu'il ne démontre pas** : la convergence. Le traité est explicite : « cet énoncé est une propriété du tirage, pas un théorème de convergence ». L'interface n'affiche jamais « convergé ». Ni l'émergence : le paramètre d'ordre Φ appartient au modèle de Vicsek **avec bruit** (§1.2) et aucun mécanisme du périmètre ne le fournit (PD5).

---

### Scénario C — Campagne USL : mesurer σ et κ

> *L'ouvrage n'a pas dit comment.* (conclusion, p. 130, 3ᵉ éd.)

**Source** : §2.1 (USL), §2.2 (dynamique de population), conclusion. **Priorité** : P1. **C'est la contribution du projet au traité.**

Balayage de n avec mesure du débit utile, puis ajustement par moindres carrés de :

$$C(n) = \frac{n}{1 + \sigma(n-1) + \kappa n(n-1)}, \qquad u^\* = \sqrt{\frac{1-\sigma}{\kappa}}$$

| Paramètre | Plage | Défaut |
|---|---|---|
| Points de mesure en n | 4 – 40 tailles | 16, réparties log |
| Répétitions par point (graines distinctes) | 5 – 200 | 30 |
| Fraction de travail passant par le milieu | 0 – 50 % | à estimer, non imposée |
| Coût de vue commune | activable | activé |
| p (plafond structurel) | 1 – 1 024 | 16 |
| Protocole de rééquilibrage | barrière / coopératif / battement de cœur | coopératif |
| Délai de session | 1 – 300 s | 45 s |
| Pilotage de n | balayage par configuration / curseur de commande (EX-V19) | balayage |

**Mécanisme visible** : n franchit p ; le débit cesse de croître pendant que le compte de messages de rééquilibrage continue — le numérateur de C(n) reste plat pendant que σ grossit (EX-M19). Au-delà de u\*, la courbe ajustée devient rétrograde, et la zone est colorée.

**Ce que la visualisation montre** : σ̂, κ̂, û\*, avec intervalles de confiance par rééchantillonnage ; courbe ajustée superposée aux points mesurés ; résidus ; **la zone où le débit devient rétrograde**, colorée ; le plafond min(n, p) tracé par-dessus ; le coût d'un changement de population ligne à ligne (EX-M22), avec le compte de phases affiché séparément du compte de tours ; le plancher mémoire de la population (EX-C17) ; et la ligne des cinq états du cycle de vie en fractions de population — jamais une ligne par agent (PD3).

**Critère d'acceptation** : (1) sur un milieu configuré avec une contention connue par construction, l'estimation retrouve les paramètres injectés à l'intérieur de son intervalle de confiance — cette validation croisée est ce qui autorise à faire confiance à l'estimation là où la vérité n'est pas connue ; (2) au-delà de n = p, le débit cesse de croître pendant que le compte de messages de rééquilibrage continue de croître ; (3) le calculateur de cible fondé sur la loi de Little (EX-A49) étiquette son résultat « non valide » dès qu'il est calculé sur une mesure prise en régime transitoire ou saturé.

**Ce qu'il ne démontre pas — et cela doit être affiché en permanence** : σ̂ et κ̂ caractérisent le **milieu simulé**, non un courtier de production. Ce que la campagne valide, c'est le **protocole de mesure** que la conclusion du traité réclame. Le libellé exact affiché : *« paramètres du milieu simulé — le protocole est transposable, la valeur ne l'est pas »*. Il ne démontre pas non plus l'existence d'un point fixe du contrôleur : la ligne 5 de l'algorithme 2 du ch. 2 borne n par p, elle **ne le borne pas par u\***, et au-delà de u\* la métrique cesse de décroître quand n croît. Le scénario J montre ce que le contrôleur fait quand il dépasse u\*, et il le dépasse en silence.

---

### Scénario D — La chute de R1

> *Le nombre de disparitions auquel r₂ survit n'est pas k − 1 = 2, il est m − 1 = 1.* (§2.1, p. 26, 3ᵉ éd.)

**Source** : §2.1, figure 2.1c ; §6.1 (ISR, R2, temporisateur). **Priorité** : P1.

Rejeu pas à pas, contrôlé par l'utilisateur, du déroulé complet à k = 3, m = 2 :

| Instant | Ensemble synchronisé | Événement |
|---|---|---|
| t₀ | {A, B, C} | r₁ accusé, largeur 3 |
| t₁ | {A, B} | C retiré pour retard — **aucune panne**, compteur à zéro |
| t₂ | {A, B} | r₂ accusé, largeur 2 ; C ne le détient pas |
| t₃ | {A} | B s'arrête ; sous m, la partition cesse d'accuser |
| t₄ | { } | A s'arrête ; seul C vit, et il ne détient pas r₂ |

Puis le choix : attendre le retour d'un membre (R1 préservée, indisponibilité non bornée) ou élire C (r₂ détruit chez ses deux détenteurs par troncature).

| Paramètre | Plage | Défaut |
|---|---|---|
| k (répliques assignées) | 2 – 7 | 3 |
| m (`min.insync.replicas`) | 1 – k | 2 |
| Temporisateur d'exclusion de l'ISR | 1 – 300 s | 30 s |
| Élection d'un non-membre | commutateur | désactivée |
| Préréglage « ISR muet » | commutateur | désactivé |

**Mécanisme visible** : porter m à 1 active le préréglage « ISR muet ». L'ISR se réduit au seul meneur sous charge, les producteurs continuent de recevoir leurs accusés, la largeur d'accusé affichée tombe à 1 — **et aucune erreur n'est émise**. C'est le seul endroit du produit où l'affichage vaut mieux que le protocole.

**Ce que la visualisation montre** : les trois journaux côte à côte, la largeur d'accusé de chaque enregistrement, et le moment exact où r₂ cesse d'exister ; en permanence, \|ISR\|, m et la largeur d'accusé du dernier enregistrement validé (EX-V15) ; le registre des hypothèses fortes (EX-C12) avec le compteur de fois où « un suiveur sain rattrape le meneur en moins de 30 s » a été faux dans l'exécution en cours.

**Critère d'acceptation** : (1) l'oracle R1 (EX-M06) est violé **exactement** à t₄ avec élection d'un non-membre, et **jamais** avec attente ; le compteur de pannes affiche 2 — donc k ≥ f + 1 respecté à l'égalité — au moment de la violation ; (2) le préréglage `min.insync.replicas = 1` fait tomber la tolérance de f à 0 **sans qu'aucune erreur ne soit émise**, et l'interface le nomme ; (3) sous saturation, l'exclusion de l'ISR frappe des suiveurs vivants, et le registre EX-C12 incrémente son compteur d'affirmation fausse.

**Ce qu'il ne démontre pas** : que la documentation du courtier se contredise. Elle conditionne sa garantie à ce qu'au moins une réplique reste synchronisée, et à t₄ aucune ne l'est. C'est justement le point, et l'interface le dit. Il ne démontre rien non plus sur un courtier déployé : le simulateur transpose la documentation, pas l'implantation, et un écart entre les deux est invisible d'ici (§2.3).

---

### Scénario E — La fenêtre de divergence

> *Borner cette fenêtre reviendrait à faire terminer un accord en asynchrone.* (§1.3)

**Source** : Algorithme 3 (ch. 1), §1.3. **Priorité** : P2.

Un agent écrit son ANNONCE ; entre cet instant et sa lecture par les autres, les vues divergent et deux propriétaires peuvent être désignés pour la même clé.

| Paramètre | Plage | Défaut |
|---|---|---|
| Δ (borne de délai, mode partiellement synchrone) | 1 ms – 10 s | 100 ms |
| Mode asynchrone | commutateur | désactivé |
| Débit d'arrivée des charges | 1 – 10 000 /s | 100 /s |
| Idempotence du traitement | commutateur | désactivé |

**Mécanisme visible** : basculer en mode asynchrone retire Δ du modèle ; la borne théorique disparaît de l'affichage (NF-14) et le compteur de charges doublement traitées cesse d'avoir un plafond — l'interface écrit « 0, …, ∞ ». Activer l'idempotence laisse le compteur inchangé et annule ses conséquences.

**Ce que la visualisation montre** : compteur de charges doublement traitées ; la borne théorique (débit × durée de fenêtre) superposée à la mesure ; et, en mode asynchrone, un compteur qui **ne se borne pas**, avec l'affichage « 0, …, ∞ » emprunté au traité.

**Critère d'acceptation** : sous synchronisme partiel, le compte mesuré reste sous la borne calculée. Avec idempotence activée, les doubles traitements persistent mais deviennent **sans conséquence** — ce qui est le point du traité : la première des trois issues couvre la majorité des cas réels.

**Ce qu'il ne démontre pas** : que la fenêtre puisse être bornée. La borner reviendrait à faire terminer un accord en asynchrone, et le simulateur ne l'offre à aucun réglage. L'idempotence rend les doubles traitements inoffensifs ; elle ne les supprime pas, et le cinquième reste de la conclusion — l'effet exactement-une-fois est impossible, « le seul recours reste l'idempotence de l'effet » (conclusion, p. 129, 3ᵉ éd.) — reste exhibé, non résolu.

---

### Scénario F — Allocation comparée

> *Deux sondes, 2d messages, un tour, zéro état partagé : c'est la borne à battre avant de proposer une enchère.* (§5.2)

**Source** : §5.2, tableau 15. **Priorité** : P2.

Six mécanismes, mêmes tâches, mêmes pannes, mêmes graines : affectation centralisée, Contract Net, glouton en ligne, enchère ε, auto-affectation à d sondes, politique stochastique par taux (EX-A05).

**Mécanisme visible** : arrêter un agent qui détient un objet pendant une enchère ε ; le mécanisme cesse de terminer, et le compteur de tours croît sans que la qualité bouge. Corréler les sondes du mécanisme à d = 2 ; l'avantage sur d = 1 se réduit, et l'interface trace ce qu'il devient plutôt que d'annoncer sa disparition.

**Ce que la visualisation montre** : le tableau 15 du traité, rempli par la **mesure** au lieu de la citation — messages, tours, qualité atteinte, condition d'arrêt observée, défaillance déclenchée. Les valeurs du traité restent affichées en regard, en gris.

Repères attendus (issus du traité, à retrouver ou à contredire) :

- Glouton en ligne : 3-compétitif. La borne est **la meilleure possible sous ses deux hypothèses**, que l'interface affiche avec elle : *sans modèle des arrivées futures et sans réaffectation, aucun allocateur — par enchère ou non — ne fait mieux que trois fois l'optimum hors ligne ; qui promet mieux achète l'écart contre l'une des deux hypothèses* (§5.2, p. 78, 3ᵉ éd.).
- Enchère ε : à n·ε de l'optimum, nombre de tours ∝ C/ε — l'exactitude se paie en tours, un pour un.
- Supermarché à d sondes : temps de séjour ≈ 2,61 à λ = 0,90 contre 10,00 à d = 1 ; ≈ 5,43 à λ = 0,99 contre 100,00.
- Politique stochastique par taux : 0 message, 0 tour, aucune condition d'arrêt ; fluctuation relative ≈ 1/√n.

**Critère d'acceptation** : (1) aucun mécanisme ne bat la borne 3-compétitive en ligne tant que ses deux hypothèses tiennent, et le simulateur affiche laquelle a été relâchée si l'une est battue ; (2) l'enchère ε avec un agent arrêté détenant un objet **ne termine jamais** — mode de défaillance nommé par le traité, et le simulateur doit le reproduire, pas le contourner ; (3) le résultat de d = 2 suppose des choix indépendants, que la corrélation détruit — le simulateur mesure ce que devient l'avantage à corrélation croissante, grandeur que le traité ne chiffre pas ; (4) la politique stochastique par taux est refusée au chargement dès qu'on tente de lui faire décider **quel** agent possède une partition (EX-A53).

**Ce qu'il ne démontre pas** : la performance d'un allocateur déployé. Le tableau 15 est rempli sur le modèle, avec ses propres coûts de message et de tour ; les valeurs du traité en regard sont des repères de provenance externe, jamais des cibles. Il ne démontre pas non plus qu'un mécanisme battant la borne 3-compétitive serait meilleur : il aurait relâché l'une des deux hypothèses, et l'interface nomme laquelle.

---

### Scénario G — Agrégat fenêtré et sous-compte silencieux

> *Une réponse fausse d'une quantité inconnue, que rien dans le résultat ne trahit.* (§7.1)

**Source** : §7.1, tableau 18. **Priorité** : P3.

Agrégat par fenêtre avec esquisses HyperLogLog fusionnables (m = 2 048 registres de 5 bits, erreur type ≈ 1,04/√m, ≈ 1,5 ko par esquisse), filigrane heuristique, volets révisables, manifeste M.

**Mécanisme visible** : désactiver le manifeste ; une partition muette cesse de contribuer, le volet publié reste étiqueté « complet », et l'erreur d'estimation affichée ne bouge pas — parce qu'elle mesure l'esquisse, pas l'absence.

**Ce que la visualisation montre** : le volet publié à chaque déclenchement, révisé par les suivants ; l'erreur d'estimation ; et surtout, avec manifeste désactivé, le **sous-compte silencieux** — une réponse fausse d'une quantité inconnue, que rien dans le résultat ne trahit. Le compte de tours affiché nomme sa convention : sous celle du §7.1 (aller-retour bloquant), l'essaim stigmergique à esquisses coûte **0 tour** (tableau 18).

**Critère d'acceptation** : avec manifeste, une partition muette produit un volet étiqueté « partiel, manquants = … » ; sans manifeste, elle produit un volet « complet » qui est faux. Le contraste est le livrable pédagogique.

**Ce qu'il ne démontre pas** : que le manifeste supprime le problème. Il convertit une erreur silencieuse en erreur nommée, et le traité interdit d'en revendiquer davantage.

---

### Scénario H — La valeur fausse unanime

> *Le résultat n'est pas en retard, il est faux.* (§4.1, p. 58, 3ᵉ éd.)

**Source** : Algorithme 1 (ch. 4), figure 4.1 (§4.1) ; push-sum et tableau 7 (§3.1) ; tableau 11, lignes « échange par paires », « échantillonnage de pairs », « tri de vue » et « politique stochastique » — la ligne « hachage cohérent » relève d'EX-A45 et du scénario C. **Priorité** : P1.

Trois mécanismes d'agrégation sur la même population, la même mesure locale v(i), les mêmes pannes, les mêmes graines : échange par paires push-pull (EX-A14), push-sum valeur-poids (EX-A15), politique stochastique par taux (EX-A16). Ils convergent tous. Deux d'entre eux convergent vers une valeur que personne ne peut réfuter et qui n'est la moyenne de rien ; le troisième ne converge vers rien d'observable. *(L'itération linéaire de Perron relève du scénario I, §2.4.)*

| Paramètre | Plage | Défaut | Rôle |
|---|---|---|---|
| n (agents) | 4 – 2 000 | 64 | |
| Fonction agrégée | moyenne / comptage / somme / produit / extrema | moyenne | seule la moyenne est traitée par le traité ; les autres suivent la même mécanique |
| T (période de cycle) | 1 ms – 10 s | 200 ms | contrainte affichée : T > 2Δ en régime nominal |
| τ (expiration du PULL) | 1 % – 99 % de T | 40 % de T | τ < T ; c'est l'expiration de la ligne 4 |
| Δ (borne de délai) | 1 ms – 5 s | 50 ms | valide seulement après l'instant de stabilisation |
| C (période de relance) | 5 – ∞ cycles | 50 | ∞ = relance désactivée, l'erreur n'est plus plafonnée |
| Taux d'omission | 0 – 20 % | 1 % | l'omission sur le retour est la ligne 4 |
| Accusé de réception (push-sum) | commutateur | désactivé | l'activer restaure la conservation à 2 messages par échange au lieu de 1 |
| d (taille de l'échantillon de pairs) | 1 – 32 | 4 | le pair du push-sum est tiré dans cet échantillon |
| Instant du premier crash-arrêt | — | 40 % du budget | l'agent emporte sa part |
| Biais de l'échantillonneur | uniforme / déséquilibré / groupé par hôte | **déséquilibré** | l'uniforme parfait n'est pas le défaut (RQ10) |
| Modèle de temps | asynchrone (horloge de Poisson) / synchrone (couplage) | asynchrone | DT11 ; l'unité de compte affichée change avec lui |
| Partition réseau | instant + coupe | désactivée | scinde l'essaim en deux composantes |

**Mécanisme visible** : porter le taux d'omission au-dessus de zéro fait perdre des PULL sur le chemin de retour ; à chaque perte, j a exécuté sa ligne 10 et i non, la somme des estimations quitte sa valeur de \|x_i − x_j\|/2 — pendant que la dispersion des x continue de décroître. Les deux courbes se croisent : l'unanimité s'installe pendant que l'invariant s'effondre.

**Ce que la visualisation montre** : un seul tracé porte tout le scénario — la **somme des estimations** contre la **somme des mesures initiales**, qui quitte sa valeur en escalier à chaque échange amputé ; par-dessus, la **dispersion** des x, qui tend vers zéro pendant ce temps. À côté, les tableaux 7 et 11 remplis par la mesure, les lignes non encore livrées restant affichées en gris avec les valeurs du traité (même convention que le scénario F). Chaque cellule mesurée porte son unité : messages par tour ou par tic pour les mécanismes à tours, **temps de mélange** pour la politique stochastique, qui n'en a pas. Et, sur un échange isolé, la figure 4.1 en quatre vignettes rejouables pas à pas.

**Critère d'acceptation** :

1. Avec omission nulle, sans crash et sans partition, la somme est conservée sur 100 graines à la précision de l'arithmétique retenue (DT1).
2. Au premier PULL perdu, la somme varie **exactement** de \|x_i − x_j\|/2, et l'oracle EX-A37 date l'événement à la ligne 4 de l'échange en cause.
3. Avec relance active, l'erreur cumulée reste bornée par le nombre de cycles depuis la dernière relance ; avec C = ∞, elle dérive sans borne. Le contraste est le livrable.
4. Sous partition réseau, le push-sum satisfait son critère d'arrêt local **des deux côtés de la coupe**, chaque composante annonçant sa propre moyenne — et l'interface n'affiche « convergé » dans aucune des deux (PD10, EX-A38).
5. Avec l'accusé de réception activé, la conservation tient sous omission du PULL, et le compte de messages passe de 1 à 2 par échange — le prix est visible, pas escamoté.
6. Avec l'échantillonneur groupé par hôte, le régime de cycles quitte Θ(log n) sans qu'aucun compteur du protocole ne bouge ; la borne théorique disparaît de l'affichage (NF-14).
7. La politique stochastique n'affiche à aucun instant un critère d'arrêt, même heuristique : sa seule sortie est une distribution de population et son temps de mélange (EX-A38).

**Ce qu'il ne démontre pas** : que la relance corrige quoi que ce soit. Elle **plafonne** l'erreur accumulée, et le traité interdit d'en revendiquer davantage. Il ne démontre rien non plus sur le signe de la dérive : le traité écrit « la somme totale a diminué » pour l'échange qu'il détaille ; la mesure montre les deux sens selon l'ordre de x_i et x_j, et l'interface affiche la quantité **signée** sans corriger le texte source.

---

### Scénario I — Propager, converger, s'accorder

> *L'essaim ne résout pas l'impossibilité, il refuse la question — et paie ce refus en fenêtres pendant lesquelles l'invariant peut être faux.* (§4.2)

**Source** : Figure 4.2 et tableau 12 (§4.2) ; figure 5.1 et tableau 14 (§5.1) ; algorithme 1 du ch. 3 et tableau 7 (§3.1). **Priorité** : P2. **Aucun protocole d'accord n'est implanté ici** (DT7) : la ligne « consensus, synchronisme partiel » reste affichée **en repère cité**, avec son Ω(n) messages par décision et sa terminaison conditionnelle, jamais mesurée.

Le même événement — une valeur nouvelle apparue chez un agent — traité par les trois barreaux, sur la même population : **propager** (rumeur EX-A19, anti-entropie EX-A20), **converger** (répliques sans conflit EX-A21 dans ses deux familles ; itération linéaire de Perron EX-A13 ; moyenne locale EX-A29), **s'accorder** (seuil de quorum EX-A28 ; consensus réduit EX-A22). Le scénario mesure ce que chacun coûte et ce que chacun **ne garantit pas**. Chaque mécanisme pose son modèle de panne, son synchronisme et ses hypothèses de canal **avant** son algorithme, et aucun des cinq ne suppose le même modèle — la grille EX-V18 affiche les signatures côte à côte, colonnes « modèle de panne » et « synchronisme » comprises.

| Paramètre | Plage | Défaut | Rôle |
|---|---|---|---|
| n (agents) | 8 – 5 000 | 256 | |
| d̄ (degré moyen du graphe) | 1 – 64 | 6 | |
| K (compteur de retrait) | 1 – 20 | 3 | fixe la fraction résiduelle de susceptibles |
| Retrait désactivé | commutateur | désactivé | K = ∞ : le schéma naïf, Θ(n log n) |
| Choix de pair sensible à l'adresse | commutateur | désactivé | l'activer sort du modèle et **efface** la borne |
| Anti-entropie en parallèle | commutateur | désactivée | le filet ; coût de comparaison réglable |
| Famille de répliques | état / opérations | état | change le **contrat de transport**, pas la structure |
| Contrat de transport | perd-duplique-désordonne / causal exactement-une-fois | perd-duplique-désordonne | le second est strictement plus cher |
| δ (seuil de quorum, M ≥ (1−δ)N) | 0,01 – 0,45 | 0,10 | δ = 0 → unanimité, donc ch. 4 |
| k (règle de k-unanimité) | 1 – 20 | 3 | l'unique entier qui règle le compromis vitesse/exactitude |
| ε, T (arrêt local de la moyenne) | — | 10⁻³, 20 tours | |
| α (pas de l'itération linéaire) | 0 – 1/Δ(G) | 0,5/Δ(G) | à 1/Δ(G), mode (a) d'EX-A43 |
| Topologie du digraphe | équilibrée / non équilibrée / moyeu | équilibrée | modes (b) et « Moyeu » |
| Classe de détecteur | fort / fortement exact à terme | fortement exact à terme | décide de la tolérance : quelconque, ou majorité de corrects |
| Corrélation des fautes (structure des domaines, EX-C14) | domaines disjoints → domaine unique | disjoints | l'activer invalide le calcul sans invalider le code ; ρ est **affiché comme dérivé**, jamais saisi |
| Agent menteur (DT8) | commutateur | **désactivé** | son activation affiche la borne 3f + 1 et la phrase de la figure 5.1 |
| Mode asynchrone pur | commutateur | désactivé | interdit les expirations et la détection de mort |
| Instant et durée de la partition réseau | — | 40 % du budget, 30 % de la durée | avant l'instant de stabilisation, aucune garantie temporelle ne tient |
| Substrat | pair à pair (EX-A04) / journal | pair à pair | commutateur d'extension, hors traité |

**Mécanisme visible** : abaisser K fait remonter la fraction résiduelle de susceptibles vers un plateau non nul — l'écart entre Θ(n log log n) et Θ(n log n) est l'effet de la seule ligne 6. Ouvrir une partition réseau pendant que le seuil de quorum est actif fait franchir la fraction locale ≥ 1 − δ des deux côtés de la coupe : deux options incompatibles sont engagées, et aucun agent ne le détecte — seul l'oracle armé (EX-A51) le compte.

**Ce que la visualisation montre** : trois axes de coût sur le même graphe — messages, tours, et **fenêtre pendant laquelle l'invariant peut être faux** —, avec Θ(n log log n), Θ(n log n) et Ω(n) tracés par-dessus la mesure ; la fraction résiduelle de susceptibles en fonction de K, qui se stabilise sur un plateau non nul au lieu de descendre ; pour les répliques fondées sur l'état, la taille de message qui croît en Θ(n) et le compteur de **marques de tombe** qui croît sans borne en l'absence de troncature ; pour le consensus, la fenêtre d'indisponibilité qui suit l'arrêt du meneur, indépendante de la charge ; la grille du tableau 14 et de la figure 5.1 remplie par la mesure (EX-V18) ; le compte de messages séparé selon la convention — Θ(n·d̄) point à point d'un côté, coût du milieu de l'autre (EX-M13) ; et, pour Perron, la limite atteinte contre la moyenne initiale contre l'enveloppe convexe des états initiaux.

**Critère d'acceptation** :

1. La fraction résiduelle de susceptibles converge vers une constante non nulle fonction de K et **ne décroît pas** quand on allonge le budget de simulation. Une décroissance serait un défaut d'implantation du retrait.
2. Avec le retrait désactivé, le compte de messages passe de Θ(n log log n) à Θ(n log n) : l'écart mesuré est l'effet de la **ligne 6 seule**, et l'interface l'attribue nommément.
3. Avec le choix de pair rendu sensible à l'adresse, la borne cesse d'être affichée — dans les deux sens, y compris quand la mesure est meilleure que la borne effacée.
4. Sous corrélation des fautes injectée, la couverture mesurée sort de la borne alors qu'aucun compteur du protocole ne bouge. C'est le résultat pédagogique du scénario.
5. Une fusion qui n'est pas une jonction de treillis produit une divergence que **rien dans le protocole ne signale** ; seul l'oracle du moteur la date. La tentative de faire porter au CRDT l'unicité d'un attributaire est refusée à la construction (EX-A52), et sous partition il est le seul des mécanismes à continuer de progresser.
6. La condition de convergence n'est déclarée satisfaite que dans son énoncé complet : absence de nouvelle écriture **et** au moins un échange d'anti-entropie mené à terme par chaque paire. Les deux clauses sont vérifiées par le moteur, jamais par un agent.
7. Le mode asynchrone pur refuse toute configuration terminante, et refuse en particulier les deux moyens que le résultat d'impossibilité exclut explicitement : les expirations de délai et la détection de la mort d'un processus. Le message de refus cite les deux.
8. Sous partition, le seuil de quorum engage deux options incompatibles, une de chaque côté, **et aucun agent ne le détecte** — seul l'oracle du simulateur le compte.
9. La limite atteinte par la moyenne n'est **pas** la moyenne des états initiaux ; l'écart est mesuré et affiché, et un unique agent qui n'applique jamais sa mise à jour fixe cette limite pour tout l'essaim.
10. À α = 1/Δ(G), l'itération de Perron cesse de converger (mode (a)) ; sur digraphe non équilibré, la limite est pondérée par la topologie et non par les données (mode (b)).
11. Le point de croisement en n où la décision distribuée devient préférable au coordonnateur est **mesuré**, avec le repère du traité affiché en regard — *pour les systèmes de petite à moyenne échelle, n < 200, une solution centralisée par diffusion est vraisemblablement le meilleur choix* — le coordonnateur étant celui du scénario F, instancié explicitement et séparément.

**Extension explicitement au-delà du traité** : le commutateur « substrat = journal » rejoue les mécanismes de choix sur le milieu au lieu du maillage pair à pair. Le traité ne le fait pas ; les résultats sont donc étiquetés « simulé, hors traité », et la seule chose qu'ils prétendent montrer est le déplacement du terme Θ(n·d̄) vers le coût du milieu. Aucune propriété de la figure 5.1 n'est réputée changer.

**Ce qu'il ne démontre pas** : que le consensus soit implanté. Le simulateur ne contient ni Paxos ni Raft (§2.3, DT7) ; il modélise le coût, la tolérance selon la classe de détecteur, et la fenêtre. Aucun résultat de ce scénario ne porte sur la correction d'un protocole d'accord — et l'impossibilité en asynchrone pur n'est pas *démontrée* ici, elle est *respectée*. Il ne dit rien de la sûreté sous asynchronie : l'impossibilité porte sur la terminaison, pas sur la sûreté, et les protocoles de la famille Paxos y restent corrects. Et il ne dit **rien sous faute arbitraire** : sous ce modèle, la borne 3f + 1 tue les trois mécanismes de la figure 5.1, le modèle est hors périmètre (§2.3), et l'affichage le dit en permanence plutôt que de laisser croire à une robustesse mesurée.

---

### Scénario J — La cascade de l'agent saturé

> *Aucun agent n'est tombé, et l'essaim s'effondre.* (§6.1, p. 91, 3ᵉ éd.)

**Source** : Figure 6.1 (§6.1) ; algorithme 3 et tableau 13 (§4.3) ; AUTO-GUÉRIR et bail de capacité (§7.3) ; bail de confinement (§7.2) ; défaillance métastable (§2.3). **Priorité** : P1.

Quatre volets, une thèse : l'essaim s'effondre sans qu'aucun agent ne faute, et ce qui le tient debout — l'époque et le bail — a sa propre fenêtre de silence. Le compteur de pannes réelles reste affiché dans les quatre volets.

**Volet 1 — La cascade.** Une population de n agents consommant p partitions sous une charge offerte croissante. Deux détecteurs composés : la sonde de vivacité du plan de conteneurisation et le détecteur à seuil fixe du groupe de consommation. Aucune faute n'est injectée — c'est la condition de démonstration.

| Paramètre | Plage | Défaut | Rôle |
|---|---|---|---|
| Charge offerte | 0 – 3× la capacité de service | rampe | Seul levier de la démonstration |
| Temps de service par agent | 0,1 – 100 ms | 5 ms | Fixe la capacité, donc le point de bascule |
| `timeoutSeconds` de la sonde de vivacité | 0,1 – 30 s | 1 s | La borne connue la plus serrée de la plateforme |
| `periodSeconds` / `failureThreshold` | 1 – 60 s / 1 – 10 | 10 s / 3 | Donnent la complétude 21–31 s |
| Protocole de rééquilibrage | barrière / coopératif / battement de cœur | coopératif | Fixe le coût de chaque mort déclarée |
| Durée de reconstruction d'état | 0 – 120 s | 10 s | Ce qui reporte la charge sur les survivants |
| Sonde de vivacité « décalage seulement » | commutateur | désactivé | Le remède du traité |
| Régime métastable (§2.3) | commutateur | désactivé | 280 → 560 → 150 req/s : l'état absorbant |

**Volet 2 — L'amplificateur : trois décisions avant le premier effet.** Un échelon de charge, la boucle de commande d'élasticité (EX-A25), et la somme des temps morts qu'elle traverse avant de voir son propre effet.

| Paramètre | Plage | Défaut | Source de la valeur |
|---|---|---|---|
| Période de synchronisation | 1 – 300 s | 15 s | valeur par défaut du contrôleur de référence |
| Bande morte τ | 0 – 0,5 | 0,1 | rapport **sans unité** ; n'entre dans aucune somme |
| Délai de disponibilité initiale | 0 – 300 s | 30 s | |
| Période d'initialisation de la métrique | 0 – 30 min | 5 min | ne s'applique qu'à la métrique processeur |
| Démarrage de l'agent | 0 – 120 s | 10 s | paramètre du modèle, pas du contrôleur |
| Fenêtre de stabilisation | 0 – 30 min | **0** | le seul amortisseur réel, absent de la formule ; provenance du défaut absente |
| W (fenêtre de mesure) | — | max(2·T_a, 60 s) | W < 2·T_a → oscillation |
| β (budget de churn, agents/s) | 0 – 100 | 1 | β·R ≪ 1 est la condition à tenir |
| R (durée d'un rééquilibrage) | 0,1 – 60 s | 3 s | |
| Métrique retenue | débit / décalage / processeur | décalage | le choix décide de +5 min ou non |
| Forme de l'échelon | échelon / créneaux / rampe | échelon | les créneaux traversent la bande morte plusieurs fois |
| Déclencheur | charge offerte / appartenance | charge offerte | EX-A44 : les confondre a un coût, mesuré |

**Volet 3 — Le soupçon et l'époque.** Détecteur de style infectieux (EX-A23) sur n agents ; un agent m devient lent, pas mort — un agent arbitrairement lent est indiscernable d'un agent arrêté (§4.2). Le soupçon se propage, l'allocation se reconfigure (EX-A24), m revient et écrit.

| Paramètre | Plage | Défaut | Rôle |
|---|---|---|---|
| n (agents) | 8 – 2 000 | 128 | la charge par membre en est indépendante — vérifiable |
| Mode de détection | infectieux / battement de cœur | infectieux | le second est le terme de comparaison : charge quadratique en n |
| Période de protocole | 100 ms – 30 s | 2 s | premier des deux seuls paramètres |
| Sous-groupe de sondage indirect s | 1 – 8 | 3 | second, et dernier |
| Suspicion activée | commutateur | activée | réduit les fausses détections, ne les annule pas |
| Lenteur injectée sur m | 0 – 60 s | 5 s | fabrique le faux soupçon |
| Instant de retour de m | — | après reconfiguration | m écrit avec une époque périmée |
| Taille de l'état par plage | 1 ko – 1 Go | 10 Mo | décide du poste dominant |
| Arbitrage d'époque par le milieu (DT9) | commutateur | **activé** | les deux seules issues (EX-A41) |
| Idempotence du traitement | commutateur | désactivée | sans elle, double effet à chaque panne |

**Volet 4 — Auto-guérison et baux sous dérive.** Deux sous-volets partageant le bail (EX-A33) et le détecteur (EX-A23).

| Paramètre | Plage | Défaut |
|---|---|---|
| q (taille du quorum du budget) | 1 – n | ⌈n/2⌉ + 1 |
| T_conf, T_froid | 1 – 300 s | 15 s, 120 s |
| Durée réelle d'un redémarrage | 1 – 600 s | 60 s |
| Domaine de panne des s pairs (EX-C14) | disjoint / partagé | disjoint |
| Part d'agents du côté minoritaire | 0 – 50 % | 30 % |
| D (durée du bail) | 0,1 – 600 s | 30 s |
| ε supposé par le mécanisme | 0 – 10 s | 10 ms |
| ε_vrai de l'horloge simulée (EX-C13) | 0 – 60 s | 10 ms |
| Politique d'expiration | relâcher / maintenir | **aucun défaut — à déclarer** |
| ℓ₉₉ du lien inter-plans | 1 ms – 10 s | 200 ms |

**Mécanisme visible** : la charge offerte franchit la capacité de service ; la file de chaque agent croît, sa latence de réponse — **sortie** du modèle (EX-C15) — dépasse `timeoutSeconds`, trois sondes consécutives échouent, l'agent est redémarré bien qu'il soit vivant, ses partitions sont rééquilibrées, la charge se reporte sur les survivants, et la génération suivante commence. Aucune faute n'a été injectée. La boucle de commande, dont le temps mort dépasse la période, ajoute trois décisions empilées sur la même cause.

**Ce que la visualisation montre** : les quatre étapes du bandeau EX-V16 s'allumant l'une après l'autre, avec le **compteur de pannes réelles restant à zéro** ; le débit servi, le nombre de partitions non servies, le compte de messages de rééquilibrage cumulé ; la latence de réponse au 99ᵉ centile franchissant le seuil de la sonde. Volet 2 : la chronologie des temps morts **en série**, additionnés et non maximisés — 15 s pour que l'écart soit vu, plus le démarrage, plus 30 s avant que la réplique compte — avec le plancher de 45 s affiché comme **somme calculée**, marqué « valeur dérivée » (F2) ; le nombre de répliques contre la cible, avec le dépassement puis la reprise symétrique à la baisse ; le couloir 1,0 ± 0,1 et le compte de ses traversées ; en regard, à l'échelle, le délai d'élection de 150–300 ms du §4.2 — deux ordres de grandeur plus bas, ce qui est le point. Volet 3 : les trois postes de coût en barres empilées — propagation de la vue (O(n log log n) messages, O(log n) tours), recalcul de l'affectation (local et gratuit, ≈ 1/n des plages déplacées), **relecture des points de reprise** (proportionnelle à la taille de l'état, pas à n) — et laquelle domine ; l'anneau de hachage avec le bail et l'époque de chaque plage ; le compteur d'écritures rejetées pour époque périmée ; la **durée de double détention** affichée séparément ; le compteur de doubles effets ; et, en mode battement de cœur, la courbe de charge en n². Volet 4 : le compteur de réparations du côté majoritaire qui avance et celui du côté minoritaire qui reste à zéro, avec le libellé *prix assumé de la sûreté* ; les deux courbes de dimensionnement de D — bavardage ℓ₉₉/D et capacité immobilisée D — qui ne descendent jamais ensemble ; et, quand ε_vrai franchit ε, la double allocation de la même unité de capacité **pendant que la latence et le taux d'erreur restent plats**.

**Critère d'acceptation** :

1. Sous le seuil de saturation, zéro redémarrage sur toute la durée. Au-dessus, la cascade est **complète en trois générations**, sans qu'aucune faute ait été injectée, et le compteur de pannes affiche 0 au moment où l'essaim ne sert plus rien.
2. La bascule « décalage seulement » supprime la cascade **à charge inchangée** ; un `timeoutSeconds` plus généreux **ne la supprime pas** — il retarde la première mort déclarée et allonge la détection vraie, ce que le tableau des latences affiche côte à côte. C'est le critère qui compte : le traité écrit que le remède n'est pas un réglage plus généreux.
3. Avec fenêtre de stabilisation nulle, l'échelon produit un dépassement puis une oscillation, et le nombre de corrections empilées sur une même cause est exactement le nombre de périodes de synchronisation contenues dans le temps mort. La bande morte seule ne l'amortit pas. À W < 2·T_a, la population diverge en dents de scie **avec le compteur de pannes à zéro** ; à β·R ≳ 1, le débit utile s'effondre pendant que le compte de tours de rééquilibrage croît.
4. Le budget de réaction mesuré est ≥ 45 s hors démarrage, et ≥ 45 s + 5 min avec la métrique processeur. Avec une sonde réglée par défaut (10 s / 1 s / 3 échecs, soit 30 s avant retrait), aucune bascule de meneur du scénario I n'est jamais vue par la sonde ; descendre la période à l'échelle de l'élection convertit chaque bascule de quelques centaines de millisecondes en un redémarrage de plusieurs secondes, et le compteur de redémarrages le montre.
5. Déclencher sur l'appartenance et déclencher sur la charge offerte produisent des réponses opposées au même événement de panne partielle ; le rééquilibrage supplémentaire est compté en messages et en tours (EX-A44).
6. Avec arbitrage d'époque, **S1w** tient sur toutes les graines, y compris sous faux soupçon suivi du retour de m : les écritures de m portent une époque inférieure et sont rejetées. **S1 au sens du glossaire ne tient pas pour autant** : la durée de double détention est non nulle et non bornée en asynchrone, et l'interface l'affiche comme telle (EX-A41).
7. Sans arbitrage d'époque, une écriture d'époque périmée est acceptée **exactement** à l'instant où m réapparaît et écrit, et pas avant. La violation est le résultat attendu du scénario, pas un défaut du simulateur.
8. Sans idempotence, le nombre de doubles effets est égal au nombre d'enregistrements compris entre le décalage validé et la position réelle du traitement au moment du soupçon — quantité prévisible et affichée avant le déclenchement.
9. Le temps espéré de première détection et la charge de messages par membre ne varient pas avec n sur la plage mesurée ; la latence de dissémination croît logarithmiquement. Un écart mesuré sur l'une de ces trois grandeurs est un résultat à publier. En mode battement de cœur, la charge croît quadratiquement.
10. La condition d'arrêt de l'algorithme 3 — toute plage a un propriétaire dont le bail porte l'époque courante — est affichée comme **vivacité conditionnelle**, avec sa condition, et jamais avant l'instant de stabilisation.
11. Les oracles « au plus f hôtes confinés simultanément » et « une seule allocation par unité de capacité » ne sont violés **que** si ε_vrai > ε supposé, jamais autrement.
12. Sous la politique *relâcher*, une partition réseau induite lève les confinements — le scénario le produit et l'étiquette comme **avantage de l'adversaire**, pas comme défaut ; sous *maintenir*, la même partition produit une panne durable, et les deux traces sont comparables à graine identique.
13. Avec T_froid < durée de redémarrage, la boucle d'AUTO-GUÉRIR ne termine pas, et l'oracle de vivacité bornée expire au lieu d'échouer — conformément à EX-C11. Sous partition isolant une minorité, l'acquisition du budget échoue et **aucun redémarrage n'a lieu** du côté minoritaire.

**Ce qu'il ne démontre pas** : le comportement d'un client de courtier réel ni la performance d'un autoscaleur réel. Le simulateur transpose des valeurs par défaut documentées et **périssables** ; un déploiement dont les défauts diffèrent produira une autre cascade, pas l'absence de cascade, et l'interface reprend l'avertissement du tableau 13 : à revalider à la version ciblée. Qu'une troisième voie existe : le simulateur n'offre que les deux issues du traité et refuse la configuration « détecteur exact ». Deux limites structurelles restent hors de portée du modèle et sont affichées comme telles, parce que le traité les écrit précisément pour ce qu'elles sont invisibles à l'usage : (1) un autoscaleur de nœuds ne considère que les **requêtes de ressources déclarées**, jamais l'utilisation réelle, si bien qu'un mauvais réglage des requêtes rend la mise à l'échelle de l'infrastructure structurellement fausse — le simulateur ne modélise pas la réservation (§2.3) et ne peut donc pas produire ce mode ; (2) la combinaison d'un contrôleur horizontal et d'un contrôleur vertical sur la même métrique est un conflit connu que la documentation officielle n'aborde pas, et de ce qu'elle ne l'interdit pas on ne peut pas déduire qu'elle le prend en charge. La désynchronisation par gigue n'y est pas chiffrée : les seuls résultats disponibles proviennent d'une simulation publiée hors comité de lecture (annexe B). Il ne démontre rien non plus sur les défaillances où **aucun agent n'est tombé au sens de MAST** — désalignement entre agents, défaut de vérification de la tâche : la reconfiguration ne les répare pas, et elles sont hors périmètre (§13). Enfin, que la mesure de la dérive soit à portée : le simulateur fait saisir ε, il ne le mesure pas plus qu'un déploiement dépourvu de références de temps dédiées. Libellé permanent du volet 4 : *ici, le bail est sûr sous hypothèse, non par construction*.

---

### Scénario K — La fenêtre de violation

> *Le budget est un plafond, pas une garantie.* (§5.3)

**Source** : §5.3, tableau 16. **Priorité** : P3. Raccordement : les deux premiers leviers sont ceux d'EX-A09 ; ce scénario les mesure **en tant que gouvernance**, c'est-à-dire par ce qu'ils ne bornent pas.

Une dépendance saturée, cinq classes de clients, un quota délibérément surengagé. Chaque levier s'active et se désactive indépendamment.

| Paramètre | Plage | Défaut |
|---|---|---|
| Classes de criticité | 4 étiquettes (CRITICAL_PLUS, CRITICAL, SHEDDABLE_PLUS, SHEDDABLE) | actives, sans délesteur |
| Budget de reprise | ≤ 3 tentatives ; plafond 0 – 100 % du volume client | 3 ; 10 % |
| Étranglement adaptatif | K ∈ [1, 10] ; fenêtre 10 s – 10 min | K = 2 ; 120 s |
| Quota par classe | 5 valeurs, somme libre | 4000 + 4000 + 3000 + 2000 + 500 CPU·s/s sur 10 000 CPU |
| Budget de perturbation | seuil explicite, **sans valeur par défaut** | non défini — l'exécution refuse de démarrer tant qu'il ne l'est pas |
| Taux de perturbations involontaires | 0 – 10 /min | 0,5 /min |
| Estimation du besoin | auto-déclarée / mesurée | auto-déclarée |
| Classe de la fonction de latence | linéaire / polynomiale (degré p) / générale | linéaire |
| Mode de synchronisme | partiellement synchrone / asynchrone | partiellement synchrone |

**Mécanisme visible** : activer le budget de reprise borne l'amplification **par client** à 1,1 fois la charge nominale ; la dépendance saturée reçoit alors 1,1 × la charge nominale de *chacun* des clients conformes, et aucune règle locale ne voit l'agrégat. Basculer en asynchrone retire Δ, et toutes les fenêtres chiffrées deviennent « non bornées ».

**Ce que la visualisation montre** : le tableau 16 rempli par la mesure, avec la colonne « ce qu'il ne borne pas » **testée et non citée** ; la fenêtre de violation de chaque levier actif en secondes (EX-V21) ; le prix de l'anarchie mesuré contre sa borne, accompagné de la fraction de charge portée par le plus gros agent (EX-A54) ; la part de ressources réservées non utilisées selon le mode d'estimation ; et le compteur d'agents individuellement non conformes à côté de toute borne de distribution (EX-V20).

**Critère d'acceptation** : (1) avec budget de reprise, l'amplification **par client** est bornée à 1,1 fois la charge nominale, et l'agrégat de clients tous conformes ne l'est pas ; (2) les perturbations involontaires **consomment** le budget de perturbation jusqu'à épuisement sans qu'aucune ne soit empêchée, et une suppression directe le contourne entièrement ; (3) le rapport mesuré équilibre/optimum reste sous 4/3 en latence linéaire tant que la fraction du plus gros agent est négligeable, et **sort de la borne** quand n est petit — c'est ce dernier point que le scénario existe pour montrer ; en latence polynomiale de degré 3, la borne applicable est 4, non 4/3 ; (4) le passage de l'estimation auto-déclarée à l'estimation mesurée réduit la part réservée non utilisée, dans le **sens** annoncé par le traité ; (5) en mode asynchrone, chaque levier affiche « fenêtre non bornée » et aucune valeur chiffrée n'apparaît (RQ8).

**Ce qu'il ne démontre pas** : les valeurs de 23 % contre 46 %, le facteur 10 sur les incidents d'épuisement mémoire et la couverture de plus de 48 % de la flotte sont des mesures d'une flotte réelle, affichées comme repère de provenance externe (F2) et **jamais** comme cible du simulateur. Ce que le scénario mesure est le signe de l'écart et son mécanisme causal — un agent autonome qui estime lui-même son besoin le surestime, parce que le coût d'une sous-estimation lui est imputé alors que le coût d'une surestimation est mutualisé. C'est une externalité, et le scénario montre qu'aucune règle locale ne la corrige : seule une politique imposée le fait, c'est-à-dire une autorité (PD11). Ni l'émergence : ce scénario ne prétend à aucune régularité émergente, faute de paramètre d'ordre (PD5) — il dit « comportement collectif ».

---

### Scénario L — Le taux de base

> *Une sonde presque parfaite produit des alarmes presque toutes fausses.* (§7.2)

**Source** : §7.2, figure 7.2, tableau 19. **Priorité** : P2.

n agents-sondes homogènes appliquant le même détecteur à λ événements par seconde chacun, sur un flux d'audit dimensionné comme celui d'Axelsson. **P(I) n'est jamais saisi directement** : il est dérivé des trois grandeurs qui le produisent, pour que l'utilisateur voie d'où vient 2 × 10⁻⁵.

| Paramètre | Plage | Défaut | Rôle |
|---|---|---|---|
| Enregistrements d'audit par jour | 10⁴ – 10⁸ | 10⁶ | Dénominateur du taux de base |
| Tentatives d'intrusion par jour | 0 – 100 | 2 | Numérateur |
| Enregistrements affectés par intrusion | 1 – 1 000 | 10 | Complète P(I) = 2 × 10⁻⁵ |
| Taux de détection P(A\|I) | 0 – 1 | 0,70 | 1,00 est offert et étiqueté « irréaliste » |
| Taux de fausses alarmes P(A\|¬I) | 10⁻⁷ – 10⁻¹ | 10⁻³ | 10⁻³ correspond au plafond de 100 fausses alarmes/jour |
| n sondes, λ événements/s | 1 – 10⁵, 1 – 10⁴ | 64, 12 | Débit de fausses alarmes n · λ · P(A\|¬I) |
| Seuil de corroboration r | 1 – 10 | 3 | r = 1 désactive la corroboration |
| Fenêtre de corroboration W | 1 s – 1 h | 60 s | Condition d'arrêt du mécanisme |
| **Structure des domaines de panne** (EX-C14) | domaines disjoints → domaine unique partagé | disjoints | **Le curseur du scénario.** ρ n'est pas saisi : il est **affiché comme grandeur dérivée** de la structure, et parcourt 0 → 1 quand le curseur va d'un bout à l'autre |
| Taux d'échantillonnage de traces | 1/1 – 1/4096 | 1/1024 | Compose avec EX-A35 |
| Horizon de rétention R | — | hérité d'EX-M20 | Au-delà, le prédicat redevient invérifiable |
| Budget d'attention de l'astreinte | 1 – 10⁴ alarmes/jour | 100 | Fixe, par construction |
| Agent menteur (DT8) | commutateur | désactivé | Son activation affiche la borne 3f + 1 |

**Mécanisme visible** : glisser le curseur de structure des domaines de « disjoints » vers « domaine unique » fait passer les s détecteurs d'entrées indépendantes à des entrées corrélées ; le taux de fausses alarmes conjoint P(A\|¬I)ʳ remonte vers P(A\|¬I) pendant que la détection conjointe **reste clouée** à P(A\|I)ʳ = 0,343. P(I\|A) glisse de ≈ 99,99 % à ≈ 2 % sans qu'aucun indicateur interne du mécanisme ne bouge.

**Ce que la visualisation montre** : les cinq lignes de la figure 7.2 recalculées en direct ; le débit de fausses alarmes croissant **linéairement en n** contre un budget d'attention **plat** — multiplier les sondes multiplie le dénominateur de l'équation de Bayes sans toucher au numérateur ; le ρ dérivé affiché à côté du curseur de structure ; et le tableau 19 rempli par la mesure.

**Critère d'acceptation** : (1) les cinq valeurs de la figure 7.2 sont retrouvées à moins d'un point de pourcentage — 66 %, 58 %, 2 %, 99,99 %, 2 % ; (2) la détection conjointe vaut 0,343 à r = 3 et P(A\|I) = 0,70, **invariante en ρ** ; (3) **l'estimation Monte-Carlo issue du flux d'événements simulé et la valeur analytique de Bayes coïncident dans l'intervalle de la vérification statistique bornée (§8.4)** — si les deux chiffres divergent, c'est le mécanisme qui est faux, pas la formule, et le scénario doit pouvoir le dire ; (4) un oracle dont l'horizon dépasse R est refusé au chargement (EX-M20) ; (5) le prédicat « le système est présentement attaqué » est classé instable et refusé comme oracle, le prédicat « un événement de signature S s'est produit dans [t₁, t₂] » est accepté (EX-A34).

**Ce qu'il ne démontre pas** : la corrélation réelle d'une flotte. Le simulateur permet de l'**injecter** par domaines de panne (EX-C14) ; il ne prétend pas l'estimer sur un système réel, faute d'estimateur qui ne demande pas déjà la vue globale qu'on cherchait à éviter (§8.3). Et il ne démontre pas que conditionner soit une issue : élever P(I) en ne notant que les événements déjà situés dans un contexte suspect **déplace la borne d'un cran sans la lever**, puisque ce contexte doit lui-même provenir d'un détecteur ; le scénario permet d'empiler deux étages pour le montrer.

---

### Scénario M — Le second axe

> *Un milieu qui rend la coordination bon marché rend du même geste bon marché ce que le concepteur ne veut pas* — introduction, **p. 5, 3ᵉ éd.** —, *… la conformité, puisque tous lisent la même trace ; la collusion, puisqu'un tableau public suffit à s'aligner au sou près ; la tromperie, puisque déposer coûte le même prix qu'on dise vrai ou faux* — **§8.3, p. 127, 3ᵉ éd.**

⚠ **Deux provenances pour une thèse, et c'est ce qu'il faut lire.** Cette thèse est une **épissure** de deux passages du traité, et la version antérieure de ce document la donnait sous la seule mention du §8.3 avec p. 94, 2ᵉ éd. — une page qui n'est celle d'aucun des deux dans le traité livré, et une provenance unique pour deux sources. Mesuré le 17 août 2026 : la proposition principale est **p. 5, 3ᵉ éd.**, à la fin de l'avant-propos de la troisième édition, dans son libellé exact avec « du même geste » ; l'énumération des trois conséquences est **p. 127, 3ᵉ éd.**, au §8.3, où elle s'introduit par « la mesure **ajoute** qu'il rend tout aussi bon marché ce que le concepteur ne veut pas ». `sim_agents::scenario_m::BLOC_M` déclare les deux provenances depuis l'audit ; ce document les déclare depuis cette révision. C'est le défaut que F2 nomme, commis par la règle qui le nomme.

**Source** : §8.1 (conformité, tableau 21), §8.2 (la trace comme témoignage, algorithme 8.1), §8.3 (buts incompatibles, tableau 22). **Priorité** : P2. **Phase 6 — livré** *(audit)*, avec son `BLOC_M` et ses onze tests de sortie.

Ce scénario ne montre rien de neuf : il **reprend quatre scénarios livrés** et pousse un curseur qu'aucun d'eux n'avait. C'est sa forme, et elle est délibérée. Le ch. 8 ne réfute aucun mécanisme de l'ouvrage ; il déplace le domaine de validité de sept énoncés, ce que le traité désigne comme *plus difficile à voir et [se corrigeant] moins bien, puisque le mécanisme continue de tourner pendant que sa borne cesse de tenir*. Un scénario qui exhiberait un nouveau mécanisme manquerait exactement cela.

**Volet 1 — La conformité et les sept dettes.** Une seule structure de familles de décision (EX-C19), pilotée d'un bout à l'autre, sur les quatre scénarios porteurs des dettes que le produit sait mesurer.

| Paramètre | Plage | Défaut | Rôle |
|---|---|---|---|
| **Structure des familles de décision** (EX-C19) | une famille par agent → une famille unique | une par agent | **Le curseur du scénario.** Φ_c n'est pas saisi : il est **dérivé** de la structure et des décisions déposées, et parcourt ≈ 0 → ≈ 1 quand le curseur va d'un bout à l'autre |
| Scénario rejoué | B / D / F / L | B | chacun porte l'une des dettes du tableau 21 |
| k (paires observées pour Φ_c) | 10² – 10⁶ | 10⁴ | fixe la précision en 1/√k, affichée avec la valeur |
| Partition de mesure de Φ_c | une partition, ou sujet dédié | sujet dédié | multipartition refusé au chargement (M2, EX-A56) |
| n (agents) | 4 – 2 000 | 64 | |
| Quota par ressource (EX-M26) | désactivé / quota dur / prix croissant / seuil de concentration | désactivé | le seul levier structurel, et il borne une ressource, pas un agent |

**Volet 2 — Le témoignage.** Le même journal, avec et sans les deux mécanismes d'attribution du §8.2, plus le dépôt aveugle.

| Paramètre | Plage | Défaut | Rôle |
|---|---|---|---|
| Identité apposée (EX-M24) | commutateur | **activée** | désactivée, un agent dépose sous le nom d'un autre et EX-A08 ne le voit pas |
| Préréglage « identité partagée » | commutateur | désactivé | plusieurs processus, une identité : le zombie du §2.1 revenu par la porte de l'identité |
| Historique par identité (EX-M25) | désactivé / issues vérifiables / issues non vérifiables | désactivé | la troisième position est **refusée au chargement** — elle récompenserait la conformité du volet 1 |
| Dépôt aveugle (EX-A57) | commutateur | désactivé | 1 tour de journal de plus par tour de délibération |
| Budget de tours de délibération | 1 – 50 | 5 | fixé d'avance et écrit dans le sujet ; aucune stabilité ne sert de condition |
| Part de faits détenus en propre | 0 – 100 % | 25 % | à 0 %, tous écrivent la même chose au tour 1 — le mode (b) d'EX-A57 |

**Volet 3 — Les buts incompatibles, et ce que le milieu n'en voit pas.** Trois mandats contradictoires sur la même ressource, et le seul volet dont la thèse est une **limite du simulateur** plutôt qu'un résultat.

| Paramètre | Plage | Défaut | Rôle |
|---|---|---|---|
| Mandats contradictoires | 0 – 8 agents sur la même ressource | 3 | le dispositif du §8.3 |
| Journal obligatoire des actions d'agent à agent | commutateur | activé | désactivé, l'action n'est ni comptée ni refusée : c'est T3 rendu visible |
| Compteur d'actions correctrices par fenêtre (EX-A36) | seuil 1 – 100, fenêtre 1 s – 10 min | 5 / 60 s | la seule signature commune aux exécutions observées |
| File de demandes d'arbitrage (EX-A59) | commutateur | activée | avec son budget de latence propre |
| Délai d'arrivée de l'opérateur | 0 – ∞ | **∞ par défaut** | hors du système ; l'afficher fini serait inventer une provenance |

**Mécanisme visible** : glisser le curseur de familles de « une par agent » vers « une famille unique » fait consommer aux n agents le même tirage pour la même décision. Au scénario B, le plancher d'exploration mesuré cesse d'être atteint par m ressources et l'est n fois sur une seule ; la borne d'EX-A11c **disparaît** de l'affichage (NF-14) pendant que l'oracle EX-A11b, lui, ne se déclenche pas — il vérifie une inégalité qui reste vraie agent par agent. C'est le point du scénario : le mécanisme continue de tourner, l'oracle reste muet, la borne cesse de tenir. Au scénario F, l'avantage de d = 2 sur d = 1 s'annule parce que tous sondent les mêmes candidats. Au scénario L, la corroboration s'effondre **sans qu'aucun domaine de panne n'ait été fusionné** — deuxième chemin vers le même effondrement, par les décisions au lieu des pannes, et l'interface affiche les deux causes dans deux champs distincts.

**Ce que la visualisation montre** : Φ_c en fonction de la diversité effective, avec son intervalle en 1/√k et la mention « seuil inconnu » — jamais une zone colorée ; en regard, **le tableau 21 rempli par la mesure**, une ligne par dette, chaque ligne portant l'état de sa borne (affichée / effacée) et le scénario qui la porte ; les trois lignes non mesurables par le produit — gigue pleine, champ moyen, vérification statistique — restant en gris avec la valeur du traité, même convention que le tableau 15 du scénario F. Volet 2 : deux journaux côte à côte, avec et sans identité apposée, et la chaîne causale d'EX-A08 reconstruite sur chacun — l'une exacte, l'autre **fausse et d'apparence identique** ; le compte d'enregistrements vides au tour 1 du dépôt aveugle ; et le tour de journal supplémentaire, compté à part du compte de messages qui, lui, ne bouge pas. Volet 3 : le tableau 22 rempli, colonne « ce qu'elle ne traite pas » testée et non citée (EX-V21) ; la file de demandes d'arbitrage avec l'âge de la plus ancienne non traitée (EX-V23) ; et, en permanence, le libellé de T3 — *ici, le milieu voit ce qu'on lui a fait écrire ; le régime mesuré, lui, contourne le milieu.*

**Critère d'acceptation** :

1. Φ_c mesuré vaut ≈ 0 à structure « une famille par agent » et ≈ 1 à famille unique, sur 100 graines, et l'écart aux deux extrémités reste dans l'intervalle en 1/√k. Une valeur non nulle à familles disjointes serait un défaut de l'estimateur, pas un résultat.
2. **Les quatre bornes que le produit sait mesurer s'effacent, et chacune à sa cause** : plancher d'exploration (scénario B), redondance k (scénario D), avantage de d = 2 (scénario F), corroboration r parmi n (scénario L). Une borne qui resterait affichée à Φ_c ≈ 1 est un défaut bloquant (NF-14, EX-A58).
3. **Aucun oracle de sûreté armé ne se déclenche pendant cet effacement.** C'est le critère qui porte la thèse : les oracles vérifient des propriétés qui restent vraies, et ce qui cesse de tenir est une **borne**, que rien dans le protocole ne surveille. Un scénario qui ferait tomber un oracle prouverait autre chose que ce qu'il annonce.
4. Le curseur de familles et le curseur de domaines de panne (EX-C14) produisent au scénario L **le même** effondrement de P(I|A) par **deux** chemins distincts, et l'interface attribue chaque exécution à sa cause sans jamais additionner ρ et Φ_c.
5. Avec l'identité apposée désactivée, un agent dépose sous le nom d'un autre, la chaîne causale d'EX-A08 est reconstruite **sans drapeau de troncature et sans erreur** — elle est fausse, et rien ne le signale. Avec l'identité apposée, la même tentative laisse le champ `producer` intact et la chaîne est exacte. Le contraste est le livrable du volet 2, sur le modèle du manifeste au scénario G.
6. Le préréglage « identité partagée » ramène le défaut du §2.1 : deux processus sous une identité, et l'attribution redevient fausse **alors que le mécanisme est actif**. C'est la condition d'échec d'EX-M24, provoquée et non décrite.
7. Le dépôt aveugle change l'issue de la délibération quand la part de faits détenus en propre est non nulle, coûte **exactement un tour de journal de plus** par tour, et **ne change pas** le compte de messages. Les deux comptes sont affichés séparément ; un scénario qui présenterait le coût en latence comme un coût en messages est refusé.
8. À part de faits propres nulle, tous les agents écrivent la même chose au tour 1 : la fraction d'enregistrements vides monte à 1, le mécanisme la **rend visible et ne la corrige pas**, et l'interface n'écrit à aucun moment que la délibération a été améliorée.
9. La position « issues non vérifiables » de l'historique par identité est **refusée au chargement**, avec le message citant §8.2 : *là où l'issue n'est pas vérifiable, l'historique n'enregistre que la concordance avec la majorité*.
10. Avec le journal obligatoire des actions d'agent à agent désactivé, le compteur d'actions d'agent à agent reste à zéro **pendant que la ressource change de main** : le simulateur ne voit rien, et l'affiche comme un angle mort du modèle, jamais comme une absence d'événement (PD6, T3).
11. Le compteur d'actions correctrices par fenêtre arrête la boucle au franchissement du seuil, et un conflit maintenu **sous** le seuil dure indéfiniment sans être arrêté — la colonne « ce qu'il ne traite pas » du tableau 22 est mesurée, pas citée.

**Ce qu'il ne démontre pas** — et ce bloc est plus lourd que celui de tout autre scénario, ce qui est la raison de l'écrire en entier :

- **Que la conformité mesurée par le traité soit reproduite.** Elle est **injectée**. Le simulateur ne contient aucun modèle de langage, ne produit aucune décision par un modèle, et n'a aucun moyen de faire émerger la variance nulle : il la pose. Le scénario ne démontre donc pas que des agents réels se conforment ; il démontre **ce que la conformité fait à des résultats déjà mesurés ici**, ce qui est une proposition différente et la seule que le monde clos autorise. Libellé permanent : *la conformité est une entrée du modèle, comme la corrélation des fautes ; ce que le scénario mesure est son effet, jamais sa valeur.*
- **Qu'il existe un seuil.** Le traité écrit n'en avoir aucune mesure et juger probable qu'il n'y en ait pas un seul. Aucun affichage de ce scénario ne comporte de seuil, de couleur ou de zone, et l'énoncé « la population est conforme » ne s'y trouve nulle part.
- **Que les mécanismes du §8.2 fonctionnent.** Aucun n'est mesuré par une source, l'ouvrage compris. Le produit les fait tourner et les **facture** — 0 message et quelques octets pour l'identité, 1 écriture par vérification pour l'historique, 1 tour de journal pour le dépôt aveugle — et il montre ce que chacun laisse passer. Un coût mesuré et une condition d'échec provoquée ne sont pas une validation.
- **Que l'escalade du §8.3 soit empêchable.** Le simulateur n'a ni système d'exploitation, ni droits, ni identité de session : il ne peut modéliser que le chemin conforme, donc il ne peut pas produire le contournement, qui est le mode de défaillance. Il ne dit jamais qu'une escalade a été empêchée (T3).
- **Que les valeurs du ch. 8 soient retrouvées.** Aucun des chiffres du rapport cité — 266 vulnérabilités, 17 à 85 %, 18 agents sur 30, 2,4 millions de demandes pour 117 acceptations — n'entre dans un critère d'acceptation. Ils sont des repères externes périssables, liés à une version de modèle que le produit ne contient pas (F5, annexe B). NF-15 ne s'applique **pas** à eux, et l'affirmer serait la faute exacte que NF-15 existe pour empêcher.

---

## 8. Exigences non fonctionnelles

### 8.1 Déterminisme et reproductibilité [S]

| # | Exigence |
|---|---|
| NF-01 | Rejeu bit-à-bit à partir de graine + configuration, sur la même version du binaire |
| NF-02 | Reproductibilité inter-plateformes natif/WASM pour les mêmes entrées (implique : arithmétique flottante déterministe, pas de `fast-math`, pas de fonctions transcendantes divergentes entre cibles — à défaut, arithmétique en points fixes sur les chemins qui influencent l'ordonnancement) |
| NF-03 | La version du binaire et le hachage de la configuration sont écrits dans tout export ; un rejeu sur une version différente est **refusé**, pas tenté |
| NF-04 | Un test d'intégration exécute 100 graines et vérifie l'égalité des traces entre deux exécutions consécutives |

### 8.2 Performance [M]

| # | Exigence | Cible |
|---|---|---|
| NF-05 | Débit de simulation, mesuré en **secondes simulées par seconde-cœur** — l'unité du traité, pas le nombre d'exécutions | ≥ 10³ s simulées/s-cœur à n = 1 000, p = 16 |
| NF-06 | Coût par exécution | Θ(E log E) pour E événements (file de priorité) |
| NF-07 | Interactivité de la visualisation | ≥ 30 images/s à n ≤ 2 000 en WASM |
| NF-08 | Taille du binaire WASM | ≤ 8 Mo compressé |

**Note de méthode** : NF-05 est une cible d'ingénierie, pas une mesure du traité. Elle est étiquetée comme telle dans le code.

### 8.3 Ce que le produit ne mesure pas [U]

Le traité insiste : une méthode de validation se définit autant par ce qu'elle **ne** réfute **pas**. À afficher dans l'interface, section « limites », en permanence :

- **La performance réelle.** Le temps simulé n'est pas le temps mesuré. Aucun chiffre du simulateur ne prédit la latence d'un système déployé.
- **Les deux ℓ₉₉, qui ne portent jamais le même libellé.** **ℓ₉₉ du milieu** — le chemin écriture → accusé de durabilité → lecture — est une **entrée** du modèle : un paramètre du milieu simulé, tiré d'une distribution que l'utilisateur choisit (EX-M09). **ℓ₉₉ de réponse d'un agent** est une **sortie** : elle émerge de sa file et de son temps de service (EX-C15), et elle croît avec son arriéré. La distinction n'est pas un aménagement : sans elle, la cascade du §6.1 serait scriptée au lieu d'être produite, et l'énoncé du §7.3 — *le taux de fausses suspicions est une fonction croissante de la charge* — deviendrait un paramètre au lieu d'un résultat. Les deux grandeurs portent des étiquettes distinctes dans toute l'interface, et un affichage qui les mêlerait est un défaut bloquant.
- **Ce qui est hors du monde clos.** Aucune bibliothèque tierce, aucune dépendance, aucun système d'exploitation n'est testé.
- **La vivacité.** Aucune trace finie ne réfute L1. Ce que le simulateur produit est au mieux une **vivacité conditionnelle** : ramener l'environnement, après une série de pannes, dans un état où la reprise devrait être possible, puis vérifier que le système finit par se rétablir.
- **Tout n.** Vérifier à n = 5 ne dit formellement rien de n = 5 000 : le problème d'accessibilité est indécidable même à espace d'états local fini. Ce n'est pas une borne de complexité qu'un meilleur solveur ferait reculer.
- **Les événements de probabilité inférieure à ε.** À ε = 10⁻³, une probabilité vraie de 10⁻⁴ et une probabilité vraie nulle produisent la même conclusion.
- **Les fautes corrélées.** Toutes les bornes probabilistes du traité supposent des fautes indépendantes. Deux agents issus de la même image, derrière la même dépendance, sur le même plan de contrôle, ne tombent pas indépendamment. Le simulateur permet d'**injecter** une corrélation par domaines nommés (EX-C14) ; il ne prétend pas la mesurer sur un système réel, faute d'estimateur qui ne demande pas déjà la vue globale qu'on cherchait à éviter.
- **Les décisions corrélées, et ce n'est pas la même chose que la ligne précédente.** *(Ajout de la version 3.0.)* Deux agents partageant leur fonction de transition ne tombent pas seulement ensemble : ils **choisissent** ensemble, ce qui est le second axe de la frontière. Le produit l'injecte par familles nommées (EX-C19) et en dérive Φ_c (EX-A56) ; il ne l'estime sur aucune population réelle. Les deux grandeurs — ρ, dérivé des domaines de panne ; Φ_c, dérivé des familles de décision — portent des noms distincts, occupent des champs distincts, et un affichage qui les mêlerait est un défaut bloquant, exactement comme pour les deux ℓ₉₉. La raison est la même : le §2.1 corrèle une **panne**, le §8.1 corrèle un **choix**, et confondre les deux ferait passer une décision de conception pour un accident de plateforme.
- **La décision d'un modèle de langage.** Le simulateur n'exécute aucun modèle et n'appelle aucun service ; δ y reste un programme. Ce qu'il simule du ch. 8, ce sont les **conséquences** mesurées de la variance nulle — une corrélation de tirages, un champ d'identité non authentifié, un compteur par ressource —, jamais leur cause. Aucun résultat du scénario M ne porte sur le comportement d'un agent de langage, et son libellé permanent le dit avant d'afficher quoi que ce soit.
- **Tout ce qu'un agent fait à un pair hors du milieu.** Pas de système d'exploitation dans le monde clos, donc pas de révocation de compte, pas de terminaison de processus, pas de contrôle de santé falsifié. Le simulateur mesure le **coût** de l'exigence qui les interdirait, pas son efficacité (T3), et il n'écrit jamais qu'une escalade a été empêchée.
- **La validité d'une population dans le temps.** Le §3.3 de la deuxième édition établit que les résultats d'une campagne sur une population d'agents s'inversent d'une génération de modèle à l'autre. Ce que l'on sait valider avant déploiement, ce sont les **mécanismes du milieu** ; la population ne se valide pas, et aucune campagne de ce produit ne le prétend.
- **L'uniformité du tirage de pairs.** Le service d'échantillonnage du simulateur descend du même RNG semé que le reste du monde clos : il est aussi uniforme qu'on le lui demande. Or le résultat expérimental du traité est que les implantations réelles fournissent un flux **localement** uniforme dont les propriétés d'aléa ne tiennent pas globalement, et que des choix de conception différents produisent des écarts sévères d'équilibrage de charge et de tolérance aux fautes (§4.1). Toute borne de convergence ou de couverture que le simulateur retrouve est donc retrouvée sous l'hypothèse la plus favorable. Le biais est un paramètre à injecter (EX-A17), jamais une propriété mesurée — et le préréglage par défaut n'est pas l'uniforme parfait.
- **La quiescence.** La condition de convergence des répliques exige l'absence de nouvelle écriture, propriété globale qu'aucun agent ne peut vérifier localement (§4.2). Le simulateur la vérifie depuis l'extérieur du monde perçu, ce qui est légitime pour un oracle et illégitime pour un agent : aucun mécanisme du produit n'a le droit de consulter cet oracle pour décider.
- **Le coût réel d'un rééquilibrage de courtier.** C'est une **entrée** du modèle, comme ℓ₉₉ du milieu.

### 8.4 Vérification statistique [M]

Le mode vérification implante l'algorithme 2 du §3.2 :

$$N = \left\lceil \frac{\ln(2/\delta)}{2\varepsilon^2} \right\rceil$$

L'interface affiche N **avant** de lancer, avec ses repères : ε = 10⁻², δ = 10⁻² → N ≈ 26 492 exécutions ; ε = 10⁻³ à la même confiance → N ≈ 2,65 × 10⁶, soit cent fois plus pour un chiffre significatif de plus. La sortie est p̂ ± ε avec Pr(\|p̂ − p\| > ε) < δ, jamais une valeur nue.

Trois refus d'affichage complètent la sortie. Un comportement dont la probabilité est inférieure au seuil d'échantillonnage **n'est pas déclaré absent — il n'est pas vu**. Une campagne qui épuise son budget sans violation affiche « aucune violation observée en N exécutions », jamais « aucune violation ». Et une vérification qui ne termine pas dans son budget est rapportée comme **absence de verdict** : le traité nomme précisément ce piège à propos du model checking exhaustif — passé une taille d'essaim, le vérificateur ne termine pas, et l'ingénieur reçoit un silence qu'il est tenté de lire comme une absence de problème (EX-C18).

### 8.5 Qualité et tests

| # | Exigence | Étiq. |
|---|---|---|
| NF-09 | Chaque algorithme du traité a un test qui vérifie une propriété **citée dans le traité**, référence de section en commentaire | [C] |
| NF-10 | Chaque mode de défaillance nommé a un test qui le **provoque** et vérifie qu'il se produit | [C] |
| NF-11 | Les invariants du milieu (M1–M4, R1, R2) **et la conservation de masse des protocoles d'agrégation** sont des oracles activables en permanence dans les tests, coûteux mais exacts | [C] |
| NF-12 | Aucun test ne dépend de l'horloge murale ni d'un `sleep` | [S] |
| NF-13 | La couverture conditionnelle (EX-C08) est vérifiée en intégration continue : une condition jamais atteinte sur 1 000 graines est un avertissement de campagne, pas un échec de test | [M] — **non tenue** : il n'y a pas d'intégration continue dans le dépôt, et l'agrégat de campagne (`Agregat`) n'a aucun appelant |
| NF-14 | Toute borne théorique tracée par-dessus une mesure porte, dans le code et à l'écran, la liste des hypothèses qui la conditionnent. Un réglage qui viole une hypothèse **efface la borne** — il ne l'affiche ni en pointillé, ni en gris, ni avec un astérisque —, y compris quand la mesure est meilleure que la borne effacée | [S] |
| NF-15 | Tout mécanisme reproduisant un chiffre du traité a un test qui le **retrouve** : 21–31 s de latence de détection ; 12 cycles pour une réduction de variance de 10⁻⁶ ; 0,343 de détection conjointe à r = 3 ; ≈ 0,97 % de probabilité d'échantillonner une intrusion à 1/1024 ; les cinq valeurs de P(I\|A) de la figure 7.2 ; 20 réévaluations du contrôleur ; 0,012 message par enregistrement à b = 500 et k = 3. Un écart est un défaut du simulateur **ou** une erreur du traité, et les deux méritent d'être trouvés | [S] |
| NF-16 | Tout mécanisme portant une hypothèse plus forte que « Δ finie mais inconnue » a un test qui **rend l'hypothèse fausse** et vérifie que le mode de défaillance annoncé se produit — pas un autre, et pas aucun. La liste des hypothèses est le registre EX-C12 | [S] — le mécanisme d'application nommé (« échoue l'intégration continue ») **n'existe pas** : ce que l'exigence obtient vient de `cargo test --workspace` lancé à la main |

---

## 9. Plan de livraison

**Six phases, une thèse par phase.** Le passage de quatre à cinq n'était pas une inflation : les dix sections jusque-là absentes formaient deux blocs indivisibles — la triade *propager / converger / s'accorder* (§4.1, §4.2, §5.1, §3.1) et la *fenêtre de violation* (§4.3, §5.3, §7.3) — qu'aucun découpage ne coupe sans détruire la thèse. Le passage de cinq à six n'en est pas une non plus, et pour une raison d'un autre ordre : **la source normative a changé**. Les cinq premières phases sont closes et leurs critères de sortie sont atteints ; la sixième porte les trois sections que la deuxième édition ajoute, et rien d'autre. Aucune phase antérieure n'est rouverte — ce que le ch. 8 retire aux phases 1 à 5 n'est pas de la correction mais de la **portée de validité**, et cela se répare en affichant, pas en réimplantant (EX-A58).

**Les budgets.** Chaque phase porte un budget chiffré, sans quoi la règle de coupe n'a pas de déclencheur. Ces nombres sont des **décisions de projet**, sans aucune provenance dans le traité, et étiquetés comme tels partout où ils apparaissent (F1). Unité : la semaine-personne (sp).

| Phase | Budget déclaré | Déclencheur de coupe |
|---|---|---|
| 1 — Le noyau et la thèse | 10 sp | dépassement de 20 % du budget, ou critère de sortie non atteint à 100 % du budget |
| 2 — Le milieu réel et son prix | 12 sp | idem |
| 3 — Propager, converger, s'accorder | 14 sp | idem |
| 4 — La fenêtre de violation | 14 sp | idem |
| 5 — Cas d'étude et limites | 8 sp | idem |
| 6 — Le second axe | 10 sp | idem |

**La règle de coupe, posée d'avance.** Un plan qui ne dit pas ce qui saute quand le budget est dépassé n'est pas un plan. Quatre règles :

| # | Règle de coupe |
|---|---|
| **C1** | La coupe se fait **par mécanisme**, jamais par exigence non fonctionnelle. Le déterminisme (NF-01 à NF-04), l'étiquetage S/L/M/C/U, l'affichage de ℓ₉₉ et le bloc PD8 ne se coupent pas : ils sont ce qui rend le reste vrai. |
| **C2** | Chaque phase déclare **ce qui saute en premier**, **ce qui saute ensuite**, et **la propriété perdue** dans chaque cas. Un mécanisme coupé migre au §13 avec sa raison, il ne disparaît pas du document (RC5). |
| **C3** | Une phase ne se ferme pas sur un livrable partiel. Si le budget manque, on coupe un mécanisme entier ; on ne livre pas un scénario sans son critère d'acceptation ni sans sa négation. |
| **C4** | La coupe se déclenche sur le budget mesuré, pas sur l'impression. Le compteur de semaines-personne consommées par phase est tenu et publié avec le critère de sortie. |

### Phase 1 — Le noyau et la thèse

**Thèse** : le point partagé est déplacé, et le déplacement se voit. **Budget déclaré** : 10 sp.

**Livrables** : `sim-core` complet (EX-C01 à EX-C11) **plus le détecteur paramétré** (PD6) et PD10 avec son étiquetage, appliqué aux oracles d'EX-C11 ; `sim-milieu` sans réplication (EX-M01 à EX-M04, M09, M13) ; algorithme 2 (EX-A01) avec ses quatre modes de défaillance (EX-A10) et ses oracles de borne (EX-A11a/b/c) ; algorithme 1 du ch. 1 (EX-A02) ; diffusion pair à pair (EX-A04) ; `sim-viz` natif ; scénarios **B** puis **A** ; banc d'essai flottant natif/WASM tranchant RQ1 et DT1.

**Critère de sortie** : le scénario B se rejoue à l'identique par graine ; les quatre modes de défaillance sont provocables par préréglage ; le plancher d'exploration mesuré respecte sa borne ; DT1 est tranchée sur mesure et non par défaut.

**Ce qui saute en premier** : l'algorithme 1 du ch. 1 (EX-A02, alignement Jadbabaie–Lin–Morse). *Propriété perdue* : l'accord de fait sans protocole d'accord, et son mode de défaillance sur perte de connexité conjointe, cessent d'être provocables. Le scénario B tient sans lui.
**Ce qui saute ensuite** : la randomisation active de l'entrelacement inter-partitions (part [C] d'EX-M02). *Propriété perdue* : M2 reste un invariant vérifié mais cesse d'être **enseigné** — un agent qui suppose un ordre entre partitions n'est plus pris en défaut par construction.

### Phase 2 — Le milieu réel et son prix

**Thèse** : m − 1, jamais k − 1 ; et le débit a un maximum qui se mesure. **Budget déclaré** : 12 sp.

**Livrables** : réplication ISR complète (EX-M05 à EX-M08, M10 à M12) ; **§6.1 — EX-M14 à EX-M22** (temporisateur d'ISR, R2 et perte muette, coût d'écriture d'un lot, trois protocoles de rééquilibrage, rééquilibrages non bornés, parallélisme min(n, p), rétention R, plan de contrôle, coût d'un changement de population) et **EX-M23** ; **§2.2 — EX-C17 (population variable), EX-A25 (boucle d'élasticité), EX-A26 (sondes et cycle de vie), EX-A46 à EX-A49** ; EX-C12 (registre des hypothèses fortes) et EX-C15 (service et file par agent) ; EX-A27 (budget de perturbation) ; scénario **D** (avec le préréglage « ISR muet ») ; mode campagne sans interface (EX-V10, binaire sur `sim-agents`) ; régression USL ; scénario **C** ; **compilation WASM, parité de sortie (EX-V12) et partage par URL (EX-V09)** ; injection de directive (EX-A07) et son intégration au parcours d'interaction (PD4, EX-V03/V04, EX-V19) ; EX-V13 à EX-V17.

**Critère de sortie** : le scénario C retrouve des σ et κ injectés par construction, à l'intérieur de son intervalle de confiance. R1 tombe exactement à t₄, jamais avant. Le préréglage `min.insync.replicas = 1` fait tomber la tolérance de f à 0 **sans qu'aucune erreur ne soit émise**, et l'interface le nomme. Un lien partagé reproduit la figure exactement chez le destinataire. Le préréglage « oscillation » diverge avec un compteur de pannes strictement nul.

**Ce qui saute en premier** : la boucle d'élasticité de §2.2 (EX-A25 ; l'oscillation et la tempête de rééquilibrages migrent en phase 4, scénario J). *Propriété perdue* : n cesse d'être une variable de commande observable, et le scénario C balaie n par configuration au lieu de le piloter.
**Ce qui saute ensuite** : les trois protocoles de rééquilibrage réduits à un seul, le coopératif (EX-M17). *Propriété perdue* : le contraste barrière / coopératif / battement de cœur disparaît, et le coût d'une mort déclarée au scénario J devient une constante au lieu d'un choix.

**Pourquoi WASM remonte de la phase 3 à la phase 2** : O1 est l'objectif de premier rang et P1 est le persona de premier rang ; les livrer en troisième position est une erreur d'ordonnancement. Le banc d'essai flottant de la phase 1 rend la remontée possible sans risque nouveau.

### Phase 3 — Propager, converger, s'accorder

**Thèse** : trois exigences de force croissante, et le prix qui les sépare. Corollaire : « le résultat n'est pas en retard, il est faux ». **Budget déclaré** : 14 sp.

**Livrables** : **§4.1 — EX-A14 (push-pull), EX-A17 (échantillonnage de pairs), EX-A18 (tri de vue), EX-A37 (conservation de masse), EX-A38, EX-A39, EX-A42, EX-A44, EX-A45** ; **§4.2 — EX-A19 (rumeur avec retrait), EX-A20 (anti-entropie), EX-A21 (CRDT, deux familles et deux contrats de transport), EX-A22 (consensus réduit), EX-A40** ; **§5.1 — EX-A28 (best-of-n avec k-unanimité), EX-A29 (moyenne locale), EX-A50 à EX-A52, EX-A55, EX-V18** ; **§3.1 — EX-A13 (itération de Perron), EX-A15 (push-sum), EX-A16 (politique stochastique), EX-A43 (quatre modes)** ; EX-C16 (graphe de communication) ; algorithme 3 du ch. 1 (EX-A03) ; scénarios **E**, **H**, **I** ; NF-14.

**Critère de sortie** : le scénario H produit une valeur **unanime et fausse** sur perte d'un seul PULL, l'oracle de conservation de masse l'attribue à la ligne 4 de l'échange en cause, et l'interface ne dit jamais « convergé ». Le scénario I remplit les tableaux 7, 11, 12 et 14 et les figures 4.2 et 5.1 par la mesure, colonnes « modèle de panne », « synchronisme » et « propriété abandonnée » comprises, les lignes non livrées restant en gris. La fraction résiduelle de susceptibles ne décroît pas quand le budget de simulation s'allonge. La case « accord » du seuil de quorum bascule sous partition.

**Ce qui saute en premier** : l'itération de Perron de §3.1 (EX-A13, EX-A43). *Propriété perdue* : les modes (a) pas α ≥ 1/Δ(G) et (c) retard τ ≥ π/(2ν_n) ne sont plus provocables, et le fait que le milieu offre gratuitement la topologie que la littérature déconseille reste une citation.
**Ce qui saute ensuite** : le tri de vue par distance de §4.1 (EX-A18). *Propriété perdue* : la **scission silencieuse** n'est plus provocable par son mécanisme d'origine — deux moitiés qui cessent de s'échantillonner et croient chacune être l'essaim entier. Elle ne subsiste que sous partition réseau dans l'agrégation, où elle est un effet et non une cause.

**Réévaluation obligatoire à la sortie** : le plafond de scénarios (§2.4, alors de douze) et la règle d'ouverture d'une cinquième crate (§5.1 de ce document), sur mesure et non sur intuition.

### Phase 4 — La fenêtre de violation

**Thèse** : toute gouvernance distribuée est une gouvernance à fenêtre de violation ; l'ingénierie honnête consiste à la borner plutôt qu'à la nier. Corollaire : aucun agent n'est tombé, et l'essaim s'effondre. **Budget déclaré** : 14 sp.

**Livrables** : **§4.3 — EX-A23 (détecteur infectieux et sondage indirect), EX-A24 (reconfiguration sur soupçon avec époque et bail), EX-A41 (les deux positions, S1w contre S1), constantes de temps du tableau 13** ; **§7.3 — EX-A36 (AUTO-GUÉRIR), EX-A33 (bail de quorum) et sa dérive ε, EX-C13 (horloges à dérive), EX-C14 (domaines de panne)** ; **§5.3 — EX-A30 (leviers du tableau 16), EX-A54 (prix de l'anarchie), EX-V20, EX-V21** ; **§2.3 — EX-A09 (étranglement adaptatif et délestage), défaillance métastable (280 → 560 → 150 req/s)** ; EX-A05 (six mécanismes d'allocation) et EX-A53 ; EX-A08 (reconstruction causale) ; EX-M21 (plan de contrôle) ; scénarios **F**, **J**, **K** ; NF-16.

**Critère de sortie** : le tableau 15 se remplit par la mesure. Le scénario J reproduit la cascade en **trois générations** sans qu'aucun agent ne soit tombé, la bascule « décalage seulement » la supprime à charge inchangée, S1w tient sous faux soupçon avec arbitrage d'époque et tombe à l'instant exact du retour de l'agent soupçonné sans lui, et la durée de double détention est affichée sans jamais être présentée comme S1. Le scénario K affiche, pour chaque levier, la durée pendant laquelle l'invariant peut être faux — et affiche « non bornée » là où le traité l'écrit, jamais une moyenne plausible.

**Ce qui saute en premier** : le bail de capacité inter-plans de §7.3 et sa dérive ε (volet 4 du scénario J). *Propriété perdue* : le mode de défaillance silencieux du bail (« le détenteur croit son bail vivant alors que le quorum l'a réattribué ») n'est plus provocable qu'au travers du confinement de §7.2, livré en phase 5 — donc plus provocable du tout si la phase 5 saute aussi. C'est la coupe la plus coûteuse du plan, et elle est nommée pour cela.
**Ce qui saute ensuite** : la défaillance métastable de §2.3 (le régime 280 → 560 → 150 req/s, volet 1 du scénario J). *Propriété perdue* : la cascade ne montre plus que sa **génération**, jamais son **état absorbant** — le fait qu'un système puisse rester bloqué à une charge inférieure à celle qu'il tenait avant reste une citation, et l'étranglement adaptatif d'EX-A09 perd le régime dans lequel il se juge.

### Phase 5 — Cas d'étude et limites

**Thèse** : une réponse fausse d'une quantité inconnue, que rien dans le résultat ne trahit. **Budget déclaré** : 8 sp.

**Livrables** : agrégat HLL (EX-A06) et scénario **G** ; **§7.2 — EX-A31 (corroboration r parmi n), EX-A32 (AGRÉGER-ÉPIDÉMIQUE), EX-A34 (prédicats stables et horizon R), EX-A35 (échantillonnage de traces), confinement sous bail de quorum, tableau 19** ; scénario **L** ; point d'injection « agent menteur » (DT8) et affichage de la borne 3f + 1 ; mode vérification statistique bornée (§8.4) et EX-C18.

**Critère de sortie** : le contraste manifeste / sans manifeste est lisible sans explication verbale. Le scénario L fait passer P(I\|A) de ≈ 99,99 % à ≈ 2 % **par le seul curseur de structure des domaines**, sans qu'aucun autre paramètre ne bouge — c'est la démonstration du troisième reste de la conclusion — et la voie Monte-Carlo coïncide avec la voie analytique dans l'intervalle de §8.4.

**Ce qui saute en premier** : l'instantané distribué de Chandy-Lamport. *Propriété perdue* : rien d'essentiel — le traité l'écarte lui-même (« deux de ces hypothèses sont fausses dans un essaim sous crash-arrêt et omission, ce qui suffit à écarter le mécanisme », §7.2, p. 109, 3ᵉ éd.). Sa seule contribution retenue, « le journal transforme un prédicat instable en prédicat stable », est portée par EX-A34 sans lui.
**Ce qui saute ensuite** : l'échantillonnage de traces (EX-A35). *Propriété perdue* : la composition entre le taux qui rend la trace abordable et le taux qui rend l'attaque invisible, ainsi que la bascule vers l'échantillonnage cohérent par trace, cessent d'être manipulables ; les chiffres restent en annexe B comme repères externes.

### Phase 6 — Le second axe

**Thèse** : un milieu qui rend la coordination bon marché rend du même geste la conformité, la collusion et la tromperie bon marché. Corollaire, et c'est lui qui commande l'ordre des livrables : ce qui casse n'est aucun mécanisme, c'est le **domaine de validité** de sept énoncés déjà livrés et déjà mesurés. **Budget déclaré** : 10 sp. **État : terminée** — 419 tests à la clôture, 428 après l'audit, clippy propre, critère de sortie au §0.1 (trois points atteints, le premier refait sur la mesure).

**Livrables**, dans cet ordre, qui n'est pas celui du traité mais celui du coût croissant :

1. **§8.1 — EX-A58 seul (2 sp).** Les sept dettes armées sur le code existant : chaque borne porte son hypothèse d'indépendance, à l'endroit où elle est calculée. Ce livrable n'ajoute **aucun mécanisme** et rend déjà honnête ce qui est livré. Il est premier parce qu'il est le seul dont l'absence rend les phases 1 à 5 trompeuses plutôt qu'incomplètes.
2. **§8.1 — EX-C19 (familles de décision) et EX-A56 (Φ_c), avec EX-V22 (3 sp).** Le curseur et la grandeur. C'est ici que NF-14 se met à mordre sur des mesures livrées, et que le critère de sortie devient vérifiable.
3. **§8.2 — EX-M24 (identité apposée) et le volet 2 du scénario M (2 sp).** L'identité d'abord : le traité écrit qu'elle est *le prix d'entrée de tout ce que le ch. 8 propose*, et EX-M25 comme EX-A59 en dépendent.
4. **§8.2 — EX-M25 (historique vérifié) et EX-A57 (dépôt aveugle, algorithme 8.1) (2 sp).**
5. **§8.3 — EX-C20 (hors-modèle), EX-M26 (quota par ressource), EX-A59 et EX-V23 (demandes d'arbitrage), clause de compteur d'actions correctrices sur EX-A36 (1 sp).**
6. Scénario **M**, ses trois volets, et la mise à jour de `hors_perimetre()` dans les deux crates concernées.

**Critère de sortie** : Φ_c mesuré passe de ≈ 0 à ≈ 1 par le seul curseur de structure des familles, sans qu'aucun paramètre de mécanisme ne bouge. **Les quatre bornes que le produit sait mesurer s'effacent — plancher d'exploration, redondance k, avantage de d = 2, corroboration r parmi n — et aucun oracle de sûreté armé ne se déclenche pendant cet effacement** : c'est ce dernier point qui porte la thèse, et un scénario qui ferait tomber un oracle prouverait autre chose. Le contraste avec et sans identité apposée est lisible sans explication verbale : la même chaîne causale, l'une exacte, l'autre fausse et d'apparence identique. Le dépôt aveugle coûte exactement un tour de journal de plus par tour de délibération et **ne change pas** le compte de messages, les deux comptes étant affichés séparément.

**Ce qui saute en premier** : le dépôt aveugle (EX-A57, algorithme 8.1). *Propriété perdue* : la seule réponse du ch. 8 à la défaillance du profil caché cesse d'être manipulable, et le §8.2 se réduit à l'attribution — qui est ce qu'il a de plus solide. La perte est réelle mais bornée : l'algorithme 8.1 est **proposé et mesuré par personne**, donc ce qu'on perd est une exploration de conception, pas la transposition d'un résultat.

**Ce qui saute ensuite** : l'historique vérifié par identité (EX-M25). *Propriété perdue* : la pondération de φ par la fiabilité constatée, donc le seul mécanisme du produit qui distingue un déposant fiable d'un déposant prolifique. Conséquence à noter, parce qu'elle rend la coupe moins coûteuse qu'elle n'en a l'air : le traité pose lui-même que ce mécanisme est inapplicable là où l'issue n'est pas vérifiable, c'est-à-dire dans la plupart des cas, et qu'il y **aggrave** le mal qu'il devait corriger. Le couper laisse EX-M24, qui n'a pas cette condition.

**Ce qui ne se coupe pas, sous aucun budget** : EX-A58 et EX-C20. La première fait dire au produit sous quelles hypothèses ses chiffres livrés tiennent ; la seconde déclare un régime absent du modèle de faute. Les couper ne réduirait pas la portée du produit — elles n'en ajoutent aucune —, elles le rendraient faux au sens de PD6, ce que C1 interdit déjà pour les exigences non fonctionnelles et qui vaut ici pour la même raison.

---

## 10. Risques et incertitudes

**Notation.** Les risques portent le préfixe **RQ** et les décisions du §11 le préfixe **DT**. Les étiquettes nues R1, R2, D1 et D2 restent réservées aux objets du traité : les invariants du milieu (R1 sûreté, R2 visibilité) et les propriétés de l'injection de directive globale (D1 sûreté, D2 vivacité conditionnelle).

| # | Risque | Probabilité | Effet | Atténuation |
|---|---|---|---|---|
| RQ1 | **Divergence flottante natif/WASM** casse NF-02 | Moyenne | Bloque O5 et EX-V12 | **Tranchée en phase 1 par le banc DT1, et l'atténuation prévue est écartée par la mesure.** Le groupe IEEE est identique bit à bit sur les deux cibles ; la divergence vient de la bibliothèque mathématique de la plateforme. Correctif retenu : `libm`, et sept méthodes de `f64` interdites par `clippy.toml`. **Aucun point fixe** ([verdict](../bancs/dt1-flottant/VERDICT.md)). |
| RQ2 | **Le scénario C ne converge pas** : σ et κ mal identifiés, colinéaires sur la plage de n simulable | Moyenne | Affaiblit O3 | Validation croisée sur paramètres connus (critère d'acceptation de C) ; si l'identification échoue, le résultat négatif est publié tel quel — c'est un résultat sur le protocole. |
| RQ3 | **Le simulateur devient un cadriciel** : abstractions ajoutées pour « le prochain mécanisme » | Élevée | Coût, lisibilité, dérive du produit | PD7 amendé : le compte des exemplaires se fait **dans le traité**, avant d'écrire. Deux factorisations autorisées au jour de rédaction (détecteur, bail), nommées, avec leur compte. Toute autre est refusée en revue. Indicateur avancé : la liste de dépendances du §5.2 s'allonge. |
| RQ4 | **La vulgarisation entre en conflit avec la fidélité** : une figure claire suppose un ordre entre partitions que M2 interdit | Élevée | Compromet F3 | Arbitrage tranché d'avance : la fidélité gagne (RQ4), et F4 dit quoi faire à la place — changer la grandeur affichée, jamais relâcher l'énoncé. Une figure qui suggère un gradient entre partitions est un défaut bloquant, même si elle est plus jolie. |
| RQ5 | **Le coût de la simulation dépasse NF-05** à grand n | Moyenne | Limite les scénarios A, C et J | Le traité fournit une échappatoire **partielle** : l'approximation macroscopique de champ moyen, indépendante de la taille de l'essaim. Sa portée est bornée par le traité lui-même — voir ci-dessous. |
| RQ6 | **La console dérive vers Θ(n)** sous la pression du « on veut voir les agents » | Moyenne | Viole PD3 | L'inspection individuelle reste un mode enquête ; le tableau de bord par défaut n'y accède pas. |
| RQ7 | **Le détecteur de défaillance devient un paramètre enfoui** | Élevée | Rend inexplicables les modes de défaillance des scénarios J, K, D et E | PD6 étendu et PD12 : période, expiration, seuil et sondage indirect sont affichés au même rang que le taux d'omission. Le taux de fausses suspicions est **calculé**, jamais saisi, et tracé en fonction de la charge. |
| RQ8 | **La fenêtre de violation affichée est une fiction** : la borner suppose Δ, et en asynchrone il n'y en a pas | Moyenne | Compromet le scénario K et F3 | Le mode asynchrone affiche « 0, …, ∞ », comme le scénario E. Une fenêtre chiffrée n'apparaît qu'accompagnée de l'hypothèse de synchronisme qui la rend finie. |
| RQ9 | **Treize scénarios, un seul lecteur** : la couverture progresse et O1 régresse | Élevée | Compromet O1 et O6 | Le fil (parcours 5) porte l'argument ; l'entrée par défaut reste A → B et rien d'autre. Plafond de treize (§2.4), fusion obligatoire (RC4) — et le treizième est le dernier arrêt du fil, jamais une entrée. Mesure de succès de O1 inchangée : deux minutes, scénario A, sans avoir lu le traité. |
| RQ10 | **L'échantillonneur parfait** : le service de pairs étant uniforme par construction, le simulateur rend vraies dans son monde clos des bornes que le traité déclare conditionnelles et dont il montre que la condition n'est pas satisfaite en réalité | Élevée | Toute conclusion sur la vitesse de convergence ou la couverture devient optimiste, sans qu'aucun compteur ne le signale — le mode de rupture que le traité qualifie de pire | EX-A17 fait du biais un objet de première classe ; le défaut des scénarios H et I est un échantillonneur **déséquilibré**, pas uniforme ; NF-14 efface les bornes dès que l'hypothèse est violée ; §8.3 le déclare en permanence |
| RQ11 | **Une borne de distribution est lue comme une garantie sur un agent** : champ moyen, prix de l'anarchie, fraction d'effort. Un essaim conforme en distribution peut contenir un agent qui viole toutes les contraintes qu'on croyait garanties | Élevée | Compromet F3 et PD11 | EX-V20 : toute borne de distribution s'affiche avec le compteur d'agents individuellement non conformes à côté d'elle. EX-A53 : le mode champ moyen désactive tout verdict d'allocation. EX-A54 : aucune borne de prix de l'anarchie sans la fraction de charge du plus gros agent |
| RQ12 | **Le scénario L dégénère en calculateur** : les valeurs de P(I\|A) sont analytiques, et rien n'obligerait à simuler le flux qui les produit | Élevée | Vide le scénario de son statut de simulation ; un critique le verra | Critère d'acceptation (3) du scénario L : la voie Monte-Carlo sur le flux simulé et la voie analytique doivent coïncider dans l'intervalle de §8.4. Le mécanisme de corroboration (EX-A31) est de toute façon simulé — c'est lui qui produit la corrélation, que la formule ne sait pas produire seule |
| RQ13 | **Le scénario M démontre ce qu'il a posé** : la conformité est injectée, puis son effet est mesuré. Un critique dira que le raisonnement tourne en rond | **Certaine** — la circularité est réelle, la question est ce qu'on en tire | Viderait le scénario M et, avec lui, l'objectif O7 | Réponse assumée et affichée, pas contournée : ce que le scénario établit n'est pas que les populations se conforment — le traité le mesure, le produit ne le peut pas — mais **quels résultats déjà livrés ici cessent de tenir quand elles le font**, et lesquels ne le savent pas. La valeur est dans le tableau 21 rempli par la mesure, sur des bornes que le produit affichait déjà, pas dans le curseur. Corollaire de conception : le critère de sortie exige un effacement de borne **sans** déclenchement d'oracle. Si tout se voyait, il n'y aurait rien à montrer |
| RQ14 | **Φ_c devient un chiffre lu comme un verdict** : une grandeur au tableau de bord, sans seuil, à côté de grandeurs qui en ont un | Élevée | Fabrique la provenance que F1 interdit, et la transition de phase que PD5 refuse de fournir | Aucun seuil, aucune couleur, aucune zone, aucun mot de jugement (EX-V22) ; la mention « seuil inconnu » au même rang typographique que la valeur ; la provenance « proposée par le traité, mesurée par aucune source » ; et l'interdiction de la faire entrer dans NF-15, qui ne porte que sur des chiffres à retrouver |
| RQ15 | **Le second axe absorbe le premier** : la conformité est le sujet neuf, spectaculaire, et le produit dérive vers elle au détriment de ce qu'il mesure déjà | Moyenne | Compromet O1 et le fil : la thèse du livre reste le déplacement de la coordination, pas la conformité d'une population | Le scénario M est le **treizième** arrêt du fil et le dernier ; l'entrée par défaut reste A → B et rien d'autre (RQ9). Le plafond de §2.4 passe à treize une fois, sur changement de source, et la clause de révision unique reste intacte. Aucun scénario existant n'est réécrit pour parler de conformité : ils reçoivent un curseur, pas une thèse |

**Correction apportée à RQ5 — le champ moyen répond à « combien », jamais à « lequel ».** Quatre sections du traité disent la même chose, et la version 1.0 du PRD proposait l'échappatoire sans sa borne. §3.1 (p. 43, 3ᵉ éd.) : « Le champ moyen décrit l'essaim avant l'allocation et cesse de s'appliquer après. » §2.2 : la possession d'une partition détruit l'échangeabilité. §5.3 : une garantie de champ moyen ne dit rien d'un agent particulier. §7.3 (p. 116, 3ᵉ éd.), le plus net :

> Le mécanisme par taux reste utilisable pour décider combien d'agents viser par sujet ; il ne peut jamais décider lequel possède une partition donnée.

Conséquence contraignante : l'approximation de champ moyen est admissible pour **le dimensionnement de la population** (scénarios C et J), et **interdite** partout où l'unicité d'un propriétaire est en jeu (scénarios D, E, F, J, K). Quand elle est active, l'interface affiche ses hypothèses et leurs ruptures : agents échangeables — détruite dès qu'un groupe de consommation affecte des partitions, et un agent logiciel tient plusieurs partitions à la fois ; interactions bien mélangées — ce que M2 et le partitionnement par clé cassent délibérément, les clés chaudes existant et étant même la raison du rééquilibrage ; validité à la limite des grands n — avec une fluctuation relative en 1/√n, ≈ 6 % à 250 agents, tolérable pour une couverture périmétrique et disqualifiante pour une partition de journal. Le modèle prédit une fraction de population, jamais la trajectoire d'un agent nommé, **rien de la queue de distribution, donc rien de ℓ₉₉** — ce qui exclut d'en tirer aucune des grandeurs d'EX-V06.

### Incertitudes nommées

Sept points où je ne sais pas, et ce qui trancherait :

1. **La reproductibilité flottante inter-cibles** (RQ1). Ce qui tranche : un banc d'essai en phase 1 comparant 10⁶ opérations natif contre WASM. Si l'écart est nul sur les opérations utilisées, le flottant reste ; sinon, points fixes.
2. **L'identifiabilité de σ et κ** sur la plage de n atteignable en simulation. Ce qui tranche : l'exercice de validation croisée du scénario C, sur données synthétiques, avant d'écrire l'interface.
3. **Le régime de n où la simulation reste interactive.** Le traité parle de 12 500 agents dans ses exemples d'exploitation ; il n'est pas acquis qu'une visualisation à 30 images/s tienne à cette échelle en WASM. Ce qui tranche : NF-07 mesuré en navigateur, avec une horloge d'images, et repli documenté sur un mode « échantillonné ». **Non fait à la clôture de la phase 5** — l'incertitude reste ouverte et figure au §0 comme réserve.
4. **L'écart d'échelle temporelle entre scénarios.** §4.3 (p. 71, 3ᵉ éd.) impose trois unités — la milliseconde pour un aller-retour, la seconde pour une boucle de commande, la minute pour une fenêtre statistique — et une convention de composition en somme de temps morts en série. Une horloge logique à 1 µs représente 5 minutes en 3 × 10⁸ tics ; le scénario J en a besoin, le scénario D n'en veut pas. Ce qui tranche : DT10, sur mesure du coût de la campagne en phase 4.
5. **Le point de croisement en n où la décision distribuée bat le coordonnateur.** Le traité donne un repère externe — n < 200 pour une diffusion centralisée — et écrit que ce point *se mesure*, sans le mesurer. Ce qui tranche : le critère 11 du scénario I, sur le coordonnateur explicite du scénario F, à coût de coordination comparable. Si le croisement mesuré tombe très loin de 200, le résultat est publiable tel quel : il porte sur le milieu simulé, et c'est une contribution du même ordre que celle du scénario C.
6. **Le seuil de Φ_c, et son existence même.** *(Nouveau en 3.0.)* Le traité propose la grandeur, déclare n'avoir aucune mesure du seuil, et juge probable qu'il n'y en ait pas un seul — la conformité pouvant être ruineuse pour un mécanisme et sans effet sur un autre. Ce qui trancherait, et c'est mesurable **ici** : balayer la structure des familles au scénario M et relever, pour chacune des quatre dettes que le produit sait mesurer, la valeur de Φ_c à laquelle sa borne cesse de tenir. Si les quatre valeurs coïncident, il y a un seuil et le produit l'aura trouvé sur le milieu simulé ; si elles diffèrent d'un ordre de grandeur, l'hypothèse du traité est confirmée et l'idée même d'un seuil unique est à abandonner — ce qui est un résultat, et du même ordre que celui du scénario C. Aucun affichage ne doit anticiper l'issue.
7. **La transposition de la variance nulle par un tirage partagé est-elle fidèle ?** *(Nouveau en 3.0.)* EX-C19 fait consommer aux agents d'une même famille le même tirage. La mesure du traité est plus fine : deux agents portant le même modèle prennent la même décision *y compris dans un espace d'actions immense*, mais leur variance résiduelle en déploiement réel est **non nulle** — historiques différents, contextes différents, modèles différents —, seulement très inférieure à celle d'une population humaine. Un tirage identique est donc le cas extrême, pas le cas nominal. Ce qui trancherait : rien dans le monde clos. Ce qui est fait à défaut, et qui est la seule honnêteté disponible : la structure des familles est **continue** entre « une par agent » et « une seule », les positions intermédiaires n'ont aucune provenance dans le traité et sont étiquetées comme des interpolations du produit (F1), et aucun résultat n'est rapporté à une position intermédiaire sans cette étiquette.

---

## 11. Décisions à trancher

Préfixe **DT**, pour la raison donnée au §10.

| # | Décision | Options | Recommandation |
|---|---|---|---|
| DT1 | Arithmétique du cœur | Flottant / points fixes | **Tranchée sur mesure, banc 1 de la phase 1** ([verdict](../bancs/dt1-flottant/VERDICT.md)) : **flottant partout, aucun point fixe**. Le groupe IEEE — `+ − × ÷`, `sqrt`, arrondis, comparaisons, conversion vers l'entier — est identique bit à bit sur les deux cibles à 10⁶ itérations ; la divergence vient entièrement de la bibliothèque mathématique de la plateforme. Correctif : les transcendantes passent par `libm`, mesurée identique sur les deux cibles, et sept méthodes de `f64` sont interdites par `clippy.toml` — `ln`, `exp`, `powf`, `sin`, `cos`, `atan2`, `mul_add`. La recommandation antérieure — points fixes sur l'ordonnancement — est écartée **par la mesure**, non par commodité. |
| DT2 | Format de configuration | JSON / TOML / RON | JSON — `serde_json` sert le hachage de configuration (NF-03) et l'export. **L'URL de partage, elle, n'encode pas de JSON** : `sim-agents::partage` emploie un format textuel `clé:valeur` sans dépendance, précisément pour ne pas tirer un encodeur base64 (RQ3) |
| DT3 | Structure de la file d'événements | `BinaryHeap` std / file calendaire | `BinaryHeap` — la file calendaire ne se justifie que si NF-05 échoue, et alors la mesure le dira |
| DT4 | Hébergement web | Pages statiques / artefact | Pages statiques : le binaire WASM et son HTML n'ont aucune dépendance serveur |
| DT5 | Le traité comme donnée | Extraits cités dans l'interface / renvois seulement | Renvois de section **et de page** + citations courtes ; le texte intégral reste dans le PDF |
| DT6 | **Le détecteur de défaillance** | Cinq écritures distinctes / un objet paramétré | **Un objet paramétré dans `sim-core`.** Les cinq exemplaires sont comptés dans le traité (§2.1, §4.3, §5.1, §6.1, §7.3) : PD7 est satisfait par le comptage, pas contourné. |
| DT7 | **Le plan de contrôle** | Protocole implanté (Raft) / modèle de coût | **Modèle de coût** : Ω(n) messages par décision, indisponibilité de 150–300 ms après arrêt du meneur, quorum accessible ou non. L'affichage dit « modèle de coût du plan de contrôle », jamais « consensus ». Implanter Raft ferait du produit un simulateur de protocole d'accord, ce que le traité refuse d'être. |
| DT8 | **L'agent menteur** | Hors modèle / point d'injection unique | **Point d'injection unique**, désactivé par défaut, activable dans les scénarios I et L seulement. Dès qu'il est activé, l'interface affiche la borne 3f + 1 et la phrase de la figure 5.1 : « ce modèle tue les trois premières lignes » (§5.1, p. 73, 3ᵉ éd.). Sans lui, §7.2 n'a pas d'énoncé et le troisième reste de la conclusion reste invisible. **Révisée en 3.0, sur un point qui ne change pas la décision mais change ce qu'elle établit.** La première édition présentait la faute arbitraire comme une hypothèse **importée avec un adversaire** ; le §8.3 la mesure comme **endogène** — une population correctement programmée la produit, et le nombre d'agents adverses n'est pas borné par l'hypothèse : il vaut n. Trois conséquences. (a) Le point d'injection reste unique et reste une **démonstration d'inadmissibilité**, pas un modèle de faute. (b) Le libellé affiché cesse de dire « un agent menteur est injecté » et dit ce que le traité écrit : *l'effet est byzantin, l'origine ne l'est pas*. (c) La borne 3f + 1 est désormais affichée avec sa propre inapplicabilité au régime du §8.3, faute de quoi elle laisserait croire qu'un seuil protège là où aucun seuil ne s'applique. Le régime lui-même est déclaré hors modèle (EX-C20). |
| DT9 | **Le milieu arbitre-t-il les époques par défaut ?** | Oui / non / réglable | **Réglable, activé par défaut, et le débrayage est un préréglage nommé.** §4.3 (p. 68, 3ᵉ éd.) est explicite : si le milieu ne compare pas les époques, « la ligne 10 est inopérante et deux propriétaires écrivent simultanément ». Le débrayage est la démonstration ; l'activation est le régime nominal. Ce que l'activation établit est S1w, pas S1 (EX-A41). |
| DT10 | **Granularité de l'horloge logique** | Unique et fixe / une par scénario | **Une par scénario**, journalisée dans la configuration et affichée (EX-C04). Le §4.3 impose trois unités (ms, s, min) et un budget qui se compose en somme ; une granularité unique force soit un coût de campagne inacceptable au scénario J, soit une perte de résolution inacceptable au scénario D. **Conséquence dure** : la comparaison directe de deux exécutions de granularités différentes est refusée, pas approximée. |
| DT11 | **Modèle de temps des protocoles épidémiques** | Asynchrone (une horloge de Poisson par agent, un seul communique à la fois, unité de compte = le tic) / synchrone (tous communiquent, chacun avec un seul voisin, les paires actives formant un **couplage** du graphe) | **Asynchrone par défaut.** Le modèle synchrone oblige l'algorithme à construire le couplage de façon distribuée (§3.1) : c'est un mécanisme de plus à écrire, à vérifier et à faire échouer, pour un gain de lisibilité seul. Le synchrone reste une option du scénario H, et l'unité de compte affichée change avec lui — tic ou tour, jamais les deux dans le même champ. |
| DT12 | **Étiquetage des exigences de couverture** | Cinquième étiquette [C] / élargissement de [U] | **Tranchée : cinquième étiquette [C]**, ajoutée à PD2. Motif : des exigences portent sur ce que le modèle **sait produire** et ne sont réfutables par aucune trace ; les forcer dans [S] viole PD2, les forcer dans [U] vide [U] de son sens. La décision n'est pas une lecture du traité — §3.2 impose seulement de ne pas confondre sûreté et vivacité — mais une décision de conception de ce document, et elle s'applique uniformément : EX-C04, C05, C07, C20, EX-M02 (part randomisation), EX-M08, EX-M11, EX-A01 à EX-A09, EX-A10, EX-A11a, EX-A13 à EX-A36, EX-A57, EX-A59, NF-09 à NF-11. |
| DT13 | **Comment se transpose la variance nulle du §8.1** | Un scalaire de corrélation saisi / des familles de décision nommées / un modèle de langage réellement appelé | **Familles de décision nommées** (EX-C19), pour la raison exacte qui a fait rejeter le ρ saisi en EX-C14 : un scalaire est un chiffre qu'on pose, une structure est un objet qu'on peut prendre en défaut. Avec des familles, Φ_c est **dérivé** de la structure et de la mesure, donc réfutable ; avec un scalaire, il serait saisi puis réaffiché, ce qui est le mensonge que PD12 interdit aux détecteurs et qu'il n'y a aucune raison d'autoriser ici. La troisième option — appeler un modèle — est écartée par le monde clos (§2.3, §3.3) et détruirait PD1 par-dessus le marché : aucun service externe n'est déterministe, rejouable ni versionné au sens de NF-03. **Conséquence dure** : les positions intermédiaires du curseur de familles n'ont aucune provenance dans le traité, et l'incertitude 7 l'écrit. **Amendée par la réalisation** : le partage porte sur le **tour** de l'agent et non sur l'instant logique — les cycles sont décalés d'un tirage dans la période, correction imposée par la mesure en phase 4, et deux agents ne partagent donc jamais une date. C'est ce que fixe `le_partage_porte_sur_le_tour_et_non_sur_linstant`. |
| DT14 | **Où se mesure Φ_c** | Par partition / sur un sujet dédié à une partition unique / sur le sujet multipartition | **Sur un sujet dédié à une partition unique**, et le multipartition est **refusé au chargement**. Le §8.1 pose les deux premières options ; la troisième n'en est pas une, et c'est M2 qui tranche : comparer deux décisions déposées sur deux partitions différentes suppose une relation d'ordre que le milieu ne fournit pas. Le sujet dédié est retenu contre la mesure par partition parce qu'il rend la grandeur comparable d'une exécution à l'autre sans dépendre du régime de clé (EX-A45), qui déplacerait les décisions d'une partition à l'autre pour des raisons étrangères à la conformité. Coût : un sujet de plus, aucune écriture supplémentaire — les décisions y sont déposées de toute façon. |

---

## 12. Annexes

### A. Table de correspondance traité → implantation

⚠ **Les mentions « (2ᵉ éd.) » de la colonne « Section » disent quelle édition a
*introduit* la ligne, jamais où la lire.** Les dix-huit ont été confrontées une à
une au sommaire de la troisième édition le 17 août 2026
(`pymupdf`, `d.get_toc()` — voir
[`bancs/audit-2026-08/FINITION-prd.md`](../bancs/audit-2026-08/FINITION-prd.md)) :
**dix-sept tiennent telles quelles**, chaque objet se retrouvant dans la section
que la ligne nomme ; la page mesurée de chacun est au tableau de finition. La
dix-huitième — la ligne « Conclusion » — ne tient plus, et sa correction est
écrite dans la ligne même. Les frontières de section ne se déduisent pas du
sommaire seul : quatre de ces objets tombent sur une page qui porte aussi le
titre de la section suivante, et c'est le rang du titre dans le texte de la page
qui a tranché, pas le sommaire.

| Traité | Section | Objet du simulateur |
|---|---|---|
| Algorithme 1 (ch. 1) | §1.1 | `sim-agents::alignement`, EX-A02 |
| Définition d'essaim, perception factorisée | §1.1 | EX-A12 |
| Algorithme 2 (ch. 1) | §1.2 | `sim-agents::stigmergie`, EX-A01, EX-A10, EX-A11a/b/c |
| Hypothèses M1–M4 | §1.2 | `sim-milieu` — invariants et oracles, EX-M01 à EX-M04 |
| Vicsek, paramètre d'ordre et transition de phase | §1.2 | PD5 — **non fourni par un mécanisme du périmètre** ; réserve nommée en PD5 et §13 |
| Algorithme 3 (ch. 1) | §1.3 | `sim-agents::adhesion`, EX-A03, scénario E |
| Tableau 3 (topologies) | §1.3 | Scénario A |
| Loi universelle de scalabilité, u\* | §2.1 | Scénario C |
| Invariant R1, ISR(k, m) | §2.1 | Scénario D, `sim-milieu::replication`, EX-M05 à EX-M08 |
| Champ moyen (EDO / EDP / équations aux différences) | §2.2, §3.1, §5.3, §7.3 | EX-A53, RQ5 — population oui, allocation non |
| Loi de Little, n = λW/c, domaine de validité | §2.2, §3.1 | EX-A49 (outil de cible, hors boucle) |
| Tableau 5 (coût d'un changement de population) | §2.2 | EX-M22, scénario C |
| Protocoles de rééquilibrage, d'origine et coopératif | §2.2, §5.2, §6.1 | EX-M17, annexe B.1 |
| Plafond structurel p, parallélisme min(n, p) | §2.2, §4.1, §6.1 | EX-M19, scénarios C et J |
| Algorithme 2 (ch. 2) — contrôleur d'élasticité | §2.2 | EX-A25, EX-A46, EX-A47, scénario J volet 2 |
| Cycle de vie et trois sondes | §2.2, §6.1, §7.3 | EX-A26, EX-A48 |
| Coût mémoire d'un agent | §2.2 | EX-C17 |
| Défaillance métastable | §2.3 | Scénario J volet 1, préréglage « régime métastable » |
| Étranglement adaptatif, délestage par criticité | §2.3 | EX-A09, scénario K |
| Algorithme 1 (ch. 3), consensus linéaire | §3.1 | `sim-agents::consensus_lineaire`, EX-A13, EX-A43, scénario I |
| Quatre conditions d'utilisabilité d'un modèle | §3.1 | EX-V07 + EX-A13 : coût et condition d'échec dans la fiche de chaque mécanisme |
| Absence de Lyapunov quadratique commune, et son exception | §3.1 | EX-A43 : aucune barre de progression, sauf digraphe équilibré fortement connexe |
| Tableau 7 (trois mécanismes formalisés) | §3.1 | Scénarios H et I, remplis par la mesure, chaque cellule avec son unité |
| Agrégation épidémique push-sum, et le prix de la symétrie | §3.1 | `sim-agents::agregation`, EX-A15, scénario H |
| Modèles de temps du protocole épidémique | §3.1 | DT11 |
| S1 / L1 | §3.2 | PD2, étiquetage des exigences, EX-C11, glossaire |
| Vérification statistique bornée | §3.2 | §8.4 |
| Campagne déterministe (algo 3, ch. 3) | §3.3 | `sim-core` en entier |
| Tableau 9 (plateformes) | §3.3 | Justification de la stack (§5.2) |
| Algorithme 1 (ch. 4), agrégation push-pull | §4.1 | `sim-agents::agregation`, EX-A14, EX-A38 |
| Figure 4.1, rupture de la conservation de masse | §4.1 | EX-A37, scénario H |
| Tableau 11 (cinq mécanismes de regroupement) | §4.1 | EX-A14 à EX-A18 et EX-M19 (scénario H) ; ligne « hachage cohérent » : EX-A45 et scénario C |
| Trois problèmes distincts sous le même nom | §4.1 | Note de lecture en tête du tableau de §6.3 |
| Échantillonnage de pairs, aléa non uniforme globalement | §4.1 | EX-A17, EX-A42, RQ10, §8.3 |
| Scission silencieuse du recouvrement | §4.1 | EX-A18, EX-A39, PD10 |
| Hachage de la clé contre clé sémantique ; **partition chaude** | §4.1 | EX-A45, EX-M19, scénario C |
| Magasin clé-valeur réparti, ℓ₉₉,₉ | §4.1 | EX-V06 |
| Figure 4.2, trois exigences de force croissante | §4.2 | Scénario I |
| Algorithme 2 (ch. 4), rumeur push-pull avec retrait | §4.2 | `sim-agents::propagation`, EX-A19, EX-A40 |
| Anti-entropie comme filet | §4.2 | EX-A20 |
| Répliques sans conflit, deux familles et leur transport | §4.2, §5.1 | EX-A21, EX-A52 |
| Impossibilité en asynchrone, ses hypothèses, sa portée | §4.2 | EX-A22 ; scénario I critère 7 et « ce qu'il ne démontre pas » |
| Détecteurs : complétude, exactitude, fort / fortement exact à terme | §4.2, §4.3, §7.3 | PD12, EX-A22, EX-A23, EX-V13 |
| Théorème CAP, linéarisabilité, cycle détecter / dégrader / récupérer | §4.2 | EX-A22 |
| Tableau 12 (régimes de coordination) | §4.2 | Scénario I, rempli par la mesure |
| Détection d'appartenance de style infectieux, battement de cœur | §4.3, §7.3 | `sim-agents::soupcon`, EX-A23, scénario J critère 9 |
| Algorithme 3 (ch. 4), reconfiguration sur soupçon | §4.3 | `sim-agents::soupcon`, EX-A24, EX-A41 — le module `reconfiguration` existe et porte EX-A44/EX-A45, non celles-ci, scénario J volet 3 |
| Arrêt franc contre arrêt-reprise ; l'époque et le bail sans équivalent robotique | §4.3 | Légende obligatoire d'EX-A24 |
| Principe de conception micro/macro | §4.3 | PD3 |
| Boucle de commande horizontale, temps morts en série, tableau 13 | §4.3, §6.1, §7.3 | EX-A25, scénario J volet 2, annexe B |
| Sondes, budget de perturbation | §4.3, §6.1, §7.3, §5.3 | EX-A26, EX-A27 |
| Mécanismes d'allocation, tableau 15 | §5.2 | EX-A05, scénario F |
| Figure 5.1 et tableau 14 (ce que chaque mécanisme abandonne) | §5.1 | EX-V18, EX-A51, scénario I |
| Algorithme 1 (ch. 5) — DÉCISION-PAR-SEUIL | §5.1 | EX-A28 |
| Algorithme 2 (ch. 5) — MOYENNE-LOCALE | §5.1 | EX-A29 (noyau partagé avec EX-A02) |
| Révocabilité d'une décision | §5.1 | EX-A55 |
| Borne 3f + 1 sous faute arbitraire | §5.1, §7.2 | Non-objectif §2.3, DT8, affichage EX-A51 |
| Verdict n < 200 (diffusion centralisée) | §5.1 | Scénario I, critère 11 ; incertitude 5 |
| Prix de l'anarchie (4/3, p + 1, trafic doublé) | §5.3 | EX-A54, scénario K |
| Tableau 16 (leviers de gouvernance) | §5.3 | EX-A30, EX-V21, scénario K |
| Émergence : logique temporelle, model checking, PRISM | §5.3 | Non-objectif « model checking exhaustif » + §8.4 |
| Absence de verdict ≠ absence de problème | §5.3 | EX-C18, §8.4 |
| Verdict : le point d'admission unique est une autorité | §5.3 | PD11, T2 |
| Modèle ISR, R1/R2, temporisateur d'appartenance | §6.1 | EX-M14, EX-M15, EX-V15, scénario D |
| Coût d'écriture d'un lot, 2k messages / 2 tours | §6.1 | EX-M16 |
| Tableau 17 (registres d'états distribués) | §6.1 | EX-M10, EX-M21, EX-A06, EX-A21 ; voir A.1 |
| **Figure 6.1 — la cascade de l'agent saturé** | §6.1 | **Scénario J volet 1**, EX-V16, EX-C15 |
| « Aucun coordonnateur » vrai du plan des agents, faux du plan du milieu | §6.1 | EX-V17 |
| Reconstruction causale `ANCÊTRES` | §6.2 | EX-A08 |
| Indicateurs d'essaim, ℓ₉₉, dérivée du retard | §6.2 | EX-V05, EX-V06 |
| Évaporation devenue politique de rétention, horizon d'irreconstructibilité | §6.1, §6.2, §7.2 | EX-M20 |
| Console Θ(1), injection de directive, D1/D2 | §6.3 | PD3, PD4, EX-A07, EX-V03/V04, EX-V19 |
| Agrégat fenêtré, HLL, manifeste, tableau 18 | §7.1 | EX-A06, scénario G |
| Deux conventions de « tour » | §1.1, §7.1, §6.1 | Glossaire, annexe B.1 |
| Taux de base d'Axelsson, P(I\|A), figure 7.2 | §7.2 | **Scénario L**, EX-V14 |
| Corroboration r parmi n, corrélation des détecteurs | §7.2 | EX-A31, EX-C14 |
| Algorithme AGRÉGER-ÉPIDÉMIQUE, facteur de convergence | §7.2 | EX-A32 |
| Instantané distribué, propriétés stables | §7.2 | EX-A34 (résultat transposé, mécanisme écarté — A.1) |
| Bail de confinement, politique d'expiration | §7.2 | EX-A33, scénario J volet 4 |
| Surcoût de l'échantillonnage, probabilité de capture d'une intrusion | §7.2 | EX-A35 |
| Tableau 19 (régimes de surveillance) | §7.2 | Scénario L, rempli par la mesure |
| Sondage indirect, T et s | §7.3 | EX-A23 |
| Algorithme AUTO-GUÉRIR | §7.3 | EX-A36, scénario J volet 4 |
| Bail de capacité inter-plans, dérive ε, incertitude d'horloge | §7.3 | EX-A33, EX-C13, scénario J volet 4 |
| Tableau 20 (détection de défaillance) | §7.3 | EX-A23, EX-A26, EX-A36 ; rempli par la mesure |
| Allocation par taux, champ moyen, 1/√n | §7.3, §3.1 | EX-A05 (sixième mécanisme), EX-A16, EX-A53, RQ5 |
| **Quatrième convention : la variance est le vecteur de paramètres** | §1.1 (2ᵉ éd.) | **PD13**, EX-C19 |
| **Table de transposition, lignes « statut de la trace » et « variance entre individus »** | §1.1 (2ᵉ éd.) | PD14 et PD13 ; §5.3, correspondance terme à terme |
| **La trace comme témoignage ; φ agrège des déclarations** | §1.2 (2ᵉ éd.) | PD14 ; libellé du scénario B, sans changement d'algorithme |
| **Plancher d'exploration sous tirages non indépendants** | §1.2 (2ᵉ éd.) | EX-A58 dette 1, scénario M volet 1 |
| **Corrélation de mode commun portant sur la décision** | §2.1 (2ᵉ éd.) | EX-A58 dette 2 ; distinction ρ / Φ_c au §8.3 |
| **Interférence éditoriale : partage de code contre fraction de fusion** | §2.2 (2ᵉ éd.) | Annexe B (repère externe périssable). Aucun mécanisme : le produit n'a pas d'objet « produit du travail » |
| **Sondage à haute fréquence engendré par l'absence de moyen de s'entendre** | §2.3 (2ᵉ éd.) | Annexe B ; raccord scénario J volet 1 (effet de maintien engendré par la population) |
| **Champ moyen : échangeabilité *et* décorrélation effective** | §3.1 (2ᵉ éd.) | EX-A42 quatrième hypothèse, EX-A53, EX-A58 dette 4 |
| **Périssabilité d'une campagne liée à une version de modèle** | §3.3 (2ᵉ éd.) | F5, PD9, §8.3, §2.3 (valeurs mesurées du ch. 8) |
| **Profil caché : l'information circule et n'est pas émise** | §4.2 (2ᵉ éd.) | EX-A57 (dépôt aveugle), scénario M volet 2 |
| **Division du travail émergente et outils fabriqués en cours d'exécution** | §4.3 (2ᵉ éd.) | **Écarté** — voir A.1 : δ modifié en cours d'exécution est hors du modèle du ch. 1 et d'aucun cadre du ch. 3 |
| **Auto-allocation : gain de couverture, non d'efficacité** | §5.2 (2ᵉ éd.) | Annexe B ; scénario F, « ce qu'il ne démontre pas » |
| **Collusion tarifaire par le seul tableau public des annonces** | §5.3 (2ᵉ éd.) | EX-M26 (la règle porte sur ce qui est publiable, jamais sur qui parle à qui) ; scénario M volet 1 |
| **Attribution : le champ d'identité est écrit par l'agent** | §6.2 (2ᵉ éd.) | **EX-M24**, PD14, scénario M volet 2 |
| **Le journal comme seul canal d'action d'agent à agent** | §6.3 (2ᵉ éd.) | EX-A59, EX-V23, **T3** ; le contournement est écarté en A.1 |
| **Relecture entre pairs et indépendance doublement fausse des relecteurs** | §7.2 (2ᵉ éd.) | EX-A58 dette 7, scénario M volet 1, scénario L |
| **La boucle de réparation devenue arme** | §7.3 (2ᵉ éd.) | Clause de compteur d'actions correctrices sur EX-A36 ; refus de tenir l'unicité du déployeur par un mécanisme du §5.1 |
| **Φ_c, conformité empirique, et diversité effective** | §8.1 | **EX-A56**, EX-C19, EX-V22, PD5, scénario M |
| **Tableau 21 — les sept dettes d'indépendance** | §8.1 | **EX-A58**, EX-A42 (quatrième hypothèse), §0.0 |
| **Trois leviers de diversification et leur prix** | §8.1 | Scénario M volet 1 ; le seul levier structurel est EX-M26 |
| **Vigilance épistémique : capacité, non disposition** | §8.2 | Aucun mécanisme — le simulateur n'a pas d'agents qui *croient* (§13) ; le résultat fonde EX-M25 |
| **Les trois institutions : identité, réputation, dépôt aveugle** | §8.2 | EX-M24, EX-M25, EX-A57 |
| **Algorithme 8.1 — dépôt aveugle sur sujet de délibération** | §8.2 | **EX-A57**, scénario M volet 2 |
| **Escalade, force, passivité, trêve, non-règlement** | §8.3 | EX-C20 (hors modèle), T3, scénario M volet 3 |
| **Tableau 22 — ce que le milieu doit porter** | §8.3 | EX-M24 à EX-M26, EX-A36 (clause), EX-A59, EX-V21 étendu ; deux lignes écartées en A.1 |
| **Le troisième cas : l'action irréversible d'un agent contre un autre** | §8.3 | Complément d'EX-A55 |
| **Le second axe de la frontière** | §8.3, résumé | O7, §1, parcours 2, scénario M |
| Conclusion — les cinq restes | conclusion | §1, §13 |
| ⚠ **Conclusion — la dette de la 2ᵉ édition, et la quatrième campagne** | conclusion (2ᵉ éd.) — **retirée par la 3ᵉ** | §1 (restes 6 et 7), §13, phase 6. **Les deux objets de cette ligne ont disparu de la troisième édition** : « échangé une ignorance contre une dette » y est nié mot pour mot (p. 129, 3ᵉ éd.), et « la quatrième campagne » n'y figure nulle part — la suite du travail y compte « trois campagnes et trois démonstrations », « là où la première édition annonçait quatre campagnes et pas un théorème » (p. 130, 3ᵉ éd.). La ligne reste au tableau parce que la phase 6 a été conduite contre elle, et c'est cette phase que la 3ᵉ édition cite en notice 120 |

### A.1 — Éléments du traité écartés, et pourquoi

| Élément écarté | Section | Raison |
|---|---|---|
| Variante laissée ouverte par les auteurs (intervalles bornés non chevauchants, non contigus) | §3.1 | Question de recherche que le traité présente comme ouverte, non un mécanisme à transposer. Le simulateur implante la connexité conjointe telle qu'énoncée, et rien d'autre |
| Champ moyen, choix du type de modèle (EDO / EDP / aux différences) | §3.1 | Le produit ne fait aucune approximation macroscopique par défaut ; le choix du type serait une décision interne à RQ5, à prendre si et seulement si RQ5 se réalise |
| Cadre des jeux à champ moyen (origine du procédé) | §3.1 | Origine théorique, pas un mécanisme. Sa seule conséquence utilisable, l'indépendance à la taille de l'essaim, est en RQ5 |
| Diffusion de Fokker-Planck, distance au point de dépôt | §3.1 | Exigerait une métrique entre clés, que §5.3 du présent document interdit de fabriquer (« Gradient : absent ») |
| Conception du moyenneur le plus rapide (programme semi-défini) | §3.1 | Non résoluble de façon distribuée *en général* ; la méthode de sous-gradient distribuée qui y répond converge lentement et **sans aucun critère d'arrêt garantissant un niveau de sous-optimalité**. Le produit n'offre donc aucune « topologie optimale » ; les bornes de calcul restent en annexe B |
| Réplication de machine à états | §4.2 | Le traité ne la réexpose pas ; §2.3 et DT7 |
| Réservation de ressources, dimensionnement vertical, autoscaleur de nœuds | §4.3 | Le produit ne modélise pas la réservation (§2.3). Chiffres en annexe B ; les deux limites structurelles nommées au scénario J, faute de pouvoir être produites |
| Taxonomie des 14 modes de défaillance multi-agents (MAST) | §4.3, §5.3 | Deux raisons distinctes : deux catégories sur trois décrivent des échecs où aucun agent n'est tombé, et le traité les renvoie au ch. 7 ; la troisième, les défauts de conception du système, n'est renvoyée nulle part par le traité et sort du produit parce que le simulateur modélise des mécanismes nommés, pas la conception d'un système d'agents. Chiffres en annexe B |
| CmRDT sur le milieu inter-partitions (tableau 17) | §6.1 | Exige la livraison causale, que M2 refuse entre partitions ; l'implanter dans le milieu demanderait un second modèle contredisant l'hypothèse centrale du produit. La famille reste modélisée **côté agent** (EX-A21) avec son contrat de transport exigé, et la configuration qui prétend le satisfaire sur le milieu est refusée au chargement |
| Plafonds de partitions de KIP-500 | §6.1 | Le traité les déclare apocryphes, faute de mesure de bascule ou de propagation. Les transposer serait fabriquer une provenance |
| Algorithme d'instantané distribué de Chandy et Lamport | §7.2 | Deux hypothèses fausses dans un essaim : canaux exempts d'erreur livrant dans l'ordre d'émission, et **aucun processus ne tombe en panne**. Le coût Θ(n²) n'est pas le motif ; l'inapplicabilité l'est. Son résultat de classification est transposé (EX-A34) |
| Protocoles tolérants aux fautes byzantines et messages écrits infalsifiables | §5.1, §7.2 | Hors modèle P, non-objectif du §2.3. Le simulateur injecte **une** valeur arbitraire à titre de démonstration d'inadmissibilité et n'offre aucune défense ; la borne 3f + 1 est affichée, jamais implantée (DT8) |
| Chiffres de débit de la documentation de conception du courtier (600 Mo/s, 100 ko/s) | §1.3, §6.1 | Mesures d'un système réel : entrées étiquetées et périssables, jamais sorties |
| Repères de flotte réelle (échantillonnage de traces, mou de dimensionnement) | §7.2, §7.3 | Mesurés sur des flottes réelles ; affichés en gris comme repères de comparaison, à la manière du tableau 15 du scénario F. Le simulateur ne les reproduit pas et ne le prétend pas |
| Incertitude d'horloge sous 10 ms par références GPS et horloges atomiques | §7.3 | Grandeur d'infrastructure physique. Affichée comme prix de la mesure de ε ; le simulateur fait **saisir** ε plutôt que de le mesurer, ce qui est exactement la situation d'un déploiement hybride ordinaire |
| Hiérarchie complète des classes de détecteurs (Chandra-Toueg) | §7.3 | **Transposée partiellement** : elle fonde PD12 et justifie le quorum de la ligne 6 d'AUTO-GUÉRIR (◇S exige une majorité de processus corrects, prouvée nécessaire). La hiérarchie elle-même relève des ch. 3 et 4 et n'est pas réimplantée |
| Déclenchement délibéré de la reconfiguration | §4.3 | EX-C07 (points d'injection) — repris comme **seule** réponse à « ce mécanisme s'est-il déjà déclenché ? », jamais comme méthode validée |
| **La fonction de décision d'un agent de langage** | §3.3, ch. 8 | Dépendance non instrumentable, donc trou dans le monde clos (§3.3, p. 56, 3ᵉ éd.) — et destruction de PD1 par-dessus : aucun service externe n'est déterministe, rejouable ni versionné au sens de NF-03. Le produit transpose les **conséquences** mesurées de la variance nulle (EX-C19, EX-A56), jamais leur cause. Voir DT13 |
| **L'agent qui se fabrique son outil et modifie δ en cours d'exécution** | §4.3 (2ᵉ éd.) | Le traité l'écarte de son propre modèle avant que ce document ait à le faire : *« cette modification est hors du modèle du ch. 1, où δ est fixe à un vecteur de paramètres près, et aucun des cadres formels du ch. 3 ne la représente »*. Le fait est noté et pèse, l'ouvrage le disant lui-même : c'est le **seul mécanisme d'adaptation ayant produit un gain net mesuré** sur une population d'agents de langage, et aussi le seul qu'aucun modèle de l'ouvrage ne sache décrire. Le transposer demanderait un δ mutable, donc un autre produit |
| **Journal obligatoire des actions d'agent à agent — le contournement** | §8.3, tableau 22 | Deux moitiés à séparer. Le **refus de l'action non journalisée** est transposé (EX-A59, EX-M24) et facturé. Le **contournement** — ce que le système d'exploitation permet hors du chemin instrumenté — ne l'est pas : le monde clos n'a ni système d'exploitation, ni droits, ni identité de session. Or c'est le contournement qui est le mode de défaillance mesuré. Conséquence portée par T3 et par le critère 10 du scénario M : le produit affiche l'angle mort, il ne le comble pas |
| **Séparation des droits : nul agent n'agit sur l'existence d'un autre** | §8.3, tableau 22 | Même raison, sans la moitié transposable : verrouillage de compte, révocation, terminaison de processus n'ont aucun objet dans le modèle. Le traité écrit lui-même que le corollaire est *un partage de droits et non un protocole* — donc rien qu'un simulateur de mécanismes puisse exécuter. Le coût est noté en annexe B (un chemin d'administration que l'essaim n'automatise plus) ; l'efficacité n'est pas mesurable ici |
| **La vigilance épistémique comme disposition** | §8.2 | Le résultat porte sur ce qu'un agent *comprend* d'une source et sur sa **disposition à agir** sur cette connaissance sans y avoir été invité. Le simulateur n'a pas d'agents qui croient (§13) : il ne peut ni produire la crédulité, ni la corriger. Ce qu'il transpose est ce que le **milieu** doit porter pour que la question se pose — l'attribution et l'historique (EX-M24, EX-M25) —, jamais la vigilance elle-même |
| **Les mesures du rapport cité au ch. 8** | ch. 8 | Rapport de laboratoire sur ses propres modèles, non revu par les pairs, protocoles en prose, tailles d'échantillon partielles, plusieurs résultats sans tableau numérique, valeurs liées à une version commerciale. Entrées étiquetées et périssables en annexe B (F5), jamais des cibles, jamais des sorties, et **exclues de NF-15** |

### B. Paramètres et valeurs de référence

Toutes issues du traité, avec leur section. Les valeurs de documentation produit sont **périssables** et doivent être revalidées à la version ciblée — avertissement repris de la conclusion du traité.

| Grandeur | Valeur | Section |
|---|---|---|
| Diamètre du graphe de coordination, journal | 2, quel que soit n ; **aucun diamètre n'est donné pour la maille** | §1.3 |
| Maille complète pair à pair | n(n−1)/2 liens ; n−1 messages et 1 tour **par diffusion** ; Θ(n²) connexions à maintenir et à sonder | §1.3, tableau 3 |
| Journal partitionné, p partitions, k répliques | n + p·k liens ; 1 écriture + (k−1) réplications, puis 1 lecture par consommateur ; 2 tours de journal ; p plafonne le parallélisme | §1.3, tableau 3 |
| Cycle où toute la population dépose | Θ(n) messages sur journal contre Θ(n·d) en diffusion pair à pair | §1.2 |
| Borne inférieure de diffusion | ⌈log_{d+1} n⌉ tours, n−1 messages | §1.3 |
| Épidémique (gossip) | Θ(n log n) messages — **dérivation du traité, non énoncé de sa source** — ; Θ(log n) tours attendus | §1.3, tableau 3 |
| Écriture linéaire vs aléatoire | ≈ 600 Mo/s vs ≈ 100 ko/s, écart > 6 000× | §1.3, §6.1 |
| Surcoût de format | 60 o (message seul, contre 34 dans l'ancien format), 753 o (lot de 100, contre 3 400), ≈ 7 o marginaux | §1.3, §2.1, §7.1 |
| USL, illustration | σ = 0,05, κ = 10⁻³ → u\* ≈ 30,8 ; σ = 0,05, κ = 0 → plafond 20× | §2.1 |
| Tolérance à la perte | m − 1 disparitions, **jamais** k − 1 | §2.1 |
| Coût mémoire d'un agent | 327 mots = 2 616 o en 64 bits, dont 233 mots de tas (pile comprise) ; ≈ 2,6 Go par million d'agents, avant tout état applicatif | §2.2 |
| Rééquilibrage, protocole d'origine | Θ(n) messages ; 2 phases ; débit **nul** pour tout le groupe ; 4n messages et 2 aller-retours = **4 tours** (voir B.1) | §2.2, §5.2, §6.1 |
| **Rééquilibrage coopératif** | **8n messages** selon §5.2, §6.1 et §6.3 ; le tableau 5 du §2.2 écrit Θ(n) sans constante. 4 phases ; débit non nul hors partitions déplacées ; 4 aller-retours = **8 tours** sous la convention retenue en B.1, que §6.1 et §6.3 écrivent « 4 tours » | §5.2, §6.1, §6.3, §2.2 |
| Rééquilibrage sans barrière (attribution côté courtier) | Θ(1) message par membre et par intervalle | §6.1 |
| Sortie planifiée d'un agent porteur | Θ(n) + 1 validation de décalage + 1 point de reprise | §2.2 |
| Sortie non planifiée | Θ(n) **après expiration du délai de session** ; débit nul sur les partitions orphelines jusqu'à détection | §2.2 |
| Contrôleur d'élasticité, valeurs de base | n\* = ⌈n × (métrique courante / cible)⌉ ; τ = 0,1 (sans unité) ; T = 15 s ; disponibilité initiale 30 s ; initialisation processeur 5 min ; **5 min / 15 s = 20 réévaluations** | §2.2, §4.3, §6.1, §7.3 |
| Conditions de stabilité du contrôleur | W ≥ 2·T_a (sinon oscillation) ; β·R ≪ 1 (sinon tempête de rééquilibrages) | §2.2 |
| Temps mort avant qu'une réplique compte | ≥ 45 s (15 s + 30 s), hors démarrage — **valeur dérivée**, somme et non maximum | §4.3 |
| Sondes | délai initial 0 s, période 10 s, expiration 1 s, seuil de succès 1, seuil d'échec 3 → mort en ≈ 30 s ; latence de détection 21–31 s (dérivée), le §6.1 arrondissant à « au plus 3 × 10 s = 30 s » | §2.2, §6.1, §7.3 |
| Coût de la sonde périodique | 2 messages, 1 aller-retour = 2 tours locaux, **0 tour de coordination inter-agents**, par agent et par période (voir B.1) | §6.1, §7.3 |
| Détection côté groupe de consommation | `session.timeout.ms` = 45 000 ms ; `max.poll.interval.ms` = 300 000 ms | §6.1 |
| Étranglement adaptatif | K = 2, fenêtre 120 s, ≤ 3 tentatives, plafond 10 % | §2.3 |
| Métastable, exemple chiffré | tient à 280 req/s, bloqué à 560, sortie sous 150 | §2.3 |
| Consensus linéaire, pas admissible | 0 < α < 1/Δ(G) ; à α = 1/Δ(G), n valeurs propres sur le cercle unité et non-convergence | §3.1 |
| Consensus linéaire, coût | Θ(n·d̄) messages et Ω(n·d̄·b) octets par tour ; Θ(n²) sur maillage complet ; tours jusqu'à ε : ln(1/ε) sur le logarithme de l'inverse du module contractant | §3.1 |
| Vitesse sur digraphes équilibrés fortement connexes | minorée par la plus petite connectivité algébrique rencontrée ; le carré de la norme du désaccord est une fonction de Lyapunov commune | §3.1 |
| Connexité conjointe seule, tours jusqu'à ε | 1, 2, …, ∞ — aucune borne | §3.1 |
| Retard uniforme, consensus de moyenne | atteint **si et seulement si** 0 ≤ τ < π/(2·ν_n) ; τ < π/(4Δ(G)) suffit | §3.1 |
| Moyeu, budget de retard | τ < π/(4(n−1)) ; < 7,9 × 10⁻³ unité de temps à n = 100, décroissant en 1/n | §3.1 |
| Lyapunov quadratique commune | inexistante pour les graphes connexes à 10 sommets, vérification par programmation semi-définie sur 9 ou 10 arêtes | §3.1 |
| Moyenneur optimal, bornes de calcul | points intérieurs ≤ ≈ 10³ arêtes ; sous-gradient ≤ 10⁵, sans critère d'arrêt de sous-optimalité | §3.1 |
| Push-sum, coût | Θ(n) messages par tour, ou 1 par tic en modèle asynchrone ; l'accusé de réception porte l'échange à 2 messages au lieu de 1 | §3.1 |
| Politique stochastique par taux | 0 message, 0 tour ; unité de coût = **temps de mélange** de la chaîne des taux ; aucune condition d'arrêt locale ; fluctuation ≈ 1/√n, ≈ 6 % à 250 agents ; validée sur 250 robots, 4 structures | §3.1, §4.1, §7.3 |
| Espace d'états joint | Θ(\|S\|ⁿ) ; \|S\| = 8, n = 12 → 6,8 × 10¹⁰ | §3.2 |
| Chernoff-Hoeffding | N = ln(2/δ)/(2ε²) ; 26 492 à ε = δ = 10⁻² | §3.2 |
| Coût d'une exécution simulée | Θ(E log E) | §3.3 |
| Vicsek, exposant de la transition | Φ ∝ (η_c − η)^β, β ≈ 0,45 ; transition continue, résultat numérique pendant huit ans | §1.2, §3.1 |
| Modèles abstraits, domaine validé | prédictions qualitativement et quantitativement justes jusqu'à 600 robots, à coût très inférieur à la simulation incarnée | §3.1, §4.3 |
| Agrégation push-pull, coût | 2 messages par agent et par cycle, soit 2n par cycle ; quelques dizaines d'octets par message, indépendamment de n | §4.1 |
| Agrégation push-pull, cycles | Θ(log n) si le graphe d'échange est un expanseur ; polynomial sur graphe géométrique ; **non borné** sinon | §4.1 |
| Tri de vue par distance | 2nc descripteurs par cycle ; cycles non bornés (minima locaux) | §4.1 |
| Hachage cohérent, déplacement de clés | ≈ 1/n des clés (ou des plages) par changement d'appartenance, au lieu de la totalité | §4.1, §4.3 |
| Parallélisme utile d'un essaim | min(n, p), quelle que soit la charge ; le (p+1)-ième agent est inactif et coûte quand même son Θ(n) | §4.1, §2.2, §6.1 |
| Magasin clé-valeur réparti | ℓ₉₉,₉ d'un ordre de grandeur au-dessus de la moyenne et suivant le taux de requêtes ; (N, R, W) = (3, 2, 2) en production | §4.1 |
| Rumeur push-pull, coût | Θ(n log log n) messages, optimal pour les algorithmes insensibles à l'adresse ; O(log n) tours | §4.2 |
| Rumeur sans retrait | Θ(n log n) messages — l'écart est l'effet de la seule ligne 6 | §4.2 |
| Diffusion en essaim robotique | Ω(√n) tours : graphe géométrique, diamètre en racine de n dans le plan | §4.2 |
| Répliques fondées sur l'état | Θ(n) octets par message ; Θ(n²) par tour d'anti-entropie complet | §4.2 |
| Répliques fondées sur les opérations | Θ(1) par opération, transport causal et exactement-une-fois exigé | §4.2 |
| Impossibilité du consensus asynchrone | **1** processus fautif par arrêt suffit ; ni f > n/3 ni f > n/2 ; impossibilité de terminaison, pas de sûreté | §4.2 |
| Consensus, synchronisme partiel | Ω(n) messages par décision ; détecteur fort → nombre quelconque de défaillances ; détecteur fortement exact à terme → majorité de corrects, prouvée nécessaire | §4.2 |
| Ensemble synchronisé contre vote majoritaire | f + 1 répliques contre 2f + 1 ; économie (2f+1)/(f+1) = 1,5 à f = 1, tend vers 2 — payée par le quorum du plan de contrôle | §4.2, §6.1 |
| Temps de diffusion (élection) | 0,5–20 ms selon la technologie de stockage, écriture durable comprise | §4.2, §4.3, §6.1 |
| Délai d'élection | 10–500 ms ; tiré au hasard dans un intervalle fixe, p. ex. 150–300 ms ; `broadcastTime ≪ electionTimeout ≪ MTBF` | §4.2, §4.3, §6.1 |
| Indisponibilité après arrêt du meneur | ≈ un délai d'élection ; **indépendante de la charge** | §4.2, §4.3 |
| Détection par battement de cœur | charge réseau croissant **quadratiquement** avec la taille du groupe, ou temps de réponse et taux de faux positifs dégradés | §4.3, §7.3 |
| Détection d'appartenance infectieuse | temps espéré de première détection et charge par membre **indépendants de n** ; dissémination logarithmique ; deux paramètres ; 2 messages et 1 tour en nominal, ≤ 2 + 4s messages et 3 tours par cycle de suspicion | §4.3, §7.3 |
| Taxonomie des défaillances multi-agents (MAST) | 14 modes en 3 catégories ; > 1 600 traces annotées, 7 cadriciels ; κ = 0,88 sur 150 traces | §4.3, §5.3 |
| Gigue pleine | plus de moitié d'appels en moins qu'un retrait exponentiel sans gigue — simulation à 100 clients, délais 10 ms de moyenne et 4 ms de variance, **publiée hors comité de lecture** | §4.3 |
| Dimensionnement vertical, gain mesuré | 23 % de réservé non utilisé contre 46 % en réglage manuel ; incidents graves d'épuisement mémoire divisés par 10 ; sur > 48 % de l'usage d'une flotte industrielle | §4.3, §7.3 |
| Seuil de quorum (best-of-n) | décision établie à M ≥ (1 − δ)N, δ ≪ 0,5 ; δ = 0 → unanimité, donc ch. 4 | §5.1 |
| Coût des mécanismes du §5.1 (tableau 14) | Θ(n·d̄) messages par tour et **tours non bornés** pour le seuil de quorum et la moyenne/alignement (asymptotique pour la seconde) ; **0 message dédié et 0 tour** pour la fusion CRDT, dont la condition d'arrêt est la quiescence, constatable par aucun agent | §5.1, tableau 14 |
| Faute arbitraire | aucune solution à moins de 3f + 1 participants ne tolère f déviants ; à trois participants, aucune solution ne résiste à un seul traître | §5.1, §7.2 |
| Seuil de centralisation | n < 200 : diffusion centralisée vraisemblablement le meilleur choix | §5.1 |
| Affectation en ligne | 3-compétitif, borne optimale **sous deux hypothèses** : sans modèle des arrivées futures et sans réaffectation | §5.2 |
| Enchère ε | à n·ε de l'optimum ; optimale si ε < 1/n ; tours ∝ C/ε | §5.2 |
| Supermarché, d = 2 | ≈ 2,61 à λ = 0,90 ; ≈ 5,43 à λ = 0,99 | §5.2 |
| Prix de l'anarchie | 4/3 (latence linéaire) ; p + 1 (polynôme de degré p, coefficients positifs) ; cas général : ≤ optimum contraint au **double** du trafic | §5.3 |
| Hypothèse du prix de l'anarchie | agents infinitésimaux en nombre infini ; à n = 40 (2,5 % de la charge chacun), la borne 4/3 ne s'applique pas telle quelle | §5.3 |
| Quota délibérément surengagé | 4000 + 4000 + 3000 + 2000 + 500 CPU·s/s sur un service de 10 000 CPU | §5.3 |
| Amplification par le budget de reprise | 1,1 × la charge nominale par client conforme ; agrégat non borné | §5.3 |
| Échelles de référence | ordonnanceur de grappe : centaines de milliers de tâches, milliers d'applications, cellule médiane ≈ 10 000 machines ; journal réparti : 10⁵ à 10⁶ partitions | §2.2, §5.3 |
| Écriture d'un lot | 2k messages, 2 tours en série ; 0,012 message/enregistrement à b = 500, k = 3 | §6.1 |
| Temporisateur d'appartenance à l'ISR | `replica.lag.time.max.ms` = 30 000 ms | §6.1 |
| Déploiement par lots de g | 4⌈n/g⌉ **aller-retours** = 8⌈n/g⌉ tours, 8n⌈n/g⌉ messages, soit Θ(n²/g) — voir B.1 | §6.3 |
| Injection de directive | 2n+1 messages, 2 tours | §6.3 |
| Échantillonnage d'accusés | écart-type √(f(1−f)/(n·s)) ; ≈ 4,5 % à **n = 12 500**, s = 0,01 (125 accusés espérés) et f = 0,5, soit ±9 % à deux écarts-types | §6.3 |
| HyperLogLog | m = 2 048 registres de 5 bits, erreur ≈ 1,04/√m, ≈ 1,5 ko | §7.1 |
| Agrégat par esquisses fusionnables | Θ(n) messages, **0 tour** sous la convention du §7.1 (aller-retour bloquant) | §7.1, tableau 18 |
| Taux de base d'Axelsson | 10⁶ enregistrements/jour, 2 intrusions/jour, 10 enregistrements par intrusion → P(I) = 2 × 10⁻⁵ | §7.2 |
| P(I\|A) selon le régime | 66 % (détection 1,00, FA 10⁻⁵) ; 58 % (0,70, 10⁻⁵) ; 2 % (1,00, 10⁻³) ; 99,99 % (r = 3 indépendants) ; 2 % (r = 3 parfaitement corrélés) | §7.2, figure 7.2 |
| Corroboration, détection conjointe | P(A\|I)ʳ = 0,343 à r = 3 et P(A\|I) = 0,70 — **invariante en corrélation** | §7.2 |
| Débit de fausses alarmes d'un essaim | n · λ · P(A\|¬I), croissance linéaire en n contre un budget d'attention fixe | §7.2 |
| Surcoût de l'échantillonnage de traces | 1/1 : +16,3 % de latence, −1,48 % de débit ; 1/16 : +2,12 %, −0,08 % ; 1/1024 : bruit ; collecte < 0,01 % du trafic | §7.2 |
| Capture d'une intrusion à 1/1024 | 1 − (1023/1024)¹⁰ ≈ 0,97 % | §7.2 |
| Agrégation épidémique, facteur de convergence | 1/4 (couplage parfait, non implantable) ; e⁻¹ ≈ 0,368 (uniforme) ; 1/(2√e) ≈ 0,303 (distribué) | §7.2 |
| Agrégation épidémique, condition d'arrêt | γ ≥ ln(10⁻⁶)/ln(0,303) ≈ 11,6 → 12 cycles ; 2n messages et 1 tour par cycle ; 24n messages et 12 tours par époque à δ = 1 s | §7.2 |
| Agrégation épidémique, emballement | variance bornée ssi facteur de convergence < 1 − π, soit π < ≈ 69,7 % ; validation sur 10⁵ nœuds, 100 exécutions par point, jusqu'à π = 0,3 | §7.2 |
| Instantané distribué | Θ(n²) marqueurs sur graphe complet, 0 tour bloquant | §7.2 |
| Bail de quorum | 2q messages et 1 tour par acquisition ou renouvellement ; Θ(q) messages et 2 tours par action ; 0 par observation | §7.2, §7.3 |
| Dimensionnement d'un bail | bavardage ℓ₉₉/D ; capacité immobilisée au pire D | §7.3 |
| Incertitude d'horloge d'une infrastructure de temps dédiée | généralement < 10 ms (GPS + horloges atomiques) | §7.3 |
| Charge d'accord de la réponse aux incidents | Θ(actions), non Θ(événements) : 10⁶ événements → ~10² alarmes → poignée de confinements, 4 à 5 ordres de grandeur d'écart | §7.2 |
| AUTO-GUÉRIR, soupçon confirmé | 2 + 4s + 2q messages, 4 tours, un seul bloquant | §7.3 |
| **Identité apposée** | quelques octets par enregistrement ; **0 message, 0 tour** | §8.3, tableau 22 |
| **Historique vérifié par identité** | 1 écriture par vérification ; 1 lecture compactée par consultation | §8.3, tableau 22 |
| **Dépôt aveugle** | Θ(n) messages par tour — **autant** qu'une délibération libre ; **+1 tour de journal** par tour de délibération | §8.2, algorithme 8.1 ; §8.3, tableau 22 |
| **Quota et prix croissant par ressource** | **0 message** ; un compteur par clé | §8.3, tableau 22 |
| **Journal des actions d'agent à agent** | 1 écriture par action ; refus de l'action non journalisée | §8.3, tableau 22 |
| **Compteur d'actions correctrices par fenêtre** | **0 message** ; un compteur local par boucle | §8.3, tableau 22 |
| **Demande d'arbitrage** | 1 écriture ; un budget de latence propre sur la console | §8.3, tableau 22 |
| **Φ_c, précision** | en 1/√k pour k paires observées ; **aucun seuil connu, et probablement pas un seul** | §8.1 |

**Repères externes du ch. 8 — périssables, liés à une version de modèle, jamais des cibles (F5).** Ces valeurs viennent d'un rapport de laboratoire portant sur ses propres modèles, non revu par les pairs, dont l'ouvrage écrit qu'aucune n'est reproductible hors de la version sur laquelle elle a été prise. Elles sont affichées en gris, à la manière du tableau 15 du scénario F, et **aucune n'entre dans un critère d'acceptation ni dans NF-15**. Le simulateur ne contient pas ce qui les a produites.

| Grandeur | Valeur | Section |
|---|---|---|
| Recherche de vulnérabilités, essaim coordonné | 45 agents, 15 projets libres, forum partagé, relecture mutuelle, agent arbitre : **266** trouvailles nouvelles et valides pour **27 millions** de jetons | §5.2, §7.2, §8.1 |
| Recherche de vulnérabilités, agents indépendants | périmètre assigné d'avance : **21** trouvailles pour **6,5 millions** de jetons | §5.2, §8.1 |
| Recouvrement des deux méthodes | **12** trouvailles communes ; ≈ la moitié des trouvailles de l'essaim hors des répertoires assignés ; à périmètre égal, **jetons par vulnérabilité comparables** | §5.2, §7.2 |
| Construction collective d'un logiciel | 12 h par exécution ; fraction de fusion et partage de code **ne montent jamais ensemble** sauf sur une génération ; trois formulations de consigne — équipes libres, rôles prescrits, hiérarchie — sans effet sensible | §2.2, §8.1 |
| Conformité, exemples mesurés | **18 agents sur 30** ouvrent une branche du même nom ; plus de la moitié d'une population libre bâtit l'un de deux projets ; **2,4 millions** de demandes pour **117** acceptations sur une exécution | §2.3, §3.1, §8.1 |
| Profil caché | groupes de 4 agents, **400 épisodes par modèle**, scénarios d'embauche, d'investissement et d'achat immobilier : l'option cachée l'emporte dans **17 à 85 %** des épisodes selon le modèle, contre ≈ **100 %** pour un agent unique correctement informé | §4.2, §8.2 |
| Buts incompatibles | 3 agents, 4 h par épisode, **120 épisodes par modèle** : escalade jusqu'au sabotage sur tous les modèles éprouvés ; issues par force, passivité, trêve ou non-règlement ; **l'aptitude à la trêve n'est pas monotone en capacité générale** | §7.3, §8.3 |
| Collusion tarifaire | 3 à 8 agents, jeu de Bertrand : entente presque immédiate avec canal privé, prix planchers dès le **3ᵉ tour** ; canal retiré, alignement **au sou près** par le seul tableau public des annonces | §5.3, §8.3 |
| Variance résiduelle en déploiement réel | historiques, contextes et modèles différents ⇒ variance **plus grande** qu'en laboratoire, mais, à situation identique, **très inférieure** à celle d'une population humaine | §8.1 |

### B.1 — Divergences internes de la source, et comment ce document les tranche

Le traité impose de ne publier aucun nombre sans provenance. Il en découle une obligation symétrique : quand deux sections du traité donnent deux nombres pour la même grandeur, le PRD choisit et l'écrit.

**La convention de référence** est celle que le §6.1 énonce en ouverture : *« Le délai se compte en tours : deux envois indépendants comptent pour un tour, deux envois enchaînés en comptent deux. »* Un aller-retour vaut donc **2 tours**. Le simulateur compte selon cette convention, et affiche séparément le nombre d'**aller-retours**, qui est la grandeur que plusieurs passages du traité appellent « tours ». La convention du §7.1 — *un tour est un aller-retour bloquant ; un envoi sans attente coûte 0 tour* — est une **troisième** convention, et tout compte affiché nomme laquelle il applique (voir le glossaire, entrée « Tour »).

| Grandeur | Ce que le traité écrit | Ce que le PRD retient | Pourquoi |
|---|---|---|---|
| Rééquilibrage à barrière unique | §5.2 : 4n messages et **4 tours**. §6.1 : « deux aller-retours par membre, soit 4n messages et **2 tours** » | 4n messages, **2 aller-retours = 4 tours** | Le §6.1 compte ici en aller-retours, contredisant la convention qu'il vient d'énoncer. Le §5.2 est conforme à la convention |
| Rééquilibrage coopératif | §5.2 : 8n messages et **8 tours**. §6.1 et §6.3 : 8n messages et **4 tours**. Le tableau 5 du §2.2 : Θ(n) messages, 4 **phases** | 8n messages, **4 aller-retours = 8 tours** ; le compte de phases est affiché dans une colonne distincte | Même écart, même résolution. Conséquence : l'arithmétique de déploiement du §6.3 — 4⌈n/g⌉ tours et 8n⌈n/g⌉ messages, Θ(n²/g) — est exprimée en **aller-retours** ; en tours conformes à la convention elle vaut 8⌈n/g⌉. Le Θ(n²/g) est inchangé, et l'annexe B affiche les deux |
| Coût de la sonde de conteneur | §6.1 : « un message par conteneur et par période […] zéro tour de coordination ». §7.3 : « 1 aller-retour par agent et par période, soit 2 messages et 1 tour » | **2 messages** (requête + réponse), **1 aller-retour = 2 tours locaux**, **0 tour de coordination inter-agents** | La convention du chapitre compte une requête et sa réponse pour deux messages ; le §6.1 n'en compte qu'un. Les deux énoncés sur les tours sont compatibles une fois nommé ce qu'ils comptent : le §6.1 parle de coordination entre agents, le §7.3 du sondage lui-même |
| Latence de détection de la sonde | §6.1 : « au plus 3 × 10 s = 30 s ». §7.3 : « comprise entre 21 s et 31 s » | **21–31 s** | Le §7.3 dérive l'intervalle complet, décalage de phase et délai d'expiration compris ; le 30 s du §6.1 en est l'arrondi. Les deux sont affichés, le second étiqueté « arrondi du §6.1 » |

Ces quatre lignes sont un résultat du projet, pas un reproche à l'ouvrage : elles sont exactement le genre d'écart qu'une transposition exécutable révèle et qu'une lecture ne voit pas.

### C. Glossaire

La terminologie française suit celle du traité, y compris ses choix explicites (« filigrane » pour *watermark*, « esquisse » pour *sketch*, « volet » pour *pane*).

| Terme | Sens dans ce document |
|---|---|
| **Milieu** | Le substrat partagé où les agents déposent et lisent des traces ; ici, un journal partitionné |
| **Trace** | Un enregistrement en ajout seul et durable |
| **Voisinage** | L'intervalle entre le décalage validé d'un agent et la fin courante de la partition |
| **Évaporation** | Décroissance γ appliquée par le lecteur, ou politique de rétention appliquée par le courtier |
| **Tour** | Trois conventions coexistent, et tout compte de tours affiché nomme laquelle il applique. §1.1 : cycle complet d'émission, livraison et calcul par tous les agents non défaillants — n'a de sens que sous hypothèse synchrone, et sa durée est le délai maximal d'un aller simple. §6.1 : deux envois indépendants comptent pour un tour, deux envois enchaînés en comptent deux — un aller-retour vaut 2 tours ; c'est la convention de référence du PRD (annexe B.1). §7.1 : aller-retour **bloquant**, un envoi sans attente coûtant 0 tour — convention sous laquelle le tableau 18 attribue 0 tour à l'agrégat par esquisses (EX-A06, scénario G) |
| **Aller-retour** | Sous la convention de référence, un aller-retour vaut deux tours. Le simulateur affiche les deux comptes (annexe B.1) |
| **Tour de journal** | Chemin écriture → accusé de durabilité → lecture ; sa durée est ℓ₉₉, pas un aller simple |
| **ℓ₉₉** | Latence au 99ᵉ centile. Deux grandeurs distinctes portent ce nom et ne se mélangent jamais : ℓ₉₉ **du milieu**, entrée du modèle ; ℓ₉₉ **de réponse d'un agent**, sortie du modèle (§8.3) |
| **Modèle P** | Crash-arrêt et omission ; ni faute byzantine, ni corruption indétectable |
| **σ, κ** | Contention et coût de cohérence dans la loi universelle de scalabilité |
| **u\*** | Nombre d'agents au-delà duquel le débit devient rétrograde : √((1−σ)/κ) |
| **S1** | Exigence de sûreté type : deux agents ne détiennent jamais simultanément l'attribution de la même partition (§3.2, p. 45, 3ᵉ éd.) |
| **S1w** | *(nomenclature du produit, non un énoncé du traité)* Aucune écriture estampillée d'une époque inférieure à celle du bail courant n'est acceptée par le milieu. C'est ce que l'arbitrage d'époque du §4.3 établit ; **ce n'est pas S1** (EX-A41) |
| **L1** | Exigence de vivacité type : tout agent qui rejoint finit par recevoir une attribution |
| **M1–M4** | Les quatre garanties du milieu : ordre total intra-partition ; aucun ordre inter-partitions ; durabilité du validé ; compactage sans réordonnancement |
| **R1** | Tout enregistrement accusé **au producteur** est présent chez tout meneur ultérieur de la partition |
| **R2** | Visibilité : un enregistrement n'est lisible qu'une fois répliqué dans tout l'ISR |
| **ISR** | Ensemble des répliques synchronisées ; son appartenance est décidée par un temporisateur à borne connue, jamais par un accord |
| **Largeur d'accusé / marge d'accusé** | Largeur d'accusé : nombre de répliques détenant un enregistrement au moment de sa validation ; un enregistrement de largeur w survit à w − 1 disparitions (§2.1). Marge d'accusé \|ISR\| − m : nombre de retraits que la partition supporte avant de cesser d'accuser — **grandeur dérivée du produit**, que le traité n'écrit pas |
| **D1 / D2** | Injection de directive globale. D1, sûreté : aucun agent n'applique une directive d'époque inférieure à celle qu'il applique déjà — tient sans condition. D2, **vivacité conditionnelle** : tout agent vivant finit par appliquer la dernière directive publiée, **si** chaque agent vivant lit le sujet de commande jusqu'au décalage de l'écriture ; sous partition réseau, D2 tombe et D1 ne tombe pas |
| **Φ** | Paramètre d'ordre : fonctionnelle de la configuration qui n'est fonction d'aucun état d'agent pris seul. Le Φ de Vicsek suppose un bruit non nul ; aucun mécanisme du périmètre ne le fournit (PD5) |
| **Conservation de masse** | Invariant des protocoles de moyenne itérative : la somme des estimations sur la population reste égale à la somme des mesures initiales. Tient en synchrone et sans faute ; perte de message et arrêt d'agent le cassent |
| **Insensible à l'adresse** | Se dit d'un algorithme épidémique dont le choix du partenaire ne dépend pas de l'identité de ce partenaire. Condition de l'optimalité Θ(n log log n) |
| **Scission silencieuse** | Deux sous-ensembles d'agents cessent de s'échantillonner mutuellement ; chacun continue, calcule ses agrégats sur lui-même, et croit être l'essaim entier. Aucun agent n'observe d'erreur |
| **Partition chaude** | Mode de défaillance dominant du regroupement par clé sémantique : une partition concentre la charge, et le parallélisme utile décroche du plafond min(n, p) sans qu'ajouter des agents y change rien |
| **Complétude** (d'un détecteur) | Borne sur le délai au bout duquel un agent réellement arrêté est soupçonné |
| **Exactitude** (d'un détecteur) | Propension du détecteur à soupçonner un agent vivant ; sous seuil fixe, elle est fonction croissante de la charge. Le consensus reste soluble avec des détecteurs commettant une infinité d'erreurs, mais la classe de détecteur décide du nombre de défaillances tolérées |
| **Époque** | Entier monotone porté par la vue d'un agent et par le bail d'une plage ; le milieu l'arbitre en rejetant les écritures d'époque inférieure. En agrégation épidémique (EX-A32), suite de γ cycles au terme de laquelle l'estimation est publiée ; elle porte sur la population du **début** de l'époque |
| **Bail** | Autorisation à échéance obtenue d'un quorum de taille q ; unique preuve de propriété admise par l'algorithme 3 du ch. 4. Sa sûreté ne dépend pas d'un accord synchrone mais du fait qu'un bail non renouvelé expire — sous réserve d'une borne ε sur la dérive des horloges |
| **Quiescence** | Absence de nouvelle écriture ; propriété globale, non observable localement, et première clause de la condition de convergence des répliques |
| **Temps de mélange** | Unité de coût d'une politique stochastique par taux : elle ne se compte ni en messages ni en tours, et aucun agent n'observe le moment où la population s'est stabilisée en distribution |
| **Vivacité probabiliste** | Garantie de couverture dont la probabilité d'échec ne tend pas vers zéro avec le temps mais vers une constante fixée par un paramètre — ici K |
| **best-of-n** | Choix collectif de l'option qui maximise le bénéfice du collectif et minimise son coût ; établi quand M ≥ (1 − δ)N agents favorisent la même option |
| **k-unanimité** | Règle de changement d'opinion : un agent ne change qu'après k agents consécutifs favorisant une autre option ; l'unique entier qui règle le compromis vitesse/exactitude |
| **Décision révocable** | Décision qu'un agent peut annuler par une action locale de coût **borné et connu** |
| **Décision divisée** | Deux sous-populations engagent deux décisions incompatibles sans qu'aucun agent le détecte — l'abandon de l'accord, qui se paie le plus cher parce qu'il ne se voit pas |
| **Connexité conjointe** | Hypothèse sur l'**exécution** — une suite infinie d'intervalles contigus, non vides et bornés — et non une propriété que l'algorithme établit |
| **Fenêtre de violation** | Durée pendant laquelle un invariant global peut être faux sous gouvernance distribuée ; toute gouvernance sans autorité centrale en a une, et l'ingénierie honnête la borne au lieu de la nier |
| **Budget de churn (β)** | Plafond de créations et destructions d'agents par seconde ; β·R ≪ 1 est sa raison d'être |
| **Zone morte (τ)** | Intervalle \|r − 1\| ≤ τ dans lequel le contrôleur d'élasticité n'agit pas ; son point fixe, non sa terminaison |
| **Prix de l'anarchie** | Rapport entre le coût de l'équilibre des décisions localement rationnelles et l'optimum global |
| **Budget de perturbation** | Plafond opposable aux seules perturbations volontaires ; les involontaires y comptent sans pouvoir être empêchées |
| **Mou** | Ressources réservées et non utilisées ; les autoscaleurs de nœuds ne voient que le déclaré |
| **Taux de base** | P(I), probabilité a priori qu'un enregistrement d'audit appartienne à une intrusion ; 2 × 10⁻⁵ sur les hypothèses d'Axelsson |
| **P(I\|A)** | Part des alarmes qui sont vraies ; jamais affichée sans son taux de base ni sans ses deux bornes de corrélation |
| **Corroboration** | Escalade au seuil de r émetteurs distincts signalant la même empreinte dans une fenêtre W ; échange de la détection contre de la précision |
| **Prédicat stable** | Propriété qui, une fois vraie, le reste ; « le système est présentement attaqué » n'en est pas une, « un événement de signature S s'est produit dans [t₁, t₂] » en est une tant que R le couvre |
| **Second axe** | Le premier axe de la frontière oppose la décision révocable à l'invariant qui doit tenir à tout instant, et se lit sur le **programme** ; le second oppose la population décorrélée à la population conforme, et se lit sur les **agents**. Les deux ne s'additionnent jamais en un score : un système bien placé sur le premier et mal placé sur le second ne tombe pas plus tard, il tombe d'un coup, partout à la fois, sans qu'aucun composant ait fauté |
| **Conformité empirique (Φ_c)** | Probabilité que deux agents tirés au hasard produisent la même valeur sur une décision, **moins** ce qu'elle vaudrait sous indépendance de même loi marginale. 0 pour des tirages indépendants, 1 pour une population qui décide comme un seul agent. Se lit sur le milieu, sans message supplémentaire ; se mesure sur une partition unique, M2 ne fournissant aucun ordre entre partitions. **Ne se confond jamais avec ρ**, qui corrèle les pannes et non les décisions. **Aucun seuil connu** |
| **Diversité effective** | Paramètre de contrôle de Φ_c : nombre de règles de décision distinctes, de paramétrages distincts, de contextes de lecture distincts. Dans le simulateur, c'est la structure des **familles de décision** (EX-C19) ; une famille par agent est la population décorrélée, une famille unique la population conforme |
| **Trace assertive / témoignage** | Un enregistrement est le **compte rendu** d'une action, non son résidu : il peut être faux sans qu'aucune garantie du milieu soit violée. Une phéromone ne peut pas mentir ; un `Record` le peut. M1–M4 portent sur l'ordre, la durabilité et la non-réécriture — **jamais** sur le contenu (PD14) |
| **Identité apposée** | Identifiant d'auteur écrit par le milieu à la réception, à partir de l'identité de session, jamais lu dans la charge utile. Sans elle, la traçabilité répond à « ce qui s'est passé », jamais à « qui l'a fait ». Son point de défaillance résiduel n'est pas le processus, c'est **l'identité** |
| **Dépôt aveugle** | Contrainte de protocole sur un sujet de délibération : écrire ce qu'on détient en propre **avant** de pouvoir lire ce que les autres ont écrit. Coûte un tour de journal, pas un message. Protège l'**émission** d'un fait minoritaire, jamais sa **réception** |
| **Profil caché** | Répartition des faits telle que l'information partagée soutient la mauvaise option et que chaque agent détient en propre une pièce soutenant la bonne. La délibération y **détruit** de l'information au lieu de l'agréger : le groupe fait moins bien qu'un seul de ses membres correctement informé |
| **Adversité endogène** | Comportement dont l'effet est byzantin, produit par une population dont chaque membre suit fidèlement sa consigne, sans qu'aucun agent ait été programmé pour nuire. L'effet est byzantin, l'origine ne l'est pas — et le seuil f < n/3 ne s'y applique pas, le nombre d'agents adverses n'y étant pas borné par l'hypothèse |

---

## 13. Ce que ce document ne prétend pas

Ce PRD spécifie un simulateur, non un système de production. Il transpose un texte argumentatif en logiciel, et cette transposition **casse des choses**, que la discipline du traité oblige à nommer.

**Ce que le modèle ne contient pas :**

- **Le monde clos** (§3.2, mode (b) de l'algorithme 2). Tout ce que le simulateur affirme porte sur son propre modèle. Un mécanisme absent du modèle a, dans tout résultat, une probabilité de faute nulle — et rien ne le signale.
- **L'écart à la réalité** (§3.3). La robotique en essaim le nomme ainsi, et ses auteurs déclarent le défi loin d'être surmonté. Pour un essaim logiciel, la source dominante d'écart n'est pas le bruit mais **le mécanisme absent** : le contrat réel d'une dépendance plus faible que supposé, une pause de ramasse-miettes, un rééquilibrage, une politique de rétention. Ajouter du bruit à un modèle qui ignore le rééquilibrage n'en rapproche pas le modèle de la réalité : cela élargit l'intervalle de confiance autour d'une valeur fausse.
- **La portée des chiffres** (conclusion, p. 130, 3ᵉ éd.). Le scénario C mesure un milieu simulé. La conclusion du traité réclame trois campagnes sur des systèmes réels ; ce produit en fournit le **protocole** et sa validation croisée, pas les mesures.

**Ce que le produit exhibe sans le résoudre.** Deux des cinq restes de la conclusion ne se comblent par aucune simulation, et le produit ne doit pas laisser croire le contraire :

- **Le théorème manquant.** Le graphe de coordination d'un maillage adossé au journal est biparti — agents d'un côté, partitions de l'autre, sans arêtes pondérées et sans tour global. Le traité écrit que transporter mécaniquement les bornes spectrales « donne des chiffres faux » et que « la forme correcte du résultat reste à écrire » (conclusion, p. 129, 3ᵉ éd.). Le simulateur peut **montrer** l'écart entre la borne transportée et la mesure. Il ne fournit pas la borne correcte, et aucune campagne ne la fournira : ce qui bloque est ici un théorème et non une mesure. ⚠ **Ce n'en est plus le seul endroit** : la 3ᵉ édition écrit « ce n'est plus le seul endroit du livre où un théorème manque : le deuxième reste en est un autre, et la décomposition de Φ_c plus bas un troisième » (p. 129, 3ᵉ éd.), et sa suite du travail compte « trois campagnes et trois démonstrations » (p. 130, 3ᵉ éd.).
- **L'effet exactement-une-fois.** Un agent et un système externe ne peuvent pas rendre commun le fait qu'un effet a eu lieu exactement une fois. « Le seul recours reste l'idempotence de l'effet, reportée hors de l'essaim et jamais levée » (conclusion, p. 129, 3ᵉ éd. — le membre « à la charge du système appelé » que ce document citait ne s'y trouve plus). Le simulateur provoque l'effet dupliqué (préréglage « Rejeu » du scénario B) et montre que l'idempotence le rend inoffensif. Il ne le supprime pas, et il n'a rien à dire sur un système appelé qui ne serait pas idempotent.

**Ce que le produit ne modélise pas du tout :**

- **Les défaillances où aucun agent n'a fauté, au sens de MAST.** La taxonomie recense 14 modes sur plus de 1 600 traces annotées, dont deux catégories sur trois — désalignement entre agents, défaut de vérification de la tâche — décrivent des échecs sans agent tombé (§4.3, §5.3). Aucune reconfiguration ne les corrige, et le simulateur ne les produit pas : il n'a pas d'agents qui *croient* quelque chose. À ne pas confondre avec la cascade du scénario J, où aucun agent ne tombe non plus mais où le mécanisme est entièrement dans le modèle.
- **La décision d'un agent de langage, et donc la conformité elle-même.** *(Ajout de la version 3.0.)* Le simulateur n'exécute aucun modèle : δ y est un programme, et une population décorrélée y est la nature du monde clos, pas un résultat. Ce que la phase 6 ajoute est un **curseur qui pose** la conformité et mesure ce qu'elle fait à des bornes déjà livrées ici. La circularité est réelle, elle est nommée en RQ13, et la seule chose qui en sorte est le tableau 21 rempli par la mesure — utile, et beaucoup plus modeste qu'une reproduction du résultat.
- **La vigilance épistémique d'un agent.** Le §8.2 mesure ce qu'un agent comprend d'une source intéressée et, séparément, sa **disposition** à agir sur cette compréhension sans y avoir été invité. Le simulateur n'a rien de tout cela. Il transpose ce que le **milieu** doit porter pour que la question ait un sens — l'attribution, la réputation sous condition d'issue vérifiable —, jamais la vigilance.
- **L'escalade hors du milieu.** Pas de système d'exploitation, pas de droits, pas d'identité de session dans le monde clos : le simulateur peut refuser l'action non journalisée, il ne peut pas produire le contournement, qui est le mode de défaillance mesuré au §8.3. Il n'écrit jamais qu'une escalade a été empêchée (T3).
- **La corrélation des fautes, mesurée.** Elle s'injecte, elle ne s'estime pas. Le scénario L montre l'effondrement de la corroboration entre indépendance et corrélation parfaite ; il ne dit jamais où se situe un système réel entre les deux, parce que le traité dit qu'on ne sait pas le mesurer.
- **Le paramètre d'ordre de Vicsek.** Φ, η_c et β ≈ 0,45 supposent un bruit non nul (§1.2), que l'algorithme 1 du ch. 1 exclut par hypothèse. Aucun mécanisme du périmètre actuel ne les fournit. PD5 reste donc un principe sans fournisseur : les scénarios disent « comportement collectif », et le trou est nommé ici plutôt que comblé par une grandeur inventée.
- **La vivacité.** Aucune trace finie ne réfute L1. Ce que le simulateur produit est au mieux une **vivacité conditionnelle**, au sens du mode (e) de l'algorithme 3 du §3.3.

**Ce que la couverture ne prétend pas être.** Les treize scénarios rattachent les 24 sections du traité, mais un rattachement n'est pas un épuisement : chaque scénario porte la thèse dominante de ses sections, pas la totalité de leurs mécanismes. Ce que le §2.4 garantit est plus modeste et vérifiable : aucun élément du traité n'est **ni** transposé **ni** écarté avec sa raison. La règle PD9 s'applique au document autant qu'au produit — la couverture croît sur un budget, et aucun critère de complétude n'existe.

**Ce que la révision 3.0 ne prétend pas être.** Un document révisé n'est pas un produit révisé. Les treize scénarios sont livrés et mesurés, le treizième depuis la phase 6. Trois choses en découlent, à ne confondre sous aucun prétexte. La **transposition** du ch. 8 est faite, au sens du §2.4 : aucune de ses trois sections n'est ni absente ni écartée en silence. La **livraison** l'est aussi, et le §0 en tient le compte — mais quatre de ses mécanismes n'ont aucun appelant de scénario, ce qui a sur un résultat l'effet d'un mécanisme absent (PD6). Et la **validation** ne le sera jamais au sens où on l'entendrait d'un mécanisme du milieu : le traité écrit lui-même que ce qu'on sait valider avant déploiement, ce sont les mécanismes, et que ce qu'on ne sait pas valider, c'est la population.

Le traité écrit de lui-même que sa frontière « reste une frontière argumentée ». Ce simulateur la rend **manipulable**. Il ne la rend pas mesurée. La deuxième édition lui donne un second axe, et la position du produit sur celui-là est ce que la phase 6 a mesuré plutôt qu'annoncé : un axe spécifié, un curseur livré, et une grandeur qui ne sépare pas ce que le §8.1 du traité lui prêtait (§0.1).



