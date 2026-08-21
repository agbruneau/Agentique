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
| DT5 | Le traité comme donnée | **[C] Renvois de section et de page + citations courtes** ; le texte intégral reste dans le PDF. **Amendé en 3.0** : la page fait partie de la provenance, avec l'édition — deux éditions ne partagent pas leur pagination, donc une page sans édition est une provenance fausse, non imprécise. **Amendé de nouveau le 17 août 2026, en appliquant la clause à elle-même** : la version 3.0 écrivait « la page s'entend de la **deuxième** édition », et le seul traité que le dépôt contient est la **troisième**, du 15 août 2026, **143 pages** (`python -c "import pymupdf; print(pymupdf.open('Traité.pdf').page_count)"`). La page s'entend donc de la troisième, et un renvoi qui ne nomme pas son édition n'est pas une provenance. **Ce que l'amendement ne faisait pas, et qui est fait depuis** : migrer les renvois. La passe de finition du 17 août 2026 (`bancs/audit-2026-08/FINITION-prd.md`) a repris les **75** `p. N` du PRD un par un, **par ancre textuelle** — la phrase, le tableau ou la figure cherchés dans le PDF livré, jamais une arithmétique sur l'ancienne pagination, **puisqu'aucun décalage constant n'existe** : le §3.3 glisse de +8 pages, le tableau 14 de +19, la conclusion de +32. Verdict : **23 justes, 41 corrigées, 10 citant sciemment une édition antérieure et le disant, 1 introuvable** dans la troisième édition (voir les provenances devenues fausses, plus bas). **La clause s'énonce désormais comme une forme vérifiable** : un renvoi du PRD s'écrit `p. N, Xᵉ éd.`, et une seule ligne le vérifie — `grep -oE "p\. [0-9]+(-[0-9]+)?, [0-9](ᵉ\|ʳᵉ) éd\.\|p\. [0-9]+(-[0-9]+)?" docs/PRD.md \| grep -v 'éd\.' \| wc -l` → **0**. **Ce qu'elle ne couvre pas** : les renvois de `crates/` et ceux de `docs/README.md` |
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
| [Audit du dépôt — 17 août 2026](../bancs/audit-2026-08/CONSOLIDATION.md) | **[M]** Dix agents, cinq morceaux, deux tours chacun (bâtisseur + critique en contexte neuf). Suite verte à **465 tests** ; clippy et rustdoc à 0. Le banc n'a pas de `VERDICT.md` : ses pièces sont les cinq `M*-*.md` et les cinq `M*-critique.md` de [`bancs/audit-2026-08/`](../bancs/audit-2026-08/), et sa consolidation en est le verdict | Le défaut le plus fréquent trouvé n'est pas un défaut de code : c'est **un chiffre écrit sans la commande qui le produit**. D'où la règle appliquée depuis à tous les documents — un compte se donne avec sa ligne de mesure et sa date, jamais gravé. Trois conséquences normatives : DT5 amendé sur l'édition, quatre décisions de conception ouvertes ci-dessous, et le reclassement de deux écarts au traité |

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
| `publish = false` sur tous les manifestes | **[C]** | Ces crates n'ont de sens qu'ensemble. ⚠ *« Aucune licence n'est déclarée » était le second motif : il tombe le 21 août 2026 — le dépôt porte une `LICENSE` CC BY 4.0 à sa racine, qui couvre le code. Le premier motif suffit, et la décision ne change pas : `publish = false` tient* |
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

## Les décisions ouvertes par l'audit du 17 août 2026

Quatre décisions que les bâtisseurs de l'audit ont **laissées ouvertes plutôt que
prises**, chacune parce qu'elle sort du morceau où le défaut a été mesuré. Elles
entrent ici comme décisions ouvertes, non comme faits : le motif de chacune est
dans le rapport nommé, et **aucune n'est tranchée**. Les quatre touchent une
interface publique ou une liste normative, ce qui est exactement la classe qu'un
audit de crate ne doit pas trancher seul.

