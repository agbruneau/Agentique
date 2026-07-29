#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Assemble les cinquante pieces du compendium en un seul markdown de rendu.

Sortie : un .md destine a Pandoc -> Typst (gabarit build/springer.template).

Ce que l'assemblage RETIRE, et pourquoi :
  - la section « Note de statut *(hors plan — a retirer a la publication)* »,
    que le PRD §6 et le skill §7 declarent hors plan (c'est aussi la borne de
    `PRD/decompte.sh`, qui l'exclut du corps) ;
  - l'en-tete a cinq champs (Statut / Date de gel / Socle mobilise /
    Garde-fous balayes / Volumetrie ciblee), appareil de gouvernance et non
    corps de chapitre (idem : hors du corps mesure par `decompte.sh`) ;
  - la these citee depuis le TOC, qui est le cahier des charges de la piece et
    non son propos (idem : hors du corps mesure) ;
  - les filets `---`, qui ne sont que des separateurs de section.
Les trois appareils sont neanmoins EXIGES a la lecture : leur absence fait
echouer l'assemblage, faute de quoi une piece deformee passerait sans bruit.
Ce qu'il conserve : titre, ligne de situation, et tout le corps. L'etat du
volume (brouillon non publiable) est declare une fois, au colophon du gabarit —
retire des pieces, il n'est pas efface.

