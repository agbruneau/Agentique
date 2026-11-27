#!/usr/bin/env python3
"""Extracteur structurel intégral du Compendium de l'entreprise agentique (CommonMark strict).

Parse en CommonMark strict :
- ``Compendium/README.md`` (section ``R``)
- ``Compendium/Compendium.md`` découpé selon ses 14 sections ``H1`` (``LIM``, ``P01``..``P12``, ``ANN``)
en conservant les numéros de lignes exacts ``1..8670`` de ``Compendium/Compendium.md`` et en
rattachant chaque unité (``00-liminaire``, ``ch01..ch36``, ``annexe-a..annexe-e``) à son
``compendium_unit_id`` et à son ``source_file`` déclarés dans ``manifest.json``.

Produit ``Sources/Cartographie/donnees/structure-integrale.json``.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass, field
from datetime import datetime, timezone
import json
from pathlib import Path
import re
import sys
from typing import Any

TOOLS_DIR = Path(__file__).resolve().parent
if str(TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(TOOLS_DIR))

ROMAN_TO_PART_ID: dict[str, str] = {
    "I": "P01",
    "II": "P02",
    "III": "P03",
    "IV": "P04",
    "V": "P05",
    "VI": "P06",
    "VII": "P07",
    "VIII": "P08",
    "IX": "P09",
    "X": "P10",
    "XI": "P11",
    "XII": "P12",
}

COMPENDIUM_SECTIONS_ORDER: tuple[str, ...] = (
    "R",
    "LIM",
    "P01",
    "P02",
    "P03",
    "P04",
    "P05",
    "P06",
    "P07",
    "P08",
    "P09",
    "P10",
    "P11",
    "P12",
    "ANN",
)

SECTION_DEFAULT_ROLES: dict[str, str] = {
    "R": "synthese",
    "LIM": "synthese",
    "P01": "fondation",
    "P02": "architecture",
    "P03": "etat_de_l_art",
    "P04": "etat_de_l_art",
    "P05": "patron",
    "P06": "norme",
    "P07": "gouvernance",
    "P08": "gouvernance",
    "P09": "norme",
    "P10": "patron",
    "P11": "prospective",
    "P12": "executable",
    "ANN": "synthese",
}

OPEN_FENCE_RE = re.compile(r"^( {0,3})(`{3,}|~{3,})(.*)$")
ATX_HEADING_RE = re.compile(r"^ {0,3}(#{1,6})(?:[ \t]+(.*?))?[ \t]*$")
TRAILING_HASH_RE = re.compile(r"[ \t]+#+[ \t]*$")

IDENTIFIER_PATTERNS: tuple[re.Pattern[str], ...] = (
    re.compile(r"\bSCH-(?:\d{2}|A[A-E])-\d{2}\b"),
    re.compile(r"\bSRC-\d{3}\b"),
    re.compile(r"\bPOR-\d{3}\b"),
    re.compile(r"\bSIG-\d{3}\b"),
    re.compile(r"\bINI-\d{3}\b"),
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
    re.compile(r"\bDC-P(?:0[1-9]|1[0-2])\b"),
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
    section_id: str
    level: int
    kind: str
    title: str
    line_start: int
    line_end: int = 0
    word_count: int = 0
    own_word_count: int = 0
    part_title: str | None = None
    compendium_unit_id: str | None = None
    source_file: str | None = None
    identifiers: list[str] = field(default_factory=list)
    pdf_page_start: int | None = None
    pdf_page_end: int | None = None
    reading_minutes: int = 1
    guiding_question: str | None = None
    excerpt: str = ""
    children: list[HeadingItem] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        """Convertit le nœud en dictionnaire sérialisable JSON."""
        return {
            "unit_id": self.unit_id,
            "tome_id": self.tome_id,
            "section_id": self.section_id,
            "level": self.level,
            "kind": self.kind,
            "title": self.title,
            "line_start": self.line_start,
            "line_end": self.line_end,
            "word_count": self.word_count,
            "own_word_count": self.own_word_count,
            "reading_minutes": self.reading_minutes,
            "pdf_page_start": self.pdf_page_start,
            "pdf_page_end": self.pdf_page_end,
            "guiding_question": self.guiding_question,
            "excerpt": self.excerpt,
            "part_title": self.part_title,
            "compendium_unit_id": self.compendium_unit_id,
            "source_file": self.source_file,
            "identifiers": self.identifiers,
            "children": [child.to_dict() for child in self.children],
        }


def detect_identifiers(text: str) -> list[str]:
    """Détecte les identifiants normatifs et structurants dans un extrait de texte."""
    found: set[str] = set()
    for pat in IDENTIFIER_PATTERNS:
        found.update(pat.findall(text))
    return sorted(found)


def _match_compendium_unit(section_id: str, level: int, title: str) -> str | None:
    """Rattache un titre H1/H2 du Compendium à son ``compendium_unit_id`` du manifeste."""
    low = title.lower().strip()
    if section_id == "LIM" and level == 1 and low.startswith("liminaire"):
        return "00-liminaire"
    if level == 2:
        m_ch = re.match(r"^Chapitre\s+(\d{2})\b", title, flags=re.IGNORECASE)
        if m_ch:
            return f"ch{m_ch.group(1)}"
        if section_id == "ANN":
            m_ann = re.match(r"^Annexe\s+([A-E])\b", title, flags=re.IGNORECASE)
            if m_ann:
                return f"annexe-{m_ann.group(1).lower()}"
    return None


def classify_heading(tome_id: str, level: int, title: str) -> str:
    """Détermine la nature structurelle (kind) d'un titre Markdown."""
    low = title.lower().strip()
    if (level == 1 or (tome_id == "LIM" and level == 2)) and (
        low.startswith("table des matières")
        or low.startswith("liste des tableaux")
        or low.startswith("liste des figures")
    ):
        return "toc"
    if tome_id == "R" and level == 1:
        return "document"
    if tome_id == "R" and level == 2:
        return "section"
    if level == 1 and (low.startswith("partie ") or low.startswith("livre ")):
        return "part"
    if (level == 1 and low.startswith("annexe")) or (level == 2 and low.startswith("annexe ")):
        return "annex"
    if level == 1 and low.startswith("liminaire"):
        return "liminaire"
    if level == 2 and re.match(r"^Chapitre\s+\d{2}\b", title, flags=re.IGNORECASE):
        return "chapter"
    if level == 2 and re.match(r"^0\.\d+\b", title):
        return "liminaire"
    if level == 2 and low.startswith("références du liminaire"):
        return "references"
    if level == 3 and low.startswith("références"):
        return "references"
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
    *,
    slice_end_line: int | None = None,
    unit_source_map: dict[str, str] | None = None,
    pdf_index: Any | None = None,
) -> tuple[list[HeadingItem], list[HeadingItem]]:
    """Construit l'arbre hiérarchique H1..H6 et calcule plages de lignes, mots, pages PDF, extraits et identifiants."""
    from index_pdf_compendium import clean_prose_excerpt  # noqa: E402

    total_lines = min(len(lines), slice_end_line) if slice_end_line else len(lines)
    nodes: list[HeadingItem] = []
    current_part: str | None = None
    unit_map = unit_source_map or {}

    for seq_idx, (line_no, level, title) in enumerate(raw_headings, start=1):
        kind = classify_heading(tome_id, level, title)
        if level == 1 and kind in ("part", "liminaire", "annex"):
            current_part = title
        elif level == 1 and kind == "document":
            current_part = None
        cid = _match_compendium_unit(tome_id, level, title)
        src_file = unit_map.get(cid) if cid else None
        unit_id = f"{tome_id.lower()}-u{seq_idx:04d}"
        nodes.append(
            HeadingItem(
                unit_id=unit_id,
                tome_id=tome_id,
                section_id=tome_id,
                level=level,
                kind=kind,
                title=title,
                line_start=line_no,
                part_title=current_part,
                compendium_unit_id=cid,
                source_file=src_file,
            )
        )

    # Calcul de line_end pour chaque titre : jusqu'au prochain titre de niveau <= level dans la section
    for i, node in enumerate(nodes):
        end_line = total_lines
        for j in range(i + 1, len(nodes)):
            if nodes[j].level <= node.level:
                end_line = nodes[j].line_start - 1
                break
        node.line_end = max(node.line_start, end_line)

    # Construction de l'arbre par pile monotone + héritage de compendium_unit_id/source_file
    roots: list[HeadingItem] = []
    stack: list[HeadingItem] = []
    for node in nodes:
        while stack and stack[-1].level >= node.level:
            stack.pop()
        if stack:
            parent = stack[-1]
            if node.compendium_unit_id is None and parent.compendium_unit_id is not None:
                node.compendium_unit_id = parent.compendium_unit_id
                node.source_file = parent.source_file
            parent.children.append(node)
        else:
            roots.append(node)
        stack.append(node)

    # Pré-calcul des mots par ligne sur le fichier complet pour indexation exacte 1..len(lines)
    prefix_words = [0] * (len(lines) + 1)
    for idx, line in enumerate(lines, start=1):
        prefix_words[idx] = prefix_words[idx - 1] + len(line.split())

    for node in nodes:
        node.word_count = prefix_words[node.line_end] - prefix_words[node.line_start - 1]
        node.reading_minutes = max(1, round(node.word_count / 220))
        if node.children:
            own_end = node.children[0].line_start - 1
        else:
            own_end = node.line_end
        own_end = max(node.line_start, own_end)
        node.own_word_count = prefix_words[own_end] - prefix_words[node.line_start - 1]

        own_text = "\n".join(
            lines[ln - 1]
            for ln in range(node.line_start, own_end + 1)
            if ln not in code_line_numbers
        )
        node.identifiers = detect_identifiers(own_text)

        gq, exc = clean_prose_excerpt(lines, node.line_start, node.line_end, code_line_numbers)
        node.guiding_question = gq
        node.excerpt = exc

        if pdf_index is not None:
            span = pdf_index.heading_pages_by_line.get(node.line_start)
            if span is not None:
                node.pdf_page_start, node.pdf_page_end = span
            else:
                p_start = pdf_index.resolve_line_page(node.line_start, [node.title])
                p_end = max(p_start, pdf_index.resolve_line_page(node.line_end))
                node.pdf_page_start, node.pdf_page_end = p_start, p_end

    def propagate_identifiers(node: HeadingItem) -> set[str]:
        acc = set(node.identifiers)
        for child in node.children:
            acc.update(propagate_identifiers(child))
        node.identifiers = sorted(acc)
        return acc

    for root in roots:
        propagate_identifiers(root)

    return roots, nodes


