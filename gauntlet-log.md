# Journal de boucle gauntlet — audit du compendium et des fichiers `.md`

Append-only. Un bloc par tour : morceau, verdict, écart retenu.

**Barre retenue** (choix de l'auteur) — en deux temps :

1. **Contrôle vert + zéro divergence.** Les cinq contrôles du dépôt sortent 0 ; chaque décompte
   annoncé comme état courant est re-mesuré sur la pièce et concorde ; zéro lien interne mort hors
   produits d'assemblage.
2. **Lecteur neuf sans contradiction.** Un critique qui n'a jamais vu le dépôt lit le seul
   `README.md` racine et doit énoncer sans contradiction l'état, la pagination et la publiabilité
   des cinq livrables.

**Gestes réservés — arbitrage de l'auteur.** Normaliser la casse du PDF : *oui*. Réparer
`assemble.py` du Vol. II : *oui*. Retirer les renvois morts : *oui*. Déposer une licence et poser
l'étiquette `mono-v1.0` : *non* — restent ouverts et signalés.

---

## Tour 0 — ligne de base, mesurée avant toute écriture

| Mesure | Commande | Valeur |
|---|---|---|
| Fichiers `.md` | `find . -name '*.md' -not -path './.git/*' \| wc -l` | 197 |
| Fichiers `.html` | idem `*.html` | 51 |
| `README.md` au suivi git | `git ls-files \| grep -c 'README.md'` | 12 |
| Liens relatifs internes | balayage `[..](..)` sur les 197 `.md` | 1 795 |
| dont morts | idem | **274**, sur **52** fichiers (123 dans `2 - Compendium/build/compendium-assemble.md`, produit d'assemblage) |
| `Compendium.pdf` | décompte `/Type /Page` | **1 114 p.** — le `README.md` racine en annonce **1 096** à cinq endroits d'état courant |
| `.pyc` au suivi git | `git ls-files \| grep -E '\.pyc\|__pycache__'` | **0** — le `README.md` en annonce **trois** encore versionnés : constat périmé |
| Casse du PDF | `git ls-files '2 - Compendium'` | `compendium.pdf` à l'index, `Compendium.pdf` au disque |
| `check-veille.py` | `python check-veille.py` | sortie 0 |
| `check-toc.py` | `python check-toc.py` | sortie 0 |
| `check-sieges.py` | `python check-sieges.py` | sortie 0 |
| `check-compendium.py` | `python check-compendium.py` | sortie 0 |
| `decompte.sh` | `bash decompte.sh --verifier` | sortie 0 — **sans argument, sortie 2** (message d'usage) : l'annonce « sortie 0 » du `README.md` n'est vraie qu'avec `--verifier`, qu'aucune des occurrences ne cite |
| Volumétrie Vol. I | `decompte.sh --verifier` | 225 258 (commande de référence) / 233 257 (`wc -w` brut, « chiffre publié ») — le `README.md` racine annonce **≈ 263 600 mots** : divergence à instruire |

Chapitres du compendium re-comptés : Livre I 11, II 10, III 15, IV 10, V 4 = **50**. Concorde avec
l'annonce.

⚠ **Correction de méthode, en deux temps — et le second temps corrige le premier.** *(1)* J'ai d'abord
écrit que `grep -c '/Type /Page'` rendait « exactement le double » de la pagination (2 228 pour 1 114),
et publié cette mise en garde dans deux `README.md`. *(2)* **Le critique du morceau C l'a réfutée en
réexécutant la commande, et il avait raison sur les cinq PDF** : avec l'espace, le motif rend **0** —
Typst écrit `/Type/Page` sans espace ; le doublement que j'avais mesuré venait de ma propre classe
d'exclusion `[^s]`, qui écartait `/Type/Pages` mais **laissait passer `/Type/PageLabel`**, dont il
existe un objet par page ; et le motif correctement ancré rend la pagination juste du premier coup —
`grep -aoP '/Type/Page(?![sL])' | wc -l` donne **569, 387, 427, 1 114, 161**. Les chiffres du tableau
ci-dessus viennent du `/Count` de l'objet `/Type /Pages` et sont justes ; c'était **l'explication** qui
était fausse. *Publier une commande de contrôle sans l'avoir réexécutée sur son domaine entier est
exactement la faute que ce dépôt prend pour objet — et c'est le critique, non le bâtisseur, qui l'a
vue.* `pypdf`, que cinq documents du dépôt citent comme instrument de mesure, **n'est pas installé**
dans cet environnement.

---

## Tour 1 — trois morceaux à propriété de fichiers disjointe

Découpe par **propriété exclusive de fichiers**, pour que deux bâtisseurs n'écrivent jamais le même
fichier : **B** = `2 - Compendium/`, **C** = `1 - Corpus/`, **A** = `README.md` racine. A passe après
B et C, ses chiffres dépendant de ce qu'ils corrigent réellement.

### Morceau C — `1 - Corpus/`

**Artefact** : 39 fichiers modifiés — les 2 `assemble.py`, 28 pièces du Vol. II en chirurgie de lien,
les 2 `Monographie.md` régénérés, `prd/audit.md`, `verification/relecture-CA.md`, le `PRD.md` et le
`PRDPlan.md` du Vol. III, et 4 `README.md`.

**Ce que le bâtisseur a trouvé que la ligne de base ne portait pas** :

- La panne du Vol. II était bien dans le chemin seul (`ROOT / "TOC.md"` au lieu de `ROOT / "prd" /
  "TOC.md"`). Contrôle décisif avant toute autre écriture : chaque assembleur **reproduit son
  `Monographie.md` versionné à l'octet près**, ce qui borne la panne au chemin.
- **Le Vol. III portait le même défaut de rebasage de liens que le Vol. II** — il n'était donc pas le
  témoin sain sur ce point (19 renvois morts de son côté). Correction dans les deux scripts.
- Les 17 renvois de `prd/audit.md` sont des locateurs `fichier.md:ligne` : préfixer `../` ne suffisait
  pas, le suffixe `:21` invalidant le chemin. Convertis en ancres `#L21`.
- Le total du corpus annoncé « ≈ 516 500 (> 500 000) » repose sur un Vol. I à ≈ 263 600 mots que
  **aucune commande du dépôt ne produit**. Recalculé : **486 206**. *Le corpus perd le seuil des
  500 000 qu'il s'attribuait.*

**Liens morts : 116 → 14** (balayage indépendant après la passe : 14, hors produit d'assemblage). Les
14 restants sont instruits, non rafistolés : cibles supprimées du dépôt sans remplacement
(`Borealis-Go/`, `Synthese Monographie.md`), renvois à un `CLAUDE.md` qui n'existe nulle part, un faux
positif (gabarit d'en-tête dans un bloc `sh`, correct à sa profondeur de destination) et cinq liens
internes de pages tierces cités **verbatim** dans des blockquotes de preuve.

**Laissé ouvert et signalé, conformément à l'arbitrage** : l'étiquette `mono-v1.0` est annoncée comme
posée par 4 documents de gouvernance et 17 pièces alors que `git tag -l` est **vide** — prose non
réécrite. Deux contradictions internes remontées à l'auteur : l'Annexe B du Vol. I déclarée
« ≈ 17 500 mots » contre **20 655** mesurés, dans un fichier dont l'en-tête revendique que tout
décompte est relevé et non projeté ; et trois volumétries concurrentes du Vol. II, toutes justes sous
leur méthode (92 059 / 93 242 / 90 362).

**Verdict du critique** (contexte neuf, sans le rapport du bâtisseur) — barre **tenue sur 4 points sur
5** :

| Point de barre | Verdict | Preuve du critique |
|---|---|---|
| Prose des pièces rédigées intacte | **tenu** | 48 paires de lignes changées sur 28 pièces, **48 où seule la cible de lien diffère, 0 prose**, hunks tous symétriques |
| Chaîne d'assemblage du Vol. II | **tenu**, et au-delà | les deux assembleurs reproduisent leur sortie **à l'octet** (874 348 o, 1 123 985 o) ; chaîne complète rejouée jusqu'à `typst compile` → **387 p.**, la pagination publiée |
| Statuts non requalifiés | **tenu** | les mentions « non publiable » vérifiées une à une ; les deux requalifications du diff portent sur des **sièges**, et `check-sieges.py` les confirme |
| Liens internes | **tenu sur la substance** | 6 morts sur 671, **aucun n'est un renvoi du dépôt** : 5 URL site-relatives de tiers citées *verbatim*, 1 gabarit dans un bloc `sh` |
| Chiffres d'état courant | **non tenu** | une commande de contrôle publiée qui ne rend pas ce qu'elle annonce |

**Écart retenu — un seul, et il vise le bâtisseur, pas le corpus.** *Le paragraphe écrit pour réparer
une faute de méthode en commet une de la même classe, et c'est le seul endroit du corpus où une commande
publiée, réexécutée, échoue.* La mise en garde contre `grep -c '/Type /Page'` était fausse en trois
points : le motif rend **0** (Typst écrit `/Type/Page` sans espace) ; le « double » venait d'une classe
d'exclusion qui laissait passer `/Type/PageLabel`, un objet par page ; un motif ancré donne la
pagination juste du premier coup. Partout ailleurs les décomptes de ce corpus se reproduisent à
l'unité — y compris les **onze blocs de volumétrie** du Vol. III et les **57 en-têtes de remontées** —,
et c'est ce contraste qui rend le défaut visible.

**Rebouclage appliqué dans le tour** — huit corrections, toutes issues du critique :

1. La mise en garde fausse est récrite aux **trois** endroits où elle vivait (`README.md` racine,
   `1 - Corpus/README.md`, ce journal), avec la commande qui marche et le motif de l'erreur.
2. **Vol. III : « 22 lacunes dont 4 closes » → 3 closes.** Vérifié sur le PRD §10 : « INSTRUITE ET
   CLOSE » aux seules entrées 1, 2 et 11 ; la 10 est « non arbitrée », la 15 « **NON CLOSE** » en
   capitales. Corrigé au `README.md` racine et à celui du volume.
3. **Le registre de gel du Vol. III affirmait au présent une concordance que sa propre re-mesure avait
   invalidée.** Somme des 34 en-têtes re-comptée : **160 423** contre **160 890** au registre —
   **écart de 467 mots sur 24 des 34 pièces**. La passe du 24 juillet avait repris le registre sans
   reporter dans les en-têtes, et ne le disait pas. Les en-têtes ne sont pas récrits (constats datés) ;
   c'est **l'affirmation restée au présent** qui est bornée.
4. `build/build-pdf.sh` du compendium écrivait `compendium.pdf` en minuscule : après le renommage, la
   prochaine recomposition aurait produit un **second fichier**. Nom canonique posé dans le script.
5. **Huit renvois morts que le morceau C avait instruits sans refermer** sont retirés — tous vers des
   fichiers **supprimés délibérément** (`f6183bf`, `73e7c4e`, `41666d0`) : le tableau des livrables du
   Vol. I déclarait encore `Synthese Monographie.md` et `Borealis-Go/` présents, et son champ
   « Autorité » **déléguait à un `CLAUDE.md` absent**.
6. **L'Annexe I existe** depuis le 30 juillet 2026 (1 154 entrées) : quatre documents la déclaraient
   « à écrire ».
7. Deux erreurs d'unité : `Compendium.html` **1,75 Mio** et non 1,79 ; le PDF **12,7 Mio** et non
   « 12,7 Mo ».
8. Deux décomptes de renvois corrigés : le chemin de `assemble.py` **n'est pas un renvoi** et sortait du
   total ; et la limite des ancres `#Lnnn` — GitHub ne les honore que sur `?plain=1` — est déclarée.

**Liens morts, mesure finale** : **151 → 6** hors produit d'assemblage, sur 1 641 liens relatifs. Les
6 restants sont ceux qui doivent rester.

### Morceau B — `2 - Compendium/`

**Artefact** : 14 fichiers modifiés, plus le renommage d'index du PDF et le correctif de `build-pdf.sh`.

**Verdict du critique** (contexte neuf) — **3 points de barre sur 5** :

| Point de barre | Verdict | Preuve du critique |
|---|---|---|
| Liens internes | **tenu** | 988 liens relatifs balayés sur 118 fichiers, **0 cassé**, repassé en **casse stricte** composant par composant pour ne pas être aveuglé par NTFS |
| Les cinq contrôles | **tenu** | les cinq exécutés, sorties 0 ; contre-épreuve du piège : `decompte.sh` sans argument → 2 |
| Statuts non requalifiés | **tenu** | rangées `| Statut |` du PRD et du TOC inchangées ; les 50 en-têtes portent toujours « brouillon non publiable » (P1, sortie 0) ; les seuls ☐→☑ portent sur des **sièges**, confirmés par `check-sieges.py` |
| Prose des pièces rédigées | **non tenu** | **deux annexes** ont changé dans leur prose, au-delà d'une cible de lien |
| Chiffres d'état courant | **non tenu** | trois annonces divergent : couverture des figures, attestation de non-blancheur, poids du fichier HTML |

**Écart retenu du critique — la couverture des figures.** Le conspectus et `Compendium.html` affirment
que « les cinquante chapitres en portent au moins une » ; le balayage des cinquante pièces en trouve
**quarante-neuf**, le **ch. 28** n'en portant aucune. ⚠ **Et le volume se réfute lui-même** :
`figures/programme.md` n'accordait au ch. 28 que **deux candidates, toutes deux au barème B**, qu'une
passe de barème A ne pouvait pas couvrir. *Le décompte de 118 figures est juste ; c'est la couverture
qui ne l'était pas.*

**Rebouclage appliqué** : couverture corrigée à « quarante-neuf des cinquante » aux deux endroits, avec
le motif ; attestation de non-blancheur **datée du 30 juillet et bornée** — elle porte sur un rendu de
1 072 pages, que la refonte Letter du 31 juillet a porté à 1 114, *et ne couvre pas les 42 dernières* ;
poids du fichier repris à la source.

**Entorse déclarée plutôt que défaite.** Les deux annexes touchées dans leur prose disaient faux :
`annexe-references.md` déclarait l'Annexe I « reste à écrire » (elle existe depuis le 30 juillet),
`annexe-bibliographie.md` renvoyait à un rapport retiré du dépôt. Les corrections sont conservées et
l'exception est écrite au `README.md` racine. *Une annexe qui se trompe sur le contenu de son propre
volume n'énonce pas un fait daté : elle induit en erreur sur l'état présent.* Les **cinquante
chapitres**, eux, tiennent — deux fichiers touchés, une ligne chacun, texte visible identique.

### Morceau A — `README.md` racine

**Écart le plus lourd trouvé, et il n'était pas un décompte** : le fichier décrivait le compendium comme
**arrêté** sous D-10 / PRD v0.15 / TOC v0.31, alors que **D-11 avait rouvert cet arrêt le 30 juillet
2026** (PRD v0.16, TOC v0.32) sur un rapport d'arbitrage externe concluant à une *révision majeure,
accepté sur le fond, non diffusable en l'état*. **Neuf jours de retard, et la passe du 4 août ne l'a pas
vu.** Corrigé en cinq endroits, avec un paragraphe neuf sur ce que D-11 change et ne change pas.

---

## Tour 1 — comparaison à l'aveugle

**Dispositif** : deux arbres montés dans un répertoire de travail, **étiquettes retirées**, portant les
trois mêmes documents synoptiques (`README.md` racine, conspectus du Vol. IV, synthèse du triptyque). Le
juge — contexte neuf, aucun accès aux rapports des bâtisseurs — reçoit **A** et **B** sans savoir lequel
est la reprise, avec pour seule consigne de mesurer sur le dépôt et de désigner celui qui le décrit
exactement. Ordre à alterner au tour suivant.

**Verdict : A gagne** — et A est la reprise.

> « A concorde avec la pièce sur tout ce qui se mesure […] là où B annonce au présent 1 096 (et 810)
> pages, une gouvernance de neuf jours de retard, un chiffre de mots qu'aucune commande du dépôt ne
> produit, 27 renvois vers un `compendium.pdf` qui n'existe sous ce nom ni sur disque ni à l'index, et
> trois fichiers absents présentés comme présents. **L'écart n'est pas de degré** : B se contredit
> jusqu'à l'intérieur de son propre jeu, son conspectus portant 1 114 pages quand son avant-propos en
> annonce 1 096. »

Douze écarts décisifs relevés par le juge, chacun mesuré par sa propre commande : pagination,
gouvernance courante, volumétrie du Vol. I, agrégat et cardinal des pièces, casse du nom du PDF,
fichiers cités et absents, bytecode au suivi git, assemblage du Vol. II, invocation de `decompte.sh`,
questions ouvertes de la veille, découpage en parties du Vol. II, instrument de pagination déclaré.

**Écart restant du gagnant, un seul** : *le poids de `Compendium.html` est annoncé comme un relevé du
jour (« 1,75 Mio, 1 829 940 octets ») alors que le fichier en pèse 1 826 011 — la conversion fausse a été
corrigée sans reprendre le décompte d'octets à la source.* ⚠ **Le juge a raison, et le défaut est
d'espèce** : 1,75 Mio était juste **pour le 4 août**, faux reporté au présent. Repris à la source en fin
de passe : **1 826 464 octets, soit 1,74 Mio**, fins de ligne `LF` pures, la convention étant désormais
nommée. *Une conversion juste sur un décompte périmé reste un chiffre faux.*

---

## Sortie de boucle

**Victoire à l'aveugle obtenue au premier tour**, et l'écart restant désigné par le juge a été refermé
dans le même tour. La barre 1 est atteinte :

| Point de barre | État final | Mesure |
|---|---|---|
| Cinq contrôles en sortie 0 | **atteint** | `check-veille.py`, `check-toc.py`, `check-sieges.py`, `check-compendium.py`, `decompte.sh --verifier` → 0 |
| Zéro divergence d'état courant | **atteint** sur tout ce qui a été mesuré | voir le registre du `README.md` racine |
| Zéro lien interne mort | **atteint à 6 exceptions instruites** | 6 morts sur 1 641 liens `.md` ; **0** sur 60 liens `.html` |

Les 6 renvois conservés le sont à dessein : **cinq URL site-relatives de tiers citées *verbatim*** dans
des blockquotes de preuve — les réécrire altérerait la citation, qui est l'objet du rapport — et **un
faux positif**, un gabarit d'en-tête dans un bloc `sh` clôturé, correct à la profondeur de sa
destination.

⚠ **Ce que la boucle n'a pas fait, et qui reste à l'auteur** : déposer une licence à la racine ; poser
l'étiquette `mono-v1.0` ou corriger les vingt et un endroits qui l'annoncent posée ; arbitrer les deux
contradictions internes remontées (Annexe B du Vol. I, ≈ 17 500 mots déclarés contre 20 655 mesurés ;
trois volumétries concurrentes du Vol. II). **Aucun statut n'est requalifié, aucune porte franchie,
aucune remontée refermée, rien n'est publié.**

**La leçon du tour, et elle vise le bâtisseur.** Sur les deux défauts les plus instructifs de la passe,
c'est le **critique** qui a vu juste contre lui : la commande de comptage de pages publiée sans avoir été
réexécutée, et la conversion d'octets juste sur un décompte périmé. *Les deux sont exactement la classe
de faute que ce dépôt prend pour objet, et aucune des deux n'aurait été trouvée par le bâtisseur qui
notait son propre travail.*
