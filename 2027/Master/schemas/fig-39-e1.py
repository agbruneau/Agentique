"""Chapitre 39, section 39.2 : les six étapes du cycle de vie et la décision prise à chacune."""
from dessin import Dessin, BLEU, FOND, NEUTRE, TRAIT, MARINE

ETAPES = [
    ("Qualification", "Une solution moins autonome suffirait-elle ?"),
    ("Pilote", "Propriétaire, accès limités, journaux, critères d'arrêt, plafond de "
               "consommation en place ?"),
    ("Production", "Mise en service graduelle, approuvée par une autorité imputable"),
    ("Exploitation", "Les usages réels correspondent-ils aux usages autorisés ?"),
    ("Changement", "Ce changement déclenche-t-il une nouvelle revue ?"),
    ("Retrait", "Accès supprimés, documents archivés, inscription conservée"),
]

X0, L, ECART = 30, 120, 20
Y_ETAPE, H_ETAPE = 20, 46
Y_DEC, H_DEC = 84, 124

d = Dessin(hauteur=Y_DEC + H_DEC + 20)
for i, (etape, decision) in enumerate(ETAPES):
    x = X0 + i * (L + ECART)
    d.boite(x, Y_ETAPE, L, H_ETAPE, etape, fond=FOND, trait=BLEU)
    if i < len(ETAPES) - 1:
        d.fleche(x + L, Y_ETAPE + H_ETAPE / 2, x + L + ECART, Y_ETAPE + H_ETAPE / 2, couleur=BLEU)
    d.trait(x + L / 2, Y_ETAPE + H_ETAPE, x + L / 2, Y_DEC, couleur=TRAIT)
    d.rect(x, Y_DEC, L, H_DEC, fond=NEUTRE, trait=TRAIT)
    d.paragraphe(x + L / 2, Y_DEC + 24, decision, L - 16, taille=11.5, couleur=MARINE)

d.ecrit("fig-39-e1")
