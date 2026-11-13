#let annexe-setup(first-page: 1, body) = {
  set page(width: 612pt, height: 792pt,
    margin: (left: 117pt, right: 117pt, top: 72pt, bottom: 72pt),
    footer: context align(center, text(10pt, counter(page).display())),
    footer-descent: 21.6pt)
  counter(page).update(first-page)
  set text(font: "New Computer Modern", size: 11pt, lang: "fr", hyphenate: true)
  set par(justify: true, first-line-indent: (amount: 1.5em, all: false), leading: 0.617em, spacing: 0.603em)
  show heading: set text(weight: "bold")
  show heading.where(level: 1): it => block(above: 23.81pt, below: 8.39pt, text(14pt, it.body))
  show heading.where(level: 2): it => block(above: 20.0pt, below: 6.91pt, text(12.5pt, it.body))
  show heading.where(level: 3): it => block(above: 1.0em, below: 0.62em, text(11pt, it.body))
  show raw: set text(font: "DejaVu Sans Mono", size: 8.8pt)
  body
}

#let legende(num, body) = block(above: 12pt, below: 8pt, inset: (x: 11.4pt),
  text(9pt, par(leading: 0.62em, spacing: 0.62em, first-line-indent: 0pt)[Tableau~#num.~– #body]))

#let tableau(cols, header, ..cells) = {
  set text(9pt)
  set par(justify: false, leading: 0.55em, first-line-indent: 0pt)
  block(width: 100%, breakable: true, table(
    columns: cols, stroke: none, inset: (x: 4pt, y: 3pt), align: left + top,
    table.header(repeat: true, ..header.map(h => h), table.hline(stroke: 1pt)),
    ..cells))
}

#let reference(n, body) = block(above: 0pt, below: 12.5pt, breakable: true,
  grid(columns: (19.6pt, 1fr), column-gutter: 5.46pt,
    align(right, [#n.]),
    par(justify: false, first-line-indent: 0pt, body)))
