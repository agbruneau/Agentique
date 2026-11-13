// Gabarit unique du Compendium maître (modèle pandoc pour Typst).
#let marine = rgb("#14233f")
#let bleu = rgb("#2f5fd0")
#let gris = luma(95)

#set document(
  title: "$titre$ — Compendium 2027",
  keywords: ("entreprise agentique", "interopérabilité", "orchestration", "MCP", "A2A", "gouvernance de l'IA"),
)
#set text(font: "Libertinus Serif", size: 10.3pt, lang: "fr", region: "CA")
#set par(justify: true, leading: 0.6em, spacing: 0.88em)
// Apostrophes courbes; guillemets doubles droits laissés tels quels.
#set smartquote(quotes: (single: auto, double: "\"\""))
#set terms(hanging-indent: 1.5em)
#set list(indent: 0.6em, body-indent: 0.5em)
#set enum(indent: 0.6em, body-indent: 0.5em)

#let horizontalrule = align(center, line(length: 40%, stroke: 0.4pt + luma(140)))

$if(highlighting-definitions)$
$highlighting-definitions$
$endif$

#set page(
  width: 17cm,
  height: 24cm,
  margin: (x: 1.8cm, top: 2.1cm, bottom: 2cm),
  header: context {
    let p = here().page()
    let debuts = query(heading.where(level: 1).or(heading.where(level: 2)))
      .filter(h => h.location().page() == p)
    if p > 1 and debuts.len() == 0 {
      let chapitres = query(selector(heading.where(level: 2)).before(here()))
      if chapitres.len() > 0 {
        set text(size: 8.5pt, fill: gris)
        align(right, emph(chapitres.last().body))
        v(-0.6em)
        line(length: 100%, stroke: 0.3pt + luma(170))
      }
    }
  },
  footer: context {
    if here().page() > 1 {
      align(center, text(size: 9pt, counter(page).display("1")))
    }
  },
)

// ----------------------------------------------------------------- titres
// Partie (1) et chapitre (2) sont posés par #partie et #chapitre : le titre
// complet reste un vrai titre, invisible, pour les signets, la table des
// matières et l'en-tête courant.
#show heading: set par(justify: false)
#show heading.where(level: 1): it => it.body
#show heading.where(level: 2): it => it.body
#show heading.where(level: 3): it => block(
  above: 1.6em, below: 0.8em, text(size: 12.5pt, weight: "bold", fill: marine, it.body))
#show heading.where(level: 4): it => block(
  above: 1.3em, below: 0.7em, text(size: 10.5pt, weight: "bold", it.body))
#show heading.where(level: 5): it => block(
  above: 1.2em, below: 0.6em, text(size: 10pt, weight: "bold", style: "italic", it.body))
#show <volet>: it => it.body

#let surtitre(t) = text(size: 8.5pt, weight: "bold", fill: bleu, tracking: 1.5pt, upper(t))

