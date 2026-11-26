#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Indexeur PDF déterministe pour ``Compendium/Compendium.pdf``.

Aligne les `403` titres de ``Compendium/Compendium.md`` sur les `402` signets TOC
du PDF (plus la Table des matières) et localise la page exacte des `115` figures
``SCH-00-01`` à ``SCH-36-04`` ainsi que toute ligne arbitraire.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
import sys
import unicodedata

import pymupdf

TOOLS_DIR = Path(__file__).resolve().parent
if str(TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(TOOLS_DIR))

import extraire_structure as es  # noqa: E402

_MD_IMAGE_RE = re.compile(r"!\[[^\]]*\]\([^)]*\)")
_MD_LINK_RE = re.compile(r"\[([^\]]+)\]\([^)]+\)")
_AUTOLINK_RE = re.compile(r"<(?:https?://|mailto:|ftp://)[^>]+>")
_CITATION_RE = re.compile(r"\s*\[(\d+(?:\s*,\s*\d+)*)\]")
_CAPTION_LINE_RE = re.compile(r"^\*(?:Figure|Tableau)\s+[^\n]+\*$")
_GUIDING_Q_RE = re.compile(r"\*+Question directrice\s*:\s*\*?\s*(.+)")


def _norm_for_search(text: str) -> str:
    """Normalise en minuscules sans accents ni espaces multiples."""
    decomposed = unicodedata.normalize("NFD", str(text or "").lower())
    stripped = "".join(ch for ch in decomposed if unicodedata.category(ch) != "Mn")
    return re.sub(r"\s+", " ", stripped).strip()


def _clean_prose_text(raw: str) -> str:
    """Nettoie un extrait Markdown selon la charte fr-CA sans casser le code inline."""
    s = raw.replace(r"\$", "$")
    s = _MD_IMAGE_RE.sub(" ", s)
    s = _MD_LINK_RE.sub(r"\1", s)
    s = _AUTOLINK_RE.sub(" ", s)
    s = _CITATION_RE.sub("", s)
    s = re.sub(r"\bL([1-9]\d*)-L?([1-9]\d*)\b", r"L\1–L\2", s)

    parts = re.split(r"(`[^`]*`)", s)
    for idx in range(0, len(parts), 2):
        part = parts[idx]
        part = part.replace("<->", "↔").replace("->", "→")
        part = re.sub(r"(?<![<>=])<=(?!=)", "≤", part)
        part = re.sub(r"(?<![<>=])>=(?!=)", "≥", part)
        part = (
            part.replace("Systems of Agency", "Systèmes d'agentivité")
            .replace("System of Agency", "Système d'agentivité")
            .replace("systems of agency", "systèmes d'agentivité")
        )
        part = re.sub(r"\*\*([^*]+)\*\*", r"\1", part)
        part = re.sub(r"\*([^*]+)\*", r"\1", part)
        parts[idx] = part
    return re.sub(r"\s+", " ", "".join(parts)).strip()


def _truncate_clean(text: str, max_chars: int = 460) -> str:
    """Tronque proprement sur une limite de mot sans couper un span backtick."""
    if len(text) <= max_chars:
        return text
    cut = text[:max_chars].rsplit(" ", 1)[0].rstrip(" ,;:-—")
    # Éviter de laisser un backtick ouvert si coupé en plein milieu
    if cut.count("`") % 2 == 1:
        last_bt = cut.rfind("`")
        if last_bt > 40:
            cut = cut[:last_bt].rstrip(" ,;:-—")
    return f"{cut}…"