| Décision ouverte | Ce que la mesure établit | Ce qu'il faudrait pour la trancher |
|---|---|---|
| **Fermer `Proprietes` par le type, ou renoncer à tenir PD12 par le type** ([M1](../bancs/audit-2026-08/M1-sim-core.md), C1) | `#[non_exhaustive]` interdit le littéral, **pas l'affectation de champ**. `sim_core::detecteur::Proprietes` est `Copy` avec quatre champs `pub`, et `Detecteur::proprietes()` en rend un exemplaire par valeur : depuis une crate externe, un exemplaire à `suspicions = 1 000 000, fausses = 0, exactitude = Some(0.0)` se fabrique. Ce que PD12 tient quand même est plus étroit qu'annoncé — le détecteur ne prend ces nombres que de `sonder`, donc une copie falsifiée ne trompe qu'un affichage. La doc de `detecteur.rs` porte désormais la mesure au lieu de l'affirmation contraire | Champs privés derrière quatre accesseurs. **Casse `crates/sim-agents/src/pair_a_pair.rs`**, qui lit `p.suspicions` et `p.fausses_suspicions` : c'est un changement d'interface entre deux crates, donc une décision de conception, pas un correctif d'audit |
| **Remonter dans `sim-agents` les neuf valeurs de paramètre transcrites dans `sim-viz`** ([M5](../bancs/audit-2026-08/M5-viz-et-docs.md), E6) | `VueA::default` pose six valeurs — `n: 64, p: 8, l99_ms: 20.0, aller_simple_ms: 2.0, degre_depot: 3, taux_omission: 0.01` — et `VueB::default` trois — `n: 16, budget: 150_000, graine: 1`. Aucune ne vient de `sim-agents` (`grep -rn '150_000' crates/sim-agents/src/` ne rend rien). Elles ne sont pas sans provenance pour autant : ce sont **les défauts des tableaux du §7 du PRD**, transcrits faute d'accesseur — sauf la graine, qui ne figure dans aucun tableau. Rien ne tient la transcription en accord, et un test qui comparerait la vue à elle-même serait tautologique | Un défaut nommé pour `VueB` et un constructeur de défaut pour `scenario_a`, dont l'API est aujourd'hui une fonction nue à sept paramètres. Tant que ce n'est pas fait, le contrat de `sim-viz` porte « zéro définition de scénario **à deux exceptions nommées** » au lieu d'un absolu : c'est vrai, et plus faible |
| **`ModeleFaute::avertissements` n'a aucun appelant — donc la moitié `[U]` d'EX-C06 n'est tenue par personne** ([M1](../bancs/audit-2026-08/M1-sim-core.md), C4 et D2) | Vérifié : aucun appelant dans `crates/`, `bancs/` compris. Les avertissements que `sim-agents` et `sim-viz` affichent viennent de `sim_agents::stigmergie::Params::avertissements`, homonyme et sans rapport. L'audit a **ajouté** à cette fonction l'avertissement de crash corrélé que le passage des taux par niveau rendait nécessaire — mesuré : un centre unique à 0,09 vide toute la population 9,3 % des pas, contre 0 vidage complet pour un `crash_machine` de même espérance par acteur —, et cet avertissement neuf hérite de la même réserve : calculé, affiché par personne | Un point d'appel dans la vue, ou le retrait d'EX-C06 de sa moitié `[U]`. En attendant, la réserve est déclarée par `ModeleFaute::hors_modele()` et par le §0 du PRD |
| **Ouvrir `sim_core::hors_perimetre()`, ou assumer que le cœur n'en a pas** ([M1](../bancs/audit-2026-08/M1-sim-core.md), R2) | `grep -rn 'fn hors_perimetre' crates/` rend deux fonctions, `sim-milieu` et `sim-agents` ; **`sim-core` n'en a aucune**. Les absences du cœur logent donc dans `ModeleFaute::hors_modele()`, dont ce n'est pas l'objet : sa première entrée y énumère **neuf** mécanismes sans appelant — `tirer_pannes`, `Moteur::avancer_partition`, `message_perdu`, `injection_echec`, `injection_retard`, `injection_valeur`, `retard_message`, `ecriture_corrompue`, `avertissements` —, dont six n'ont aucun rapport avec le modèle de faute pris comme modèle. Le plancher mémoire d'EX-C17, EX-C08 et EX-C16 y sont aussi, ou nulle part | Trancher : soit une quatrième liste vivante, ce qui touche `docs/PRD.md`, `docs/SPEC.md`, `CLAUDE.md` et l'onglet « Limites » (une septième section) ; soit écrire que `hors_modele()` est **par convention** la liste d'absences du cœur, ce qui coûte une phrase et laisse le nom mentir. **Le code n'est le périmètre d'aucun des deux audits** ; la décision est ici, la fonction n'est pas créée |

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

