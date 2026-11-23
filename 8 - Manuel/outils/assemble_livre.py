#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Assembleur des editions integrales MD, HTML et PDF du Volume 8 (8 - Manuel)."""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
from collections.abc import Callable
from pathlib import Path

_TOOLS_DIR = Path(__file__).resolve().parent
if str(_TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(_TOOLS_DIR))

from _communs import format_french_date, get_freeze_date  # noqa: E402
from verifie_manuscrit import _FENCE_OPEN_RE, _strip_yaml_and_preserve_lines  # noqa: E402

# Largeur utile Typst : page 6.14in - marges (0.90in + 0.78in) = 4.46in * 72 pt/in = 321.12 pt
_USABLE_PAGE_WIDTH_PT = (6.14 - 0.90 - 0.78) * 72.0

_DEFAULT_PART_TITLES = {
    "I": "Partie I — Harnais déterministe et confiance cryptographique",
    "II": "Partie II — Politiques hors modèle, sémantique d'effet et homologation vérifiable",
}

_HTML_HEADER_CSS = """<style>
  :root { color-scheme: light; }
  body {
    font-family: "Libertinus Serif", Georgia, "Times New Roman", serif;
    max-width: 48rem;
    margin: 2.5rem auto;
    padding: 0 1.4rem;
    line-height: 1.65;
    color: #111827;
    background: #ffffff;
  }
  header#title-block-header {
    border-bottom: 2px solid #1B365D;
    padding-bottom: 1.4rem;
    margin-bottom: 2rem;
  }
  h1.title { color: #132238; font-size: 2.1rem; margin-bottom: 0.35rem; }
  p.subtitle { color: #334155; font-size: 1.15rem; font-style: italic; margin-top: 0; }
  h1, h2, h3, h4 {
    font-family: "Segoe UI", system-ui, -apple-system, sans-serif;
    color: #132238;
    margin-top: 2rem;
  }
  h1 { border-bottom: 1px solid #CBD5E1; padding-bottom: 0.3rem; }
  nav#TOC {
    background: #F8FAFC;
    border: 1px solid #CBD5E1;
    border-left: 4px solid #1B365D;
    padding: 1rem 1.25rem;
    margin-bottom: 2.5rem;
  }
  blockquote {
    background: #F1F5F9;
    border-left: 4px solid #1B365D;
    margin: 1.4rem 0;
    padding: 0.85rem 1.1rem;
    color: #1E293B;
  }
  table {
    width: 100%;
    border-collapse: collapse;
    margin: 1.5rem 0;
    font-size: 0.92rem;
  }
  th, td {
    border: 1px solid #CBD5E1;
    padding: 0.5rem 0.65rem;
    text-align: left;
    vertical-align: top;
  }
  thead th { background: #1B365D; color: #ffffff; }
  tbody tr:nth-child(even) { background: #F8FAFC; }
  figure {
    margin: 1.6rem auto;
    text-align: center;
  }
  figure img {
    max-width: 100%;
    height: auto;
  }
  img {
    display: block;
    margin: 1.6rem auto;
    max-width: 100%;
    height: auto;
  }
  figcaption {
    font-style: italic;
    color: #475569;
    font-size: 0.9rem;
    margin-top: 0.45rem;
  }
  code {
    background: #F1F5F9;
    padding: 0.1rem 0.3rem;
    border-radius: 3px;
    font-size: 0.9em;
  }
  pre code { display: block; padding: 0.85rem; overflow-x: auto; }
</style>
"""


def _shift_markdown_headings(text: str, delta: int) -> str:
    """Decale les niveaux de titres Markdown (#) hors blocs de code clotures."""
    if delta == 0:
        return text
    out: list[str] = []
    fence_char: str | None = None
    fence_len = 0
    for line in text.split("\n"):
        if fence_char is None:
            m_open = _FENCE_OPEN_RE.match(line)
            if m_open:
                fence_char = m_open.group(1)[0]
                fence_len = len(m_open.group(1))
                out.append(line)
                continue
            m_head = re.match(r"^(#{1,5})(\s+.*)$", line)
            if m_head:
                new_level = min(6, len(m_head.group(1)) + delta)
                out.append(("#" * new_level) + m_head.group(2))
            else:
                out.append(line)
        else:
            stripped = line.lstrip()
            if stripped.startswith(fence_char * fence_len) and stripped.strip() == fence_char * len(stripped.strip()):
                fence_char = None
                fence_len = 0
            out.append(line)
    return "\n".join(out)


def _normalize_image_paths(
    text: str,
    fig_ext_map: dict[str, str],
    prefix: str | None = None,
) -> str:
    """Normalise les liens images Fig-XX vers `<prefix>/Fig-XX.ext`."""
    clean_prefix = (prefix or "../8 - Manuel/diagrammes/rendus").rstrip("/")

    def _repl(match: re.Match[str]) -> str:
        alt = match.group(1)
        raw_path = match.group(2).strip()
        m_fig = re.search(r"(Fig-\d{2})", raw_path)
        if m_fig:
            fid = m_fig.group(1)
            ext = fig_ext_map.get(fid, "svg")
            return f"![{alt}]({clean_prefix}/{fid}.{ext})"
        return match.group(0)

    return re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", _repl, text)


def _resolve_book_root(root: Path) -> Path:
    """Retourne un chemin racine exploitable (resout les chemins relatifs ou '.')."""
    path = Path(root)
    return path if path.is_absolute() and path.name else path.resolve()


