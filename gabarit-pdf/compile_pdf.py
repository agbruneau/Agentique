#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Compilateur PDF unifie de la collection Agentique fonde sur gabarit-collection.typ.

Permet de compiler :
  - n'importe quel tome catalogue (Tome 1 a Tome 8) dans `gabarit-pdf/volumes.json` ;
  - n'importe quel document Markdown arbitraire (avec metadonnees YAML ou options CLI) ;
  - les pipelines existants `Tomes/Tome 7 - Gouverner l'industrialisation cognitive/outils/assemble_livre.py`
    et `Tomes/Tome 8 - Ingénierie exécutable et homologation vérifiable/outils/assemble_livre.py`.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

GABARIT_DIR = Path(__file__).resolve().parent
REPO_ROOT = GABARIT_DIR.parent
TEMPLATE_PATH = GABARIT_DIR / "gabarit-collection.typ"
CATALOG_PATH = GABARIT_DIR / "volumes.json"

if str(GABARIT_DIR) not in sys.path:
    sys.path.insert(0, str(GABARIT_DIR))

from postprocess_typst import (  # noqa: E402
    escape_typst_content,
    escape_typst_string,
    postprocess_typst_body,
)
from preprocess_md import preprocess_markdown  # noqa: E402


def load_catalog(catalog_path: Path = CATALOG_PATH) -> dict[str, Any]:
    """Charge le catalogue JSON des volumes du depot."""
    return json.loads(catalog_path.read_text(encoding="utf-8"))


def get_volume_config(volume_ref: str, catalog_path: Path = CATALOG_PATH) -> dict[str, Any]:
    """Resout un tome par identifiant (`1`..`8`), slug (`Tome 8 - ...`), nom (`Tome 8`) ou sous-chaine unique."""
    catalog = load_catalog(catalog_path)
    defaults = dict(catalog.get("defaults", {}))
    ref_norm = volume_ref.strip().lower()
    matches: list[dict[str, Any]] = []
    for vol in catalog.get("volumes", []):
        pdf_path = Path(vol.get("default_pdf", ""))
        md_path = Path(vol.get("source_md", ""))
        pdf_stem = pdf_path.stem.lower()
        exact_keys = {
            vol["id"].lower(),
            vol["slug"].lower(),
            pdf_stem,
            pdf_path.name.lower(),
            md_path.name.lower(),
        }
        if ref_norm in exact_keys:
            merged = dict(defaults)
            merged.update(vol)
            return merged
        if ref_norm in vol["slug"].lower() or ref_norm in pdf_stem or ref_norm in vol.get("title", "").lower():
            matches.append(vol)
    if len(matches) == 1:
        merged = dict(defaults)
        merged.update(matches[0])
        return merged
    valid = ", ".join(f"{v['id']} ({v['slug']})" for v in catalog.get("volumes", []))
    raise KeyError(f"Volume introuvable : {volume_ref!r}. Volumes disponibles : {valid}")


def _typst_opt_content(val: str | None, raw_typst: bool = False) -> str:
    if val is None or not str(val).strip():
        return "none"
    inner = str(val) if raw_typst else escape_typst_content(str(val))
    return f"[{inner}]"


def _typst_str_tuple(items: list[str] | tuple[str, ...]) -> str:
    escaped = [f'"{escape_typst_string(str(x))}"' for x in items]
    if len(escaped) == 1:
        return f"({escaped[0]},)"
    return "(" + ", ".join(escaped) + ")"


def _typst_bool(val: bool) -> str:
    return "true" if val else "false"


def _can_import_template(typst_root: Path, template_path: Path = TEMPLATE_PATH) -> str | None:
    """Retourne le chemin d'import absolu Typst (`/gabarit-pdf/...`) si le gabarit est sous `typst_root`."""
    try:
        rel = template_path.resolve().relative_to(typst_root.resolve()).as_posix()
        return "/" + rel
    except ValueError:
        return None


