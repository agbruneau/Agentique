#!/usr/bin/env python3
"""Extracteur structurel intégral du Corpus Agentique (Markdown CommonMark strict).

Parse les 9 fichiers Markdown de ``Corpus/`` (``README.md`` et ``Tome 1`` à ``Tome 8``),
en respectant strictement la spécification CommonMark des blocs de code clôturés
(backticks `` ``` `` / ```` ```` ```` et tildes `` ~~~ `` de longueur >= 3) afin
qu'aucun commentaire ``# ...`` dans un bloc de code ne soit pris pour un titre.

Produit ``Cartographie/donnees/structure-integrale.json``.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass, field
from datetime import datetime, timezone
import json
from pathlib import Path
import re
from typing import Any

# Ordre canonique des 9 fichiers Markdown de Corpus/
CORPUS_FILES_ORDER: list[tuple[str, str, str]] = [
    ("R", "Corpus/README.md", "Index consolidé du Corpus"),
    (
        "T1",
        "Corpus/Tome 1 - Confiance protocolaire et encadrement financier.md",
        "Tome 1 — Confiance protocolaire et encadrement financier",
    ),
    (
        "T2",
        "Corpus/Tome 2 - Cadre normatif et exigences d'architecture.md",
        "Tome 2 — Cadre normatif et exigences d'architecture",
    ),
    (
        "T3",
        "Corpus/Tome 3 - Ingénierie du tissu conjonctif et état de l'art.md",
        "Tome 3 — Ingénierie du tissu conjonctif et état de l'art",
    ),
    (
        "T4",
        "Corpus/Tome 4 - Prospective stratégique et trajectoire 2028-2035.md",
        "Tome 4 — Prospective stratégique et trajectoire 2028–2035",
    ),
    (
        "T5",
        "Corpus/Tome 5 - Synthèse exécutive et concordance architecturale.md",
        "Tome 5 — Synthèse exécutive et concordance architecturale",
    ),
    (
        "T6",
        "Corpus/Tome 6 - Architecture multisectorielle et patrons de référence.md",
        "Tome 6 — Architecture multisectorielle et patrons de référence",
    ),
    (
        "T7",
        "Corpus/Tome 7 - Gouverner l'industrialisation cognitive.md",
        "Tome 7 — Gouverner l'industrialisation cognitive",
    ),
    (
        "T8",
        "Corpus/Tome 8 - Ingénierie exécutable et homologation vérifiable.md",
        "Tome 8 — Ingénierie exécutable et homologation vérifiable",
    ),
]

OPEN_FENCE_RE = re.compile(r"^( {0,3})(`{3,}|~{3,})(.*)$")
ATX_HEADING_RE = re.compile(r"^ {0,3}(#{1,6})(?:[ \t]+(.*?))?[ \t]*$")
TRAILING_HASH_RE = re.compile(r"[ \t]+#+[ \t]*$")

IDENTIFIER_PATTERNS: tuple[re.Pattern[str], ...] = (
    re.compile(r"\bEXIG-[A-Z0-9]+(?:-[A-Z0-9]+)*\b"),
    re.compile(r"\bCAP-[A-Z0-9]+(?:-[A-Z0-9]+)*\b"),
    re.compile(r"\bPEX-[A-Z0-9]+(?:-[A-Z0-9]+)*\b"),
    re.compile(r"\bPRR-75\b"),
    re.compile(r"\bCRE-IA-2026-01\b"),
    re.compile(r"\b2027-B001\b"),
    re.compile(r"\bDIV-0[1-9]\b"),
    re.compile(r"\bDISC-0[1-9]\b"),
    re.compile(r"\bOO[1-4]\b"),
    re.compile(r"\bSBB-[A-Z]+(?:-[A-Z]+)*\b"),
    re.compile(r"\bADR-[0-9]{1,3}\b"),
    re.compile(r"\bASI(?:0[1-9]|10)\b"),
    re.compile(r"\bCA-(?:[0-9]{2}|G0-SYNC)\b"),
    re.compile(r"\bC(?:0[1-9]|[1-3][0-9]|40)\b"),
    re.compile(r"\bL[0-4]\b"),
    re.compile(r"\bG[0-5]\b"),
    re.compile(r"\bT(?:10|[1-9])\b"),
    re.compile(r"\bE[1-3]\b"),
    re.compile(r"\bP[0-3]\b"),
    re.compile(r"\bRQ[1-6]\b"),
    re.compile(r"\bDC-P12\b"),
    re.compile(r"\bAO-0[1-9]\b"),
)


@dataclass
class FencedBlock:
    """Bloc de code clôturé détecté selon CommonMark §4.5."""

    line_start: int
    line_end: int
    fence_char: str
    fence_length: int
    info: str


@dataclass
class HeadingItem:
    """Titre ATX extrait hors blocs de code."""

    unit_id: str
    tome_id: str
    level: int
    kind: str
    title: str
    line_start: int
    line_end: int = 0
    word_count: int = 0
    own_word_count: int = 0
    part_title: str | None = None
    identifiers: list[str] = field(default_factory=list)
    children: list[HeadingItem] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        """Convertit le nœud en dictionnaire sérialisable JSON."""
        return {
            "unit_id": self.unit_id,
            "tome_id": self.tome_id,
            "level": self.level,
            "kind": self.kind,
            "title": self.title,
            "line_start": self.line_start,
            "line_end": self.line_end,
            "word_count": self.word_count,
            "own_word_count": self.own_word_count,
            "part_title": self.part_title,
            "identifiers": self.identifiers,
            "children": [child.to_dict() for child in self.children],
        }


def detect_identifiers(text: str) -> list[str]:
    """Détecte les identifiants normatifs et structurants dans un extrait de texte."""
    found: set[str] = set()
    for pat in IDENTIFIER_PATTERNS:
        found.update(pat.findall(text))
    return sorted(found)


def classify_heading(tome_id: str, level: int, title: str) -> str:
    """Détermine la nature structurelle (kind) d'un titre Markdown."""
    low = title.lower().strip()
    if level == 1 and (
        low.startswith("table des matières")
        or low.startswith("liste des tableaux")
        or low.startswith("liste des figures")
    ):
        return "toc"
    if level == 1 and (
        low.startswith("tome ")
        or low.startswith("suite intégrale")
    ):
        return "document"
    if level == 1 and (
        low.startswith("livre ")
        or low.startswith("partie ")
    ):
        return "part"
    if (level == 1 and low.startswith("annexe")) or (
        level == 2 and (low.startswith("annexe") or (tome_id == "T2" and re.match(r"^[A-H]\s+[A-ZÉÈÊÀ]", title)))
    ):
        return "annex"
    if level == 1 and (
        low.startswith("liminaire")
        or low.startswith("à propos")
        or low.startswith("historique")
        or low.startswith("méthode")
        or low.startswith("sommaire exécutif")
        or low.startswith("synthèse exécutive")
        or low.startswith("ouverture")
    ):
        return "liminaire"
    if tome_id == "T6" and level == 1 and low.startswith("chapitre "):
        return "chapter"
    if level == 2 and (
        low.startswith("chapitre ")
        or (tome_id == "T1" and re.match(r"^\d+\s*·", title))
        or (tome_id == "T2" and re.match(r"^\d+\s+[A-ZÉÈÊÀ]", title))
        or (tome_id == "R")
    ):
        return "chapter"
    if level == 2 and re.match(r"^0\.\d+\b", title):
        return "liminaire"
    return "section"