def _resolve_deliverable_paths(root: Path, manifest: dict) -> tuple[Path, Path, Path, str]:
    """Resout les chemins de livrables (md, pdf, html, image_prefix) depuis manifest.json."""
    root = _resolve_book_root(root)
    book_stem = root.name
    deliv = manifest.get("deliverables", {})
    if book_stem == "8 - Manuel" and isinstance(deliv, dict):
        md_rel = str(deliv.get("md") or deliv.get("markdown") or f"../0 - PDF-MD/{book_stem}.md")
        pdf_rel = str(deliv.get("pdf") or f"../0 - PDF-MD/{book_stem}.pdf")
        html_rel = str(deliv.get("html") or f"livrables/{book_stem}.html")
        img_pref = str(deliv.get("image_prefix") or f"../{book_stem}/diagrammes/rendus")
        return (
            (root / md_rel).resolve(),
            (root / pdf_rel).resolve(),
            (root / html_rel).resolve(),
            img_pref,
        )
    return (
        (root.parent / "0 - PDF-MD" / f"{book_stem}.md").resolve(),
        (root.parent / "0 - PDF-MD" / f"{book_stem}.pdf").resolve(),
        (root / "livrables" / f"{book_stem}.html").resolve(),
        f"../{book_stem}/diagrammes/rendus",
    )


def _clean_residual_livrables(root: Path, expected_html_name: str | None = None) -> None:
    """Supprime tout fichier .md, .pdf, .typ, .tmp ou .html parasite dans livrables/."""
    root = _resolve_book_root(root)
    livrables_dir = root / "livrables"
    if not livrables_dir.is_dir():
        return
    expected_html = expected_html_name or f"{root.name}.html"
    for item in livrables_dir.iterdir():
        if not item.is_file():
            continue
        suffix = item.suffix.lower()
        if suffix in {".md", ".pdf", ".typ", ".tmp"} or (suffix == ".html" and item.name != expected_html):
            item.unlink(missing_ok=True)


def _format_license_label(manifest: dict) -> str:
    lic = manifest.get("license_mode", {})
    if lic.get("commercial_override"):
        return "Tous droits réservés"
    text_lic = str(lic.get("text_and_figures", "CC-BY-4.0"))
    return "CC BY 4.0" if text_lic.upper() == "CC-BY-4.0" else text_lic


def build_consolidated_markdown(
    root: Path,
    image_prefix: str | None = None,
) -> tuple[str, str, dict]:
    """Construit en memoire le Markdown consolide et retourne (full_md, body_sans_yaml, meta)."""
    root = _resolve_book_root(root)
    manifest = json.loads((root / "specs" / "manifest.json").read_text(encoding="utf-8"))
    _, _, _, default_prefix = _resolve_deliverable_paths(root, manifest)
    effective_prefix = image_prefix if image_prefix is not None else default_prefix

    part_titles = manifest.get("part_titles", _DEFAULT_PART_TITLES)
    if not isinstance(part_titles, dict) or not part_titles:
        part_titles = _DEFAULT_PART_TITLES

    fig_ext_map = {
        f["id"]: ("svg" if f["engine"] == "puml" else "png")
        for f in manifest.get("figures", [])
    }

    freeze_label = format_french_date(get_freeze_date(root))
    pub_label = f"janvier {manifest.get('edition_year', 2027)}"
    license_label = _format_license_label(manifest)
    title = manifest["title"]
    subtitle = manifest["subtitle"]
    author = manifest["author_credit"]

    chunks: list[str] = []
    current_part: str | None = None
    annex_header_added = False

    for u in manifest["units"]:
        upath = root / u["file"]
        if not upath.is_file():
            raise FileNotFoundError(f"Unite manquante pour l'assemblage : {upath}")

        raw = upath.read_text(encoding="utf-8")
        body, _ = _strip_yaml_and_preserve_lines(raw)
        body = _normalize_image_paths(body.strip(), fig_ext_map, prefix=effective_prefix)

        kind = u["kind"]
        if kind == "frontmatter":
            chunks.append(body)
        elif kind == "chapter":
            part = u.get("part")
            if part and part != current_part:
                current_part = part
                part_title = part_titles.get(part, f"Partie {part}")
                chunks.append(f"# {part_title}")
            chunks.append(_shift_markdown_headings(body, delta=1))
        elif kind == "annex":
            if not annex_header_added:
                annex_header_added = True
                chunks.append("# Annexes — Instruments de référence")
            chunks.append(_shift_markdown_headings(body, delta=1))

    body_only = "\n\n".join(chunks).strip() + "\n"
    yaml_header = (
        "---\n"
        f'title: "{title}"\n'
        f'subtitle: "{subtitle}"\n'
        f'author: "{author}"\n'
        f'date: "Parution : {pub_label} (gel des faits : {freeze_label})"\n'
        f'lang: "{manifest.get("language", "fr-CA")}"\n'
        f'rights: "{license_label}"\n'
        "---\n\n"
    )
    meta = {
        "title": title,
        "subtitle": subtitle,
        "author": author,
        "freeze_date": freeze_label,
        "pub_date": pub_label,
        "license_text": license_label,
    }
    return yaml_header + body_only, body_only, meta


def assemble_markdown(root: Path) -> tuple[Path, str, dict]:
    """Assemble le fichier consolide (../0 - PDF-MD/8 - Manuel.md) et retourne (path, body_sans_yaml, meta)."""
    root = _resolve_book_root(root)
    manifest = json.loads((root / "specs" / "manifest.json").read_text(encoding="utf-8"))
    md_out, _, html_out, img_prefix = _resolve_deliverable_paths(root, manifest)
    full_md, body_only, meta = build_consolidated_markdown(root, image_prefix=img_prefix)
    md_out.parent.mkdir(parents=True, exist_ok=True)
    md_out.write_text(full_md, encoding="utf-8", newline="\n")
    _clean_residual_livrables(root, expected_html_name=html_out.name)
    return md_out, body_only, meta