def render_typst_document(
    body_typst: str,
    config: dict[str, Any],
    typst_root: Path = REPO_ROOT,
    template_path: Path = TEMPLATE_PATH,
    raw_notice_typst: bool = True,
) -> str:
    """Assemble le document Typst complet invoquant `collection-pdf(...)` sur `body_typst`.

    Si `template_path` se trouve sous `typst_root`, utilise `#import "/..."` (aucune duplication).
    Si `typst_root` est un repertoire isole (ex. tests pytest en `tmp_path`), integre la source
    canonique de `gabarit-collection.typ` en tete afin que `typst compile --root` reste hermetique.
    """
    import_path = _can_import_template(typst_root, template_path)
    if import_path is not None:
        preamble = f'#import "{import_path}": collection-pdf, divider, horizontalRule\n'
    else:
        preamble = template_path.read_text(encoding="utf-8") + "\n"

    part_prefixes = config.get("part_prefixes") or ["Partie ", "Livre ", "Annexes"]
    chapter_prefixes = config.get("chapter_prefixes") or ["Chapitre ", "Annexe "]

    notice_lines_cfg = config.get("notice_lines")
    if notice_lines_cfg:
        rendered_lines = [
            _typst_opt_content(line, raw_typst=raw_notice_typst) for line in notice_lines_cfg
        ]
        notice_arg = "(" + ", ".join(rendered_lines) + ("," if len(rendered_lines) == 1 else "") + ")"
    else:
        notice_arg = "none"

    call_lines = [
        "#show: collection-pdf.with(",
        f"  title: {_typst_opt_content(config.get('title', 'Sans titre'))},",
        f"  subtitle: {_typst_opt_content(config.get('subtitle'))},",
        f"  author: {_typst_opt_content(config.get('author', 'André-Guy Bruneau, M.Sc IT'))},",
        f"  collection: {_typst_opt_content(config.get('collection', 'COLLECTION ARCHITECTURE & GOUVERNANCE AGENTIQUE'))},",
        f"  pub-date: {_typst_opt_content(config.get('pub_date'))},",
        f"  freeze-date: {_typst_opt_content(config.get('freeze_date'))},",
        f"  edition-line: {_typst_opt_content(config.get('edition_line'))},",
        f"  license-badge: {_typst_opt_content(config.get('license_badge'))},",
        f"  notice-lines: {notice_arg},",
        f"  diffusion-note: {_typst_opt_content(config.get('diffusion_note'), raw_typst=raw_notice_typst)},",
        f"  integrity-note: {_typst_opt_content(config.get('integrity_note'), raw_typst=raw_notice_typst)},",
        f"  show-cover: {_typst_bool(bool(config.get('show_cover', True)))},",
        f"  show-title-page: {_typst_bool(bool(config.get('show_title_page', True)))},",
        f"  show-toc: {_typst_bool(bool(config.get('show_toc', True)))},",
        f"  toc-title: {_typst_opt_content(config.get('toc_title', 'Table des matières'))},",
        f"  toc-depth: {int(config.get('toc_depth', 2))},",
        f'  lang: "{escape_typst_string(str(config.get("lang", "fr")))}",',
        f'  region: "{escape_typst_string(str(config.get("region", "CA")))}",',
        f"  part-prefixes: {_typst_str_tuple(part_prefixes)},",
        f"  chapter-prefixes: {_typst_str_tuple(chapter_prefixes)},",
        f"  numbered-h2-chapters: {_typst_bool(bool(config.get('numbered_h2_chapters', False)))},",
        f"  breakable-long-code: {_typst_bool(bool(config.get('breakable_long_code', True)))},",
        f"  code-break-threshold: {int(config.get('code_break_threshold', 40))},",
        f"  breakable-long-quote: {_typst_bool(bool(config.get('breakable_long_quote', True)))},",
        ")",
    ]
    return preamble + "\n" + "\n".join(call_lines) + "\n\n" + body_typst


