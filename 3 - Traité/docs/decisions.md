# Registre des décisions

Ce que ce document sert à éviter : refaire un choix déjà tranché, ou le défaire
sans savoir ce qu'il portait. Chaque entrée dit **ce qui a été décidé**, **sur
quoi**, et **ce qu'il faudrait pour la rouvrir**.

Trois provenances, et elles ne se valent pas :

| Marque | Provenance | Ce qu'il faut pour rouvrir |
|---|---|---|
| **[M]** | Tranchée par la **mesure** — un banc a rendu un verdict | Une mesure contraire, sur le même banc |
| **[C]** | Décision de **conception** du PRD | Un argument, et une mise à jour du PRD |
| **[R]** | Contrainte de **réalisation** — l'environnement l'impose | La disparition de la contrainte |

## Les décisions du PRD (§11)

| # | Décision | État |
|---|---|---|
| DT1 | Arithmétique du cœur | **[M] Flottant partout, aucun point fixe.** Le groupe IEEE est identique bit à bit sur les deux cibles à 10⁶ itérations ; la divergence vient entièrement de la bibliothèque mathématique de la plateforme. Correctif : `libm`, et sept méthodes de `f64` interdites par `clippy.toml`. La recommandation antérieure — points fixes sur l'ordonnancement — est écartée **par la mesure**. [Verdict](../bancs/dt1-flottant/VERDICT.md) |
| DT2 | Format de configuration | **[C] JSON** — `serde_json` est déjà requis pour l'export. L'URL de partage, elle, n'encode **pas** de JSON : `sim-agents::partage` emploie un format textuel `clé:valeur` sans dépendance, précisément pour ne pas tirer un encodeur base64 (RQ3) |
| DT3 | File d'événements | **[C] `BinaryHeap`** — la file calendaire ne se justifie que si NF-05 échoue. NF-05 **a** échoué, mais pour une raison structurelle en Θ(n²) qu'une meilleure file ne corrige pas |
| DT4 | Hébergement web | **[C] Pages statiques.** Tenu : trois fichiers côte à côte, aucune dépendance serveur |
| DT5 | Le traité comme donnée | **[C] Renvois de section et de page + citations courtes** ; le texte intégral reste dans le PDF. **Amendé en 3.0** : la page s'entend de la **deuxième édition**, et l'édition fait partie de la provenance — les deux éditions ne partagent pas leur pagination, donc une page sans édition est une provenance fausse, non imprécise |
| DT6 | Le détecteur de défaillance | **[C] posée, non tenue.** Un objet paramétré dans `sim-core` — mais il n'a **qu'un** consommateur (`sim-agents::pair_a_pair`), `sim-milieu` n'en instancie aucun, et le sondage indirect est un second objet, `sim-agents::soupcon::DetecteurInfectieux`. Les cinq exemplaires comptés dans le traité n'ont pas produit une factorisation ; PD7 reste à trancher |
| DT7 | Le plan de contrôle | **[C] Modèle de coût**, jamais un protocole implanté. L'affichage dit « modèle de coût du plan de contrôle », jamais « consensus ». Implanter Raft ferait du produit un simulateur de protocole d'accord, ce que le traité refuse d'être |
| DT8 | L'agent menteur | **[C] Point d'injection unique**, désactivé par défaut, activable dans les scénarios I et L seulement. **Révisée en 3.0** : la première édition présentait la faute arbitraire comme **importée avec un adversaire** ; le §8.3 de la seconde la mesure comme **endogène** — une population dont chaque membre suit fidèlement sa consigne produit l'escalade. La décision ne change pas, ce qu'elle établit change : le libellé affiché dit désormais *l'effet est byzantin, l'origine ne l'est pas*, la borne 3f + 1 est affichée avec sa propre inapplicabilité à ce régime (le nombre d'agents adverses n'y est pas borné : il vaut n), et le régime lui-même est déclaré hors modèle (EX-C20) |
| DT9 | Le milieu arbitre-t-il les époques ? | **[C] Réglable, activé par défaut, débrayage nommé.** Ce que l'activation établit est S1w, pas S1. **Non tenue dans le code** : le milieu ne compare aucune époque, l'arbitrage vit côté agent (`sim-agents::soupcon`), et `sim_milieu::hors_perimetre()` le déclare |
| DT10 | Granularité de l'horloge | **[C] Une par scénario**, journalisée. Conséquence dure : comparer deux exécutions de granularités différentes est **refusé**, pas approximé. Le champ `scenario` de `Config` entre dans le hachage pour rendre l'incomparabilité visible plutôt que de la contrôler séparément |
| DT11 | Temps des protocoles épidémiques | **[C] Asynchrone par défaut** ; le synchrone reste une option du scénario H, et l'unité affichée change avec lui. **Sans commutateur dans le code** : ni horloge de Poisson, ni couplage — `sim_agents::hors_perimetre()` le déclare |
| DT12 | Étiquette de couverture | **[C] Cinquième étiquette [C]**, ajoutée à PD2. Étendue en 3.0 à EX-C20, EX-A57 et EX-A59 |
| DT13 | **Comment se transpose la variance nulle du §8.1** *(nouvelle en 3.0, livrée)* | **[C] Familles de décision nommées** (EX-C19), et non un scalaire de corrélation saisi. **Amendée par la réalisation** : le partage porte sur le **tour** de l'agent, non sur l'instant logique. Les cycles sont décalés d'un tirage dans la période — correction imposée par la mesure en phase 4, sans quoi la population tombait d'un bloc —, donc deux agents ne partagent jamais une date, et une clé par instant rendait EX-C19 **inerte**. Ce qu'ils partagent est le rang de la décision dans leur boucle, ce qui est aussi le fait mesuré : dix-huit agents sur trente ouvrent une branche du même nom, pas à la même microseconde. Même motif qu'EX-C14 : un scalaire est un chiffre qu'on pose, une structure est un objet qu'on peut prendre en défaut, et Φ_c dérivé d'une structure est réfutable. La troisième option — appeler un vrai modèle de langage — est écartée par le monde clos **et** par PD1 : aucun service externe n'est déterministe, rejouable ni versionné au sens de NF-03. Conséquence dure : les positions intermédiaires du curseur de familles n'ont aucune provenance dans le traité et sont étiquetées comme des interpolations du produit |
| DT14 | **Où se mesure Φ_c** *(nouvelle en 3.0, livrée)* | **[C] Sur un sujet dédié à une partition unique** ; le multipartition est **refusé au chargement**. C'est M2 qui tranche : comparer deux décisions déposées sur deux partitions suppose une relation d'ordre que le milieu ne fournit pas. Le sujet dédié est retenu contre la mesure par partition parce qu'il rend la grandeur comparable d'une exécution à l'autre sans dépendre du régime de clé (EX-A45), qui déplacerait les décisions pour des raisons étrangères à la conformité |