def _section_id_for_h1(title: str) -> str:
    """Associe un titre H1 de ``Compendium/Compendium.md`` à son identifiant canonique (LIM, P01..P12, ANN)."""
    low = title.lower().strip()
    if low.startswith("liminaire"):
        return "LIM"
    if low.startswith("annexes"):
        return "ANN"
    m_part = re.match(r"^Partie\s+(XII|XI|IX|X|VIII|VII|VI|IV|V|III|II|I)\b", title, flags=re.IGNORECASE)
    if m_part:
        return ROMAN_TO_PART_ID[m_part.group(1).upper()]
    raise ValueError(f"Section H1 non reconnue dans Compendium/Compendium.md : {title!r}")


def _load_unit_source_map(repo_root: Path) -> dict[str, str]:
    """Charge la table ``unit_id -> Sources/Compendium/ouvrage/manuscrit/...`` depuis ``manifest.json``."""
    manifest_path = repo_root / "Sources" / "Compendium" / "ouvrage" / "specs" / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    return {
        u["id"]: f"Sources/Compendium/ouvrage/{u['file']}"
        for u in manifest.get("units", [])
    }


def _build_section_payload(
    *,
    section_id: str,
    rel_path: str,
    title: str,
    lines: list[str],
    raw_headings: list[tuple[int, int, str]],
    fenced_blocks: list[FencedBlock],
    code_lines: set[int],
    slice_start_line: int,
    slice_end_line: int,
    unit_source_map: dict[str, str] | None,
    pdf_index: Any | None = None,
) -> tuple[dict[str, Any], int]:
    """Construit l'entrée JSON pour une section (``R`` ou ``LIM..ANN``)."""
    roots, flat_nodes = build_heading_tree(
        section_id,
        lines,
        raw_headings,
        code_lines,
        slice_end_line=slice_end_line,
        unit_source_map=unit_source_map,
        pdf_index=pdf_index,
    )
    by_level = {f"H{lvl}": 0 for lvl in range(1, 7)}
    for _, lvl, _ in raw_headings:
        by_level[f"H{lvl}"] += 1

    file_ids: set[str] = set()
    for r in roots:
        file_ids.update(r.identifiers)

    slice_word_count = sum(len(lines[ln - 1].split()) for ln in range(slice_start_line, slice_end_line + 1))
    slice_fenced = sum(
        1 for fb in fenced_blocks if slice_start_line <= fb.line_start <= slice_end_line
    )
    mapped_units = sorted({n.compendium_unit_id for n in flat_nodes if n.compendium_unit_id})

    pdf_starts = [n.pdf_page_start for n in flat_nodes if n.pdf_page_start is not None]
    pdf_ends = [n.pdf_page_end for n in flat_nodes if n.pdf_page_end is not None]

    payload = {
        "tome_id": section_id,
        "section_id": section_id,
        "file": rel_path,
        "filename": Path(rel_path).name,
        "title": title,
        "line_start": slice_start_line,
        "line_end": slice_end_line,
        "line_count": slice_end_line - slice_start_line + 1,
        "word_count": slice_word_count,
        "reading_minutes": max(1, round(slice_word_count / 220)),
        "pdf_page_start": min(pdf_starts) if pdf_starts else None,
        "pdf_page_end": max(pdf_ends) if pdf_ends else None,
        "heading_count": len(flat_nodes),
        "headings_by_level": by_level,
        "fenced_code_blocks_count": slice_fenced,
        "compendium_units": mapped_units,
        "identifiers_count": len(file_ids),
        "identifiers": sorted(file_ids),
        "tree": [r.to_dict() for r in roots],
    }
    return payload, slice_fenced


