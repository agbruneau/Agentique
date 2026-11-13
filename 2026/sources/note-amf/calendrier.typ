#import "gabarit.typ": *

// Figure du § 12 : calendrier indicatif 2026-2027. Abscisse en mois depuis le
// 1er décembre 2026 (0) jusqu'au 31 décembre 2027 (13).
#let calendrier() = {
  let mois = ("déc.", "janv.", "févr.", "mars", "avr.", "mai", "juin", "juil.", "août", "sept.", "oct.", "nov.", "déc.")
  let gris-jalon = rgb("#a9b1bb")
  let lignes = (
    // (libellé, sorte, début, fin, étiquette, côté de l'étiquette)
    ("Phase Fondations", "barre", 0, 3.47, "1er déc. à mi-mars", none),
    ("Jalon J1", "jalon", 3.47, none, "mi-mars", right),
    ("Phase Plateforme", "barre", 3.47, 10.0, "mi-mars à fin sept.", none),
    ("J-AMF : LD IA et E-23", "amf", 5.0, none, "1er mai", right),
    ("Migration MCP", "jalon", 7.87, none, "28 juil.", right),
    ("Jalon J2", "jalon", 10.1, none, "début oct.", left),
    ("Jalon J2a (RIA)", "jalon", 11.0, none, "au plus tard le 1er nov.", left),
    ("RIA, annexe III", "jalon", 12.03, none, "2 déc.", left),
  )
  let lw = 118pt
  let tw = 344pt
  let rh = 19pt
  let haut = 30pt
  let x(m) = lw + tw * m / 13
  let total = haut + lignes.len() * rh
  set text(font: sans, size: 7.5pt)
  set par(justify: false)
  figure(kind: image, supplement: [Figure],
    alt: "Calendrier 2026-2027 : phase Fondations du 1er décembre 2026 à la mi-mars 2027, jalon J1 à la mi-mars 2027, phase Plateforme de la mi-mars à la fin septembre 2027, jalon J-AMF (ligne directrice IA de l'AMF et E-23) au 1er mai 2027, migration MCP au 28 juillet 2027, jalon J2 début octobre 2027, jalon J2a (RIA) au plus tard le 1er novembre 2027 et annexe III du RIA au 2 décembre 2027.",
    caption: [Calendrier 2026-2027 · 2 phases, 6 jalons],
    align(left, block(width: 100%, {
      text(size: 9.5pt, weight: "semibold")[L'AMF prend effet six à sept semaines après J1, en pleine phase Plateforme]
      linebreak()
      text(size: 7.5pt, fill: gris)[Calendrier indicatif du cadre (tableau 59), mois 0 au 1er décembre 2026]
      v(6pt)
      box(width: 100%, height: total + 4pt, {
        // quadrillage et mois
        for i in range(14) {
          place(dx: x(i), dy: haut - 4pt, line(angle: 90deg, length: total - haut + 4pt, stroke: 0.4pt + filet))
        }
        for (i, m) in mois.enumerate() {
          place(dx: x(i), dy: 11pt, box(width: tw / 13, align(center, text(fill: gris, m))))
        }
        place(dx: x(0), dy: 0pt, box(width: tw / 13, align(center, text(fill: gris)[2026])))
        place(dx: x(1), dy: 0pt, box(width: tw / 13, align(center, text(fill: gris)[2027])))
        // 1er mai 2027 : trait pointillé
        place(dx: x(5), dy: haut - 4pt, line(angle: 90deg, length: total - haut + 4pt,
          stroke: (paint: accent, thickness: 0.9pt, dash: "dashed")))
        for (k, (lib, sorte, a, b, etiq, cote)) in lignes.enumerate() {
          let y = haut + k * rh
          let amf = sorte == "amf"
          place(dx: 0pt, dy: y + 5pt, text(weight: if amf { "bold" } else { "regular" }, lib))
          if sorte == "barre" {
            place(dx: x(a), dy: y + 3pt, rect(width: x(b) - x(a), height: rh - 6pt, radius: 6pt,
              fill: accent-pale, stroke: 0.5pt + accent.lighten(40%),
              inset: (x: 6pt, y: 0pt), align(horizon, text(size: 7pt, etiq))))
          } else {
            let c = if amf { accent } else { gris-jalon }
            let d = if amf { 7.5pt } else { 6pt }
            place(dx: x(a) - d / 2, dy: y + rh / 2 - d / 2 - 1pt,
              rotate(45deg, rect(width: d, height: d, fill: c, stroke: 0.5pt + white)))
            let t = text(size: 7pt, weight: if amf { "bold" } else { "regular" }, etiq)
            if cote == right {
              place(dx: x(a) + 7pt, dy: y + 5pt, t)
            } else {
              place(dx: x(a) - 7pt - 140pt, dy: y + 5pt, box(width: 140pt, align(right, t)))
            }
          }
        }
      })
    })))
}
