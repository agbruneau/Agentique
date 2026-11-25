#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Assembleur des éditions intégrales MD et PDF du Compendium (`Sources/Compendium/ouvrage/`)."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import unicodedata
from pathlib import Path
from urllib.parse import urlparse

_TOOLS_DIR = Path(__file__).resolve().parent
_GABARIT_PDF_DIR = _TOOLS_DIR.parents[2] / "gabarit-pdf"
for _p in (_TOOLS_DIR, _GABARIT_PDF_DIR):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

from _communs import format_french_date, get_freeze_date  # noqa: E402
from compile_pdf import render_typst_document  # noqa: E402
from postprocess_typst import (  # noqa: E402
    _transform_inline_backticks,
    escape_typst_content as _escape_typst_content,
    postprocess_typst_body as _postprocess_typst_body,
)
from verifie_manuscrit import _FENCE_OPEN_RE, _strip_yaml_and_preserve_lines  # noqa: E402

_BIBLIO_MARKER_RE = re.compile(r"^\s*<!--\s*BIBLIOGRAPHIE_BRUTE_(?:DEBUT|FIN)\s*-->\s*$", re.MULTILINE)
_SRC_HEAD_RE = re.compile(r"^###\s*\[(\d+)\]\s*(SRC-\d+)\s*[—–-]\s*(.+?)\s*$", re.MULTILINE)


def _shift_markdown_headings(text: str, delta: int) -> str:
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
    """Normalise les liens images SCH-XX-YY (ou Fig-XX) vers `<prefix>/<id>.<ext>`."""
    clean_prefix = (prefix or "../Sources/Compendium/ouvrage/schemas/rendus").rstrip("/")

    def _repl(match: re.Match[str]) -> str:
        alt = match.group(1)
        raw_path = match.group(2).strip()
        m_sch = re.search(r"(SCH-\d{2}-\d{2}|Fig-\d{2})", raw_path)
        if m_sch:
            fid = m_sch.group(1)
            ext = fig_ext_map.get(fid, "svg")
            return f"![{alt}]({clean_prefix}/{fid}.{ext})"
        return match.group(0)

    return re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", _repl, text)


def _strip_biblio_markers(text: str) -> str:
    """Retire les marqueurs HTML techniques BIBLIOGRAPHIE_BRUTE_* dans les livrables assemblés."""
    cleaned = _BIBLIO_MARKER_RE.sub("", text)
    return re.sub(r"\n{3,}", "\n\n", cleaned).strip()


def _unescape_dollars_outside_fences(md_text: str) -> str:
    """Supprime les échappements Markdown `\\$` (prose et backticks inline) hors blocs clôturés."""
    out_lines: list[str] = []
    fence_char: str | None = None
    fence_len = 0
    for ln in md_text.splitlines(keepends=True):
        raw_ln = ln.rstrip("\r\n")
        if fence_char is None:
            m_fence = _FENCE_OPEN_RE.match(raw_ln)
            if m_fence:
                fence_char = m_fence.group(1)[0]
                fence_len = len(m_fence.group(1))
                out_lines.append(ln)
            else:
                out_lines.append(ln.replace(r"\$", "$"))
        else:
            out_lines.append(ln)
            stripped = raw_ln.strip()
            if stripped.startswith(fence_char * fence_len) and stripped == fence_char * len(stripped):
                fence_char = None
                fence_len = 0
    return "".join(out_lines)


def _gfm_slug(heading: str) -> str:
    """Calcule l'ancre GFM standard d'un titre Markdown."""
    s = unicodedata.normalize("NFC", heading).strip().lower()
    s = re.sub(r"`([^`]+)`", r"\1", s)
    s = re.sub(r"[^\w\s-]", "", s, flags=re.UNICODE)
    s = re.sub(r"\s+", "-", s)
    return s.strip("-")


