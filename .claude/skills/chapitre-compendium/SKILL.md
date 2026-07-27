---
name: chapitre-compendium
description: >-
  Rédiger une pièce du compendium « La somme agentique » (Vol. IV) — un chapitre des Livres I à V,
  l'avant-propos ou une annexe — en deux rendus, le `.md` source et la page `.html` à thème sombre
  orange, dans `2 - Compendium/Livre N/`. Charge ce skill dès que la demande porte sur l'écriture,
  la reprise ou la révision d'une pièce du compendium, même formulée sans son nom : « rédige le
  chapitre 12 », « écris le ch. 37 », « fais le Livre III », « continue la somme », « attaque
  l'avant-propos », « reprends la pièce du maillage », « ajoute un chapitre au compendium ». Il
  s'applique aussi quand la demande vise seulement l'un des deux rendus (« refais le HTML du
  chapitre 1 », « la page du ch. 3 »), puisque les deux se versionnent ensemble. Ne pas l'utiliser
  pour les trois monographies sources (Vol. I, II, III), qui ont leurs propres conventions, ni pour
  la veille technologique de la racine, ni pour éditer le `TOC.md` ou le `PRD.md` du compendium —
  un rédacteur ne les corrige jamais, il remonte.
---

# Rédiger une pièce du compendium

Le compendium est le **Vol. IV** du dépôt : un omnibus qui absorbe les trois monographies en un seul
ouvrage réordonné et dédoublonné, **50 chapitres en 5 livres**. Son plan est entièrement spécifié —
chaque entrée du `TOC.md` **est** le cahier des charges de son chapitre. Rédiger une pièce, ici, ne
veut donc pas dire inventer : cela veut dire **exécuter une spécification déjà écrite**, en signalant
tout ce qui l'en écarte.

C'est la clé du travail. Ce qui distingue une bonne pièce d'une mauvaise n'est pas l'ampleur de la
prose : c'est la fidélité au plan et l'honnêteté sur les écarts.

## 1. D'abord : où en sont les portes ?

Le [`PRD.md`](../../../2%20-%20Compendium/PRD/PRD.md) §5 pose sept portes de lancement. **G-1** (gel
unique), **G-2** (commande de décompte de référence) et **G-3** (refonte du socle) conditionnent
*toute* rédaction ; G-4 à G-7 conditionnent les livres qu'elles nomment. La règle cardinale du
volume :

> *Un chapitre écrit sur un socle vide n'est pas un chapitre en avance, c'est une inférence longue.*

Lire le champ **Statut** du PRD et vérifier l'état réel des portes avant d'écrire une ligne. Deux
cas, et un seul geste les sépare :

- **Portes franchies** — rédiger normalement, socle consolidé à l'appui.
- **Portes ouvertes** (le cas courant à ce jour) — rédiger **est possible sur instruction d'auteur**,
  mais la pièce doit alors **se déclarer brouillon non publiable** et porter en clôture une section
  hors plan qui énumère les conséquences. Voir §7.

Ce qui n'est jamais acceptable, c'est d'écrire hors portes **en silence** : une pièce qui se présente
comme recevable alors que son socle n'existe pas contamine tout ce qui la citera. L'écart se déclare,
il ne se lisse pas.

## 2. Les quatre lectures qui précèdent l'écriture

Aucune ne se saute — chacune ferme une classe d'erreur que les autres ne voient pas.

1. **L'entrée du chapitre au [`PRD/TOC.md`](../../../2%20-%20Compendium/PRD/TOC.md)** (v0.24) :
   thèse, phrase « Sections : … », **ligne Fusion**, table des matières détaillée, table de
   couverture (décision 6), et les écarts que le TOC signale parfois sous l'entrée. C'est le cahier
   des charges ; il ne se résume pas, il se suit.
2. **Le `PRD.md`** : §5 portes, §6 en-tête à cinq champs et ordre de rédaction, §7 régimes de preuve,
   §8 garde-fous et formulations imposées, §11 critères CA-IV-01 à 14.
