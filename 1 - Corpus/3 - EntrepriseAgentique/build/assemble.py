# -*- coding: utf-8 -*-
"""Assemble les 34 pièces de `monographie/` en un seul `Monographie.md` au format
du gabarit FESP (Pandoc -> Typst). Voir build/build-pdf.sh pour la suite du pipeline.

Copie adaptée de l'assembleur du volume II (`2 - OrchestrationAgentique/build/assemble.py`),
lui-même issu du pipeline FESP du volume I : les trois copies évoluent séparément, un
correctif là-bas ne se propage pas ici (PRDPlan §7, P5.4 — décision de rendre au gabarit
des monographies, sur demande de l'auteur).

Ce que l'assembleur retire de chaque pièce (appareil de rédaction interne, hors PDF) :
  - le tableau d'en-tête « | Champ | Valeur | » (statut, gel, socle, garde-fous, volumétrie) ;
  - le renvoi « ([TOC.md](…)) » dans la ligne de thèse (la thèse elle-même est conservée) ;
  - le titre « ## Notes » et tout ce qui suit (journaux de relecture).
Ce qu'il conserve : la thèse d'exergue, tout le corps doctrinal, les encadrés
« > Lecture de l'auteur » / « > État de la connaissance vérifiable », les tableaux.

Le volume III ne porte aucune note de bas de page [^n] (constaté sur les 34 pièces le
23 juillet 2026) : aucun préfixage n'est nécessaire, à la différence du volume II.
"""
import re
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
MONO = ROOT / "monographie"
TOC = ROOT / "prd" / "TOC.md"
OUT = ROOT / "Monographie.md"

# Chemin relatif à monographie/ — ordre de lecture (avant-propos, ch. 1-28, annexes A-E).
PIECES = [
    "00-avant-propos.md",
    "01-partie-I/ch-01-identites-non-humaines.md",
    "01-partie-I/ch-02-standards-etires.md",
    "01-partie-I/ch-03-identite-decentralisee.md",
    "01-partie-I/ch-04-grille-cinq-questions.md",
    "02-partie-II/ch-05-agent-card-signee.md",
    "02-partie-II/ch-06-annuaires-commerciaux.md",
    "02-partie-II/ch-07-registres-gouvernes.md",
    "02-partie-II/ch-08-passeport-agent.md",
    "03-partie-III/ch-09-chaine-de-mandat.md",
    "03-partie-III/ch-10-deux-sauts.md",
    "03-partie-III/ch-11-know-your-agent.md",
    "04-partie-IV/ch-12-taxonomie-attaques.md",
    "04-partie-IV/ch-13-usurpation-rug-pull.md",
    "04-partie-IV/ch-14-revocation.md",
    "04-partie-IV/ch-15-soc-agentique.md",
    "05-partie-V/ch-16-menace-quantique.md",
    "05-partie-V/ch-17-crypto-agilite.md",
    "05-partie-V/ch-18-dette-migration.md",
    "06-partie-VI/ch-19-e23-amf.md",
    "06-partie-VI/ch-20-loi25-rgpd.md",
    "06-partie-VI/ch-21-normalisation-institutionnelle.md",
    "07-partie-VII/ch-22-genealogie-maillage.md",
    "07-partie-VII/ch-23-maillage-application.md",
    "08-partie-VIII/ch-24-observabilite-agentique.md",
    "08-partie-VIII/ch-25-cycle-de-vie.md",
    "08-partie-VIII/ch-26-indicateurs-agentops.md",
    "09-partie-IX/ch-27-architecture-reference.md",
    "09-partie-IX/ch-28-instanciation-cloture.md",
    "90-annexes/annexe-a-methodologie.md",
    "90-annexes/annexe-b-matrice.md",
    "90-annexes/annexe-c-chronologie.md",
    "90-annexes/annexe-d-glossaire.md",
    "90-annexes/annexe-e-catalogue-patrons.md",
]