def parse_markdown_lines(lines: list[str]) -> tuple[list[tuple[int, int, str]], list[FencedBlock], set[int]]:
    """Parse des lignes Markdown selon CommonMark §4.2 (titres ATX) et §4.5 (blocs clôturés).

    Retourne :
      - la liste des titres ``(line_no_1based, level, title)`` hors blocs de code ;
      - la liste des blocs de code clôturés détectés ;
      - l'ensemble des numéros de ligne (1-based) situés à l'intérieur des blocs de code.
    """
    headings: list[tuple[int, int, str]] = []
    fenced_blocks: list[FencedBlock] = []
    code_line_numbers: set[int] = set()

    in_fence = False
    fence_char = ""
    fence_len = 0
    fence_start = 0
    fence_info = ""

    for idx, line in enumerate(lines, start=1):
        if not in_fence:
            m_open = OPEN_FENCE_RE.match(line)
            if m_open:
                seq = m_open.group(2)
                char = seq[0]
                info = m_open.group(3)
                # CommonMark §4.5 : l'info string d'un bloc backtick ne peut contenir de backtick
                if not (char == "`" and "`" in info):
                    in_fence = True
                    fence_char = char
                    fence_len = len(seq)
                    fence_start = idx
                    fence_info = info.strip()
                    code_line_numbers.add(idx)
                    continue
        else:
            code_line_numbers.add(idx)
            close_pat = re.compile(
                rf"^ {{0,3}}{re.escape(fence_char)}{{{fence_len},}}[ \t]*$"
            )
            if close_pat.match(line):
                fenced_blocks.append(
                    FencedBlock(
                        line_start=fence_start,
                        line_end=idx,
                        fence_char=fence_char,
                        fence_length=fence_len,
                        info=fence_info,
                    )
                )
                in_fence = False
                fence_char = ""
                fence_len = 0
                fence_start = 0
                fence_info = ""
            continue

        m_head = ATX_HEADING_RE.match(line)
        if m_head:
            level = len(m_head.group(1))
            raw_title = m_head.group(2) or ""
            # Retrait de la séquence fermante optionnelle de # précédée d'espace/tab (CommonMark §4.2)
            title = TRAILING_HASH_RE.sub("", raw_title).strip()
            # Cas limite où le titre ne contenait que des # (ex: "## ###")
            if title and set(title) == {"#"}:
                title = ""
            headings.append((idx, level, title))

    if in_fence:
        fenced_blocks.append(
            FencedBlock(
                line_start=fence_start,
                line_end=len(lines),
                fence_char=fence_char,
                fence_length=fence_len,
                info=fence_info,
            )
        )

    return headings, fenced_blocks, code_line_numbers


