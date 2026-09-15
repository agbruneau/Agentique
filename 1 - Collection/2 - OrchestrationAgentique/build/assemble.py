# -*- coding: utf-8 -*-
"""Assemble les 29 pièces de `monographie/` en un seul `Monographie.md` au format
du gabarit FESP (Pandoc -> Typst). Voir build/build-pdf.sh pour la suite du pipeline.

Ce que l'assembleur retire de chaque pièce (appareil de rédaction interne, hors PDF publié) :
  - le tableau d'en-tête « | Champ | Valeur | » (statut, gel, socle, garde-fous, volumétrie) ;
  - les bandeaux « > ⚠ Correctif de la rédaction … » (notes de gouvernance éditoriale) ;
  - le bloc de gouvernance HTML final « <!-- … --> » ;
  - le titre « ## Notes » (les définitions [^n] sont conservées ; Pandoc/Typst les
    place en notes de bas de page au point d'appel).
Ce qu'il conserve : la thèse d'exergue (renvoi TOC.md retiré), tout le corps doctrinal,
les encadrés « > État de la connaissance vérifiable », les tableaux, les notes.
Les labels de notes sont préfixés par pièce (`[^c1-1]`, `[^ap-1]`, …) pour éviter les
collisions à la concaténation.
"""
import posixpath
import re
import pathlib
import sys
sys.stdout.reconfigure(encoding="utf-8")  # console cp1252 : ⚠ et ☑ ne s'y encodent pas
sys.stderr.reconfigure(encoding="utf-8")

ROOT = pathlib.Path(__file__).resolve().parent.parent
MONO = ROOT / "monographie"
TOC = ROOT / "prd" / "TOC.md"
OUT = ROOT / "Monographie.md"

# (chemin relatif à monographie/, préfixe de notes unique) — ordre de lecture.
PIECES = [
    ("00-avant-propos.md", "ap"),
    ("01-partie-I/ch-01-genealogie-gouvernance.md", "c1"),
    ("01-partie-I/ch-02-anatomie-mcp-a2a.md", "c2"),
    ("01-partie-I/ch-03-ap2-agntcy-acp.md", "c3"),
    ("01-partie-I/ch-04-risques-protocolaires.md", "c4"),
    ("02-partie-II/ch-05-options-orchestration.md", "c5"),
    ("02-partie-II/ch-06-autonomie-encadree.md", "c6"),
    ("02-partie-II/ch-07-frameworks.md", "c7"),
    ("02-partie-II/ch-08-identite-registres.md", "c8"),
    ("03-partie-III/ch-09-e23-risque-modele.md", "c9"),
    ("03-partie-III/ch-10-vide-federal-c36.md", "c10"),
    ("03-partie-III/ch-11-quebec-amf-loi25.md", "c11"),
    ("03-partie-III/ch-12-acvm-11-348.md", "c12"),
    ("03-partie-III/ch-13-pont-frames.md", "c13"),
    ("04-partie-IV/ch-14-cadre-bancaire.md", "c14"),
    ("04-partie-IV/ch-15-iso20022-lynx-rtr.md", "c15"),
    ("04-partie-IV/ch-16-ap2-rails.md", "c16"),
    ("05-partie-V/ch-17-etudes-de-cas.md", "c17"),
    ("06-partie-VI/ch-18-matrice.md", "c18"),
    ("06-partie-VI/ch-19-architecture-reference.md", "c19"),
    ("06-partie-VI/ch-20-instrumentation-feuille-route.md", "c20"),
    ("06-partie-VI/ch-21-frontiere.md", "c21"),
    ("07-partie-VII/ch-22-principes-couches.md", "c22"),
    ("07-partie-VII/ch-23-correspondance-flux.md", "c23"),
    ("07-partie-VII/ch-24-lacunes-revalidation.md", "c24"),
    ("90-annexes/annexe-a-methodologie.md", "aa"),
    ("90-annexes/annexe-b-matrice.md", "ab"),
    ("90-annexes/annexe-c-chronologie.md", "ac"),
    ("90-annexes/annexe-d-glossaire.md", "ad"),
]

