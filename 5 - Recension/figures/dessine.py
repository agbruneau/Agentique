# -*- coding: utf-8 -*-
"""Grave les figures de « État de l'art — services financiers ».

Convention du dépôt : W = 468 unités = 468 pt = 6,5 po — la largeur que
`pad(x: -45pt)` rend aux figures dans le gabarit typst. Une unité vaut un
point : `font-size="8.5"` sort à 8,5 pt sur la page, sans mise à l'échelle.
Ne pas graver à une autre largeur sans régénérer : typst met l'image à
l'échelle du corps et fait tomber les textes sous 7 pt, panne silencieuse.

Sortie SVG, une source pour les deux cibles — typst la rend en texte
vectoriel dans la fonte demandée, le navigateur aussi. La pile de fontes est
Arial d'abord : métriques compatibles Helvetica et Liberation Sans, donc les
mêmes retours de ligne sous Windows, macOS et Linux. Les textes sont coupés à
la main, il n'y a pas de moteur de mesure ici.

Le fond est `#f9f7f7`, exactement le fond du thème clair du HTML : la figure y
disparaît dans la page, s'imprime en tramé chaud très pâle, et reste lisible
en thème sombre où elle se lit comme une planche posée sur la page.

    python figures/dessine.py
"""

import math
import pathlib

W = 468
SANS = "Arial, Helvetica, 'Liberation Sans', sans-serif"

INK = "#1c1a17"
GREY = "#6b6459"
PALE = "#8c857a"
WASH = "#f9f7f7"
RULE = "#ddd8d2"

C = {
    "bleu": dict(line="#1f5c8b", fill="#d9e6f1", deep="#123f5d", soft="#edf3f8"),
    "ambre": dict(line="#a87524", fill="#f6e6cb", deep="#7a5316", soft="#fbf2e4"),
    "vert": dict(line="#2c6e57", fill="#d6e7df", deep="#1d4c3b", soft="#edf4f1"),
    "brique": dict(line="#a8412c", fill="#f4ded7", deep="#7c2e1f", soft="#fbede9"),
    "violet": dict(line="#6b4a86", fill="#e6ddf0", deep="#4c3361", soft="#f3eff8"),
    "gris": dict(line="#8c857a", fill="#e7e3dc", deep="#4f483f", soft="#f2f0ec"),
}


# ── Primitives ─────────────────────────────────────────────────────────────

def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def tw(s, size):
    """Largeur approchée d'une chaîne en Arial. Sert à dimensionner les
    pastilles, pas à composer : le centrage vient de `text-anchor`."""
    u = 0.0
    for ch in s:
        if ch in "il|.,:;'!ïî":
            u += 0.28
        elif ch in "jtfrI()[]{} ":
            u += 0.34
        elif ch in "mw":
            u += 0.83
        elif ch in "MW@%":
            u += 0.90
        elif ch.isupper():
            u += 0.68
        else:
            u += 0.55
    return u * size


def rect(x, y, w, h, fill="none", stroke="none", sw=0.8, rx=0, dash=None, op=None):
    a = f'<rect x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}"'
    if rx:
        a += f' rx="{rx}"'
    a += f' fill="{fill}"'
    if stroke != "none":
        a += f' stroke="{stroke}" stroke-width="{sw}"'
    if dash:
        a += f' stroke-dasharray="{dash}"'
    if op is not None:
        a += f' opacity="{op}"'
    return a + "/>"


def seg(x1, y1, x2, y2, stroke=INK, sw=0.8, dash=None, cap="butt"):
    a = (f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}"'
         f' stroke="{stroke}" stroke-width="{sw}" stroke-linecap="{cap}"')
    if dash:
        a += f' stroke-dasharray="{dash}"'
    return a + "/>"


def circ(cx, cy, r, fill="none", stroke="none", sw=0.8):
    a = f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="{r:.2f}" fill="{fill}"'
    if stroke != "none":
        a += f' stroke="{stroke}" stroke-width="{sw}"'
    return a + "/>"


def txt(x, y, s, size=8.5, fill=INK, anchor="start", weight=None, style=None):
    a = (f'<text x="{x:.2f}" y="{y:.2f}" font-family="{SANS}" font-size="{size}"'
         f' fill="{fill}" text-anchor="{anchor}"')
    if weight:
        a += f' font-weight="{weight}"'
    if style:
        a += f' font-style="{style}"'
    return a + f">{esc(s)}</text>"


def para(x, y, rows, size=7.6, lh=10.0, **kw):
    """Suite de lignes déjà coupées à la main."""
    return "".join(txt(x, y + i * lh, r, size=size, **kw) for i, r in enumerate(rows))


def arrow(x1, y1, x2, y2, color=INK, sw=1.1, head=4.4, dash=None):
    dx, dy = x2 - x1, y2 - y1
    L = math.hypot(dx, dy) or 1.0
    ux, uy = dx / L, dy / L
    bx, by = x2 - ux * head, y2 - uy * head
    px, py = -uy, ux
    k = head * 0.52
    pts = (f"{x2:.2f},{y2:.2f} {bx - px * k:.2f},{by - py * k:.2f} "
           f"{bx + px * k:.2f},{by + py * k:.2f}")
    return (seg(x1, y1, bx, by, color, sw, dash, cap="round")
            + f'<polygon points="{pts}" fill="{color}"/>')