def _build_gfm_toc(body_only: str) -> str:
    """Construit une Table des matières Markdown (H1 et H2) avec ancres GFM pour Compendium.md."""
    toc_lines = ["## Table des matières", ""]
    seen_slugs: dict[str, int] = {}
    fence_char: str | None = None
    fence_len = 0

    for line in body_only.split("\n"):
        if fence_char is None:
            m_open = _FENCE_OPEN_RE.match(line)
            if m_open:
                fence_char = m_open.group(1)[0]
                fence_len = len(m_open.group(1))
                continue
            m_h = re.match(r"^(#{1,2})\s+(.+?)\s*$", line)
            if not m_h:
                continue
            level = len(m_h.group(1))
            title = m_h.group(2).strip()
            base_slug = _gfm_slug(title)
            count = seen_slugs.get(base_slug, 0)
            seen_slugs[base_slug] = count + 1
            anchor = base_slug if count == 0 else f"{base_slug}-{count}"
            indent = "" if level == 1 else "  "
            toc_lines.append(f"{indent}- [{title}](#{anchor})")
        else:
            stripped = line.lstrip()
            if stripped.startswith(fence_char * fence_len) and stripped.strip() == fence_char * len(stripped.strip()):
                fence_char = None
                fence_len = 0

    return "\n".join(toc_lines) + "\n"


def _render_unit_references(root: Path, unit_meta: dict) -> str:
    """Génère la sous-section « Références » d'une unité narrative depuis sources/chXX-sources.md."""
    uid = unit_meta["id"]
    sname = "ch00-sources.md" if uid == "00-liminaire" else f"{uid}-sources.md"
    spath = root / "sources" / sname
    if not spath.is_file():
        return ""

    raw = spath.read_text(encoding="utf-8")
    # S'arrête avant la section éventuelle des exclusions en statut F
    main_part = re.split(r"(?m)^##\s+Exclusions\s+en\s+statut\s+F\b", raw, maxsplit=1)[0]
    matches = list(_SRC_HEAD_RE.finditer(main_part))
    if not matches:
        return ""

    heading = "## Références du liminaire" if unit_meta.get("kind") == "frontmatter" else "## Références du chapitre"
    lines = [heading, ""]

    def _extract_field(block: str, label: str) -> str:
        m = re.search(rf"(?m)^-\s+\*\*{re.escape(label)}\s*:\*\*\s*(.+?)\s*$", block)
        if not m:
            return ""
        val = m.group(1).strip()
        return val.strip("`").strip()

    for idx, m in enumerate(matches):
        num = int(m.group(1))
        src_id = m.group(2).strip()
        title = m.group(3).strip().replace(r"\$", "$")
        start = m.end()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(main_part)
        block = main_part[start:end]

        authors = _extract_field(block, "Auteurs / Émetteur")
        pub_date = _extract_field(block, "Date de publication")
        venue = _extract_field(block, "Organisme / Revue")
        ident = _extract_field(block, "Identifiant")
        url_raw = _extract_field(block, "URL d'origine")
        m_url = re.search(r"https?://[^\s)>]+", url_raw)
        url = m_url.group(0).rstrip(".,;") if m_url else ""

        parts: list[str] = [f"**[{num}]** `{src_id}` — "]
        meta_bits: list[str] = []
        if authors:
            meta_bits.append(authors.rstrip("."))
        meta_bits.append(f"*{title}*")
        if venue and venue.lower() != authors.lower():
            meta_bits.append(venue.rstrip("."))
        if pub_date:
            meta_bits.append(pub_date)
        if ident:
            meta_bits.append(f"`{ident}`")
        meta_bits.append("statut `L+`")
        if url:
            host = urlparse(url).netloc or "source"
            meta_bits.append(f"[{host}]({url})")

        entry_line = f"- {parts[0]}" + ", ".join(meta_bits) + "."
        # Normalise espace avant ':' / ';' en fr-CA sans toucher aux URLs
        entry_line = entry_line.replace(r"\$", "$")
        lines.append(entry_line)

    return "\n".join(lines)


def _resolve_book_root(root: Path) -> Path:
    path = Path(root)
    return path if path.is_absolute() and path.name else path.resolve()


