#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Reporte la mesure de `decompte.sh` aux TROIS sites qui la publient.

⚠ **Ce script ne mesure rien, et c'est sa propriété essentielle.** La seule
autorité de décompte du volume est [`decompte.sh`](decompte.sh) (PRD §9, porte
G-2) ; celui-ci **l'invoque** et **recopie** ce qu'elle rend. *Y porter un
tokéniseur créerait une seconde autorité, c'est-à-dire une divergence qui
attend.*

Pourquoi il existe
------------------
Le registre de gel pose sa propre règle : *« ce qui est dû n'est pas une
correction de registre, c'est une passe qui re-mesure les cinquante en-têtes ET
ce registre au même commit »*. **Trois sites publient la mesure** — l'en-tête de
la pièce, le registre, le `README` du Livre —, et **un chiffre couplé par
contrôle à deux autres ne se rafraîchit pas d'un seul côté**.

⚠ **Le 2 septembre 2026, la propagation a dû être refaite TROIS FOIS dans la même
journée** : chaque passe qui touchait un corps déplaçait la mesure, et
`decompte.sh --registre` refusait le registre quelques heures après l'avoir
accepté. *Une opération qu'on refait trois fois à la main se fait mal la
troisième* — d'où cet outil.

Usage :
    python PRD/reporter-volumetrie.py            # écrit
    python PRD/reporter-volumetrie.py --verifier # ne fait que rapporter l'écart
"""

import collections
import os
import re
import subprocess
import sys
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8")  # console cp1252 : ⚠ et ☑ ne s'y encodent pas
sys.stderr.reconfigure(encoding="utf-8")

RACINE = Path(os.environ.get("COMPENDIUM_RACINE",
                             Path(__file__).resolve().parent.parent))
ENVELOPPES = {"I": 65000, "II": 50000, "III": 90000, "IV": 69000, "V": 34000}
LETTRES = {"I": "onze", "II": "dix", "III": "quinze", "IV": "dix", "V": "quatre"}

VOLUMETRIE_TETE = re.compile(r"(Réel : )([\d ]+)( mots de corps pour une cible ≈ )([\d ]+)( mots \()([−+][\d,]+ %)(\))")
RANGEE_REGISTRE = re.compile(r"^\| \d+ \|")
FICHIER_REGISTRE = re.compile(r"Livre%20([IVX]+)/([\w.-]+\.md)")


def fmt(n):
    return f"{n:,}".replace(",", " ").replace(" ", " ")


def pourcent(reel, cible):
    e = (reel - cible) / cible * 100
    return f"{'−' if e < 0 else '+'}{abs(e):.1f} %".replace(".", ",")


def mesurer():
    """Invoque l'autorité et rend {chemin relatif: mots}."""
    pieces = sorted(p.relative_to(RACINE).as_posix()
                    for p in RACINE.glob("Livre */[0-9][0-9]-*.md"))
    # ⚠ Chemin RELATIF et `cwd` à la racine : sur Windows, `bash` ne résout ni
    # un chemin à antislashs ni une lettre de lecteur — seulement du POSIX.
    r = subprocess.run(["bash", "PRD/decompte.sh", *pieces],
                       capture_output=True, text=True, encoding="utf-8", cwd=RACINE)
    if r.returncode != 0:
        raise SystemExit(f"[volumétrie] decompte.sh a échoué :\n{r.stderr.strip()[:500]}")
    mes = {}
    for ligne in r.stdout.splitlines():
        m = re.match(r"\s*(\d+)\s+(Livre .*\.md)", ligne)
        if m:
            mes[m.group(2)] = int(m.group(1))
    if len(mes) != 50:
        raise SystemExit(f"[volumétrie] {len(mes)} pièces mesurées, cinquante attendues.")
    return mes