def pill(cx, y, label, col, size=7.0, h=13.0, weight="bold"):
    """Pastille centrée sur cx, coin haut à y."""
    w = tw(label, size) + 12
    c = C[col]
    return (rect(cx - w / 2, y, w, h, fill=c["fill"], stroke=c["line"], sw=0.7, rx=h / 2)
            + txt(cx, y + h * 0.72, label, size=size, fill=c["deep"],
                  anchor="middle", weight=weight))


def svg(h, body, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{h}"'
            f' viewBox="0 0 {W} {h}" role="img">'
            f"<title>{esc(title)}</title>"
            + rect(0, 0, W, h, fill=WASH)
            + body + "</svg>")


# ── Pictogrammes ───────────────────────────────────────────────────────────

def picto_balance(cx, cy, col, s=1.0):
    """Balance — ce qui oblige."""
    c = C[col]["line"]
    g = []
    g.append(seg(cx, cy - 10 * s, cx, cy + 9 * s, c, 1.3, cap="round"))
    g.append(seg(cx - 11 * s, cy - 8 * s, cx + 11 * s, cy - 8 * s, c, 1.3, cap="round"))
    g.append(seg(cx - 6 * s, cy + 9 * s, cx + 6 * s, cy + 9 * s, c, 1.3, cap="round"))
    for d in (-1, 1):
        px = cx + d * 11 * s
        g.append(seg(px, cy - 8 * s, px - 4 * s, cy - 1 * s, c, 0.8))
        g.append(seg(px, cy - 8 * s, px + 4 * s, cy - 1 * s, c, 0.8))
        g.append(seg(px - 4.6 * s, cy - 1 * s, px + 4.6 * s, cy - 1 * s, c, 1.3, cap="round"))
    return "".join(g)


def picto_bulle(cx, cy, col, s=1.0):
    """Bulle de parole — ce qui nomme sans obliger."""
    c = C[col]["line"]
    f = C[col]["fill"]
    g = [rect(cx - 12 * s, cy - 10 * s, 24 * s, 16 * s, fill=f, stroke=c, sw=1.2, rx=3.5)]
    g.append(f'<polygon points="{cx - 4 * s:.2f},{cy + 6 * s:.2f} '
             f'{cx + 2 * s:.2f},{cy + 6 * s:.2f} {cx - 6 * s:.2f},{cy + 11 * s:.2f}"'
             f' fill="{f}" stroke="{c}" stroke-width="1.2" stroke-linejoin="round"/>')
    for i in range(3):
        g.append(circ(cx - 6 * s + i * 6 * s, cy - 2 * s, 1.3 * s, fill=c))
    return "".join(g)


def picto_engrenage(cx, cy, col, s=1.0):
    """Roue dentée — ce qui exécute."""
    c = C[col]["line"]
    f = C[col]["fill"]
    g = []
    for k in range(8):
        a = k * math.pi / 4
        g.append(rect(cx - 1.9 * s, cy - 12 * s, 3.8 * s, 5 * s, fill=c, rx=0.8))
        g[-1] = g[-1].replace("<rect", f'<rect transform="rotate({k * 45} {cx:.2f} {cy:.2f})"')
    g.append(circ(cx, cy, 8.2 * s, fill=f, stroke=c, sw=1.6))
    g.append(circ(cx, cy, 3.0 * s, fill=WASH, stroke=c, sw=1.1))
    return "".join(g)


def picto_serveur(cx, cy, col, s=1.0):
    """Baie — le serveur d'outils partagé."""
    c = C[col]["line"]
    f = C[col]["fill"]
    g = []
    for i in range(3):
        y = cy - 12 * s + i * 9 * s
        g.append(rect(cx - 13 * s, y, 26 * s, 7.2 * s, fill=f, stroke=c, sw=1.0, rx=1.4))
        g.append(circ(cx - 9 * s, y + 3.6 * s, 1.2 * s, fill=c))
        g.append(seg(cx - 5 * s, y + 3.6 * s, cx + 9.5 * s, y + 3.6 * s, c, 0.7))
    return "".join(g)


def vide(cx, cy, r=7.0, col="brique", sw=1.4):
    """Ensemble vide — rien ne porte cette exigence."""
    c = C[col]["line"]
    k = r * 0.72
    return (circ(cx, cy, r, fill="none", stroke=c, sw=sw)
            + seg(cx - k, cy + k, cx + k, cy - k, c, sw, cap="round"))


def croix(cx, cy, r=4.6, col="brique", sw=1.5):
    c = C[col]["line"]
    return (seg(cx - r, cy - r, cx + r, cy + r, c, sw, cap="round")
            + seg(cx - r, cy + r, cx + r, cy - r, c, sw, cap="round"))


# ── F1 — Le décalage central ───────────────────────────────────────────────

