"""Fig. 16-e1 : les trois topologies de coordination (section 16.1)."""
from dessin import Dessin, BLEU, FOND, NEUTRE, GRIS, MARINE, TRAIT

d = Dessin(hauteur=290)
R = 13          # rayon d'un agent


def bord_rect(cx, cy, l, h, vx, vy):
    """Point où la demi-droite partant du centre du rectangle, de direction (vx, vy), sort du bord."""
    tx = (l / 2) / abs(vx) if vx else float("inf")
    ty = (h / 2) / abs(vy) if vy else float("inf")
    t = min(tx, ty)
    return cx + vx * t, cy + vy * t


def lien(a, b):
    """Trait entre deux nœuds; chaque nœud est ('c', x, y) ou ('r', cx, cy, l, h)."""
    ax, ay = a[1], a[2]
    bx, by = b[1], b[2]
    lg = ((bx - ax) ** 2 + (by - ay) ** 2) ** 0.5
    vx, vy = (bx - ax) / lg, (by - ay) / lg
    if a[0] == "c":
        p = (ax + vx * R, ay + vy * R)
    else:
        p = bord_rect(ax, ay, a[3], a[4], vx, vy)
    if b[0] == "c":
        q = (bx - vx * R, by - vy * R)
    else:
        q = bord_rect(bx, by, b[3], b[4], -vx, -vy)
    d.trait(p[0], p[1], q[0], q[1], couleur=TRAIT, epaisseur=1.3)


def agent(x, y):
    d.cercle(x, y, R, fond=NEUTRE, trait=GRIS, epaisseur=1.3)
    return ("c", x, y)


def chef(cx, cy, l, h, titre, taille=12):
    d.boite(cx - l / 2, cy - h / 2, l, h, titre, taille=taille)
    return ("r", cx, cy, l, h)


def legende(cx, nom, texte):
    d.texte(cx, 234, nom, 14, True, MARINE)
    d.paragraphe(cx, 256, texte, 215, taille=11.5, couleur=GRIS)


# ---- centralisée
cx = 160
hub = chef(cx, 115, 116, 34, "Orchestrateur")
for (x, y) in [(cx - 88, 48), (cx + 88, 48), (cx - 88, 182), (cx + 88, 182)]:
    lien(hub, agent(x, y))
legende(cx, "Centralisée", "Les agents ne communiquent qu'avec l'orchestrateur")

# ---- décentralisée
cx = 440
pairs = [agent(x, y) for (x, y) in [(cx - 82, 48), (cx + 82, 48), (cx + 82, 182), (cx - 82, 182)]]
for i in range(4):
    for j in range(i + 1, 4):
        lien(pairs[i], pairs[j])
legende(cx, "Décentralisée", "Échanges directs entre pairs, sans point de passage obligé")

# ---- hiérarchique
cx = 720
haut = chef(cx, 42, 116, 30, "Superviseur")
for dx in (-62, 62):
    mx = cx + dx
    milieu = chef(mx, 112, 112, 40, "Superviseur intermédiaire", taille=11)
    lien(haut, milieu)
    for ex in (-30, 30):
        lien(milieu, agent(mx + ex, 182))
legende(cx, "Hiérarchique", "La centralisation répétée sur plusieurs niveaux")

d.ecrit("fig-16-e1")
