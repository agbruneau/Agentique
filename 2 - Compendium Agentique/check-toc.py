#!/usr/bin/env python3
"""Contrôles de publication du TOC du compendium (Vol. IV).

Couvre les défauts qu'une relecture à l'œil ne rattrape pas sur un plan à
57 chapitres : renumérotation incomplète, renvoi interne pendant, décompte
annoncé périmé, budget qui ne tombe pas dans sa propre fourchette.

    python check-toc.py     # sortie 0 si tout passe, 1 sinon

⚠ Ce script est du contenu : il se vérifie comme le reste. Avant de publier
une modification, la valider par mutation — introduire chacune des fautes
dans une copie, vérifier que le script échoue, après avoir constaté qu'il
passe sur le document intact.

Faux positifs déjà neutralisés (ne pas « simplifier » ces motifs) :
  - « Vol. I ch. 4 », « Vol. II ch. 19 », « Vol. III Annexe B » désignent les
    volumes SOURCES, pas le compendium : leurs numéros tombent dans la plage
    des chapitres du compendium et passeraient inaperçus. D'où le retrait
    préalable de toute référence préfixée par un volume.
  - « Livre VI » dans une ligne « Fusion » peut désigner une partie d'un
    volume source ; seules les formes non préfixées sont contrôlées.
"""

import re
import sys
from pathlib import Path

DOC = Path(__file__).with_name("TOC.md")
ROMAINS = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII",
           "XIII", "XIV", "XV"]

# Toute référence préfixée par un volume source est retirée avant le contrôle
# des renvois internes (voir en-tête).
REF_SOURCE = re.compile(
    r"Vol\.\s*I{1,3}\s*(?:\*?(?:Monographie|Synthèse|PRD)\*?\s*)?"
    r"(?:ch\.\s*[\d]+(?:\s*[-–]\s*\d+)?|Annexe\s+[A-Z]|Partie[s]?\s+[IVX]+(?:\s*[-–]\s*[IVX]+)?)"
    r"(?:\s*\(ch\.\s*\d+(?:\s*[-–]\s*\d+)?\))?"  # « Vol. II Partie VII (ch. 22-23) »
)


