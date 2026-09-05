# Journal du gauntlet — mise à jour de la documentation après réorganisation

Barre retenue : `git show HEAD~1:README.md` — le README d'avant la réorganisation,
jugé sur son propre arbre, contre la version réécrite jugée sur le nouveau.
Plafond fixé avant lancement : **3 tours**.

Réorganisation à couvrir :

| Avant | Après |
|---|---|
| `3 - Traité/` | `4 - Essais/1 - Traité/` |
| `4 - Veille/` | `3 - Veille/` |
| `6 - Article/` | `4 - Essais/2 - Article/` |
| — | `Évaluation académique.md` / `.html` (racine, nouveaux) |

Contrainte non mécanique : le dépôt tient une chronique datée. Les mentions
historiques d'anciens chemins restent ; les liens actifs et les commandes bougent.

---

## Tour 1 — M3 (outillage et texte courant)

**Bâtisseur** — 14 fichiers. Un script réellement cassé réparé
(`5 - Recension/build/build-pdf.sh:58`, invoquait `../4 - Veille/Python/check-resume.py`).
Preuves : `bash -n` sur 3 scripts, `py_compile` sur 5, chaînes Pandoc/Typst exécutées
de bout en bout, quatre portes du Compendium repassées. `Évaluation académique.md`
laissé daté (il se déclare « à l'état du commit 69eeee2 », antérieur à la
réorganisation) avec une note d'ancrage ajoutée en tête.

**Verdict du critique : NON.**

**Écart retenu** — la réécriture a falsifié un relevé daté. `docs/DEVELOPPEMENT.md:55,64`
et `CLAUDE.md:104` datent du 21 août 2026 une expérience où **la forme du chemin est la
donnée mesurée** (« même accent, même espace », et six lignes plus bas un rapport de
longueur « deux fois plus longue »). Le chemin `4 - Essais/1 - Traité/` n'existait pas
à cette date — il naît au commit `daacbec` du 5 septembre. La réécriture substitue au
chemin testé une forme jamais testée : un segment, deux espaces et seize caractères de
plus, ce qui casse le rapport de longueur cité juste après.

*Contre-preuve interne relevée par le critique : `build/build-pdf.sh:12` traite le fait
daté symétrique correctement, en ancrant au lieu de réécrire. La règle était connue.*

**Coût du tour** : bâtisseur 123 k jetons / 46 outils ; critique 117 k / 27 outils.

## Tour 1 — M1 (carte du dépôt : `README.md`, `APPAREIL.md`)

**Bâtisseur** — 18 liens morts réparés (0 restant sur 42 vérifiés), arbre de la
« Carte du dépôt » refait avec le niveau `4 - Essais/`, table de traduction des
trois renommages, `Évaluation académique` intégrée. Décomptes remesurés :
584 fichiers, 76 998 245 o. à l'index au commit `daacbec`.

**Comparaison à l'aveugle** — `candidat-A` (README d'avant + son arbre complet)
contre `candidat-B` (le nôtre + le sien). Juge sans accès au dépôt ni à `git`.

**VERDICT : B gagne** — donc le nôtre. Départage sur la fidélité à l'arbre : les
deux sont à 0 lien mort, mais l'inventaire de B tombe exactement sur son arbre
(584 = 584, 19 postes de ventilation concordants), tandis que celui de A est
périmé de 11 fichiers. Écart relevé chez le perdant : A annonce « 571 fichiers,
217 .md, 32 .py » quand son propre arbre en porte 582, 219 et 39.

**Sortie de boucle sur ce morceau : victoire à l'aveugle.** Pas de tour 2.

