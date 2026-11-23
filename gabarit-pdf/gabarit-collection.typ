// SPDX-License-Identifier: MIT
// Gabarit Typst editorial partage — Collection Architecture & Gouvernance Agentique
// Fonde sur la charte de reference de 0 - PDF-MD/8 - Manuel.pdf (6.14in x 9.21in, fr-CA).
// Exploitable par tous les volumes du depot (1 a 8+) via #import ou via gabarit-pdf/compile_pdf.py.

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

#let _numbered-chapter-re = regex("^([1-9][0-9]*\\s*·\\s+|[1-9][0-9]*\\s+[A-ZÀ-ÖØ-Þ]|[A-Z]\\s+[A-ZÀ-ÖØ-Þ])")

#let _is-part-divider(txt, part-prefixes) = {
  part-prefixes.any(p => txt.starts-with(p))
}

#let _is-h2-chapter(txt, chapter-prefixes, numbered-h2-chapters) = {
  chapter-prefixes.any(p => txt.starts-with(p)) or (
    numbered-h2-chapters and txt.match(_numbered-chapter-re) != none
  )
}

#let collection-pdf(
  title: [Titre de l'ouvrage],
  subtitle: none,
  author: [André-Guy Bruneau, M.Sc IT],
  collection: [COLLECTION ARCHITECTURE & GOUVERNANCE AGENTIQUE],
  pub-date: none,
  freeze-date: none,
  edition-line: none,
  license-badge: none,
  notice-lines: none,
  diffusion-note: none,
  integrity-note: none,
  show-cover: true,
  show-title-page: true,
  show-toc: true,
  toc-title: [Table des matières],
  toc-depth: 2,
  lang: "fr",
  region: "CA",
  part-prefixes: ("Partie ", "Livre ", "Annexes"),
  chapter-prefixes: ("Chapitre ", "Annexe "),
  numbered-h2-chapters: false,
  breakable-long-code: true,
  code-break-threshold: 40,
  breakable-long-quote: true,
  body,
) = {
  let has-content(val) = val != none and extract-plain-text(val).trim() != ""

  set document(
    title: extract-plain-text(title),
    author: extract-plain-text(author),
  )

  set page(
    width: 6.14in,
    height: 9.21in,
    margin: (inside: 0.90in, outside: 0.78in, top: 0.92in, bottom: 0.90in),
  )

  set text(
    font: ("Libertinus Serif", "Georgia", "Palatino Linotype"),
    size: 10.6pt,
    lang: lang,
    region: region,
    fill: rgb("#111827"),
    hyphenate: true,
  )

  set par(
    justify: true,
    leading: 0.78em,
    spacing: 0.96em,
  )

  // 1. Page de couverture editoriale (identique a 8 - Manuel.pdf)
  if show-cover {
    let cover-meta = if has-content(edition-line) {
      edition-line
    } else if has-content(pub-date) and has-content(freeze-date) {
      [Parution : #pub-date · Gel des faits : #freeze-date]
    } else if has-content(pub-date) {
      [Parution : #pub-date]
    } else if has-content(freeze-date) {
      [Gel des faits : #freeze-date]
    } else {
      none
    }

    page(
      margin: (x: 0.75in, y: 0.85in),
      fill: rgb("#132238"),
      header: none,
      footer: none,
      numbering: none,
    )[
      #set text(fill: white, hyphenate: false)
      #set par(justify: false)
      #v(0.55in)
      #if has-content(collection) [
        #text(
          font: ("Segoe UI", "Libertinus Serif"),
          size: 8.5pt,
          tracking: 0.14em,
          fill: rgb("#F59E0B"),
          weight: "bold",
        )[#collection]
        #v(0.35in)
      ]
      #line(length: 2.2in, stroke: 2pt + rgb("#F59E0B"))
      #v(0.35in)
      #text(
        font: ("Libertinus Serif", "Georgia"),
        size: 25pt,
        weight: "bold",
        fill: white,
        hyphenate: false,
      )[#title]
      #if has-content(subtitle) [
        #v(0.22in)
        #text(
          font: ("Libertinus Serif", "Georgia"),
          size: 12.5pt,
          style: "italic",
          fill: rgb("#CBD5E1"),
          hyphenate: false,
        )[#subtitle]
      ]
      #v(1fr)
      #line(length: 100%, stroke: 0.5pt + rgb("#334155"))
      #v(0.2in)
      #grid(
        columns: if has-content(license-badge) { (1fr, auto) } else { (1fr,) },
        align: if has-content(license-badge) { (left, right) } else { (left,) },
        [
          #text(font: ("Segoe UI", "Libertinus Serif"), size: 11.5pt, weight: "bold", fill: white)[#author]
          #if cover-meta != none [
            \
            #v(0.08in)
            #text(size: 8.5pt, fill: rgb("#94A3B8"))[#cover-meta]
          ]
        ],
        ..if has-content(license-badge) {
          (
            [
              #box(
                stroke: 0.75pt + rgb("#F59E0B"),
                inset: (x: 8pt, y: 5pt),
                radius: 2pt,
              )[#text(font: ("Segoe UI", "Libertinus Serif"), size: 8.5pt, fill: rgb("#FDE68A"), weight: "bold")[#license-badge]]
            ],
          )
        } else {
          ()
        },
      )
    ]
  }

  // 2. Page de titre interieure et encadre de mentions de reference
  if show-title-page {
    let resolved-notice = if notice-lines != none and notice-lines.len() > 0 {
      notice-lines
    } else {
      let auto-lines = ()
      if has-content(pub-date) and has-content(freeze-date) {
        auto-lines.push([*Édition de référence* : #pub-date. *Date de gel des faits* : #freeze-date.])
      } else if has-content(pub-date) {
        auto-lines.push([*Édition de référence* : #pub-date.])
      } else if has-content(freeze-date) {
        auto-lines.push([*Date de gel des faits* : #freeze-date.])
      }
      if has-content(diffusion-note) {
        auto-lines.push(diffusion-note)
      } else if has-content(license-badge) {
        auto-lines.push([*Régime de diffusion* : #license-badge.])
      }
      if has-content(integrity-note) {
        auto-lines.push(integrity-note)
      }
      auto-lines
    }

    page(
      margin: (x: 0.85in, y: 0.85in),
      header: none,
      footer: none,
      numbering: none,
    )[
      #set par(justify: false)
      #set text(hyphenate: false)
      #v(1.2in)
      #align(center)[
        #text(size: 20pt, weight: "bold", fill: rgb("#132238"), hyphenate: false)[#title]
        #if has-content(subtitle) [
          #v(0.22in)
          #text(size: 11.5pt, style: "italic", fill: rgb("#334155"), hyphenate: false)[#subtitle]
        ]
        #v(0.45in)
        #line(length: 1.6in, stroke: 1pt + rgb("#1B365D"))
        #v(0.45in)
        #text(font: ("Segoe UI", "Libertinus Serif"), size: 11pt, weight: "bold", fill: rgb("#111827"))[#author]
      ]
      #v(1fr)
      #if resolved-notice.len() > 0 [
        #box(
          width: 100%,
          fill: rgb("#F8FAFC"),
          stroke: (left: 2pt + rgb("#1B365D")),
          inset: 10pt,
        )[
          #set text(size: 8.4pt, fill: rgb("#334155"), hyphenate: true)
          #set par(leading: 0.52em, spacing: 0.45em)
          #resolved-notice.join(linebreak())
        ]
      ]
    ]
  }

  // 3. Table des matieres liminaire en chiffres romains
  if show-toc {
    page(
      header: none,
      footer: none,
      numbering: "i",
    )[
      #counter(page).update(1)
      #set par(justify: false)
      #text(font: ("Segoe UI", "Libertinus Serif"), size: 14pt, weight: "bold", fill: rgb("#132238"))[#toc-title]
      #v(0.2in)
      #outline(
        title: none,
        indent: 1.2em,
        depth: toc-depth,
      )
    ]
  }

  // 4. Configuration du corps principal (en-tetes courants alternes + pagination arabe)
  set page(
    numbering: "1",
    header: context {
      let pnum = counter(page).get().first()
      let cur-page = here().page()
      let major-sel = heading.where(level: 1).or(heading.where(level: 2))
      let starts-here = query(major-sel).filter(h => {
        let t = extract-plain-text(h.body)
        h.location().page() == cur-page and (
          h.level == 1 or _is-h2-chapter(t, chapter-prefixes, numbered-h2-chapters)
        )
      })
      if pnum <= 1 or starts-here.len() > 0 { return none }

      let majors = query(major-sel.before(here())).filter(h => {
        let t = extract-plain-text(h.body)
        h.level == 1 or _is-h2-chapter(t, chapter-prefixes, numbered-h2-chapters)
      })
      let current = if calc.even(pnum) {
        title
      } else if majors.len() > 0 {
        format-running-header(majors.last().body)
      } else {
        title
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
  counter(page).update(1)

  // 5. Hierarchie des titres sans veuves ni orphelines ni cesure
  show heading: set text(hyphenate: false)
  show heading: set par(justify: false)
  show heading: set block(sticky: true)

  show heading.where(level: 1): it => {
    pagebreak(weak: true)
    let txt = extract-plain-text(it.body)
    if _is-part-divider(txt, part-prefixes) {
      v(1.4in)
      align(center)[
        #line(length: 2.2in, stroke: 1.5pt + rgb("#B45309"))
        #v(0.25in)
        #text(font: ("Segoe UI", "Libertinus Serif"), size: 16pt, weight: "bold", fill: rgb("#132238"), hyphenate: false)[#it.body]
        #v(0.25in)
        #line(length: 2.2in, stroke: 0.75pt + rgb("#CBD5E1"))
      ]
      v(0.28in)
    } else {
      block(width: 100%, sticky: true, above: 0.32in, below: 0.14in)[
        #set par(justify: false)
        #text(font: ("Segoe UI", "Libertinus Serif"), size: 15pt, weight: "bold", fill: rgb("#132238"), hyphenate: false)[#it.body]
        #v(0.10in)
        #line(length: 100%, stroke: 0.8pt + rgb("#1B365D"))
      ]
    }
  }

  show heading.where(level: 2): it => {
    let txt = extract-plain-text(it.body)
    if _is-h2-chapter(txt, chapter-prefixes, numbered-h2-chapters) {
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

  show heading.where(level: 3): it => block(width: 100%, sticky: true, above: 0.16in, below: 0.06in)[
    #set par(justify: false)
    #text(font: ("Segoe UI", "Libertinus Serif"), size: 10.2pt, weight: "bold", fill: rgb("#1E293B"), hyphenate: false)[#it.body]
  ]

  show heading.where(level: 4): it => block(width: 100%, sticky: true, above: 0.12in, below: 0.07in)[
    #set par(justify: false)
    #text(font: ("Segoe UI", "Libertinus Serif"), size: 9.8pt, weight: "bold", style: "italic", fill: rgb("#334155"), hyphenate: false)[#it.body]
  ]

  // 6. Encadres de decision et citations (indivisibles si <= 6.2in, coupure propre au-dela)
  show quote.where(block: true): it => {
    let styled-inner = [
      #set text(size: 9.3pt, fill: rgb("#1E293B"))
      #set par(leading: 0.56em, spacing: 0.55em)
      #show raw.where(block: false): r => highlight(
        fill: white,
        extent: 1pt,
        radius: 2pt,
      )[#text(font: ("Consolas", "DejaVu Sans Mono"), size: 8.2pt, fill: rgb("#0F172A"))[#r]]
      #it.body
    ]
    let render-quote(can-break) = block(
      width: 100%,
      fill: rgb("#F1F5F9"),
      stroke: (left: 2.5pt + rgb("#1B365D")),
      inset: (x: 10pt, y: 8pt),
      radius: (right: 3pt),
      breakable: can-break,
      above: 0.7em,
      below: 0.7em,
    )[#styled-inner]

    if breakable-long-quote {
      layout(avail => {
        let m = measure(width: avail.width, render-quote(false))
        render-quote(m.height > 6.2in)
      })
    } else {
      render-quote(false)
    }
  }

  // 7. Code inline enveloppant proprement et blocs de code (indivisibles <= seuil, coupure propre au-dela)
  show raw.where(block: false): it => highlight(
    fill: rgb("#F1F5F9"),
    extent: 1pt,
    radius: 2pt,
  )[#text(font: ("Consolas", "DejaVu Sans Mono"), size: 8.4pt, fill: rgb("#0F172A"))[#it]]

  show raw.where(block: true): it => {
    let can-break = breakable-long-code and it.lines.len() > code-break-threshold
    block(
      width: 100%,
      fill: rgb("#F8FAFC"),
      stroke: 0.5pt + rgb("#CBD5E1"),
      inset: 5pt,
      radius: 3pt,
      breakable: can-break,
    )[
      #set par(justify: false, leading: 0.48em, spacing: 0.40em)
      #text(font: ("Consolas", "DejaVu Sans Mono"), size: 6.7pt, fill: rgb("#0F172A"))[#it]
    ]
  }

  // 8. Tableaux responsives bordes sans debordement ni coupure en milieu de ligne
  set table(
    stroke: 0.45pt + rgb("#CBD5E1"),
    inset: (x: 3.0pt, y: 3.5pt),
    fill: (x, y) => if y == 0 { rgb("#1B365D") } else if calc.odd(y) { rgb("#F8FAFC") } else { white },
  )
  set table.cell(breakable: false)
  show figure.where(kind: table): set block(breakable: true, above: 0.9em, below: 1.0em)
  show table: it => {
    let ncols = if type(it.columns) == array {
      it.columns.len()
    } else if type(it.columns) == int {
      it.columns
    } else {
      1
    }
    let fsize = if ncols >= 9 { 5.6pt } else if ncols >= 8 { 6.1pt } else { 7.0pt }
    let csize = if ncols >= 9 { 5.1pt } else if ncols >= 8 { 5.6pt } else { 6.5pt }
    block(width: 100%)[
      #set text(font: ("Segoe UI", "Libertinus Serif"), size: fsize, hyphenate: true)
      #set par(justify: false, leading: 0.45em, spacing: 0.30em)
      #show raw.where(block: false): r => text(font: ("Consolas", "DejaVu Sans Mono"), size: csize, fill: rgb("#0F172A"), r.text)
      #show table.cell.where(y: 0): cell => {
        set text(fill: white, weight: "bold")
        show raw.where(block: false): r => text(font: ("Consolas", "DejaVu Sans Mono"), size: csize, fill: white, r.text)
        cell
      }
      #it
    ]
  }

  // 9. Figures vectorielles et matricielles centrees a 96 % max, hauteur plafonnee a 5.4in
  show figure.where(kind: image): it => block(
    width: 100%,
    breakable: false,
    sticky: true,
    above: 0.9em,
    below: 0.35em,
    align(center, it.body),
  )
  show image: it => layout(avail => {
    let maxw = avail.width * 0.96
    let d = measure(block(width: maxw, { set image(width: 100%); it }))
    let maxh = 5.4in
    let w = if d.height > maxh and d.height > 0pt { maxw * (maxh / d.height) } else { maxw }
    align(center, block(width: w, { set image(width: 100%); it }))
  })

  body
}
