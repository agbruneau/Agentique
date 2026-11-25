#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Assembleur des editions integrales MD et PDF du Tome 8 (Tome 8 - Ingénierie exécutable et homologation vérifiable)."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

_TOOLS_DIR = Path(__file__).resolve().parent
_GABARIT_PDF_DIR = _TOOLS_DIR.parents[2] / "gabarit-pdf"
for _p in (_TOOLS_DIR, _GABARIT_PDF_DIR):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

from _communs import format_french_date, get_freeze_date  # noqa: E402
from compile_pdf import render_typst_document  # noqa: E402
from postprocess_typst import (  # noqa: E402
    USABLE_PAGE_WIDTH_PT as _USABLE_PAGE_WIDTH_PT,
    escape_typst_content as _escape_typst_content,
    postprocess_typst_body as _postprocess_typst_body,
)
from verifie_manuscrit import _FENCE_OPEN_RE, _strip_yaml_and_preserve_lines  # noqa: E402

_DEFAULT_PART_TITLES = {
    "I": "Partie I — Harnais déterministe et confiance cryptographique",
    "II": "Partie II — Politiques hors modèle, sémantique d'effet et homologation vérifiable",
}


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


_OFFICIAL_BOOK_DIR_NAME = "Tome 8 - Ingénierie exécutable et homologation vérifiable"


def _normalize_image_paths(
    text: str,
    fig_ext_map: dict[str, str],
    prefix: str | None = None,
) -> str:
    """Normalise les liens images Fig-XX vers `<prefix>/Fig-XX.ext`."""
    clean_prefix = (prefix or f"../Sources/Tomes/{_OFFICIAL_BOOK_DIR_NAME}/diagrammes/rendus").rstrip("/")

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


def _resolve_deliverable_paths(root: Path, manifest: dict) -> tuple[Path, Path, str]:
    """Resout les chemins de livrables (md, pdf, image_prefix) depuis manifest.json."""
    root = _resolve_book_root(root)
    book_stem = root.name
    consolidated_dir = root.parents[2] / "Tomes"
    default_img_prefix = f"../Sources/Tomes/{book_stem}/diagrammes/rendus"
    deliv = manifest.get("deliverables", {})
    if book_stem == _OFFICIAL_BOOK_DIR_NAME and isinstance(deliv, dict):
        md_rel = str(deliv.get("md") or deliv.get("markdown") or f"../../../Tomes/{book_stem}.md")
        pdf_rel = str(deliv.get("pdf") or f"../../../Tomes/{book_stem}.pdf")
        img_pref = str(deliv.get("image_prefix") or default_img_prefix)
        return (
            (root / md_rel).resolve(),
            (root / pdf_rel).resolve(),
            img_pref,
        )
    return (
        (consolidated_dir / f"{book_stem}.md").resolve(),
        (consolidated_dir / f"{book_stem}.pdf").resolve(),
        default_img_prefix,
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
    """Construit en memoire le Markdown consolide et retourne (full_md, body_sans_yaml, meta)."""
    root = _resolve_book_root(root)
    manifest = json.loads((root / "specs" / "manifest.json").read_text(encoding="utf-8"))
    _, _, default_prefix = _resolve_deliverable_paths(root, manifest)
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
    """Assemble le fichier consolide (../../../Tomes/<livrable>.md) et retourne (path, body_sans_yaml, meta)."""
    root = _resolve_book_root(root)
    manifest = json.loads((root / "specs" / "manifest.json").read_text(encoding="utf-8"))
    md_out, _, img_prefix = _resolve_deliverable_paths(root, manifest)
    full_md, body_only, meta = build_consolidated_markdown(root, image_prefix=img_prefix)
    md_out.parent.mkdir(parents=True, exist_ok=True)
    md_out.write_text(full_md, encoding="utf-8", newline="\n")
    return md_out, body_only, meta


def compile_pdf(root: Path, body_md: str, meta: dict) -> Path:
    """Convertit en Typst via Pandoc, injecte dans Sources/gabarit-pdf/gabarit-collection.typ et compile en ../../../Tomes/<livrable>.pdf."""
    root = _resolve_book_root(root)

    manifest = json.loads((root / "specs" / "manifest.json").read_text(encoding="utf-8"))
    _, pdf_out, _ = _resolve_deliverable_paths(root, manifest)
    fig_ext_map = {
        f["id"]: ("svg" if f["engine"] == "puml" else "png")
        for f in manifest.get("figures", [])
    }
    body_for_pdf = _normalize_image_paths(body_md, fig_ext_map, prefix="/diagrammes/rendus")

    p_conv = subprocess.run(
        ["pandoc", "-f", "markdown-tex_math_dollars+tex_math_single_backslash-citations", "-t", "typst"],
        input=body_for_pdf,
        shell=False,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    if p_conv.returncode != 0:
        raise RuntimeError(f"Echec pandoc -> typst (code {p_conv.returncode}) :\n{p_conv.stderr}")

    body_typst = _postprocess_typst_body(p_conv.stdout)

    lic_escaped = _escape_typst_content(meta["license_text"])
    deliv = manifest.get("deliverables", {}) if root.name == _OFFICIAL_BOOK_DIR_NAME else {}
    pdf_title = str(deliv.get("pdf_title") or meta["title"])
    pdf_collection = str(deliv.get("pdf_collection") or "COLLECTION ARCHITECTURE & GOUVERNANCE AGENTIQUE")
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
                f"*Régime de diffusion* : {lic_escaped} (manuel et figures); "
                f"trousse exécutable `Sources/Tomes/{_OFFICIAL_BOOK_DIR_NAME}/trousse/` et outillage sous licence MIT."
            ),
            "integrity_note": (
                "*Note d'intégrité (`AO-05` & `DC-P12`)* : ouvrage conçu sur cahier des charges humain, "
                "rédigé et vérifié intégralement en six barrières `G0–G5` sur corpus ouvert haché `SHA-256` "
                "et doublures synthétiques hors modèle. Référence figée et vérifiée à la date de gel; "
                "ne constitue ni un avis juridique, ni une certification, ni une homologation sur système réel."
            ),
        },
        typst_root=root,
    )

    pdf_out.parent.mkdir(parents=True, exist_ok=True)

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


def build_deliverables(root: Path, make_md: bool = True, make_pdf: bool = True) -> dict[str, Path]:
    """Construit les livrables demandes dans ../../../Tomes/."""
    root = _resolve_book_root(root)
    results: dict[str, Path] = {}
    if not (make_md or make_pdf):
        return results
    md_path, body_only, meta = assemble_markdown(root)
    if make_md:
        results["md"] = md_path
    if make_pdf:
        results["pdf"] = compile_pdf(root, body_only, meta)
    return results


def main() -> int:
    parser = argparse.ArgumentParser(description=f"Assembleur MD / PDF du Tome 8 ({_OFFICIAL_BOOK_DIR_NAME}).")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent, help=f"Racine du livre (`{_OFFICIAL_BOOK_DIR_NAME}`)")
    parser.add_argument("--all", action="store_true", help="Produire MD et PDF")
    parser.add_argument("--md", action="store_true", help="Produire le Markdown assemble")
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