## Les verdicts de banc

| Banc | Verdict | Conséquence |
|---|---|---|
| [EX-V12 — parité natif/WASM](../bancs/parite-wasm/VERDICT.md) | **[M]** Tenue sur les six cas du scénario B, bits des flottants compris | La bibliothèque partagée entre les deux cibles est ce qui rend la parité mesurable |
| [DT1 — arithmétique](../bancs/dt1-flottant/VERDICT.md) | **[M]** Flottant conservé, transcendantes par `libm` | Sept méthodes de `f64` interdites par lint. Le verdict de `mul_add` **dépend de la machine de construction**, ce qui renforce l'interdiction au lieu de l'affaiblir |
| [NF-05 — débit](../bancs/nf05-debit/VERDICT.md) | **[M] Cible non atteinte** : de l'ordre de 10 à 15 s simulées/s-cœur à n = 1 000 contre 10³ (remesuré à la clôture de la phase 5 ; la mesure de phase 1, 0,2–2,0, était périmée d'un facteur cinquante depuis que la rétention existe) | L'écart est structurel — chaque agent lit ce que toute la population écrit, donc Θ(n²). **La cible est à refaire sur la mesure**, comme DT1 l'a été. Rien de la phase 1 n'en dépend |

## Les réévaluations obligatoires

Le PRD impose deux réévaluations à la sortie de la phase 3. Les deux sont faites
et consignées au §0 ; la révision 3.0 en a rouvert une pour une raison qui n'est
pas celle qu'elles surveillaient.

**Le plafond de scénarios est reconduit à la sortie de la phase 3, puis porté de
douze à treize par la deuxième édition du traité.** Sept scénarios implantés à la
sortie de la phase 3, cinq au plan, total exactement douze, **aucun ajouté** en
trois phases : le plafond n'a pas été mis à l'épreuve, et il a été reconduit. Ce
qui a absorbé la matière nouvelle, ce sont les préréglages — trente-quatre à la
sortie de la phase 3, davantage depuis ; le compte exact n'est pas tenu, aucun
registre ne les énumère, et il ne doit donc pas être cité comme s'il l'était (F1).

