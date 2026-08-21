---
title: "Revue de la littérature académique"
subtitle: "Interopérabilité et Orchestration Agentiques"
author:
  - "André-Guy Bruneau, M.Sc. IT · agbruneau@gmail.com · 15 août 2026"
lang: fr
region: CA
papersize: us-letter
fontsize: 10pt
linestretch: 0.95
mainfont: "New Computer Modern"
margin:
  x: 117pt
  y: 72pt
section-numbering: "1.1.1"
abstract-title: "Résumé"
abstract: |
  Cette revue examine la littérature académique sur l'interopérabilité et l'orchestration des agents fondés sur les grands modèles de langue en entreprise, arrêtée au 15 août 2026. Elle prend pour corpus 192 pièces, dont 189 déposées sur arXiv, chacune ouverte sur sa notice et confrontée aux métadonnées canoniques du dépôt.

  Le premier résultat tient à la forme du corpus retenu, non à son contenu. **Douze pièces sur 189 — 6 % — portent une attestation de publication dans leur notice.** Trente-deux autres annoncent une acceptation dans le seul champ de commentaire libre, que personne ne vérifie. **Les 145 restantes, soit 77 % de ce corpus arXiv, ne présentent aucun signe de revue par les pairs à leur notice.** La proportion mesure un dépôt de prépublications lu au seul critère de la notice ; elle ne s'étend pas au champ, et une passe de contrôle sur les bases de littérature arbitrée en borne l'écart dans les deux sens. Soixante-trois pour cent du corpus a été déposé en 2026 et plus de la moitié n'a jamais été révisée. *Un corpus dont les trois quarts ne déclarent aucun comité ne peut pas fonder à lui seul une décision d'architecture au même titre qu'une littérature établie, et cette revue le déclare avant d'en rapporter le contenu.*

  Dix fronts sont examinés — protocoles, sécurité, identité et délégation, systèmes multi-agents, évaluation, couche transactionnelle, processus d'affaires, gouvernance, Web agentique, chorégraphie et essaim. Pour chacun, la revue distingue ce que la littérature établit, où elle se contredit réellement, et ce qu'elle ne traite pas. Quatre désaccords méritent d'être nommés : la validité même des instruments qui mesurent le risque protocolaire, l'utilité du multi-agent comparé à l'agent unique, le choix entre suspendre l'effet jusqu'à confirmation ou l'émettre et organiser sa révision, et la place de la vérification dans un collectif sans chef d'orchestre.

  La revue confronte enfin trois énoncés de la veille technologique du même auteur à ce que la littérature en dit. Deux en ressortent modifiés : le déficit de délégation au-delà de deux sauts est un déficit d'adoption et non d'invention, et la dissymétrie entre agents et formalismes de processus est industrielle, non scientifique. Le troisième — l'absence de vocabulaire de trace décrivant une chaîne de mandat — est confirmé par une seconde voie, plus sévère que la première.