def f1():
    g = []
    cols = [
        dict(x=8, col="bleu", picto=picto_balance,
             tete="CE QUI OBLIGE", sous="instruments opposables",
             items=[("E-23 — BSIF", ["1er mai 2027 · inventaire", "d'entreprise des modèles"]),
                    ("LD utilisation de l'IA — AMF", ["1er mai 2027 · imputabilité", "nominative d'un dirigeant"]),
                    ("B-10 · E-21 · B-13 — BSIF", ["tiers, continuité, technologie"])],
             pied=["« agent » et « orchestration »", "n'y figurent pas"]),
        dict(x=160, col="ambre", picto=picto_bulle,
             tete="CE QUI NOMME L'AGENT", sous="descriptions sans force exécutoire",
             items=[("Bulletin IA générative", ["et agentique — BSIF, juillet 2026",
                                                "identités non humaines, chaînage",
                                                "d'outils, points d'approbation"]),
                    ("Directive conjointe", ["Five Eyes — 1er mai 2026",
                                             "définition de l'IA agentique"])],
             pied=["registre des saines pratiques :", "non contraignant"]),
        dict(x=312, col="vert", picto=picto_engrenage,
             tete="CE QUI L'EXÉCUTE", sous="spécifications de projet",
             items=[("MCP  2026-07-28", ["agent → outils · sans état"]),
                    ("A2A  v1.0.1 — 28 mai 2026", ["agent → agent · tâche persistante"]),
                    ("ANP — livre blanc, vnext", ["réseau ouvert · DID W3C"])],
             pied=["aucun attribut de mandat,", "de titulaire ni de révocation"]),
    ]
    CW, CH, TOP = 148, 172, 8
    for d in cols:
        c = C[d["col"]]
        x, cx = d["x"], d["x"] + CW / 2
        g.append(rect(x, TOP, CW, CH, fill=c["soft"], stroke=c["line"], sw=0.9, rx=4))
        g.append(rect(x, TOP, CW, 19, fill=c["line"], rx=4))
        g.append(rect(x, TOP + 12, CW, 7, fill=c["line"]))
        g.append(txt(cx, TOP + 13.4, d["tete"], size=9.0, fill=WASH,
                     anchor="middle", weight="bold"))
        g.append(txt(cx, TOP + 30, d["sous"], size=6.9, fill=c["deep"],
                     anchor="middle", style="italic"))
        g.append(d["picto"](cx, TOP + 51, d["col"], 0.92))
        y = TOP + 74
        for titre, det in d["items"]:
            g.append(txt(x + 9, y, titre, size=7.9, fill=c["deep"], weight="bold"))
            g.append(para(x + 9, y + 9.4, det, size=7.0, lh=8.6, fill=INK))
            y += 9.4 + 8.6 * len(det) + 4.6
        g.append(seg(x + 9, TOP + CH - 24, x + CW - 9, TOP + CH - 24, c["line"], 0.6, dash="2 2"))
        g.append(para(cx, TOP + CH - 14, d["pied"], size=7.0, lh=8.4,
                      fill=c["deep"], anchor="middle", style="italic"))

    # Descente vers la bande du mandat
    BY = 200
    for d in cols:
        g.append(arrow(d["x"] + CW / 2, TOP + CH + 2, d["x"] + CW / 2, BY - 3,
                       C["gris"]["line"], 1.0, 4.0, dash="3 2.5"))

    g.append(rect(8, BY, W - 16, 74, fill=C["brique"]["soft"],
                  stroke=C["brique"]["line"], sw=1.0, rx=4, dash="4 2.5"))
    g.append(txt(W / 2, BY + 15, "LE MANDAT", size=9.0,
                 fill=C["brique"]["deep"], anchor="middle", weight="bold"))
    g.append(txt(W / 2, BY + 26,
                 "pour le compte de qui ?   ·   sous quelle autorisation ?   ·   "
                 "jusqu'à quelle limite ?   ·   révocable comment ?",
                 size=7.4, fill=C["brique"]["deep"], anchor="middle"))
    verdicts = [("ne le nomme pas", "ni l'agent ni l'orchestration"),
                ("ne l'oblige pas", "saines pratiques, non contraignant"),
                ("ne l'exprime pas", "ni mandat, ni titulaire, ni révocation")]
    for d, (v1, v2) in zip(cols, verdicts):
        cx = d["x"] + CW / 2
        g.append(rect(d["x"] + 10, BY + 33, CW - 20, 33, fill=WASH,
                      stroke=C["brique"]["line"], sw=0.7, rx=3, dash="3 2"))
        g.append(vide(cx - 52, BY + 49, 7.2))
        g.append(txt(cx - 40, BY + 46.6, v1, size=7.4,
                     fill=C["brique"]["deep"], weight="bold"))
        g.append(txt(cx - 40, BY + 55.6, v2, size=6.6, fill=GREY))
    return svg(BY + 82, "".join(g), "Le décalage central")


# ── F2 — Trois surveillants, une plateforme à double qualification ─────────