3. **Le [`CLAUDE.md` du compendium](../../../2%20-%20Compendium/CLAUDE.md)** : plafond de cinquante
   chapitres, cartes de renumérotation chaînées, pièges propres au fichier.
4. **Le texte source**, retrouvé par la ligne Fusion — les chapitres correspondants des Vol. I, II ou
   III sous `1 - Corpus/`. **Condenser suppose d'avoir lu.** Une pièce écrite de mémoire sur un
   corpus qu'on n'a pas ouvert produit du plausible, pas du fidèle.

   ⚠ **Lire l'INTÉGRALITÉ du périmètre de fusion, pas la source que le plan met en avant.** Une ligne
   Fusion cite souvent deux ou trois provenances, et le TOC ne commente d'ordinaire que celle qui
   porte la thèse. Lire l'autre **jusqu'au bout** : c'est là que se logent les faits qui périment un
   énoncé du plan. **La faute a déjà été commise sur le ch. 7**, dont la ligne Fusion cite le Vol. I
   §3.0-3.1 **et §3.13.1** en plus du Vol. II ch. 1 : la pièce a repris du plan « transfert de
   gouvernance annoncé, non vérifié au socle » alors que le §3.13.1 — sa propre source — portait le
   fait daté et sourcé. Corrigé au ch. 10 § 10.1.3, remontée R-IV-12.

   ⚠ **Comparer la thèse du TOC au texte rédigé de sa source AVANT d'écrire.** La thèse se cite
   **verbatim**, le PRD l'exige — mais elle peut avoir été **bornée à la source après la passe de plan
   qui l'a reprise**. Le Livre II l'a payé cinq fois sur dix chapitres : quantificateur universel
   négatif, verbe que R-02 proscrit, proportion non dénombrée, échéance empruntée à une entrée [C].
   *La pièce cite verbatim et **écrit son corps sous la forme bornée**, puis remonte l'écart* — mais le
   repérage se fait **avant la rédaction**, pas au moment de la relecture.

   ⚠ **Et quand deux volumes divergent, vérifier d'abord que c'en est une.** « Le socle de A ne
   documente pas X » et « B documente X » sont **logiquement compatibles** : c'est une **lacune de
   couverture**, pas une contradiction, et elle se traite en exposant les deux états datés — jamais
   en corrigeant le volume le plus ancien, dont l'énoncé reste exact dans son périmètre.

Puis lire [`references/conventions.md`](references/conventions.md) de ce skill : renvois, marqueurs,
garde-fous, et les pièges qui ont déjà coûté une passe.

⚠ **En cas d'écart entre la phrase « Sections : … » et la ligne Fusion, la ligne Fusion prime** —
c'est elle qui porte l'arbitrage de provenance. La table détaillée n'est que son dépliage, et se
corrigera sur le chapitre rédigé, jamais l'inverse (décision 8 du TOC). Quand l'écart est réel,
suivre la ligne Fusion **et le signaler en remontée** (§8) : la liste de sections se réaligne par une
passe du `TOC.md`, hors mandat d'un rédacteur.

## 3. Le squelette de la pièce

Une pièce se compose toujours des mêmes blocs, dans cet ordre. Le gabarit commenté est en
[`references/gabarit-piece.md`](references/gabarit-piece.md) — le copier plutôt que le reconstruire.

1. **Titre** — `# Chapitre N — <titre exact du TOC>`, suivi d'une ligne de situation (livre,
   mouvement, position dans le mouvement).
2. **En-tête à cinq champs** (PRD §6), en tableau : *Statut*, *Date de gel*, *Socle mobilisé*,
   *Garde-fous balayés*, *Volumétrie cible*. Aucun n'est décoratif ; §4 dit ce que chacun doit
   contenir.