def pandoc_markdown_to_typst(
    md_body: str,
    pandoc_from: str = "markdown-tex_math_dollars+tex_math_single_backslash-citations",
) -> str:
    """Convertit un corps Markdown en Typst via Pandoc."""
    res = subprocess.run(
        ["pandoc", "-f", pandoc_from, "-t", "typst"],
        input=md_body,
        shell=False,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    if res.returncode != 0:
        raise RuntimeError(f"Echec pandoc -> typst (code {res.returncode}) :\n{res.stderr}")
    return res.stdout


def compile_typst_source(
    typst_source: str,
    pdf_out: Path,
    typst_root: Path = REPO_ROOT,
) -> Path:
    """Compile une source Typst en PDF via `typst compile --root`."""
    pdf_out.parent.mkdir(parents=True, exist_ok=True)
    res = subprocess.run(
        ["typst", "compile", "--root", str(typst_root), "-", str(pdf_out)],
        input=typst_source,
        shell=False,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    if res.returncode != 0:
        raise RuntimeError(f"Echec typst compile (code {res.returncode}) :\n{res.stderr}")
    return pdf_out


def compile_markdown_to_pdf(
    md_text: str,
    pdf_out: Path,
    config: dict[str, Any] | None = None,
    *,
    md_source_path: Path | None = None,
    typst_root: Path = REPO_ROOT,
    emit_typst: Path | None = None,
    pandoc_from: str = "markdown-tex_math_dollars+tex_math_single_backslash-citations",
) -> Path:
    """Pipeline complet : pre-traitement MD -> Pandoc -> post-traitement Typst -> PDF."""
    cfg = dict(config or {})
    clean_md, yaml_meta = preprocess_markdown(
        md_text,
        repo_root=typst_root,
        md_source_path=md_source_path,
        options=cfg,
    )

    # Remplir les champs manquants depuis le YAML liminaire si present
    if yaml_meta:
        cfg.setdefault("title", yaml_meta.get("title", "Sans titre"))
        if yaml_meta.get("subtitle"):
            cfg.setdefault("subtitle", yaml_meta["subtitle"])
        if yaml_meta.get("author"):
            cfg.setdefault("author", yaml_meta["author"])
        if yaml_meta.get("rights"):
            cfg.setdefault("license_badge", yaml_meta["rights"])
        if yaml_meta.get("date") and not cfg.get("pub_date") and not cfg.get("edition_line"):
            cfg["edition_line"] = yaml_meta["date"]

    raw_typst = pandoc_markdown_to_typst(clean_md, pandoc_from=pandoc_from)
    body_typst = postprocess_typst_body(raw_typst)
    full_typst = render_typst_document(body_typst, cfg, typst_root=typst_root)

    if emit_typst is not None:
        emit_typst.parent.mkdir(parents=True, exist_ok=True)
        emit_typst.write_text(full_typst, encoding="utf-8", newline="\n")

    return compile_typst_source(full_typst, pdf_out, typst_root=typst_root)


def compile_volume(
    volume_ref: str,
    output_path: Path | None = None,
    *,
    in_place: bool = False,
    inject_diagrams: bool | None = None,
    emit_typst: Path | None = None,
    repo_root: Path = REPO_ROOT,
    catalog_path: Path = CATALOG_PATH,
) -> Path:
    """Compile un volume du catalogue (`1`..`8`) vers `output_path` (ou `Corpus/` si `in_place=True`)."""
    cfg = get_volume_config(volume_ref, catalog_path=catalog_path)
    src_md = repo_root / cfg["source_md"]
    if not src_md.is_file():
        raise FileNotFoundError(f"Source Markdown introuvable : {src_md}")

    if output_path is None:
        if not in_place:
            raise ValueError(
                "Par securite, specifiez --output / --output-dir, ou ajoutez --in-place "
                "pour ecraser le PDF dans Corpus/."
            )
        pdf_out = repo_root / cfg["default_pdf"]
    else:
        pdf_out = output_path

    if inject_diagrams is not None:
        cfg["inject_diagrams"] = inject_diagrams
    md_text = src_md.read_text(encoding="utf-8")
    return compile_markdown_to_pdf(
        md_text,
        pdf_out,
        cfg,
        md_source_path=src_md,
        typst_root=repo_root,
        emit_typst=emit_typst,
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Compilateur PDF unifié de la collection Agentique (gabarit de référence Tome 8)."
    )
    src_group = parser.add_mutually_exclusive_group(required=True)
    src_group.add_argument("--list", action="store_true", help="Lister les 8 tomes du catalogue")
    src_group.add_argument(
        "--volume",
        help="Identifiant (1..8), slug de répertoire (ex. Tome 8 - ...) ou sous-chaîne unique (ex. Tome 8)",
    )
    src_group.add_argument("--all", action="store_true", help="Compiler les 8 tomes du catalogue")
    src_group.add_argument("--input", type=Path, help="Fichier Markdown arbitraire à compiler")

    parser.add_argument("--output", type=Path, help="Chemin du PDF de sortie (avec --volume ou --input)")
    parser.add_argument("--output-dir", type=Path, help="Répertoire de sortie (avec --all ou --volume)")
    parser.add_argument(
        "--in-place",
        action="store_true",
        help="Autoriser l'écrasement des PDF cibles (Tome 1 à Tome 8) dans Corpus/",
    )
    parser.add_argument(
        "--inject-diagrams",
        dest="inject_diagrams",
        action="store_true",
        default=None,
        help="Forcer l'injection automatique des diagrammes rendus (.svg/.png) depuis Tomes/<Tome>/Diagrammes/rendus/",
    )
    parser.add_argument(
        "--no-inject-diagrams",
        dest="inject_diagrams",
        action="store_false",
        help="Desactiver l'injection automatique des diagrammes rendus meme si activee dans volumes.json",
    )
    parser.add_argument("--emit-typst", type=Path, help="Ecrire aussi la source Typst generee (.typ)")
    parser.add_argument("--title", help="Surcharge du titre (mode --input)")
    parser.add_argument("--subtitle", help="Surcharge du sous-titre (mode --input)")
    parser.add_argument("--author", help="Surcharge de l'auteur (mode --input)")
    parser.add_argument("--license", dest="license_badge", help="Surcharge du badge de licence (mode --input)")
    parser.add_argument("--toc-depth", type=int, help="Profondeur de la table des matieres")
    args = parser.parse_args(argv)

    if args.list:
        catalog = load_catalog()
        for v in catalog["volumes"]:
            lic = v.get("license_badge") or "aucune"
            print(f"[{v['id']}] {v['title']} ({lic}) | {v['source_md']} -> {v['default_pdf']}")
        return 0

    if args.all:
        catalog = load_catalog()
        if args.output_dir is None and not args.in_place:
            parser.error("Avec --all, specifiez --output-dir <dir> ou --in-place.")
        for v in catalog["volumes"]:
            out = (args.output_dir / Path(v["default_pdf"]).name) if args.output_dir else None
            pdf = compile_volume(
                v["id"],
                output_path=out,
                in_place=args.in_place,
                inject_diagrams=args.inject_diagrams,
            )
            print(f"OK [{v['id']}] : {pdf} ({pdf.stat().st_size:,} octets)")
        return 0

    if args.volume:
        out = args.output
        if out is None and args.output_dir is not None:
            cfg = get_volume_config(args.volume)
            out = args.output_dir / Path(cfg["default_pdf"]).name
        pdf = compile_volume(
            args.volume,
            output_path=out,
            in_place=args.in_place,
            inject_diagrams=args.inject_diagrams,
            emit_typst=args.emit_typst,
        )
        print(f"OK : {pdf} ({pdf.stat().st_size:,} octets)")
        return 0

    # Mode --input arbitraire
    if not args.input.is_file():
        parser.error(f"Fichier introuvable : {args.input}")
    out = args.output or args.input.with_suffix(".pdf")
    cfg: dict[str, Any] = {}
    if args.title:
        cfg["title"] = args.title
    if args.subtitle:
        cfg["subtitle"] = args.subtitle
    if args.author:
        cfg["author"] = args.author
    if args.license_badge:
        cfg["license_badge"] = args.license_badge
    if args.toc_depth is not None:
        cfg["toc_depth"] = args.toc_depth

    pdf = compile_markdown_to_pdf(
        args.input.read_text(encoding="utf-8"),
        out,
        cfg,
        md_source_path=args.input.resolve(),
        typst_root=REPO_ROOT,
        emit_typst=args.emit_typst,
    )
    print(f"OK : {pdf} ({pdf.stat().st_size:,} octets)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