def clean_prose_excerpt(
    lines: list[str],
    line_start: int,
    line_end: int,
    code_lines: set[int],
    max_chars: int = 460,
) -> tuple[str | None, str]:
    """Extrait ``(guiding_question, excerpt)`` pour une section de ``Compendium.md``."""
    hi = min(len(lines), max(line_start, line_end))
    lo = max(1, line_start)

    guiding_question: str | None = None
    probe_hi = min(hi, lo + 18)
    for ln in range(lo, probe_hi + 1):
        if ln in code_lines:
            continue
        m_q = _GUIDING_Q_RE.search(lines[ln - 1].strip())
        if m_q:
            guiding_question = _clean_prose_text(m_q.group(1).strip().rstrip("*").strip())
            break

    paragraphs: list[str] = []
    fallback_paragraphs: list[str] = []
    cur: list[str] = []
    in_yaml = False
    in_comment = False

    def flush_para() -> None:
        if not cur:
            return
        raw_para = " ".join(cur).strip()
        cur.clear()
        if not raw_para:
            return
        is_non_avis = raw_para.startswith(">") and "Clause non-avis" in raw_para
        cleaned = _clean_prose_text(re.sub(r"^>\s*", "", raw_para))
        if len(cleaned) < 60:
            if len(cleaned) >= 24:
                fallback_paragraphs.append(cleaned)
            return
        if is_non_avis:
            fallback_paragraphs.append(cleaned)
        else:
            paragraphs.append(cleaned)

    for ln in range(lo + 1, hi + 1):
        if ln in code_lines:
            flush_para()
            continue
        raw_line = lines[ln - 1]
        st = raw_line.strip()
        if ln <= 10 and st == "---":
            in_yaml = not in_yaml
            flush_para()
            continue
        if in_yaml:
            continue
        if "<!--" in st:
            if "-->" not in st:
                in_comment = True
            flush_para()
            continue
        if in_comment:
            if "-->" in st:
                in_comment = False
            continue
        if not st or st == "---":
            flush_para()
            continue
        if st.startswith("#"):
            # Stopper dès le premier sous-titre si on a déjà un paragraphe substantiel
            flush_para()
            if paragraphs:
                break
            continue
        if st.startswith("![") or st.startswith("|") or _CAPTION_LINE_RE.match(st):
            flush_para()
            continue
        if _GUIDING_Q_RE.search(st):
            flush_para()
            continue
        if re.match(r"^[-*+]\s+\*\*\[", st):
            # Entrée de bibliographie
            flush_para()
            continue
        cur.append(re.sub(r"^[-*+]\s+", "", st))

    flush_para()
    chosen = paragraphs[0] if paragraphs else (fallback_paragraphs[0] if fallback_paragraphs else "")
    return guiding_question, _truncate_clean(chosen, max_chars=max_chars)


@dataclass
class _HeadingSpan:
    line_start: int
    line_end: int
    level: int
    pdf_start: int
    pdf_end: int