def _transform_inline_backticks(
    text: str,
    transform: Callable[[str], str],
    *,
    respect_escapes: bool = False,
) -> str:
    """Applique `transform` aux spans de code inline hors blocs de code clotures."""
    out_lines: list[str] = []
    fence_char: str | None = None
    fence_len = 0

    for ln in text.splitlines(keepends=True):
        raw_ln = ln.rstrip("\r\n")
        if fence_char is None:
            m_fence = _FENCE_OPEN_RE.match(raw_ln)
            if m_fence:
                fence_char = m_fence.group(1)[0]
                fence_len = len(m_fence.group(1))
                out_lines.append(ln)
                continue
            res: list[str] = []
            i = 0
            n = len(ln)
            while i < n:
                if respect_escapes and ln[i] == "\\":
                    res.append(ln[i : i + 2])
                    i += 2
                    continue
                if ln[i] == "`":
                    run = _count_backtick_run(ln, i)
                    delim = "`" * run
                    end = ln.find(delim, i + run)
                    while end != -1 and _count_backtick_run(ln, end) != run:
                        end = ln.find(delim, end + 1)
                    if end != -1:
                        res.append(delim + transform(ln[i + run : end]) + delim)
                        i = end + run
                        continue
                res.append(ln[i])
                i += 1
            out_lines.append("".join(res))
        else:
            out_lines.append(ln)
            stripped = raw_ln.strip()
            if stripped.startswith(fence_char * fence_len) and stripped == fence_char * len(stripped):
                fence_char = None
                fence_len = 0
    return "".join(out_lines)


def _unescape_dollars_in_inline_code_md(md_text: str) -> str:
    """Remplace \\$ par $ uniquement dans les spans de code inline Markdown (hors blocs clotures)."""
    return _transform_inline_backticks(md_text, lambda s: s.replace(r"\$", "$"), respect_escapes=False)


def compile_html(root: Path, md_path: Path) -> Path:
    """Compile l'edition HTML autonome via Pandoc dans livrables/8 - Manuel.html."""
    root = _resolve_book_root(root)
    manifest = json.loads((root / "specs" / "manifest.json").read_text(encoding="utf-8"))
    _, _, html_out, _ = _resolve_deliverable_paths(root, manifest)
    livrables_dir = html_out.parent
    livrables_dir.mkdir(parents=True, exist_ok=True)
    resource_path = os.pathsep.join(
        str(p) for p in (md_path.parent, livrables_dir, root.parent, root)
    )

    sanitized_md = _unescape_dollars_in_inline_code_md(md_path.read_text(encoding="utf-8"))
    with tempfile.NamedTemporaryFile("w", suffix=".md", encoding="utf-8", delete=False) as mf:
        mf.write(sanitized_md)
        temp_md_path = Path(mf.name)

    with tempfile.NamedTemporaryFile("w", suffix=".html", encoding="utf-8", delete=False) as tf:
        tf.write(_HTML_HEADER_CSS)
        css_header_path = Path(tf.name)

    try:
        cmd = [
            "pandoc",
            str(temp_md_path),
            "-f",
            "markdown-tex_math_dollars+tex_math_single_backslash-implicit_figures-citations",
            "--standalone",
            "--embed-resources",
            "--toc",
            "--toc-depth=2",
            "--mathml",
            "--include-in-header",
            str(css_header_path),
            "--resource-path",
            resource_path,
            "-o",
            str(html_out),
        ]
        res = subprocess.run(cmd, shell=False, capture_output=True, text=True, encoding="utf-8")
        if res.returncode != 0:
            raise RuntimeError(f"Echec pandoc HTML (code {res.returncode}) :\n{res.stderr}")
    finally:
        css_header_path.unlink(missing_ok=True)
        temp_md_path.unlink(missing_ok=True)
    return html_out


def _escape_typst_content(text: str) -> str:
    return text.replace("\\", "\\\\").replace("#", "\\#").replace("$", "\\$").replace("[", "\\[").replace("]", "\\]")


def _strip_typst_markup(cell: str) -> str:
    s = re.sub(r"#(?:strong|emph|link\([^)]*\)|text\([^)]*\))\[", "", cell)
    s = s.replace("[", "").replace("]", "").replace("`", "")
    s = re.sub(r"\\([\[\]$#_])", r"\1", s)
    return " ".join(s.split())


def _apply_cell_prose_nbsp(text: str) -> str:
    text = re.sub(r"(?i)\b([cdjlmnst]['’])(?=[A-Za-zÀ-ÖØ-öø-ÿ]{9,})", lambda m: m.group(1) + "\u200b", text)
    text = re.sub(r"(\d)\s+%", lambda m: m.group(1) + "\u00a0%", text)
    text = re.sub(r"(\d)\s+\\\$", lambda m: m.group(1) + "\u00a0\\$", text)
    text = re.sub(r"(\\\$)\s+(CA|US)\b", lambda m: m.group(1) + "\u00a0" + m.group(2), text)
    text = re.sub(r"(?<=\d) (?=\d{3}\b)", "\u00a0", text)
    text = re.sub(r"(\d)\s+(s|ms|min|h|o|Kio|Mio|po|pt)\b", lambda m: m.group(1) + "\u00a0" + m.group(2), text)
    text = re.sub(r"(?<!-) -> (?!-)", " → ", text)
    return text