**Reclassement du 17 août 2026, contre la troisième édition livrée.** Le compte
reste à cinq et la troisième édition le confirme : sa conclusion écrit *« Cinq
écarts entre le livre et sa transposition y sont consignés, dont trois contre
l'ouvrage »* et cite ce dépôt en notice 120 (`Traité.md:1743`, `Traité.pdf`
p. 129). Ce qui change est le statut de trois lignes du tableau, et il faut le
dire parce qu'un écart absorbé par la source cesse d'être une contradiction sans
cesser d'être un fait.

- **Les deux premiers sont absorbés dans le texte de la troisième édition.** Le
  §3.1 (`Traité.md:736`, p. 42) écrit désormais **7,933 × 10⁻³** et qualifie
  lui-même 7,9 × 10⁻³ d'« énoncé faux, non une imprécision » ; le §4.1
  (`Traité.md:981`, p. 58) écrit « Sans relance, l'erreur ne croît pas sans
  borne : **elle se fige** », puis « La relance de la ligne 11 **ne plafonne donc
  pas** l'erreur ». Les deux mesures sont retrouvées par la source, mot pour mot.
  Ils restent des écarts contre la **deuxième** édition et contre le PRD, qui écrit
  encore « moins de 7,9 × 10⁻³ » au §0 et « elle dérive sans borne ».
- **Le contrôleur d'élasticité change de camp, et n'est pas tranché.** Le registre
  le classait « ne contredit pas le traité » sur la foi du §2.2. Le §7.3 de la
  troisième édition (`Traité.md:1576`, p. 114) conclut le contraire du constat que
  le module affiche : *« Le comportement par défaut n'est donc pas une
  oscillation, c'est un dépassement en escalier suivi d'une descente filtrée — et
  qui cherche une oscillation ne trouve rien à corriger. »* La contradiction est
  frontale, et elle n'est **pas** arbitrable en l'état : le produit ne transpose
  ni la fenêtre nulle à la hausse, ni les deux politiques de montée (100 % ou
  4 répliques par tranche de 15 s) que la même page publie, et ce sont elles que
  le traité invoque pour conclure à l'escalier. L'écart peut donc venir d'une
  transposition incomplète autant que du traité. Ce qu'il faut pour trancher :
  transposer les deux politiques, rejouer
  `cargo run -p sim-agents --example diagnostic_elasticite --release`, et
  reclasser ici. **Ouvert.**
- **`mul_add` et Φ_c sont inchangés.** Le premier ne porte pas sur le traité ; le
  second est cité par la conclusion de la troisième édition avec les valeurs
  mesurées ici, 0,173 et 0,228.

**Quatre citations du PRD que la troisième édition retire ou inverse** — trois
mesurées à la consolidation, la quatrième par la passe de finition des renvois.
Mesurées Elles ne sont pas des écarts au sens de NF-15 — aucune mesure
n'est en cause — mais des provenances devenues fausses, ce que F2 traite comme un
défaut bloquant. (a) Le PRD cite *« Le livre a donc échangé une ignorance contre
une dette »* (§1, p. 96) ; la troisième édition écrit « Le livre n'a donc **pas**
échangé une ignorance contre une dette : il a proposé, l'auteur a mesuré, et la
mesure lui est revenue contre » (`Traité.md:1743`, p. 129). (b) Le PRD donne le
troisième reste pour *« inchangé »*, sur l'absence d'estimateur de corrélation ne
demandant pas la vue globale ; la troisième édition écrit « **la phrase ne tient
plus** » et lui oppose φ = 0,916 sur 18 000 missions (`Traité.md:1737`).
(c) Le PRD décrit l'ouvrage comme faisant « 100 pages, dont 95 d'argument, les
Références commençant p. 96 » ; mesuré, 143 pages et Références p. 130.
**(d) *(17 août 2026, passe de finition des renvois)*** Le §1 du PRD donnait le
quatrième reste de la conclusion sous la citation *« un théorème manquant, et non
une mesure manquante, est ce qui bloque »* (p. 95, 2ᵉ éd.). **Cette phrase ne se
retrouve nulle part dans la troisième édition**, et aucune page ne lui a donc été
attribuée — c'est le seul des soixante-quinze renvois du PRD qui reste sans page
mesurée. Ce que la troisième édition écrit à la place, au même endroit, la
contredit sur son point de fond : « ce n'est plus le seul endroit du livre où un
théorème manque : le deuxième reste en est un autre, et la décomposition de Φ_c
plus bas un troisième » (p. 129, 3ᵉ éd.), et sa conclusion générale retourne
l'opposition — « ce que le livre laisse ouvert n'est donc pas une théorie
manquante mais une métrologie manquante » (p. 130, 3ᵉ éd.). Le PRD porte désormais
la citation qui existe — « transporter mécaniquement les bornes donne des chiffres
faux ; la forme correcte du résultat reste à écrire » (p. 129, 3ᵉ éd.) — et le §8.3
du PRD ne dit plus « le seul endroit ». **Aucune mesure n'est en cause, donc le
compte de cinq écarts NF-15 est inchangé** ; ce qui l'est, c'est une provenance.
Une **cinquième**, plus étroite, est corrigée au passage : la citation du
cinquième reste portait « à la charge du système appelé », membre que la
troisième édition retire.
Les quatre sont corrigées au PRD, et consignées au §0.2.