**Réserve sur l'aveugle** — imparfait, et il faut le dire : le README d'aujourd'hui
nomme la réorganisation du 5 septembre, ce qui laisse deviner lequel des deux est
neuf. Le juge n'a pas été informé, mais rien ne garantit qu'il n'a pas déduit.
Le verdict repose toutefois sur une mesure reproductible (l'inventaire contre
l'arbre), pas sur une impression — c'est ce qui le sauve.

**Coût du tour** : bâtisseur 204 k jetons / 48 outils ; juge 106 k / 8 outils.

## Tour 2 — M3 (reprise sur l'écart)

**Bâtisseur** (nouvel agent) — les trois relevés du 21 août 2026 redisent
`…/3 - Traité/` et portent l'ancre vers le nom d'aujourd'hui, sur le patron déjà
présent dans `build-pdf.sh:12`. Preuve `git` que `4 - Essais/` n'existait pas à
cette date : `git ls-tree df9e14e` (21 août) montre une racine à cinq dossiers
dont `3 - Traité`, et `git ls-tree df9e14e -- "4 - Essais"` sort vide.

Rapport de longueur cité au §(c), recalculé : **2,65×** sous l'ancien chemin
(la phrase « deux fois plus longue » se vérifie), **1,61×** sous le nouveau
(elle devient fausse). La restauration rétablit le seul état où la phrase tient.

*Réserve du bâtisseur, portée telle quelle* : la lecture « longueur relative à la
racine du dépôt » est sa déduction — aucun document ne dit sur quels chemins la
mesure du 21 août a été prise. Sur les chemins absolus, la phrase est fausse dans
les deux états. Défaut préexistant, hors périmètre, non corrigé.

**Coût du tour** : bâtisseur 109 k jetons / 25 outils. Critique en cours.

## Tour 1 — M2 (les quinze README de branche)

**Bâtisseur** — **27 liens morts → 0** sur 517 vérifiés, vérificateur éprouvé par
mutation (on pose un lien vers l'ancien chemin : il sort 1 ; on le retire : il sort 0).
Règle appliquée : un ancien chemin reste écrit quand il nomme un dossier tel qu'il
était le jour dont la phrase parle, et reçoit alors sa glose datée ; toutes les
cibles de lien sont repointées, y compris sous un libellé historique.

Deux défauts de fond trouvés en chemin, sans rapport avec la réorganisation, déclarés
dans les fichiers plutôt que corrigés en silence : `4 - Essais/2 - Article/README.md`
inventoriait un `audit.md` supprimé le 3 septembre (`4a7ec0f`) ; et deux README
publiaient +12,6 pt de dégagement pour la planche de `5 - Recension/`, qui sort
`[LIMITE] +0,3 pt` depuis sa recomposition du 25 août (`91ed417`).

**Verdict du critique : NON.**

**Écart retenu** — une contradiction entre deux README du même dossier.
`1 - Collection/3 - EntrepriseAgentique/README.md` affirme au présent, en six
endroits, que `verification/` et ses 30 rapports « ne se lisent plus qu'à
l'historique git » ; `1 - Collection/README.md:421` le répète et omet le répertoire
de son arbre. Or `git ls-files` en compte 30 sur le disque, restaurés le 21 août
2026 (`696bcac`) — restauration que `1 - Collection/README.md:5` raconte lui-même
huit cents lignes plus haut. Le passé est juste, c'est le présent qui est faux.

*Le reste tient : 521 liens résolvent, aucun chemin daté n'a été réécrit, et les
valeurs republiées se rejouent au chiffre près (check-veille, check-revue, check-toc,
check-sieges, decompte.sh, check-traite, check-article, rejeu-politique — tous à 0).*

**Coût du tour** : bâtisseur 254 k jetons / 85 outils ; critique 186 k / 39 outils.

**Verdict du critique (nouvel agent, tour 2) : NON.**

**Écart retenu** — même famille, autre fichier. `2 - Compendium/PRD/PRD.md:523-524`
date du 1er septembre 2026 l'entrée de l'article, « dixième document publié et
**sixième dossier numéroté** », et pointe vers `4 - Essais/2 - Article/` — qui
n'est ni un dossier numéroté de la racine, ni le sixième : il n'y en a plus que
cinq. L'énoncé était exact à sa date (`git ls-tree 69eeee2` en donne six) ; la
réécriture du chemin sans reprise du dénombrement l'a rendu faux, dans un document
dont l'en-tête se déclare « CLOS ET FINAL ». `PRD.md` est le seul fichier du
périmètre où un chemin a été réécrit sans ancre — les trois autres cas du dépôt
portent la leur.

*Le reste passe : `bash -n` et `py_compile` sur trois scripts shell et cinq Python ;
rejeu réel du build du traité (143 pages, conforme au chiffre publié) et de celui
de la Recension en copie hors dépôt ; les relevés d'octets du 21 août reproduisent
exactement au commit `df9e14e`. Deux liens `../audit.md` morts dans le PRD du
compendium, antérieurs à la réorganisation (`60e1b99`), signalés non corrigés.*

**Coût du tour** : critique 124 k jetons / 39 outils.

## Tour 2 — M2 (reprise sur la contradiction `verification/`)

**Bâtisseur** (nouvel agent) — les deux README disent maintenant au présent que les
30 rapports sont sur l'arbre, sans effacer ni la suppression du 8 août ni la
restauration du 21. Il a trouvé pourquoi la chronique et `git log` semblaient se
contredire : la suppression (`659241b`) porte sur `1 - Corpus/…`, chemin antérieur
au renommage `1 - Corpus/` → `1 - Collection/` (`d786adb`, 20 août), donc invisible
à un `git log` sur le chemin actuel.

Mesure : **156 renvois vers `verification/`, 156 résolvent, 0 mort.** Les « cent dix
renvois morts » de la chronique datent l'état à la suppression et restent justes
comme relevé.

Deux corrections de plus, dans le périmètre : trois renvois que le README avait
dégradés en texte nu — en invoquant une disparition qui n'a pas tenu — sont
redevenus des liens ; et `verification/`, que l'arborescence plaçait sous
`monographie/`, est remis à la racine du volume.

**Coût du tour** : bâtisseur 133 k jetons / 41 outils. Critique en cours.

## Tour 3 — M3 (reprise sur `PRD.md`)

**Bâtisseur** (nouvel agent) — les deux énoncés datés du PRD reprennent `6 - Article/`,
le nom du dossier au 1er septembre 2026, et portent l'incise d'ancrage vers le chemin
d'aujourd'hui plus la mention que la racine passe de six dossiers numérotés à cinq.
Patron identique à celui de `CLAUDE.md:104`, `DEVELOPPEMENT.md:55` et `build-pdf.sh:13` :
une incise dans la phrase datée, pas un paragraphe neuf qui rouvrirait un document
déclaré « CLOS ET FINAL ».

Dénombrement vérifié : `git ls-tree da6255b` donne six dossiers numérotés à la racine
au 1er septembre, `HEAD` en donne cinq. L'énoncé était exact à sa date.

Balayage des 903 lignes du fichier sur trois axes (chemins réorganisés, 23 liens
relatifs résolus un à un, énoncés de rang et de dénombrement) : rien d'autre à
corriger. Deux liens `../audit.md` (L6, L595) restent cassés — le fichier n'existe
ni à `69eeee2` ni à `HEAD`, la casse précède la réorganisation, laissée et signalée.

**Coût du tour** : bâtisseur 87 k jetons / 20 outils. Critique en cours.

**Verdict du critique (nouvel agent, tour 2) : OUI — l'artefact tient.**

478 liens relatifs résolvent, 0 mort. Les trois renommages sont annotés de façon
identique et exacte dans les quinze fichiers. Le bloc de rejeu daté du 5 septembre
se reproduit au signe près. Un lecteur qui arrive sur `4 - Essais/` comprend le
regroupement sans index : chaque sous-README se déclare « premier / second dossier
des Essais » et renvoie à l'autre.

**Sortie de boucle sur ce morceau : verdict positif au tour 2.**

**Écart résiduel, reporté au lissage** — `4 - Essais/2 - Article/README.md:20-22`
avertit que la chronique de `1 - Collection/README.md` « s'arrête à la onzième
réouverture » et ne porte pas les passes du 22 au 28 août. Or ce fichier les porte,
et l'avertissement et le comblement ont été écrits **dans le même commit** (`c81be4a`,
1er septembre) : l'avertissement était faux dès sa première seconde. Défaut
préexistant, sans rapport avec la réorganisation, mais c'est le seul endroit des
quinze où un README envoie le lecteur se défier d'un autre à tort.

**Coût du tour** : critique 206 k jetons / 30 outils.

**Verdict du critique (nouvel agent, tour 3) : OUI — l'artefact tient.**

Les trois chaînes de fabrication tournent de bout en bout depuis les dossiers
réorganisés : traité (143 p., parité d'octets refaite à l'identique), veille
(144 et 59 p.), recension (186 et 7 p.) — cette dernière franchissant l'appel
inter-dossiers `../3 - Veille/Python/check-resume.py`, qui était le point de
rupture réel de la réorganisation. Les cinq `check-*.py` compilent et sortent 0.
Zéro lien mort dans le périmètre, sauf les deux `../audit.md` préexistants.

**Sortie de boucle sur ce morceau : verdict positif au tour 3, budget épuisé.**

**Écart relevé hors périmètre — un trou dans le découpage, pas dans le travail** :
`2 - Compendium/PRD/TOC.md:12` porte un lien vivant vers `4 - Veille/Veille
Technologique.md` qui ne résout plus. Ce fichier n'était assigné à aucun des trois
morceaux. Sur dix liens relatifs morts dans le dépôt hors README, c'est le seul qui
contienne un ancien chemin — donc le seul vrai oubli de réécriture. Reporté au lissage.

*Défaut préexistant signalé, non corrigé : `4 - Essais/1 - Traité/audit.md:3` annonce
« 78 fichiers .rs » au commit `a7df123` ; les 29 690 lignes se reproduisent exactement,
mais sur 76 fichiers.*

**Coût du tour** : critique 135 k jetons / 47 outils.

---

# Phase 5 — passe de lissage

Trois morceaux améliorés séparément par des agents qui ne se voyaient pas. Un agent
neuf reprend l'ensemble : le fichier oublié de tous (`TOC.md`), le faux avertissement
entre deux README, le balayage des coutures, et les divergences de registre, doublons
et contradictions chiffrées que trois voix produisent forcément.

**Ce que le lissage a rattrapé** — 5 fichiers, 2 liens morts fermés, 4 registres remis
d'accord. Trois trouvailles que le découpage en morceaux ne pouvait pas voir :

1. `2 - Compendium/PRD/TOC.md:12` — lien vivant vers `4 - Veille/`. Fichier assigné à
   aucun des trois morceaux : trou de découpage, pas défaut de bâtisseur.
2. `4 - Essais/1 - Traité/docs/README.md:10` — `../../README.md` cassé par la descente
   d'un niveau. Vrai dommage de la réorganisation, oublié de tous.
3. **Le faux avertissement était recopié** dans le `README.md` racine (l. 77-79), où le
   pli de ligne le cachait à un `grep`. Corrigé une fois, puis remplacé par un renvoi au
   lieu du doublon — ce qui est exactement le geste que cette phase existe pour faire.

Plus `APPAREIL.md:123-128`, devenu faux (« le reste du dépôt n'a pas été repris »,
« 70 mentions ») du fait même du travail des morceaux 2 et 3.

**Coût** : 233 k jetons / 80 outils.

---

# Vérification finale, faite à la main

Vérificateur écrit indépendamment de ceux des agents — se faire vérifier par l'outil de
celui qui a fait le travail ne prouve rien. Il a d'abord accusé 42 morts : défaut du
vérificateur, pas du dépôt (la forme `[texte](<url>)` à chevrons, que la regex prenait
au pied de la lettre). Corrigé, il donne :

```
220 fichiers .md versionnes, 1989 liens relatifs, 3 MORTS
  MORT 2 - Compendium/PRD/PRD.md:6    -> ../audit.md
  MORT 2 - Compendium/PRD/PRD.md:597  -> ../audit.md
  MORT 2 - Compendium/PRD/TOC.md:4131 -> ../audit.md
mentions d'anciens chemins : 100 (30 Traité, 38 Veille, 32 Article)
```

Les trois morts sont **antérieurs à la réorganisation** : `git ls-tree HEAD~1` ne montre
aucun `audit.md` sous `2 - Compendium/`, supprimé le 2 septembre (`60e1b99`). Aucun des
trois n'est imputable à cette passe, et les délier serait une décision d'auteur.

`bash -n` passe sur les trois `build-pdf.sh`, `py_compile` sur les `check-*.py`, et la
porte inter-dossiers réparée (`5 - Recension/build/build-pdf.sh:58` →
`../3 - Veille/Python/check-resume.py`) résout.

Les 100 mentions d'anciens chemins ne sont pas une dette : la règle d'ancrage **ajoute**
le nom d'aujourd'hui sans retirer l'ancien, donc le compte monte quand le travail avance.
81 portent leur ancrage sur la même ligne, 12 dans le paragraphe voisin, 5 sont des
relevés datés en bloc de code, 2 ont été inspectés à la main.

---

# Bilan

| Morceau | Tours | Sortie |
|---|---|---|
| M1 — carte du dépôt | 1 | **victoire à l'aveugle** contre le README d'avant |
| M2 — quinze README de branche | 2 | verdict positif |
| M3 — outillage et texte courant | 3 | verdict positif, budget épuisé |
| Lissage | — | 5 fichiers, 3 trouvailles inter-morceaux |

Budget annoncé : 3 tours. Tenu. **11 agents**, ~1,8 M jetons.

**Ce que la boucle a produit que la demande ne demandait pas** : un script de fabrication
réellement cassé, réparé (`5 - Recension/build/build-pdf.sh`) ; trois relevés datés
sauvés d'une falsification par réécriture ; une contradiction entre deux README sur
trente rapports déclarés supprimés mais présents ; un faux avertissement recopié à deux
endroits. Aucun de ces défauts n'est un lien mort — un `sed` les aurait tous manqués,
et en aurait créé trois.

**Ce qui reste, et qui demande une décision d'auteur, pas une passe** : les trois renvois
vers `2 - Compendium/audit.md`, supprimé sur décision — le restaurer ou délier les renvois
n'est pas un arbitrage de documentation. Et le dépôt n'a toujours aucun contrôle qui
résolve un lien Markdown : c'est ce trou qui a laissé mourir 27 renvois en août et 18 de
plus le 5 septembre. Le vérificateur de cette passe est resté hors du dépôt ; l'y verser
fermerait la classe entière de défauts, mais c'est un ajout, pas un lissage.
