// Gabarit Typst editorial — Livre 2027 (6.14in x 9.21in, fr-CA)
// Utilise par assemble_livre.py avec pandoc (-f markdown-tex_math_dollars+tex_math_single_backslash -t typst)

#let livre-title = [/* {{TITLE}} */]
#let livre-subtitle = [/* {{SUBTITLE}} */]
#let livre-author = [/* {{AUTHOR}} */]
#let livre-freeze = [/* {{FREEZE_DATE}} */]
#let livre-pub = [/* {{PUB_DATE}} */]
#let livre-license = [/* {{LICENSE_TEXT}} */]

#let horizontalRule = align(center, v(0.5em) + line(length: 36%, stroke: 0.6pt + rgb("#CBD5E1")) + v(0.5em))
#let divider() = horizontalRule

#let extract-plain-text(el) = {
  let raw = if el == none {
    ""
  } else if type(el) == str {
    el
  } else if el == [ ] {
    " "
  } else if type(el) == content and el.func() == smartquote {
    if el.at("double", default: true) { "\"" } else { "’" }
  } else if type(el) == content and el.has("text") {
    el.text
  } else if type(el) == content and el.has("children") {
    if el.children.len() == 0 {
      ""
    } else {
      el.children.map(extract-plain-text).join("")
    }
  } else if type(el) == content and el.has("body") {
    extract-plain-text(el.body)
  } else {
    ""
  }
  if raw == none { "" } else { str(raw) }
}

#let truncate-header-words(s, max-cl) = {
  let cl = s.clusters()
  if cl.len() <= max-cl {
    s
  } else {
    let pref = cl.slice(0, max-cl - 1).join("")
    let parts = pref.split(" ")
    if parts.len() > 1 {
      parts.slice(0, parts.len() - 1).join(" ") + "…"
    } else {
      pref + "…"
    }
  }
}

#let format-running-header(content) = {
  let t = extract-plain-text(content)
  let cl = t.clusters()
  if cl.len() > 54 and t.contains(" : ") {
    let short = t.split(" : ").first()
    truncate-header-words(short, 64)
  } else if cl.len() > 54 and t.contains(" ? ") {
    let short = t.split(" ? ").first() + " ?"
    truncate-header-words(short, 64)
  } else {
    truncate-header-words(t, 64)
  }
}

#set document(
  title: extract-plain-text(livre-title),
  author: extract-plain-text(livre-author),
)

#set page(
  width: 6.14in,
  height: 9.21in,
  margin: (inside: 0.90in, outside: 0.78in, top: 0.92in, bottom: 0.90in),
)

#set text(
  font: ("Libertinus Serif", "Georgia", "Palatino Linotype"),
  size: 10.6pt,
  lang: "fr",
  region: "CA",
  fill: rgb("#111827"),
  hyphenate: true,
)

#set par(
  justify: true,
  leading: 0.78em,
  spacing: 0.96em,
)

// Page de couverture editoriale
#page(
  margin: (x: 0.75in, y: 0.85in),
  fill: rgb("#132238"),
  header: none,
  footer: none,
  numbering: none,
)[
  #set text(fill: white, hyphenate: false)
  #set par(justify: false)
  #v(0.55in)
  #text(
    font: ("Segoe UI", "Libertinus Serif"),
    size: 8.5pt,
    tracking: 0.14em,
    fill: rgb("#F59E0B"),
    weight: "bold",
  )[COLLECTION ARCHITECTURE & GOUVERNANCE AGENTIQUE]
  #v(0.35in)
  #line(length: 2.2in, stroke: 2pt + rgb("#F59E0B"))
  #v(0.35in)
  #text(
    font: ("Libertinus Serif", "Georgia"),
    size: 25pt,
    weight: "bold",
    fill: white,
    hyphenate: false,
  )[#livre-title]
  #v(0.22in)
  #text(
    font: ("Libertinus Serif", "Georgia"),
    size: 12.5pt,
    style: "italic",
    fill: rgb("#CBD5E1"),
    hyphenate: false,
  )[#livre-subtitle]
  #v(1fr)
  #line(length: 100%, stroke: 0.5pt + rgb("#334155"))
  #v(0.2in)
  #grid(
    columns: (1fr, auto),
    align: (left, right),
    [
      #text(font: ("Segoe UI", "Libertinus Serif"), size: 11.5pt, weight: "bold", fill: white)[#livre-author]\
      #v(0.08in)
      #text(size: 8.5pt, fill: rgb("#94A3B8"))[Parution : #livre-pub · Gel des faits : #livre-freeze]
    ],
    [
      #box(
        stroke: 0.75pt + rgb("#F59E0B"),
        inset: (x: 8pt, y: 5pt),
        radius: 2pt,
      )[#text(font: ("Segoe UI", "Libertinus Serif"), size: 8.5pt, fill: rgb("#FDE68A"), weight: "bold")[#livre-license]]
    ],
  )
]

