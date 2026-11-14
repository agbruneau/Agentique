"""Chapitre 49, sections 49.3 à 49.5 : les échéances datées de 2027 à 2031, sur trois lignes
(normalisation, réglementation, cryptographie). Dates des tableaux du chapitre."""
from dessin import Dessin, BLEU, FOND, GRIS, TRAIT, MARINE

d = Dessin(hauteur=388)
X0, X1, AN0, AN1 = 150, 850, 2027.0, 2032.0


def x(date):
    return X0 + (X1 - X0) * (date - AN0) / (AN1 - AN0)


# ---- Axe des années
Y_AXE = 362
d.trait(X0, Y_AXE, X1, Y_AXE, couleur=TRAIT)
for an in range(2027, 2033):
    d.trait(x(an), 46, x(an), Y_AXE, couleur="#e3e7ee", epaisseur=1)
    if an < 2032:
        d.texte((x(an) + x(an + 1)) / 2, Y_AXE + 18, str(an), 12, True, MARINE)

LIGNES = [("Normalisation", "jalons annoncés", 108),
          ("Réglementation", "échéances fixées", 222),
          ("Cryptographie", "échéances fixées", 322)]
for titre, sous, y in LIGNES:
    d.texte(30, y - 2, titre, 12.5, True, MARINE, "start")
    d.texte(30, y + 13, sous, 10.5, False, GRIS, "start", italique=True)
    d.trait(X0, y, X1, y, couleur=TRAIT, epaisseur=1)


def jalon(date, y, lignes, haut=True, plein=True, ancre="middle", dx=0):
    """Un point sur la ligne et son étiquette, au-dessus ou au-dessous."""
    d.cercle(x(date), y, 5.5, fond=BLEU if plein else "#ffffff", trait=BLEU)
    pas = 12.5
    y0 = y - 12 - pas * (len(lignes) - 1) if haut else y + 20
    for k, ligne in enumerate(lignes):
        d.texte(x(date) + dx, y0 + k * pas, ligne, 10.5, k == 0, MARINE if k == 0 else GRIS, ancre)


# Normalisation : points creux, ce sont des intentions.
jalon(2027.25, 108, ["31 mars 2027", "IETF : projet de protocole", "de dialogue adopté"], plein=False)
jalon(2028.0, 108, ["31 déc. 2027", "IETF : découverte", "d'agents à l'IESG"], haut=False, plein=False)
jalon(2028.25, 108, ["31 mars 2028", "IETF : protocole de", "dialogue à l'IESG"], plein=False,
      ancre="start", dx=-8)

# Réglementation
jalon(2027.33, 222, ["1er mai 2027", "E-23 et AMF"])
jalon(2027.93, 222, ["2 et 11 déc. 2027", "AI Act, annexe III;", "cyberrésilience"], haut=False)
jalon(2028.58, 222, ["2 août 2028", "AI Act, annexe I"])
jalon(2029.58, 222, ["2 août 2029", "Réexamen de l'AI Act"], haut=False)
jalon(2030.58, 222, ["2 août 2030", "AI Act, systèmes des", "autorités publiques"])

# Cryptographie
jalon(2031.0, 322, ["Fin de 2030", "NIST : dépréciation;", "clés post-quantiques"], ancre="end", dx=8)
jalon(2031.99, 322, ["Fin de 2031", "Signatures; systèmes", "prioritaires au Canada"], ancre="end",
      dx=8)

d.cercle(X0 + 6, 28, 5, fond=BLEU, trait=BLEU)
d.texte(X0 + 17, 32, "échéance fixée par un texte", 10.5, False, GRIS, "start")
d.cercle(X0 + 196, 28, 5, fond="#ffffff", trait=BLEU)
d.texte(X0 + 207, 32, "jalon annoncé par une charte, susceptible de glisser", 10.5, False, GRIS, "start")

d.ecrit("fig-49-e1")