def _break_long_tokens_in_cell(cell: str) -> str:
    def _wrap_raw_inner(inner: str) -> str:
        inner = inner.replace(r"\$", "$")
        inner = re.sub(r"(\d)\s+%", lambda x: x.group(1) + "\u00a0%", inner)
        inner = inner.replace("->", "-\u2060>")
        inner = inner.replace("-*", "-\u2060*")
        inner = re.sub(r"(?<![A-Za-z0-9])(--?)(?=[A-Za-z0-9*])", lambda x: "".join(c + "\u2060" for c in x.group(1)), inner)
        if "://" in inner:
            return f"`{_wrap_url_display(inner)}`"

        def _chunk_cell(m2: re.Match[str]) -> str:
            tok = m2.group(0)
            return "\u200b".join(tok[k : k + 12] for k in range(0, len(tok), 12))

        def _wrap_part(part: str) -> str:
            if "\u200b" in part:
                return part
            part = re.sub(
                r"(::|[_/:,=(]|(?<!\d)\.|(?<=\d)\.(?=[A-Za-z_]))(?=[A-Za-z0-9_{\"'])",
                lambda x: x.group(1) + "\u200b",
                part,
            )
            if len(part) >= 12:
                part = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", "\u200b", part)
            return re.sub(r"[A-Za-zÀ-ÖØ-öø-ÿ0-9]{16,}", _chunk_cell, part)

        wrapped = re.sub(r"\S+", lambda mm: _wrap_part(mm.group(0)), inner)
        return f"`{wrapped}`"

    protected_re = re.compile(r'((?<!`)`[^`\n]+`(?!`)|#link\("[^"]+"\)(?:\[[^\]]*\])?)')
    parts: list[str] = []
    pos = 0
    for m in protected_re.finditer(cell):
        if m.start() > pos:
            parts.append(_apply_cell_prose_nbsp(cell[pos : m.start()]))
        tok = m.group(0)
        if tok.startswith("`"):
            parts.append(_wrap_raw_inner(tok[1:-1]))
        else:
            parts.append(tok)
        pos = m.end()
    if pos < len(cell):
        parts.append(_apply_cell_prose_nbsp(cell[pos:]))
    return "".join(parts)


def _count_backtick_run(text: str, idx: int) -> int:
    n = len(text)
    end = idx
    while end < n and text[end] == "`":
        end += 1
    return end - idx


def _normalize_typst_math_commas(typst_src: str) -> str:
    """Convertit les virgules decimales (, ou \\,) en ',' typographique dans les blocs $...$."""
    out: list[str] = []
    pos = 0
    n = len(typst_src)
    raw_ticks = 0
    in_math = False
    in_math_str = False
    math_start = 0

    def _fix_math_inner(inner: str) -> str:
        parts: list[str] = []
        p = 0
        for sm in re.finditer(r'"(?:[^"\\]|\\.)*"', inner):
            parts.append(re.sub(r"(\d)(?:\\,|,)(?=\d)", r'\1","', inner[p : sm.start()]))
            parts.append(sm.group(0))
            p = sm.end()
        parts.append(re.sub(r"(\d)(?:\\,|,)(?=\d)", r'\1","', inner[p:]))
        return "".join(parts)

    while pos < n:
        ch = typst_src[pos]
        if raw_ticks > 0:
            if ch == "`":
                run = _count_backtick_run(typst_src, pos)
                out.append("`" * run)
                if run == raw_ticks:
                    raw_ticks = 0
                pos += run
            else:
                out.append(ch)
                pos += 1
            continue

        if in_math:
            if in_math_str:
                if ch == "\\" and pos + 1 < n:
                    pos += 2
                    continue
                if ch == '"':
                    in_math_str = False
                pos += 1
                continue
            if ch == "\\" and pos + 1 < n:
                pos += 2
                continue
            if ch == '"':
                in_math_str = True
                pos += 1
                continue
            if ch == "$":
                inner = typst_src[math_start:pos]
                out.append("$" + _fix_math_inner(inner) + "$")
                in_math = False
                pos += 1
                continue
            pos += 1
            continue

        if ch == "\\" and pos + 1 < n:
            out.append(typst_src[pos : pos + 2])
            pos += 2
            continue
        if ch == "`":
            run = _count_backtick_run(typst_src, pos)
            out.append("`" * run)
            raw_ticks = run
            pos += run
            continue
        if ch == "$":
            in_math = True
            in_math_str = False
            math_start = pos + 1
            pos += 1
            continue
        out.append(ch)
        pos += 1

    if in_math:
        out.append("$" + typst_src[math_start:])
    return "".join(out)


def _split_top_level_args(body: str) -> list[str]:
    args: list[str] = []
    cur: list[str] = []
    paren_stack = [0]
    in_str = False
    raw_ticks = 0
    i = 0
    n = len(body)
    while i < n:
        ch = body[i]
        if in_str:
            cur.append(ch)
            if ch == "\\" and i + 1 < n:
                cur.append(body[i + 1])
                i += 2
                continue
            if ch == '"':
                in_str = False
            i += 1
            continue
        if raw_ticks > 0:
            if ch == "`":
                run = _count_backtick_run(body, i)
                cur.append("`" * run)
                if run == raw_ticks:
                    raw_ticks = 0
                i += run
            else:
                cur.append(ch)
                i += 1
            continue
        if ch == "\\":
            cur.append(ch)
            if i + 1 < n:
                cur.append(body[i + 1])
                i += 2
                continue
        elif ch == '"':
            in_str = True
        elif ch == "`":
            run = _count_backtick_run(body, i)
            cur.append("`" * run)
            raw_ticks = run
            i += run
            continue
        elif ch == "[":
            paren_stack.append(0)
        elif ch == "]":
            if len(paren_stack) > 1:
                paren_stack.pop()
        elif ch == "(":
            paren_stack[-1] += 1
        elif ch == ")":
            paren_stack[-1] = max(0, paren_stack[-1] - 1)
        elif ch == "," and len(paren_stack) == 1 and paren_stack[0] == 0:
            args.append("".join(cur))
            cur = []
            i += 1
            continue
        cur.append(ch)
        i += 1
    if "".join(cur).strip():
        args.append("".join(cur))
    return args