# Pages de garde de partie, insérées avant le chapitre-clé (H1 -> nouvelle page via le gabarit).
PART_TITLES = {
    "01-partie-I/ch-01-identites-non-humaines.md":
        "Partie I — L'héritage : l'identité machine avant l'entreprise agentique",
    "02-partie-II/ch-05-agent-card-signee.md":
        "Partie II — Les mécanismes émergents : émettre l'identité",
    "03-partie-III/ch-09-chaine-de-mandat.md":
        "Partie III — La délégation : le mandat dans l'entreprise",
    "04-partie-IV/ch-12-taxonomie-attaques.md":
        "Partie IV — La confiance hostile : l'identité comme fondation de la défense",
    "05-partie-V/ch-16-menace-quantique.md":
        "Partie V — L'horloge post-quantique",
    "06-partie-VI/ch-19-e23-amf.md":
        "Partie VI — Le droit de l'entreprise agentique",
    "07-partie-VII/ch-22-genealogie-maillage.md":
        "Partie VII — Le maillage d'agents : où l'entreprise applique la confiance",
    "08-partie-VIII/ch-24-observabilite-agentique.md":
        "Partie VIII — AgentOps : exploiter la confiance dans la durée",
    "09-partie-IX/ch-27-architecture-reference.md":
        "Partie IX — Blueprint : l'entreprise agentique de confiance",
    "90-annexes/annexe-a-methodologie.md":
        "Annexes",
}

TITLE = "L'entreprise agentique"
SUBTITLE = ("La fabrique de confiance : identité non humaine, délégation vérifiable, "
            "maillage d'agents et AgentOps à l'horloge post-quantique (2026-2030)")
DESCRIPTOR = "Monographie en science et génie informatique"
AUTHOR = "André-Guy Bruneau, M.Sc. IT"
DATE = "Juillet 2026"

def read_resume():
    """Le résumé est la « ## Thèse d'ensemble » du TOC (jusqu'à la sous-section suivante)."""
    toc = TOC.read_text(encoding="utf-8")
    m = re.search(r"## Thèse d'ensemble\n+(.*?)\n## ", toc, re.S)
    return m.group(1).strip()


def clean_piece(text):
    lines = text.split("\n")
    h1 = lines[0].rstrip()

    # --- séparer en-tête (jusqu'au 1er '---' seul) et corps ---
    sep = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), None)
    header = lines[1:sep] if sep is not None else []
    body_lines = lines[sep + 1:] if sep is not None else lines[1:]

    # --- thèse : la conserver, débarrassée du renvoi ([TOC.md](…)) ---
    these = ""
    for ln in header:
        if ln.lstrip().startswith("> **Thèse"):
            these = re.sub(r" *\(\[TOC\.md\]\([^)]*\)\)", "", ln).rstrip()
            break

    body = "\n".join(body_lines)
    # --- retirer « ## Notes » et tout ce qui suit (journaux de relecture) ---
    body = re.split(r"(?m)^##\s+Notes\s*$", body, maxsplit=1)[0]

    out = h1 + "\n"
    if these:
        out += "\n" + these + "\n"
    out += "\n" + body.strip("\n") + "\n"
    return out.strip("\n")


def preamble():
    t = TITLE.replace("]", "\\]")
    st = SUBTITLE.replace("]", "\\]")
    return f"""```{{=typst}}
#[
#set par(justify: false, leading: 0.72em)
#align(center)[
  #v(3.2cm)
  #text(size: 25pt, weight: "bold")[{t}]

  #v(0.8cm)
  #text(size: 12.5pt, style: "italic")[{st}]

  #v(3cm)
  #text(size: 13pt)[{DESCRIPTOR}]

  #v(3cm)
  #text(size: 14pt, weight: "bold")[{AUTHOR}]

  #v(0.8cm)
  #text(size: 13pt)[{DATE}]
]
]
#pagebreak()
```

# Résumé {{.unnumbered}}

{read_resume()}

```{{=typst}}
#pagebreak()
#outline(title: [Table des matières], depth: 2)
#pagebreak()
```

# Note sur les tableaux et les figures

Le corps de cette monographie ne comporte aucune figure ni illustration. Les tableaux
d'analyse — taxonomies, grilles de correspondance, matrices de décision — sont présentés
*en place*, au fil des sections où ils appuient le propos, plutôt que rassemblés en une
liste distincte : ce sont des outils de comparaison locaux, indissociables de leur
contexte d'argumentation. L'Annexe B rassemble la matrice détaillée des mécanismes, et
l'Annexe D le glossaire qui tient lieu de liste d'abréviations.
"""


def main():
    parts = [preamble()]
    for rel in PIECES:
        if rel in PART_TITLES:
            parts.append(f"# {PART_TITLES[rel]}\n")
        parts.append(clean_piece((MONO / rel).read_text(encoding="utf-8")))
    OUT.write_text("\n\n".join(parts) + "\n", encoding="utf-8")
    print(f"écrit -> {OUT}  ({len(PIECES)} pièces, {OUT.stat().st_size // 1024} Ko)")


if __name__ == "__main__":
    main()