header-includes: |
  ```{=typst}
  // ═══════════════════════════════════════════════════════════════════════
  //  RÉGLAGE COMMUN — traité, veille technologique, revue de littérature.
  //  Ce bloc est IDENTIQUE dans les trois en-têtes, au rang des titres près
  //  et aux deux règles propres au traité qui closent le sien — chacune dit
  //  pourquoi. Les trois documents doivent se lire comme un seul ouvrage, et
  //  toute reprise se fait sur les trois.
  //
  //  Géométrie, posée dans le YAML ci-dessus et rappelée ici parce qu'elle
  //  commande tout le reste :
  //    corps de texte    378 pt (5,25 po) — 612 moins deux marges de 117 pt,
  //                      soit 75 à 79 signes par ligne à 11 pt.
  //    interligne        14,3 pt — 0,95 × 0,65 em de blanc sur 11 pt de
  //                      corps, soit 1,30 fois le corps.
  //    hauteur composée  648 pt (9 po), 45 lignes.
  //    Le bloc composé fait donc 378 × 648 pt : mêmes proportions, à 1 % près,
  //    que l'article de référence (343 × 581 pt), qui compose 85 signes par
  //    ligne sur un interligne de 1,20 là où celui-ci en compose 77 sur 1,30.
  //
  //  ⚠ `fontsize` VAUT 10 pt ET LE CORPS VAUT 11 pt. Ce n'est pas une
  //  contradiction : le gabarit compose le bloc de titre et le résumé AVANT
  //  d'entrer dans le document, donc à `fontsize`, et `include-before` remet
  //  le corps à 11 pt dès la première ligne du texte. Le résumé se compose
  //  ainsi un corps sous le texte, comme l'usage le veut — et surtout il
  //  tient sur sa page : le gabarit pose le bloc de titre en FLOTTANT NON
  //  SÉCABLE, et un résumé qui déborde est rogné sans que Pandoc ni Typst ne
  //  le signalent. `4 - Veille/Python/check-resume.py` est la porte qui le
  //  mesure, et elle est la seule.
  //
  //  ⚠ L'APPAREIL GARDE LA MESURE D'UN POUCE. Les dix-neuf figures du traité
  //  sont gravées à 468 unités (figures/dessine.py, W = 468) et son
  //  pseudocode aligne des lignes de 86 signes, soit 466 pt à 9 pt : l'un et
  //  l'autre débordent d'un corps de 378 pt. `pad(x: -45pt)` rend aux
  //  figures, aux tableaux et aux blocs de code les 468 pt (6,5 po) auxquels
  //  ils ont été composés, centrés sur le corps, et laisse un pouce franc de
  //  chaque côté. Retirer ce débord SANS régénérer les figures à la largeur
  //  du corps les met à l'échelle de celui-ci et fait tomber leurs textes de
  //  8,5 pt à 6,9 pt — la panne est silencieuse, elle ne se voit qu'au rendu.

  // ── Folio : centré en pied, jamais sur la page de titre.
  #set page(footer: context {
    let n = counter(page).get().first()
    if n > 1 { align(center)[#text(size: 10pt)[#n]] }
  })

  // ── Paragraphes : alinéa, pas de blanc intercalaire. Typst n'indente pas
  //    le premier paragraphe d'un bloc ni celui qui suit un titre : c'est
  //    exactement la convention d'un `article`, ne pas passer `all: true`.
  #set par(spacing: 0.6em, first-line-indent: 1.5em)

  // ── Emphase : le gras dénote un TERME, pas une proposition. ⚠ SEUL POSTE
  //    OÙ LE GABARIT CORRIGE LA SOURCE, et il ne lui retire rien : le texte
  //    reste entier, seule la graisse tombe.
  //    Relevé sur les rendus du 15 août, même réglage pour les trois :
  //    1,9 % des signes du traité composés en gras, 10,7 % de la veille,
  //    10,5 % de la revue — et jusqu’à 33,9 % sur une page. À ces densités le
  //    gras ne signale plus, il tache : deux lecteurs indépendants, en
  //    comparaison à l’aveugle, ont décrit la même page en « plaques noires
  //    réparties au hasard de la colonne », lue de tache en tache au lieu
  //    d’être parcourue — le traité, à 0,5 % dans son texte courant, a gagné
  //    le même tour sans qu’aucun lecteur ne mentionne sa graisse.
  //    Le critère est la LARGEUR, parce que c’est elle que l’œil voit — un
  //    compte de mots ne distingue pas un terme d’une incise. En deçà de
  //    14 em (154 pt à 11 pt, deux cinquièmes de la mesure, ≈ 29 signes), le
  //    gras est un repère ponctuel et se conserve ; au-delà il fait plaque et
  //    se rend au romain. Mesuré en gras à 11 pt : « Le moteur comme
  //    client. » 138 pt et « Ce que la revue renvoie. » 135 pt passent — les
  //    titres courants d’entrée de paragraphe tiennent, et ce sont eux qui
  //    donnent le rythme de la page ; « prépublication non révisée par les
  //    pairs » 219 pt, « Un socle achevé, à une révision près. » 204 pt et
  //    toute ouverture de section de deux lignes et demie tombent. L’échantillon
  //    ne montre rien entre 138 et 169 pt : le seuil est posé dans ce creux.
  //    ⚠ EN EM, PAS EN POINTS : le seuil vaut 126 pt dans les tableaux, qui
  //    composent à 9 pt, soit le même nombre de signes qu’à 11 pt.
  //    ⚠ `measure` mesure le corps HORS du gras qui l’enveloppe, donc à 3 %
  //    près en dessous de sa largeur composée. C’est un seuil, pas une cote.
  //    ⚠ Précédent maison : `2 - Compendium/build/accentuation.lua` tranche la
  //    même chose au filtre Pandoc, au compte de mots. La règle vit ici et non
  //    dans un filtre parce que les trois chaînes d’appel de Pandoc ne portent
  //    pas de `--lua-filter` et ne doivent pas en porter.
  #show strong: it => context {
    if measure(it.body).width < 14em.to-absolute() { it }
    else { text(weight: "regular", it.body) }
  }

  // ── Titres : c'est le blanc AU-DESSUS qui fait la hiérarchie, pas le corps.
  #show heading: set text(hyphenate: false)
  #show heading: set par(justify: false, first-line-indent: 0pt)
  #show heading: set block(sticky: true)

  // ── Appareil : tableaux, blocs de code et légendes à 9 pt, légendes ferrées
  //    à gauche et collées à ce qu'elles légendent.
  #show figure.where(kind: table): set text(size: 9pt)
  #show raw.where(block: true): set text(size: 9pt)
  #show figure.caption: set text(size: 9pt)
  #show figure.caption: set par(justify: false, first-line-indent: 0pt)
  #show figure.caption: set block(sticky: true)
  //    ⚠ La légende revient sur la MESURE DU TEXTE. Le débord de 45 pt vaut
  //    pour ce qui est gravé large — figures, tableaux, pseudocode —, pas pour
  //    la phrase qui les nomme : un lecteur l'a vue « ferrée sur le tableau et
  //    non sur le texte », et elle l'était, son fer tombant 45 pt à gauche de
  //    la colonne. `pad(x: 45pt)` annule ici, pour la seule légende, le
  //    `pad(x: -45pt)` posé plus bas sur la figure entière : elle se compose
  //    donc sur 378 pt, au fer du texte courant, sous un appareil qui garde
  //    ses 468 pt. ⚠ Le compte est exact quand la figure OCCUPE ses 468 pt,
  //    c'est-à-dire toujours sauf pour un tableau que Pandoc laisse en
  //    colonnes automatiques : celui-là se rétrécit à son contenu, Typst le
  //    centre, et sa légende suit le bloc rétréci — 1 légende sur 54, décalée
  //    de 11,4 pt, mesurée sur la légende des sigles de la veille. ⚠ NE PAS
  //    écrire ici « tableau » suivi d'un nombre : `check-revue.py` lit tout le
  //    fichier, en-tête compris, et prend le mot pour un renvoi hors plage.
  #show figure.caption: set align(left)
  #show figure.caption: it => pad(x: 45pt, it)

  // ── Tableaux : en drapeau, ferrés en haut. ⚠ La justification dans une
  //    colonne de seize signes ouvre des lézardes et force la césure à chaque
  //    ligne : c'est ce qui rendait la page 12 de la veille illisible. Le
  //    centrage vertical, lui, faisait flotter chaque cellule au milieu de la
  //    rangée, sans ligne de base commune d'une colonne à l'autre.
  #set table(inset: (x: 5pt, y: 4pt))
  #show table.cell: set par(justify: false, first-line-indent: 0pt, leading: 0.5em)
  //    ⚠ Le FER HORIZONTAL, lui, échappe à cette règle : l'argument `align:`
  //    que Pandoc pose sur chaque tableau l'emporte, et un `left` écrit ici
  //    serait sans effet. Il n'est pour autant PAS TOUJOURS CELUI QUE LA
  //    SOURCE DÉCLARE, contrairement à ce que ce commentaire a dit jusqu'au
  //    16 août 2026 — relevé sur le typst intermédiaire des trois : les 24
  //    tableaux de la veille déclarent le leur colonne par colonne (11 ferrés
  //    à gauche, 13 centrés) et l'obtiennent ; les 22 du traité et les 8 de la
  //    revue ne déclarent rien, Pandoc y pose `auto`, et `auto` hérite du
  //    `align(center)` dont Pandoc enveloppe tout tableau. Ces trente-là sont
  //    donc centrés par défaut d'appel et non par choix, cellules de trois
  //    lignes comprises. Les reprendre au fer à gauche tient en un mot ici
  //    (`top + left`), mais fait refluer trente tableaux et deux paginations :
  //    c'est un arbitrage ouvert, pas un résidu de tour, et il se tranche sur
  //    les sources, où le fer se déclare.
  #show table.cell: set align(top)

  // ── Blocs : figures, tableaux, code et listes respirent, et se scindent.
  #show figure: set block(breakable: true, above: 1.4em, below: 1.4em)
  #show raw.where(block: true): set block(above: 1.4em, below: 1.4em)
  #show enum: set block(above: 1.0em, below: 1.0em)
  #show list: set block(above: 1.0em, below: 1.0em)
  #set image(width: 100%)

  // ── Débord de l'appareil — cf. l'avertissement en tête de bloc.
  #show figure: it => pad(x: -45pt, it)
  #show raw.where(block: true): it => pad(x: -45pt, it)

  // ── Bibliographies : le bloc `::: {#refs}` que Pandoc pose autour de la liste
  //    de notices. ⚠ C'EST LE SEUL ENDROIT OÙ UNE RÈGLE SUR `enum` PUISSE ÊTRE
  //    COMMUNE AUX TROIS : hors de lui, la veille porte 44 items de liste
  //    numérotée dans son corps, qu'une règle générale atteindrait du même
  //    geste. Le traité a reçu le `:::` le 16 août 2026 — sa liste de
  //    références était nue, elle sort désormais du même mécanisme que les
  //    deux autres, sans qu'une notice ni une référence bouge.
  //    Deux défauts mesurés sur les rendus du 15 août, tous deux propres aux
  //    bibliographies, et un lecteur en aveugle les a nommés ensemble : « une
  //    nappe continue », « une seule colonne grise » où rien ne marque le début
  //    d'une notice sauf le chiffre, et des trous verticaux dans les lignes.
  //
  //    ① LES NOTICES SE TOUCHAIENT. `par.spacing` vaut 0,6 em, soit 6,6 pt ;
  //      l'interligne vaut 0,95 × 0,65 em, soit 6,79 pt. Le blanc entre deux
  //      notices était donc PLUS PETIT que celui entre deux lignes d'une même
  //      notice — mesuré page 98 de la veille : 14,11 pt de ligne de base à
  //      ligne de base d'une notice à la suivante, contre 14,31 pt à
  //      l'intérieur d'une notice. Treize notices y tenaient 46 lignes sans un
  //      blanc. 1,15 em (12,65 pt) porte ce blanc à 1,9 fois l'interligne.
  //      Le renfoncement pendant, lui, ne bouge pas : Typst ferre déjà les
  //      numéros à droite d'une colonne commune de 25 pt (2,3 em) — ce qui lui
  //      manquait pour se voir était le blanc au-dessus, pas de la largeur.
  //
  //    ② LES NOTICES SE FERRENT EN DRAPEAU, comme les tableaux et pour la même
  //      raison. ⚠ CE N'EST PAS LA JUSTIFICATION DU CORPS QUI EST EN CAUSE, et
  //      elle n'est pas touchée : c'est la rencontre de la justification et
  //      d'une URL. Le lecteur a mis les trous sur le compte d'« URL
  //      insécables » ; c'est FAUX, et la mesure le dit — Typst coupe déjà aux
  //      barres obliques, et une règle qui en ouvrait d'autres explicitement
  //      (`h(0pt)` après chaque barre) rendait le MÊME PDF, aux mêmes coupures,
  //      sur les 1 637 lignes de la bibliographie de la veille. Le vrai
  //      mécanisme est ailleurs : une ligne dont l'essentiel est une URL ne
  //      porte qu'un ou deux blancs, la justification y verse tout son mou, et
  //      la coupure optimisée de Typst en reporte une part sur les lignes
  //      VOISINES pour égaliser — d'où des trous à trois lignes de l'URL qui
  //      les cause. Mesuré sur la bibliographie de la veille, blanc naturel de
  //      3,06 pt : justifiée, 51,6 % des lignes passent 1,5 fois ce blanc,
  //      3,4 % le passent trois fois, la pire ligne l'ouvre à 19,2 pt, six
  //      fois sa valeur. `linebreaks: "simple"` aggrave (64,3 % à 1,5 fois) :
  //      il concentre le mou au lieu de l'étaler, il ne le supprime pas. En
  //      drapeau il n'y a plus de mou du tout, et le bord droit d'une notice
  //      reste peu dentelé parce que les lignes sont naturellement pleines.
  //      C'est la règle déjà écrite plus haut pour les tableaux, appliquée où
  //      elle vaut aussi. ⚠ LE CORPS DES TROIS DOCUMENTS RESTE JUSTIFIÉ.
  #show <refs>: it => {
    set enum(spacing: 1.15em)
    set par(justify: false)
    it
  }

  // ── Table des matières : sa propre page, à 9 pt — le corps de l'appareil.
  //    ⚠ SECOND POSTE OÙ LE BLOC DIFFÈRE D'UN DOCUMENT À L'AUTRE, avec le rang
  //    des titres qui le suit. Le bloc commun n'y pose PLUS le saut de page qui
  //    ferme la table : les mots-clés, premier paragraphe du corps, montent à sa
  //    suite. La raison est une mesure et non un goût — la table de la revue
  //    s'arrête à y = 208,6 pt sur sa dernière page, soit 36 lignes libres pour
  //    les 8 que font ses mots-clés, et le saut leur donnait une page entière
  //    où ils tenaient seuls sur un huitième de la hauteur composée.
  //    ⚠ NE PAS REPORTER TEL QUEL SUR LA VEILLE NI SUR LE TRAITÉ. La table de
  //    la veille s'arrête à y = 677 pt, trois lignes libres, et ses mots-clés
  //    en font quinze : sans le saut ils se couperaient en deux pages. Un
  //    document dont la table remplit sa dernière page garde le saut ; celui
  //    dont elle s'arrête haut ramène ses mots-clés dessous. La règle ne peut
  //    pas trancher pour les deux, et c'est pourquoi elle ne tranche plus ici.
  //    Le saut qui ouvre la première section, lui, reste écrit dans la source
  //    des trois — il n'a jamais dépendu de cette règle.
  #show outline: set text(size: 9pt)
  #show outline: it => [#pagebreak(weak: true) #it #v(1.4em)]

  // ── Bloc de titre : titre, description du livrable, auteur, résumé.
  //    ⚠ LE GABARIT PANDOC EST REPRIS ICI, PAS COMPLÉTÉ. C'est le seul poste
  //    du bloc commun qui redéfinisse une fonction du gabarit, et il le fait
  //    faute d'autre voie : aucune règle `show` n'atteint un bloc de titre que
  //    le gabarit compose en dur, et le YAML n'en règle ni les graisses ni les
  //    blancs. Deux défauts mesurés sur les rendus du 15 août, les mêmes aux
  //    trois documents, et qui se répondent :
  //    ① L'AUTEUR COLLE AU TITRE — 2,4 pt sous le sous-titre de la revue,
  //      1,9 pt sous la seconde ligne du titre de la veille, soit rien. Le
  //      `par(spacing: 0.6em)` posé plus haut vaut aussi pour l'écart entre le
  //      bloc de titre et la grille des auteurs, que le gabarit laissait au
  //      défaut de Typst : la règle qui resserre les paragraphes du corps
  //      resserrait du même geste ce qui sépare l'ouvrage de qui le signe.
  //    ② DEUX LIGNES VIDES TOMBENT SOUS L'AUTEUR. Le gabarit compose
  //      `nom \ affiliation \ courriel`, et un auteur donné en simple chaîne
  //      — c'est le cas des trois — n'a ni l'une ni l'autre : 35,9 pt de blanc
  //      entre l'auteur et le résumé de la revue, 35,9 pt à la veille.
  //    Le blanc était donc tout entier du mauvais côté, quinze fois plus bas
  //    que haut, et le bloc se lisait comme un titre suivi d'un orphelin. Il
  //    va maintenant CROISSANT — 6,1 pt sous le titre, 9,9 pt sous le
  //    sous-titre, 21,9 pt sous l'auteur —, chaque rang séparé du suivant par
  //    un peu plus de blanc que du précédent.
  //    Le wrapper appelle le gabarit SANS TITRE : privé de titre il ne compose
  //    ni titre, ni sous-titre, ni auteur, ni date, ni résumé, et garde tout le
  //    reste — réglage de page, langue, numérotation, métadonnées d'auteur. Les
  //    cinq sont posés ici, dans le même flottant, à la même géométrie.
  //    ⚠ LE FLOTTANT NE SE SCINDE PAS : un résumé trop long n'est pas reporté,
  //    il est rogné, et ni Pandoc ni Typst ne sortent autre chose que 0.
  //    `Python/check-resume.py` reste la seule porte qui le mesure.
  //    ⚠ `set document` DOIT ÊTRE POSÉ DANS LE CONTENU, pas avant l'appel : le
  //    gabarit pose le sien après, et un titre écrit trop tôt est écrasé par le
  //    `title: none` qu'on lui passe — le PDF sortait alors sans titre.
  //    ⚠ LE SOUS-TITRE PASSE DU GRAS 12,5 pt AU ROMAIN 12 pt. Il nomme le
  //    livrable — « veille technologique en entreprise », « revue de la
  //    littérature académique » —, il ne prolonge pas le titre : deux graisses
  //    identiques à deux points et demi d'écart ne font pas deux rangs, elles
  //    font un titre de deux lignes. Le titre garde ses 15 pt gras.
  #let conf-pandoc = conf
  #let conf(title: none, subtitle: none, authors: (), date: none,
            abstract: none, abstract-title: none, ..reste, doc) = {
    conf-pandoc(..reste, authors: authors, {
      set document(title: if title != none { content-to-string(title) })
      place(top, float: true, scope: "parent", clearance: 4mm,
            block(below: 1em, width: 100%)[
        #align(center)[
          #block(below: 1.05em)[
            #text(size: 15pt, weight: "bold", hyphenate: false)[#title]
          ]
          #if subtitle != none {
            block(below: 1.35em)[
              #text(size: 12pt, weight: "regular", hyphenate: false)[#subtitle]
            ]
          }
          #if authors != none and authors != () {
            block(below: 0pt)[#authors.map(a => a.name).join(h(1.5em))]
          }
          #if date != none {
            block(above: 0.45em, below: 0pt)[#date]
          }
        ]
        #if abstract != none {
          block(inset: (x: 2em), above: 2.5em)[
            #text(weight: "semibold")[#abstract-title] #h(1em) #abstract
          ]
        }
      ])
      doc
    })
  }

  // ── Rang typographique des titres. ⚠ SECOND POSTE OÙ LE BLOC DIFFÈRE D'UN
  //    DOCUMENT À L'AUTRE — l'autre est le saut de page qui fermait la table
  //    des matières —, et il n'a pas le choix : la veille et la revue
  //    ouvrent leurs chapitres en `#` (niveau 1), le traité les siens en `##`
  //    (niveau 2). C'est le RANG qui doit se composer pareil, pas le niveau ;
  //    les trois échelles ci-dessous sont donc la même, décalée.
  //    ⚠ EN POINTS, PAS EN EM : Typst a déjà mis le titre à l'échelle de son
  //    niveau quand cette règle s'applique, et un « 1.30em » s'y multiplie au
  //    lieu de s'y substituer — le rang 1 sortait à 20 pt au lieu de 14.
  #show heading.where(level: 1): set text(size: 14pt)
  #show heading.where(level: 1): set block(above: 1.7em, below: 0.6em)
  #show heading.where(level: 2): set text(size: 12.5pt)
  #show heading.where(level: 2): set block(above: 1.6em, below: 0.55em)
  #show heading.where(level: 3): set text(size: 11pt)
  #show heading.where(level: 3): set block(above: 1.5em, below: 0.5em)
  ```
include-before: |
  ```{=typst}
  // ⚠ LE CORPS DU DOCUMENT COMPOSE À 11 pt. `fontsize: 10pt` dans le YAML ne
  // vaut que pour le bloc de titre et le résumé, que le gabarit compose avant
  // d'entrer ici. Voir l'avertissement en tête de `header-includes`.
  #set text(size: 11pt)
  ```
---

**Mots-clés —** revue de littérature ; interopérabilité des agents ; IA agentique ; Model Context Protocol ; Agent2Agent ; systèmes multi-agents ; chorégraphie agentique ; essaim multiagents ; coordination décentralisée ; identité non humaine ; chaîne de délégation ; révocation ; sécurité des agents ; injection d'invite indirecte ; bancs d'essai d'agents ; observabilité agentique ; provenance ; paiements agentiques ; collusion algorithmique ; gestion des processus d'affaires ; exécution durable ; conformité ; responsabilité ; Web agentique ; régime de preuve ; prépublication.

```{=typst}
#pagebreak(weak: true)
```

# Introduction

L'interopérabilité des agents fondés sur les grands modèles de langue est passée, en moins de trois ans, du statut de curiosité de laboratoire à celui de question d'architecture d'entreprise. Des protocoles de composition ont été publiés, des registres montés, des mécanismes de paiement et de délégation proposés, des textes réglementaires adoptés qui s'appliquent à ces systèmes sans les nommer. La production académique a suivi le même rythme. C'est précisément ce rythme qui pose problème : une littérature qui double de volume en douze mois n'a pas eu le temps d'être filtrée par les procédures qui, ailleurs, séparent le résultat de la revendication.

## Question de revue

Cette revue pose une question en deux parties : **que la littérature académique établit-elle réellement sur l'interopérabilité et l'orchestration agentiques en entreprise, et à quel régime de preuve ?** La seconde partie commande la première. Un énoncé de la forme « tel protocole présente telle vulnérabilité dans tel pourcentage des serveurs observés » n'a pas la même portée selon qu'il provient d'une mesure sur un parc réel, d'une simulation, ou d'un raisonnement sur la spécification ; et il n'a pas la même autorité selon qu'un comité de lecture l'a examiné ou que son auteur l'a déposé la semaine dernière.

Trois termes sont pris au sens suivant. L'*interopérabilité* désigne la capacité de composer des agents, des outils et des services hétérogènes sous un vocabulaire commun, qu'il s'agisse d'accès aux outils, de communication entre agents ou de découverte. L'*orchestration* désigne la conduite d'un travail à plusieurs étapes, avec ses garanties d'exécution, sa trace et sa reprise sur défaillance. La restriction *en entreprise* écarte les travaux qui n'envisagent que l'agent isolé ou le banc d'essai jouet, et retient ceux qui portent sur des systèmes soumis à une contrainte d'exploitation, d'audit ou de droit.

## Rapport à la veille technologique

Cette revue prolonge une veille technologique du même auteur, qui dresse l'état du champ sur sources primaires : spécifications, dépôts de code, communiqués de fondations, textes réglementaires. L'auto-citation est déclarée ici et signalée à chaque renvoi. Les deux exercices ne répondent pas à la même question et ne se valident pas l'un l'autre.

La veille dit ce que le monde déployé fait ; la présente revue dit ce que la littérature sait, et l'intérêt tient à ce qu'elles ne coïncident pas. La veille observe des protocoles adoptés à grande échelle sans démonstration de sécurité publiée ; la littérature, elle, mesure des vulnérabilités sur des parcs que personne n'a mandat de corriger. La veille constate des couches comblées hors de la couche commune ; la littérature les traite parfois abondamment, parfois pas du tout. Trois de ses énoncés sont mis à l'épreuve en fin de revue.

# Méthode

## Constitution du corpus

Le corpus compte 192 entrées et a trois origines. La première est le socle hérité de la veille : ses 50 pièces académiques **[1-50]**, reprises telles quelles puis re-vérifiées pièce à pièce contre leur notice courante, plusieurs ayant été révisées depuis leur lecture initiale. La deuxième est une passe de recherche neuve conduite sur dix fronts thématiques : protocoles **[51-63]**, sécurité **[64-74]**, identité et délégation **[75-87]**, systèmes multi-agents **[88-101]**, évaluation et observabilité **[102-113]**, couche transactionnelle **[114-125]**, processus d'affaires **[126-137]**, gouvernance **[138-148]**, Web agentique et horizon **[149-158]**, chorégraphie et essaim **[159-173]**. Trois pièces à DOI **[174-176]** complètent l'ensemble : textes normatifs et littérature d'ingénierie antérieure au dépôt, sans laquelle le front transactionnel n'aurait pas de point d'appui. La troisième origine est la reprise du 15 août elle-même : **seize pièces déposées entre le 9 et le 13 août 2026 [177-192]**, retenues au même critère que la passe neuve et rattachées chacune au front où sa mesure porte.

Les trois origines ne portent pas le même régime de citation, et le contrôle de publication de cette revue l'exige : **chacune des 142 entrées hors socle — les 123 de la passe neuve, les seize de la reprise du 15 août et les trois à DOI — est discutée nommément** dans le corps, tandis que le socle hérité est repris en bloc — **vingt-trois de ses cinquante pièces y sont engagées une à une, vingt-sept ne le sont pas** et ne valent ici que comme arrière-plan. *Une plage citée en prose couvre une référence sans la discuter ; le distinguer est ce qui empêche une bibliographie de grossir sans que le texte y gagne.*

Le découpage en dix fronts n'est pas une taxinomie du champ mais un plan de couverture : il sépare ce que la veille avait identifié comme des couches distinctes de la pile. Un même travail peut relever de deux fronts ; il est alors rattaché à celui où sa mesure porte, et non à celui que son titre annonce.

La passe neuve a été conduite par des agents indépendants, à consigne de source primaire exclusive : aucun ne pouvait retenir une pièce sur la foi d'un résumé secondaire, chacun devait ouvrir la notice de chaque pièce et en rapporter les métadonnées. Le critère de rétention est la conséquence : les pièces les plus conséquentes de chaque front, la conséquence se jugeant à la mesure produite et non à la citation reçue. Sur un corpus dont 119 pièces sur 189 ont été déposées en 2026, le compte de citations ne mesure rien d'autre que l'antériorité de dépôt.

## Régime de vérification

Toutes les notices arXiv ont été reprises à l'API d'exportation du dépôt le 9 août 2026, puis reprises une seconde fois, intégralement, le 15 août 2026 : **189 notices demandées, 189 obtenues, aucune retirée ni devenue introuvable** — les 173 du premier relevé et les seize entrées depuis, interrogées le même jour à la même interface. Chaque reprise donne, pour chacune des pièces : titre exact, auteurs, version courante, date de dépôt initial, date de dernière révision, champ `journal_ref`, champ DOI et champ `comment`. La première a corrigé plusieurs statuts que les agents avaient rapportés comme « à comité de lecture » sur la seule foi du champ de commentaire — correction qui a motivé la section suivante et, plus largement, la construction de toute la revue. La seconde n'a trouvé, sur les 173 pièces du premier relevé, que deux notices révisées dans l'intervalle : [113], passée en v2 le 13 août, et [146], passée en v2 le 10 août ; l'une et l'autre sont instruites plus bas.

La règle appliquée est stricte : seule une attestation portée à la notice elle-même — champ `journal_ref` ou champ DOI — vaut publication établie. ⚠ *Le premier relevé de cette revue ne retenait que le premier des deux champs et comptait sept pièces là où il y en a douze ; l'écart a été trouvé en confrontant les notices aux entrées, et il est rapporté ici plutôt que corrigé en silence.* Une acceptation annoncée ailleurs est enregistrée comme telle, comme déclaration de l'auteur, et comptée séparément. Ce second partage a été refait notice par notice le 15 août, sur la règle suivante : une acceptation ou une présentation annoncée compte, une soumission annoncée ne compte pas — [163], dont le commentaire porte « submitted to OOPSLA 2026 », reste donc hors du compte, et un dépôt d'archive ouverte sans arbitrage aussi, tel le Zenodo de [86].

## Ce que cette revue ne peut pas établir

Ni protocole enregistré au sens PRISMA, ni double codage, ni recherche multi-bases : un seul jugement décide de chaque rétention, et l'interrogation porte sur arXiv complété de trois références à DOI. Surtout, il n'y a **aucune réplication** : aucune expérience n'a été refaite, aucun banc réexécuté, et la revue rapporte ce que les pièces revendiquent en distinguant ce qui est mesuré de ce qui est avancé. **Les décomptes qui suivent sont donc un recensement du corpus retenu, non une estimation du champ.**

# Physionomie du corpus

## Ce que la forme du corpus dit avant son contenu

Avant tout énoncé de contenu, la forme du corpus le qualifie. Sur les 189 pièces déposées sur arXiv, **douze** portent une attestation de publication dans leur notice — les mêmes douze qu'au relevé du 9 août : sept au champ `journal_ref` — [15], [37], [38], [46], [59], [136], [143] — et cinq au seul champ DOI — [4], [44], [142], [144], [158] ; l'annexe donne pour chacune sa publication et son apport. Trente-deux pièces annoncent une acceptation ou une présentation dans le seul champ de commentaire libre. Les 145 restantes ne présentent aucun signe de revue par les pairs à leur notice — part de ce corpus arXiv relevée au seul critère de la notice, non estimation du champ, et les limites en mesurent l'écart.

Ces trente-deux ne sont pas les vingt-huit du 9 août, et l'écart tient à quatre entrées. Trois viennent du partage refait sur les 173 notices du premier relevé. [113] a gagné son annonce de lieu en révisant sa notice le 13 août : sa v1 ne portait aucun commentaire, sa v2 déclare qu'une version condensée paraît dans les actes d'un sommet. [137] et [145] portent au 15 août l'annonce d'une présentation en atelier et un nom de conférence, dans la forme exacte de pièces qui étaient comptées ; le premier relevé les rangeait en prépublication. *Depuis quand ces deux commentaires sont-ils là, on ne peut pas le dire : une édition de métadonnées seule ne change ni la version ni la date de révision, et arXiv ne publie aucun historique de ces champs. Ce qui est établi, c'est qu'ils y sont aujourd'hui et qu'ils n'étaient pas comptés.* La quatrième entrée est une arrivante : des seize pièces versées le 15 août, [183] est la seule à annoncer un lieu — une acceptation en atelier au seul champ de commentaire —, et aucune des seize ne porte d'attestation en notice.

Trois régimes de preuve se distinguent donc, et la distinction n'est pas formelle : le champ de commentaire est rempli par l'auteur et n'est vérifié par personne. La plupart de ces trente-deux annonces sont vraisemblablement exactes ; l'objection ne porte pas sur leur véracité individuelle mais sur la nature de la garantie — un contrôle que nul n'exerce ne devient pas un contrôle parce que les déclarants sont honnêtes.

: Régimes de preuve des 189 pièces déposées sur arXiv, d'après les notices reprises à l'API du dépôt le 15 août 2026. Les parts portent sur ce corpus et sur ce que la notice déclare, non sur le champ.

| Régime | Pièces | Part |
|---|---|---|
| Publication attestée en notice (`journal_ref` ou DOI) | 12 | 6 % |
| Acceptation auto-déclarée (champ de commentaire) | 32 | 17 % |
| Aucun signe de revue par les pairs | 145 | 77 % |
| Total | 189 | 100 % |

L'âge du corpus va dans le même sens. Le dépôt initial se répartit ainsi : 2023, cinq pièces ; 2024, treize ; 2025, cinquante-deux ; 2026, cent dix-neuf — soit 63 % des pièces déposées sur arXiv, dans les huit premiers mois de 2026. La révision suit : 136 pièces sur 189, soit 72 %, ont été révisées pour la dernière fois en 2026, dont vingt-huit en juin, vingt et une en juillet et vingt-deux dans les quinze premiers jours d'août. Quant à la stabilité des textes, 103 pièces en sont encore à leur version initiale, 52 à la deuxième, 24 à la troisième et 10 au-delà : plus de la moitié du corpus — 103 sur 189, soit 54 % — n'a jamais été révisée.

*Deux de ces chiffres sont en partie fabriqués par l'instrument, et il faut le dire avant d'en tirer quoi que ce soit.* Les vingt-deux révisions d'août comptent les seize pièces que la reprise vient d'ajouter, retenues précisément parce qu'elles étaient neuves : on n'y lira donc pas une accélération du champ. Et la part des textes jamais révisés monte de deux points et demi depuis le 9 août pour la même raison — quinze des seize arrivantes sont en v1. La reprise rajeunit le corpus qu'elle mesure.

Vingt-huit révisions en juin sur un corpus de 189 pièces : 15 % des textes ont bougé en un mois. Une pièce lue en avril et citée en août peut avoir changé de résultat, de jeu de données ou de conclusion entre-temps ; c'est ce qui a imposé la re-vérification du socle. Le risque n'est pas théorique et la reprise du 15 août en donne le cas : **[146] a doublé de volume le 10 août — 21 pages en v1, 44 en v2 — et a réétiqueté ses propres démonstrations**, requalifiant en illustrations synthétiques calibrées ce que sa v1 donnait pour des instanciations calculables ; le front de la gouvernance en instruit le détail. *La pièce n'a pas corrigé un résultat ; elle a rendu explicite le régime de preuve que ce résultat avait déjà, et c'est une semaine après son dépôt, sans qu'aucun avis parte vers qui la citait.* L'autre révision, [113], laisse son résumé inchangé mot pour mot et ne déplace que son régime de publication déclaré — de prépublication sans signe de revue à acceptation autodéclarée. Le corpus est ici gelé au 15 août 2026, et chaque énoncé rapporté vaut pour la version courante à cette date.

Le constat commande la lecture de tout ce qui suit : 77 % des énoncés retenus ici ne déclarent aucun comité à leur notice, 63 % ont été déposés en 2026, plus de la moitié n'a jamais été révisée. **Le chiffre est celui du corpus, pris sur le dépôt où va le travail non arbitré ; le lire comme une part du champ serait circulaire, et le tenir pour un compte exact de l'arbitrage subi serait faux dans l'autre sens** — la passe de contrôle rapportée aux limites trouve de la littérature arbitrée hors arXiv sur quatre fronts, et des pièces de ce corpus publiées sans que leur notice le dise. Cela n'interdit pas de s'y appuyer, mais interdit de les traiter comme un acquis, et impose de rapporter chaque résultat avec le régime qui le porte.

## Répartition par front et par régime de preuve

: Répartition des 192 entrées par front, avec la plage de références de la passe neuve et, à sa suite, les pièces versées à la reprise du 15 août.

| Front | Références | Pièces |
|---|---|---|
| Socle hérité de la veille | [1-50] | 50 |
| Protocoles | [51-63], [177], [183] | 15 |
| Sécurité | [64-74], [178], [184], [185] | 14 |
| Identité et délégation | [75-87], [179], [186] | 15 |
| Systèmes multi-agents | [88-101], [187] | 15 |
| Évaluation et observabilité | [102-113], [181], [182], [188], [189], [190] | 17 |
| Couche transactionnelle | [114-125] | 12 |
| Processus d'affaires | [126-137] | 12 |
| Gouvernance | [138-148], [191], [192] | 13 |
| Web agentique et horizon | [149-158] | 10 |
| Chorégraphie et essaim | [159-173], [180] | 16 |
| Pièces à DOI | [174-176] | 3 |

Les dix fronts neufs comptent 139 pièces, de dix à dix-sept chacun. Cet équilibre est un artefact de méthode : le critère de rétention est comparatif à l'intérieur de chaque front, non proportionnel au volume produit. Le tableau mesure l'attention de cette revue, pas l'activité de la littérature. Les seize entrées du 15 août sont numérotées à la suite plutôt qu'insérées dans les plages, mais rattachées chacune au front où sa mesure est discutée : les tenir en fin de colonne garde visible ce qu'une semaine de dépôts a suffi à ajouter, et où elle n'a rien ajouté — cinq pièces à l'évaluation, aucune à la couche transactionnelle, aux processus d'affaires ni au Web agentique.

Le régime de preuve, lui, ne se distribue pas uniformément. Six des douze publications attestées appartiennent au socle hérité — [4], [15], [37], [38], [44] et [46], dont deux antérieures à 2025 — et les six autres se répartissent entre protocoles [59], processus d'affaires [136], gouvernance [142], [143], [144] et horizon [158] : quatre fronts neufs sur dix. L'attestation en notice se produit là où des communautés établies existent depuis longtemps : gestion des processus d'affaires, systèmes d'information, droit. **Elle est absente de ce corpus là où le champ se construit, c'est-à-dire là où portent les questions d'interopérabilité elles-mêmes — mais elle n'est pas absente du champ**, et la passe de contrôle sur DBLP et Crossref rapportée aux limites trouve de la littérature arbitrée sur quatre des fronts que ce corpus donne pour vides.

# Les protocoles d'interopérabilité

## Ce que la littérature établit

La sous-spécification de la couche sémantique est passée du statut de « défi ouvert » des surveys [1], [2] à celui de résultat mesuré, par quatre chemins indépendants. Empiriquement : sur 856 outils de 103 serveurs MCP, 97,1 % des descriptions portent au moins un défaut et 56 % n'énoncent pas clairement leur objet ; les enrichir ne gagne que 5,85 points médians de succès, allonge l'exécution de 67,46 % et régresse dans 16,67 % des cas [53]. Sur 19 200 paires description/code issues de 2 214 serveurs réels, 9,93 % sont incohérentes, sans qu'aucun mécanisme du protocole ne vérifie que la description reflète l'implémentation [55]. Formellement : MCP et Schema-Guided Dialogue sont bisimilaires sous une application dont l'inverse est partielle et à perte, ce qui démontre au lieu de conjecturer les manques d'expressivité de MCP [56]. Analytiquement : sur 18 protocoles, transport, schéma et cycle de vie sont mûrs, mais clarification, alignement de contexte et vérification restent hors protocole [62].

Deuxième acquis, l'écosystème déployé ne se conforme pas aux hypothèses de la littérature de protocole. Sur 1 723 applications consommatrices, seules 37,2 % imposent une approbation bloquante avant exécution d'outil, le protocole ne spécifiant pas le côté client [54]. Le registre officiel n'est pas stable : sur 88,6 jours, 8,6 % de serveurs réécrivent une description, la moitié des changements atterrissant sur des arrivants qu'un classement par dérive ne peut atteindre, d'où un ré-audit ciblé couvrant environ 10 % des changements [58]. Enfin, sur 2 297 projets validés (précision 83 %), une strate purement pédagogique doit être exclue sous peine de gonfler toute mesure d'écosystème [59].

Le côté client ne consomme même pas ce que le serveur lui remet. Sur 54 000 essais et 24 modèles interrogeant un serveur MCP juridique en production, retirer l'outil de recherche concurrent porte à 98 % au moins la lecture des données embarquées dans les instructions du serveur chez 23 modèles sur 24 ; la seule présence de cet outil la fait retomber sous 15 % chez neuf d'entre eux. **L'échec relève donc de la préférence comportementale et non d'une incapacité**, et aucune ingénierie d'invite par serveur n'y remédie de façon portable, certaines interventions se retournant contre des familles de modèles précises [183]. *Quatre pages, acceptation annoncée au seul champ de commentaire, pour un atelier que ce champ déclare lui-même non archival.*

Troisième acquis, aucun protocole ne s'impose et la question s'est déplacée vers la composition : l'analyse séparée de MCP et A2A crée un fossé sémantique, que le premier cadre unifiant les deux formalise en 30 propriétés temporelles [60] ; la seule comparaison adossée à deux implémentations de la même tâche conclut que la répartition des responsabilités de coordination, non les fonctionnalités, sépare les deux protocoles, ses auteurs qualifiant ce résultat d'observations de conception [57] ; la seule interopération hétérogène publiée superpose une spécification déclarative à un protocole industriel au lieu de le remplacer [61]. Une position minoritaire récuse l'unité d'échange : l'intention représentée comme programme typé par effets réduit la latence jusqu'à 53,4 % et le trafic client jusqu'à 96,1 % [63].

## Le désaccord : prévalence mesurée ou prévalence héritée

Une ligne de travaux mesure l'écosystème MCP et alarme ; un travail mesure l'instrument et l'invalide. Sur 64 611 serveurs uniques dont 37 288 analysables dynamiquement — extension du jeu de données [52] —, les scanners qui déclarent 96,89 % des serveurs « à risque » présentent moins de 50 % de vrais positifs à la validation manuelle et se contredisent entre eux [51]. Le désaccord n'est pas de vocabulaire : deux corpus réels, une divergence sur la validité de l'outil, aucune réplication par un tiers. Deux traits l'aggravent, documentés par les pièces elles-mêmes. Monoculture méthodologique : les études de sécurité MCP partagent un même dispositif, l'audit d'un registre à un instant unique, et aucune n'a mesuré la durée de validité du texte qu'elle juge [58]. Chiffre hérité : le taux de 96,89 % provient de scanners appliqués à peu de cas et se propage par citation — repris, non reproduit [51].

Le même vice se retrouve là où le champ a voulu chiffrer non plus le danger de MCP mais son coût. Les estimations publiées de l'écart entre appel d'outil par MCP et par ligne de commande divergent de plus d'un ordre de grandeur et reposent sur des rapports de praticiens irreproductibles. La première mesure contrôlée à les départager — une tâche logicielle unique de six opérations contre un dépôt git privé, sept échafaudages d'agent, cinq modèles, achèvement vérifié par inspection de l'état du dépôt et non par l'auto-rapport de l'agent — conclut que **la comparaison elle-même ne tient pas** : treize rapports MCP/CLI strictement appariés s'étalent de 0,43× à 29× [177]. L'effet dominant est l'échafaudage, non l'interface : deux des sept échafaudages n'offrent aucun support MCP, achèvent pourtant chaque exécution en ligne de commande seule, et reviennent de 5,0 à 28 fois moins cher que les cinq qui en offrent — comparaison faite entre exécutions en ligne de commande de part et d'autre, sans serveur MCP attaché nulle part. Et les agents ignorent fréquemment l'interface qui leur est assignée, de sorte qu'**une comparaison qui ne vérifie pas le comportement effectif mesure un mélange inconnu** [177]. *Prépublication de quatre auteurs ; harnais, tâche, validateur et jeu de données publiés sous licence libre.*

## Ce qu'elle ne traite pas

Manque vérifiable : aucune publication ne rapporte un taux mesuré d'échec, de latence ou de perte sémantique pour une tâche traversant deux protocoles distincts dans un système déployé, sur corpus reproductible. Toutes les mesures d'écosystème portent sur MCP seul [51], [53], [54], [55], [58], [59], [183] ; la seule comparaison implémentée entre deux protocoles est un scénario unique dont les auteurs récusent la généralisation [57] ; la seule interopération hétérogène démontrée ne rapporte aucun taux d'échec [61]. [177] fournit le premier dispositif contrôlé et reproductible du front, mais il oppose MCP à une ligne de commande, non à un second protocole d'agent. Corollaires : aucune mesure longitudinale pour A2A, ACP ou ANP [58] ; aucune propriété formelle vérifiée sur un déploiement réel — 30 propriétés définies sans vérification [60], une équivalence prouvée sans évaluation sur agents [56].

# La sécurité des agents et de leurs protocoles

## Ce que la littérature établit

Le défaut de fond n'est pas dans le modèle : c'est l'absence d'isolation entre contenu de confiance et contenu non fiable. Quatre pièces y aboutissent par des voies distinctes. La famille des injections de *donnée* — charge déguisée en identifiant de ressource, en origine de données ou en format de réponse d'outil, échappant donc aux défenses conçues contre l'injection d'instruction — est démontrée sur six agents commerciaux nommés, et le diagnostic y est posé comme tel [64]. L'analyse de cause racine des chaînes d'outils parasites, sur 12 230 outils de 1 360 serveurs, l'identifie sous sa forme jumelle : MCP n'offre ni isolation contexte–outil, ni moindre privilège [66]. Le banc de 202 paires injection–tâche sur les fichiers de compétences conclut que ni l'échelle des modèles ni le filtrage d'entrée n'y suffiront [68]. La seule proposition constructive du lot en tire la conséquence : convertir la donnée non fiable en types de portée et de contenu bornés [74].

Deuxième acquis, mesuré sur un même banc : la capacité aggrave l'exposition et l'alignement ne protège pas. Sur 45 serveurs vivants, 353 outils authentiques et 1 312 cas de test évalués sur 20 agents, l'empoisonnement de métadonnées atteint 72,8 % de succès **sur le modèle le plus vulnérable du lot, o1-mini** ; la susceptibilité croît avec la capacité du modèle, et le taux de refus le plus élevé reste inférieur à 3 %, l'attaque n'employant que des outils légitimes [67]. Un second banc atteint 80 % sur les modèles de pointe [68].

Troisième acquis, décisif pour la lecture de tout le front : les scores de défense obtenus sur bancs statiques ne survivent pas à l'adaptatif. Une défense mesurée à 0 % de succès d'attaque en statique remonte à 28 % au global et 64 % sur les tâches où l'action elle-même est déléguée à du contenu contrôlé par l'attaquant, dès qu'une optimisation en boîte noire et à bas coût la cible — trois suites de tâches, cinq modèles cibles [71]. L'audit de dix défenses sur 60 tâches ouvertes et 560 cas d'injection conclut que **presque aucune n'est déployable**, chacune étant soit insuffisamment sûre, soit sur-défensive au point d'entamer la fonctionnalité [72]. ⚠ *Le gel du 9 août écrivait « aucune » : la pièce conclut sur « presque toutes », et la correction est faite ici plutôt qu'en silence.* Sur six systèmes multi-agents et 1 356 cas, les défenses mises au point en environnement simplifié ne transfèrent pas et peuvent créer de nouvelles vulnérabilités [69]. Trois mécanismes de contrôle d'accès publiés tombent à 86,3 % de contournement pour 4,4 % de dégradation d'utilité [73]. Deux attaques enfin sont opposables en production : 14 scénarios contre des assistants déployés, dont 73 % classés en risque élevé à critique avant mitigation par l'éditeur [65], et la famille précitée [64].

Un contre-exemple revendiqué est apparu le 13 août, et son régime décide de sa portée. Un filtrage des unités de réponse par provenance et par attente sémantique ramène le succès d'attaque moyen de 84,7 % à 2,3 % sur six découpages de deux bancs — dont AgentDyn [72] —, en préservant l'utilité bénigne, 92,5 % contre 90,6 % sans défense [185]. *Défense évaluée par ses propres auteurs, sur un seul agent cible, contre des attaques adaptatives de type PAIR.* **Ce n'est pas le régime qui a fait tomber les autres défenses** : nulle optimisation en boîte noire ne vient ici cibler la défense elle-même, comme dans [71]. Le contre-exemple est à retenir, non à opposer.

## Où elle se contredit

Premier désaccord, le coût d'utilité de la prévention par construction. Le typage de la donnée non fiable revendique une prévention systématique assortie d'une utilité « forte et non triviale » [74] — revendication adossée à des études de cas non dénombrées, donc auto-évaluation et non évaluation adverse. Deux mesures indépendantes disent l'inverse : l'audit de dix défenses trouve que celles qui tiennent le font par des mesures excessivement défensives dégradant la fonctionnalité [72] ; et le travail qui obtient pourtant le meilleur rabattement du front, de 85–100 % à 0–5 % sur quatre architectures de mémoire, qualifie le déploiement réel de problème ouvert à cause d'un coût d'utilité très variable [70].

Second désaccord, plus lourd. L'écosystème MCP est déclaré criblé de *gadgets* exploitables en conditions réelles, sur 12 230 outils et 1 360 serveurs [66] ; sur un corpus cinquante fois plus grand, l'instrument qui produit ce type de constat est montré faux à plus de moitié [51]. Les deux ne peuvent décrire correctement le même parc, et ce désaccord entame la valeur probante de tous les pourcentages de prévalence du front, y compris ceux repris par les surveys [3], puisque soit la sévérité est sous-décrite, soit une part importante des taux publiés est un artefact d'outil.

Deux pièces de la mi-août tranchent dans le sens de l'artefact, chacune à sa portée. La première audite une campagne d'évaluation de sécurité MCP conservée et **montre que le défaut était dans le correcteur** : 10 200 lignes d'exécution ramenées à 180 requêtes liées au modèle, 45 requêtes sémantiques et 15 stimuli observables ; la métadonnée de traitement conditionnait la classe ATTACK_SUCCESS, si bien qu'un comportement inchangé changeait de classe sous simple réétiquetage. Une reconstruction aveugle au traitement reclasse 58 étiquettes ATTACK_SUCCESS ou HIJACK_ATTEMPT en achèvements bénins autorisés, tout en préservant trois transferts de données protégées vérifiés et un cas distinct de réacheminement non autorisé ; **le recensement verrouillé ne contient plus aucun ATTACK_SUCCESS** [178]. *Prépublication de deux auteurs, qui bornent eux-mêmes le résultat à un audit circonscrit à une campagne — ni taux d'attaque de population, ni classement de modèles, ni efficacité de défense. La notice ne nomme pas la campagne auditée, ne la rattache à aucune pièce du présent corpus, et ne dit pas si les auteurs auditent leur propre travail.*

La seconde rend le constat systématique. **Réduire la sécurité d'un agent à un taux de succès d'attaque unique confond exposition, exécution, observation et adjudication**, et confond une violation réelle avec la visibilité de sa preuve. Sur 1 661 cas répartis sur cinq surfaces de service, six modèles et trois harnais, le taux moyen s'établit à 65,69 % — **mais le taux rapporté varie avec le harnais retenu et avec la vue de preuve**, et divulguer le contexte d'évaluation change le comportement d'exécution [184]. La pièce vérifie les effets nuisibles sur les reçus de service et l'état final plutôt que sur la sortie de l'agent, et relève un écart reconnaissance–exécution : près d'une violation confirmée sur cinq survient après que l'agent a énoncé la contrainte qu'il enfreint. *Prépublication de neuf auteurs.*

## Ce qu'elle ne traite pas

Aucune pièce ne mesure quoi que ce soit sur un parc d'entreprise en exploitation. Les tailles d'échantillon se comptent en serveurs (64 611 ; 1 360 ; 45), en outils (12 230 ; 353), en cas de test (1 661 ; 1 356 ; 1 312 ; 560 ; 202), en modèles ou agents (20 ; 6 implémentations), en produits (6 nommés ; 14 scénarios) — jamais en organisations, en déploiements ni en incidents observés, sans aucune télémétrie de production.

La lacune de second rang du gel s'est en revanche comblée. La fiabilité des scanners avait été auditée [51] ; celle des dispositifs qui notent les attaques l'est désormais aussi, par un audit de campagne [178] et par un cadre qui mesure l'écart entre taux rapporté et violation vérifiée sur l'état final [184]. **Ce qui reste ouvert n'est plus l'absence d'audit mais son absence de réplication** : aucune de ces deux pièces n'a été reproduite par un tiers, et elles ne portent pas sur les mêmes bancs. Demeure enfin la lacune inter-organisationnelle : la seule pièce inter-agents reste intra-système [69], rien ne portant sur la chaîne d'appel entre organisations distinctes.

# L'identité, la délégation et la révocation

## Ce que la littérature établit

La convergence la plus forte du corpus porte sur l'atténuation : l'autorité doit décroître à chaque saut au lieu de se transmettre intacte, et le jeton porteur relayé tel quel est unanimement tenu pour le mauvais primitif. Elle est obtenue par des travaux qui ne partagent ni méthode ni objet : atténuation de portée de ressource comme opérateur compositionnel, avec preuves formelles et évaluation d'applicabilité [83] ; rétrécissement d'autorité mécaniquement vérifié en TLA+ sur 2,7 M d'états, aux côtés du confinement de cascade et de la reconstructibilité forensique [76] ; chaîne append-only où chaque saut est signé et vérifiable hors ligne, contre l'incapacité d'OAuth 2.0 et des JWT à porter une délégation multi-sauts autorisée par un humain [77] ; capacités bornées par époque se fermant à l'achèvement de la tâche [87]. Le socle proposait déjà des jetons de capacité liés à l'invocation [16].

Deuxième convergence : la validité doit être liée à un événement, non à une horloge. Trois travaux indépendants, qui ne se citent pas et ne partagent ni domaine d'application ni vocabulaire, obtiennent des gains d'ordre cent sur les baux temporels et sur OAuth 2.0. *Les trois ne les obtiennent pas au même régime, et la colonne de droite le dit : un facteur mesuré en simulation et un facteur mesuré sur essaim d'agents réels ne s'additionnent pas.*

: Trois voies indépendantes vers une validité liée à un événement, chacune avec le régime où son gain a été obtenu.

| Pièce | Événement liant la validité | Gain rapporté | Référentiel | Régime de mesure |
|---|---|---|---|---|
| [75] | compteur d'exécutions, cohérence dirigée | D ≤ n, indépendant de la vitesse de l'agent ; 120–184× | baux temporels | simulation à événements discrets, 120 exécutions, 3 scénarios |
| [80] | preuve périodique de vivacité du parent | ~90× sur la fenêtre d'agent zombie | OAuth 2.0 | couche protocolaire et essaims d'agents réels (GPT-4o-mini) |
| [87] | achèvement de tâche, poignées bornées par époque | fermeture de l'accès futur, sans facteur chiffré | autorité résiduelle | moniteur de référence, tâches de codage contrôlées, dépôts réels figés |

Troisième acquis : l'identité ne suffit pas, c'est l'action qu'il faut prouver. Le contexte de délégation doit être lié pendant l'exécution et non reconstitué après [84] ; la preuve d'action doit être ancrée plutôt que déclarée par l'opérateur [86] ; chez les identités non humaines, une modélisation à l'échelle d'une flotte infonuagique réelle montre que le sur-privilège est un régime temporel et non un état [82]. Le terrain ne tient pas le socle à un seul saut : sur 7 973 serveurs MCP distants, 40,55 % exposent des outils sans aucune authentification, les failles d'enregistrement dynamique de client touchent 96,6 % des serveurs testés [81] ; près de 100 000 enregistrements d'identité multi-chaînes confirment une infrastructure immature [42]. La vérification formelle des spécifications relève enfin 35 lacunes de spécification et 30 défaillances nées de la seule composition : un seul protocole applique effectivement un contrôle de sécurité, aucun n'assigne la responsabilité d'application au comportement inter-protocoles [85].

Le seul parc d'entreprise décrit dans le corpus est arrivé le 11 août. Un rapport de déploiement industriel — des dizaines de serveurs MCP internes montés en une année, chaque équipe ayant implémenté son authentification de son côté, certaines sans aucune, d'autres par clé d'API, d'autres par OAuth complet — place devant chaque serveur en aval une passerelle unique d'agrégation, de gouvernance et d'authentification : modèle à deux axes croisant la personne, utilisateur interactif ou automate non humain, avec le type de justificatif ; trois octrois d'authentification unique d'entreprise ; trois modèles d'approvisionnement de jeton ; et délégation par échange de jetons RFC 8693 [179]. Le motif déclaré du chantier est ce que la littérature du front traite le moins : autoriser les appelants de façon cohérente, savoir qui a fait quoi, et retirer ses accès à un employé qui part, à l'échelle du parc. *Rapport d'expérience de trois auteurs : aucune mesure, aucun taux, aucun effectif au-delà de « des dizaines de serveurs ». Sa notice ne dit rien de l'atténuation d'autorité par saut, ni pour ni contre. Elle atteste d'une architecture en production, pas d'un résultat.*

## Où elle se contredit

Premier désaccord, l'emplacement de la racine de confiance et son prix opérationnel. Une position soutient qu'aucune preuve d'action n'est opposable sans ancrage matériel — architecture IETF RATS composée avec des paquets de preuves d'action et une mesure d'intégrité TPM, l'objet vérifié étant la production effective de la sortie par la version de modèle annoncée sur du matériel non modifié [86]. Deux travaux revendiquent l'opposabilité sans matériel spécialisé ni vérificateur en ligne : vérification hors ligne à la seule clé publique Ed25519 de l'émetteur [77] ; fraîcheur appliquée avec les seules clés en cache et l'horloge locale du vérificateur [80]. Le désaccord est symétrique dans ses coûts : le premier camp exige une infrastructure d'attestation que la quasi-totalité des parcs d'entreprise n'a pas ; le second accepte structurellement qu'un agent compromis mais vivant signe des sauts parfaitement valides.

Second désaccord, un arbitrage de type CAP déguisé en question d'identité. Borner les opérations non autorisées indépendamment de la vitesse de l'agent suppose, par l'analogie même avec la cohérence mémoire qui fonde le résultat, un point de sérialisation partagé [75]. L'autre position refuse tout aller-retour réseau au moment de la vérification et assume en contrepartie une fenêtre résiduelle égale à l'intervalle de battement [80]. Aucune des deux pièces ne reconnaît la position adverse : le champ n'a pas nommé l'arbitrage qu'il pratique.

## Ce qu'elle ne traite pas

Toutes ces pièces bornent la fenêtre pendant laquelle un agent révoqué agit encore ; aucune ne dit ce qu'il advient des effets et des sous-délégations déjà émis quand un saut amont est invalidé après coup. Il n'existe ni sémantique de compensation en cascade, ni critère décidant quels effets aval sont annulables. La lacune est vérifiable par lecture : un compte d'opérations non autorisées est borné [75], une fenêtre est bornée [80], un accès futur est fermé [87] — tous en régime purement préventif. Deux constats l'aggravent : des traces d'exécution identiques peuvent correspondre à plusieurs assignations de délégation mutuellement incompatibles, si bien que l'ensemble des effets à compenser n'est pas calculable a posteriori [84] ; et aucun des quatre régimes réglementaires européens examinés — règlement IA, RGPD, règlement Machines, directive Responsabilité du fait des produits — ne définit à qui incombe cette compensation, la dégradation de la chaîne de consentement restant non traitée dans ses dimensions centrales [79].

Une pièce du 12 août traite la moitié informationnelle du problème, et il faut resserrer la lacune d'autant. **Un modèle bitemporel à admission liée à la source décide si un enregistrement contradictoire, remplacé, rétracté, supprimé ou périmé peut encore étayer une affirmation sortante**, par cinq clauses exécutables dont la non-résurrection après rétractation ou suppression ; sur un banc de 3 600 cas figé par empreinte, la voie gouvernée reproduit tous les dénouements complets, quand la meilleure de trois politiques complètes simples n'en apparie que la moitié [186]. *Auteur unique ; la pièce borne elle-même sa portée à des résultats de contrat et d'implémentation, non à une exactitude en monde ouvert.* Ce qu'elle gouverne, ce sont les enregistrements et les affirmations qui en dérivent. **Les effets déjà produits et les sous-délégations déjà consenties restent sans sémantique de compensation** : chaîner les droits de façon vérifiable, et même chaîner la validité des faits, ne dit rien du chaînage des conséquences.

# Les systèmes multi-agents : orchestration et défaillance

## Ce que la littérature établit

Sur les journaux de 127 systèmes multi-agents rassemblés par le jeu Who&When, la meilleure attribution automatique trouve l'agent fautif dans 53,5 % des cas et l'étape décisive dans 14,2 %, plusieurs méthodes faisant moins bien que le hasard [88]. **Ce plafond est celui d'un banc, non celui de la tâche.** Un modèle de contextualisation agent–étape déposé le 11 août rapporte 81,58 % sur l'agent fautif et 63,90 % sur l'étape fautive, contre 78,20 % et 56,33 % pour sa meilleure ligne de base — mais sur deux autres bancs, TracerTraj et Aegis-Bench, Who&When ne lui servant que d'épreuve hors domaine [187]. *Prépublication non révisée par les pairs : les auteurs y mesurent leur propre modèle.* Les traces complètes — entrées et contexte, non les seules sorties — améliorent quant à elles l'attribution jusqu'à 76 % contre une observation partielle [89], gain relatif sans effectif ni condition nommée. **Trois mesures d'attribution, trois bancs, aucun dénominateur commun : sur ce front, le chiffre d'attribution est d'abord une propriété du banc.** MAST impute ces échecs à la coordination plutôt qu'au modèle de base, sur plus de 1 600 traces annotées [48] ; sur six cadriciels, une erreur atomique unique fige un faux consensus [90]. La coordination s'isole comme couche, à modèle, outils et invite figés [91].

Le rendement du multi-agent est non monotone. Un agent unique bien invité égale presque la meilleure discussion multi-agents, qui ne l'emporte que sans démonstration dans l'invite [92] ; sur six bancs et 245 caractéristiques, l'agent unique gagne dans environ 43,3 % des cas [95] ; les architectures engendrées automatiquement restent sous la chaîne de pensée avec auto-cohérence, à coût jusqu'à dix fois supérieur [94]. Les favorables ne l'infirment pas : la loi d'échelle collaborative, établie jusqu'à plus d'un millier d'agents, est logistique donc saturante [96] ; l'optimisation entrelacée invites-topologie-invites fait dépendre la performance davantage du réglage des invites que du patron topologique [97]. Le surcoût de coordination va de 1,15× à 2,3× selon le patron sur 10 000 dépôts SEC rejoués [98] ; la supervision d'exécution en récupère −29,68 % de jetons sans perte de succès sur GAIA [99].

Une pièce du 13 août atteint le calcul qui justifie la redondance, en amont de toute architecture. **Les bornes de fiabilité compositionnelle multiplient les fiabilités des composants, opération que seule autorise une hypothèse d'indépendance conditionnelle qu'on énonce couramment et qu'on ne teste jamais.** Testée, elle tombe : deux instances d'un même modèle, en passage de main à deux agents, échouent ensemble sur 90,0 % des missions où l'une des deux échoue, et **l'erreur a un signe qui joue contre l'exploitant — la redondance est sur-créditée exactement quand les composants partagent un modèle** [180]. *Évaluation préenregistrée sur 18 000 missions, notées par du code déterministe et sans juge modèle : le régime de mesure le plus exigeant du front. La pièce est rattachée à la chorégraphie et à l'essaim, où son dispositif est instruit au complet.*

## Où le désaccord est réel

Le clivage sur l'utilité du multi-agent suit la méthode, non l'objet ; la ligne de base dite forte s'entend comme invite riche, auto-cohérence et ensemblage. Une pièce tranche en partie : le débat multi-agents n'est pas intrinsèquement inférieur, il est hypersensible aux hyperparamètres et redevient compétitif après réglage [93]. Tout résultat mesure donc d'abord l'effort de réglage consenti à chaque bras, qu'aucune pièce du front n'égalise.

: Les quatorze pièces du front retenues au gel du 9 août : onze évaluent une construction de leurs auteurs et quatre annoncent un comité de lecture ; les quatre évaluations indépendantes contre ligne de base forte concluent toutes au non-avantage.

| Position | Système évalué | Ligne de base | Pièces |
|---|---|---|---|
| Avantage du multi-agent | architecture des auteurs | non optimisée | [96], [97] |
| Non-avantage | architecture de tiers | forte | [92], [93], [95], [94] |

[180] ne prend pas parti dans ce clivage, et c'est ce qui lui donne son poids : il n'oppose pas une architecture à une autre, il éprouve une hypothèse dont les deux camps se servent. **Tant que la dépendance entre composants n'est pas mesurée, une fiabilité annoncée par composition n'est pas une fiabilité mesurée** — et l'échappatoire est fermée : ajuster un modèle de dépendance fait pire que s'en passer, la pièce prouvant qu'une borne bootstrap sur la fonctionnelle d'un modèle ajusté perd la couverture de la vérité à mesure que *n* croît, l'écart d'identification étant en O(1) quand la correction bootstrap n'est qu'en O(n^−1/2). *Plus de données rend alors le certificat plus faux, sans symptôme visible.*

Second désaccord : ce que résout la traçabilité. Levier de diagnostic principal pour [89], elle laisse échapper un canal d'état — un contexte toxique compressé en résumé passe sous le seuil des détecteurs en augmentant la toxicité en aval [100] : instrumenter davantage et gouverner l'écriture en mémoire sont deux corollaires opposés. Même partage sur la supervision : machine, elle réduit le coût sans perte [99] ; humaine et fatigable, elle suit un U inversé, la sécurité réalisée se dégradant au-delà d'un seuil d'escalade (125 actions étiquetées, kappa de Fleiss = 0,52, auteur unique) [101].

## Ce qui n'est pas traité

Aucune pièce ne mesure un assemblage en exploitation d'entreprise, taux de défaillance observé sur durée et volume réels. Les mesures portent sur des bancs académiques, des corpus hors ligne (10 000 documents [98]), des marchés de prédiction (100 marchés [91]), des journaux a posteriori (127 systèmes [88]), des missions synthétiques en dispositif contrôlé (18 000 [180]) ; le 41 à 87 % d'échec « en production » est repris de la littérature par [91], non mesuré par son protocole. Manque également toute comparaison contrôlée des patrons d'orchestration — superviseur, transfert, graphe, marché — à modèle, invite, outils et budget figés sur plusieurs domaines. Deux pièces s'en approchent : [98] compare les patrons, sur un domaine unique et sans comité de lecture ; [91] fige modèle, invite et outils, sur cinq configurations d'un seul modèle. La seule normalisation multi-bancs du corpus porte sur des architectures, non sur ces patrons [159].

# L'évaluation, les bancs d'essai et l'observabilité

## Ce que la littérature établit

Le score publié n'est pas ce qui s'observe, et cinq voies indépendantes l'établissent. Défauts de conception : tests insuffisants, réponses vides comptées comme succès et récompenses mal spécifiées faussent les scores des bancs les plus utilisés [107]. Généralisation : une part substantielle de la performance sur SWE-bench Verified relève de la mémorisation du dépôt, les mêmes modèles chutant fortement sur des tâches hors distribution appariées [108]. Enchaînement en exploitation : sur une chaîne de construction de compilateur à dépendances sérielles, la réussite s'effondre de 100 % au premier étage à 20 % au dernier, aucun des 15 modèles n'achevant le pipeline [105]. Les bancs d'entreprise donnent la même pente : environ 30 % de tâches professionnelles achevées en autonomie dans une entreprise logicielle simulée [102], 58 % en tour unique contre 35 % en multi-tours sur des scénarios d'affaires [104].

Transport d'exécution, quatrième voie. Un banc de 56 tâches en un coup, tirées de 14 familles dérivées d'incidents réels, croise le contrat de génération avec le chemin d'exécution autour d'un analyseur syntaxique délibérément ajouté et non échappé. **Rejouer la même réponse à travers cet analyseur fait chuter la réussite de 55,4 à 73,2 points** selon huit configurations comparables ; divulguer la frontière au modèle en récupère 30,4 à 60,7 points pour six d'entre elles, zéro ou légèrement négatif pour les deux autres. Un modèle dont l'écart de score apparié n'est que de −3,6 points cache ainsi −64,3 points de dégât et +60,7 points de compensation, et la configuration de déploiement réordonne les modèles : sur 26 paires comparables, un renversement est net et quatre autres tiennent à une tâche près [181]. La génération brute est presque saturée à la frontière ; ce qui sépare encore les modèles est leur adaptation à cette frontière. **Le score n'est donc pas une propriété du modèle mais du montage**, et une évaluation qui ne déclare pas sa configuration de modèle, son contrat de génération, son chemin d'exécution, son point de fonctionnement et son validateur d'état final ne dit pas de quoi elle parle. *Prépublication de quatre auteurs.*

Décomposition de variance, cinquième voie, et la plus radicale. Sur trois bancs ouverts de traces d'agents — dont TheAgentCompany [102] —, **l'effet propre de l'agent explique moins de 3 % de la variance totale dans chaque jeu et chaque type de contrôle, quand l'interaction agent × tâche en explique de 7 à 23 %** ; la fiabilité agrégée s'effondre sur le quartile de tâches le plus dur, un coefficient tombant de 0,752 à 0,000 ; et la fiabilité mesurée en cellule d'entraînement est négativement corrélée à la fiabilité hors échantillon, à r = −0,90 [190]. Sur la taxinomie d'échecs MAST [48], les profils relevés trace par trace sont idiosyncrasiques quand les profils par cellule se généralisent. *Décomposition à quatre facettes, trois estimateurs concordant à trois décimales, artefacts publiés ; auteur unique, prépublication.* La conclusion excède les quatre autres voies : **un classement d'agents ne classe pas des capacités, il classe des spécialisations.**

Deuxième acquis : le coût et le régime d'exécution sont des dimensions d'évaluation, non des annexes. L'exactitude seule est vide de sens sans axe de coût, et l'absence de jeu de retenue rend les scores irreproductibles [106] ; en exploitation, la dépense varie de trois ordres de grandeur entre modèles de qualité comparable [105] ; le prix de l'auditabilité se chiffre à son tour, **8,3 ms de surcoût médian** pour une médiation pré-exécution à traces infalsifiables, mesurés sur 1 000 interceptions consécutives d'appels d'outil — P95 à 14,7 ms, P99 à 23,1 ms, 1,2 % de faux positifs sur 500 appels bénins [113]. ⚠ *Ce chiffre et les 617 constats de sécurité relevés par analyse statique dans six projets ouverts sont deux mesures distinctes de la même pièce ; le gel du 9 août les présentait comme une seule.*

Troisième acquis : la trace est devenue l'objet évalué, et les modèles la lisent mal. Sur 148 traces annotées par des humains, collectées au format d'observabilité réellement déployé, le meilleur modèle à long contexte n'atteint que 11 % en localisation d'anomalie [111]. La provenance doit relier l'invite, la décision, l'appel d'outil et le résultat en aval [112] ; l'auditabilité se décompose en cinq dimensions — recouvrabilité de l'action, couverture du cycle de vie, vérifiabilité de la politique, attribution de responsabilité, intégrité de la preuve —, et la pièce désigne **l'intégrité de la preuve et la couverture du cycle de vie** comme les plus négligées de tous les travaux qu'elle recense [113]. ⚠ *Le gel du 9 août désignait à cette place l'attribution de responsabilité ; la pièce, v1 comme v2, nomme les deux autres.*

## Où le désaccord est réel

Le litige dur porte sur l'évaluateur automatique. Une pièce conclut qu'un juge agentique, notant les étapes intermédiaires et non le seul résultat, s'approche de la fiabilité humaine à une fraction du coût [110]. Une autre démontre l'inverse au niveau du principe : dès lors que le juge n'est pas plus exact que l'évalué, aucune méthode de débiaisage ne réduit de plus de moitié le besoin d'étiquettes de référence [109]. Le désaccord oppose une mesure empirique à un plafond théorique et n'est pas dissoluble par davantage de données ; la mesure empirique est de surcroît auto-arbitrée, les mêmes auteurs publiant le banc (55 tâches, 365 exigences) et le juge qui y domine [110]. Deux autres conflits d'intérêts sont vérifiés : un banc d'entreprise partage quatre auteurs avec le système de référence qu'il mesure [102], [103] ; un banc d'affaires est publié par le fournisseur du produit agentique concurrent du domaine évalué [104].

Une pièce du 10 août déplace la question en amont du juge. **Toute une classe de portes de qualité expédiées dans les cadriciels d'agents — filtres de déduplication, caches sémantiques, gardes de dérive, correcteurs de réponse — décide à un seuil de similarité cosinus, c'est-à-dire mesure de combien la formulation a changé, quand la question posée est si le sens a changé.** Les deux divergent précisément sur les cas que ces portes existent pour attraper : la garde de dérive en production auditée n'a détecté aucune des 56 mutations qui rompent le sens, dont « withhold the study drug » devenu « administer the study drug », approuvé à un cosinus de 0,9608 ; sur 90 cellules de configuration, de seuil et de tâche, l'exactitude équilibrée ne dépasse jamais 0,700, pour une médiane de 0,525. **Le même biais corrompt l'évaluation censée le détecter** : un corpus construit naïvement en hérite et peut rendre un verdict inversé, l'AUROC de décision valant exactement 0,000 dans 13 cellules sur 18 [188]. *Auteur unique ; corpus, harnais et résultats figés publiés — et la pièce rapporte que le biais avait d'abord pris deux fois ses propres conclusions.*

Second désaccord : l'auditabilité s'obtient-elle par lecture a posteriori de la trace ou par médiation à l'exécution ? Le programme dominant instrumente puis analyse [111], [112]. Une pièce le tient pour structurellement borné : deux attributions de mandat incompatibles peuvent produire des traces strictement identiques, la télémétrie usuelle étant sémantiquement insuffisante pour reconstruire la propagation d'autorité [84]. Deux pièces de la mi-août prennent le second parti et le chiffrent. Une couche de mémoire à provenance typée exclut les enregistrements inéligibles, repondère les éligibles par confiance multiplicative de chemin et applique une porte sensible au risque avant exécution : sur 2 700 tâches synthétiques par méthode et trois domaines, 94,96 % de réussite et 72,70 % de décision exacte, d'où la thèse de **la provenance comme signal de contrôle opérationnel plutôt que comme métadonnée d'audit a posteriori** [189]. *Banc synthétique construit par ses auteurs, conclusion qu'ils bornent au cadre évalué.* L'autre définit l'exécution gouvernée par une provenance inspectable et mesure ce qu'elle coûte [182].

## Ce qui n'est pas traité

La trace comme preuve reste hors banc, mais l'énoncé du gel était trop large. Les bancs d'entreprise notent l'état final [102], [104], [105] ; les corpus de traces notent la localisation d'erreur [111], [48] ; l'auditabilité est proposée comme modèle de données [112], [84]. **[113], lui, mesure bel et bien une reconstruction** : son expérience de traçage implicite retrouve, sur des sorties dépouillées de leurs métadonnées et sous trois conditions de dégradation — retrait d'identité, corruption de frontière, caviardage —, une attribution de jetons voisine de 0,95, un recouvrement de segments d'environ 0,93 et une similarité d'arêtes approchant 0,96, sur des topologies de quatre à six agents en chaîne, en étoile et en arbre. *Auto-évaluation sur banc maison, sans arbitrage.* Ce qu'il reconstruit est la structure d'interaction, non le mandat.

**Il n'existe donc toujours aucun banc dont le critère de réussite soit : à partir de cette trace, un tiers peut-il reconstruire qui a mandaté quoi, et imputer la responsabilité ?** Une pièce du 13 août s'en approche par un autre bord : elle définit l'exécution gouvernée comme un travail dont les décisions, l'achèvement et la réaction au changement sont adossés à une provenance inspectable, et ses comparaisons contrôlées montrent que le chemin gouverné et le chemin direct atteignent souvent le même résultat, seul le premier conservant la preuve de l'autorité, refusant la clôture non étayée et bornant la reprise aux seules tâches dépendantes [182]. **Elle rapporte aussi son propre échec** — une épreuve de transfert entre rôles séparés où le contrat de complétude appliqué de façon déterministe sur-bloque massivement des paquets produits hors de son contexte de rédaction — et refuse de se présenter comme un gain d'exactitude. *Prépublication d'un seul auteur.* Restent non arbitrées les deux propositions qui lient contexte de délégation et exécution : prépublication de deux auteurs [84], auto-évaluation sur banc maison [76].

# La couche transactionnelle : paiements, marchés, réputation

## Ce que la littérature établit

Le mandat signé n'est pas le point de rupture ; ses deux bords le sont. En amont, l'intention que la signature scelle est déjà falsifiable : deux injections dans le contexte d'un agent d'achat de référence détournent le classement produit et exfiltrent des données utilisateur (90 à 100 % de réussite) [116]. En aval, les garanties de signature tiennent au niveau de la spécification mais pas à l'exécution — reprises, concurrence, orchestration —, défaut qu'une vérification à consommation unique et liaison de contexte corrige en banc de charge (~3,8 ms à 10 000 tr/s) [117]. Les deux systématisations nomment le même défaut autrement : liaison d'intention faible et découplage paiement/service [115] ; autorisation traitée comme une dimension parmi cinq qu'aucun protocole ne couvre entièrement [114]. C'est la seule convergence du front où mesure et systématisation disent la même chose.

Deuxième acquis, non contesté : des agents tarificateurs en langue naturelle atteignent en oligopole des prix supra-concurrentiels sans communication explicite, l'ampleur dépendant de formulations anodines de l'invite [119]. Le phénomène est retrouvé sous auto-optimisation des invites [121] et pris comme point de départ par la pièce qui n'en discute que la stabilité [120].

Troisième acquis : la réputation telle qu'implémentée ne porte aucun signal exploitable. Sur trois chaînes, la plupart des identités enregistrées n'exposent aucun point de service actif, les scores sont Sybil-attaquables par construction et la majorité des avis n'a aucun ancrage vérifiable [118] ; le socle établit par ailleurs que ces agents manquent de l'ancrage identitaire que présuppose tout mécanisme réputationnel [44]. Les marchés agentiques restent manipulables du côté vendeur [122], [124]. Le seul correctif qui déplace l'aiguille est économique — garantie exécutable, séquestre, sanction — et non réputationnel.

## Où le désaccord est réel

La collusion algorithmique est-elle un régime ou un artefact d'homogénéité ? Des stratégies collusoires stables et généralisantes émergent dès que les agents raffinent eux-mêmes leurs invites [121] ; à l'inverse, l'hétérogénéité fait chuter le surprix de 22 % à 10 % par la patience et à 7 % par l'asymétrie d'accès aux données, et aucune collusion soutenue n'est observée sur 1 000 périodes entre Q-learning et LLM [120]. Les deux mesurent des agents simulés en oligopole et divergent sur ce qui constitue le cas de base. L'arbitrage est empirique et personne ne l'a fait : si les marchés réels convergent vers deux ou trois modèles frontière, l'homogénéité est le cas réaliste et l'hétérogénéité le laboratoire. Aucune pièce ne mesure la population effective de modèles tarificateurs.

Second litige : les agents sont-ils des agents économiques compétents ? Quasi optimaux en conditions idéales, dégradés à mesure que le nombre d'options croît [122] ; déficitaires en raisonnement stratégique en négociation libre [123] ; non superposables au comportement humain sous mêmes institutions, dans la seule pièce à se donner un étalon humain [125] ; instables au point qu'un changement de modèle réordonne les préférences d'achat [124]. Le désaccord porte moins sur les agents que sur le protocole : structurés, ils s'en sortent ; en langue libre, ils échouent. Aucune pièce ne teste les deux régimes sur le même marché.

## Régimes de preuve et lacunes

: Régimes probatoires des douze pièces ; la seule mesure en production porte sur un registre de réputation, non sur un flux de paiement.

| Régime probatoire | Pièces | Part |
|---|---|---|
| Mesuré sur système déployé | [118], registres sur trois chaînes | 1 / 12 |
| Mesuré sur implémentation de référence ou banc de charge | [116], [117] | 2 / 12 |
| Simulé en environnement synthétique | [119], [120], [121], [122], [123], [124], [125] | 7 / 12 |
| Systématisé ou argumenté, sans donnée propre | [114], [115] | 2 / 12 |

Aucune pièce ne mesure de transaction réelle à valeur réelle sur une pile de paiement agentique en exploitation : tout énoncé sur le comportement des agents payeurs repose sur de la simulation. Le seul chiffre de volume du corpus est repris d'un texte de spécification et qualifié de non audité par les auteurs eux-mêmes [114].

Première lacune : aucune pièce ne traite la responsabilité d'une transaction non autorisée. Aucun travail ne modélise la répartition entre émetteur, acquéreur, marchand et fournisseur d'agent ; aucun ne confronte un mandat correctement circonscrit au régime de rétrofacturation existant ; aucun ne mesure un taux de contestation. Le contrôle porte sur le domaine entier et ne rend qu'une pièce principal-agent conceptuelle et jamais transactionnelle [142], une cartographie de conformité muette sur le contrat et le paiement [138], et une pile assurantielle qui présuppose résolue l'allocation de responsabilité qu'elle ne traite pas [45].

Seconde lacune, plus dure : la littérature raisonne sur une pile qui n'existe pas, et la fracture est visible dans les bibliographies. La systématisation la plus complète du règlement couvre x402, MPP, ERC-4337, Permit2, EIP-8004, Kite, Skyfire et Tempo, et ne mentionne ni AP2, ni ACP, ni L402 [115] ; symétriquement, les deux pièces AP2 ignorent x402 [116], [117]. Une seule pose les piles côte à côte, conclut à la fragmentation et date l'état de maintenance des spécifications qu'elle traite : AP2 sans implémentation de référence adoptée, ERC-8004 à déploiement limité, MPP le plus mûr [114]. Personne ne propose ni ne mesure un vocabulaire de capacités partagé ; le cadre analytique en quatre étapes fabriqué a posteriori pour comparer des protocoles sans terme commun [115] est le symptôme, non le remède. Les économistes présentent l'angle mort inverse : indifférents au rail de paiement [119], [124], [125], leurs résultats survivront à n'importe quelle obsolescence de spécification, mais restent muets sur l'autorisation et le règlement. Aucune pièce ne tient ensemble la formation du prix et le rail qui l'exécute.

*Reprise du 15 août 2026 : aucune des douze notices du front n'a bougé depuis le gel, et la fenêtre du 9 au 15 août n'a rien livré qui touche le rail de paiement, le taux de contestation ou la population de modèles tarificateurs. Le front est inchangé, et ses deux lacunes le sont aussi.*

# Les processus d'affaires et l'exécution durable

## Ce qui est établi

**L'installé est enveloppé, pas remplacé.** Le mouvement dominant ne substitue pas l'agent au moteur de processus : il l'encercle. Le harnais CUGA FLO place une couche agentique régie par politiques autour d'un moteur de workflow déterministe qui conserve l'autorité d'exécution [132] ; l'agenda neuro-symbolique fait des modèles de processus typés et des contraintes de conformité des composants architecturaux de l'agent, non une surveillance externe [131] ; l'architecture CHAI subordonne le modèle de langue à un graphe DCR qui encode les obligations légales et pilote le dialogue [137]. L'agent n'intervient qu'à des points de contrôle nommés — décider, adapter, formuler — jamais sur la trajectoire entière. La ligne prolonge les travaux d'ouverture sur les modèles de langue en gestion des processus [31], [37] et le relevé des perspectives praticiennes sur la gouvernance des agents en processus [32].

**La fiabilité vient d'une couche transactionnelle en aval, pas du modèle.** Ce que produit le modèle y est une proposition, jamais un effet. Atomix établit que le retour d'outil est une frontière de règlement fausse et n'engage les effets externes qu'une fois écartée toute arrivée concurrente antérieure [126]. Mnemosyne soumet toute action produite par un modèle à un contrôle d'admission déterministe et démontre que la correction de l'état engagé devient indépendante de la compétence du proposant, à moins de 6 % de surcoût [127]. La formalisation en TLA+ de quatre anomalies de concurrence des exécutifs multi-agents, avec exécutif Rust prouvé, fournit à cette thèse ses premières garanties mécanisées [128]. La filiation est assumée : le patron Saga [175] plutôt que l'ACID strict, et la sémantique de l'exécution durable [176] pour la persistance de l'état.

**La gouvernance passe par la conversion de la trace en journal de processus standardisé.** Traduire traces de raisonnement, appels d'outils et coûts en jetons vers un modèle d'événements normalisé est posé comme la précondition de l'audit, et dix-huit praticiens tiennent la transparence comportementale pour un prérequis de la confiance [130]. Les mêmes journaux servent en retour à engendrer les agents : la fouille de processus sur les enregistrements d'un dépôt découvre les rôles propres au projet et en produit les spécifications [135]. La ligne prolonge l'observabilité de la variabilité comportementale [38] et l'évaluation des modèles sur les tâches de fouille [39] ; le programme de la gestion agentique des processus [33], [34] en fait sa condition d'entrée.

## Le désaccord dur : atomicité contre réversibilité

: Deux ontologies incompatibles de la fiabilité agentique, non deux réglages d'un même paramètre.

|  | Atomicité [126], [127], [128] | Réversibilité [129] |
|---|---|---|
| Unité de fiabilité | la frontière de règlement | la position de l'action sur l'échelle idempotent / réversible / compensable / irréversible |
| Statut de l'effet | invisible avant engagement | émis, puis révisé |
| Place de l'humain | hors transaction | concurrente de l'exécution |
| Borne de l'agent | ce qu'on peut valider | ce qu'on peut défaire |

*Revisable by Design* rejette explicitement le paradigme transactionnel et pose que la flexibilité d'un agent est bornée par sa réversibilité [129]. Sous réversibilité, l'effet est visible et possiblement faux pendant un intervalle borné, et la correction est un flux, non une porte. Adopter l'un rend l'autre inatteignable : on ne peut pas simultanément suspendre l'effet jusqu'à la certitude et l'émettre pour organiser sa révision. Aucune pièce du corpus ne compose les deux régimes ni ne fournit de critère pour choisir entre eux selon la classe d'effet.

Second désaccord, moins tranché mais structurant : le modèle de processus est-il prescriptif *a priori* ou découvert *a posteriori* ? Le métamodèle BPMN étendu de constructions natives d'agent [133], le langage de protocole faisant des portes d'approbation humaine des invariants applicables [134] et le contrôleur DCR [137] écrivent le formalisme d'avance ; la génération de règles par modèle de langue relève du même geste [36]. La fouille inverse la causalité : le modèle est extrait des journaux et sert à produire les agents [135] ou la gouvernance [130]. Même communauté, directions opposées, et aucune des deux ne traite l'autre comme un cas particulier.

## Ce que la littérature ne traite pas

Personne ne mesure la conformité d'exécution d'un agent à un modèle de processus. Le contrôle de conformité au sens de la discipline — aligner une trace réelle contre un modèle de référence, quantifier *fitness* et précision — n'est appliqué à aucune trace d'agent autonome. [130] produit le journal mais s'arrête à la découverte et à la gouvernance ; [131] énonce la conformité par construction comme agenda et non comme résultat mesuré ; [136] évalue le modèle produit, jamais l'exécution. Contrôle vérifiable, refait à l'API du dépôt le 15 août 2026 et de compte inchangé depuis le gel : la requête `"conformance checking" AND "LLM"` rend sept entrées, la plus récente du 8 juin 2026, dont aucune ne porte sur des traces d'agents autonomes — celles qui s'en approchent alignent des plans ou du code, pas l'exécution d'un agent contre un modèle métier.

# La gouvernance, le risque et la responsabilité

## Ce qui est établi

**Aucune pièce ne réclame la personnalité juridique de l'agent.** Trois disciplines aboutissent à la même structure. En droit de la responsabilité délictuelle, l'imputation se fait par type d'interaction — dérive autonome, usage-outil, planification collaborative — et les journaux d'interaction deviennent le moyen de preuve situant l'écart à l'action autorisée [140]. En analyse économique du droit, le cadre principal-agent distingue les problèmes inhérents à la délégation de ceux qui émergent de la composition multi-agents [142]. En droit du mandat, les devoirs de divulgation et de loyauté ne sont pas encodés par les architectures d'agents et doivent devenir contrainte de conception [141]. Toutes remontent au mandant humain, et toutes conditionnent cette remontée à un enregistrement d'exécution.

**L'auditabilité est posée comme condition préalable de la conformité, non comme son corollaire.** L'informatique le pose formellement — pas de responsabilité sans auditabilité — et le mesure : lacunes répandues dans des projets d'agents libres, surcoût faible des enregistrements infalsifiables [113]. *Cette pièce a été étendue le 13 août 2026 : ses mesures ne bougent pas, mais son régime change — elle annonce désormais, au seul champ de commentaire, une version condensée dans les actes d'un sommet ACM, à une piste de « papiers visionnaires ».* Le droit en tire la conséquence la plus dure du corpus : un système à haut risque dont la dérive est intraçable ne peut satisfaire les exigences essentielles du règlement européen [138]. Le relevé documentaire, à cheval sur l'informatique et la politique publique, constate côté offre que la documentation de sûreté est majoritairement absente des systèmes déployés [144]. Le constat rejoint l'inexpressivité relevée des protocoles [21] et les cadres de gestion du risque [20], [174].

**Ce que la capacité du modèle n'achète pas, c'est la rejouabilité de sa décision.** Une mesure déposée le 11 août 2026 déplace la question d'un cran, de la disponibilité des journaux vers la reproductibilité de l'acte : sur neuf versions de modèles, d'un modèle local de trois milliards de paramètres à un système frontière commercial, **les commandes dont dépend le rejeu appartiennent au fournisseur et non au déployeur** — le système frontière refuse température, top_p et top_k et n'expose aucune graine. Sous les commandes les plus serrées que chaque point d'accès admet, le modèle local rejoue 320 exécutions sur 320, les modèles hébergés 319 sur 320 et 959 sur 960 ; l'architecture d'orchestration modifie l'action finale et aucun enregistrement d'exécution ne se répète, à aucune configuration ni à aucune échelle ; et deux versions déterministes d'un modèle de crédit rejouent chacune parfaitement leur action courante sans pouvoir retrouver l'action historique [191]. *La reproductibilité n'y est pas un scalaire mais un profil, et l'autorité déléguée n'est défendable que tant que la preuve conservée en soutient l'exercice.* Régime : **prépublication non révisée par les pairs**, d'un auteur unique, trois études sur ses propres montages, non répliquées ; l'énoncé d'ouverture sur l'ampleur de la délégation en finance y est argumenté, non mesuré.

**La supervision humaine n'est démontrée nulle part comme contrôle effectif.** Le droit établit que le règlement charge la supervision humaine de corriger le biais d'automatisation sans base empirique attestant qu'elle y parvient, et avec une répartition contestable entre fournisseur et déployeur [143]. L'enquête de terrain en santé, relevant de l'informatique et de l'interaction humain-machine, observe une supervision quasi totale : non un contrôle calibré, mais un frein imposé par la responsabilité [147].

## Deux désaccords, dont un de prémisse

Le premier porte sur le lieu de la défaillance réglementaire. Le droit répond que le règlement est opérationnalisable sous condition, une architecture de conformité étant constructible dans le droit existant, l'obstacle restant technique [138]. La politique publique répond que le déficit est institutionnel — surveillance, mise en application, ressources — et qu'aucune architecture côté fournisseur ne le comble [139]. La revue de gouvernance émergente cartographie ce front sans l'arbitrer, et qualifie elle-même son évaluation de préliminaire [145].

Le second est plus grave : c'est un désaccord de prémisse factuelle. La littérature juridique légifère sur des agents déployés à l'échelle, planifiant et exécutant des chaînes d'actions avec implication humaine réduite [138], [139], [140]. Les pièces empiriques documentent l'inverse : autonomie opérationnelle marginale en santé [147] ; en génie logiciel, une erreur de calibration de 43 points entre vitesse anticipée et ralentissement mesuré, et des gains quasi nuls en documentation clinique [148]. Les deux camps ne se citent pas, et ils ne sont pas arbitrables entre eux : la doctrine établit par interprétation de textes et cohérence, la mesure d'effet par entretiens codés ou observation. Une doctrine n'est pas réfutée par vingt entretiens, ni une mesure par une exégèse. La revue enregistre l'écart plutôt qu'elle ne le tranche.

La pièce sectorielle du corpus, du côté de la finance quantitative, a été révisée le 10 août 2026, et sa révision est instructive au-delà de son contenu : le texte double de volume et **sépare désormais explicitement ses deux régimes de preuve** — deux illustrations synthétiques calibrées, dont le moniteur de dérive à covariance de regret et la simulation d'encombrement portant le risque de perte conjointe de 39,2 % à 79,3 %, et trois cas réels documentés, dont un jugement de tribunal tenant un transporteur aérien responsable de son agent conversationnel [146]. Ce que la première version présentait comme un instrument détectant la dérive à partir des seules données observées est requalifié par ses auteurs en démonstration de calculabilité. Son chiffre d'accroche, lui, reste nu au résumé des deux versions : **88 % des professionnels de la finance interrogés déclarent n'avoir aucun cadre de gouvernance opérationnel pour l'IA agentique** [146]. La qualification de ce chiffre ne se lit qu'au corps de la deuxième version — sondage informel sur un réseau professionnel, mai 2026, échantillon auto-sélectionné dont les auteurs reconnaissent le biais, section 3.1 du rendu HTML consulté le 15 août 2026 — et **elle n'est vérifiable ni à la notice ni au résumé**. *La mise en garde de cette revue tient donc toujours : un chiffre que son propre auteur qualifie à l'intérieur du texte reste, pour qui ne lit que la notice, un chiffre non qualifié.* Le cas du transporteur aérien est par ailleurs le seul jugement rendu que le corpus rapporte à l'appui de la ligne délictuelle [140], [141], [142] — rapporté de seconde main, dans une pièce d'ingénierie financière, et non analysé par une pièce de droit.

## Ce que la littérature ne traite pas

L'écart entre ce que le droit exige et ce que les protocoles savent exprimer est nommé, jamais instrumenté. Aucune pièce ne confronte les champs d'un message de protocole aux éléments exigés par les articles 12, 14 et 26 du règlement européen. La cartographie juridique raisonne sur des catégories de déploiement et des flux de données, pas sur des schémas de messages [138] ; la mesure d'auditabilité porte sur des dépôts logiciels, pas sur la capacité d'un format d'échange à porter une identité de mandant, une portée d'autorisation ou un point d'intervention [113] ; le relevé recense des systèmes, pas des formats [144] ; le cadre délictuel fait du journal le pivot probatoire sans spécifier ce qu'il doit contenir pour tenir devant un tribunal [140] ; la mesure de rejouabilité porte sur les commandes d'un point d'accès, pas sur les champs d'un message [191]. La proposition « dérive intraçable donc non-conformité » est donc énoncée comme constat normatif alors qu'elle est une hypothèse testable. Lacune connexe : toutes ces pièces supposent un mandant unique identifiable et aucune ne traite l'attribution lorsque la chaîne d'actions traverse plusieurs entités.

# Le Web agentique et l'horizon

Ce front compte quatre mesures, dont deux arbitrées, trois propositions d'architecture, trois positions, et aucune simulation. Le registre est indiqué pour chaque énoncé, faute de quoi une proposition y prendrait le ton d'un résultat.

## Ce qui est établi

*Position et architectures.* Le Web humain est tenu pour une interface inadaptée aux clients agentiques, et le remède est partout le même : un canal déclaratif servi par le site. Une architecture propose un domaine à double couche servant contenu humain et contenu optimisé pour agents, avec un successeur déclaré de `robots.txt` gradué par intention [149] ; une autre expose les capacités du site par des balises `<tool>` et `<context>`, avec pour seule évidence la faisabilité de construction établie sur seize développeurs [150]. Convergence de propositions, non de résultats.

*Mesure, des deux côtés.* Les mécanismes de consentement hérités ne contraignent pas les clients automatisés : la conformité au protocole d'exclusion décroît à mesure que la directive se durcit, et les moissonneurs de recherche par intelligence artificielle ne le consultent quasiment jamais [151] ; la détection commerciale déployée n'identifie qu'un des sept agents de navigation testés, là où les empreintes comportementales les séparent tous [152]. Deux voies indépendantes — journaux de sites contrôlés, site-appât instrumenté — pour l'énoncé le mieux étayé du front.

*Une mesure, deux positions.* L'écart entre capacité annoncée et capacité réalisée n'est mesuré qu'une fois : 102 agents commerciaux et 31 participants [158]. Les explications qui en sont données — l'échafaudage externe [157], le déficit d'auto-amélioration [153] — sont des positions.

## Où elle se contredit

L'autonomie est-elle une décision de conception certifiable, ou une propriété qui dérive ? *Position* : le niveau d'autonomie est un choix délibéré, séparable de la capacité et de l'environnement, et certifiable [155] ; *architecture* : il s'opérationnalise par inspection statique du code d'orchestration [156]. Or l'agent y est formalisé, ailleurs, comme un opérateur de mise à jour auto-induit dont les cibles licites sont les invites, la mémoire, les outils et la logique de contrôle — soit l'objet même de cette inspection, *position* [153] ; et un banc d'essai non répliqué mesure que cet échafaudage est la surface où une compromission devient permanente, *mesure* [154]. Un certificat établi au déploiement cesse alors d'être valide. Aucune des deux familles ne cite l'autre.

Corollaire, et point de bascule du front : l'identification coopérative postulée par les architectures [149], [150] — jusqu'à revendiquer une politique appliquée et non honorifique — est démentie par les deux mesures [151], [152] : une propriété d'application affirmée par conception, contredite par observation.

## Ce que la littérature ne traite pas

Aucune pièce ne définit un niveau d'autonomie invariant sous auto-modification, ni ne mesure la dérive d'autonomie après évolution. Les échelles fixent l'autonomie au déploiement [155], [156] ; la littérature auto-évolutive décrit et mesure des systèmes qui réécrivent leur propre échafaudage sans jamais rapporter le niveau d'autonomie résultant [153], [154]. Les deux portent sur le même objet, sans lien établi : la gouvernance par niveaux d'autonomie n'a aujourd'hui aucune garantie de tenir sur les systèmes que ce front annonce [40], [41], [46].

*La lacune se creuse plutôt qu'elle ne se comble. Contrôle refait à l'API du dépôt le 15 août 2026, sur le titre ou le résumé : du 9 au 15 août, **trente-cinq dépôts** portent « self-evolving », « self-improving » ou « self-evolution ». Quinze emploient les mots « autonome » ou « supervision », tous au sens du domaine — conduite autonome, évolution autonome du dispositif — ou de l'apprentissage — supervision de jetons, ajustement supervisé. **Aucun des trente-cinq ne rapporte un niveau d'autonomie, une certification ou une supervision humaine** ; le plus proche est un panorama qui pose la sûreté de processus évolutifs de plus en plus autonomes comme problème ouvert, sans en mesurer aucun. Six jours de production sur le sujet, et pas un énoncé raccordable aux échelles d'autonomie.*

# La chorégraphie et l'essaim

Le front des systèmes multi-agents mesurait des assemblages conduits ; celui-ci prend la question par l'autre bout — ce que la coordination achète et coûte quand aucun superviseur ne la tient, l'interaction n'étant réglée que par protocole. Aucune de ses seize pièces n'est publiée en comité de lecture — [162] et [172] annoncent une acceptation au seul champ de commentaire, [163] une simple soumission, et la pièce entrée à la reprise du 15 août ne porte aucun signe de revue [180].

## Ce que la littérature établit

**Aucune architecture n'est supérieure ; il y a un alignement architecture-tâche.** La seule comparaison contrôlée multi-bancs du front — 260 configurations, six bancs, cinq architectures, outils, invites et calcul normalisés — mesure un écart à l'agent unique de +80,8 % (raisonnement financier décomposable) à −70,0 % (planification séquentielle), et désigne la meilleure architecture dans 87 % des configurations hors ajustement [159].

**Ce que la suppression du chef achète est mesuré.** Contrôle et données sérialisés sur files distribuées : à matériel identique, sur trois scénarios de synthèse hétérogènes, le débit dépasse de 2 à 15× celui de cadres à orchestrateur central, sans écart de qualité chiffré [162]. Un contexte partagé vérifié plus une file où les agents réclament leurs sous-tâches : +10,5 points sur SWE-bench Verified à coût par tâche réduit de moitié [160] ; la vérification y est déplacée vers le substrat, non supprimée. Au tableau noir, des subordonnés volontaires gagnent 13 à 57 % en relatif sur trois bancs et lèvent l'exigence que le contrôleur connaisse d'avance les compétences de chacun [161] — c'est cette exigence qui interdit le parc d'agents hétérogène.

**Le plafond de l'essaim n'est pas topologique.** Une loi à deux paramètres, R² > 0,99 sur 44 cellules : trente agents en débat dense n'excèdent pas la diversité d'un seul sur MMLU-Hard, un placebo de bruit aléatoire suivant l'autocorrection à 4× l'échelle [166] — contre la loi logistique jusqu'au millier [96]. Deux mécanismes : par théorème, l'attention étroite borne l'échantillon effectif [167], plafonnant l'optimisation topologique [97] ; le plancher d'erreur tient au modèle interne de l'agent, un essaim plat égalant une hiérarchie à deux boucles à mémoire égale [168]. L'accord échoue d'abord par perte de vivacité, sans aucun agent byzantin [165]. Contrepoids : des milliers d'agents produisent 45 000 déclarations Lean 4 sous arbitre externe dur [169] ; le plafond frappe la délibération, non la décomposition vérifiable.

**La redondance d'un collectif est surcréditée dès que ses agents partagent un modèle.** Le calcul usuel de fiabilité composée multiplie les fiabilités des composants, geste qu'autorise une hypothèse d'indépendance conditionnelle rarement testée. Elle l'est ici : dans un relais à deux agents, deux instances d'un même modèle échouent ensemble sur 90,0 % des missions où l'une échoue (rapport de cotes logarithmique 6,66 ; φ = 0,916), sur 18 000 missions notées par code déterministe sans juge automatique ; changer de modèle réduit l'association dans six contrastes sur six, changer de fournisseur à modèle déjà différent ne la réduit pas — hypothèse enregistrée d'avance, rapportée comme nulle [180]. **L'erreur est signée et joue contre l'exploitant :** la dépendance positive gonfle l'échec conjoint au-dessus du produit des fiabilités, de sorte que le certificat crédite la redondance exactement là où elle n'existe pas. Régime : **prépublication non révisée par les pairs**, banc des auteurs, non répliquée, mais préenregistrée et à notation déterministe. *La pièce propose par ailleurs son propre certificat — un programme linéaire dont l'enrichissement de dix à quatorze fonctionnelles de moments resserre l'intervalle identifié de 85,7 % et relève le plancher certifié de 0,2455 à 0,4116 : pour cette moitié-là, elle évalue sa propre construction, et c'est le test de l'hypothèse, non le certificat, qui est repris ici.*

**La décentralisation ouvre une surface propre** : une attaque exploitant la délégation inter-agents, inerte contre l'agent unique, compromet la multi-agents à 80 % en moyenne chez trois modèles sur quatre, à un taux de détection de 0 % [170]. Vérifier le protocole aide sans suffire : en ablation appariée à runtime fixe sur 3 456 essais, les protocoles vérifiés par TLC font tomber le taux d'interblocage et de blocage vivant de 31,1 % à 14,1 %, écart maximal sous injection de fautes [171]. La collusion sort du marché [119], [120], [121] : mesurée en actions par le regret à l'optimum coopératif, elle diverge de la collusion en communication — planifiée en texte, souvent non posée en actes [173].

## Où elle se contredit

Le désaccord dur porte sur le mot « chorégraphie » lui-même. Une preuve de correction par construction pour sagas décentralisées pose ses conditions en résultat : participants **déterministes**, transactions idempotentes, messages en file durable, code compilé en sidecars [163]. Un agent fondé sur un modèle de langue ne satisfait pas la première ; [160], [161] et [162] revendiquent le mot sans discuter la condition. Les deux ne tiennent pas ensemble : ou la correction exige un participant déterministe, et le chorégraphié est le sidecar, l'agent confiné à la proposition — comme à la frontière de règlement [126] et sous contrôleur DCR [137] ; ou elle tolère un participant stochastique, et la preuve tombe. L'arbitre est disponible, non produit : personne ne mesure le taux de reprise sur panne d'une saga à participants agents contre celui d'un orchestrateur dont l'état local est source unique de vérité [163].

Second désaccord : le lieu de la vérification. La régularité de [159] conclut à la vérification centralisée ; une preuve de (F+1)-robustesse sur le graphe établit l'inverse, chef et confiance auto-déclarée étant manipulables par un pair adverse [164]. Le point d'observation est lui-même borné : le rappel d'un moniteur à automate fini tombe de 68-75 % à 6-13 % quand les attaques passent à haute entropie, invariant au réentraînement [172] — mesure d'un auteur unique, sur huit dorsales. Or le moniteur d'exécution de [171], qui rejette les opérations hors topologie, relève exactement de cette classe d'automates finis, dont [172] démontre le plafond. Le compte des fautes tolérées est lui aussi en cause : une borne en F suppose des défaillances qu'on peut compter séparément, et la co-défaillance mesurée entre agents d'un même modèle interdit ce décompte [180].

## Ce qu'elle ne traite pas

Aucune pièce ne mesure un essaim réparti entre organisations distinctes : tout tient sous opérateur unique, la frontière organisationnelle simulée, non franchie. Manquent la comparaison en production, le coût d'exploitation sans orchestrateur — diagnostic, MTTR, débogage —, la conformité d'exécution sur traces déployées et l'imputation d'une défaillance. Performance et coût ne sont jamais croisés au-delà de trente agents : [166] y plafonne, [169] atteint le millier sans courbe de coût, le point de rentabilité restant non mesuré. Aucun comportement byzantin émergent n'est rapporté, la fraction étant injectée par construction et la propension de [173] répondant à la sonde ; la seule défaillance corrélée obtenue sans injection est celle du modèle partagé [180], qui n'est pas un comportement byzantin mais en produit l'effet sur le calcul de robustesse. Aucun protocole déclaratif ne tient de contrat d'exécution entre agents hétérogènes à conformité mesurée : le modèle y est générateur, jamais participant contraint [61].

# Ce que la littérature établit, et où elle se contredit

## Un défaut de fond unique, décliné en trois matières

Les dix fronts convergent sur un énoncé qu'aucun ne porte seul : **rien, dans les piles examinées, ne sépare ce qui est autorisé de ce qui est seulement présent.** *Contenu :* rien n'isole donnée de confiance et donnée non fiable [64] [66] [68], rien ne lie une description d'outil à son code — 9,93 % de paires divergentes sur parc réel [55], 97,1 % de descriptions défectueuses [53], 37,2 % d'applications à approbation bloquante [54]. *Autorité :* le jeton porteur transmis intact est le mauvais primitif, elle doit s'atténuer à chaque saut [83], se rétrécir sous vérification mécanique [76], se fermer à l'achèvement de la tâche [87] — or 40,55 % des serveurs MCP distants n'authentifient rien [81], et, dans une famille de scénarios de blanchiment appariés, un garde qui lit l'autorité dans l'état local admet des violations dans 22 épisodes sur 96 là où l'application par provenance n'en admet aucune, ses échecs se concentrant là où une transformation ordinaire change la politique visible alors que l'autorité d'origine, elle, n'a pas bougé [192]. *Effet :* la sortie du modèle vaut fait accompli là où elle n'est qu'une proposition — d'où la frontière de règlement déplacée hors du retour d'outil [126], le contrôle d'admission rendant l'état engagé indépendant du proposant [127].

Le dixième front n'y entre qu'à moitié. Sans chef, rien ne sépare le pair fiable du pair seulement présent : chef et confiance auto-déclarée sont manipulables par un pair adverse, quand la robustesse tient de la seule topologie [164] ; la délégation inter-agents devient la surface, inerte contre l'agent unique, une attaque compromettant la multi-agents à 80 %, détection 0 % [170]. L'autre moitié ne relève pas de l'autorisation : le plafond de l'essaim tient à la vivacité perdue [165], à l'attention qui borne l'échantillon effectif [166] [167], à la mémoire par agent [168], et la fiabilité qu'on croit gagner en dupliquant tient à une hypothèse d'indépendance que la mesure dément [180].

## L'instrument de mesure est le maillon faible

Trois fronts qui ne se citent pas y aboutissent. Les scanners MCP déclarent 96,89 % des serveurs à risque ; moins de la moitié des alertes sont des vrais positifs à la validation manuelle, et les scanners se contredisent [51]. Les bancs les plus employés comptent des réponses vides comme succès [107], la performance sur SWE-bench relève pour partie de la mémorisation [108], le juge automatique bute sur un plafond démontré [109]. L'attribution de défaillance n'identifie l'agent fautif que dans 53,5 % des cas, l'étape décisive dans 14,2 %, certaines méthodes faisant moins bien que le hasard [88] ; l'observabilité des entrées et du contexte améliore l'attribution jusqu'à 76 % contre une observation partielle [89] — gain relatif, sans effectif de banc ni condition nommée, sans dénominateur commun avec le 53,5 % : le plafond d'instrumentation est une hypothèse. **Un pourcentage y renseigne sur un dispositif autant que sur le monde.**

## Proposer n'est pas prouver

Sur les 123 pièces des dix fronts **[51-173]**, **67 — 54 % — rapportent la performance d'un artefact de leurs propres auteurs**. Maximum en sécurité (10/11) et en multi-agents (11/14, les exceptions étant exactement les pièces concluant au non-avantage) ; minimum en gouvernance (2/11) et en protocoles (4/13). **Ce corpus s'auto-arbitre à moitié** — l'énoncé porte sur les pièces lues, dont aucune n'a été retenue hors arXiv, et non sur le champ. *Le décompte porte sur cette plage et n'a pas été refait : les pièces entrées à la reprise du 15 août n'y sont pas comptées, et la répartition par front, elle, les compte.*

: Les dix désaccords réels du champ, un par front, avec ce qui les arbitrerait.

| Front | Désaccord | Ce qui l'arbitrerait |
|---|---|---|
| Protocoles | MCP suffit-il ? Oui [57] ; non, schéma prouvé à perte [56] ; prémisse récusée [63] | La même tâche, deux protocoles, un tiers |
| Sécurité | Prévention par construction : utilité préservée [74] ou payée cher [72] [70] | [74] sous attaque adaptative [71], coût d'utilité publié |
| Identité | Ancrage matériel [86] contre opposabilité hors ligne [77] [80] | La part de parcs à racine d'attestation |
| Multi-agents | Marge réelle [96] [97] contre non-avantage à dix fois le prix [94] [95] [92] | Réglage égalisé sur les deux bras [93] |
| Évaluation | Juge automatique : quasi humain [110] ou plafond démontré [109] | Un juge indépendant, étiquettes humaines |
| Transactionnel | Collusion stable sous auto-optimisation [121] ou artefact d'homogénéité [120] | La population de modèles tarificateurs |
| Processus | Suspendre l'effet jusqu'à certitude [126] [127] ou l'émettre et le réviser [129] | La part d'actions irréversibles en flux réel |
| Gouvernance | RIA opérationnalisable [138] ou inadéquat [139] ; prémisse d'autonomie contestée [147] [148] | Un message contre les articles 12, 14 et 26 |
| Web agentique | Identification coopérative [149] [150] ou détection imposée [151] [152] | La conformité d'agents non coopératifs |
| Chorégraphie et essaim | Vérifier au centre [159], ou sans chef, la (F+1)-robustesse tenant du graphe quand chef et confiance auto-déclarée se manipulent [164] ; or la correction chorégraphiée exige un participant déterministe [163], et le décompte des fautes suppose une indépendance démentie [180] | La même saga, participants déterministes puis agents, sous injection de fautes [171] |

# Trois énoncés de la veille mis à l'épreuve

Ces trois énoncés proviennent d'une veille sur sources primaires — brouillons de normalisation, moteurs d'orchestration, conventions d'observabilité — arrêtée au 8 août 2026. La littérature ne peut ni les confirmer ni les infirmer en bloc : elle en éclaire une part et laisse l'autre à la veille. Chaque verdict est donc écrit en deux temps, **ce que la littérature porte seule** et **ce qui reste suspendu à l'état du monde déployé**, de sorte qu'un mouvement de ce dernier depuis le gel déplace la date d'un fait, jamais la conclusion.

## 1. « Au-delà de deux sauts de délégation, aucun mécanisme normalisé ne maintient de traçabilité opposable. »

**Proposer est dépassé.** Chaîne append-only, *chaque* saut signé, vérifiable hors ligne à la seule clé publique de l'émetteur, sans borne de profondeur [77] ; jetons de capacité liés à l'invocation [16]. « Aucun mécanisme » est faux.

**Prouver est partagé.** Une vérification en TLA+ sur 2,7 M d'états établit, à profondeur arbitraire, rétrécissement d'autorité, reconstructibilité forensique et confinement de cascade, mais démontre la préservation d'intention *pratiquement infaisable* de façon déterministe [76] ; ni l'atténuation récursive [83] ni la borne de propagation de responsabilité [78] ne déplacent ce partage. **On prouve ce qui fut fait sous quelle autorité, non que cela servait le mandat.**

**Normaliser ne tient pas.** La vérification formelle des spécifications relève 35 lacunes et 30 défaillances nées de la seule composition, et qu'*aucun protocole n'assigne l'application inter-protocoles* [85] — or deux sauts en entreprise traversent des protocoles, et le socle à un saut n'est pas tenu [81]. **L'obstacle est de normalisation et d'instrumentation, non d'invention.**

*Ce que la littérature porte seule, et qui ne dépend d'aucun brouillon :* les mécanismes existent et sont publiés ; leurs preuves s'arrêtent avant l'intention ; et **aucune pièce du corpus ne mesure une chaîne de délégation à plus d'un saut en exploitation** — la seule mesure de parc du front porte sur l'authentification d'un saut, et elle échoue [81]. Le déficit d'adoption est donc établi par l'absence de mesure autant que par les mesures existantes.

*Ce qui reste à la veille :* le mot « normalisé » lui-même. Qu'un brouillon de délégation ait avancé, stagné ou été adopté depuis le 8 août ne change ni le constat d'invention ni l'absence de mesure de terrain — cela date le franchissement d'une étape de procédure, et cette étape est de la compétence de la veille, non de la littérature. Le verdict tient dans les deux cas ; seul son temps de verbe change.

## 2. « L'arrimage entre la couche d'orchestration installée et la pile agentique est unilatéral. »

**Exact sur le déploiement, faux sur la littérature.** Le mouvement dominant enveloppe le moteur déterministe, qui garde l'autorité d'exécution [132]. Mais quatre formalismes conçus *pour* les agents existent depuis fin 2024 : BPMN à constructions natives d'agent [133], graphe DCR pilotant le dialogue [137], portes d'approbation érigées en invariants applicables [134], modèles de processus typés promus composants de l'agent [131]. **Ce qui manque est l'adoption : la dissymétrie est industrielle, pas scientifique.**

*Ce que la littérature porte seule :* l'existence datée des quatre formalismes, et l'absence complète de mesure de leur adoption ou de leur conformité d'exécution — [130] produit le journal et s'arrête à la découverte, [131] pose la conformité par construction comme agenda, [136] évalue le modèle produit et non l'exécution. **La littérature ne sait pas si la dissymétrie se referme, et elle ne s'est pas donné les moyens de le savoir.**

*Ce qui reste à la veille :* deux faits, non un. D'abord la négative « aucun protocole déployé ne porte de sémantique de processus » — **elle relève du relevé de spécifications de la veille, non de la littérature** : [132] décrit un harnais autour d'un moteur, il n'établit aucune négative universelle, et aucune pièce du corpus ne recense les protocoles déployés sous cet angle. Ensuite l'état des moteurs installés : si l'un d'eux a publié depuis le gel des primitives agentiques natives, la dissymétrie se referme du côté industriel, ce qui confirme le verdict au lieu de l'infirmer, puisque le verdict porte précisément sur le fait que le mouvement vient de l'industrie et non de la science. L'énoncé ne serait renversé que par une pièce mesurant l'adoption d'un formalisme agentique par un moteur de production ; le corpus n'en contient aucune au 15 août 2026.

## 3. « Aucun attribut du socle d'observabilité agentique ne décrit une chaîne de mandat ou de délégation. »

**Confirmé par une seconde voie, plus sévèrement.** Journaux d'audit, OCSF et OpenTelemetry sont sémantiquement insuffisants pour reconstruire la propagation d'autorité : des traces identiques admettent plusieurs assignations de mandat incompatibles, donc l'exécution déléguée n'est pas *identifiable* [84]. La seule pièce arbitrée du front étend la provenance W3C aux flux agentiques **sans jamais instancier `actedOnBehalfOf`** : elle s'en tient à `wasAssociatedWith` et `wasInformedBy` [112]. *Le modèle le plus normatif renonce à la primitive de son standard.*

*Ce que la littérature porte seule — et il faut en donner le cadre exact, sans quoi la mesure dirait plus qu'elle n'établit.* Une suite gelée de 5 280 épisodes met deux dispositifs à l'épreuve. Sur son **expérience de délégation pré-spécifiée**, à quatre familles de modèles, une invite constitutionnelle détaillée produit 0 violation réalisée sur 384 — et le garde exécutable à provenance produit lui aussi 0 sur 384, en bloquant au passage 51 tentatives sur 384, dont 44 aboutissent quand même ensuite [192]. **Sur le critère de sortie, une invite égale une application par provenance.** Les deux ne se séparent que dans une famille de scénarios ciblés : en **scénarios de blanchiment appariés**, le garde qui lit l'autorité dans l'état local admet des violations dans 22 épisodes sur 96, l'application par provenance dans 0 sur 96 (p = 4,77 × 10⁻⁷), et ses échecs se concentrent là où une transformation ordinaire change la politique visible alors que l'autorité d'origine reste fixe [192]. Régime : **prépublication non révisée par les pairs**, auteur unique, dépôt de reproductibilité public, non répliquée.

**Ce que cette mesure établit, et ce qu'elle n'établit pas.** Elle n'établit pas qu'une chaîne de mandat portée à la trace fasse baisser un taux de violation : sur l'expérience principale, elle ne le fait pas. Elle établit deux choses que cette revue tient pour plus importantes. D'abord que **le taux de violation final ne distingue pas les deux mécanismes** — la pièce le dit elle-même : un même taux final peut recouvrir des mécanismes très différents —, de sorte qu'un banc qui mesure la sortie ne peut pas dire si le mandat a été suivi ; c'est la non-identifiabilité de [84] déplacée de la trace vers l'évaluation. Ensuite que l'écart apparaît exactement là où l'énoncé le prédit : quand la politique visible change sans que l'autorité d'origine bouge. **Le verdict reste donc une position appuyée par une mesure de portée étroite, non un fait mesuré de portée générale** — et il faut le dire ainsi, puisque cette revue reproche ailleurs au champ de citer ses pourcentages hors de leur dispositif.

**Le déficit est de liaison, non de vocabulaire** — et c'est la formulation qui tient quel que soit l'état du socle. La primitive existe déjà dans le standard de provenance et n'est pas instanciée [112] ; là où l'autorité n'est pas liée à son origine, la trace reste non identifiable [84] ; et un garde qui la lit ailleurs qu'à l'origine échoue là où la politique visible se transforme [192]. **Qu'un attribut de délégation soit ajouté demain à une convention sémantique ne réfuterait pas cet énoncé** : un nom d'attribut que rien n'oblige à émettre, et que rien ne lie à un mandat vérifiable, laisse la trace exactement aussi ambiguë. L'arbitrage porte sur l'émission et la liaison, pas sur la nomenclature.

*Ce qui reste à la veille :* la liste des attributs effectivement publiés, et leur date. Ce fait est porté par elle seule ; cette revue ne le vérifie pas et ne s'y adosse pas.

# Lacunes et programme de recherche

**Il n'existe aucun taux de base.** Aucun front ne compte ses échantillons autrement qu'en serveurs, en outils, en cas de test, en dépôts et en marchés simulés — **jamais en organisations, en déploiements ni en incidents observés**. Testable : quelle fraction des agents en service subit une tentative d'injection, à quel taux d'aboutissement ? Quel taux de contestation pour une transaction agentique non autorisée, dont le front transactionnel n'offre aucune pièce pour l'établir [114] [115] ?

**Personne ne mesure une propriété de bout en bout franchissant une frontière réelle.** Ni de protocole à protocole — tout est mesuré sur MCP seul, la seule comparaison implémentée est un scénario unique non généralisable de l'aveu des auteurs [57], les 30 propriétés temporelles unifiant MCP et A2A ne sont vérifiées nulle part [60] — ni d'organisation à organisation. Testable : pour une tâche A2A → MCP entre deux organisations en exploitation, quels taux d'échec, latence ajoutée et perte sémantique ? Et quels *fitness* et précision pour une trace d'agent alignée contre un modèle de processus [130] [136] ?

# Limites de cette revue

Aux restrictions de méthode déjà posées — ni protocole PRISMA, ni double codage, ni réplication — s'ajoute celle de la couverture : l'interrogation porte sur arXiv, notices vérifiées une à une, et ACM DL, IEEE Xplore, SpringerLink et la littérature grise restent hors du corpus — à l'exception de la passe de contrôle décrite ci-dessous, qui les interroge pour mesurer ce que cette restriction coûte, sans rien verser au corpus. Le biais anglophone reste entier. Les chiffres rapportés sont ceux des auteurs, y compris là où la revue signale que l'instrument qui les produit est contesté. Le classement d'un artefact comme « construction des auteurs » relève d'un jugement de lecture ; son critère est publié pour être réfutable. La revue hérite enfin de la faiblesse qu'elle mesure : **77 % de son corpus ne présente aucun signe de revue par les pairs** et 63 % a été déposé en 2026 — proportions recomptées sur la bibliographie à la reprise du 15 août 2026 : la première est inchangée au point de pourcentage près, la seconde monte de trois points, les seize pièces versées ce jour-là étant toutes de 2026.

**Le biais d'échantillonnage a été mesuré, non déclaré.** Mesurer la part de non-arbitré sur un dépôt de prépublications, puis en conclure quelque chose du champ, serait circulaire. Une passe de contrôle a donc été conduite le 15 août 2026 sur DBLP, Crossref et OpenAlex, aux quatre fronts que l'annexe donne pour vides de pièce arbitrée et qui sont les plus réfutables — sécurité, évaluation, couche transactionnelle, chorégraphie et essaim —, avec la consigne inverse de celle du corpus : chercher ce qui réfute le résultat central. **Elle en trouve, sur les quatre.** Sécurité : l'injection d'invite est arbitrée à IEEE S&P 2026 (*PromptLocate*), à ESORICS 2025 (*Prompt Infection*, injection de modèle à modèle en système multi-agents), à CODASPY 2025 (*PromptShield*), dans *IEEE Transactions on Information Forensics and Security* 2026 et dans *ICT Express* 2026, cette dernière sur les exploits de protocole eux-mêmes. Évaluation : ICLR 2025 porte *AgentHarm* et *Agent Security Bench*, NeurIPS 2025 *AgentRecBench*, AIware 2026 un banc de détection de fautes pour l'observabilité d'agents. Couche transactionnelle : la collusion algorithmique est arbitrée à ITCS 2025, à ACM CS&Law 2024 et 2025, dans *Games and Economic Behavior* 157 et dans l'*European Journal of Operational Research* 318. ⚠ **Ce rattachement est le plus faible des quatre, et il faut le dire** : ces cinq pièces relèvent de l'économie industrielle et portent toutes sur la tarification collusoire ; *elles n'établissent rien sur les paiements agentiques ni sur la réputation*, qui sont les deux autres tiers de ce front. Le front n'est donc pas couvert par une littérature arbitrée — **un de ses trois objets l'est**. Chorégraphie et essaim : la coordination multi-agents robuste aux fautes byzantines est arbitrée à l'ACM TURC 2024 (*BlockAgents*) et à IEEE CSCWD 2026 (*RoMa*). Aucune de ces pièces n'est au corpus et aucune n'y est versée ici. **L'énoncé « aucune publication arbitrée sur ce front » est donc vrai du corpus retenu et faux du champ.**

**La notice sous-déclare l'arbitrage, et l'écart a été chiffré.** Le critère de cette revue — attestation portée au champ `journal_ref` ou DOI — ne relève un arbitrage que si l'auteur a mis sa notice à jour après acceptation. Sept pièces dont DBLP ou Crossref établit la publication en actes ou en revue ont été confrontées à leur notice arXiv : une seule y porte l'attestation, deux ne la déclarent qu'au champ de commentaire, **quatre ne portent rien du tout** et tomberaient donc au régime sans revue. Le même test, refait sur ce corpus-ci — sept entrées classées sans revue dont l'identifiant arXiv est antérieur au gel —, **en donne quatre publiées** : [92] aux actes de l'ACL 2024, [102] et [107] à NeurIPS 2025, [124] aux actes de l'ACM Web Conference 2026 ; les trois autres n'ont pas de version arbitrée trouvable. Le contrôle est un plancher, non une mesure : Crossref n'indexe ni PMLR ni OpenReview, de sorte qu'aucune acceptation à ICML ou à ICLR n'y apparaît, et l'échantillon de quatorze pièces penche vers deux fronts. **Conséquence pour le résultat central : 145 est un plafond du non-arbitré et douze un plancher de l'arbitré ; les trois régimes mesurent ce que les notices déclarent, non ce que les comités ont fait.** Ce qui reste établi est plus étroit et plus sûr que ce que le chiffre laissait croire : sur les questions d'interopérabilité que cette revue instruit, le régime de chaque pièce citée est nommé une à une, et c'est cette nomination-là, non la proportion, qui porte l'argument.

**La date de validité est celle de la reprise, pas celle de la lecture.** Les notices ont été reprises à l'API du dépôt le 15 août 2026 : deux avaient été révisées en six jours, aucune publication neuve n'était attestée, et rien ne garantit qu'aucune ne bougera demain. Une révision peut changer un résultat sans changer un titre — la pièce sectorielle de gouvernance en donne l'exemple dans cette même reprise [146]. **La notice ne dit pas tout non plus** : la qualification du chiffre d'accroche de cette même pièce ne se lit qu'à son corps, et un lecteur qui s'arrêterait au résumé, comme le fait cette revue pour la plupart de ses entrées, ne la verrait pas.

Auto-citation déclarée : la veille dont trois énoncés sont ici mis à l'épreuve est du même auteur. Quatre faits qu'elle porte seule — l'état des brouillons de normalisation de la délégation, l'absence de sémantique de processus dans les protocoles déployés, l'état des moteurs d'orchestration installés, les attributs publiés des conventions d'observabilité — ne sont pas vérifiés par cette revue. *Ils sont nommés comme siens à l'endroit où ils comptent, et aucun verdict de la section précédente n'y est suspendu.*

# Conclusion

Le meilleur résultat de cette revue n'est pas un fait du champ, mais une propriété du corpus qu'elle a lu. Un corpus dont les trois quarts ne déclarent aucun comité à leur notice, dont la moitié évalue une construction de ses propres auteurs, et dont trois fronts indépendants concluent que l'instrument de mesure est faux, ne peut pas à lui seul arbitrer une décision d'architecture. **La passe de contrôle sur DBLP et Crossref, rapportée aux limites, borne ce constat dans les deux sens** : de la littérature arbitrée existe hors arXiv sur quatre des fronts que ce corpus donne pour vides, et des pièces de ce corpus sont publiées sans que leur notice le dise. Les 77 % restent le fait qu'ils mesurent — un corpus de prépublications lu au critère de la notice — et cessent d'être ce qu'on aurait voulu leur faire dire du champ. Ce corpus peut seulement dire où regarder — et sur les trois énoncés soumis, elle l'a fait : deux déficits d'invention étaient des déficits d'adoption ; le troisième est plus profond qu'annoncé, mais la mesure qui l'appuie ne vaut que pour la famille de scénarios où elle a été prise [192], et la revue le dit plutôt que de l'élargir.

**Le corpus a été repris notice par notice le 15 août 2026, six jours après le premier relevé.** Deux notices seulement avaient bougé, dont une du front gouvernance, qui requalifie en démonstration de calculabilité ce qu'elle présentait comme un instrument de détection de dérive [146] ; aucune publication neuve n'est attestée ; et les trois pièces que la fenêtre du 9 au 15 août fait entrer aux fronts de la gouvernance et de l'essaim sont toutes des prépublications sans signe de revue [180], [191], [192]. *Une reprise qui change peu est un résultat : elle mesure la vitesse à laquelle ce corpus se périme, et cette vitesse se compte en semaines, pas en jours.* C'est aussi la seule garantie qu'un lecteur peut exiger d'une revue sur un champ pareil — non qu'elle soit complète, mais qu'elle dise à quelle date chacun de ses énoncés a été rouvert, ce qu'elle n'a pas pu rouvrir, et jusqu'où porte chaque chiffre qu'elle cite.

# Annexe : le corpus arbitré, et ce qu'il ne couvre pas {-}

Un lecteur qui refuserait de s'appuyer sur autre chose qu'une publication attestée en notice
disposerait des douze pièces ci-dessous, et de rien d'autre dans ce corpus, relevé du 15 août 2026. Sept d'entre elles portent une
référence de revue ou d'actes au champ `journal_ref` — dont quatre portent aussi un DOI d'éditeur —
et cinq ne sont attestées que par un DOI ; le tableau est ordonné par numéro de référence, non par
champ. **La liste est inchangée depuis le relevé du 9 août** : en une semaine, aucune pièce n'y est
entrée, aucune n'en est sortie, et les seize arrivées au corpus n'en approchent pas.

: Les douze pièces du corpus dont la publication est attestée en notice, avec leur apport propre.

| Réf. | Publication attestée | Apport |
|---|---|---|
| [4] | *IEEE Trans. on Cognitive Communications and Networking* | Pose l'« Internet des agents » comme objet d'architecture et en énumère les couches manquantes |
| [15] | ICAART 2026 | Applique identifiants décentralisés et justificatifs vérifiables du W3C à des agents |
| [37] | *Künstliche Intelligenz*, 2024 | Formule la vision des grands modèles de processus, d'où descend le front des processus d'affaires |
| [38] | Actes PMAI 25 (CEUR, vol. 4087) | Découvre la variabilité comportementale d'agents par fouille de processus sur leurs traces |
| [44] | Actes FAccT 2026 | Établit que les agents de langue n'ont pas l'ancrage requis par un mécanisme de réputation |
| [46] | Actes ICML 2024 | Propose l'échelle d'autonomie la plus citée du champ, et la seule opérationnalisable |
| [59] | Actes MSR '26 | Constitue le seul jeu de données validé d'implémentations MCP — 2 297 dépôts, précision de 83 % |
| [136] | *Information Systems*, vol. 142, art. 102761 | Mesure la compétence réelle des modèles à produire des modèles de processus valides |
| [142] | Actes REALM @ ACL 2025 | Instruit la responsabilité par la relation de mandat, et non par l'autonomie du système |
| [143] | *European Journal of Risk Regulation* 16 | Établit que le règlement européen alloue une responsabilité de supervision sans base empirique |
| [144] | Actes FAccT 2026 | Documente les caractéristiques techniques et de sûreté d'agents effectivement déployés |
| [158] | Actes ACM, 2026 | Mesure l'écart entre capacité annoncée et capacité réalisée — 102 agents, 31 participants |

**Ce que cette liste montre par ce qui n'y figure pas.** **Six fronts neufs n'y comptent aucune
pièce** — la sécurité, l'identité et la délégation, les systèmes multi-agents, l'évaluation, la
couche transactionnelle, la chorégraphie et l'essaim. Or ce sont exactement ceux qui portent les
énoncés les plus conséquents de cette revue : que les scores de défense ne survivent pas à
l'adversaire adaptatif, que l'autorité doive s'atténuer à chaque saut, que le rendement du
multi-agent soit non monotone, que le score publié ne soit pas ce qui s'observe, que le mandat signé
ne soit pas le point de rupture, que la coordination sans chef échange une surface d'attaque
contre une autre. *Aucun de ces six résultats ne repose, dans ce corpus et au seul critère de la
notice, sur une pièce dont la publication soit attestée.*

**L'énoncé porte sur ce corpus, et une passe de contrôle le réfute au niveau du champ.** DBLP et
Crossref donnent de la littérature arbitrée sur quatre de ces six fronts — les limites la nomment —,
et **quatre** pièces déjà retenues ici sont publiées en actes sans que leur notice le déclare : [92] en
multi-agents, [102] et [107] en évaluation, [124] à la couche transactionnelle. Le tableau ci-dessus recense
donc ce que les notices attestent, non ce que les comités ont arbitré, et le vide de ces six fronts
est un vide de déclaration autant qu'un vide de revue.

Il ne s'ensuit pas que ces résultats soient faux : plusieurs sont adossés à des mesures que rien
d'autre ne fournit. Il s'ensuit que **ce corpus produit ses résultats les plus décisifs là où son
appareil de contrôle déclaré est le plus faible**, et qu'un architecte qui s'y appuie le fait sous
sa propre responsabilité — constat qui ne se lit ni dans les résumés ni dans les comptes de
citations : il fallait ouvrir les cent quatre-vingt-neuf notices pour l'obtenir, deux fois plutôt
qu'une, puis sortir d'arXiv pour en connaître la portée.

# Références {-}

*Chaque entrée porte le régime de publication relevé sur la notice du dépôt le 15 août 2026 : la
référence de revue ou d'actes lorsqu'elle y figure, la mention d'une acceptation autodéclarée au seul
champ de commentaire lorsqu'il n'y a que cela, et la qualification de prépublication non révisée par
les pairs à défaut. Cette dernière mention enregistre le silence de la notice, non l'absence
d'arbitrage : les limites de cette revue chiffrent l'écart entre les deux, et nomment quatre entrées
ainsi qualifiées dont une base de littérature arbitrée établit la publication.*

::: {#refs}
1. Abul Ehtesham, Aditi Singh *et al.*. « A survey of agent interoperability protocols: Model Context Protocol (MCP), Agent Communication Protocol (ACP), Agent-to-Agent Protocol (A2A), and Agent Network Protocol (ANP) ». [arXiv:2505.02279v2](https://arxiv.org/abs/2505.02279), déposée le 4 mai 2025, v2 du 23 mai 2025 — **prépublication non révisée par les pairs**.
2. Yingxuan Yang, Huacan Chai *et al.*. « A Survey of AI Agent Protocols ». [arXiv:2504.16736v3](https://arxiv.org/abs/2504.16736), déposée le 23 avril 2025, v3 du 21 juin 2025 — **prépublication non révisée par les pairs**.
3. Dezhang Kong, Shi Lin *et al.*. « A Survey of LLM-Driven AI Agent Communication: Protocols, Security Risks, and Defense Countermeasures ». [arXiv:2506.19676v4](https://arxiv.org/abs/2506.19676), déposée le 24 juin 2025, v4 du 27 novembre 2025 — **prépublication non révisée par les pairs**.
4. Yuntao Wang, Shaolong Guo *et al.*. « Internet of Agents: Fundamentals, Applications, and Challenges ». [arXiv:2505.07176v2](https://arxiv.org/abs/2505.07176), déposée le 12 mai 2025, v2 du 16 octobre 2025 — **publication attestée en notice**, doi:10.1109/TCCN.2025.3623369.
5. Xinyi Hou, Yanjie Zhao *et al.*. « Model Context Protocol (MCP): Landscape, Security Threats, and Future Research Directions ». [arXiv:2503.23278v3](https://arxiv.org/abs/2503.23278), déposée le 30 mars 2025, v3 du 7 octobre 2025 — **prépublication non révisée par les pairs**.
6. Mohammed Mehedi Hasan, Hao Li *et al.*. « Model Context Protocol (MCP) at First Glance: Studying the Security and Maintainability of MCP Servers ». [arXiv:2506.13538v5](https://arxiv.org/abs/2506.13538), déposée le 16 juin 2025, v5 du 13 avril 2026 — **prépublication non révisée par les pairs**.
7. Xiaofan Li et Xing Gao. « A First Look at the Security Issues in the Model Context Protocol Ecosystem ». [arXiv:2510.16558v2](https://arxiv.org/abs/2510.16558), déposée le 18 octobre 2025, v2 du 27 avril 2026 — acceptation annoncée au seul champ *Comments* (« This paper has been accepted to DSN 2026. The title has »), non confirmée en notice.
8. Kehui Chen, Yicheng Sun *et al.*. « Understanding How Enterprises Adopt the Model Context Protocol for LLM-Driven Software Engineering ». [arXiv:2606.09182v1](https://arxiv.org/abs/2606.09182), déposée le 8 juin 2026 — acceptation annoncée au seul champ *Comments* (« 12pages, preliminary version accepted at the 26th Inter »), non confirmée en notice.
9. Idan Habler, Ken Huang *et al.*. « Building A Secure Agentic AI Application Leveraging A2A Protocol ». [arXiv:2504.16902v2](https://arxiv.org/abs/2504.16902), déposée le 23 avril 2025, v2 du 2 mai 2025 — **prépublication non révisée par les pairs**.
10. Gaowei Chang, Eidan Lin *et al.*. « Agent Network Protocol Technical White Paper ». [arXiv:2508.00007v1](https://arxiv.org/abs/2508.00007), déposée le 18 juillet 2025 — **prépublication non révisée par les pairs**.
11. Zeynab Anbiaee, Mahdi Rabbani *et al.*. « Security Threat Modeling for Emerging AI-Agent Protocols: A Comparative Analysis of MCP, A2A, Agora, and ANP ». [arXiv:2602.11327v2](https://arxiv.org/abs/2602.11327), déposée le 11 février 2026, v2 du 17 avril 2026 — **prépublication non révisée par les pairs**.
12. Ken Huang, Vineeth Sai Narajala *et al.*. « A Novel Zero-Trust Identity Framework for Agentic AI: Decentralized Authentication and Fine-Grained Access Control ». [arXiv:2505.19301v2](https://arxiv.org/abs/2505.19301), déposée le 25 mai 2025, v2 du 28 mai 2025 — **prépublication non révisée par les pairs**.
13. Subramanya Nagabhushanaradhya. « OpenID Connect for Agents (OIDC-A) 1.0: A Standard Extension for LLM-Based Agent Identity and Authorization ». [arXiv:2509.25974v1](https://arxiv.org/abs/2509.25974), déposée le 30 septembre 2025 — **prépublication non révisée par les pairs**.
14. Abhishek Goswami. « Agentic JWT: A Secure Delegation Protocol for Autonomous AI Agents ». [arXiv:2509.13597v1](https://arxiv.org/abs/2509.13597), déposée le 16 septembre 2025 — **prépublication non révisée par les pairs**.
15. Sandro Rodriguez Garzon, Awid Vaziry *et al.*. « AI Agents with Decentralized Identifiers and Verifiable Credentials ». [arXiv:2511.02841v2](https://arxiv.org/abs/2511.02841), déposée le 1 octobre 2025, v2 du 15 décembre 2025 — **18th International Conference on Agents and Artificial Intelligence (ICAART), 2026, volume 1, pp. 252-259**, doi:10.5220/0014234400004052.
16. Sunil Prakash. « AIP: Agent Identity Protocol for Verifiable Delegation Across MCP and A2A ». [arXiv:2603.24775v1](https://arxiv.org/abs/2603.24775), déposée le 25 mars 2026 — **prépublication non révisée par les pairs**.
17. Ken Huang, Vineeth Sai Narajala *et al.*. « Agent Name Service (ANS): A Universal Directory for Secure AI Agent Discovery and Interoperability ». [arXiv:2505.10609v1](https://arxiv.org/abs/2505.10609), déposée le 15 mai 2025 — **prépublication non révisée par les pairs**.
18. Kunlun Zhu, Hongyi Du *et al.*. « MultiAgentBench: Evaluating the Collaboration and Competition of LLM agents ». [arXiv:2503.01935v1](https://arxiv.org/abs/2503.01935), déposée le 3 mars 2025 — **prépublication non révisée par les pairs**.
19. Asaf Yehudai, Lilach Eden *et al.*. « Survey on Evaluation of LLM-based Agents ». [arXiv:2503.16416v2](https://arxiv.org/abs/2503.16416), déposée le 20 mars 2025, v2 du 23 avril 2026 — acceptation annoncée au seul champ *Comments* (« ACL Findings »), non confirmée en notice.
20. Shaina Raza, Ranjan Sapkota *et al.*. « TRiSM for Agentic AI: A Review of Trust, Risk, and Security Management in LLM-based Agentic Multi-Agent Systems ». [arXiv:2506.04133v5](https://arxiv.org/abs/2506.04133), déposée le 4 juin 2025, v5 du 18 décembre 2025 — **prépublication non révisée par les pairs**.
21. Richard Kang et Yudho Diponegoro. « Governance Gaps in Agent Interoperability Protocols: What MCP, A2A, and ACP Cannot Express ». [arXiv:2606.31498v1](https://arxiv.org/abs/2606.31498), déposée le 30 juin 2026 — **prépublication non révisée par les pairs**.
22. Juan A. Wibowo et George C. Polyzos. « Toward a Safe Internet of Agents ». [arXiv:2512.00520v2](https://arxiv.org/abs/2512.00520), déposée le 29 novembre 2025, v2 du 27 avril 2026 — **prépublication non révisée par les pairs**.
23. Grégoire Mialon, Clémentine Fourrier *et al.*. « GAIA: a benchmark for General AI Assistants ». [arXiv:2311.12983v1](https://arxiv.org/abs/2311.12983), déposée le 21 novembre 2023 — **prépublication non révisée par les pairs**.
24. Shunyu Yao, Noah Shinn *et al.*. « $τ$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains ». [arXiv:2406.12045v1](https://arxiv.org/abs/2406.12045), déposée le 17 juin 2024 — **prépublication non révisée par les pairs**.
25. Erik Pautsch, Tanmay Singla *et al.*. « AgentHub: A Registry for Discoverable, Verifiable, and Reproducible AI Agents ». [arXiv:2510.03495v2](https://arxiv.org/abs/2510.03495), déposée le 3 octobre 2025, v2 du 26 février 2026 — **prépublication non révisée par les pairs**.
26. Georgios Ioannides, Christos Constantinou *et al.*. « MOD-X: A Modular Open Decentralized eXchange Framework proposal for Heterogeneous Interoperable Artificial Intelligence Agents ». [arXiv:2507.04376v2](https://arxiv.org/abs/2507.04376), déposée le 6 juillet 2025, v2 du 8 juillet 2025 — **prépublication non révisée par les pairs**.
27. Roland R. Rodriguez. « Agent Identity URI Scheme: Topology-Independent Naming and Capability-Based Discovery for Multi-Agent Systems ». [arXiv:2601.14567v2](https://arxiv.org/abs/2601.14567), déposée le 21 janvier 2026, v2 du 13 juillet 2026 — **prépublication non révisée par les pairs**.
28. Tatiana Petrova, Boris Bliznioukov *et al.*. « From Multi-Agent Systems and the Semantic Web to Agentic AI: A Unified Narrative of the Web of Agents ». [arXiv:2507.10644v4](https://arxiv.org/abs/2507.10644), déposée le 14 juillet 2025, v4 du 24 mai 2026 — **prépublication non révisée par les pairs**.
29. Takumi Otsuka, Kentaroh Toyoda *et al.*. « AI Identity: Standards, Gaps, and Research Directions for AI Agents ». [arXiv:2604.23280v1](https://arxiv.org/abs/2604.23280), déposée le 25 avril 2026 — **prépublication non révisée par les pairs**.
30. Krti Tallam. « Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure ». [arXiv:2605.05440v1](https://arxiv.org/abs/2605.05440), déposée le 6 mai 2026 — **prépublication non révisée par les pairs**.
31. Maxim Vidgof, Stefan Bachhofner *et al.*. « Large Language Models for Business Process Management: Opportunities and Challenges ». [arXiv:2304.04309v1](https://arxiv.org/abs/2304.04309), déposée le 9 avril 2023 — **prépublication non révisée par les pairs**.
32. Hoang Vu, Nataliia Klievtsova *et al.*. « Agentic Business Process Management: Practitioner Perspectives on Agent Governance in Business Processes ». [arXiv:2504.03693v2](https://arxiv.org/abs/2504.03693), déposée le 23 mars 2025, v2 du 3 juillet 2025 — acceptation annoncée au seul champ *Comments* (« Accepted for Responsible BPM 2025, 15 pages including r »), non confirmée en notice.
33. Marlon Dumas, Fredrik Milani *et al.*. « Agentic Business Process Management Systems ». [arXiv:2601.18833v1](https://arxiv.org/abs/2601.18833), déposée le 25 janvier 2026 — acceptation annoncée au seul champ *Comments* (« Presented at the BPM'2025 conference on Artificial Inte »), non confirmée en notice.
34. Diego Calvanese, Angelo Casciani *et al.*. « Agentic Business Process Management: A Research Manifesto ». [arXiv:2603.18916v3](https://arxiv.org/abs/2603.18916), déposée le 19 mars 2026, v3 du 12 avril 2026 — **prépublication non révisée par les pairs**.
35. Tianbao Xie, Danyang Zhang *et al.*. « OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments ». [arXiv:2404.07972v2](https://arxiv.org/abs/2404.07972), déposée le 11 avril 2024, v2 du 30 mai 2024 — **prépublication non révisée par les pairs**.
36. Shangeetha Sivasothy, Scott Barnett *et al.*. « Large language models for generating rules, yay or nay? ». [arXiv:2406.06835v1](https://arxiv.org/abs/2406.06835), déposée le 10 juin 2024 — **prépublication non révisée par les pairs**.
37. Timotheus Kampik, Christian Warmuth *et al.*. « Large Process Models: A Vision for Business Process Management in the Age of Generative AI ». [arXiv:2309.00900v3](https://arxiv.org/abs/2309.00900), déposée le 2 septembre 2023, v3 du 17 janvier 2025 — **Künstl Intell (2024)**, doi:10.1007/s13218-024-00863-8.
38. Fabiana Fournier, Lior Limonad *et al.*. « Agentic AI Process Observability: Discovering Behavioral Variability ». [arXiv:2505.20127v2](https://arxiv.org/abs/2505.20127), déposée le 26 mai 2025, v2 du 3 juillet 2025 — **PMAI 25 (CEUR proceedings); Vol 4087; 2025**.
39. Alessandro Berti, Humam Kourani *et al.*. « PM-LLM-Benchmark: Evaluating Large Language Models on Process Mining Tasks ». [arXiv:2407.13244v1](https://arxiv.org/abs/2407.13244), déposée le 18 juillet 2024 — **prépublication non révisée par les pairs**.
40. Yingxuan Yang, Mulei Ma *et al.*. « Agentic Web: Weaving the Next Web with AI Agents ». [arXiv:2507.21206v1](https://arxiv.org/abs/2507.21206), déposée le 28 juillet 2025 — **prépublication non révisée par les pairs**.
41. Cameron Pattison, Matthew Boulos *et al.*. « The Agentic Web Requires New Normative Infrastructure ». [arXiv:2606.10711v2](https://arxiv.org/abs/2606.10711), déposée le 9 juin 2026, v2 du 15 juillet 2026 — **prépublication non révisée par les pairs**.
42. Yuhan Jin, Shuohan Wu *et al.*. « The Web4 Agent Economy: A Large-Scale Empirical Study of the Landscape, Challenges, and Opportunities ». [arXiv:2606.25876v1](https://arxiv.org/abs/2606.25876), déposée le 24 juin 2026 — **prépublication non révisée par les pairs**.
43. Shengchen Ling, Yihang Huang *et al.*. « Free-Riding the Agentic Web: A Systematic Security Analysis of x402 Payments ». [arXiv:2605.30998v2](https://arxiv.org/abs/2605.30998), déposée le 29 mai 2026, v2 du 22 juin 2026 — **prépublication non révisée par les pairs**.
44. Botao Amber Hu, Helena Rong *et al.*. « Dissociative Identity: Language Model Agents Lack Grounding for Reputation Mechanisms ». [arXiv:2605.30169v3](https://arxiv.org/abs/2605.30169), déposée le 28 mai 2026, v3 du 2 juillet 2026 — **publication attestée en notice**, doi:10.1145/3805689.3806748.
45. Cristian Trout, Sanmi Koyejo *et al.*. « Underwriting the Agent Economy: The Blueprint for an AI Insurance Stack ». [arXiv:2607.11999v2](https://arxiv.org/abs/2607.11999), déposée le 13 juillet 2026, v2 du 15 juillet 2026 — **prépublication non révisée par les pairs**.
46. Meredith Ringel Morris, Jascha Sohl-Dickstein *et al.*. « Levels of AGI for Operationalizing Progress on the Path to AGI ». [arXiv:2311.02462v5](https://arxiv.org/abs/2311.02462), déposée le 4 novembre 2023, v5 du 24 septembre 2025 — **Proceedings of ICML 2024**.
47. Zelin Li, Qin Wang *et al.*. « Five Attacks on x402 Agentic Payment Protocol ». [arXiv:2605.11781v1](https://arxiv.org/abs/2605.11781), déposée le 12 mai 2026 — **prépublication non révisée par les pairs**.
48. Mert Cemri, Melissa Z. Pan *et al.*. « Why Do Multi-Agent LLM Systems Fail? ». [arXiv:2503.13657v3](https://arxiv.org/abs/2503.13657), déposée le 17 mars 2025, v3 du 26 octobre 2025 — **prépublication non révisée par les pairs**.
49. Nicolás Padilla. « Exposed by Design: A Dynamic Security Assessment of Internet-Facing MCP Servers at Scale ». [arXiv:2608.00150v1](https://arxiv.org/abs/2608.00150), déposée le 31 juillet 2026 — **prépublication non révisée par les pairs**.
50. Xuanze Chen, Xukang Xie *et al.*. « MemSecBench: Tracking Agent Memory Poisoning from Persistence to Consequence and Repair ». [arXiv:2607.27080v1](https://arxiv.org/abs/2607.27080), déposée le 29 juillet 2026 — **prépublication non révisée par les pairs**.
51. Pei Chen, Baichao An *et al.*. « Rethinking MCP Security: A Large-Scale Study of Runtime MCP Servers and Security Scanner Reliability ». [arXiv:2607.11086v1](https://arxiv.org/abs/2607.11086), déposée le 13 juillet 2026 — **prépublication non révisée par les pairs**.
52. Mengying Wu, Pei Chen *et al.*. « MCPZoo: A Large-Scale Dataset of Runnable Model Context Protocol Servers for AI Agent ». [arXiv:2512.15144v3](https://arxiv.org/abs/2512.15144), déposée le 17 décembre 2025, v3 du 26 décembre 2025 — **prépublication non révisée par les pairs**.
53. Mohammed Mehedi Hasan, Hao Li *et al.*. « Model Context Protocol (MCP) Tool Descriptions Are Smelly! Towards Improving AI Agent Efficiency with Augmented MCP Tool Descriptions ». [arXiv:2602.14878v3](https://arxiv.org/abs/2602.14878), déposée le 16 février 2026, v3 du 31 mai 2026 — **prépublication non révisée par les pairs**.
54. Muhammad Hamza Arshad Majeed, May Mahmoud *et al.*. « An Empirical Study of Model Context Protocol Applications ». [arXiv:2607.25635v2](https://arxiv.org/abs/2607.25635), déposée le 28 juillet 2026, v2 du 29 juillet 2026 — **prépublication non révisée par les pairs**.
55. Yutao Shi, Xiaohan Zhang *et al.*. « Description-Code Inconsistency in Real-world MCP Servers: Measurement, Detection, and Security Implications ». [arXiv:2606.04769v1](https://arxiv.org/abs/2606.04769), déposée le 3 juin 2026 — **prépublication non révisée par les pairs**.
56. Andreas Schlapbach. « Formal Semantics for Agentic Tool Protocols: A Process Calculus Approach ». [arXiv:2603.24747v3](https://arxiv.org/abs/2603.24747), déposée le 25 mars 2026, v3 du 2 juillet 2026 — **prépublication non révisée par les pairs**.
57. Ionut Predoaia, Tuong Manh Vu *et al.*. « A Comparative Study of MCP and A2A for Inter-Agent Coordination in LLM-Based Systems ». [arXiv:2607.23884v1](https://arxiv.org/abs/2607.23884), déposée le 26 juillet 2026 — **prépublication non révisée par les pairs**.
58. Gautam Bharti. « Registry Descriptions Go Stale Unevenly: An 89-Day Measurement of Model Context Protocol Drift, and Why Drift-Ranked Re-Auditing Under-Covers It ». [arXiv:2608.00997v2](https://arxiv.org/abs/2608.00997), déposée le 2 août 2026, v2 du 4 août 2026 — **prépublication non révisée par les pairs**.
59. Benny Toeppe, Amine Barrak *et al.*. « A Large-Scale Dataset of MCP Implementations on GitHub ». [arXiv:2607.10123v1](https://arxiv.org/abs/2607.10123), déposée le 11 juillet 2026 — **Proceedings of MSR '26: 23rd International Conference on Mining Software Repositories, April 13-14, 2026, Rio de Janeiro, Brazil. ACM, 2026**.
60. Edoardo Allegrini, Ananth Shreekumar *et al.*. « Formalizing the Safety, Security, and Functional Properties of Agentic AI Systems ». [arXiv:2510.14133v2](https://arxiv.org/abs/2510.14133), déposée le 15 octobre 2025, v2 du 15 avril 2026 — **prépublication non révisée par les pairs**.
61. Samuel H. Christie, Amit K. Chopra *et al.*. « Strabo: Declarative Specification and Implementation of Agentic Interaction Protocols ». [arXiv:2606.05043v1](https://arxiv.org/abs/2606.05043), déposée le 3 juin 2026 — acceptation annoncée au seul champ *Comments* (« Presented in the Engineering Multiagent Systems Worksho »), non confirmée en notice.
62. Dun Yuan, Fuyuan Lyu *et al.*. « Beyond Message Passing: A Semantic View of Agent Communication Protocols ». [arXiv:2604.02369v3](https://arxiv.org/abs/2604.02369), déposée le 30 mars 2026, v3 du 13 avril 2026 — **prépublication non révisée par les pairs**.
63. Mugeng Liu, Shuoqi Li *et al.*. « Beyond Static Endpoints: Tool Programs as an Interface for Flexible Agentic Web Services ». [arXiv:2606.19992v1](https://arxiv.org/abs/2606.19992), déposée le 18 juin 2026 — acceptation annoncée au seul champ *Comments* (« Accepted by ICML 2026 »), non confirmée en notice.
64. Woohyuk Choi, Juhee Kim *et al.*. « Agent Data Injection Attacks are Realistic Threats to AI Agents ». [arXiv:2607.05120v1](https://arxiv.org/abs/2607.05120), déposée le 6 juillet 2026 — **prépublication non révisée par les pairs**.
65. Ben Nassi, Stav Cohen *et al.*. « Invitation Is All You Need! Promptware Attacks Against LLM-Powered Assistants in Production Are Practical and Dangerous ». [arXiv:2508.12175v1](https://arxiv.org/abs/2508.12175), déposée le 16 août 2025 — **prépublication non révisée par les pairs**.
66. Shuli Zhao, Qinsheng Hou *et al.*. « Parasites in the Toolchain: A Large-Scale Analysis of Attacks on the MCP Ecosystem ». [arXiv:2509.06572v5](https://arxiv.org/abs/2509.06572), déposée le 8 septembre 2025, v5 du 1 mai 2026 — acceptation annoncée au seul champ *Comments* (« Accepted by IEEE Symposium on Security and Privacy, 202 »), non confirmée en notice.
67. Zhiqiang Wang, Yichao Gao *et al.*. « MCPTox: A Benchmark for Tool Poisoning Attack on Real-World MCP Servers ». [arXiv:2508.14925v1](https://arxiv.org/abs/2508.14925), déposée le 19 août 2025 — **prépublication non révisée par les pairs**.
68. David Schmotz, Luca Beurer-Kellner *et al.*. « Skill-Inject: Measuring Agent Vulnerability to Skill File Attacks ». [arXiv:2602.20156v3](https://arxiv.org/abs/2602.20156), déposée le 23 février 2026, v3 du 25 février 2026 — **prépublication non révisée par les pairs**.
69. Hengyu An, Minxi Li *et al.*. « ACIArena: Toward Unified Evaluation for Agent Cascading Injection ». [arXiv:2604.07775v1](https://arxiv.org/abs/2604.07775), déposée le 9 avril 2026 — acceptation annoncée au seul champ *Comments* (« ACL 2026 »), non confirmée en notice.
70. Debeshee Das, Julien Piet *et al.*. « Trojan Hippo: Weaponizing Agent Memory for Data Exfiltration ». [arXiv:2605.01970v3](https://arxiv.org/abs/2605.01970), déposée le 3 mai 2026, v3 du 15 mai 2026 — **prépublication non révisée par les pairs**.
71. Xinhang Ma, Taoran Li *et al.*. « AutoDojo: Adaptive Black-Box Attacks Reveal the Limits of IPI Defenses and Task-Specification Effects in LLM Agents ». [arXiv:2606.15057v2](https://arxiv.org/abs/2606.15057), déposée le 13 juin 2026, v2 du 19 juin 2026 — **prépublication non révisée par les pairs**.
72. Hao Li, Ruoyao Wen *et al.*. « AgentDyn: Are Your Agent Security Defenses Deployable in Real-World Dynamic Environments? ». [arXiv:2602.03117v3](https://arxiv.org/abs/2602.03117), déposée le 3 février 2026, v3 du 7 mai 2026 — **prépublication non révisée par les pairs**.
73. Zixin Rao, Wentian Zhu *et al.*. « FragFuse: Bypassing Access Control of Large Language Model Agents via Memory-Based Query Fragmentation and Fusion ». [arXiv:2606.15609v1](https://arxiv.org/abs/2606.15609), déposée le 14 juin 2026 — acceptation annoncée au seul champ *Comments* (« 33 pages, 4 figures. Accepted by USENIX Security 2026 »), non confirmée en notice.
74. Dennis Jacob, Emad Alghamdi *et al.*. « Preventing Prompt Injection with Type-Directed Privilege Separation ». [arXiv:2509.25926v2](https://arxiv.org/abs/2509.25926), déposée le 30 septembre 2025, v2 du 8 mai 2026 — **prépublication non révisée par les pairs**.
75. Vladyslav Parakhin. « The Bureaucracy of Speed: Structural Equivalence Between Memory Consistency Models and Multi-Agent Authorization Revocation ». [arXiv:2603.09875v1](https://arxiv.org/abs/2603.09875), déposée le 10 mars 2026 — **prépublication non révisée par les pairs**.
76. KrishnaSaiReddy Patil. « SentinelAgent: Intent-Verified Delegation Chains for Securing Federal Multi-Agent AI Systems ». [arXiv:2604.02767v1](https://arxiv.org/abs/2604.02767), déposée le 3 avril 2026 — **prépublication non révisée par les pairs**.
77. Asiri Dalugoda. « HDP: A Lightweight Cryptographic Protocol for Human Delegation Provenance in Agentic AI Systems ». [arXiv:2604.04522v1](https://arxiv.org/abs/2604.04522), déposée le 6 avril 2026 — **prépublication non révisée par les pairs**.
78. Yuan Sun. « Safe Bilevel Delegation (SBD): A Formal Framework for Runtime Delegation Safety in Multi-Agent Systems ». [arXiv:2604.27358v1](https://arxiv.org/abs/2604.27358), déposée le 30 avril 2026 — **prépublication non révisée par les pairs**.
79. Mehmet Haklidir. « Consent Chain Degradation in Embodied Multi-Agent Systems: Bridging the Gap Between AI Agent Governance and Robot Ethics ». [arXiv:2605.16300v1](https://arxiv.org/abs/2605.16300), déposée le 17 avril 2026 — acceptation annoncée au seul champ *Comments* (« Accepted for oral presentation at the 2nd Workshop on R »), non confirmée en notice.
80. Saurabh Deochake. « Heartbeat-Bound Hierarchical Credentials: Cryptographic Revocation for AI Agent Swarms ». [arXiv:2605.20704v1](https://arxiv.org/abs/2605.20704), déposée le 20 mai 2026 — **prépublication non révisée par les pairs**.
81. Huijun Zhou, Xiaohan Zhang *et al.*. « A First Measurement Study on Authentication Security in Real-World Remote MCP Servers ». [arXiv:2605.22333v1](https://arxiv.org/abs/2605.22333), déposée le 21 mai 2026 — **prépublication non révisée par les pairs**.
82. Christophe Parisel. « Privilege Risk Evolution for Non-Human Identities: A Temporal Fiber Model for Cloud IAM ». [arXiv:2606.03289v1](https://arxiv.org/abs/2606.03289), déposée le 2 juin 2026 — **prépublication non révisée par les pairs**.
83. Amjad Ibrahim et Yong Li. « Overlaying Governance: A Compositional Authorization Framework for Delegation and Scope in Agentic AI ». [arXiv:2606.03518v1](https://arxiv.org/abs/2606.03518), déposée le 2 juin 2026 — **prépublication non révisée par les pairs**.
84. Abhinav Mishra et Kumar Sharad. « Observability for Delegated Execution in Agentic AI Systems ». [arXiv:2606.09692v1](https://arxiv.org/abs/2606.09692), déposée le 8 juin 2026 — **prépublication non révisée par les pairs**.
85. Shenghan Zheng, Qifan Zhang *et al.*. « Formal Security Analysis of Agent Protocol Composition ». [arXiv:2606.28690v1](https://arxiv.org/abs/2606.28690), déposée le 27 juin 2026 — **prépublication non révisée par les pairs**.
86. Anton Sokolov. « Hardware-rooted attestation for AI-agent evidence: composing IETF RATS with action evidence packages ». [arXiv:2608.00801v1](https://arxiv.org/abs/2608.00801), déposée le 1 août 2026 — **prépublication non révisée par les pairs**.
87. Igor Santos-Grueiro. « Lingering Authority: Revocable Resource-and-Effect Capabilities for Coding Agents ». [arXiv:2606.22504v1](https://arxiv.org/abs/2606.22504), déposée le 21 juin 2026 — **prépublication non révisée par les pairs**.
88. Shaokun Zhang, Ming Yin *et al.*. « Which Agent Causes Task Failures and When? On Automated Failure Attribution of LLM Multi-Agent Systems ». [arXiv:2505.00212v3](https://arxiv.org/abs/2505.00212), déposée le 30 avril 2025, v3 du 2 juin 2025 — acceptation annoncée au seul champ *Comments* (« camera-ready »), non confirmée en notice.
89. Mengzhuo Chen, Junjie Wang *et al.*. « Seeing the Whole Elephant: A Benchmark for Failure Attribution in LLM-based Multi-Agent Systems ». [arXiv:2604.22708v1](https://arxiv.org/abs/2604.22708), déposée le 24 avril 2026 — acceptation annoncée au seul champ *Comments* (« Accepted by ACL 2026 »), non confirmée en notice.
90. Yizhe Xie, Congcong Zhu *et al.*. « From Spark to Fire: Modeling and Mitigating Error Cascades in LLM-Based Multi-Agent Collaboration ». [arXiv:2603.04474v2](https://arxiv.org/abs/2603.04474), déposée le 4 mars 2026, v2 du 11 mai 2026 — **prépublication non révisée par les pairs**.
91. Maksym Nechepurenko et Pavel Shuvalov. « Coordination as an Architectural Layer for LLM-Based Multi-Agent Systems ». [arXiv:2605.03310v1](https://arxiv.org/abs/2605.03310), déposée le 5 mai 2026 — **prépublication non révisée par les pairs**.
92. Qineng Wang, Zihao Wang *et al.*. « Rethinking the Bounds of LLM Reasoning: Are Multi-Agent Discussions the Key? ». [arXiv:2402.18272v1](https://arxiv.org/abs/2402.18272), déposée le 28 février 2024 — **prépublication non révisée par les pairs** *selon la notice*. ⚠ **Publication établie hors notice**, recoupement Crossref du 15 août 2026 : actes de l'ACL 2024 (article long), doi:10.18653/v1/2024.acl-long.331 — *la notice ne porte ni `journal_ref` ni DOI.*
93. Andries Smit, Paul Duckworth *et al.*. « Should we be going MAD? A Look at Multi-Agent Debate Strategies for LLMs ». [arXiv:2311.17371v3](https://arxiv.org/abs/2311.17371), déposée le 29 novembre 2023, v3 du 18 juillet 2024 — **prépublication non révisée par les pairs**.
94. Prathyusha Jwalapuram, Hehai Lin *et al.*. « The Illusion of Multi-Agent Advantage ». [arXiv:2606.13003v2](https://arxiv.org/abs/2606.13003), déposée le 11 juin 2026, v2 du 13 juin 2026 — **prépublication non révisée par les pairs**.
95. Yuxuan Zhao, Sijia Chen *et al.*. « When Does Multi-Agent Collaboration Help? An Entropy Perspective ». [arXiv:2602.04234v6](https://arxiv.org/abs/2602.04234), déposée le 4 février 2026, v6 du 4 juin 2026 — **prépublication non révisée par les pairs**.
96. Chen Qian, Zihao Xie *et al.*. « Scaling Large Language Model-based Multi-Agent Collaboration ». [arXiv:2406.07155v3](https://arxiv.org/abs/2406.07155), déposée le 11 juin 2024, v3 du 17 mars 2025 — acceptation annoncée au seul champ *Comments* (« Accepted to ICLR-2025 »), non confirmée en notice.
97. Han Zhou, Xingchen Wan *et al.*. « Multi-Agent Design: Optimizing Agents with Better Prompts and Topologies ». [arXiv:2502.02533v2](https://arxiv.org/abs/2502.02533), déposée le 4 février 2025, v2 du 31 janvier 2026 — acceptation annoncée au seul champ *Comments* (« ICLR 2026 »), non confirmée en notice.
98. Siddhant Kulkarni et Yukta Kulkarni. « Benchmarking Multi-Agent LLM Architectures for Financial Document Processing: A Comparative Study of Orchestration Patterns, Cost-Accuracy Tradeoffs and Production Scaling Strategies ». [arXiv:2603.22651v1](https://arxiv.org/abs/2603.22651), déposée le 24 mars 2026 — **prépublication non révisée par les pairs**.
99. Fulin Lin, Shaowen Chen *et al.*. « Stop Wasting Your Tokens: Towards Efficient Runtime Multi-Agent Systems ». [arXiv:2510.26585v2](https://arxiv.org/abs/2510.26585), déposée le 30 octobre 2025, v2 du 2 mars 2026 — acceptation annoncée au seul champ *Comments* (« Accepted to ICLR 2026. The code is available at https:/ »), non confirmée en notice.
100. Yian Wang, Agam Goyal *et al.*. « State Contamination in Memory-Augmented LLM Agents ». [arXiv:2605.16746v1](https://arxiv.org/abs/2605.16746), déposée le 16 mai 2026 — **prépublication non révisée par les pairs**.
101. Emre Turan. « Oversight Has a Capacity: Calibrating Agent Guards to a Subjective, Fatiguing Human ». [arXiv:2606.08919v1](https://arxiv.org/abs/2606.08919), déposée le 8 juin 2026 — **prépublication non révisée par les pairs**.
102. Frank F. Xu, Yufan Song *et al.*. « TheAgentCompany: Benchmarking LLM Agents on Consequential Real World Tasks ». [arXiv:2412.14161v3](https://arxiv.org/abs/2412.14161), déposée le 18 décembre 2024, v3 du 10 septembre 2025 — **prépublication non révisée par les pairs** *selon la notice*. ⚠ **Publication établie hors notice**, recoupement du 15 août 2026 : actes NeurIPS 2025, piste *Datasets and Benchmarks* — *la notice ne porte ni `journal_ref` ni DOI.*
103. Xingyao Wang, Boxuan Li *et al.*. « OpenHands: An Open Platform for AI Software Developers as Generalist Agents ». [arXiv:2407.16741v3](https://arxiv.org/abs/2407.16741), déposée le 23 juillet 2024, v3 du 18 avril 2025 — acceptation annoncée au seul champ *Comments* (« Accepted by ICLR 2025; Code: https://github.com/All-Han »), non confirmée en notice.
104. Kung-Hsiang Huang, Akshara Prabhakar *et al.*. « CRMArena-Pro: Holistic Assessment of LLM Agents Across Diverse Business Scenarios and Interactions ». [arXiv:2505.18878v1](https://arxiv.org/abs/2505.18878), déposée le 24 mai 2025 — **prépublication non révisée par les pairs**.
105. Yipeng Ouyang, Xin Huang *et al.*. « Benchmarks are Not Enough: RAMP for Runtime Assessing of Agentic Models in Production Systems ». [arXiv:2605.27492v1](https://arxiv.org/abs/2605.27492), déposée le 26 mai 2026 — **prépublication non révisée par les pairs**.
106. Sayash Kapoor, Benedikt Stroebl *et al.*. « AI Agents That Matter ». [arXiv:2407.01502v1](https://arxiv.org/abs/2407.01502), déposée le 1 juillet 2024 — **prépublication non révisée par les pairs**.
107. Yuxuan Zhu, Tengjun Jin *et al.*. « Establishing Best Practices for Building Rigorous Agentic Benchmarks ». [arXiv:2507.02825v5](https://arxiv.org/abs/2507.02825), déposée le 3 juillet 2025, v5 du 7 août 2025 — **prépublication non révisée par les pairs** *selon la notice*. ⚠ **Publication établie hors notice**, recoupement du 15 août 2026 : actes NeurIPS 2025, piste *Datasets and Benchmarks* — *la notice ne porte ni `journal_ref` ni DOI, et cette pièce n'est pas non plus indexée à DBLP sous NeurIPS : le recoupement lui-même décroche.*
108. Shanchao Liang, Spandan Garg *et al.*. « The SWE-Bench Illusion: When State-of-the-Art LLMs Remember Instead of Reason ». [arXiv:2506.12286v4](https://arxiv.org/abs/2506.12286), déposée le 14 juin 2025, v4 du 1 décembre 2025 — **prépublication non révisée par les pairs**.
109. Florian E. Dorner, Vivian Y. Nastl *et al.*. « Limits to scalable evaluation at the frontier: LLM as Judge won't beat twice the data ». [arXiv:2410.13341v3](https://arxiv.org/abs/2410.13341), déposée le 17 octobre 2024, v3 du 6 janvier 2026 — acceptation annoncée au seul champ *Comments* (« ICLR 2025; 28 pages, 8 figures »), non confirmée en notice.
110. Mingchen Zhuge, Changsheng Zhao *et al.*. « Agent-as-a-Judge: Evaluate Agents with Agents ». [arXiv:2410.10934v2](https://arxiv.org/abs/2410.10934), déposée le 14 octobre 2024, v2 du 16 octobre 2024 — **prépublication non révisée par les pairs**.
111. Darshan Deshpande, Varun Gangal *et al.*. « TRAIL: Trace Reasoning and Agentic Issue Localization ». [arXiv:2505.08638v3](https://arxiv.org/abs/2505.08638), déposée le 13 mai 2025, v3 du 23 juin 2025 — **prépublication non révisée par les pairs**.
112. Renan Souza, Amal Gueroudji *et al.*. « PROV-AGENT: Unified Provenance for Tracking AI Agent Interactions in Agentic Workflows ». [arXiv:2508.02866v3](https://arxiv.org/abs/2508.02866), déposée le 4 août 2025, v3 du 20 août 2025 — acceptation annoncée au seul champ *Comments* (« Paper accepted for publication in the Proceedings of th »), non confirmée en notice.
113. Yi Nian, Aojie Yuan *et al.*. « Auditable Agents ». [arXiv:2604.05485v2](https://arxiv.org/abs/2604.05485), déposée le 7 avril 2026, v2 du 13 août 2026 — acceptation annoncée au seul champ *Comments* (« 24 pages, 1 figure. Extended version. A condensed 4-pag »), non confirmée en notice.
114. Qian'ang Mao, Jiaxin Wang *et al.*. « SoK: Security of Autonomous LLM Agents in Agentic Commerce ». [arXiv:2604.15367v2](https://arxiv.org/abs/2604.15367), déposée le 15 avril 2026, v2 du 1 mai 2026 — **prépublication non révisée par les pairs**.
115. Yuanzhe Zhang, Yuexin Xiang *et al.*. « SoK: Blockchain Agent-to-Agent Payments ». [arXiv:2604.03733v1](https://arxiv.org/abs/2604.03733), déposée le 4 avril 2026 — **prépublication non révisée par les pairs**.
116. Tanusree Debi, Wentian Zhu *et al.*. « Whispers of Wealth: Red-Teaming Google's Agent Payments Protocol via Prompt Injection ». [arXiv:2601.22569v2](https://arxiv.org/abs/2601.22569), déposée le 30 janvier 2026, v2 du 18 mai 2026 — **prépublication non révisée par les pairs**.
117. Qianlong Lan, Anuj Kaul *et al.*. « Zero-Trust Runtime Verification for Agentic Payment Protocols: Mitigating Replay and Context-Binding Failures in AP2 ». [arXiv:2602.06345v1](https://arxiv.org/abs/2602.06345), déposée le 6 février 2026 — **prépublication non révisée par les pairs**.
118. Xihan Xiong, Zelin Li *et al.*. « Can Trustless Agents Be Trusted? An Empirical Study of the ERC-8004 Decentralized AI Agent Ecosystem ». [arXiv:2606.26028v2](https://arxiv.org/abs/2606.26028), déposée le 24 juin 2026, v2 du 8 juillet 2026 — **prépublication non révisée par les pairs**.
119. Sara Fish, Yannai A. Gonczarowski *et al.*. « Algorithmic Collusion by Large Language Models ». [arXiv:2404.00806v5](https://arxiv.org/abs/2404.00806), déposée le 31 mars 2024, v5 du 5 mars 2026 — **prépublication non révisée par les pairs**.
120. Jussi Keppo, Yuze Li *et al.*. « On the Fragility of AI Agent Collusion ». [arXiv:2603.20281v1](https://arxiv.org/abs/2603.20281), déposée le 18 mars 2026 — **prépublication non révisée par les pairs**.
121. Yingtao Tian. « Prompt Optimization Enables Stable Algorithmic Collusion in LLM Agents ». [arXiv:2604.17774v1](https://arxiv.org/abs/2604.17774), déposée le 20 avril 2026 — **prépublication non révisée par les pairs**.
122. Gagan Bansal, Wenyue Hua *et al.*. « Magentic Marketplace: An Open-Source Environment for Studying Agentic Markets ». [arXiv:2510.25779v1](https://arxiv.org/abs/2510.25779), déposée le 27 octobre 2025 — **prépublication non révisée par les pairs**.
123. Xianyang Liu, Shangding Gu *et al.*. « AgenticPay: A Multi-Agent LLM Negotiation System for Buyer-Seller Transactions ». [arXiv:2602.06008v1](https://arxiv.org/abs/2602.06008), déposée le 5 février 2026 — **prépublication non révisée par les pairs**.
124. Amine Allouah, Omar Besbes *et al.*. « What Is Your AI Agent Buying? Evaluation, Biases, Model Dependence, & Emerging Implications for Agentic E-Commerce ». [arXiv:2508.02630v3](https://arxiv.org/abs/2508.02630), déposée le 4 août 2025, v3 du 17 décembre 2025 — **prépublication non révisée par les pairs** *selon la notice*. ⚠ **Publication établie hors notice**, recoupement Crossref du 15 août 2026 : *Proceedings of the ACM Web Conference 2026*, doi:10.1145/3774904.3792943 — *la notice ne porte ni `journal_ref` ni DOI ; à ne pas confondre avec la version SSRN de 2025 des mêmes auteurs, au sous-titre différent.*
125. Alexander Erlei et Lukas Meub. « LLM-Agent Interactions on Markets with Information Asymmetries ». [arXiv:2603.08853v1](https://arxiv.org/abs/2603.08853), déposée le 9 mars 2026 — **prépublication non révisée par les pairs**.
126. Bardia Mohammadi, Nearchos Potamitis *et al.*. « Atomix: Timely, Transactional Tool Use for Reliable Agentic Workflows ». [arXiv:2602.14849v2](https://arxiv.org/abs/2602.14849), déposée le 16 février 2026, v2 du 29 mai 2026 — **prépublication non révisée par les pairs**.
127. Edward Y. Chang, Longling Geng *et al.*. « Mnemosyne: Agentic Transaction Processing for Validating and Repairing AI-generated Workflows ». [arXiv:2607.00269v2](https://arxiv.org/abs/2607.00269), déposée le 30 juin 2026, v2 du 5 juillet 2026 — **prépublication non révisée par les pairs**.
128. Sajjad Khan. « Verified Detection and Prevention of Concurrency Anomalies in Multi-Agent Large Language Model Systems ». [arXiv:2606.17182v1](https://arxiv.org/abs/2606.17182), déposée le 15 juin 2026 — **prépublication non révisée par les pairs**.
129. Zhiyuan Zhai, Ming Li *et al.*. « Revisable by Design: A Theory of Streaming LLM Agent Execution ». [arXiv:2604.23283v1](https://arxiv.org/abs/2604.23283), déposée le 25 avril 2026 — **prépublication non révisée par les pairs**.
130. Hoang Vu, Maximilian Körner *et al.*. « Agent Behavior Mining: Generative AI Agent Governance in Business Processes ». [arXiv:2606.20669v1](https://arxiv.org/abs/2606.20669), déposée le 12 juin 2026 — acceptation annoncée au seul champ *Comments* (« Accepted at BPM conference 2026 management main track »), non confirmée en notice.
131. Alexander Rombach, Chantale Lauer *et al.*. « Neuro-Symbolic Agents for Regulated Process Automation: Challenges and Research Agenda ». [arXiv:2606.13405v2](https://arxiv.org/abs/2606.13405), déposée le 11 juin 2026, v2 du 22 juin 2026 — acceptation annoncée au seul champ *Comments* (« Accepted as a poster in NILA Workshop @ IJCAI-ECAI 2026 »), non confirmée en notice.
132. Fabiana Fournier et Lior Limonad. « A Process Harness for Uplifting Legacy Workflows to Agentic BPM: Design and Realization in CUGA FLO ». [arXiv:2606.27188v1](https://arxiv.org/abs/2606.27188), déposée le 25 juin 2026 — **prépublication non révisée par les pairs**.
133. Adem Ait, Javier Luis Cánovas Izquierdo *et al.*. « Towards Modeling Human-Agentic Collaborative Workflows: A BPMN Extension ». [arXiv:2412.05958v3](https://arxiv.org/abs/2412.05958), déposée le 8 décembre 2024, v3 du 27 juin 2025 — acceptation annoncée au seul champ *Comments* (« Accepted in the Euromicro Conference Series on Software »), non confirmée en notice.
134. Ylli Prifti. « Specifying AI-SDLC Processes: A Protocol Language for Human-Agent Boundaries ». [arXiv:2606.20615v2](https://arxiv.org/abs/2606.20615), déposée le 24 mai 2026, v2 du 24 juin 2026 — **prépublication non révisée par les pairs**.
135. Saimir Bala, Fabiana Fournier *et al.*. « Using Process Mining to Generate AI Agents from Software Engineering Process Records ». [arXiv:2607.04948v1](https://arxiv.org/abs/2607.04948), déposée le 6 juillet 2026 — acceptation annoncée au seul champ *Comments* (« To be published at the 24th International Conference on »), non confirmée en notice.
136. Chantale Lauer, Peter Pfeiffer *et al.*. « Assessing the Business Process Modeling Competences of Large Language Models ». [arXiv:2601.21787v2](https://arxiv.org/abs/2601.21787), déposée le 29 janvier 2026, v2 du 29 juin 2026 — **Information Systems, Vol. 142 (2026), Art. 102761**, doi:10.1016/j.is.2026.102761.
137. Ilias Chalkidis, Vlad Paul Cosma *et al.*. « Hybrid AI for Explainable and Accurate Conversational Agents in eGovernment ». [arXiv:2608.01346v1](https://arxiv.org/abs/2608.01346), déposée le 2 août 2026 — acceptation annoncée au seul champ *Comments* (« Presented at AIDA2J Workshop at ICAIL 2026, SMU, Singap »), non confirmée en notice.
138. Luca Nannini, Adam Leon Smith *et al.*. « AI Agents Under EU Law ». [arXiv:2604.04604v1](https://arxiv.org/abs/2604.04604), déposée le 6 avril 2026 — **prépublication non révisée par les pairs**.
139. Kathrin Gardhouse, Amin Oueslati *et al.*. « Regulating AI Agents ». [arXiv:2603.23471v2](https://arxiv.org/abs/2603.23471), déposée le 24 mars 2026, v2 du 7 juillet 2026 — **prépublication non révisée par les pairs**.
140. Yiheng Yao. « Acting with AI: An Interaction-Based Framework for Agentic Tort Liability ». [arXiv:2606.00518v1](https://arxiv.org/abs/2606.00518), déposée le 30 mai 2026 — **prépublication non révisée par les pairs**.
141. Mark O. Riedl et Deven R. Desai. « AI Agents and the Law ». [arXiv:2508.08544v1](https://arxiv.org/abs/2508.08544), déposée le 12 août 2025 — acceptation annoncée au seul champ *Comments* (« 2025 AAAI Conference on AI, Ethics, and Society »), non confirmée en notice.
142. Garry A. Gabison et R. Patrick Xian. « Inherent and emergent liability issues in LLM-based agentic systems: a principal-agent perspective ». [arXiv:2504.03255v2](https://arxiv.org/abs/2504.03255), déposée le 4 avril 2025, v2 du 17 juin 2025 — **publication attestée en notice**, doi:10.18653/v1/2025.realm-1.9.
143. Johann Laux et Hannah Ruschemeier. « Automation Bias in the AI Act: On the Legal Implications of Attempting to De-Bias Human Oversight of AI ». [arXiv:2502.10036v2](https://arxiv.org/abs/2502.10036), déposée le 14 février 2025, v2 du 20 juin 2025 — **Eur. j. risk regul. 16 (2025) 1519-1534**, doi:10.1017/err.2025.10033.
144. Leon Staufer, Kevin Feng *et al.*. « The 2025 AI Agent Index: Documenting Technical and Safety Features of Deployed Agentic AI Systems ». [arXiv:2602.17753v2](https://arxiv.org/abs/2602.17753), déposée le 19 février 2026, v2 du 6 mai 2026 — **publication attestée en notice**, doi:10.1145/3805689.3806728.
145. Mubarak Raji et Masooda Bashir. « Towards Agentic AI Governance: A Preliminary Assessment ». [arXiv:2607.07612v1](https://arxiv.org/abs/2607.07612), déposée le 8 juillet 2026 — acceptation annoncée au seul champ *Comments* (« International Conference on the AI Revolution: Research »), non confirmée en notice.
146. Irene Aldridge et Steve Krawciw. « AI Governance for Institutional Readiness in Finance ». [arXiv:2608.02311v2](https://arxiv.org/abs/2608.02311), déposée le 3 août 2026, v2 du 10 août 2026 — **prépublication non révisée par les pairs**.
147. Gabriela Aránguiz Dias, Kiana Jafari *et al.*. « The Doctor Will (Still) See You Now: On the Structural Limits of Agentic AI in Healthcare ». [arXiv:2602.18460v1](https://arxiv.org/abs/2602.18460), déposée le 6 février 2026 — **prépublication non révisée par les pairs**.
148. Sebastian Lobentanzer. « Quantifying the Expectation-Realisation Gap for Agentic AI Systems ». [arXiv:2602.20292v2](https://arxiv.org/abs/2602.20292), déposée le 23 février 2026, v2 du 25 février 2026 — **prépublication non révisée par les pairs**.
149. Eranga Bandara, Ross Gore *et al.*. « Towards an Agent-First Web: Redesigning the Web for AI Agents ». [arXiv:2606.19116v1](https://arxiv.org/abs/2606.19116), déposée le 17 juin 2026 — **prépublication non révisée par les pairs**.
150. Sven Schultze, Meike Verena Kietzmann *et al.*. « Building the Web for Agents: A Declarative Framework for Agent-Web Interaction ». [arXiv:2511.11287v1](https://arxiv.org/abs/2511.11287), déposée le 14 novembre 2025 — **prépublication non révisée par les pairs**.
151. Taein Kim, Karstan Bock *et al.*. « Scrapers selectively respect robots.txt directives: evidence from a large-scale empirical study ». [arXiv:2505.21733v2](https://arxiv.org/abs/2505.21733), déposée le 27 mai 2025, v2 du 23 octobre 2025 — **prépublication non révisée par les pairs**.
152. Ethan Wang, Zubair Shafiq *et al.*. « FP-Agent: Fingerprinting AI Browsing Agents ». [arXiv:2605.01247v1](https://arxiv.org/abs/2605.01247), déposée le 2 mai 2026 — **prépublication non révisée par les pairs**.
153. Zhe Ren, Yimeng Chen *et al.*. « Self-Improvements in Modern Agentic Systems: A Survey ». [arXiv:2607.13104v1](https://arxiv.org/abs/2607.13104), déposée le 14 juillet 2026 — **prépublication non révisée par les pairs**.
154. Ruixiao Lin, Xinhao Deng *et al.*. « Safety in Self-Evolving LLM Agent Systems: Threats, Amplification, and Case Studies ». [arXiv:2606.23075v1](https://arxiv.org/abs/2606.23075), déposée le 22 juin 2026 — **prépublication non révisée par les pairs**.
155. K. J. Kevin Feng, David W. McDonald *et al.*. « Levels of Autonomy for AI Agents ». [arXiv:2506.12469v2](https://arxiv.org/abs/2506.12469), déposée le 14 juin 2025, v2 du 28 juillet 2025 — acceptation annoncée au seul champ *Comments* (« Published in the Knight 1st Amendment Institute's "AI a »), non confirmée en notice.
156. Peter Cihon, Merlin Stein *et al.*. « Measuring AI agent autonomy: Towards a scalable approach with code inspection ». [arXiv:2502.15212v1](https://arxiv.org/abs/2502.15212), déposée le 21 février 2025 — acceptation annoncée au seul champ *Comments* (« NeurIPS Socially Responsible Language Modelling Researc »), non confirmée en notice.
157. Eric Xing, Mingkai Deng *et al.*. « Critique of Agent Model ». [arXiv:2606.23991v1](https://arxiv.org/abs/2606.23991), déposée le 22 juin 2026 — **prépublication non révisée par les pairs**.
158. Pradyumna Shome, Sashreek Krishnan *et al.*. « Why Johnny Can't Use Agents: Industry Aspirations vs. User Realities with AI Agents ». [arXiv:2509.14528v2](https://arxiv.org/abs/2509.14528), déposée le 18 septembre 2025, v2 du 3 mai 2026 — **publication attestée en notice**, doi:10.1145/3786335.3813140.
159. Yubin Kim, Ken Gu *et al.*. « Towards a Science of Scaling Agent Systems ». [arXiv:2512.08296v3](https://arxiv.org/abs/2512.08296), déposée le 9 décembre 2025, v3 du 8 avril 2026 — **prépublication non révisée par les pairs**.
160. Yuzhen Mao et Azalia Mirhoseini. « Decentralized Multi-Agent Systems with Shared Context ». [arXiv:2606.10662v1](https://arxiv.org/abs/2606.10662), déposée le 9 juin 2026 — **prépublication non révisée par les pairs**.
161. Alireza Salemi, Mihir Parmar *et al.*. « LLM-Based Multi-Agent Blackboard System for Information Discovery in Data Science ». [arXiv:2510.01285v2](https://arxiv.org/abs/2510.01285), déposée le 30 septembre 2025, v2 du 31 janvier 2026 — **prépublication non révisée par les pairs**.
162. Dong Wang, Yang Li *et al.*. « Matrix: Peer-to-Peer Multi-Agent Synthetic Data Generation Framework ». [arXiv:2511.21686v2](https://arxiv.org/abs/2511.21686), déposée le 26 novembre 2025, v2 du 18 avril 2026 — acceptation annoncée au seul champ *Comments* (« MLSys 2026 »), non confirmée en notice.
163. Viktor Strate Kløvedal, Dan Plyukhin *et al.*. « Accompanist: A Runtime for Resilient Choreographic Programming ». [arXiv:2603.20942v1](https://arxiv.org/abs/2603.20942), déposée le 21 mars 2026 — **prépublication non révisée par les pairs** — le champ *Comments* annonce une soumission (« 23 pages, 16 figures, submitted to OOPSLA 2026 »), non une acceptation.
164. Haejoon Lee, Vincent-Daniel Yun *et al.*. « Robust Multi-Agent LLMs under Byzantine Faults ». [arXiv:2605.09076v2](https://arxiv.org/abs/2605.09076), déposée le 9 mai 2026, v2 du 29 juin 2026 — **prépublication non révisée par les pairs**.
165. Frédéric Berdoz, Leonardo Rugli *et al.*. « Can AI Agents Agree? ». [arXiv:2603.01213v2](https://arxiv.org/abs/2603.01213), déposée le 1 mars 2026, v2 du 12 mars 2026 — **prépublication non révisée par les pairs**.
166. Blaž Bertalanič et Carolina Fortuna. « The Ringelmann Effect in Multi-Agent LLM Systems: A Scaling Law for Effective Team Size ». [arXiv:2606.02646v1](https://arxiv.org/abs/2606.02646), déposée le 31 mai 2026 — **prépublication non révisée par les pairs**.
167. Kaixuan Liu, Guojun Xiong *et al.*. « Social Networks of LLM Agents ». [arXiv:2607.03695v1](https://arxiv.org/abs/2607.03695), déposée le 4 juillet 2026 — **prépublication non révisée par les pairs**.
168. Oleksandr Kuznetsov et Emanuele Frontoni. « Width, Memory, and Delay: A Resource Accounting for the Limits of Flat Multi-Agent Systems ». [arXiv:2608.00028v1](https://arxiv.org/abs/2608.00028), déposée le 14 juillet 2026 — **prépublication non révisée par les pairs**.
169. Ahmad Rammal, Niket Patel *et al.*. « Formalizing Mathematics at Scale ». [arXiv:2605.29955v1](https://arxiv.org/abs/2605.29955), déposée le 28 mai 2026 — **prépublication non révisée par les pairs**.
170. Yashaswi Malla et Sandra Siby. « From Monoliths to Swarms: A Study of Attack Surface Evolution in the Transition to Multi-Agent Web Systems ». [arXiv:2608.00202v1](https://arxiv.org/abs/2608.00202), déposée le 31 juillet 2026 — **prépublication non révisée par les pairs**.
171. Shuren Xia, Qiwei Li *et al.*. « TraceFix: Repairing Agent Coordination Protocols with TLA+ Counterexamples ». [arXiv:2605.07935v1](https://arxiv.org/abs/2605.07935), déposée le 8 mai 2026 — **prépublication non révisée par les pairs**.
172. Ruiyang Zhang. « Why Formal Monitors Fail: Attack Distribution Entropy as a Coverage Bound for LTL-Based LLM Agent Safety ». [arXiv:2608.01388v1](https://arxiv.org/abs/2608.01388), déposée le 2 août 2026 — acceptation annoncée au seul champ *Comments* (« 6 pages, 1 figure. Accepted at the 13th IEEE Internat »), non confirmée en notice.
173. Mason Nakamura, Abhinav Kumar *et al.*. « Colosseum: Auditing Collusion in Cooperative Multi-Agent Systems ». [arXiv:2602.15198v2](https://arxiv.org/abs/2602.15198), déposée le 16 février 2026, v2 du 27 mai 2026 — **prépublication non révisée par les pairs**.
174. Institut national des normes et de la technologie (NIST). « Artificial Intelligence Risk Management Framework (AI RMF 1.0) ». NIST AI 100-1, janvier 2023. https://doi.org/10.6028/NIST.AI.100-1
175. H. Garcia-Molina et K. Salem. « Sagas ». *ACM SIGMOD Record*, vol. 16, n° 3, 1987, p. 249-259 — **actes SIGMOD 1987**. https://doi.org/10.1145/38714.38742
176. S. Burckhardt, C. Gillum, D. Justo *et al.* « Durable Functions: Semantics for Stateful Serverless ». *Proceedings of the ACM on Programming Languages*, vol. 5, OOPSLA, 2021 — **comité de lecture**. https://doi.org/10.1145/3485510
177. Marc Alier Forment, María José Casañ Guerrero *et al.*. « The Scaffolding Matters More Than the Interface: A Controlled Comparison of MCP and CLI Tool Use Across Seven Agent Scaffoldings, Five Language Models, and One Software Task ». [arXiv:2608.08654v1](https://arxiv.org/abs/2608.08654), déposée le 9 août 2026 — **prépublication non révisée par les pairs**.
178. Rana Muhammad Ahmed et Sabahat Abbas. « Labels Are Not Endpoints: Treatment Leakage and Construct Validity in MCP Agent Security Evaluation ». [arXiv:2608.12880v1](https://arxiv.org/abs/2608.12880), déposée le 13 août 2026 — **prépublication non révisée par les pairs**.
179. Suraj Kumar, Amy Wang *et al.*. « A Gateway Architecture for Enterprise MCP Authentication: Unifying Heterogeneous Auth, Identity Delegation, and the User / Non-User Persona Problem ». [arXiv:2608.10760v1](https://arxiv.org/abs/2608.10760), déposée le 11 août 2026 — **prépublication non révisée par les pairs**.
180. Varun Pratap Bhardwaj, Garima Singh *et al.*. « Agent Behavioral Contracts II: Certifying Compositional Reliability Without Assuming Independence ». [arXiv:2608.12895v1](https://arxiv.org/abs/2608.12895), déposée le 13 août 2026 — **prépublication non révisée par les pairs**.
181. Shangao Li, Yao Zhang *et al.*. « QuoteBench: How Matched Scores Can Hide Command-Path Failures ». [arXiv:2608.13547v1](https://arxiv.org/abs/2608.13547), déposée le 13 août 2026 — **prépublication non révisée par les pairs**.
182. Jesus Salas. « Correct Is Not Governed: Provenance Integrity in Agentic Workflows ». [arXiv:2608.12761v1](https://arxiv.org/abs/2608.12761), déposée le 13 août 2026 — **prépublication non révisée par les pairs**.
183. Minhan Cho, Soyoung Park *et al.*. « LLM within MCP Matters: Measuring Inefficient Resource Utilization Driven by LLMs ». [arXiv:2608.08467v1](https://arxiv.org/abs/2608.08467), déposée le 9 août 2026 — acceptation annoncée au seul champ *Comments* (« 4 pages, 1 table. Accepted at the AgentSearch Workshop »), non confirmée en notice.
184. Zixing Chen, Xingyuan Liu *et al.*. « REDAgentBench: Executable Red Teaming and Faithful Measurement of LLM Agent Systems ». [arXiv:2608.10669v1](https://arxiv.org/abs/2608.10669), déposée le 11 août 2026 — **prépublication non révisée par les pairs**.
185. Sanjay Kariyappa, Severin Klingler *et al.*. « PIPES: Securing Agent Perception with Provenance and Priors ». [arXiv:2608.12789v1](https://arxiv.org/abs/2608.12789), déposée le 13 août 2026 — **prépublication non révisée par les pairs**.
186. Guodong Xu. « Governed Persistent Memory: Source-Bound State Semantics and Fail-Closed Release for Long-Horizon Agents ». [arXiv:2608.12476v1](https://arxiv.org/abs/2608.12476), déposée le 12 août 2026 — **prépublication non révisée par les pairs**.
187. Shuyu Jiang, Yue Ran *et al.*. « ASCon: A Direction-Aware Reciprocal Agent--Step Contextualization Model for Failure Attribution in Multi-Agent Systems ». [arXiv:2608.10646v1](https://arxiv.org/abs/2608.10646), déposée le 11 août 2026 — **prépublication non révisée par les pairs**.
188. Scott E. Frias. « Similarity Gates Approve Reversals: A Validity Audit of Embedding-Cosine Thresholds in Agent Systems ». [arXiv:2608.10216v1](https://arxiv.org/abs/2608.10216), déposée le 10 août 2026 — **prépublication non révisée par les pairs**.
189. Yiqi Wang, Zihao Yan *et al.*. « MAP-Graph: Provenance-Aware Shared Memory for Multi-Agent Workflows ». [arXiv:2608.10509v1](https://arxiv.org/abs/2608.10509), déposée le 11 août 2026 — **prépublication non révisée par les pairs**.
190. Vasundra Srinivasan. « Deployment Decision Reliability: A Generalizability-Theory Framework for Sizing Long-Horizon Agent Evaluations ». [arXiv:2608.11323v1](https://arxiv.org/abs/2608.11323), déposée le 11 août 2026 — **prépublication non révisée par les pairs**.
191. Henry Han. « Governing Agentic AI in FinTech ». [arXiv:2608.11344v2](https://arxiv.org/abs/2608.11344), déposée le 11 août 2026, v2 du 13 août 2026 — **prépublication non révisée par les pairs**.
192. Abdullah X. « Multi-Agent AI Safety as an Institutional Design Problem ». [arXiv:2608.09828v1](https://arxiv.org/abs/2608.09828), déposée le 10 août 2026 — **prépublication non révisée par les pairs**.
:::