def f2():
    g = []
    reg = [
        dict(x=8, col="bleu", sigle="AMF",
             nom="Autorité des marchés financiers · Québec",
             ent=["198 caisses (Québec)", "Caisse Desjardins Ontario CU",
                  "Fédération des caisses", "Fonds de sécurité Desjardins",
                  "filiales d'assurance de personnes"],
             pied="actif de 510,2 G$ au 31 déc. 2025"),
        dict(x=160, col="vert", sigle="BSIF",
             nom="Bureau du surintendant · Canada",
             ent=["Fiducie Desjardins inc.", "assurance de dommages fédérale",
                  "garde de valeurs", "services fiduciaires"],
             pied="membre de la SADC"),
        dict(x=312, col="violet", sigle="OCRI",
             nom="Organisme canadien de réglementation",
             ent=["Valeurs mobilières", "Desjardins inc."],
             pied="courtier membre"),
    ]
    CW = 148
    for d in reg:
        c = C[d["col"]]
        x, cx = d["x"], d["x"] + CW / 2
        g.append(rect(x, 8, CW, 30, fill=c["line"], rx=4))
        g.append(txt(cx, 22, d["sigle"], size=12.5, fill=WASH,
                     anchor="middle", weight="bold"))
        g.append(txt(cx, 32.5, d["nom"], size=6.5, fill=WASH, anchor="middle"))
        g.append(seg(cx, 38, cx, 48, c["line"], 1.1))
        g.append(rect(x, 48, CW, 74, fill=c["soft"], stroke=c["line"], sw=0.9, rx=4))
        y = 61
        for e in d["ent"]:
            g.append(circ(x + 11, y - 2.6, 1.6, fill=c["line"]))
            g.append(txt(x + 17, y, e, size=7.4, fill=INK))
            y += 10.2
        g.append(txt(cx, 116, d["pied"], size=6.6, fill=c["deep"],
                     anchor="middle", style="italic"))

    g.append(txt(W / 2, 138, "UN SEUL SOCLE TECHNIQUE, TROIS RÉGIMES",
                 size=8.6, fill=GREY, anchor="middle", weight="bold"))
    g.append(seg(8, 145, W - 8, 145, RULE, 0.9))

    # Scène du bas : le même serveur, deux qualifications
    SY = 158
    g.append(rect(174, SY + 14, 120, 62, fill=C["gris"]["fill"],
                  stroke=C["gris"]["line"], sw=1.2, rx=4))
    g.append(picto_serveur(234, SY + 34, "gris", 0.86))
    g.append(txt(234, SY + 60, "un serveur d'outils", size=8.0,
                 fill=C["gris"]["deep"], anchor="middle", weight="bold"))
    g.append(txt(234, SY + 70, "de la plateforme mutualisée", size=6.9,
                 fill=GREY, anchor="middle"))

    g.append(rect(8, SY + 22, 150, 46, fill=C["bleu"]["soft"],
                  stroke=C["bleu"]["line"], sw=0.9, rx=4))
    g.append(txt(83, SY + 36, "L'entité provinciale", size=8.0,
                 fill=C["bleu"]["deep"], anchor="middle", weight="bold"))
    g.append(txt(83, SY + 46, "qui l'exploite", size=8.0,
                 fill=C["bleu"]["deep"], anchor="middle", weight="bold"))
    g.append(txt(83, SY + 58, "régie par l'AMF", size=6.9, fill=GREY, anchor="middle"))

    g.append(rect(310, SY + 22, 150, 46, fill=C["brique"]["soft"],
                  stroke=C["brique"]["line"], sw=0.9, rx=4))
    g.append(txt(385, SY + 36, "L'entité fédérale", size=8.0,
                 fill=C["brique"]["deep"], anchor="middle", weight="bold"))
    g.append(txt(385, SY + 46, "qui le consomme", size=8.0,
                 fill=C["brique"]["deep"], anchor="middle", weight="bold"))
    g.append(txt(385, SY + 58, "régie par le BSIF", size=6.9, fill=GREY, anchor="middle"))

    g.append(arrow(160, SY + 45, 172, SY + 45, C["bleu"]["line"], 1.2, 4.6))
    g.append(arrow(308, SY + 45, 296, SY + 45, C["brique"]["line"], 1.2, 4.6))
    g.append(pill(83, SY, "ACTIF INTERNE", "bleu", size=7.2, h=14))
    g.append(pill(385, SY, "ENTENTE DE TIERS — B-10", "brique", size=7.2, h=14))

    g.append(txt(W / 2, SY + 92, "Le même objet, deux qualifications réglementaires selon l'appelant.",
                 size=8.4, fill=INK, anchor="middle", weight="bold"))
    g.append(txt(W / 2, SY + 103,
                 "B-10 range « parent holding companies, affiliates, and subsidiaries » "
                 "dans les ententes de tiers, sans régime allégé pour l'intragroupe.",
                 size=7.2, fill=GREY, anchor="middle"))
    g.append(txt(W / 2, SY + 113,
                 "La même exécution d'agent change de régime selon l'entité juridique qui l'invoque",
                 size=7.2, fill=GREY, anchor="middle"))
    g.append(txt(W / 2, SY + 123,
                 "— et aucun protocole examiné ne transporte cette entité dans sa trace.",
                 size=7.2, fill=GREY, anchor="middle"))
    return svg(SY + 132, "".join(g), "Trois surveillants, une plateforme à double qualification")