3. **La thèse**, citée depuis le TOC, en bloc de citation, avec sa provenance.
4. **Les sections**, `## § N.M`, dans l'ordre exact de la table détaillée du TOC, sous-sections
   incluses.
5. **Une section de sortie** — « Synthèse : ce que le chapitre lègue à la somme » — quand la table
   détaillée en prévoit une. C'est une **construction d'éditeur**, à déclarer telle.
6. **La note de statut**, seulement si la pièce est écrite hors portes (§7).

## 4. Les cinq champs, et ce qu'ils refusent

L'en-tête est l'endroit où une pièce dit ce qu'elle vaut. Le remplir mollement vide la méthode du
volume de son contenu.

**Statut** — « rédigé » ou « brouillon, non publiable », avec le motif. Si les portes ne sont pas
franchies, le dire ici, en toutes lettres, avec la date de l'instruction d'auteur.

**Date de gel** — le gel unique du compendium relève de la décision **D-1**. Tant qu'elle n'est pas
prise, écrire « Aucune » et nommer le gel de la source (juin 2026 pour le Vol. I, 16-17 juillet 2026
pour le Vol. II, 21 juillet 2026 pour le Vol. III) **en précisant qu'il n'en tient pas lieu**.
Emprunter le gel d'une source, c'est dater la somme d'une date qui n'est pas la sienne.

**Socle mobilisé** — tant que G-3 est ouverte, l'Annexe B n'existe pas et le socle consolidé compte
zéro entrée. Écrire contre quoi les énoncés résolvent réellement, et à quel régime : les faits du
Vol. I entrent en **[C]** (PRD §7.1 — sa vérification porte sur les références, non sur le contenu
des affirmations), ceux du Vol. II et du Vol. III conservent leur niveau d'origine. En **[C]**, la
conséquence se tire : **aucun énoncé n'est central au sens de CA-IV-01**, et il faut le dire.

**Garde-fous balayés** — les deux séries héritées, **R-1 à R-8** (Vol. II) et **R-01 à R-14**
(Vol. III), nommées par volume. La contrepartie est obligatoire : **déclarer aussi les zéros**. Un
chapitre pré-agentique n'a aucune occurrence de la plupart des garde-fous, et c'est cette déclaration
— non le silence — qui prouve que le balayage a eu lieu. Signaler les faux amis : « plan de
contrôle » au sens du maillage de services pré-agentique n'est pas le « control plane » que R-13
proscrit nu.

**Volumétrie cible** — le TOC ne donne d'enveloppe qu'au **Livre**, pas au chapitre. Dériver la
cible, écrire d'où elle vient, et rappeler que **tant que G-2 est ouverte aucun décompte n'est
publiable**. Le Vol. II a payé l'ordre inverse : commande de décompte publiée après avoir été testée
sur deux fichiers pour vingt-neuf, puis **quatre mesures successives** avant d'arrêter un chiffre —
chacune vraie à sa date et fausse à la suivante.

## 5. Écrire le corps

Le registre du dépôt s'applique intégralement : **français canadien soutenu**, ton professionnel et
neutre, ni marketing ni première personne, terminologie technique anglaise entre parenthèses à la
première occurrence.