// Page de titre interieure et mentions de reference
#page(
  margin: (x: 0.85in, y: 0.85in),
  header: none,
  footer: none,
  numbering: none,
)[
  #set par(justify: false)
  #set text(hyphenate: false)
  #v(1.2in)
  #align(center)[
    #text(size: 20pt, weight: "bold", fill: rgb("#132238"), hyphenate: false)[#livre-title]
    #v(0.22in)
    #text(size: 11.5pt, style: "italic", fill: rgb("#334155"), hyphenate: false)[#livre-subtitle]
    #v(0.45in)
    #line(length: 1.6in, stroke: 1pt + rgb("#1B365D"))
    #v(0.45in)
    #text(font: ("Segoe UI", "Libertinus Serif"), size: 11pt, weight: "bold", fill: rgb("#111827"))[#livre-author]
  ]
  #v(1fr)
  #box(
    width: 100%,
    fill: rgb("#F8FAFC"),
    stroke: (left: 2pt + rgb("#1B365D")),
    inset: 10pt,
  )[
    #set text(size: 8.4pt, fill: rgb("#334155"), hyphenate: true)
    #set par(leading: 0.52em, spacing: 0.45em)
    *Édition de référence* : #livre-pub. *Date de gel des faits* : #livre-freeze.\
    *Régime de diffusion* : #livre-license (textes et figures); scripts d'assurance qualité sous licence MIT.\
    *Note d'intégrité (`AO-05`)* : ouvrage conçu sur cahier des charges humain, rédigé et vérifié intégralement par chaîne d'agents indépendants sur corpus ouvert haché `SHA-256`. Document de référence architecturale à portée consultative; ne constitue ni un avis juridique, ni une certification actuarielle ou d'audit.
  ]
]

// Table des matieres liminaire
#page(
  header: none,
  footer: none,
  numbering: "i",
)[
  #counter(page).update(1)
  #set par(justify: false)
  #text(font: ("Segoe UI", "Libertinus Serif"), size: 14pt, weight: "bold", fill: rgb("#132238"))[Table des matières]
  #v(0.2in)
  #outline(
    title: none,
    indent: 1.2em,
    depth: 2,
  )
]

// Configuration du corps principal
#set page(
  numbering: "1",
  header: context {
    let pnum = counter(page).get().first()
    let cur-page = here().page()
    let major-sel = heading.where(level: 1).or(heading.where(level: 2))
    let starts-here = query(major-sel).filter(h => {
      let t = extract-plain-text(h.body)
      h.location().page() == cur-page and (h.level == 1 or t.starts-with("Chapitre ") or t.starts-with("Annexe "))
    })
    if pnum <= 1 or starts-here.len() > 0 { return none }

    let majors = query(major-sel.before(here())).filter(h => {
      let t = extract-plain-text(h.body)
      h.level == 1 or t.starts-with("Chapitre ") or t.starts-with("Annexe ")
    })
    let current = if calc.even(pnum) {
      livre-title
    } else if majors.len() > 0 {
      format-running-header(majors.last().body)
    } else {
      livre-title
    }
    set text(font: ("Segoe UI", "Libertinus Serif"), size: 7.8pt, fill: rgb("#64748B"), hyphenate: false)
    set par(justify: false)
    block(
      width: 100%,
      stroke: (bottom: 0.35pt + rgb("#CBD5E1")),
      inset: (bottom: 3pt),
      below: 0pt,
    )[
      #if calc.even(pnum) { align(left, current) } else { align(right, current) }
    ]
  },
  footer: context {
    let pnum = counter(page).get().first()
    align(center, text(font: ("Segoe UI", "Libertinus Serif"), size: 8.5pt, fill: rgb("#475569"))[#pnum])
  },
)
#counter(page).update(1)

// Hierarchie des titres sans veuves ni orphelines ni cesure
#show heading: set text(hyphenate: false)
#show heading: set par(justify: false)
#show heading: set block(sticky: true)

#show heading.where(level: 1): it => {
  pagebreak(weak: true)
  let txt = extract-plain-text(it.body)
  if txt.starts-with("Partie ") or txt.starts-with("Annexes") {
    v(1.4in)
    align(center)[
      #line(length: 2.2in, stroke: 1.5pt + rgb("#B45309"))
      #v(0.25in)
      #text(font: ("Segoe UI", "Libertinus Serif"), size: 16pt, weight: "bold", fill: rgb("#132238"), hyphenate: false)[#it.body]
      #v(0.25in)
      #line(length: 2.2in, stroke: 0.75pt + rgb("#CBD5E1"))
    ]
    pagebreak(weak: true)
  } else {
    block(width: 100%, sticky: true, above: 0.32in, below: 0.14in)[
      #set par(justify: false)
      #text(font: ("Segoe UI", "Libertinus Serif"), size: 15pt, weight: "bold", fill: rgb("#132238"), hyphenate: false)[#it.body]
      #v(0.10in)
      #line(length: 100%, stroke: 0.8pt + rgb("#1B365D"))
    ]
  }
}

