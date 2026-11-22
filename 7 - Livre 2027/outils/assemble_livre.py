#!/usr/bin/env python3
"""Assembleur des editions integrales MD, HTML et PDF du Livre 2027 (Tache 6)."""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

_TOOLS_DIR = Path(__file__).resolve().parent
if str(_TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(_TOOLS_DIR))

from verifie_manuscrit import _FENCE_OPEN_RE, _strip_yaml_and_preserve_lines  # noqa: E402

_PART_TITLES = {
    "I": "Partie I — L'industrialisation cognitive face au réel",
    "II": "Partie II — L'exosquelette déterministe : concevoir en 80/20",
    "III": "Partie III — La fabrique de confiance et l'économie de la preuve",
    "IV": "Partie IV — Gouverner jusqu'en 2035 sans atrophier l'humain",
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


def _normalize_image_paths(text: str, fig_ext_map: dict[str, str]) -> str:
    """Normalise les liens images Fig-XX vers ../diagrammes/rendus/Fig-XX.ext depuis livrables/."""

    def _repl(match: re.Match[str]) -> str:
        alt = match.group(1)
        raw_path = match.group(2).strip()
        m_fig = re.search(r"(Fig-\d{2})", raw_path)
        if m_fig:
            fid = m_fig.group(1)
            ext = fig_ext_map.get(fid, "svg")
            return f"![{alt}](../diagrammes/rendus/{fid}.{ext})"
        return match.group(0)

    return re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", _repl, text)


def _format_license_label(manifest: dict) -> str:
    lic = manifest.get("license_mode", {})
    if lic.get("commercial_override"):
        return "Tous droits réservés"
    text_lic = str(lic.get("text_and_figures", "CC-BY-4.0"))
    return "CC BY 4.0" if text_lic.upper() == "CC-BY-4.0" else text_lic


def assemble_markdown(root: Path) -> tuple[Path, str, dict]:
    """Assemble le fichier consolide livrables/7 - Livre 2027.md et retourne (path, body_sans_yaml, meta)."""
    root = Path(root)
    manifest = json.loads((root / "specs" / "manifest.json").read_text(encoding="utf-8"))
    fig_ext_map = {
        f["id"]: ("svg" if f["engine"] == "puml" else "png")
        for f in manifest.get("figures", [])
    }

    freeze_label = "31 décembre 2026"
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
        body = _normalize_image_paths(body.strip(), fig_ext_map)

        kind = u["kind"]
        if kind == "frontmatter":
            chunks.append(body)
        elif kind == "chapter":
            part = u.get("part")
            if part and part != current_part:
                current_part = part
                part_title = _PART_TITLES.get(part, f"Partie {part}")
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

    livrables_dir = root / "livrables"
    livrables_dir.mkdir(parents=True, exist_ok=True)
    md_out = livrables_dir / "7 - Livre 2027.md"
    md_out.write_text(yaml_header + body_only, encoding="utf-8")

    meta = {
        "title": title,
        "subtitle": subtitle,
        "author": author,
        "freeze_date": freeze_label,
        "pub_date": pub_label,
        "license_text": license_label,
    }
    return md_out, body_only, meta


def compile_html(root: Path, md_path: Path) -> Path:
    """Compile l'edition HTML autonome via Pandoc."""
    livrables_dir = root / "livrables"
    html_out = livrables_dir / "7 - Livre 2027.html"
    resource_path = f"{livrables_dir}{os.pathsep}{root}"

    with tempfile.NamedTemporaryFile("w", suffix=".html", encoding="utf-8", delete=False) as tf:
        tf.write(_HTML_HEADER_CSS)
        css_header_path = Path(tf.name)

    try:
        cmd = [
            "pandoc",
            str(md_path),
            "-f",
            "markdown-tex_math_dollars+tex_math_single_backslash",
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
        res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
        if res.returncode != 0:
            raise RuntimeError(f"Echec pandoc HTML (code {res.returncode}) :\n{res.stderr}")
    finally:
        css_header_path.unlink(missing_ok=True)
    return html_out


def _escape_typst_content(text: str) -> str:
    return text.replace("\\", "\\\\").replace("#", "\\#").replace("$", "\\$").replace("[", "\\[").replace("]", "\\]")


def _strip_typst_markup(cell: str) -> str:
    s = re.sub(r"#(?:strong|emph|link\([^)]*\))\[", "", cell)
    s = s.replace("[", "").replace("]", "").replace("`", "")
    s = re.sub(r"\\([\[\]$#_])", r"\1", s)
    return " ".join(s.split())


def _break_long_tokens_in_cell(cell: str) -> str:
    def _wrap_raw(m: re.Match[str]) -> str:
        inner = m.group(1)
        if len(inner) >= 14:
            inner = re.sub(r"([_./:])(?=[A-Za-z0-9])", lambda x: x.group(1) + "\u200b", inner)
        return f"`{inner}`"

    return re.sub(r"`([^`\n]+)`", _wrap_raw, cell)


def _split_top_level_args(body: str) -> list[str]:
    args: list[str] = []
    cur: list[str] = []
    paren_stack = [0]
    in_str = False
    in_raw = False
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
        if in_raw:
            cur.append(ch)
            if ch == "`":
                in_raw = False
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
            in_raw = True
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
        m = re.match(r"^\s*columns:\s*\(([^)]+)\)\s*$", arg, re.DOTALL)
        if m:
            col_idx = idx
            ncols = len([x for x in m.group(1).split(",") if x.strip()])
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
                    cell_texts.append(_strip_typst_markup(hs))
                    hs = _break_long_tokens_in_cell(hs)
                fixed_h.append(hs)
            new_args.append("\n    table.header(" + ", ".join(fixed_h) + ",)")
        elif st.startswith("[") and st.endswith("]"):
            cell_texts.append(_strip_typst_markup(st))
            new_args.append(arg.replace(st, _break_long_tokens_in_cell(st), 1))
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
        # Respect exact longest unbroken word width in column (especially narrow header/label columns)
        max_word = max((max((len(w) for w in v.split()), default=0) for v in vals), default=0)
        hdr_max_word = max((len(w) for w in vals[0].split()), default=0) if vals else 0
        eff_word = max(max_word, hdr_max_word)
        req_floor = max(0.095, min(0.27, (eff_word * 4.5 + 13.0) / 321.0))
        min_shares.append(req_floor)
        score = max(float(hdr_len) * 1.15, 0.55 * max(med, 5) + 0.45 * min(p90, 95), min(eff_word, 24) * 1.4)
        col_scores.append(max(score, 8.0))

    floor_sum = sum(min_shares)
    if floor_sum > 0.85:
        scale_f = 0.85 / floor_sum
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


def _postprocess_typst_body(typst_src: str) -> str:
    out: list[str] = []
    pos = 0
    marker = "#table("
    n = len(typst_src)
    while pos < n:
        hit = typst_src.find(marker, pos)
        if hit == -1:
            out.append(typst_src[pos:])
            break
        out.append(typst_src[pos:hit])
        i = hit + len(marker)
        paren_stack = [1]
        in_str = False
        in_raw = False
        while i < n and paren_stack[0] > 0:
            ch = typst_src[i]
            if in_str:
                if ch == "\\":
                    i += 2
                    continue
                if ch == '"':
                    in_str = False
            elif in_raw:
                if ch == "`":
                    in_raw = False
            else:
                if ch == "\\":
                    i += 2
                    continue
                elif ch == '"':
                    in_str = True
                elif ch == "`":
                    in_raw = True
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
            inner = typst_src[hit + len(marker) : i - 1]
            out.append("#table(" + _rebalance_single_table(inner) + ")")
            pos = i
        else:
            out.append(marker)
            pos = hit + len(marker)

    res = "".join(out)

    # Centrer les legendes canoniques *Figure X — ...*, *Fig-00 — ...* et *Tableau X.Y — ...*
    res = re.sub(
        r"(?ms)^(#emph\[(?:Figure\s+|Fig-\d+\s+|Tableau\s+)[^\n]+(?:\n(?!\s*\n)[^\n]+)*\])(?=\s*(?:\n\s*\n|\Z))",
        r'#align(center)[#set par(justify: false); #set text(size: 8.6pt, fill: rgb("#475569")); \1]',
        res,
    )

    # Desactiver la justification excessive et permettre la coupure des URLs dans la bibliographie d'Annexe C
    m_bib = re.search(r"(?m)^=+\s+Bibliographie classée des sources intégrales vérifiées\b[^\n]*(?:\n<[^>\n]+>)?", res)
    if m_bib:
        b_idx = m_bib.end()
        head, tail = res[:b_idx], res[b_idx:]
        tail = re.sub(r"(https?://[^\s`\]\)\"]+)", lambda m: m.group(1).replace("/", "/\u200b").replace("-", "-\u200b"), tail)
        tail = re.sub(
            r"#link\(\"([^\"]+)\"\)\[([^\]]+)\]",
            lambda m: f'#link("{m.group(1).replace("/\u200b", "/").replace("-\u200b", "-")}")[{m.group(2)}]',
            tail,
        )
        res = head + "\n\n#block(width: 100%, breakable: true)[\n#set par(justify: false, leading: 0.56em, spacing: 0.45em)\n" + tail.strip() + "\n]\n"
    return res


def compile_pdf(root: Path, body_md: str, meta: dict) -> Path:
    """Convertit en Typst via Pandoc, injecte dans gabarit-livre.typ et compile en PDF."""
    template_path = Path(__file__).resolve().parent / "gabarit-livre.typ"
    template_src = template_path.read_text(encoding="utf-8")

    p = subprocess.run(
        ["pandoc", "-f", "markdown-tex_math_dollars+tex_math_single_backslash", "-t", "typst"],
        input=body_md,
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

    livrables_dir = root / "livrables"
    livrables_dir.mkdir(parents=True, exist_ok=True)
    typ_tmp = livrables_dir / ".livre-2027-compile.typ"
    pdf_out = livrables_dir / "7 - Livre 2027.pdf"
    typ_tmp.write_text(typst_source, encoding="utf-8")

    try:
        res = subprocess.run(
            ["typst", "compile", "--root", str(root), str(typ_tmp), str(pdf_out)],
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
        if res.returncode != 0:
            raise RuntimeError(f"Echec typst compile (code {res.returncode}) :\n{res.stderr}")
    finally:
        typ_tmp.unlink(missing_ok=True)
    return pdf_out


def build_deliverables(root: Path, make_md: bool = True, make_html: bool = True, make_pdf: bool = True) -> dict[str, Path]:
    """Construit les livrables demandes et retourne leurs chemins."""
    md_path, body_only, meta = assemble_markdown(root)
    results: dict[str, Path] = {}
    if make_md:
        results["md"] = md_path
    if make_html:
        results["html"] = compile_html(root, md_path)
    if make_pdf:
        results["pdf"] = compile_pdf(root, body_only, meta)
    return results


def main() -> int:
    parser = argparse.ArgumentParser(description="Assembleur MD / HTML / PDF du Livre 2027.")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent, help="Racine du livre")
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