def _rebalance_single_table(table_inner: str) -> str:
    args = _split_top_level_args(table_inner)
    col_idx = -1
    ncols = 0
    for idx, arg in enumerate(args):
        m = re.match(r"^\s*columns:\s*(?:\(([^)]+)\)|(\d+))\s*$", arg, re.DOTALL)
        if m:
            col_idx = idx
            if m.group(1) is not None:
                ncols = len([x for x in m.group(1).split(",") if x.strip()])
            else:
                ncols = int(m.group(2))
            break
    if col_idx < 0 or ncols <= 1:
        return table_inner

    cell_texts: list[str] = []
    new_args: list[str] = []
    for arg in args:
        st = arg.strip()
        if st.startswith("table.header(") and st.endswith(")"):
            h_inner = st[len("table.header(") : -1]
            h_args = _split_top_level_args(h_inner)
            fixed_h = []
            for h in h_args:
                hs = h.strip()
                if hs.startswith("[") and hs.endswith("]"):
                    hs = _break_long_tokens_in_cell(hs)
                    cell_texts.append(_strip_typst_markup(hs).replace("\u200b", " ").replace("\u2060", ""))
                fixed_h.append(hs)
            new_args.append("\n    table.header(" + ", ".join(fixed_h) + ",)")
        elif re.match(r"^align:\s*\(", st):
            new_args.append(re.sub(r"\bauto\b", "left", arg))
        elif st.startswith("[") and st.endswith("]"):
            broken = _break_long_tokens_in_cell(st)
            cell_texts.append(_strip_typst_markup(broken).replace("\u200b", " ").replace("\u2060", ""))
            new_args.append(arg.replace(st, broken, 1))
        else:
            new_args.append(arg)

    if len(cell_texts) < ncols:
        return table_inner

    col_scores: list[float] = []
    min_shares: list[float] = []
    for c in range(ncols):
        vals = [cell_texts[i] for i in range(c, len(cell_texts), ncols)]
        lens = sorted(len(v) for v in vals)
        med = lens[len(lens) // 2]
        p90 = lens[min(len(lens) - 1, int(0.9 * len(lens)))]
        hdr_len = len(vals[0]) if vals else 4
        max_word = max((max((len(w) for w in v.split()), default=0) for v in vals), default=0)
        hdr_max_word = max((len(w) for w in vals[0].split()), default=0) if vals else 0
        if med < 15:
            eff_word = min(max(max_word, hdr_max_word), 12)
            req_floor = max(0.085, (eff_word * 3.8 + 8.0) / _USABLE_PAGE_WIDTH_PT)
        else:
            eff_word = min(max(max_word, hdr_max_word), 16)
            cap = 47.0 if ncols >= 6 else 72.0
            req_floor = max(0.085, min(cap / _USABLE_PAGE_WIDTH_PT, (eff_word * 3.7 + 7.5) / _USABLE_PAGE_WIDTH_PT))
        min_shares.append(req_floor)
        score = max(float(hdr_len) * 1.15, 0.55 * max(med, 5) + 0.45 * min(p90, 95), min(eff_word, 16) * 1.4)
        col_scores.append(max(score, 8.0))

    floor_sum = sum(min_shares)
    max_floor_sum = 0.94 if ncols >= 6 else 0.88
    if floor_sum > max_floor_sum:
        scale_f = max_floor_sum / floor_sum
        min_shares = [s * scale_f for s in min_shares]
        floor_sum = sum(min_shares)

    remaining = max(0.0, 1.0 - floor_sum)
    total_score = sum(col_scores) or 1.0
    shares = [min_shares[c] + remaining * (col_scores[c] / total_score) for c in range(ncols)]
    sh_sum = sum(shares)
    pcts = [round(100.0 * s / sh_sum, 2) for s in shares]
    pcts[-1] = round(100.0 - sum(pcts[:-1]), 2)
    col_spec = ", ".join(f"{p:.2f}%" for p in pcts)

    new_args[col_idx] = f"\n    columns: ({col_spec})"
    return ",".join(new_args) + ("," if not table_inner.rstrip().endswith(",") else "")


def _wrap_url_display(url: str) -> str:
    if "://" in url:
        scheme, rest = url.split("://", 1)
        rest = rest.replace("/", "/\u200b").replace("-", "-\u200b")
        rest = re.sub(r"(?<!\.)\.(?=[A-Za-z0-9])", ".\u200b", rest)
        return scheme + "://" + rest
    res = url.replace("/", "/\u200b").replace("-", "-\u200b")
    return re.sub(r"(?<!\.)\.(?=[A-Za-z0-9])", ".\u200b", res)


def _format_typst_link_safe(m: re.Match[str]) -> str:
    url = m.group(1)
    label = m.group(2)
    if label is None:
        disp = _wrap_url_display(url)
    elif label.startswith(("http://", "https://")):
        disp = _wrap_url_display(label.replace("\u200b", ""))
    else:
        return f'#link("{url}")[{label}]'
    escaped = disp.replace("\\", "\\\\").replace('"', '\\"')
    return f'#link("{url}")[#text(hyphenate: false)[#("{escaped}")]]'


def _wrap_inline_raw_tokens_typst(inner: str) -> str:
    """Deseschappe \\$ et ajoute des points de cesure discrets (\\u200b) dans le code inline hors tableaux."""
    fixed = inner.replace(r"\$", "$")
    fixed = re.sub(r"(\d)\s+%", lambda x: x.group(1) + "\u00a0%", fixed)
    fixed = re.sub(r"\b8\s+-\s+Manuel", "8\u00a0-\u00a0Manuel", fixed)
    fixed = fixed.replace("->", "-\u2060>")
    fixed = fixed.replace("-*", "-\u2060*")
    fixed = re.sub(r"(?<![A-Za-z0-9])(--?)(?=[A-Za-z0-9*])", lambda x: "".join(c + "\u2060" for c in x.group(1)), fixed)
    if "://" in fixed or "\u200b" in fixed:
        return fixed

    def _chunk_long_run(m: re.Match[str]) -> str:
        tok = m.group(0)
        if len(tok) < 32:
            return tok
        return "\u200b".join(tok[k : k + 16] for k in range(0, len(tok), 16))

    def _wrap_part(part: str) -> str:
        if len(part) < 16:
            return part
        part = re.sub(
            r"(::|[_/,=]|(?<!\d)\.|(?<=\d)\.(?=[A-Za-z_]))(?=[A-Za-z0-9_{\"'])",
            lambda x: x.group(1) + "\u200b",
            part,
        )
        if len(part) >= 26:
            part = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", "\u200b", part)
        return re.sub(r"[A-Za-zÀ-ÖØ-öø-ÿ0-9]{32,}", _chunk_long_run, part)

    return re.sub(r"\S+", lambda m: _wrap_part(m.group(0)), fixed)


def _postprocess_inline_raw_typst(typst_src: str) -> str:
    """Traite le code inline hors blocs clotures sans alterer les blocs ``` ni la prose."""
    return _transform_inline_backticks(typst_src, _wrap_inline_raw_tokens_typst, respect_escapes=True)


def _protect_typst_prose_line(line: str) -> str:
    """Applique les espaces insecables et -> en prose hors spans `...`, math $...$ et appels #link/#(...)."""
    if line.lstrip().startswith(("#set ", "#show ", "#page", "#let ", "#import ", "#figure(", "#block(", "#align(")):
        return line
    protected_re = re.compile(r'(`[^`\n]+`|(?<!\\)\$(?:\\.|[^$\n\\])+\$|#link\("[^"]+"\)|#\("(?:[^"\\]|\\.)*"\))')
    parts: list[str] = []
    pos = 0
    for m in protected_re.finditer(line):
        if m.start() > pos:
            parts.append(_apply_prose_nbsp_segment(line[pos : m.start()]))
        parts.append(m.group(0))
        pos = m.end()
    if pos < len(line):
        parts.append(_apply_prose_nbsp_segment(line[pos:]))
    return "".join(parts)


def _apply_prose_nbsp_segment(seg: str) -> str:
    seg = re.sub(r"(\d)\s+%", lambda m: m.group(1) + "\u00a0%", seg)
    seg = re.sub(r"(\d)\s+\\\$", lambda m: m.group(1) + "\u00a0\\$", seg)
    seg = re.sub(r"(\\\$)\s+(CA|US)\b", lambda m: m.group(1) + "\u00a0" + m.group(2), seg)
    seg = re.sub(r"(?<=\d) (?=\d{3}\b)", "\u00a0", seg)
    seg = re.sub(r"(\d)\s+(s|ms|min|h|o|Kio|Mio|po|pt)\b", lambda m: m.group(1) + "\u00a0" + m.group(2), seg)
    seg = re.sub(r"(§{1,2})\s+(?=\d)", lambda m: m.group(1) + "\u00a0", seg)
    seg = re.sub(r"([−–])\s+(?=\d)", lambda m: m.group(1) + "\u00a0", seg)
    seg = re.sub(r"\b8\s+-\s+Manuel", "8\u00a0-\u00a0Manuel", seg)
    seg = re.sub(r"(?<!-) -> (?!-)", " → ", seg)
    return seg


def _bind_small_tables_to_captions(typst_src: str) -> str:
    """Enveloppe chaque petit tableau (<= 12 lignes) avec sa legende Tableau X.Y dans un bloc indivisible."""
    out: list[str] = []
    pos = 0
    n = len(typst_src)
    marker = "#figure("
    cap_re = re.compile(
        r"^\s*\n\s*\n(#align\(center\)\[#set par\(justify: false\); #set text\(size: 8\.6pt, fill: rgb\(\"#475569\"\)\); #emph\[Tableau\s+\d+\.\d+\b[^\n]*\]\])"
    )
    while pos < n:
        hit = typst_src.find(marker, pos)
        if hit == -1:
            out.append(typst_src[pos:])
            break
        out.append(typst_src[pos:hit])
        i = hit + len(marker)
        paren_depth = 1
        in_str = False
        raw_ticks = 0
        while i < n and paren_depth > 0:
            ch = typst_src[i]
            if in_str:
                if ch == "\\" and i + 1 < n:
                    i += 2
                    continue
                if ch == '"':
                    in_str = False
            elif raw_ticks > 0:
                if ch == "`":
                    run = _count_backtick_run(typst_src, i)
                    if run == raw_ticks:
                        raw_ticks = 0
                    i += run
                    continue
            else:
                if ch == "\\":
                    i += 2
                    continue
                elif ch == '"':
                    in_str = True
                elif ch == "`":
                    run = _count_backtick_run(typst_src, i)
                    raw_ticks = run
                    i += run
                    continue
                elif ch == "(":
                    paren_depth += 1
                elif ch == ")":
                    paren_depth -= 1
            i += 1
        fig_block = typst_src[hit:i]
        is_small_table = ", kind: table" in fig_block and fig_block.count("\n    [") <= 16
        m_cap = cap_re.match(typst_src[i:]) if is_small_table else None
        if m_cap and (typst_src[hit:hit + 6] == "#figur"):
            end_cap = i + m_cap.end()
            out.append(
                "\n#block(width: 100%, breakable: false)[\n"
                + fig_block
                + "\n\n"
                + m_cap.group(1)
                + "\n]\n"
            )
            pos = end_cap
        else:
            out.append(fig_block)
            pos = i
    return "".join(out)


def _apply_outside_fences(typst_src: str, line_fn: Callable[[str], str]) -> str:
    out_lines: list[str] = []
    fence_char: str | None = None
    fence_len = 0
    for ln in typst_src.splitlines(keepends=True):
        raw_ln = ln.rstrip("\r\n")
        if fence_char is None:
            m_fence = _FENCE_OPEN_RE.match(raw_ln)
            if m_fence:
                fence_char = m_fence.group(1)[0]
                fence_len = len(m_fence.group(1))
                out_lines.append(ln)
            else:
                ending = ln[len(raw_ln) :]
                out_lines.append(line_fn(raw_ln) + ending)
        else:
            out_lines.append(ln)
            stripped = raw_ln.strip()
            if stripped.startswith(fence_char * fence_len) and stripped == fence_char * len(stripped):
                fence_char = None
                fence_len = 0
    return "".join(out_lines)


def _wrap_unjustified_section(typst_src: str, start_pattern: str, stop_pattern: str) -> str:
    m_start = re.search(start_pattern, typst_src, re.MULTILINE)
    if not m_start:
        return typst_src
    s_idx = m_start.end()
    after = typst_src[s_idx:]
    m_stop = re.search(stop_pattern, after, re.MULTILINE)
    if m_stop:
        body = after[: m_stop.start()]
        rest = "\n" + after[m_stop.start() :].lstrip("\n")
    else:
        body = after
        rest = ""
    return (
        typst_src[:s_idx]
        + "\n\n#block(width: 100%, breakable: true)[\n#set par(justify: false, leading: 0.56em, spacing: 0.45em)\n"
        + body.strip()
        + "\n]\n"
        + rest
    )


def _postprocess_typst_body(typst_src: str) -> str:
    normalized = _normalize_typst_math_commas(typst_src)
    out: list[str] = []
    pos = 0
    marker = "#table("
    n = len(normalized)
    while pos < n:
        hit = normalized.find(marker, pos)
        if hit == -1:
            out.append(normalized[pos:])
            break
        out.append(normalized[pos:hit])
        i = hit + len(marker)
        paren_stack = [1]
        in_str = False
        raw_ticks = 0
        while i < n and paren_stack[0] > 0:
            ch = normalized[i]
            if in_str:
                if ch == "\\":
                    i += 2
                    continue
                if ch == '"':
                    in_str = False
            elif raw_ticks > 0:
                if ch == "`":
                    run = _count_backtick_run(normalized, i)
                    if run == raw_ticks:
                        raw_ticks = 0
                    i += run
                    continue
            else:
                if ch == "\\":
                    i += 2
                    continue
                elif ch == '"':
                    in_str = True
                elif ch == "`":
                    run = _count_backtick_run(normalized, i)
                    raw_ticks = run
                    i += run
                    continue
                elif ch == "[":
                    paren_stack.append(0)
                elif ch == "]":
                    if len(paren_stack) > 1:
                        paren_stack.pop()
                elif ch == "(":
                    paren_stack[-1] += 1
                elif ch == ")":
                    if len(paren_stack) > 1:
                        paren_stack[-1] = max(0, paren_stack[-1] - 1)
                    else:
                        paren_stack[0] -= 1
            i += 1
        if paren_stack[0] == 0:
            inner = normalized[hit + len(marker) : i - 1]
            out.append("#table(" + _rebalance_single_table(inner) + ")")
            pos = i
        else:
            out.append(marker)
            pos = hit + len(marker)

    res = "".join(out)

    # Retirer un separateur horizontal immédiatement avant un titre
    res = re.sub(r"(?m)^#divider\(\)\s*\n+(?=={1,6}\s+)", "", res)

    # Centrer strictement les legendes numerotees *Figure N — ...* et *Tableau X.Y — ...*
    res = re.sub(
        r"(?ms)^(#emph\[(?:Figure\s+\d+\s*[—–-]|Tableau\s+\d+\.\d+\s*[—–-])[^\n]+(?:\n(?!\s*\n)[^\n]+)*\])(?=\s*(?:\n\s*\n|\Z))",
        r'#align(center)[#set par(justify: false); #set text(size: 8.6pt, fill: rgb("#475569")); \1]',
        res,
    )

    # Lier chaque petit tableau (<= 16 lignes) a sa legende *Tableau X.Y*
    res = _bind_small_tables_to_captions(res)

    # Securiser tous les #link HTTP/HTTPS contre l'autolinker Typst et autoriser la cesure des URLs
    def _fix_line_urls(line: str) -> str:
        line = re.sub(r'#link\("(https?://[^"]+)"\)(?:\[([^\]]+)\])?', _format_typst_link_safe, line)
        return re.sub(r"`(https?://[^`\n]+)`", lambda m: "`" + _wrap_url_display(m.group(1)) + "`", line)

    res = _apply_outside_fences(res, _fix_line_urls)

    # Desactiver la justification excessive dans la bibliographie/journaux d'Annexe A et les listes d'Annexe B
    res = _wrap_unjustified_section(
        res,
        r"^=+\s+Bibliographie classée des sources intégrales vérifiées\b[^\n]*(?:\n<[^>\n]+>)?",
        r"^={1,2}\s+(?:Annexe\s+|Chapitre\s+|Partie\s+)",
    )
    res = _wrap_unjustified_section(
        res,
        r"^=+\s+Matrice détaillée\b[^\n]*(?:\n<[^>\n]+>)?",
        r"^={1,2}\s+(?:Annexe\s+|Chapitre\s+|Partie\s+)",
    )

    res = _apply_outside_fences(res, _protect_typst_prose_line)
    return _postprocess_inline_raw_typst(res)


def compile_pdf(root: Path, body_md: str, meta: dict) -> Path:
    """Convertit en Typst via Pandoc, injecte dans gabarit-livre.typ et compile en ../0 - PDF-MD/8 - Manuel.pdf."""
    root = _resolve_book_root(root)
    template_path = Path(__file__).resolve().parent / "gabarit-livre.typ"
    template_src = template_path.read_text(encoding="utf-8")

    manifest = json.loads((root / "specs" / "manifest.json").read_text(encoding="utf-8"))
    _, pdf_out, html_out, _ = _resolve_deliverable_paths(root, manifest)
    fig_ext_map = {
        f["id"]: ("svg" if f["engine"] == "puml" else "png")
        for f in manifest.get("figures", [])
    }
    body_for_pdf = _normalize_image_paths(body_md, fig_ext_map, prefix="/diagrammes/rendus")

    p = subprocess.run(
        ["pandoc", "-f", "markdown-tex_math_dollars+tex_math_single_backslash-citations", "-t", "typst"],
        input=body_for_pdf,
        shell=False,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    if p.returncode != 0:
        raise RuntimeError(f"Echec pandoc -> typst (code {p.returncode}) :\n{p.stderr}")

    body_typst = _postprocess_typst_body(p.stdout)

    typst_source = template_src
    replacements = {
        "/* {{TITLE}} */": _escape_typst_content(meta["title"]),
        "/* {{SUBTITLE}} */": _escape_typst_content(meta["subtitle"]),
        "/* {{AUTHOR}} */": _escape_typst_content(meta["author"]),
        "/* {{FREEZE_DATE}} */": _escape_typst_content(meta["freeze_date"]),
        "/* {{PUB_DATE}} */": _escape_typst_content(meta["pub_date"]),
        "/* {{LICENSE_TEXT}} */": _escape_typst_content(meta["license_text"]),
        "/* {{BODY_TYPST}} */": body_typst,
    }
    for marker, val in replacements.items():
        typst_source = typst_source.replace(marker, val)

    pdf_out.parent.mkdir(parents=True, exist_ok=True)
    _clean_residual_livrables(root, expected_html_name=html_out.name)

    res = subprocess.run(
        ["typst", "compile", "--root", str(root), "-", str(pdf_out)],
        input=typst_source,
        shell=False,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    if res.returncode != 0:
        raise RuntimeError(f"Echec typst compile (code {res.returncode}) :\n{res.stderr}")
    return pdf_out


def build_deliverables(root: Path, make_md: bool = True, make_html: bool = True, make_pdf: bool = True) -> dict[str, Path]:
    """Construit les livrables demandes et nettoie tout residu dans livrables/."""
    root = _resolve_book_root(root)
    manifest = json.loads((root / "specs" / "manifest.json").read_text(encoding="utf-8"))
    _, _, html_out, _ = _resolve_deliverable_paths(root, manifest)
    _clean_residual_livrables(root, expected_html_name=html_out.name)
    md_path, body_only, meta = assemble_markdown(root)
    results: dict[str, Path] = {}
    if make_md:
        results["md"] = md_path
    if make_html:
        results["html"] = compile_html(root, md_path)
    if make_pdf:
        results["pdf"] = compile_pdf(root, body_only, meta)
    _clean_residual_livrables(root, expected_html_name=html_out.name)
    return results


def main() -> int:
    parser = argparse.ArgumentParser(description="Assembleur MD / HTML / PDF du Volume 8 (8 - Manuel).")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent, help="Racine du livre (`8 - Manuel`)")
    parser.add_argument("--all", action="store_true", help="Produire MD, HTML et PDF")
    parser.add_argument("--md", action="store_true", help="Produire le Markdown assemble")
    parser.add_argument("--html", action="store_true", help="Produire le HTML autonome")
    parser.add_argument("--pdf", action="store_true", help="Produire le PDF via Typst")
    args = parser.parse_args()

    make_all = args.all or not (args.md or args.html or args.pdf)
    outputs = build_deliverables(
        args.root,
        make_md=make_all or args.md,
        make_html=make_all or args.html,
        make_pdf=make_all or args.pdf,
    )
    for fmt, path in outputs.items():
        print(f"OK ({fmt.upper()}) : {path} ({path.stat().st_size} octets)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
