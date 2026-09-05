// Figures de l'article étendu. Toutes produites par l'auteur (ED-4) : aucune
// n'est reprise d'une source. Les structures reprennent les sources Mermaid du
// mémoire (memoire/figures/*.mmd), redessinées en Typst natif.

#import "@preview/fletcher:0.5.8" as fletcher: diagram, node, edge
#import "@preview/cetz:0.4.2"

#let cadre = luma(35%)
#let accent = rgb("#dbe6f3")
#let accent-fort = rgb("#93aecb")
#let env-fill = rgb("#f4efe3")
#let reg-fill = rgb("#e6f0e6")
#let amp-fill = rgb("#f5e4e4")

#let dtext(body, size: 7.5pt, ..rest) = text(size: size, ..rest, body)
#let env-stroke = (dash: "dashed", paint: cadre, thickness: 0.5pt)

// ─────────────────────────────────────────────────────────────────────────────
// Figure 1 — Frontière du système et environnement
// ─────────────────────────────────────────────────────────────────────────────
#let fig-frontiere = {
  set text(size: 7.2pt)
  diagram(
    spacing: (30mm, 5mm),
    node-stroke: 0.5pt + cadre,
    node-corner-radius: 2pt,
    node-inset: 5pt,

    // Système — colonne centrale
    node((0, 0), [Couche d'accès \ #dtext(size: 6.4pt)[point d'entrée unique]],
      width: 40mm, fill: accent),
    node((0, 1), [Orchestration \ #dtext(size: 6.4pt)[décomposition, caractérisation]],
      width: 40mm, fill: accent),
    node((0, 2), [`ORDONNANCEUR` + politique], width: 40mm, fill: accent),
    node((0, 3), [Abstraction matérielle \ #dtext(size: 6.4pt)[`ETAT_RESSOURCE` publié]],
      width: 40mm, fill: accent),
    node((0, 4.3), [`RESSOURCE_CALCUL` \ #dtext(size: 6.4pt)[CPU · GPU · FPGA · QPU]],
      width: 40mm, fill: accent),
    node((-1, 2.6), [Télémétrie et \ journalisation], width: 30mm, fill: accent),

    edge((0, 0), (0, 1), "-|>"),
    edge((0, 1), (0, 2), "-|>"),
    edge((0, 2), (0, 3), "-|>"),
    edge((0, 3), (0, 4.3), "-|>"),
    edge((0, 4.3), (0, 3), "-|>", bend: 42deg, stroke: (dash: "dashed"),
      label: dtext(size: 6.2pt)[état, fidélité], label-side: right),
    edge((0, 2), (-1, 2.6), "-|>", stroke: (dash: "dashed")),
    edge((0, 4.3), (-1, 2.6), "-|>", stroke: (dash: "dashed")),

    node(enclose: ((-1, 2.6), (0, 0), (0, 4.3)), inset: 10pt, stroke: 0.8pt + cadre,
      fill: none, snap: false),
    node((-0.5, -0.95), dtext(size: 7.4pt, weight: "bold")[Système : la plateforme consolidée],
      stroke: none, fill: none),

    // Environnement — colonne droite
    node((1, 0), [Réseau de recherche], width: 34mm, fill: env-fill, stroke: env-stroke),
    node((1, 1.7), [Fournisseur de QPU \
      #dtext(size: 6.4pt)[calendrier, file propre — opaques]],
      width: 34mm, fill: env-fill, stroke: env-stroke),
    node((1, 3), [Service quantique en nuage],
      width: 34mm, fill: env-fill, stroke: env-stroke),
    node((1, 4.1), [Chaîne d'approvisionnement],
      width: 34mm, fill: env-fill, stroke: env-stroke),
    node((1, 5.1), [Centre de calcul hôte],
      width: 34mm, fill: env-fill, stroke: env-stroke),

    edge((1, 0), (0, 0), "-|>", label: dtext(size: 6.2pt)[identité]),
    edge((1, 1.7), (0, 3), "-|>", label: dtext(size: 6.2pt)[gestion]),
    edge((1, 3), (0, 3), "-|>", label: dtext(size: 6.2pt)[API distante]),
    edge((1, 4.1), (0, 4.3), "-|>", label: dtext(size: 6.2pt)[cycle long]),
    edge((1, 5.1), (0, 4.3), "-|>", label: dtext(size: 6.2pt)[hébergement]),

    node((1, -0.95), dtext(size: 7.4pt, weight: "bold")[Environnement — hors frontière],
      stroke: none, fill: none),
  )
}

// ─────────────────────────────────────────────────────────────────────────────
// Figure 2 — Vue fonctionnelle : couches, fonctions et interfaces
// ─────────────────────────────────────────────────────────────────────────────
#let couche(titre, contenu) = [
  #set align(left)
  #dtext(size: 7pt, weight: "bold")[#titre] \
  #dtext(size: 6.7pt)[#contenu]
]

#let fig-fonctionnelle = {
  set text(size: 7.2pt)
  diagram(
    spacing: (14mm, 7mm),
    node-stroke: 0.5pt + cadre,
    node-corner-radius: 2pt,
    node-inset: 6pt,

    node((0, -1), [`UTILISATEUR`], width: 34mm, fill: white),
    edge((0, -1), (0, 0), "-|>", label: dtext(size: 6.5pt)[I1], label-side: right),

    node((0, 0), couche([L1 — Couche d'accès],
      [F1 réception · F16 classification de service · F8 agrégation et restitution]),
      width: 92mm, fill: accent),
    edge((0, 0), (0, 1), "-|>", label: dtext(size: 6.5pt)[I2], label-side: right,
      label-pos: 0.4),

    node((0, 1), couche([L2 — Couche d'orchestration],
      [F2 décomposition en charges · F3 caractérisation]),
      width: 92mm, fill: accent),
    edge((0, 1), (0, 2), "-|>", label: dtext(size: 6.5pt)[I3], label-side: right,
      label-pos: 0.4),

    node((0, 2), couche([L3 — Couche de gestion des ressources],
      [F4 application de la politique · F6 réservation des fenêtres · F7 repli ·
       F9 arbitrage d'équité · F10 comptabilisation]),
      width: 92mm, fill: accent),
    edge((0, 2), (0, 3), "-|>", label: dtext(size: 6.5pt)[I6], label-side: right,
      label-pos: 0.35),

    node((0, 3), couche([L4 — Couche d'abstraction matérielle],
      [*F5 publication de l'état* · F11 estimation de file opaque ·
       F12 adaptation de _backend_]),
      width: 92mm, fill: accent-fort),
    edge((0, 3), (0, 4), "-|>", label: dtext(size: 6.5pt)[I7], label-side: right,
      label-pos: 0.35),

    node((0, 4), [`RESSOURCE_CALCUL` — CPU · GPU · FPGA · QPU], width: 92mm, fill: white),

    // Remontées, routées à gauche pour ne pas croiser la descente
    edge((0, 4), (0, 3), "-|>", bend: 72deg, stroke: 0.7pt,
      label: dtext(size: 6.5pt)[I8], label-side: left, label-pos: 0.88),
    edge((0, 3), (0, 2), "-|>", bend: 62deg, stroke: 1.2pt,
      label: dtext(size: 7.5pt, weight: "bold")[I4], label-side: left, label-pos: 0.55),
    edge((0, 4), (0, 0), "-|>", bend: 80deg, stroke: 0.7pt,
      label: dtext(size: 6.5pt)[I12], label-side: left, label-pos: 0.5),

    // Transverse, à droite
    node((1, 2), couche([L5 — Transverse],
      [F13 journalisation \ F14 télémétrie \ F15 isolation]),
      width: 32mm, fill: env-fill, stroke: env-stroke),
    edge((0, 2), (1, 2), "-|>", label: dtext(size: 6.5pt)[I5]),
    node((1, 4), [Tableaux de bord], width: 32mm, fill: white),
    edge((1, 2), (1, 4), "-|>", label: dtext(size: 6.5pt)[I9], label-side: right),
  )
}

// ─────────────────────────────────────────────────────────────────────────────
// Figure 3 — Position de la projection dans le paysage des interfaces
// ─────────────────────────────────────────────────────────────────────────────
#let fig-projection = {
  set text(size: 7.5pt)
  diagram(
    spacing: (8mm, 7mm),
    node-stroke: 0.6pt + cadre,
    node-corner-radius: 2pt,
    node-inset: 7pt,

    node((0, 0), [Ordonnanceur — placement, files, quotas], width: 82mm, fill: white),
    node((1.3, 0), dtext(size: 7.2pt)[couvert : \ *QRMI*], stroke: none, fill: none),

    edge((0, 1), (0, 0), "-|>",
      label: dtext(size: 7pt)[I4 : `ETAT_RESSOURCE` daté, cinq champs]),

    node((0, 1), [*F5 — Projection de l'état de ressource* \
      #dtext(size: 6.8pt, style: "italic")[non couvert par les interfaces publiées]],
      width: 82mm, fill: accent-fort, stroke: 1.2pt),
    node((1.3, 1), dtext(size: 7.2pt, weight: "bold")[la \ contribution],
      stroke: none, fill: none),

    edge((0, 2), (0, 1), "-|>",
      label: dtext(size: 7pt)[I8 : propriétés changeantes, fidélité vivante]),

    node((0, 2), [Dispositif quantique — étalonnage, dérive], width: 82mm, fill: white),
    node((1.3, 2), dtext(size: 7.2pt)[couvert : \ *QDMI*], stroke: none, fill: none),
  )
}

// ─────────────────────────────────────────────────────────────────────────────
// Figure 4 — Machine d'états du QPU
// ─────────────────────────────────────────────────────────────────────────────
#let fig-etats = {
  set text(size: 7.4pt)
  diagram(
    spacing: (30mm, 24mm),
    node-stroke: 0.7pt + cadre,
    node-corner-radius: 3pt,
    node-inset: 7pt,

    node((1, 0), [`etalonnage`], fill: rgb("#f2ecdc")),
    node((2.2, 0), [`disponible`], fill: rgb("#e2eee4")),
    node((2.2, 1.05), [`degrade`], fill: rgb("#f7f0dd")),
    node((0, 1.05), [`hors_service`], fill: rgb("#f0e2e2")),

    // Retour de service : toujours par etalonnage, jamais par disponible
    edge((0, 1.05), (1, 0), "-|>", bend: 20deg,
      label: dtext(size: 6.5pt)[E6 retour de contact \ E8 remise en service \
        (gardés par la cause)],
      label-pos: 0.5),
    // etalonnage <-> disponible
    edge((1, 0), (2.2, 0), "-|>", bend: 24deg,
      label: dtext(size: 6.5pt)[E2 fin, conforme]),
    edge((2.2, 0), (1, 0), "-|>", bend: 24deg,
      label: dtext(size: 6.5pt)[E1 début], label-pos: 0.24),
    // etalonnage <-> degrade
    edge((1, 0), (2.2, 1.05), "-|>", bend: 14deg,
      label: dtext(size: 6.5pt)[E2 fin, sous seuil], label-pos: 0.28),
    edge((2.2, 1.05), (1, 0), "-|>", bend: 14deg,
      label: dtext(size: 6.5pt)[E1], label-pos: 0.34),
    // disponible <-> degrade
    edge((2.2, 0), (2.2, 1.05), "-|>", bend: 26deg,
      label: dtext(size: 6.5pt)[E3 seuil franchi \ E9 péremption], label-pos: 0.5),
    edge((2.2, 1.05), (2.2, 0), "-|>", bend: 26deg,
      label: dtext(size: 6.5pt)[E4 retour \ sous seuil], label-pos: 0.5),
    // Sorties vers hors_service
    edge((1, 0), (0, 1.05), "-|>", bend: 20deg),
    edge((2.2, 0), (0, 1.05), "-|>", bend: 52deg),
    edge((2.2, 1.05), (0, 1.05), "-|>", bend: -26deg,
      label: dtext(size: 6.5pt)[E5 · E7 \ (depuis les trois états)], label-pos: 0.5),
  )
}

// Figure 5 — Diagramme causal des boucles de rétroaction
// ─────────────────────────────────────────────────────────────────────────────
#let fig-boucles = {
  set text(size: 7pt)
  diagram(
    spacing: (18mm, 15mm),
    node-stroke: 0.5pt + cadre,
    node-corner-radius: 2pt,
    node-inset: 5pt,

    node((0, 0), [dérive de \ fidélité], width: 24mm),
    node((1, 0), [déclenchement \ d'étalonnage], width: 26mm),
    node((2, 0), [occupation par \ l'étalonnage], width: 26mm),
    node((2, 1), [profondeur de \ `FILE_ATTENTE`], width: 26mm),
    node((1, 1), [pic de charge à \ la réouverture], width: 26mm),
    node((3, 1), [éligibilité perçue \ de la ressource], width: 27mm),
    node((3, 2), [placements dirigés \ vers la ressource], width: 27mm),
    node((2, 2), [priorité effective \ du `TENANT`], width: 26mm),
    node((1, 2), [part consommée \ par un `TENANT`], width: 26mm),

    edge((0, 0), (1, 0), "-|>", label: [+]),
    edge((1, 0), (2, 0), "-|>", label: [+]),
    edge((2, 0), (0, 0), "-|>", bend: -38deg, label: [−]),
    edge((2, 0), (2, 1), "-|>", label: [+], label-side: right),
    edge((2, 1), (1, 1), "-|>", label: [+]),
    edge((1, 1), (0, 0), "-|>", label: [+], label-side: right),
    edge((2, 1), (3, 1), "-|>", label: [−]),
    edge((3, 1), (3, 2), "-|>", label: [+], label-side: right),
    edge((3, 2), (2, 1), "-|>", bend: -28deg, label: [+]),
    edge((1, 2), (2, 2), "-|>", label: [−]),
    edge((2, 2), (3, 2), "-|>", label: [+]),
    edge((3, 2), (1, 2), "-|>", bend: 32deg, label: [+], label-side: right),

    node((1.5, 0.42), dtext(size: 6.5pt)[*B1* régulatrice], fill: reg-fill,
      stroke: 0.4pt + cadre),
    node((1.5, 1.42), dtext(size: 6.5pt)[*B2* amplificatrice], fill: amp-fill,
      stroke: 0.4pt + cadre),
    node((2.5, 2.45), dtext(size: 6.5pt)[*B3* régulatrice], fill: reg-fill,
      stroke: 0.4pt + cadre),
    node((3, 1.5), dtext(size: 6.5pt)[*B4* régul.], fill: reg-fill,
      stroke: 0.4pt + cadre),
  )
}

// ─────────────────────────────────────────────────────────────────────────────
// Figure 6 — Flux de la POLITIQUE_DELEGATION
// ─────────────────────────────────────────────────────────────────────────────
#let fig-flux = {
  set text(size: 7pt)
  diagram(
    spacing: (14mm, 7mm),
    node-stroke: 0.5pt + cadre,
    node-corner-radius: 2pt,
    node-inset: 5pt,

    node((0, 0), [Entrées : caractérisation, état de ressource, métrique datée, \
      réservations, estimation de file, quota du tenant], width: 74mm, fill: white),
    edge((0, 0), (0, 1), "-|>"),

    node((0, 1), [*Étape 1* — filtrage d'éligibilité \
      #dtext(size: 6.2pt)[R1 état · R1b péremption · R2 fidélité · R3 fenêtre ·
        R4 quota QPU · R5 faisabilité · R6 confiance]], width: 74mm, fill: accent),
    edge((0, 1), (0, 2), "-|>"),

    node((0, 2), [ensemble éligible \ vide?],
      shape: fletcher.shapes.diamond, width: 44mm, fill: white),
    edge((0, 2), (0, 3), "-|>", label: dtext(size: 6.5pt)[non], label-side: left),
    edge((0, 2), (1, 2), "-|>", label: dtext(size: 6.5pt)[oui]),

    node((0, 3), [*Étape 2* — normalisation min-max des cinq critères \
      sur l'ensemble éligible], width: 74mm, fill: accent),
    edge((0, 3), (0, 4), "-|>"),

    node((0, 4), [*Étape 3* — score pondéré par classe de service \
      #dtext(size: 6.5pt)[$S(r) = sum_k w_k ("classe") dot n_k (r)$]],
      width: 74mm, fill: accent),
    edge((0, 4), (0, 5), "-|>"),

    node((0, 5), [maximum atteint par \ une seule ressource?],
      shape: fletcher.shapes.diamond, width: 50mm, fill: white),
    edge((0, 5), (0, 7), "-|>", label: dtext(size: 6.5pt)[oui], label-side: left),
    edge((0, 5), (0, 6), "-|>", label: dtext(size: 6.5pt)[non]),

    node((0, 6), [*Étape 4* — départage lexicographique total \
      #dtext(size: 6.2pt)[fidélité, puis temps, puis coût, puis identifiant croissant]],
      width: 74mm, fill: accent),
    edge((0, 6), (0, 7), "-|>"),

    node((0, 7), [`DECISION_DELEGATION` \
      #dtext(size: 6.2pt)[ressource · repli · alternatives · confiance · motif · horodatage]],
      width: 74mm, fill: accent-fort),

    // Branche de repli — colonne entière distincte
    node((1, 2), [*Étape 5* — repli], width: 42mm, fill: env-fill),
    edge((1, 2), (1, 3), "-|>"),
    node((1, 3), [cause transitoire, bornée, \ reports < MAX?],
      shape: fletcher.shapes.diamond, width: 44mm, fill: white),
    edge((1, 3), (1, 5), "-|>", bend: 58deg,
      label: dtext(size: 6.2pt)[oui : report borné], label-side: right, label-pos: 0.32),
    edge((1, 3), (1, 5), "-|>",
      label: dtext(size: 6.2pt)[non : rejet motivé], label-side: left, label-pos: 0.68),

    node((1, 5), [sortie de repli], width: 34mm, fill: env-fill),
    edge((1, 5), (0, 7), "-|>"),
  )
}

// ─────────────────────────────────────────────────────────────────────────────
// Figure 7 — Coordination d'une fenêtre d'étalonnage planifiée (PR-01)
// ─────────────────────────────────────────────────────────────────────────────
#let fig-etalonnage = {
  set text(size: 6.8pt)
  let acteurs = (
    (0, [Fournisseur \ PP-006]),
    (1, [Opérateur \ PP-003]),
    (2, [Plateforme \ F5, F6]),
    (3, [Ordonnanceur \ F4]),
    (4, [Utilisateur \ PP-001]),
  )
  let n = 11.6
  diagram(
    spacing: (9mm, 7.5mm),
    node-stroke: 0.5pt + cadre,
    node-corner-radius: 2pt,
    node-inset: 4pt,

    ..acteurs.map(((x, l)) => node((x, 0), l, width: 22mm, fill: accent)),
    ..acteurs.map(((x, _)) => edge((x, 0), (x, n),
      stroke: (dash: "dashed", paint: luma(62%), thickness: 0.4pt))),

    edge((0, 1), (1, 1), "-|>", label: dtext(size: 6.3pt)[annonce de fenêtre]),
    edge((1, 2), (2, 2), "-|>", label: dtext(size: 6.3pt)[inscription auprès de F6]),
    edge((2, 3), (3, 3), "-|>", label: dtext(size: 6.3pt)[I10 — fenêtre sur l'horizon]),
    edge((2, 4), (4, 4), "-|>", label: dtext(size: 6.3pt)[préavis publié (SLO-04)]),
    node((2.5, 5), dtext(size: 6.3pt, style: "italic")[la politique écarte la ressource
      par la règle R3], fill: env-fill, stroke: (dash: "dotted", paint: cadre), inset: 3pt),
    edge((3, 6), (4, 6), "-|>", label: dtext(size: 6.3pt)[report borné]),
    edge((0, 7), (2, 7), "-|>", label: dtext(size: 6.3pt)[E1 début d'étalonnage]),
    edge((2, 8), (3, 8), "-|>", label: dtext(size: 6.3pt)[I4 — `etalonnage` / `planifie`]),
    node((1, 9.2), dtext(size: 6.3pt, style: "italic")[aucun incident ouvert :
      l'étalonnage est un état nominal],
      fill: env-fill, stroke: (dash: "dotted", paint: cadre), inset: 3pt),
    edge((0, 10.4), (2, 10.4), "-|>", label: dtext(size: 6.3pt)[E2 fin + métrique datée]),
    edge((2, 11.6), (3, 11.6), "-|>",
      label: dtext(size: 6.3pt)[I4 — `disponible`, sinon `degrade` → PR-05]),
  )
}

// ─────────────────────────────────────────────────────────────────────────────
// Figure 8 — Chronologie : validité de la métrique, décision, exécution
// ─────────────────────────────────────────────────────────────────────────────
#let fig-chronologie = {
  set text(size: 7.5pt)
  cetz.canvas({
    import cetz.draw: *
    let y = 0
    line((0, y), (12.6, y), mark: (end: "straight"), stroke: 0.6pt)
    content((13.15, y), text(size: 7.5pt)[temps])

    let tick(x, lbl, sub) = {
      line((x, y - 0.16), (x, y + 0.16), stroke: 0.6pt)
      content((x, y + 0.95), text(size: 7.5pt)[#lbl])
      content((x, y - 0.72), text(size: 6.8pt, style: "italic")[#sub])
    }
    tick(1.2, $t_c$, [fin d'étalonnage])
    tick(5.2, $t_d$, [décision])
    tick(8.0, $t_e$, [début d'exécution])
    tick(10.7, $t_v$, [péremption])

    rect((1.2, y + 1.3), (10.7, y + 1.8), fill: reg-fill, stroke: 0.4pt)
    content((5.95, y + 1.55), text(size: 7.2pt)[métrique de fidélité valide])

    rect((5.2, y - 1.95), (8.0, y - 1.45), fill: amp-fill, stroke: 0.4pt)
    content((6.6, y - 1.7), text(size: 7pt)[dérive non observée])

    line((1.2, y + 1.18), (1.2, y + 1.3), stroke: (dash: "dashed", thickness: 0.4pt))
    line((5.2, y - 0.16), (5.2, y - 1.45), stroke: (dash: "dashed", thickness: 0.4pt))
    line((8.0, y - 0.16), (8.0, y - 1.45), stroke: (dash: "dashed", thickness: 0.4pt))
    line((10.7, y + 1.18), (10.7, y + 1.3), stroke: (dash: "dashed", thickness: 0.4pt))

    content((2.6, y - 2.55), text(size: 7pt)[R1b vérifie $t_v > t_d$ — satisfait ici])
    content((10.1, y - 2.55), text(size: 7pt)[E9 se déclenche si $t_e > t_v$])
  })
}