La révision 3.0 le porte à treize, et la distinction est celle qui fait tenir la
clause de révision unique. Cette clause borne la croissance du produit **par son
propre appétit** : elle interdit d'ajouter un scénario parce qu'un mécanisme est
intéressant. Elle ne peut pas borner la croissance de la **source**, qui n'est pas
une décision du produit. Le traité est passé de 21 à 24 sections ; tenir douze
reviendrait à écarter trois sections en silence, ce que RC5 interdit. **Aucun
treizième scénario n'aurait été admis si le traité n'avait pas changé**, et le
quatorzième ne l'est pas.

**Aucune cinquième crate n'est ouverte.** La règle exige les deux conditions —
plus d'une crate consommatrice **et** une dépendance que les autres ne doivent
pas hériter. Sur le graphe réel, aucun candidat ne les satisfait. Réévaluée de
nouveau à la révision 3.0 : le chapitre 8 n'introduit aucune dépendance — un
compteur par clé, une projection compactée, une statistique de paires, une
contrainte d'ordre de lecture — et sa consommation reste la chaîne unique.

## Les décisions de réalisation

| Décision | Marque | Motif |
|---|---|---|
| Toolchain `x86_64-pc-windows-gnu` | **[R]** | Le linker MSVC exige le toolset C++ de Visual Studio, absent de la machine. `rustup` fournit tout pour `windows-gnu`. Ne touche aucune exigence : NF-02 porte sur la parité natif/WASM, mesurée sur la cible native effectivement employée |
| mingw-w64 (WinLibs) requis | **[R]** | `dlltool.exe`, exigé par `eframe`. **L'interface seule** en a besoin |
| `wasm-bindgen-cli` épinglée sur `Cargo.lock` | **[R]** | Une version de CLI différente de celle de la bibliothèque est refusée à l'exécution |
| `web_time::Instant` au lieu de `std::time::Instant` dans `sim-viz` | **[M]** | `std::time::Instant` **panique** sur `wasm32-unknown-unknown`. Le natif compilait sans rien dire ; seule la construction WASM l'a révélé. `web-time` était déjà dans l'arbre par egui : aucune dépendance nouvelle |
| Pas de lint contre `std::time::Instant` | **[M]** | Tenté, puis retiré : sur cible native, `web_time::Instant` **est** `std::time::Instant` par réexport, et clippy résout le chemin canonique. Le lint frappait le correctif en même temps que le défaut. **Aucun garde-fou ne le remplace** : la construction pour `wasm32-unknown-unknown` ne le voit pas — le type compile pour cette cible et ne panique qu'à l'exécution. `cargo clippy --target wasm32-unknown-unknown` avec le type interdit marcherait, et n'est pas câblé |
| `#![deny(missing_docs)]` sur les quatre crates | **[C]** | Rustdoc **est** la documentation d'interface du dépôt. Une interface à demi documentée ne dit pas laquelle des deux moitiés manque |
| `#![deny(rustdoc::broken_intra_doc_links)]` sur les quatre crates | **[C]** | Un renvoi rustdoc cassé ne compile pas. C'est ce qui garde vrais les liens entre modules quand un type est renommé — le seul contrôle mécanique que le dépôt possède sur sa propre documentation |
| `publish = false` sur tous les manifestes | **[C]** | Ces crates n'ont de sens qu'ensemble, et aucune licence n'est déclarée |
| Documentation regroupée dans `docs/` | **[C]** | Sauf `README.md` et `CLAUDE.md`, que leurs outils attendent à la racine, et les `VERDICT.md`, gardés à côté de la mesure qui les produit |
| `SPEC.md` distinct du PRD | **[C]** | Le PRD dit ce qui est **exigé** et pourquoi, avec le traité pour autorité ; `SPEC.md` dit ce que le code **garantit**, avec le code pour autorité. Un seul document pour les deux rôles devient faux d'un côté à chaque changement de l'autre, sans qu'on sache lequel. Pour rouvrir : montrer que les deux ne divergent jamais — ce que les listes `hors_perimetre()` contredisent déjà |

## Les arbitrages ouverts par la révision de l'interface

Trois choix pris **dans la vue** faute de pouvoir les prendre ailleurs. Les
trois tiennent aujourd'hui ; les trois se rouvrent par un changement de
`sim-agents`, listé au §0 du PRD.