def _resolve_deliverable_paths(root: Path, manifest: dict) -> tuple[Path, Path, str]:
    """Résout les chemins de livrables (md, pdf, image_prefix) vers Compendium/Compendium.*."""
    root = _resolve_book_root(root)
    deliv = manifest.get("deliverables", {}) if isinstance(manifest.get("deliverables"), dict) else {}
    md_rel = str(deliv.get("md") or "../../../Compendium/Compendium.md")
    pdf_rel = str(deliv.get("pdf") or "../../../Compendium/Compendium.pdf")
    img_pref = str(deliv.get("image_prefix") or "../Sources/Compendium/ouvrage/schemas/rendus")
    return (
        (root / md_rel).resolve(),
        (root / pdf_rel).resolve(),
        img_pref,
    )


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
    """Construit en mémoire le Markdown consolidé et retourne (full_md, body_sans_yaml_ni_toc, meta)."""
    root = _resolve_book_root(root)
    manifest = json.loads((root / "specs" / "manifest.json").read_text(encoding="utf-8"))
    _, _, default_prefix = _resolve_deliverable_paths(root, manifest)
    effective_prefix = image_prefix if image_prefix is not None else default_prefix

    part_titles = manifest.get("part_titles", {})
    fig_ext_map = {
        f["id"]: ("png" if f["engine"] == "mmd" else "svg")
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
            raise FileNotFoundError(f"Unité manquante pour l'assemblage : {upath}")

        raw = upath.read_text(encoding="utf-8")
        body, _ = _strip_yaml_and_preserve_lines(raw)
        body = _strip_biblio_markers(body)
        body = _normalize_image_paths(body.strip(), fig_ext_map, prefix=effective_prefix)
        body = _unescape_dollars_outside_fences(body)

        kind = u["kind"]
        if kind in {"frontmatter", "chapter"}:
            refs_block = _render_unit_references(root, u)
            if refs_block:
                body = f"{body.rstrip()}\n\n{refs_block}"

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
    toc_md = _build_gfm_toc(body_only)
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
    return yaml_header + toc_md + "\n" + body_only, body_only, meta


def assemble_markdown(root: Path) -> tuple[Path, str, dict]:
    root = _resolve_book_root(root)
    manifest = json.loads((root / "specs" / "manifest.json").read_text(encoding="utf-8"))
    md_out, _, img_prefix = _resolve_deliverable_paths(root, manifest)
    full_md, body_only, meta = build_consolidated_markdown(root, image_prefix=img_prefix)
    md_out.parent.mkdir(parents=True, exist_ok=True)
    md_out.write_text(full_md, encoding="utf-8", newline="\n")
    return md_out, body_only, meta


def _unescape_dollars_in_inline_code_md(md_text: str) -> str:
    return _transform_inline_backticks(md_text, lambda s: s.replace(r"\$", "$"), respect_escapes=False)


def _unwrap_backticked_latex_math(md_text: str) -> str:
    """Déballe les formules LaTeX `\\(...\\)` / `\\[...\\]` encadrées par erreur de backticks hors blocs clôturés."""
    math_span_re = re.compile(r"(?<!`)`(\\\([^`\n]+\\\)|\\\[[^`\n]+\\\])`(?!`)")
    out_lines: list[str] = []
    fence_char: str | None = None
    fence_len = 0
    for ln in md_text.splitlines(keepends=True):
        raw_ln = ln.rstrip("\r\n")
        if fence_char is None:
            m_fence = _FENCE_OPEN_RE.match(raw_ln)
            if m_fence:
                fence_char = m_fence.group(1)[0]
                fence_len = len(m_fence.group(1))
                out_lines.append(ln)
            else:
                ending = ln[len(raw_ln) :]
                out_lines.append(math_span_re.sub(r"\1", raw_ln) + ending)
        else:
            out_lines.append(ln)
            stripped = raw_ln.strip()
            if stripped.startswith(fence_char * fence_len) and stripped == fence_char * len(stripped):
                fence_char = None
                fence_len = 0
    return "".join(out_lines)


def _format_pass_k_typst(typst_text: str) -> str:
    """Formate `pass^k` ou `pass\\^k` dans les titres Typst en `pass#super[k]` (TdM PDF propre)."""
    return re.sub(
        r"(?m)^(={1,6}\s+[^\n]*)\bpass\\?\^k\b",
        r"\1pass#super[k]",
        typst_text,
    )


def compile_pdf(root: Path, body_md: str, meta: dict) -> Path:
    root = _resolve_book_root(root)
    repo_root = root.parents[2]
    manifest = json.loads((root / "specs" / "manifest.json").read_text(encoding="utf-8"))
    _, pdf_out, _ = _resolve_deliverable_paths(root, manifest)
    fig_ext_map = {
        f["id"]: ("png" if f["engine"] == "mmd" else "svg")
        for f in manifest.get("figures", [])
    }
    body_for_pdf = _unwrap_backticked_latex_math(
        _normalize_image_paths(body_md, fig_ext_map, prefix="/Sources/Compendium/ouvrage/schemas/rendus")
    )

    p_conv = subprocess.run(
        ["pandoc", "-f", "markdown-tex_math_dollars+tex_math_single_backslash-citations", "-t", "typst"],
        input=body_for_pdf,
        shell=False,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    if p_conv.returncode != 0:
        raise RuntimeError(f"Échec pandoc -> typst (code {p_conv.returncode}) :\n{p_conv.stderr}")

    body_typst = _format_pass_k_typst(_postprocess_typst_body(p_conv.stdout))

    lic_escaped = _escape_typst_content(meta["license_text"])
    deliv = manifest.get("deliverables", {})
    pdf_title = str(deliv.get("pdf_title") or meta["title"])
    pdf_collection = str(deliv.get("pdf_collection") or "COLLECTION ARCHITECTURE & GOUVERNANCE AGENTIQUE · COMPENDIUM")
    typst_source = render_typst_document(
        body_typst,
        {
            "title": pdf_title,
            "subtitle": meta["subtitle"],
            "author": meta["author"],
            "collection": pdf_collection,
            "pub_date": meta["pub_date"],
            "freeze_date": meta["freeze_date"],
            "license_badge": meta["license_text"],
            "diffusion_note": (
                f"*Régime de diffusion* : {lic_escaped} (manuscrit et schémas) ; "
                "trousse exécutable `Sources/Tomes/Tome 8 - Ingénierie exécutable et homologation vérifiable/trousse/` et outillage sous licence MIT."
            ),
            "integrity_note": (
                "*Note d'intégrité (`AO-05` & `DC-P12`)* : ouvrage conçu sur cahier des charges humain, "
                "rédigé et vérifié intégralement en six barrières `G0–G5` sur corpus ouvert haché `SHA-256` "
                "et doublures synthétiques hors modèle. Référence figée et vérifiée à la date de gel ; "
                "ne constitue ni un avis juridique, ni une certification, ni une homologation sur système réel."
            ),
        },
        typst_root=repo_root,
    )

    pdf_out.parent.mkdir(parents=True, exist_ok=True)
    res = subprocess.run(
        ["typst", "compile", "--root", str(repo_root), "-", str(pdf_out)],
        input=typst_source,
        shell=False,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    if res.returncode != 0:
        raise RuntimeError(f"Échec typst compile (code {res.returncode}) :\n{res.stderr}")
    return pdf_out


def build_deliverables(root: Path, make_md: bool = True, make_pdf: bool = True) -> dict[str, Path]:
    root = _resolve_book_root(root)
    results: dict[str, Path] = {}
    if make_md:
        md_path, body_only, meta = assemble_markdown(root)
        results["md"] = md_path
    elif make_pdf:
        manifest = json.loads((root / "specs" / "manifest.json").read_text(encoding="utf-8"))
        _, _, img_prefix = _resolve_deliverable_paths(root, manifest)
        _, body_only, meta = build_consolidated_markdown(root, image_prefix=img_prefix)
    if make_pdf:
        results["pdf"] = compile_pdf(root, body_only, meta)
    return results


def main() -> int:
    parser = argparse.ArgumentParser(description="Assembleur MD / PDF du Compendium.")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent, help="Racine Sources/Compendium/ouvrage")
    parser.add_argument("--all", action="store_true", help="Produire MD et PDF")
    parser.add_argument("--md", action="store_true", help="Produire le Markdown assemblé")
    parser.add_argument("--pdf", action="store_true", help="Produire le PDF via Typst")
    args = parser.parse_args()

    make_all = args.all or not (args.md or args.pdf)
    outputs = build_deliverables(
        args.root,
        make_md=make_all or args.md,
        make_pdf=make_all or args.pdf,
    )
    for fmt, path in outputs.items():
        print(f"OK ({fmt.upper()}) : {path} ({path.stat().st_size} octets)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