# ── F3 — La fenêtre 2026-2030 ──────────────────────────────────────────────

F3_ROWS = [
    ("20 août 2026", "gel", "Faits arrêtés", [
        "Point de gel du document. Onze jours avant la première échéance prudentielle."]),
    ("24 août 2026", "impose", "DORS/2026-133 — rail de paiement en temps réel", [
        "Un message ne peut être ni modifié ni révoqué après émission.",
        "Le point d'approbation précède donc l'effet ; la compensation après coup n'existe pas.",
        "Aucun champ du portefeuille de messages ne déclare qu'un ordre a été formé par un agent."]),
    ("1er sept. 2026", "impose", "E-21 — BSIF · gestion du risque opérationnel et résilience", [
        "Opérations critiques cartographiées de bout en bout, dépendances aux tiers comprises,",
        "tolérance de perturbation éprouvée par scénarios sévères mais plausibles."]),
    ("31 déc. 2026", "decide", "A1 · A2 · A6 · A7 — les quatre décisions au coût de report asymétrique", [
        "Passerelle d'outils obligatoire · identité non humaine unique par agent ·",
        "registre de mandat en ajout seul · interdiction des conceptions cryptographiques figées.",
        "A2 ne se rattrape pas : un journal produit sous identité partagée ne se ré-attribue pas."]),
    ("31 mars 2027", "decide", "A3 — patron d'orchestration", [
        "Hiérarchique superviseur-travailleur, augmenté du cache sémantique, du routage de",
        "modèle et de la reprise adaptative. Décidé une fois le domaine pilote arrêté."]),
    ("1er avril 2027", "impose", "LD gestion du risque lié aux tiers — AMF", [
        "Cycle de vie des ententes, sous-traitants, responsabilité ultime conservée.",
        "Les ententes intragroupes sont explicitement visées."]),
    ("1er mai 2027", "impose", "E-23 (BSIF) et LD utilisation de l'IA (AMF) — le même jour", [
        "Inventaire d'entreprise permanent des modèles, dont la définition englobe les méthodes d'IA.",
        "Imputabilité nominative d'un membre de la haute direction pour l'ensemble des systèmes d'IA.",
        "Ni « agent » ni « orchestration » ne figurent dans E-23."]),
    ("30 juin 2027", "decide", "A4 · premier relevé d'A5", [
        "Portabilité exigée en démonstration, pas en clause. Premier relevé du taux d'infirmation."]),
    ("30 sept. 2027", "decide", "A5 — décider ou recommander", [
        "Tranché sur la mesure du 30 juin, pas sur le réflexe juridique."]),
    ("2028-2030", "suspend", "S1 · S2 — suspendus sur signal extérieur", [
        "Paiement agentique : règle d'exploitation traitant l'initiation par un mandataire non humain.",
        "Découverte inter-organisationnelle : une fédération d'accréditation réutilisable."]),
    ("après 2030", "suspend", "NIST IR 8547 — brouillon, sans version finale au 20 août 2026", [
        "Dépréciation de RSA-2048 et des courbes P-256 après 2030, interdiction après 2035."]),
]

F3_LANE = {
    "gel": ("gris", "gel"),
    "impose": ("bleu", "ce que le régulateur impose"),
    "decide": ("ambre", "ce que l'institution décide"),
    "suspend": ("violet", "suspendu — signal extérieur"),
}


def f3():
    g = []
    RAIL = 104
    # Légende
    lx = 8
    for k in ("impose", "decide", "suspend"):
        col, lib = F3_LANE[k]
        c = C[col]
        g.append(rect(lx, 8, 9, 9, fill=c["fill"], stroke=c["line"], sw=0.9, rx=2))
        g.append(txt(lx + 14, 15.6, lib, size=7.2, fill=c["deep"]))
        lx += tw(lib, 7.2) + 34
    g.append(seg(8, 25, W - 8, 25, RULE, 0.9))

    y = 36
    nodes = []
    for date, kind, titre, det in F3_ROWS:
        col, _ = F3_LANE[kind]
        c = C[col]
        h = 13 + 9.2 * len(det) + 9
        g.append(rect(RAIL + 12, y - 2, W - 8 - (RAIL + 12), h - 4,
                      fill=c["soft"], stroke=c["line"], sw=0.7, rx=3))
        g.append(rect(RAIL + 12, y - 2, 2.6, h - 4, fill=c["line"]))
        g.append(txt(96, y + 9, date, size=8.2, fill=c["deep"],
                     anchor="end", weight="bold"))
        g.append(txt(RAIL + 21, y + 9, titre, size=8.0, fill=c["deep"], weight="bold"))
        g.append(para(RAIL + 21, y + 19.6, det, size=7.1, lh=9.2, fill=INK))
        nodes.append((y + 6, col, kind))
        y += h + 5

    # Rail vertical + nœuds, tracés après pour passer au-dessus
    g.insert(0, seg(RAIL, 32, RAIL, y - 9, RULE, 2.0))
    for cy, col, kind in nodes:
        c = C[col]
        if kind == "gel":
            g.append(circ(RAIL, cy, 4.4, fill=WASH, stroke=c["line"], sw=1.6))
            g.append(circ(RAIL, cy, 1.6, fill=c["line"]))
        else:
            g.append(circ(RAIL, cy, 4.4, fill=c["line"], stroke=WASH, sw=1.6))
    return svg(y + 4, "".join(g), "La fenêtre 2026-2030")