def erreurs(txt):
    err = []

    chapitres = [(int(n), t) for n, t in
                 re.findall(r"^### Chapitre (\d+) — (.+)$", txt, re.M)]
    livres = re.findall(r"^# LIVRE ([IVX]+) — (.+)$", txt, re.M)
    annexes = re.findall(r"^- \*\*Annexe ([A-Z]) — ", txt, re.M)

    # 1. Numérotation des chapitres : continue à partir de 1, sans doublon.
    nums = [n for n, _ in chapitres]
    if nums != list(range(1, len(nums) + 1)):
        err.append(f"chapitres non continus : {nums}")

    # 2. Livres : numérotation romaine dans l'ordre, sans trou.
    if [l for l, _ in livres] != ROMAINS[:len(livres)]:
        err.append(f"livres non continus : {[l for l, _ in livres]}")

    # 3. Chaque livre contient au moins deux chapitres (un livre d'un seul
    #    chapitre est une anomalie de structure, pas une organisation).
    bornes = [(m.group(1), m.start()) for m in re.finditer(r"^# LIVRE ([IVX]+) — ", txt, re.M)]
    pos_ch = [(n, m.start()) for (n, _), m in
              zip(chapitres, re.finditer(r"^### Chapitre \d+ — ", txt, re.M))]
    for i, (rom, deb) in enumerate(bornes):
        fin = bornes[i + 1][1] if i + 1 < len(bornes) else len(txt)
        dedans = [n for n, p in pos_ch if deb < p < fin]
        if len(dedans) < 2:
            err.append(f"Livre {rom} : {len(dedans)} chapitre(s) — livre d'un seul chapitre")
        if dedans != list(range(min(dedans), max(dedans) + 1)) if dedans else False:
            err.append(f"Livre {rom} : chapitres non contigus {dedans}")

    # Renvois internes : on retire d'abord les références aux volumes sources.
    interne = REF_SOURCE.sub("", txt)

    # 4. Renvois « ch. N » et « ch. N-M » vers un chapitre existant.
    for m in re.finditer(r"ch\.\s*(\d+)(?:\s*[-–]\s*(\d+))?", interne):
        for g in (m.group(1), m.group(2)):
            if g and int(g) not in nums:
                err.append(f"renvoi vers un chapitre inexistant : ch. {g}")

    # 4bis. Numéro de chapitre nu en queue de liste (« ch. 17 et 16 ») : il
    #    survit intact à une renumérotation et devient faux sans rien signaler.
    #    Chaque numéro porte son propre « ch. ». Les plages « ch. N-M » restent
    #    licites : leurs deux bornes sont contrôlées ci-dessus.
    for m in re.finditer(r"ch\.\s*\d+\s*(?:,|et)\s*(\d+)", interne):
        err.append(f"numéro de chapitre nu en queue de liste : « {m.group()} » "
                   "— écrire « ch. N et ch. M »")

    # 5. Renvois « Livre X » / « Livres X-Y » vers un livre existant.
    romains_doc = {l for l, _ in livres}
    # « Livres IX-X » comme « Livres II et XII » : les deux formes se contrôlent.
    for m in re.finditer(r"Livres?\s+([IVX]+)(?:\s*(?:[-–]|et)\s*([IVX]+))?", interne):
        for g in (m.group(1), m.group(2)):
            if g and g not in romains_doc:
                err.append(f"renvoi vers un livre inexistant : Livre {g}")

    # 6. Renvois « Annexe X » vers une annexe déclarée.
    for m in re.finditer(r"Annexe\s+([A-Z])\b", interne):
        if m.group(1) not in annexes:
            err.append(f"renvoi vers une annexe inexistante : Annexe {m.group(1)}")

    # 7. Décomptes annoncés dans la volumétrie.
    m = re.search(r"(\d+)\s*chapitres en (\d+) livres[^.]*?(\d+) annexes", txt)
    if not m:
        err.append("bloc de volumétrie introuvable (décomptes chapitres/livres/annexes)")
    else:
        annonce = (int(m.group(1)), int(m.group(2)), int(m.group(3)))
        reel = (len(chapitres), len(livres), len(annexes))
        if annonce != reel:
            err.append(f"décomptes annoncés {annonce} != réels {reel} "
                       "(chapitres, livres, annexes)")

    # 8. Budget : la somme des enveloppes doit tomber dans la fourchette annoncée.
    # Les milliers sont séparés par des espaces de largeurs variables selon la
    # saisie (U+0020, U+00A0, U+202F) : on ne garde que les chiffres.
    entier = lambda s: int(re.sub(r'\D', '', s))
    parts = [entier(x) for x in re.findall(r'~([\d\s]+)000 mots', txt)]
    fourchette = re.search(r'≈\s*([\d\s]+000)\s*[–-]\s*([\d\s]+000) mots', txt)
    if not parts:
        err.append("aucune enveloppe « ~N 000 mots » trouvée")
    elif not fourchette:
        err.append("fourchette de projection « N 000-M 000 mots » introuvable")
    else:
        somme = sum(parts) * 1000  # les enveloppes sont libellées en milliers
        bas, haut = (entier(g) for g in fourchette.groups())
        if not bas <= somme <= haut:
            err.append(f'somme des enveloppes = {somme} mots, hors fourchette '
                       f'annoncée {bas}-{haut}')

    # 9. Chapitres consommateurs du corpus d'appui : la mention doit figurer
    #    dans le chapitre (parade du risque « corpus hérité sans re-déclaration »).
    m = re.search(r"Chapitres consommateurs\s*:\s*([^.]+)\.", txt)
    if not m:
        err.append("liste des chapitres consommateurs du corpus d'appui introuvable")
    else:
        # Les annotations entre parenthèses (« 15 (grille × maturité) ») sont
        # retirées : seuls les numéros de la liste comptent.
        declares = [int(x) for x in
                    re.findall(r"\d+", re.sub(r"\([^)]*\)", "", m.group(1)))]
        corps = re.split(r"^### Chapitre ", txt, flags=re.M)[1:]
        par_num = {int(re.match(r"(\d+)", c).group(1)): c for c in corps}
        for n in declares:
            if n not in par_num:
                err.append(f"chapitre consommateur {n} inexistant")
            elif "corpus d'appui" not in par_num[n]:
                err.append(f"chapitre {n} déclaré consommateur du corpus d'appui "
                           "sans porter la mention")

    # 10. Chaque chapitre trace sa provenance : ligne « Fusion » ou « Chapitre neuf ».
    for n, c in par_num.items() if m else []:
        if "*Fusion :" not in c and "*Chapitre neuf" not in c:
            err.append(f"chapitre {n} sans ligne « Fusion » ni « Chapitre neuf »")

    return err


def main():
    txt = DOC.read_text(encoding="utf-8")
    err = erreurs(txt)
    for e in err:
        print(f"ÉCHEC : {e}")
    if err:
        print(f"\n{len(err)} contrôle(s) en échec.")
        return 1
    print("Tous les contrôles passent.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