| Décision | Marque | Ce qu'il faudrait pour la rouvrir |
|---|---|---|
| **L'axe de lecture du scénario A est le délai d'aller simple, pas ℓ₉₉** | **[M]** | Constat de figure : les deux temps s'égalent quand l'aller simple vaut 2 · ℓ₉₉. Balayé **en ℓ₉₉**, le croisement tombe à aller simple / 2, soit au plus 25 ms sur un axe qui va à 500 — écrasé contre le bord gauche, invisible même là où il existe. Balayé en aller simple, il tombe à 2 · ℓ₉₉, soit 40 ms sur un axe qui va à 50 : au milieu de la figure, dès l'ouverture. Pour rouvrir : porter la plage d'aller simple du §7 du PRD à 1 000 ms, ou y noter que l'axe de lecture du scénario A est l'aller simple |
| **La sentinelle `+∞` est traduite dans la vue, pas dans le type** | **[C]**, *portée réduite par l'audit* | `Mesures::plancher_observe` vaut `f64::INFINITY` tant qu'aucun cycle ne l'a mis à jour, et `sim-viz` rend « jamais observé » au lieu de `inf`. **Le cas de γ = 1 ne le produit plus** : `verifier_bornes` relève les deux minimums *avant* de consulter le portail NF-14, donc une borne effacée n'efface plus la mesure. La sentinelle ne subsiste que pour une exécution qui n'aurait exécuté aucun cycle. Le bon correctif reste `Option<f64>`, comme `ecart_a_loptimum` juste à côté ; il change une signature publique de `sim-agents`. Pour rouvrir : le changement de type, et la traduction de la vue disparaît avec |
| **Le vainqueur en temps est lu dans une chaîne française** | **[R]** | `Comparaison::verdict_temps` ne rend le vainqueur que dans une phrase formatée ; la figure du croisement le lit par `contains("la maille gagne")`. Une reformulation le casserait **sans erreur de compilation** — d'où un test de `sim-viz` (`le_vainqueur_se_lit_encore_dans_la_phrase_de_verdict`) qui échoue à la place. Pour rouvrir : `qui_gagne_en_temps() -> Vainqueur` dans `sim-agents`, dont `verdict_temps` se sert pour composer sa phrase |

## Les modélisations que la mesure a corrigées

Elles ne sont pas des décisions de conception mais des **erreurs trouvées par le
test**, consignées ici parce qu'elles se reproduiraient sans cela.

| Ce qui était écrit | Ce que la mesure a imposé |
|---|---|
| Le cycle d'agent attendait l'accusé de durabilité | Rendait `T < ℓ₉₉` — l'essaim aveugle — **inexprimable**. Le cycle est cadencé sur T seul |
| Φ_c estimé sur une coupe transversale — une décision par agent | **Identiquement nul** : la loi marginale s'estimait sur le même échantillon que l'accord observé, et les deux termes étaient égaux par construction. L'estimation aligne désormais les suites de décisions **par rang**, la loi marginale d'un agent venant de sa propre suite |
| EX-A58 effaçait les bornes sur Φ_c mesuré | Fausse alarme : Φ_c ne sépare pas la conformité de la coordination, donc l'effacement affirmait une violation de l'indépendance des **tirages** là où était mesurée une **coordination**. NF-14 porte sur un *réglage* — c'est la structure des familles, qui est connue |
| Le partage de tirage était clé par instant logique | **Inerte** : les cycles d'agents sont décalés, donc deux agents ne partagent jamais une date. La clé est le **tour** de l'agent |
| La lecture sautait les enregistrements non durables | Cassait M1 côté lecture. `take_while(durable)`, ce qui a révélé un problème de dimensionnement |
| `lire_multi` appliquait le budget **par partition** | Perception non bornée, donc violation d'EX-A12. Le budget est **total** |
| Hachage multiplicatif dans HyperLogLog | 81 % d'erreur. HLL exige une avalanche complète : splitmix64 |
| Toutes les sondes de cascade en phase | La population tombait d'un bloc : **aucune génération**, donc rien à montrer. Décalage de phase ajouté |
| Hystérésis de descente déclarée, jamais implantée | Implantée : divise les inversions par cinq — sans supprimer l'oscillation, qui est structurelle |

## Les écarts au traité relevés par la mesure