# ── F4 — Cinq exigences, aucun mécanisme complet ───────────────────────────

F4_COLS = [["Identité", "de l'agent"], ["Mandat", "(pour qui)"],
           ["Atténuation", "prouvée", "par saut"], ["Révocation"],
           ["Preuve", "à cinq ans"]]

F4_STAT = [
    ("vert", "loi en vigueur"),
    ("bleu", "norme ou recommandation publiée"),
    ("ambre", "brouillon avancé"),
    ("brique", "brouillon individuel, zéro adoption"),
    ("gris", "sans statut normatif"),
]

F4_ROWS = [
    ("Échange de jetons — RFC 8693", "norme proposée, 2020", "bleu", "ponpn"),
    ("Jetons de transaction — Txn-Tokens", "document de groupe, dernier appel (-11)", "ambre", "ponpn"),
    ("Chaînage inter-domaines", "soumis à l'IESG, file du RFC Editor (-17)", "ambre", "ponpn"),
    ("Agent Card signée — A2A v1.0", "spécification de projet, stable", "gris", "onnnp"),
    ("Douze brouillons de chaîne de délégation", "brouillons individuels, zéro adoption", "brique", "oopph"),
    ("AuthZEN Authorization API 1.0", "spécification finale OpenID", "bleu", "--o-p"),
    ("Profils AARP et COAZ", "brouillons de groupe de travail", "ambre", "--o-n"),
    ("Justificatifs vérifiables W3C v2.0", "Recommandation W3C, 15 mai 2025", "bleu", "opppp"),
    ("Identité de charge de travail — WIMSE", "architecture adoptée, pratiques en évaluation", "ambre", "opopn"),
    ("Registre d'agents gouverné", "outillage, sans statut normatif", "gris", "pnnpp"),
    ("Système d'archivage fiable — art. 31.2-31.3", "loi en vigueur", "vert", "----o"),
]


def f4_marque(cx, cy, k):
    if k == "o":
        return circ(cx, cy, 4.6, fill=C["vert"]["line"])
    if k == "p":
        c = C["ambre"]["line"]
        return (circ(cx, cy, 4.6, fill=C["ambre"]["fill"], stroke=c, sw=1.2)
                + f'<path d="M {cx:.2f} {cy - 4.6:.2f} A 4.6 4.6 0 0 0 {cx:.2f} '
                  f'{cy + 4.6:.2f} Z" fill="{c}"/>')
    if k in "nh":
        return circ(cx, cy, 4.6, fill=WASH, stroke=C["brique"]["line"], sw=1.2)
    return seg(cx - 3.6, cy, cx + 3.6, cy, PALE, 1.2, cap="round")


def f4():
    g = []
    LX, LW = 8, 196
    n = len(F4_COLS)
    GX, GW = 210, W - 8 - 210
    cw = GW / n
    HY, RH = 8, 19.4

    for i, head in enumerate(F4_COLS):
        cx = GX + cw * (i + 0.5)
        base = HY + 30 - 9.0 * (len(head) - 1)
        for j, ln in enumerate(head):
            g.append(txt(cx, base + j * 9.0, ln, size=6.9, fill=GREY,
                         anchor="middle", weight="bold"))
        if i:
            g.append(seg(GX + cw * i, HY + 4, GX + cw * i, HY + 34 + RH * len(F4_ROWS),
                         RULE, 0.6))
    g.append(seg(LX, HY + 34, W - 8, HY + 34, INK, 1.0))

    y = HY + 34
    for i, (nom, stat, col, cells) in enumerate(F4_ROWS):
        c = C[col]
        if i % 2:
            g.append(rect(LX, y, W - 16, RH, fill="#f1eee9"))
        g.append(rect(LX, y + 3.4, 2.8, RH - 6.8, fill=c["line"], rx=1.2))
        g.append(txt(LX + 8, y + 8.6, nom, size=7.9, fill=INK, weight="bold"))
        g.append(txt(LX + 8, y + 16.4, stat, size=6.7, fill=c["deep"], style="italic"))
        for j, k in enumerate(cells):
            g.append(f4_marque(GX + cw * (j + 0.5), y + RH / 2, k))
        y += RH
    g.append(seg(LX, y, W - 8, y, INK, 1.0))

    # Légendes
    ly = y + 14
    g.append(txt(LX, ly + 4, "Réponse à l'exigence", size=7.0, fill=GREY, weight="bold"))
    lx = LX + 88
    for k, lib in (("o", "oui"), ("p", "partielle"), ("n", "non"), ("-", "sans objet")):
        g.append(f4_marque(lx, ly, k))
        g.append(txt(lx + 8, ly + 2.6, lib, size=7.0, fill=INK))
        lx += tw(lib, 7.0) + 34
    ly += 15
    g.append(txt(LX, ly + 4, "État normatif", size=7.0, fill=GREY, weight="bold"))
    lx = LX + 88
    for col, lib in F4_STAT:
        pas = tw(lib, 6.8) + 24
        if lx + pas > W - 8:          # retour à la ligne, la légende déborderait
            lx, ly = LX + 88, ly + 11
        g.append(rect(lx - 2, ly - 3.6, 2.8, 8, fill=C[col]["line"], rx=1.2))
        g.append(txt(lx + 5, ly + 2.6, lib, size=6.8, fill=C[col]["deep"]))
        lx += pas
    return svg(ly + 14, "".join(g), "Cinq exigences, aucun mécanisme complet")