def build_heading_tree(
    tome_id: str,
    lines: list[str],
    raw_headings: list[tuple[int, int, str]],
    code_line_numbers: set[int],
) -> tuple[list[HeadingItem], list[HeadingItem]]:
    """Construit l'arbre hiérarchique H1..H6 et calcule plages de lignes, mots et identifiants."""
    total_lines = len(lines)
    nodes: list[HeadingItem] = []
    current_part: str | None = None

    for seq_idx, (line_no, level, title) in enumerate(raw_headings, start=1):
        kind = classify_heading(tome_id, level, title)
        if level == 1 and kind in ("part", "liminaire", "annex"):
            current_part = title
        elif level == 1 and kind == "document":
            current_part = None
        unit_id = f"{tome_id.lower()}-u{seq_idx:04d}"
        nodes.append(
            HeadingItem(
                unit_id=unit_id,
                tome_id=tome_id,
                level=level,
                kind=kind,
                title=title,
                line_start=line_no,
                part_title=current_part,
            )
        )

    # Calcul de line_end pour chaque titre : jusqu'au prochain titre de niveau <= level
    for i, node in enumerate(nodes):
        end_line = total_lines
        for j in range(i + 1, len(nodes)):
            if nodes[j].level <= node.level:
                end_line = nodes[j].line_start - 1
                break
        node.line_end = max(node.line_start, end_line)

    # Construction de l'arbre par pile monotone
    roots: list[HeadingItem] = []
    stack: list[HeadingItem] = []
    for node in nodes:
        while stack and stack[-1].level >= node.level:
            stack.pop()
        if stack:
            stack[-1].children.append(node)
        else:
            roots.append(node)
        stack.append(node)

    # Pré-calcul des mots par ligne pour O(1) par intervalle
    prefix_words = [0] * (total_lines + 1)
    for idx, line in enumerate(lines, start=1):
        prefix_words[idx] = prefix_words[idx - 1] + len(line.split())

    # Calcul own_word_count, word_count et identifiants détectés hors blocs de code
    for node in nodes:
        node.word_count = prefix_words[node.line_end] - prefix_words[node.line_start - 1]
        if node.children:
            own_end = node.children[0].line_start - 1
        else:
            own_end = node.line_end
        own_end = max(node.line_start, own_end)
        node.own_word_count = prefix_words[own_end] - prefix_words[node.line_start - 1]

        # Détection d'identifiants sur les lignes propres (hors code) puis fusion ascendante
        own_text = "\n".join(
            lines[ln - 1]
            for ln in range(node.line_start, own_end + 1)
            if ln not in code_line_numbers
        )
        node.identifiers = detect_identifiers(own_text)

    def propagate_identifiers(node: HeadingItem) -> set[str]:
        acc = set(node.identifiers)
        for child in node.children:
            acc.update(propagate_identifiers(child))
        node.identifiers = sorted(acc)
        return acc

    for root in roots:
        propagate_identifiers(root)

    return roots, nodes