def reporter(mes, ecrire):
    """Rend la liste des écarts trouvés ; les corrige si `ecrire`."""
    ecarts = []

    # --- site 1 : le registre de gel (cinquante lignes) -------------------
    reg = RACINE / "PRD" / "registre-gel.md"
    lignes = reg.read_text(encoding="utf-8").split("\n")
    for i, l in enumerate(lignes):
        if not RANGEE_REGISTRE.match(l):
            continue
        c = l.split("|")
        m = FICHIER_REGISTRE.search(c[3])
        cle = f"Livre {m.group(1)}/{m.group(2)}"
        reel, cible = mes[cle], int(re.sub(r"\D", "", c[6]))
        if int(re.sub(r"\D", "", c[7])) != reel:
            ecarts.append(f"registre : {cle} porte {c[7].strip()}, mesuré {fmt(reel)}")
            c[7], c[8] = f" {fmt(reel)} ", f" {pourcent(reel, cible)} "
            lignes[i] = "|".join(c)
    if ecrire:
        reg.write_text("\n".join(lignes), encoding="utf-8", newline="\n")

    # --- site 2 : la tête des cinquante pièces ------------------------------
    # ⚠ Depuis le 15 septembre 2026 (plan d'exécution, T4.3), les CINQUANTE têtes publient
    # la mesure, sous une forme fixe — « Réel : N mots de corps pour une cible ≈ C mots
    # (±x,x %) » —, et l'écart se recalcule avec le réel. Vingt-six seulement la publiaient
    # jusque-là. Le « Réel » du tableau de rédaction, reporté en fin de pièce, est daté de
    # sa passe : il ne se touche pas. Une tête sans cette forme arrête le report — *la
    # passer en silence rendrait le site muet, et le contrôle P6 le verrait trop tard.*
    for f, reel in sorted(mes.items()):
        p = RACINE / f
        lignes = p.read_text(encoding="utf-8").split("\n")
        fin = lignes.index("---") if "---" in lignes else len(lignes)
        i = next((k for k in range(fin) if lignes[k].startswith("| **Volumétrie cible**")), None)
        m = VOLUMETRIE_TETE.search(lignes[i]) if i is not None else None
        if not m:
            raise SystemExit(f"[volumétrie] {f} : la tête ne porte pas la mesure sous la forme "
                             f"« Réel : N mots de corps pour une cible ≈ C mots (±x,x %) ».")
        juste = (m.group(1) + fmt(reel) + m.group(3) + m.group(4) + m.group(5)
                 + pourcent(reel, int(re.sub(r"\D", "", m.group(4)))) + m.group(7))
        if m.group(0) != juste:
            ecarts.append(f"en-tête : {f} porte {m.group(2).strip()} ({m.group(6)}), mesuré {fmt(reel)}")
            lignes[i] = lignes[i][:m.start()] + juste + lignes[i][m.end():]
            if ecrire:
                p.write_text("\n".join(lignes), encoding="utf-8", newline="\n")

    # --- site 3 : les README de Livre (table et total) --------------------
    par_livre = collections.Counter()
    for f, n in mes.items():
        par_livre[f.split("/")[0].split()[-1]] += n
    for livre, total in sorted(par_livre.items()):
        p = RACINE / f"Livre {livre}" / "README.md"
        t = p.read_text(encoding="utf-8")
        # Forme de la page d'accueil réécrite le 15 septembre 2026 (tâche T4.2), sans
        # marqueur ni gras. Une forme introuvable est un écart : sans cela, réécrire la
        # page éteindrait ce site en silence.
        m = re.search(r"(Volumétrie : )([\d ]+)( mots de corps)", t)
        if not m:
            ecarts.append(f"README Livre {livre} : forme « Volumétrie : N mots de corps » introuvable")
        elif int(re.sub(r"\D", "", m.group(2))) != total:
            ecarts.append(f"README Livre {livre} : porte {m.group(2)}, mesuré {fmt(total)}")
            t = t[:m.start()] + m.group(1) + fmt(total) + m.group(3) + t[m.end():]
        m2 = re.search(r"(enveloppe de Livre de [\d ]+ au TOC, soit )[−+][\d,]+ %()", t)
        if not m2:
            ecarts.append(f"README Livre {livre} : forme « enveloppe de Livre de N au TOC, soit ±x % » introuvable")
        else:
            juste = pourcent(total, ENVELOPPES[livre])
            if m2.group(0) != m2.group(1) + juste + m2.group(2):
                t = t[:m2.start()] + m2.group(1) + juste + m2.group(2) + t[m2.end():]
        if ecrire:
            p.write_text(t, encoding="utf-8", newline="\n")

    return ecarts, sum(mes.values())


def main():
    verif = "--verifier" in sys.argv
    mes = mesurer()
    ecarts, total = reporter(mes, ecrire=not verif)
    for e in ecarts:
        print(f"  {'☐' if verif else '☑'} {e}")
    if verif and ecarts:
        print(f"\nÉCART — {len(ecarts)} site(s) ne portent pas la mesure ({fmt(total)} mots).")
        return 1
    print(f"\nOK — {fmt(total)} mots de corps"
          + (f", {len(ecarts)} report(s) écrit(s)." if ecarts else ", les trois sites concordent."))
    print("⚠ Les tables par chapitre des README et la table de synthèse du registre ne sont PAS")
    print("  touchées : elles portent des colonnes DATÉES, et une colonne datée se lit, elle ne se")
    print("  rafraîchit pas. Ajouter une colonne est un geste de passe, pas de script.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
