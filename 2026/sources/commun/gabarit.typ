// Gabarit commun des livrables du corpus (Typst 0.15.1).
// Format lettre, texte justifié avec césure française, tableaux en sans empattement.

#let encre = rgb("#1b2430")
#let accent = rgb("#1f4e79")
#let accent-pale = rgb("#e8eef5")
#let filet = rgb("#c5ced9")
#let zebre = rgb("#f5f7fa")
#let gris = rgb("#5b6573")
#let serif = ("Libertinus Serif",)
#let sans = ("Selawik",)

#let texte-lien(it) = {
  if it.has("text") { it.text }
  else if it.has("children") { it.children.map(texte-lien).join() }
  else if it.has("body") { texte-lien(it.body) }
  else if it == [ ] { " " }
  else { "" }
}

#let note(titre-court: "", pied: [], body) = {
  set page(
    paper: "us-letter",
    margin: (left: 72pt, right: 72pt, top: 78pt, bottom: 72pt),
    header: context {
      let p = here().page()
      if p <= 1 { return }
      // Chapitre en cours au haut de la page : celui qui s'ouvre dans le premier
      // quart de la page, sinon le dernier ouvert avant elle. Rien sur une page de partie.
      let partie = query(heading.where(level: 1)).any(h => h.location().page() == p)
      let ici = query(heading.where(level: 2)).filter(h =>
        h.location().page() == p and h.location().position().y < 200pt)
      let avant = query(selector(heading.where(level: 2)).before(here()))
      let courant = if partie { none } else if ici.len() > 0 { ici.first().body } else if avant.len() > 0 { avant.last().body }
      set text(font: sans, size: 7.5pt, fill: gris)
      grid(columns: (auto, 1fr), column-gutter: 12pt,
        text(weight: "semibold", fill: accent, titre-court),
        align(right, if courant != none { courant }))
      v(-4pt)
      line(length: 100%, stroke: 0.5pt + filet)
    },
    footer: context {
      if here().page() <= 1 { return }
      set text(font: sans, size: 7.5pt, fill: gris)
      set par(justify: false)
      grid(columns: (1fr, auto), column-gutter: 12pt,
        pied,
        align(right)[Page #counter(page).display() sur #counter(page).final().first()])
    },
  )
  set document(author: "André-Guy Bruneau M.Sc. IT")
  set text(font: serif, size: 10.8pt, lang: "fr", region: "CA", hyphenate: true, fill: encre)
  set par(justify: true, leading: 0.62em, spacing: 0.95em, linebreaks: "optimized")
  set list(indent: 0.4em, body-indent: 0.55em, spacing: 0.75em,
    marker: text(fill: accent, size: 0.8em, baseline: -0.1em, sym.bullet))
  set enum(indent: 0.4em, body-indent: 0.55em, spacing: 0.75em)
  show link: set text(fill: accent)
  // Liens : coupés à leurs barres, points et traits seulement, sans boîtes par mot
  // (qui morcelleraient chaque adresse en dizaines d'annotations PDF). Le trait
  // conditionnel dans « :// » désactive la coupure intra-mot de Typst sur les URL.
  show link: it => {
    if type(it.dest) != str or it.body.func() == raw { return it }
    let u = texte-lien(it.body)
    if u.contains(sym.hyph.soft) or u.contains(" ") or not u.contains("/") { return it }
    let s = (u.replace(sym.zws, "")
      .replace("://", ":" + sym.hyph.soft + "//")
      .replace("/", "/" + sym.zws)
      .replace(".", "." + sym.zws)
      .replace("-", "-" + sym.zws)
      .replace("_", "_" + sym.zws)
      .replace("?", "?" + sym.zws)
      .replace("&", "&" + sym.zws)
      .replace("=", "=" + sym.zws)
      .replace(":" + sym.hyph.soft + "/" + sym.zws + "/", ":" + sym.hyph.soft + "//")
      .trim(sym.zws, at: end))
    link(it.dest, text(hyphenate: false, s))
  }
  show strong: set text(weight: "bold")
  // Symboles forcés sur les polices embarquées (sans repli sur les polices système) :
  // DejaVu Sans Mono pour ⚖, ⚠, ✎ et Inter pour ✓, ✗.
  show regex("[⚖⚠✎]"): set text(font: ("DejaVu Sans Mono",))
  show regex("[✓✗]"): set text(font: ("Inter", "DejaVu Sans Mono"))
  show "⚠": set text(fill: accent)

  // Parties (niveau 1) : page neuve, bandeau.
  show heading.where(level: 1): it => {
    pagebreak(weak: true)
    v(70pt)
    block(width: 100%, below: 36pt, {
      line(length: 42pt, stroke: 2.5pt + accent)
      v(10pt)
      set text(font: sans, size: 22pt, weight: "semibold", fill: accent)
      set par(justify: false, leading: 0.4em)
      it.body
    })
  }
  // Chapitres et annexes (niveau 2).
  show heading.where(level: 2): it => block(above: 26pt, below: 12pt, sticky: true, {
    set text(font: sans, size: 14pt, weight: "semibold", fill: accent)
    set par(justify: false, leading: 0.45em)
    it.body
    v(-6pt)
    line(length: 100%, stroke: 0.6pt + filet)
  })
  show heading.where(level: 3): it => block(above: 18pt, below: 8pt, sticky: true, {
    set text(font: sans, size: 11pt, weight: "semibold", fill: encre)
    set par(justify: false)
    it.body
  })
  show heading.where(level: 4): it => block(above: 12pt, below: 6pt, sticky: true,
    text(font: sans, size: 10pt, weight: "semibold", style: "italic", it.body))
  show heading.where(level: 5): it => block(above: 10pt, below: 5pt, sticky: true,
    text(font: sans, size: 9.5pt, weight: "regular", style: "italic", fill: gris, it.body))

  // Tableaux : en-tête répété, zébrure, texte aligné à gauche (pas de justification
  // dans les cellules étroites).
  show figure.where(kind: table): set block(breakable: true)
  show figure.where(kind: table): set align(left)
  show figure.where(kind: table): set figure(gap: 6pt)
  show figure.where(kind: table): set block(above: 14pt, below: 16pt)
  set table(
    stroke: none,
    inset: (x: 5pt, y: 4.2pt),
    fill: (_, y) => if y == 0 { accent } else if calc.even(y) { zebre },
  )
  set table.hline(stroke: 0.6pt + accent)
  show table: set text(font: sans, size: 8pt)
  show table: set par(justify: false, leading: 0.5em, spacing: 0.6em)
  show table: set list(indent: 0pt, body-indent: 0.4em, spacing: 0.4em)
  show table.cell.where(y: 0): set text(fill: white, weight: "semibold")
  show table: it => block(stroke: (bottom: 0.6pt + filet), it)

  set figure.caption(separator: [ — ])
  show figure.caption: set text(font: sans, size: 8pt, fill: gris)
  body
}

// Fiche signalétique de la couverture : paires rubrique / valeur.
#let fiche(..cellules) = {
  let c = cellules.pos()
  set text(font: sans, size: 8.3pt)
  set par(justify: false, leading: 0.5em)
  block(width: 100%, stroke: (top: 1.2pt + accent, bottom: 0.6pt + filet), inset: (y: 4pt),
    grid(columns: (92pt, 1fr), column-gutter: 12pt, row-gutter: 0pt,
      ..range(0, c.len(), step: 2).map(i => (
        grid.cell(inset: (y: 5.5pt), text(weight: "semibold", fill: accent, c.at(i))),
        grid.cell(inset: (y: 5.5pt), c.at(i + 1)),
      )).flatten()))
}