class CompendiumPdfIndex:
    """Index déterministe reliant lignes/titres/figures de ``Compendium.md`` à ``Compendium.pdf``."""

    def __init__(
        self,
        *,
        page_count: int,
        page_texts: dict[int, str],
        page_norm_texts: dict[int, str],
        heading_pages_by_line: dict[int, tuple[int, int]],
        heading_spans: list[_HeadingSpan],
        comp_lines: list[str],
    ) -> None:
        self.page_count = page_count
        self.page_texts = page_texts
        self.page_norm_texts = page_norm_texts
        self.heading_pages_by_line = heading_pages_by_line
        self.heading_spans = heading_spans
        self.comp_lines = comp_lines

    @classmethod
    def from_repo(cls, repo_root: Path) -> CompendiumPdfIndex:
        pdf_path = repo_root / "Compendium" / "Compendium.pdf"
        md_path = repo_root / "Compendium" / "Compendium.md"
        if not pdf_path.is_file():
            raise FileNotFoundError(f"Compendium PDF introuvable : {pdf_path}")
        if not md_path.is_file():
            raise FileNotFoundError(f"Compendium Markdown introuvable : {md_path}")

        comp_lines = md_path.read_text(encoding="utf-8").splitlines()
        raw_headings, _, _ = es.parse_markdown_lines(comp_lines)

        with pymupdf.open(pdf_path) as doc:
            page_count = int(doc.page_count)
            toc = doc.get_toc()
            page_texts: dict[int, str] = {}
            page_norm_texts: dict[int, str] = {}
            for pno in range(1, page_count + 1):
                txt = doc[pno - 1].get_text("text")
                page_texts[pno] = txt
                page_norm_texts[pno] = _norm_for_search(txt)

        # Calculer line_end par titre
        line_ends: list[int] = []
        for i, (_, lvl, _) in enumerate(raw_headings):
            end_ln = len(comp_lines)
            for j in range(i + 1, len(raw_headings)):
                if raw_headings[j][1] <= lvl:
                    end_ln = raw_headings[j][0] - 1
                    break
            line_ends.append(max(raw_headings[i][0], end_ln))

        toc_headings = [
            (idx, ln, lvl, ttl)
            for idx, (ln, lvl, ttl) in enumerate(raw_headings)
            if es.classify_heading("LIM", lvl, ttl) == "toc"
        ]
        non_toc_headings = [
            (idx, ln, lvl, ttl)
            for idx, (ln, lvl, ttl) in enumerate(raw_headings)
            if es.classify_heading("LIM", lvl, ttl) != "toc"
        ]

        if len(non_toc_headings) != len(toc):
            raise ValueError(
                f"Désalignement titres Compendium.md ({len(non_toc_headings)}) != TOC PDF ({len(toc)})"
            )

        heading_pages_by_line: dict[int, tuple[int, int]] = {}
        heading_spans: list[_HeadingSpan] = []

        first_toc_page = int(toc[0][2]) if toc else 7
        for idx, ln, lvl, _ in toc_headings:
            p_start = min(3, first_toc_page)
            p_end = max(p_start, first_toc_page - 1)
            heading_pages_by_line[ln] = (p_start, p_end)
            heading_spans.append(_HeadingSpan(ln, line_ends[idx], lvl, p_start, p_end))

        for pos, (idx, ln, lvl, ttl) in enumerate(non_toc_headings):
            toc_lvl, _, toc_page = toc[pos]
            if int(toc_lvl) != int(lvl):
                raise ValueError(
                    f"Désalignement de niveau à l'entrée {pos} ({ttl!r}) : MD H{lvl} != PDF H{toc_lvl}"
                )
            p_start = max(1, min(page_count, int(toc_page)))
            p_end = page_count
            for nxt_pos in range(pos + 1, len(non_toc_headings)):
                nxt_lvl = int(toc[nxt_pos][0])
                if nxt_lvl <= lvl:
                    nxt_page = max(1, min(page_count, int(toc[nxt_pos][2])))
                    if lvl <= 2 and nxt_page > p_start:
                        p_end = nxt_page - 1
                    else:
                        p_end = max(p_start, nxt_page)
                    break
            heading_pages_by_line[ln] = (p_start, p_end)
            heading_spans.append(_HeadingSpan(ln, line_ends[idx], lvl, p_start, p_end))

        heading_spans.sort(key=lambda s: (s.line_start, -s.level))
        return cls(
            page_count=page_count,
            page_texts=page_texts,
            page_norm_texts=page_norm_texts,
            heading_pages_by_line=heading_pages_by_line,
            heading_spans=heading_spans,
            comp_lines=comp_lines,
        )

    def resolve_figure_page(
        self,
        schema_id: str,
        unit_page_span: tuple[int, int] | None = None,
    ) -> int:
        """Localise la page PDF exacte d'un schéma ``SCH-XX-YY``."""
        pat = re.compile(rf"\b{re.escape(schema_id)}\b")

        def search_range(p_lo: int, p_hi: int, require_figure: bool) -> int | None:
            for pno in range(max(1, p_lo), min(self.page_count, p_hi) + 1):
                txt = self.page_texts[pno]
                for m in pat.finditer(txt):
                    if not require_figure:
                        return pno
                    ctx = txt[max(0, m.start() - 40) : min(len(txt), m.end() + 20)]
                    if "Figure" in ctx:
                        return pno
            return None

        if unit_page_span is not None:
            lo, hi = unit_page_span
            hit = search_range(lo, hi, True) or search_range(lo, hi, False)
            if hit is not None:
                return hit

        hit_global = search_range(1, self.page_count, True) or search_range(1, self.page_count, False)
        if hit_global is not None:
            return hit_global
        raise ValueError(f"Schéma {schema_id} introuvable dans Compendium/Compendium.pdf")

    def resolve_line_page(
        self,
        line_no: int,
        hints: list[str] | None = None,
    ) -> int:
        """Résout une ligne de ``Compendium.md`` vers sa page PDF dans ``Compendium.pdf``."""
        if line_no in self.heading_pages_by_line:
            return self.heading_pages_by_line[line_no][0]

        best_span: _HeadingSpan | None = None
        for sp in self.heading_spans:
            if sp.line_start <= line_no <= sp.line_end:
                if best_span is None or sp.level >= best_span.level:
                    best_span = sp

        if best_span is None:
            p_lo, p_hi = 1, self.page_count
            l_lo, l_hi = 1, len(self.comp_lines)
        else:
            p_lo, p_hi = best_span.pdf_start, best_span.pdf_end
            l_lo, l_hi = best_span.line_start, best_span.line_end

        if p_lo >= p_hi:
            return p_lo

        # Recherche par ancres textuelles dans la fenêtre PDF de la section
        probe_needles: list[str] = []
        for h in hints or []:
            nh = _norm_for_search(h)
            if len(nh) >= 3:
                probe_needles.append(nh)
        if 1 <= line_no <= len(self.comp_lines):
            raw_line = _clean_prose_text(self.comp_lines[line_no - 1])
            n_line = _norm_for_search(raw_line)
            if len(n_line) >= 18:
                probe_needles.append(n_line[:56])

        for needle in probe_needles:
            for pno in range(p_lo, p_hi + 1):
                if needle in self.page_norm_texts[pno]:
                    return pno

        # Repli déterministe par interpolation proportionnelle dans [p_lo, p_hi]
        ratio = (line_no - l_lo) / max(1, l_hi - l_lo)
        ratio = max(0.0, min(1.0, ratio))
        return min(p_hi, max(p_lo, p_lo + round(ratio * (p_hi - p_lo))))