# Pages de garde de partie, insérées avant le chapitre-clé (H1 -> nouvelle page via le gabarit).
PART_TITLES = {
    "c1": "Partie I — Fondements : les protocoles d'interopérabilité agentique",
    "c5": "Partie II — L'orchestration multi-agents en entreprise",
    "c9": "Partie III — Le cadre réglementaire canadien",
    "c14": "Partie IV — L'interopérabilité financière canadienne",
    "c17": "Partie V — L'adoption par les institutions financières canadiennes",
    "c18": "Partie VI — Synthèse : l'architecture de référence",
    "c22": "Partie VII — Le blueprint : plateforme d'intégration d'entreprise (instanciation IBM)",
    "aa": "Annexes",
}

TITLE = "Orchestration agentique"
SUBTITLE = ("Interopérabilité et orchestration agentique dans les services financiers "
            "canadiens — protocoles ouverts, cadre réglementaire et blueprint "
            "d'intégration d'entreprise (état des lieux 2024-2026)")
AUTHOR = "André-Guy Bruneau, M.Sc. IT"
DATE = "Juillet 2026"

# Résumé anglais de la page « Abstract » (tâche T7.1 du plan d'exécution, 15 septembre 2026) :
# traduction du « ## Abstract » de TOC.md, que la page « Résumé » reprend, faite avec
# assistance de modèle et non relue par un humain. Elle ne suit pas sa source d'elle-même :
# qui reprend l'abstract de TOC.md reprend ce texte.
ABSTRACT_EN = """\
Between 2024 and 2026, two trajectories that had until then run in parallel converged in Canadian financial services. On one side, agentic interoperability protocols — MCP for agents' access to tools, A2A for collaboration between agents, AP2 for transactions, AGNTCY for infrastructure — moved from proprietary projects to open projects, integrating with the major cloud platforms; three of them are now under foundation governance — the evidence base documents no governance transfer for AP2 — and two have reached a first stable version (A2A v1.0; the MCP revision of 25 November 2025). On the other, Canadian financial institutions put agentic artificial intelligence into production — mortgage pre-adjudication, autonomous processing of commercial e-mail, enterprise agentic platforms — while the regulatory framework was being reorganized: OSFI Guideline E-23 and the AMF guideline on AI, both coming into force on 1 May 2027, the consumer-driven banking framework entrusted to the Bank of Canada, completion of the ISO 20022 migration on Lynx and the imminent launch of the Real-Time Rail.

This monograph advances an architectural thesis: **framed autonomy** (*autonomie encadrée*) is the convergent state of the art for deploying multi-agent systems in a regulated financial context. Three sources — the academic manifesto of Agentic Business Process Management, the empirical work on orchestration options, and IBM's agentic reference architecture — formulate the same principle: processes under strict regulatory requirements run within deterministic frameworks that orchestrate the agents, never the reverse. The book establishes that these three sources are not independent — two share an author, two an organization — and draws from this the exact scope of their convergence rather than overstating its authority (ch. 13). The monograph develops this thesis in seven parts: the protocols (I), enterprise orchestration (II), the Canadian regulatory framework (III), Canadian financial interoperability (IV), adoption by institutions (V), the architectural synthesis (VI) and a detailed enterprise integration platform blueprint instantiated on the IBM portfolio (VII).

The method is that of the PRD governing the book: a dated and cited factual evidence base, built through multi-judge adversarial verification and direct consultation of official sources, with explicit levels of evidence, systematic attribution of self-reported metrics, a strict distinction between documented link and author inference, and honest disclosure of gaps. Intended audiences: enterprise architects and technology leadership of Canadian financial institutions, risk and compliance officers, strategy leadership and researchers."""


def read_abstract():
    """L'abstract est le §Abstract de TOC.md (entre '## Abstract' et la ligne '(≈ … mots)')."""
    toc = TOC.read_text(encoding="utf-8")
    m = re.search(r"## Abstract\n(.*?)\n\*\(≈", toc, re.S)
    return m.group(1).strip()