def extract_corpus_structure(repo_root: Path) -> dict[str, Any]:
    """Extrait la structure intégrale des 9 fichiers Markdown de ``Corpus/``."""
    files_payload: list[dict[str, Any]] = []
    total_lines = 0
    total_words = 0
    total_headings = 0
    total_fences = 0
    headings_by_level_global = {f"H{lvl}": 0 for lvl in range(1, 7)}
    global_identifiers: set[str] = set()

    for tome_id, rel_path, default_title in CORPUS_FILES_ORDER:
        file_path = repo_root / rel_path
        if not file_path.is_file():
            raise FileNotFoundError(f"Fichier Corpus introuvable : {file_path}")
        raw_text = file_path.read_text(encoding="utf-8")
        lines = raw_text.splitlines()
        line_count = len(lines)
        word_count = len(raw_text.split())

        raw_headings, fenced_blocks, code_lines = parse_markdown_lines(lines)
        roots, flat_nodes = build_heading_tree(tome_id, lines, raw_headings, code_lines)

        by_level = {f"H{lvl}": 0 for lvl in range(1, 7)}
        for _, lvl, _ in raw_headings:
            key = f"H{lvl}"
            by_level[key] += 1
            headings_by_level_global[key] += 1

        file_ids: set[str] = set()
        for r in roots:
            file_ids.update(r.identifiers)
        global_identifiers.update(file_ids)

        doc_title = default_title
        for r in roots:
            if r.level == 1 and r.title:
                if r.kind == "document" or tome_id in ("R",):
                    doc_title = r.title
                break

        files_payload.append(
            {
                "tome_id": tome_id,
                "file": rel_path,
                "filename": Path(rel_path).name,
                "title": doc_title,
                "line_count": line_count,
                "word_count": word_count,
                "heading_count": len(flat_nodes),
                "headings_by_level": by_level,
                "fenced_code_blocks_count": len(fenced_blocks),
                "identifiers_count": len(file_ids),
                "identifiers": sorted(file_ids),
                "tree": [r.to_dict() for r in roots],
            }
        )

        total_lines += line_count
        total_words += word_count
        total_headings += len(flat_nodes)
        total_fences += len(fenced_blocks)

    return {
        "schema_version": "1.0.0",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "generator": "Tomes/Cartographie/outils/extraire_structure.py",
        "totals": {
            "files": len(files_payload),
            "lines": total_lines,
            "words": total_words,
            "headings": total_headings,
            "headings_by_level": headings_by_level_global,
            "fenced_code_blocks": total_fences,
            "unique_identifiers": len(global_identifiers),
        },
        "files": files_payload,
    }


def main() -> int:
    """Point d'entrée CLI pour l'extraction structurelle du Corpus."""
    parser = argparse.ArgumentParser(
        description="Extrait l'arbre hiérarchique H1–H6 des 9 fichiers Markdown de Corpus/."
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path(__file__).resolve().parents[3],
        help="Racine du dépôt Agentique (défaut : 3 niveaux au-dessus du script).",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Chemin du JSON produit (défaut : <repo-root>/Tomes/Cartographie/donnees/structure-integrale.json).",
    )
    args = parser.parse_args()

    repo_root = args.repo_root.resolve()
    output_path = (
        args.output.resolve()
        if args.output
        else repo_root / "Tomes" / "Cartographie" / "donnees" / "structure-integrale.json"
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)

    payload = extract_corpus_structure(repo_root)
    output_path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )

    totals = payload["totals"]
    print(
        f"Extraction terminée : {totals['files']} fichiers, {totals['lines']} lignes, "
        f"{totals['words']} mots, {totals['headings']} titres H1–H6, "
        f"{totals['fenced_code_blocks']} blocs de code filtrés, "
        f"{totals['unique_identifiers']} identifiants uniques -> {output_path}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