NF-15 : « un écart est un défaut du simulateur **ou** une erreur du traité, et
les deux méritent d'être trouvés. » **Cinq** à ce jour, tous consignés dans le
code à l'endroit où ils se constatent.

**Trois** d'entre eux contredisent un énoncé du traité. Deux sont repris au §0 du
PRD — le budget de retard du mode « moyeu » et la dérive de la somme sans
relance ; le troisième est Φ_c, relevé par la phase 6, et il porte contre le
traité **autant que** contre le PRD, puisque c'est le §8.1 qui propose la
grandeur et le PRD qui lui prêtait un comportement. Les **deux autres** sont des
constats de mesure qui ne contredisent aucun énoncé : le contrôleur
d'élasticité, dont le §2.2 du traité décrit déjà le comportement, et `mul_add`,
qui porte sur la machine de construction et non sur le traité.

| Écart | Ce que le traité écrit | Ce que la mesure donne |
|---|---|---|
| Budget de retard du mode « moyeu » | « moins de 7,9 × 10⁻³ à n = 100 » | π/(4 × 99) = **7,933 × 10⁻³**, qui dépasse la borne annoncée. L'ordre de grandeur est juste, l'inégalité stricte ne l'est pas |
| Dérive de la somme sans relance | « avec C = ∞, elle dérive sans borne » | Elle **se fige**. L'unanimité installée, il n'y a plus de masse à perdre. La conséquence est pire : l'erreur devient stable, donc indétectable par l'attente |
| Contrôleur d'élasticité | Convergence attendue aux valeurs documentées | Il tourne autour de sa cible. `visées = courantes × r` est un correcteur proportionnel à gain unitaire et le temps mort vaut deux périodes. Ne contredit pas le traité, qui décrit ce mécanisme comme mesurant « l'effet d'une décision qu'il n'a pas fini d'appliquer » |
| `mul_add` | Attendu identique entre cibles | Verdict **dépendant de la machine de construction** : il a changé entre deux passages, après installation de mingw |
| **Φ_c, paramètre d'ordre de la conformité** *(relevé par la phase 6)* | Le §8.1 du traité le propose comme la grandeur qui mesure la conformité d'une population, et le §9 du PRD en attendait un passage de ≈ 0 à ≈ 1 sous le curseur de familles | Il vaut **déjà ≈ 0,17** avec un tirage par agent, et le curseur ne le déplace que de ≈ 0,055 — de 0,173 à 0,228 —, non monotonement. La cause n'est pas l'estimateur : les agents lisent tous la même trace, donc leurs décisions sont corrélées. **Φ_c mesure la somme de la corrélation due à la fonction de décision et de celle due au milieu partagé, sans les séparer** — et sur un essaim stigmergique la seconde domine. L'écart porte contre le traité autant que contre le PRD. Voir `conformite::CONSTAT_DE_MESURE` et le §0.1 du PRD |

## Ce que la deuxième édition du traité rouvre, et ce qu'elle ne rouvre pas

La deuxième édition, datée du 13 août 2026, ajoute un chapitre 8 et des
insertions dans chacun des sept autres. **Aucune décision de ce registre n'est
défaite.** Deux sont amendées — DT5 sur la pagination, DT8 sur ce que le point
d'injection établit —, deux sont ajoutées — DT13 et DT14 —, et une réévaluation
est rouverte sur changement de source (le plafond de scénarios).

Ce qui **n'est pas** rouvert, et qu'il faut dire pour éviter la relecture :

- **DT1** — l'arithmétique. Le chapitre 8 n'ajoute aucune transcendante.
- **DT3** — la file d'événements. Rien du chapitre 8 ne change le profil de coût.
- **DT7** — le plan de contrôle reste un modèle de coût. Le chapitre 8 ne demande
  aucun protocole d'accord ; son seul invariant global — l'unicité du déployeur
  d'un service — est explicitement renvoyé par le traité au chapitre 4, donc à
  l'accord, donc au modèle de coût existant.
- **La règle de la cinquième crate** — réévaluée, reconduite.

Et le point qui pèse le plus, parce qu'il ne se lit dans aucune décision : la
deuxième édition établit que **six des sept énoncés du tableau 21 sont livrés et
mesurés dans ce dépôt sous une hypothèse d'indépendance qu'aucun réglage ne met
en défaut.** Ce n'est pas une décision à trancher, c'est une réserve — elle est au
§0.0 du PRD, exigence par exigence, et EX-A58 est ce qui la lèvera.