Deux dispositifs hérités du Vol. I sont reconduits dans le Livre I et se citent tels quels : les
encadrés **« Perspective recherche »** (formalismes, résultats d'impossibilité) et **« Mise en
œuvre »** (normes datées, outils, déploiement). Ils cessent au Livre III, dont la matière
réglementaire ne s'y prête pas.

Ce qui fait la valeur d'une pièce du compendium, et qu'une simple condensation manquerait : **elle
dit ce qu'elle lègue**. Le compendium existe pour que chaque notion soit posée **une seule fois**.
Quand une section pose un socle que des chapitres aval réutiliseront, le nommer — « le ch. 37 en fait
un point d'application de l'identité ; il ne redémontre pas le patron ». C'est l'économie qui
justifie la refonte des trois volumes en un ouvrage ; chaque chapitre aval qui reconstruit annule
cette économie.

⚠ **Ne jamais écrire une section dont le plan déclare le socle « à établir avant rédaction ».** Le
TOC marque certaines sections « front neuf — sources primaires à établir **avant rédaction** ». Quand
ces sources ne l'ont pas été, **le seul geste admissible est d'exposer le vide et de formuler la
question instruisible** — corpus à ouvrir, critère de clôture — sans écrire une ligne de contenu
plausible. Trois motifs : le régime de preuve l'interdit (CA-IV-01) ; *une lacune déclarée ne se comble
pas par une source de moindre qualité* ; et **une construction d'auteur produite à l'endroit exact où
le socle est muet est celle qu'aucune relecture ne peut réfuter, faute de fait auquel la confronter**.
Le § 17.5 du ch. 17 en est le cas de référence (remontée R-IV-27).

Symétriquement, **déclarer ce qui n'est pas traité et pourquoi**. Les sorties de périmètre sont
écrites dans la table de couverture ; les répéter dans le corps, au moment où le lecteur les
attendrait, évite qu'on les prenne pour un oubli.

Trois marquages ne sont pas négociables, parce qu'ils portent le régime de preuve :

- **`Lecture de l'auteur`** devant toute construction d'auteur (CA-IV-07), suivi de ce que le socle
  établit et n'établit pas. Une inférence non marquée devient un fait au premier lecteur pressé.
- **Les trois degrés d'absence** (R-14 du Vol. III) : *fait négatif vérifié* > *fait négatif établi*
  > *absence de documentation*, jamais interchangeables. « Aucun modèle ne traite X » est presque
  toujours une absence de documentation, pas un fait négatif vérifié — l'écrire ainsi.
- **Les métriques auto-déclarées** attribuées **à chaque occurrence**, sans exception d'usage
  illustratif (PRD Vol. II §7.5).

Le détail des conventions de renvoi, des formulations imposées et des pièges se lit dans
[`references/conventions.md`](references/conventions.md). Deux valent d'être ici, parce qu'on les
casse sans s'en apercevoir : le compendium **sépare** sa section du § par une espace (`ch. 44 §
44.1`) là où un renvoi vers une source **la colle** (`Vol. I `*Monographie*` §1.3.4`) ; et **toute
table porte une légende**, faute de quoi elle consomme un numéro et creuse un trou dans la série.

## 6. Les deux rendus

Chaque pièce existe en `.md` et en `.html`, **versionnés ensemble**, dans
`2 - Compendium/Livre <N>/`, nommés `NN-slug.md` / `NN-slug.html`.

Le `.md` **fait foi**. Le `.html` est un **rendu** : toute correction se fait dans le `.md` puis se
reporte, au même commit — jamais l'inverse, jamais l'un sans l'autre. C'est la transposition de la
règle « PDF versionné avec sa source » du dépôt. Le compendium n'a **pas** de pipeline de rendu : les
trois copies du FESP appartiennent aux Vol. I, II et III, et aucune n'a été copiée ici — le `.html`
s'écrit à la main depuis le gabarit.

**Le rendu se génère, il ne se recopie pas** :

```bash
python .claude/skills/chapitre-compendium/scripts/rendre-piece.py "2 - Compendium/Livre I/NN-slug.md"
```

Le script projette le `.md` sur [`assets/gabarit.html`](assets/gabarit.html) — sections, ancres,
navigation, encadrés, tables et légendes, marquage « Lecture de l'auteur ». Écrire les dix pages
d'un livre à la main garantit qu'elles divergeront : une classe oubliée sur un encadré, une ancre
qui ne suit plus son titre, une légende perdue. Le générateur ne produit pas ces défauts ; il en
produit d'autres, du balisage resté littéral, que le contrôle [8] attrape.

Le gabarit porte : thème sombre orange, CSS et script
intégrés, **aucune ressource externe** (ni police, ni image, ni script distant), prose justifiée avec
césure, navigation de chapitre, barre de progression, styles d'impression. Les marqueurs du corpus y
ont déjà leur traitement — `.avert` pour les ⚠, `.encadre--recherche`, `.encadre--oeuvre`,
`.auteur` pour « Lecture de l'auteur ». Le gabarit porte ses points de substitution en commentaire.

⚠ La césure s'appuie sur `lang="fr-CA"` : le retirer la désactive **sans prévenir**, et une
justification sans césure creuse des lézardes dans une colonne de cette largeur.

⚠ Ce n'est **pas** une page de publication en ligne. Aucune balise `canonical` ni `og:url`, aucune
adresse GitHub Pages : les deux `index.html` du dépôt ont été supprimés le 22 juillet 2026 (commit
`fd8f1be`) parce qu'ils annonçaient des adresses fausses. Ne pas les rétablir par inadvertance.

## 7. Écrire hors portes — le régime de déclaration

Quand la pièce est rédigée avant G-1/G-2/G-3, elle porte en clôture une section **hors plan**,
numérotée à la suite, intitulée « Note de statut » et marquée **à retirer à la publication**. Elle
contient :

- **ce qui est enfreint** — quelles portes, quelle règle du PRD, sur quelle instruction et à quelle
  date ;
- **les conséquences**, une par une : aucun énoncé central au sens de CA-IV-01 ; aucun décompte
  publiable ; les renvois « ch. N » sont des **renvois de plan, non de texte** tant que les chapitres
  cibles ne sont pas rédigés, et se re-vérifieront contre le texte quand il existera ;
- **les remontées ouvertes** (§8) ;
- **ce qui n'est pas enfreint** — structure suivie, table de couverture respectée, garde-fous
  balayés, inférences marquées. Cette dernière liste n'est pas de la coquetterie : elle dit au
  relecteur ce qu'il n'a pas besoin de revérifier.

## 8. Ce qu'un rédacteur ne touche jamais

La règle d'escalade du PRD (Annexe A) est explicite :

> *Un rédacteur ne corrige jamais le TOC, ce PRD ni le Conspectus — il **remonte**.*

Donc : ne pas éditer `PRD/TOC.md`, `PRD/PRD.md`, ni le `README.md` du compendium (le conspectus),
même quand on y voit une erreur, **surtout** quand on y voit une erreur. Ouvrir une remontée dans la
note de statut de la pièce, numérotée `R-IV-NN`, avec son objet, son caractère bloquant ou non, et le
chapitre qu'elle bloque le cas échéant. Une remontée marquée « bloquant pour le ch. N » **interdit de
lancer le ch. N**.

Les documents qui décrivent l'état du dépôt, eux, se mettent à jour : le `CLAUDE.md` du compendium,
le `README.md` et le `CLAUDE.md` de la racine, quand ils affirment quelque chose que la nouvelle
pièce dément. Y signaler le fait **sans requalifier le volume** — un brouillon écrit hors portes ne
fait pas passer le Vol. IV de « cadrage » à « rédigé ».

⚠ **Ne jamais corriger la veille technologique** pour tenir compte d'une pièce neuve. Sa réf. [220]
décrit le Vol. IV comme un cadrage sans chapitre, et cela **reste vrai à sa date**. Une revue publiée
décrit l'état de ses sources à son gel ; la rattraper après coup effacerait la seule information
qu'elle porte. Le fait se signale au `CLAUDE.md` de la racine, jamais dans la veille.

## 9. Contrôles avant de committer

Dans cet ordre, et sans en sauter :

```bash
# 1. Contrôles mécaniques de la pièce : structure HTML, ancres, liens, parité md/html
python .claude/skills/chapitre-compendium/scripts/verifier-piece.py "2 - Compendium/Livre I/01-slug"

# 2. Contrôle inter-pièces : qu'un siège déclaré ne soit pas reconstruit ailleurs
python "2 - Compendium/PRD/check-sieges.py"  # S1-S5, sortie 0 exigée

# 3. Contrôles du dépôt — même si on croit n'avoir pas touché à leur domaine
python "2 - Compendium/PRD/check-toc.py"    # C1-C15, sortie 0 exigée
python check-veille.py                       # sortie 0 exigée
```

⚠ **`check-sieges.py` est le seul qui lise plusieurs pièces à la fois, et c'est pour cela qu'il
existe.** L'économie qui justifie la refonte des trois volumes en un ouvrage repose sur des
**sièges** — une matière posée **une seule fois** —, et jusqu'à la v0.24 aucun instrument ne
vérifiait l'abstention : `check-toc.py` ne lit pas les pièces, `verifier-piece.py` n'en connaît
qu'une. Trois sièges y sont déclarés (socle IAM au ch. 3 ; encadré R-8 au ch. 7 § 7.5 ; mécanique de
la fusion au ch. 8 § 8.5.1). **Un siège neuf s'ajoute à la table `SIEGES` du script**, et la pièce
qui le porte doit écrire son marqueur `SIÈGE DE … POUR TOUTE LA SOMME` — sans quoi aucun rédacteur
aval ne peut savoir qu'il doit s'abstenir. *Ce qu'aucun outil ne regarde finit par diverger.*

⚠ **Décompte** : depuis le franchissement de **G-2** (27 juillet 2026), les décomptes **sont
publiables**, et [`PRD/decompte.sh`](../../../2%20-%20Compendium/PRD/decompte.sh) en est la **seule
autorité** — jamais `wc -w`, qui sur-compte la ponctuation de balisage d'environ 3,5 %. Écrire le
réel à côté de la cible dans le champ *Volumétrie cible*, et **ne jamais corriger un écart par
amputation ni par gonflement**.

Puis **regarder la page**. Un rendu qui passe les contrôles peut être illisible : une valeur CSS
invalide, un encadré qui déborde, une légende collée au paragraphe suivant. Chromium est disponible
dans l'environnement ; `references/controles.md` donne la commande de capture et les trois cadrages
utiles.

⚠ Un contrôle en échec **interdit de pousser**. La consigne de flux du dépôt — committer tout et
pousser sur `main` — ne dispense d'aucun contrôle ; elle supprime l'étape de revue, pas la relecture.

## 10. Committer

Les deux rendus **dans le même commit**, avec les fichiers de documentation mis à jour s'il y en a.
Message court, en français, nommé par livrable, dans la manière du dossier :

```
Livre I — chapitre 3 rédigé en .md et .html (brouillon hors portes)
```

Le corps du message dit ce que la pièce couvre, ce qu'elle enfreint, ce qu'elle ne touche pas, et
les contrôles exécutés avec leur résultat. Puis pousser sur `main`, selon la consigne de flux du
[`CLAUDE.md` de la racine](../../../CLAUDE.md).

## Fichiers de ce skill

| Fichier | Quand le lire |
|---|---|
| [`references/conventions.md`](references/conventions.md) | **avant d'écrire** — renvois, marqueurs, formulations imposées, pièges datés |
| [`references/gabarit-piece.md`](references/gabarit-piece.md) | au moment de créer le `.md` — squelette commenté à copier |
| [`references/controles.md`](references/controles.md) | au moment de vérifier — commandes de contrôle et de capture |
| [`assets/gabarit.html`](assets/gabarit.html) | au moment de créer le `.html` — thème et structure, à substituer |
| [`scripts/rendre-piece.py`](scripts/rendre-piece.py) | à chaque passe — génère le `.html` depuis le `.md`, sur le gabarit |
| [`scripts/verifier-piece.py`](scripts/verifier-piece.py) | à chaque passe — huit contrôles mécaniques sur les deux rendus |
| [`scripts/verifier-piece-mutations.py`](scripts/verifier-piece-mutations.py) | **seulement si le vérificateur est modifié** — douze mutations, à repasser avant de publier le changement |