def extract_corpus_structure(repo_root: Path) -> dict[str, Any]:
    """Extrait la structure intégrale de ``Compendium/README.md`` (``R``) et ``Compendium/Compendium.md`` (14 sections H1)."""
    from index_pdf_compendium import CompendiumPdfIndex  # noqa: E402

    unit_source_map = _load_unit_source_map(repo_root)
    pdf_index = None
    if (repo_root / "Compendium" / "Compendium.pdf").is_file() and (repo_root / "Compendium" / "Compendium.md").is_file():
        pdf_index = CompendiumPdfIndex.from_repo(repo_root)
    sections_payload: list[dict[str, Any]] = []
    headings_by_level_global = {f"H{lvl}": 0 for lvl in range(1, 7)}
    global_identifiers: set[str] = set()
    mapped_units_all: set[str] = set()
    total_lines = 0
    total_words = 0
    total_headings = 0
    total_fences = 0

    # 1. Index éditorial : Compendium/README.md -> section_id="R"
    readme_rel = "Compendium/README.md"
    readme_path = repo_root / readme_rel
    if not readme_path.is_file():
        raise FileNotFoundError(f"Index Compendium introuvable : {readme_path}")
    r_text = readme_path.read_text(encoding="utf-8")
    r_lines = r_text.splitlines()
    r_headings, r_fenced, r_code = parse_markdown_lines(r_lines)
    r_title = r_headings[0][2] if r_headings else "Compendium de l'entreprise agentique"
    r_sec, r_fcnt = _build_section_payload(
        section_id="R",
        rel_path=readme_rel,
        title=r_title,
        lines=r_lines,
        raw_headings=r_headings,
        fenced_blocks=r_fenced,
        code_lines=r_code,
        slice_start_line=1,
        slice_end_line=len(r_lines),
        unit_source_map=None,
    )
    sections_payload.append(r_sec)
    for k, v in r_sec["headings_by_level"].items():
        headings_by_level_global[k] += v
    global_identifiers.update(r_sec["identifiers"])
    total_lines += r_sec["line_count"]
    total_words += r_sec["word_count"]
    total_headings += r_sec["heading_count"]
    total_fences += r_fcnt

    # 2. Ouvrage maître : Compendium/Compendium.md -> 14 sections H1 (LIM, P01..P12, ANN)
    comp_rel = "Compendium/Compendium.md"
    comp_path = repo_root / comp_rel
    if not comp_path.is_file():
        raise FileNotFoundError(f"Compendium Markdown introuvable : {comp_path}")
    c_text = comp_path.read_text(encoding="utf-8")
    c_lines = c_text.splitlines()
    c_headings, c_fenced, c_code = parse_markdown_lines(c_lines)

    h1_indices = [idx for idx, (_, lvl, _) in enumerate(c_headings) if lvl == 1]
    if len(h1_indices) != 14:
        raise ValueError(f"14 sections H1 attendues dans {comp_rel}, trouvées {len(h1_indices)}")

    for pos, h1_idx in enumerate(h1_indices):
        h1_line, _, h1_title = c_headings[h1_idx]
        sec_id = _section_id_for_h1(h1_title)
        slice_start = 1 if pos == 0 else h1_line
        if pos + 1 < len(h1_indices):
            next_h1_line = c_headings[h1_indices[pos + 1]][0]
            slice_end = next_h1_line - 1
        else:
            slice_end = len(c_lines)

        slice_headings = [
            h for h in c_headings if slice_start <= h[0] <= slice_end
        ]
        sec_obj, sec_fcnt = _build_section_payload(
            section_id=sec_id,
            rel_path=comp_rel,
            title=h1_title,
            lines=c_lines,
            raw_headings=slice_headings,
            fenced_blocks=c_fenced,
            code_lines=c_code,
            slice_start_line=slice_start,
            slice_end_line=slice_end,
            unit_source_map=unit_source_map,
            pdf_index=pdf_index,
        )
        sections_payload.append(sec_obj)
        for k, v in sec_obj["headings_by_level"].items():
            headings_by_level_global[k] += v
        global_identifiers.update(sec_obj["identifiers"])
        mapped_units_all.update(sec_obj["compendium_units"])
        total_lines += sec_obj["line_count"]
        total_words += sec_obj["word_count"]
        total_headings += sec_obj["heading_count"]
        total_fences += sec_fcnt

    return {
        "schema_version": "2.0.0",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "generator": "Sources/Cartographie/outils/extraire_structure.py",
        "totals": {
            "files": len(sections_payload),
            "sections": len(sections_payload),
            "compendium_units_mapped": len(mapped_units_all),
            "compendium_lines": len(c_lines),
            "compendium_headings": len(c_headings),
            "lines": total_lines,
            "words": total_words,
            "headings": total_headings,
            "headings_by_level": headings_by_level_global,
            "fenced_code_blocks": total_fences,
            "unique_identifiers": len(global_identifiers),
        },
        "files": sections_payload,
    }


def main() -> int:
    """Point d'entrée CLI pour l'extraction structurelle du Compendium."""
    parser = argparse.ArgumentParser(
        description="Extrait l'arbre hiérarchique H1–H6 de Compendium/README.md et Compendium/Compendium.md."
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
        help="Chemin du JSON produit (défaut : <repo-root>/Sources/Cartographie/donnees/structure-integrale.json).",
    )
    args = parser.parse_args()

    repo_root = args.repo_root.resolve()
    output_path = (
        args.output.resolve()
        if args.output
        else repo_root / "Sources" / "Cartographie" / "donnees" / "structure-integrale.json"
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
        f"Extraction Compendium terminée : {totals['sections']} sections ({totals['compendium_units_mapped']} unités), "
        f"{totals['compendium_lines']} lignes Compendium.md ({totals['compendium_headings']} titres), "
        f"{totals['lines']} lignes totales, {totals['words']} mots, {totals['headings']} titres H1–H6, "
        f"{totals['fenced_code_blocks']} blocs de code filtrés, "
        f"{totals['unique_identifiers']} identifiants uniques -> {output_path}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