#let partie(sur, titre, chapitres) = {
  pagebreak(weak: true)
  place(hide(heading(level: 1, if titre == none { sur } else [#sur — #titre])))
  set par(justify: false)
  v(4.5cm)
  if titre != none { surtitre(sur) }
  v(0.25cm)
  text(size: 23pt, weight: "bold", fill: marine, if titre == none { sur } else { titre })
  v(0.1cm)
  line(length: 2.6cm, stroke: 1.6pt + bleu)
  v(0.9cm)
  set text(size: 9.8pt, fill: gris)
  set par(leading: 0.5em, spacing: 0.7em)
  for c in chapitres { par(c) }
}

#let chapitre(sur, titre) = {
  pagebreak(weak: true)
  place(hide(heading(level: 2)[#sur — #titre]))
  set par(justify: false)
  v(0.5cm)
  surtitre(sur)
  v(0.15cm)
  text(size: 18pt, weight: "bold", fill: marine, titre)
  v(0.15cm)
  line(length: 2.6cm, stroke: 1.6pt + bleu)
  v(0.7cm)
}

// Volet « Mise en œuvre » d'un chapitre : nouvelle page, bandeau distinct.
#let volet(titre) = {
  // Le volet s'enchaîne sans saut de page; son bandeau ne reste pas seul en bas de page.
  set par(justify: false)
  block(width: 100%, above: 1.2cm, below: 1.3em, breakable: false, sticky: true, {
    // Le titre invisible voyage avec le bandeau : le signet tombe sur la bonne page.
    place(hide[#heading(level: 3)[Mise en œuvre — #titre] <volet>])
    surtitre[Mise en œuvre]
    v(0.2cm)
    text(size: 14pt, weight: "bold", fill: marine, titre)
    v(0.25cm)
    line(length: 100%, stroke: 0.8pt + bleu)
  })
}

// --------------------------------------------------------------- encadrés
#let genres = (
  executive: ("Synthèse exécutive", marine),
  filrouge: ("Fil rouge — Groupe Boréal", rgb("#2c6b58")),
  adr: ("Décision d’architecture", rgb("#5a3e8f")),
  sectoriel: ("Éclairage sectoriel", rgb("#8a5a12")),
  important: ("Important", rgb("#9c2f2f")),
  warning: ("Avertissement", rgb("#9c2f2f")),
  tip: ("Conseil", rgb("#2c6b58")),
  note: ("Note", marine),
)
#let encadre(genre, titre, corps) = {
  let (libelle, couleur) = genres.at(genre, default: genres.note)
  block(
    width: 100%, breakable: true, above: 1.3em, below: 1.3em,
    fill: luma(247), stroke: (left: 2.2pt + couleur),
    inset: (left: 0.9em, right: 0.8em, top: 0.7em, bottom: 0.75em),
    {
      set text(size: 9.6pt)
      set par(leading: 0.56em, spacing: 0.8em)
      text(size: 7.8pt, weight: "bold", fill: couleur, tracking: 1.2pt, upper(libelle))
      if titre != "" {
        v(-0.25em)
        par(justify: false, text(weight: "bold", titre))
      }
      v(-0.1em)
      corps
    },
  )
}

// ------------------------------------- tableaux, figures, code, citations
#set table(
  inset: (x: 4pt, y: 4.5pt),
  stroke: (_, y) => if y > 0 { (top: 0.3pt + luma(170)) },
)
#show table: set text(size: 8.4pt, hyphenate: true)
#show table: set par(justify: false, leading: 0.5em)
#show table.cell.where(y: 0): set text(weight: "bold")
#show figure: set block(breakable: true)
#show figure.where(kind: table): set figure.caption(position: top)
#show figure.where(kind: image): set image(width: 100%)
#show figure.where(kind: image): set block(above: 1.4em, below: 1.4em)
#show figure.caption: set text(size: 8.8pt, fill: gris)
#set math.equation(numbering: none)
// Une formule plus large que la colonne est réduite pour y tenir.
#show math.equation.where(block: true): it => layout(place => {
  let largeur = measure(it).width
  if largeur > place.width {
    align(center, scale(place.width / largeur * 100%, reflow: true, it))
  } else {
    it
  }
})

#show raw: set text(font: "DejaVu Sans Mono", size: 8.3pt)
// Un jeton trop long pour la ligne (signature, adresse) peut se couper.
#show raw.where(block: true): it => block(
  width: 100%, fill: luma(245), inset: 8pt, radius: 2pt, breakable: true,
  {
    show regex("[^ ]{36}"): m => { m; "\u{200B}" }
    text(size: 7.6pt, it)
  })
// Dans un tableau, un identifiant peut se couper après un séparateur ou entre deux mots collés.
#let cesure(corps) = {
  show regex("[_./:=]"): m => { m; "\u{200B}" }
  show regex("[a-z][A-Z]"): m => { let t = m.text; t.at(0) + "\u{200B}" + t.at(1) }
  corps
}
#show table: it => { show raw.where(block: false): cesure; it }
#show quote.where(block: true): it => block(
  width: 100%,
  inset: (left: 0.9em, right: 0.4em, y: 0.5em),
  stroke: (left: 2pt + luma(170)),
  text(size: 9.6pt, it.body),
)
#show link: set text(fill: rgb("#1a3d7c"))

// -------------------------------------------------------------- liminaire
#page(header: none, footer: none)[
  #set par(justify: false)
  #line(length: 100%, stroke: 3pt + marine)
  #v(3.2cm)
  #surtitre[Compendium 2027]
  #v(0.5cm)
  #text(size: 27pt, weight: "bold", fill: marine)[Interopérabilité et Orchestration \ en Entreprise Agentique]
  #v(0.6cm)
  #text(size: 13pt, fill: gris)[Protocoles, sémantique, orchestration, architecture, confiance et gouvernance]
  #v(1fr)
  #text(size: 10.5pt)[$edition$]
  #v(0.3cm)
  #line(length: 100%, stroke: 1.5pt + bleu)
]