#let couverture(surtitre: [], titre: [], sous-titre: [], auteur: [], date: [], fiche: []) = page(header: none, footer: none, {
  set par(justify: false)
  v(30pt)
  text(font: sans, size: 8.5pt, weight: "semibold", fill: accent, tracking: 1.2pt,
    upper(surtitre))
  v(14pt)
  line(length: 56pt, stroke: 3pt + accent)
  v(16pt)
  block(text(font: serif, size: 25pt, fill: encre, hyphenate: false, par(leading: 0.42em, titre)))
  v(12pt)
  text(font: serif, size: 14pt, style: "italic", fill: gris, sous-titre)
  v(18pt)
  text(font: sans, size: 9pt)[#text(weight: "semibold", auteur) #h(6pt) · #h(6pt) #date]
  v(1fr)
  fiche
})

#let sommaire() = {
  page(header: none, {
    v(40pt)
    text(font: sans, size: 18pt, weight: "semibold", fill: accent)[Table des matières]
    v(4pt)
    line(length: 100%, stroke: 0.6pt + filet)
    v(10pt)
    set par(justify: false)
    show outline.entry.where(level: 1): it => {
      v(9pt, weak: true)
      text(font: sans, size: 9.5pt, weight: "semibold", fill: accent, it)
    }
    show outline.entry.where(level: 2): set text(font: sans, size: 9pt)
    outline(title: none, depth: 2, indent: 1.2em)
  })
}