Depuis le 29 juillet 2026, l'assemblage ajoute apres le chapitre 50 une ANNEXE
HORS PLAN, `audit-references.md` : un rapport de mesure sans autorite, qui n'est
aucune des neuf annexes A a I du TOC et ne consomme aucun numero de chapitre.
"""
import re
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent

LIVRES = [
    ("I", "Livre I",
     "Coopérer",
     "Fondements de l'interopérabilité et couche protocolaire agentique"),
    ("II", "Livre II",
     "Faire confiance",
     "Identité, délégation et fabrique de confiance — émission, confiance "
     "hostile, horloge post-quantique"),
    ("III", "Livre III",
     "Encadrer",
     "Orchestration en entreprise, cadre réglementaire canadien et terrain "
     "financier"),
    ("IV", "Livre IV",
     "Appliquer, exploiter, produire et composer",
     "AgentMesh, AgentOps, fabrique d'agents et synthèse architecturale"),
    ("V", "Livre V",
     "Livrer et clore",
     "L'agent comme livrable logiciel, horizon et frontière"),
]

RE_TITRE = re.compile(r"^# Chapitre (\d+) — (.+)$")
RE_SECTION = re.compile(r"^## § (\d+\.\d+) — (.+)$")
RE_MOUVEMENT = re.compile(r"^# ((?:Premier|Second|Troisième) mouvement — .+)$")
RE_NOTE_STATUT = re.compile(r"^## § (\d+\.\d+) — Note de statut\b")


def echappe_typst(texte):
    """Neutralise le balisage Typst dans un texte insere en mode contenu."""
    for c in "\\#$@[]*_`<>":
        texte = texte.replace(c, "\\" + c)
    return texte


def brut(code):
    return "```{=typst}\n" + code + "\n```\n"


def piece(chemin, numero):
    """Rend une piece : ouverture de chapitre + these + corps epure."""
    lignes = chemin.read_text(encoding="utf-8").splitlines()
    sortie = []

    i = 0
    titre = None
    situation = []
    these = []

    # --- titre ---
    while i < len(lignes):
        m = RE_TITRE.match(lignes[i])
        if m:
            if int(m.group(1)) != numero:
                sys.exit(f"[assemble] {chemin} : numero {m.group(1)} != {numero}")
            titre = m.group(2)
            i += 1
            break
        i += 1
    if titre is None:
        sys.exit(f"[assemble] {chemin} : titre de chapitre introuvable")

    # --- ligne de situation (italique, une ou deux lignes) ---
    while i < len(lignes) and not lignes[i].strip():
        i += 1
    if i < len(lignes) and lignes[i].startswith("*Livre "):
        while i < len(lignes) and lignes[i].strip():
            situation.append(lignes[i])
            i += 1

    # --- en-tete a cinq champs : retire ---
    while i < len(lignes):
        if lignes[i].startswith("| Champ "):
            while i < len(lignes) and lignes[i].startswith("|"):
                i += 1
            break
        if lignes[i].startswith("> "):
            break
        i += 1

    # --- these : retiree du rendu, comme l'en-tete et la note de statut ---
    while i < len(lignes) and not lignes[i].strip():
        i += 1
    if i < len(lignes) and lignes[i].startswith(">"):
        while i < len(lignes) and lignes[i].startswith(">"):
            these.append(lignes[i])
            i += 1

    # --- ouverture de chapitre ---
    sortie.append(brut(f"#ouverture-chapitre({numero})"))
    sortie.append(f"# {titre}\n")
    if situation:
        sortie.append(brut("#situation["))
        sortie.append("\n".join(situation) + "\n")
        sortie.append(brut("]"))
    if not these:
        sys.exit(f"[assemble] {chemin} : these introuvable (borne d'en-tete)")

    # --- corps ---
    corps = []
    note = None
    for ligne in lignes[i:]:
        m = RE_NOTE_STATUT.match(ligne)
        if m:
            note = m.group(1)
            break
        if ligne.strip() == "---":
            continue
        m = RE_SECTION.match(ligne)
        if m:
            corps.append(f"## {m.group(1)} {m.group(2)}\n")
            continue
        m = RE_MOUVEMENT.match(ligne)
        if m:
            corps.append(f"## {m.group(1)}\n")
            continue
        corps.append(ligne + "\n")
    if note is None:
        sys.exit(f"[assemble] {chemin} : note de statut absente (borne de coupe)")

    # Le corps renvoie parfois a la note de statut qu'on vient de retirer : le
    # renvoi n'est pas efface, il est marque d'une dague, dont l'avertissement
    # liminaire donne la lecture. Un renvoi pendant serait pire que la coupe.
    texte = "".join(corps)
    texte, marques = re.subn(r"§\s*" + re.escape(note) + r"(?!\d)",
                            f"§ {note} †", texte)
    sortie.append(texte)
    return "".join(sortie), marques


def annexe(chemin):
    """Rend l'annexe hors plan placee apres le chapitre 50.

    Elle n'a ni en-tete a cinq champs, ni these, ni note de statut : ce n'est
    pas une piece du plan, et l'ouverture ne porte aucun numero — le plafond de
    cinquante chapitres reste tenu.
    """
    lignes = chemin.read_text(encoding="utf-8").splitlines()
    i = 0
    while i < len(lignes) and not lignes[i].startswith("# "):
        i += 1
    if i == len(lignes):
        sys.exit(f"[assemble] {chemin} : titre d'annexe introuvable")
    # L'ouverture imprime deja « Annexe » : le titre ne le redit pas.
    titre = re.sub(r"^Annexe\s+[—-]\s+", "", lignes[i][2:].strip())
    i += 1

    situation = []
    while i < len(lignes) and not lignes[i].strip():
        i += 1
    if i < len(lignes) and lignes[i].startswith("*"):
        while i < len(lignes) and lignes[i].strip():
            situation.append(lignes[i])
            i += 1

    sortie = [brut("#ouverture-annexe()"), f"# {titre}\n"]
    if situation:
        sortie.append(brut("#situation["))
        sortie.append("\n".join(situation) + "\n")
        sortie.append(brut("]"))
    else:
        sys.exit(f"[assemble] {chemin} : ligne de situation introuvable")
    sortie.append("\n".join(l for l in lignes[i:] if l.strip() != "---") + "\n")
    return "".join(sortie)


def main():
    dest = Path(sys.argv[1]) if len(sys.argv) > 1 else RACINE / "build" / "compendium-assemble.md"
    morceaux = []
    numero = 0
    dagues = 0
    for romain, dossier, verbe, sous in LIVRES:
        morceaux.append(brut(
            f"#ouverture-livre[{echappe_typst(romain)}]"
            f"[{echappe_typst(verbe)}][{echappe_typst(sous)}]"))
        for md in sorted((RACINE / dossier).glob("[0-9]*.md")):
            numero += 1
            texte, marques = piece(md, numero)
            morceaux.append(texte)
            dagues += marques
    if numero != 50:
        sys.exit(f"[assemble] {numero} chapitres assembles, 50 attendus")
    morceaux.append(annexe(RACINE / "audit-references.md"))
    dest.write_text("\n".join(morceaux), encoding="utf-8")
    print(f"[assemble] {numero} chapitres, 5 livres, 1 annexe hors plan, "
          f"{dagues} renvois a la note de statut marques -> {dest}")


if __name__ == "__main__":
    main()