#page[
  #set text(size: 10pt)
  #let titre2(t) = block(above: 1.05em, below: 0.6em, text(size: 12pt, weight: "bold", fill: marine, t))
  #text(size: 17pt, weight: "bold", fill: marine)[À propos de cette édition]
  #v(-0.5em)
  #line(length: 2.6cm, stroke: 1.6pt + bleu)
  #v(0.5em)

  Cet ouvrage réunit en un seul volume deux éditions du Compendium 2027 rédigées séparément~: un exposé de référence, sobre et sourcé, et une édition d'architecture appliquée. Il les présente sous un plan, une numérotation et une mise en page uniques.

  #titre2[Comment l'ouvrage est construit]

  - *L'ouverture* cadre le sujet~: enjeux, parcours de lecture par rôle, échelle d'autonomie L0 à L4, et dossier initial du Groupe Boréal, l'entreprise fictive qui sert de fil rouge.
  - *Cinquante chapitres*, en dix parties. Chacun commence par un exposé de référence~: question directrice, sections numérotées, grille de décision, points à retenir, sources et limites.
  - *$nbvolets$ volets «~Mise en œuvre~»*, répartis dans $nbhotes$ chapitres, prolongent l'exposé~: architecture prescrite, extraits de code, application au Groupe Boréal, décision d'architecture (ADR) et liste de contrôle. Leurs sections continuent la numérotation du chapitre.
  - *La partie X, «~Recherche scientifique~»*, ajoutée aux neuf parties d'origine, regarde l'ouvrage du dehors~: revue de littérature, veille technologique, puis projection de 2027 à 2030 avec étude de marché (chapitres 48 à 50). Ses trois chapitres suivent le gabarit des exposés, sans volet «~Mise en œuvre~».
  - *Huit annexes*~: glossaire, fiches protocoles, grilles d'évaluation, chronologie et bibliographie (A à E); registre des décisions d'architecture, listes de contrôle d'homologation et index des standards (F à H).

  #titre2[Conventions]

  - *Renvois.* «~Chapitre 14~» et «~section 14.2~» désignent toujours la numérotation de ce volume.
  - *Sources.* Les numéros entre crochets renvoient aux sources de l'exposé de référence du chapitre. Les volets «~Mise en œuvre~» ne citent pas de sources.
  - *Fil rouge.* Le cas du Groupe Boréal, fiction située en 2027 et en 2028 et racontée au passé, se lit dans les volets; écrit dans un autre ordre que celui des chapitres, il évoque parfois une étape traitée plus loin.
  - *Dates de référence.* Faits arrêtés au 11 novembre 2026 (chapitres 1 à 47) et au 13 novembre 2026 (partie X).
  - *Plan initial.* Les sections «~Limites~» appellent ainsi le plan de commande de l'ouvrage et son relevé de sources.
  - *Encadrés.* Synthèse exécutive, fil rouge, décision d'architecture, éclairage sectoriel~: chaque genre garde la même présentation dans tout l'ouvrage.

  #titre2[Rapprochement des deux éditions]

  Les volets «~Mise en œuvre~», l'ouverture et les annexes F à H ont été réécrits dans le ton des exposés; ce que l'exposé d'un chapitre établit déjà y est remplacé par un renvoi. Là où un volet contredisait l'exposé, qui est sourcé, il a été corrigé d'après lui. Quand un volet prescrit plus que l'exposé ne retient, ou qu'un extrait de code suit une version antérieure d'un protocole, une phrase le signale. Un audit de publication a ensuite relu tout l'ouvrage et y a porté $nbcorrections$ corrections, consignées dans un registre. Rapprochement et audit ont été faits par des agents sous contrôle automatique, sans relecture humaine intégrale~: des écarts peuvent subsister.
]

// Table des matières : parties, chapitres et volets.
#page[
  #text(size: 17pt, weight: "bold", fill: marine)[Table des matières]
  #v(-0.5em)
  #line(length: 2.6cm, stroke: 1.6pt + bleu)
  #v(0.5em)
  #set par(justify: false)
  #show outline.entry.where(level: 1): it => {
    v(1em, weak: true)
    text(weight: "bold", fill: marine, it)
  }
  // Volets : titre en retrait, sans points de conduite, page à droite.
  #show outline.entry.where(level: 3): it => link(it.element.location(), block(
    inset: (left: 2.2em), above: 0.45em, below: 0.45em,
    grid(
      columns: (1fr, auto), column-gutter: 1em, align: (left, bottom + right),
      text(size: 8.8pt, fill: gris, style: "italic", it.body()),
      text(size: 8.8pt, fill: gris, it.page()),
    )))
  #outline(
    title: none, indent: 1em,
    target: selector(heading.where(level: 1)).or(heading.where(level: 2)).or(<volet>),
  )
]

$body$

#context [#metadata(here().page()) <fin>]
