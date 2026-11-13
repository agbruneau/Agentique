from dessin import Dessin, OCRE, FOND_OCRE, VERT, FOND_VERT, GRIS, TRAIT

d = Dessin(hauteur=320)


def panneau(x, titre, couleur, fond, echanges, note):
    d.surtitre(x, 26, titre, couleur)
    cx, sx = x + 60, x + 340          # lignes de vie du client et du serveur
    d.boite(cx - 50, 38, 100, 36, "Client", fond=fond, trait=couleur)
    d.boite(sx - 50, 38, 100, 36, "Serveur", fond=fond, trait=couleur)
    d.trait(cx, 74, cx, 262, TRAIT, tirets=True)
    d.trait(sx, 74, sx, 262, TRAIT, tirets=True)
    y = 112
    for sens, etiquette in echanges:
        if sens == ">":
            d.fleche(cx, y, sx, y, etiquette, couleur=couleur)
        else:
            d.fleche(sx, y, cx, y, etiquette, couleur=couleur)
        y += 42
    d.paragraphe(x + 200, 292, note, 380, taille=11.5, couleur=couleur)


panneau(30, "Jusqu'à 2025-11-25", OCRE, FOND_OCRE, [
    (">", "initialize : poignée de main"),
    ("<", "session ouverte : Mcp-Session-Id"),
    (">", "requêtes avec Mcp-Session-Id"),
    ("<", "requête initiée par le serveur"),
], "État de session côté serveur, canal de retour ouvert")

panneau(470, "Depuis 2026-07-28", VERT, FOND_VERT, [
    (">", "requête + version et capacités"),
    ("<", "input_required : ce qu'il manque"),
    (">", "requête d'origine réémise, avec les réponses"),
    ("<", "complete"),
], "Aucune session : des paires requête-réponse HTTP ordinaires")

d.trait(450, 20, 450, 300, TRAIT)
d.ecrit("fig-05-e2")