# ── F5 — L'architecture qui se démontre ────────────────────────────────────

def f5():
    g = []
    # Panneau A — qui invoque qui
    g.append(txt(8, 14, "A.  QUI INVOQUE QUI", size=8.4, fill=GREY, weight="bold"))
    g.append(seg(8, 19, W - 8, 19, RULE, 0.9))

    PX, PY, PW, PH = 8, 28, 336, 204
    g.append(rect(PX, PY, PW, PH, fill=C["bleu"]["soft"],
                  stroke=C["bleu"]["line"], sw=1.3, rx=5))
    g.append(txt(PX + 12, PY + 14, "PÉRIMÈTRE RÉGI DE L'ASSUJETTI", size=7.6,
                 fill=C["bleu"]["deep"], weight="bold"))

    g.append(rect(PX + 12, PY + 22, 222, 38, fill=WASH,
                  stroke=C["bleu"]["line"], sw=1.1, rx=4))
    g.append(txt(PX + 123, PY + 38, "Cadre d'exécution déterministe", size=8.4,
                 fill=C["bleu"]["deep"], anchor="middle", weight="bold"))
    g.append(txt(PX + 123, PY + 51, "BPMN · moteur durable · points d'approbation",
                 size=6.9, fill=GREY, anchor="middle"))

    g.append(arrow(PX + 62, PY + 62, PX + 62, PY + 79, C["bleu"]["line"], 1.3, 4.8))
    g.append(txt(PX + 70, PY + 74, "invoque", size=7.2,
                 fill=C["bleu"]["deep"], weight="bold"))
    g.append(arrow(PX + 190, PY + 82, PX + 190, PY + 60, C["brique"]["line"], 1.1, 4.4,
                   dash="3 2"))
    g.append(circ(PX + 190, PY + 74, 4.6, fill=C["bleu"]["soft"]))
    g.append(croix(PX + 190, PY + 74, 3.8))
    g.append(txt(PX + 182, PY + 74, "jamais l'inverse", size=7.0,
                 fill=C["brique"]["deep"], anchor="end", style="italic"))

    g.append(rect(PX + 12, PY + 82, 222, 46, fill=C["vert"]["soft"],
                  stroke=C["vert"]["line"], sw=0.9, rx=3))
    for i in range(3):
        ax = PX + 24 + i * 70
        g.append(rect(ax, PY + 88, 58, 17, fill=C["vert"]["fill"],
                      stroke=C["vert"]["line"], sw=0.9, rx=3))
        g.append(txt(ax + 29, PY + 100, f"agent {i + 1}", size=7.4,
                     fill=C["vert"]["deep"], anchor="middle", weight="bold"))
    g.append(txt(PX + 123, PY + 116, "Identité non humaine unique par agent", size=7.4,
                 fill=C["vert"]["deep"], anchor="middle", weight="bold"))
    g.append(txt(PX + 123, PY + 124.5,
                 "émission, rotation, révocation, recertification — mandat hors bande",
                 size=6.6, fill=GREY, anchor="middle"))

    g.append(arrow(PX + 123, PY + 130, PX + 123, PY + 140, C["ambre"]["line"], 1.1, 4.4))
    g.append(rect(PX + 12, PY + 142, 222, 52, fill=C["ambre"]["fill"],
                  stroke=C["ambre"]["line"], sw=1.1, rx=3))
    g.append(txt(PX + 22, PY + 155, "Registre de mandat et de décision", size=8.0,
                 fill=C["ambre"]["deep"], weight="bold"))
    g.append(para(PX + 22, PY + 166,
                  ["ajout seul · identité de l'agent, mandat, horodatage,",
                   "entrées déterminantes, effet produit",
                   "propriété non déléguée · conservation cinq ans"],
                  size=6.8, lh=9.0, fill=INK))

    # Passerelle, frontière, extérieur
    g.append(rect(258, PY + 67, 76, 70, fill=C["brique"]["fill"],
                  stroke=C["brique"]["line"], sw=1.2, rx=4))
    for j, w in enumerate(["PASSERELLE", "INTERNE", "OBLIGATOIRE"]):
        g.append(txt(296, PY + 88 + j * 11, w, size=7.4,
                     fill=C["brique"]["deep"], anchor="middle", weight="bold"))
    g.append(txt(296, PY + 124, "sans exception", size=6.8,
                 fill=GREY, anchor="middle", style="italic"))
    g.append(arrow(246, PY + 100, 256, PY + 100, C["bleu"]["line"], 1.2, 4.4))

    FX = 349
    g.append(seg(FX, PY + 6, FX, PY + PH - 6, C["brique"]["line"], 1.3, dash="5 3"))
    g.append(rect(356, PY + 50, W - 8 - 356, 104, fill=C["gris"]["soft"],
                  stroke=C["gris"]["line"], sw=0.9, rx=4, dash="4 2.5"))
    g.append(txt(364, PY + 64, "HORS PÉRIMÈTRE", size=7.4,
                 fill=C["gris"]["deep"], weight="bold"))
    g.append(para(364, PY + 78,
                  ["Serveurs MCP de tiers", "Agents A2A externes",
                   "Registres et places", "de marché ouvertes"],
                  size=6.9, lh=9.4, fill=INK))
    g.append(para(364, PY + 132, ["protocoles ouverts", "à la frontière,",
                                  "et là seulement"],
                  size=6.6, lh=8.6, fill=C["gris"]["deep"], style="italic"))
    g.append(arrow(336, PY + 92, 354, PY + 92, C["brique"]["line"], 1.1, 4.2))
    g.append(arrow(354, PY + 110, 336, PY + 110, C["brique"]["line"], 1.1, 4.2))
    g.append(txt(FX, PY + PH + 9, "frontière du périmètre régi", size=6.9,
                 fill=C["brique"]["deep"], anchor="middle", style="italic"))

    # Panneau B — où se place l'approbation
    BY = PY + PH + 32
    g.append(txt(8, BY, "B.  OÙ SE PLACE L'APPROBATION", size=8.4, fill=GREY, weight="bold"))
    g.append(seg(8, BY + 5, W - 8, BY + 5, RULE, 0.9))

    RY = BY + 18
    steps = [
        (8, 96, "vert", "L'agent propose", "sans effet externe"),
        (114, 104, "bleu", "Un composant déterministe", "et non agentique initie"),
        (228, 92, "ambre", "POINT D'APPROBATION", "ex ante, humain ou règle"),
    ]
    for x, w, col, t1, t2 in steps:
        c = C[col]
        g.append(rect(x, RY, w, 40, fill=c["fill"], stroke=c["line"], sw=1.0, rx=4))
        g.append(txt(x + w / 2, RY + 17, t1, size=7.6, fill=c["deep"],
                     anchor="middle", weight="bold"))
        g.append(txt(x + w / 2, RY + 28, t2, size=6.9, fill=GREY, anchor="middle"))
    g.append(arrow(106, RY + 20, 112, RY + 20, GREY, 1.1, 4.2))
    g.append(arrow(220, RY + 20, 226, RY + 20, GREY, 1.1, 4.2))

    GX = 336
    g.append(seg(GX, RY - 10, GX, RY + 54, C["brique"]["line"], 1.6))
    g.append(txt(GX - 4, RY - 14, "frontière de règlement", size=7.0,
                 fill=C["brique"]["deep"], anchor="end", weight="bold"))
    g.append(arrow(326, RY + 20, GX + 8, RY + 20, C["brique"]["line"], 1.2, 4.6))
    g.append(rect(GX + 14, RY, W - 8 - (GX + 14), 40, fill=C["brique"]["fill"],
                  stroke=C["brique"]["line"], sw=1.2, rx=4))
    g.append(txt(GX + 73, RY + 17, "EFFET IRRÉVOCABLE", size=7.6,
                 fill=C["brique"]["deep"], anchor="middle", weight="bold"))
    g.append(txt(GX + 73, RY + 28, "Lynx · RTR au 24 août 2026", size=6.9,
                 fill=GREY, anchor="middle"))
    g.append(txt(GX + 4, RY + 52, "après : la compensation n'existe pas", size=6.9,
                 fill=C["brique"]["deep"], style="italic"))
    return svg(RY + 62, "".join(g), "L'architecture qui se démontre")


# ── Gravure ────────────────────────────────────────────────────────────────

# L'ordre est celui de leur apparition dans le document : le numéro de fichier
# et le numéro que typst compose sur la page sont donc le même.
FIGURES = [
    ("f1-decalage-central.svg", f1),      # §1  Introduction
    ("f2-trois-surveillants.svg", f2),    # §4  Coopérative financière régie
    ("f3-cinq-exigences.svg", f4),        # §7  Grille de décision
    ("f4-architecture-cible.svg", f5),    # §11 Architecture cible
    ("f5-fenetre-2026-2030.svg", f3),     # §12 Trajectoire
]

if __name__ == "__main__":
    ici = pathlib.Path(__file__).parent
    for nom, fn in FIGURES:
        s = fn()
        (ici / nom).write_text(s, encoding="utf-8")
        h = s.split('height="', 1)[1].split('"', 1)[0]
        print(f"{nom:32s} {W} x {h}")