| Écart | Ce que le traité écrit | Ce que la mesure donne |
|---|---|---|
| Budget de retard du mode « moyeu » *(absorbé par la 3ᵉ édition)* | 2ᵉ éd. : « moins de 7,9 × 10⁻³ à n = 100 » | π/(4 × 99) = **7,933 × 10⁻³**, qui dépasse la borne annoncée. L'ordre de grandeur est juste, l'inégalité stricte ne l'est pas. **La 3ᵉ édition écrit désormais 7,933 × 10⁻³** et qualifie l'arrondi d'énoncé faux (§3.1, p. 42) : la mesure est retrouvée par la source. Reste un écart contre le PRD, dont le §0 cite encore l'ancien chiffre en colonne « ce que le PRD écrit » |
| Dérive de la somme sans relance *(absorbé par la 3ᵉ édition)* | 2ᵉ éd. : « avec C = ∞, elle dérive sans borne » | Elle **se fige**. L'unanimité installée, il n'y a plus de masse à perdre. La conséquence est pire : l'erreur devient stable, donc indétectable par l'attente. **La 3ᵉ édition écrit « elle se fige »** et « la relance ne plafonne donc pas l'erreur » (§4.1, p. 58) |
| Contrôleur d'élasticité *(reclassé le 17 août 2026 — **ouvert**)* | Le §2.2 décrit le mécanisme comme mesurant « l'effet d'une décision qu'il n'a pas fini d'appliquer ». Mais le §7.3 de la 3ᵉ édition conclut que « le comportement par défaut n'est donc pas une oscillation, c'est un dépassement en escalier suivi d'une descente filtrée » | Il tourne autour de sa cible. `visées = courantes × r` est un correcteur proportionnel à gain unitaire et le temps mort vaut deux périodes ; l'hystérésis de descente divise les inversions par cinq sans les supprimer. **Ne contredisait pas la 2ᵉ édition ; contredit le §7.3 de la 3ᵉ.** Non tranché : le produit ne transpose ni la fenêtre nulle à la hausse ni les deux politiques de montée que cette page publie, et ce sont elles que le traité invoque pour conclure à l'escalier |
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

## Ce que la troisième édition rouvre, et ce qu'elle ne rouvre pas

La troisième édition, du **15 août 2026**, est la seule que le dépôt contienne :
`Traité.pdf` à la racine, **143 pages**, en-tête « 15 août 2026 — troisième
édition, revue sur sa propre mesure » (`head -6 Traité.md`). Elle est **revue sur
la mesure de ce dépôt** : sa conclusion cite `stigmergie-lab` en notice 120, avec
les valeurs de Φ_c mesurées ici et le compte de cinq écarts. La source et sa
transposition se lisent donc l'une dans l'autre, ce qui a une conséquence de
méthode : un écart trouvé ici peut reparaître dans la source à l'édition
suivante, et le registre doit dire lequel des deux a bougé.

**Une seule décision est amendée : DT5**, sur l'édition dont la page s'entend.
Aucune n'est défaite, aucune n'est ajoutée. Ce qui change est du fait, non de la
décision, et se lit trois sections plus haut : deux écarts absorbés, un reclassé
et ouvert, quatre citations du PRD devenues fausses — la quatrième étant la
seule ancre des soixante-quinze renvois de page qui ne se retrouve pas dans
l'édition livrée.

**Ce qui n'est pas rouvert.** DT1 — la troisième édition n'ajoute aucune
transcendante, et le verdict `mul_add` porte sur la machine de construction, pas
sur le traité. DT13 et DT14 — le §8.1 est inchangé sur Φ_c, sa définition et sa
condition d'échec par partition. Le plafond de treize scénarios — le traité reste
à 24 sections (`grep -c '^### ' Traité.md` → 24), donc la clause de révision
unique n'est pas sollicitée une seconde fois. La règle de la cinquième crate — le
graphe de dépendances est celui de la clôture de la phase 6.