def rebase_links(text, base):
    """Réécrit les cibles de liens relatives : elles sont résolues depuis le répertoire
    de la pièce (`base`), la sortie assemblée vit à la racine du volume. Sans cela un
    renvoi valide dans `monographie/03-partie-III/` pointe sur rien dans `Monographie.md`."""
    def sub(m):
        target = m.group(2)
        if re.match(r"^(?:[a-z][a-z0-9+.-]*:|[#/])", target):
            return m.group(0)
        return m.group(1) + posixpath.normpath(posixpath.join(base, target)) + m.group(3)
    return re.sub(r"(\]\()([^)\s]+)(\))", sub, text)


def clean_piece(text, prefix, rel):
    lines = text.split("\n")
    h1 = lines[0].rstrip()

    # --- séparer en-tête (jusqu'au 1er '---' seul) et corps ---
    sep = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            sep = i
            break
    header = lines[1:sep] if sep is not None else []
    body = lines[sep + 1:] if sep is not None else lines[1:]

    # --- thèse : la conserver, débarrassée du renvoi TOC.md ---
    these = ""
    for ln in header:
        if ln.lstrip().startswith("> **Thèse"):
            these = re.sub(r"\s*\(\[TOC\.md\]\([^)]*\)[^)]*\)", "", ln).rstrip()
            break

    body = "\n".join(body)

    # --- retirer le bloc de gouvernance HTML final <!-- … --> ---
    body = re.sub(r"\n?<!--.*?-->\s*$", "", body, flags=re.S)
    body = re.sub(r"\n?<!--.*?-->", "", body, flags=re.S)  # tout bloc HTML résiduel

    # --- retirer le titre « ## Notes » (les définitions restent) ---
    body = re.sub(r"(?m)^##\s+Notes\s*$", "", body)

    # --- retirer d'éventuels bandeaux « > ⚠ Correctif … » résiduels dans le corps ---
    body = re.sub(r"(?m)^> ⚠ \*\*(Correctif|Deux correctifs|Correctifs).*(?:\n>.*)*\n?", "", body)

    out = h1 + "\n"
    if these:
        out += "\n" + these + "\n"
    out += "\n" + body.strip("\n") + "\n"

    # --- préfixer les labels de notes pour éviter les collisions inter-pièces ---
    out = re.sub(r"\[\^([0-9]+)\]", lambda m: f"[^{prefix}-{m.group(1)}]", out)
    return rebase_links(out.strip("\n"), posixpath.dirname("monographie/" + rel))


def preamble():
    abstract = read_abstract()
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
  #text(size: 13pt)[Monographie — interopérabilité et orchestration agentique
  en écosystème d'entreprise de services financiers au Canada]

  #v(3cm)
  #text(size: 14pt, weight: "bold")[{AUTHOR}]

  #v(0.8cm)
  #text(size: 13pt)[{DATE}]
]
]
#pagebreak()
```

# Résumé {{.unnumbered}}

{abstract}

# Abstract {{.unnumbered}}

::: {{lang=en}}
{ABSTRACT_EN}
:::

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
contexte d'argumentation. L'Annexe B rassemble la matrice détaillée protocoles ×
réglementation, et l'Annexe D le glossaire bilingue qui tient lieu de liste d'abréviations.
"""


def main():
    parts = [preamble()]
    for rel, prefix in PIECES:
        if prefix in PART_TITLES:
            parts.append(f"# {PART_TITLES[prefix]}\n")
        text = (MONO / rel).read_text(encoding="utf-8")
        parts.append(clean_piece(text, prefix, rel))
    OUT.write_text("\n\n".join(parts) + "\n", encoding="utf-8", newline="\n")
    print(f"écrit -> {OUT}  ({len(parts)} blocs, {OUT.stat().st_size // 1024} Ko)")


if __name__ == "__main__":
    main()