#show heading.where(level: 2): it => {
  let txt = extract-plain-text(it.body)
  if txt.starts-with("Chapitre ") or txt.starts-with("Annexe ") {
    pagebreak(weak: true)
    block(width: 100%, sticky: true, above: 0.28in, below: 0.14in)[
      #set par(justify: false)
      #text(font: ("Segoe UI", "Libertinus Serif"), size: 14pt, weight: "bold", fill: rgb("#132238"), hyphenate: false)[#it.body]
      #v(0.08in)
      #line(length: 100%, stroke: 0.7pt + rgb("#1B365D"))
    ]
  } else {
    block(width: 100%, sticky: true, above: 0.20in, below: 0.08in)[
      #set par(justify: false)
      #text(font: ("Segoe UI", "Libertinus Serif"), size: 11.2pt, weight: "bold", fill: rgb("#1B365D"), hyphenate: false)[#it.body]
    ]
  }
}

#show heading.where(level: 3): it => block(width: 100%, sticky: true, above: 0.16in, below: 0.06in)[
  #set par(justify: false)
  #text(font: ("Segoe UI", "Libertinus Serif"), size: 10.2pt, weight: "bold", fill: rgb("#1E293B"), hyphenate: false)[#it.body]
]

#show heading.where(level: 4): it => block(width: 100%, sticky: true, above: 0.12in, below: 0.04in)[
  #set par(justify: false)
  #text(font: ("Segoe UI", "Libertinus Serif"), size: 9.8pt, weight: "bold", style: "italic", fill: rgb("#334155"), hyphenate: false)[#it.body]
]

// Encadres de decision et citations (indivisibles pour eviter orphelins)
#show quote.where(block: true): it => block(
  width: 100%,
  fill: rgb("#F1F5F9"),
  stroke: (left: 2.5pt + rgb("#1B365D")),
  inset: (x: 10pt, y: 8pt),
  radius: (right: 3pt),
  breakable: false,
  above: 0.7em,
  below: 0.7em,
)[
  #set text(size: 9.3pt, fill: rgb("#1E293B"))
  #set par(leading: 0.56em, spacing: 0.55em)
  #it.body
]

// Code inline et blocs de code
#show raw.where(block: false): it => box(
  fill: rgb("#F1F5F9"),
  inset: (x: 3pt, y: 0pt),
  outset: (y: 1.5pt),
  radius: 2pt,
)[#text(font: ("Consolas", "DejaVu Sans Mono"), size: 8.5pt, fill: rgb("#0F172A"))[#it]]

#show raw.where(block: true): it => block(
  width: 100%,
  fill: rgb("#F8FAFC"),
  stroke: 0.5pt + rgb("#CBD5E1"),
  inset: 8pt,
  radius: 3pt,
)[#text(font: ("Consolas", "DejaVu Sans Mono"), size: 8pt, fill: rgb("#0F172A"))[#it]]

// Tableaux responsives bordes sans debordement ni coupure en milieu de ligne
#set table(
  stroke: 0.45pt + rgb("#CBD5E1"),
  inset: (x: 4.5pt, y: 4pt),
  fill: (x, y) => if y == 0 { rgb("#1B365D") } else if calc.odd(y) { rgb("#F8FAFC") } else { white },
)
#set table.cell(breakable: false)
#show figure.where(kind: table): set block(breakable: true, above: 0.9em, below: 1.0em)
#show table: it => block(width: 100%)[
  #set text(font: ("Segoe UI", "Libertinus Serif"), size: 7.4pt, hyphenate: true)
  #set par(justify: false, leading: 0.45em, spacing: 0.30em)
  #show raw.where(block: false): r => text(font: ("Consolas", "DejaVu Sans Mono"), size: 7.0pt, fill: rgb("#0F172A"), r.text)
  #show table.cell.where(y: 0): it => {
    set text(fill: white, weight: "bold")
    show raw.where(block: false): r => text(font: ("Consolas", "DejaVu Sans Mono"), size: 7.0pt, fill: white, r.text)
    it
  }
  #it
]

// Figures vectorielles et matricielles centrees a 96 % max, sans double legende
#show figure.where(kind: image): it => block(
  width: 100%,
  breakable: false,
  sticky: true,
  above: 0.9em,
  below: 0.35em,
  align(center, it.body),
)
#show image: it => layout(avail => {
  let maxw = avail.width * 0.96
  let d = measure(block(width: maxw, { set image(width: 100%); it }))
  let maxh = 5.4in
  let w = if d.height > maxh and d.height > 0pt { maxw * (maxh / d.height) } else { maxw }
  align(center, block(width: w, { set image(width: 100%); it }))
})

/* {{BODY_TYPST}} */