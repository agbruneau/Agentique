// Gabarit « arXiv preprint » (d'après arxiv.sty, G. Kour) porté en Typst.
// Colonne unique, New Computer Modern, bandeau de résumé encadré de filets,
// titre courant « PRÉPUBLICATION — <date> » à partir de la page 2.

#let arxiv(
  titre: [],
  auteurs: (),
  date: [],
  resume: [],
  motscles: (),
  corps,
) = {
  set document(
    title: titre,
    author: auteurs.map(a => a.nom),
    keywords: motscles,
    description: "Prépublication.",
  )

  set page(
    paper: "us-letter",
    margin: (x: 1in, y: 1in),
    header: context {
      if counter(page).get().first() > 1 {
        set text(size: 8pt, tracking: 0.4pt)
        smallcaps[Prépublication — #date]
        v(-0.7em)
        line(length: 100%, stroke: 0.5pt)
      }
    },
    footer: context {
      align(center, text(size: 9pt, str(counter(page).get().first())))
    },
  )

  set text(font: "New Computer Modern", size: 10pt, lang: "fr", region: "CA")
  set par(justify: true, leading: 0.62em, spacing: 0.95em, first-line-indent: 0pt)
  set heading(numbering: "1.1")
  show heading: set block(above: 1.3em, below: 0.7em, sticky: true)
  show heading.where(level: 1): set text(size: 12pt)
  show heading.where(level: 2): set text(size: 10.5pt)
  show heading.where(level: 3): set text(size: 10pt, style: "italic")
  show link: set text(fill: rgb("#1a4f8a"))
  // Taille relative : un extrait de code hérite du corps qui l'entoure, ce qui
  // évite qu'un libellé de figure en 6,3 pt porte du code en 8,5 pt.
  show raw: set text(font: "DejaVu Sans Mono", size: 0.85em)
  show raw.where(block: true): set text(size: 8pt)
  show raw.where(block: true): it => block(
    width: 100%, fill: luma(96%), inset: 7pt, radius: 2pt, it,
  )

  set table(
    stroke: (x, y) => if y == 0 { (bottom: 0.6pt + black) }
                      else { (bottom: 0.3pt + luma(65%)) },
    inset: (x: 5pt, y: 4pt),
  )
  show table: set text(size: 8.5pt)
  show table: set par(justify: false, leading: 0.5em)
  show table.cell.where(y: 0): strong
  show figure: set block(breakable: true)
  show figure.caption: set text(size: 8.5pt)
  set figure.caption(separator: [ — ])

  // ---- Bloc de titre -------------------------------------------------
  align(center)[
    #block(width: 100%)[#text(size: 17pt)[#titre]]
    #v(1.2em)
    #grid(
      columns: (1fr,) * calc.min(auteurs.len(), 3),
      column-gutter: 1.5em,
      ..auteurs.map(a => align(center)[
        #text(size: 11pt, weight: "bold")[#a.nom] \
        // L'affiliation est facultative : un auteur sans rattachement n'a pas
        // de ligne vide à sa place.
        #let aff = a.at("affiliation", default: none)
        #if aff != none [#text(size: 9pt, style: "italic")[#aff] \ ]
        #text(size: 9pt, font: "DejaVu Sans Mono")[#a.courriel]
      ])
    )
    #v(0.6em)
    #text(size: 9.5pt)[#date]
  ]

  // ---- Résumé --------------------------------------------------------
  v(1.4em)
  line(length: 100%, stroke: 0.6pt)
  v(0.3em)
  align(center, text(size: 10pt, tracking: 1.2pt)[#smallcaps[Résumé]])
  v(0.2em)
  pad(x: 0.4in, text(size: 9.5pt)[#resume])
  v(0.4em)
  line(length: 100%, stroke: 0.6pt)
  v(0.6em)
  pad(x: 0.4in, text(size: 9.5pt)[
    *Mots-clés* — #motscles.join(" · ")
  ])
  v(1.2em)

  corps
}
