#!/usr/bin/env python3
"""Inventorie les 139 schémas compilés du Compendium (SCH-00-01 à SCH-AD-01).

Vérifie :
- le catalogue des 139 figures dans ``Sources/Compendium/ouvrage/specs/manifest.json``
- la présence sur disque de 139/139 fichiers sources dans ``Sources/Compendium/ouvrage/schemas/``
- la présence sur disque de 139/139 rendus dans ``Sources/Compendium/ouvrage/schemas/rendus/``
- la ligne exacte d'inclusion de chaque figure dans ``Compendium/Compendium.md``
  et dans son unité source ``Sources/Compendium/ouvrage/manuscrit/...``

Produit ``Sources/Cartographie/donnees/inventaire-139-schemas-compendium.json``.
"""

from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
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

PART_TO_DOMAIN_ID: dict[str, str] = {
    "LIM": "GLOBAL",
    "P01": "D01",
    "P02": "D02",
    "P03": "D03",
    "P04": "D04",
    "P05": "D05",
    "P06": "D06",
    "P07": "D07",
    "P08": "D08",
    "P09": "D09",
    "P10": "D10",
    "P11": "D11",
    "P12": "D12",
    "ANN": "ANNEXE",
}

ENGINE_TO_RENDER_EXT: dict[str, str] = {
    "svg": ".svg",
    "puml": ".svg",
    "mmd": ".png",
}


def _sha256_file(path: Path) -> str:
    """Calcule l'empreinte SHA-256 hexadécimale d'un fichier."""
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def _unit_part_and_chapter(unit_meta: dict[str, Any]) -> tuple[str, int]:
    """Retourne ``(part_id, chapter_number)`` pour une unité du manifeste."""
    uid = unit_meta["id"]
    if uid == "00-liminaire":
        return "LIM", 0
    if uid.startswith("ch") and uid[2:].isdigit():
        roman = unit_meta.get("part") or ""
        return ROMAN_TO_PART_ID.get(roman, "ANN"), int(uid[2:])
    return "ANN", 0


def _compute_compendium_unit_spans(comp_lines: list[str]) -> dict[str, tuple[int, int]]:
    """Détermine la plage de lignes ``(line_start, line_end)`` de chaque unité dans ``Compendium.md``."""
    anchors: list[tuple[str, int]] = []
    for idx, line in enumerate(comp_lines, start=1):
        if line.startswith("# Liminaire "):
            anchors.append(("00-liminaire", idx))
        else:
            m_ch = re.match(r"^## Chapitre (\d{2})\s+[—–-]", line)
            if m_ch:
                anchors.append((f"ch{m_ch.group(1)}", idx))
            else:
                m_ann = re.match(r"^## Annexe ([A-E])\s+[—–-]", line)
                if m_ann:
                    anchors.append((f"annexe-{m_ann.group(1).lower()}", idx))

    spans: dict[str, tuple[int, int]] = {}
    total = len(comp_lines)
    for pos, (uid, start_ln) in enumerate(anchors):
        end_ln = anchors[pos + 1][1] - 1 if pos + 1 < len(anchors) else total
        spans[uid] = (start_ln, end_ln)
    return spans


def _locate_figure_line(
    lines: list[str],
    schema_id: str,
    start_line: int = 1,
    end_line: int | None = None,
) -> int | None:
    """Repère la ligne exacte d'insertion (priorité à ``![`` ou ``Figure ... SCH-``) dans une plage."""
    hi = min(len(lines), end_line or len(lines))
    lo = max(1, start_line)

    # 1. Ligne d'image Markdown pointant vers le rendu
    for ln in range(lo, hi + 1):
        text = lines[ln - 1]
        if schema_id in text and text.lstrip().startswith("!["):
            return ln
    # 2. Ligne de légende Figure N — SCH-XX-YY
    for ln in range(lo, hi + 1):
        text = lines[ln - 1]
        if schema_id in text and re.search(r"\bFigure\s+\d+\b", text):
            return ln
    # 3. Toute mention dans la plage de l'unité
    for ln in range(lo, hi + 1):
        if schema_id in lines[ln - 1]:
            return ln
    return None


def build_compendium_schemas_inventory(repo_root: Path) -> dict[str, Any]:
    """Construit l'inventaire vérifié des 139 schémas du Compendium."""
    from index_pdf_compendium import CompendiumPdfIndex  # noqa: E402

    ouvrage_dir = repo_root / "Sources" / "Compendium" / "ouvrage"
    manifest_path = ouvrage_dir / "specs" / "manifest.json"
    comp_md_path = repo_root / "Compendium" / "Compendium.md"
    schemas_dir = ouvrage_dir / "schemas"
    rendus_dir = schemas_dir / "rendus"

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    comp_lines = comp_md_path.read_text(encoding="utf-8").splitlines()
    unit_spans = _compute_compendium_unit_spans(comp_lines)
    pdf_index = (
        CompendiumPdfIndex.from_repo(repo_root)
        if (repo_root / "Compendium" / "Compendium.pdf").is_file()
        else None
    )

    units_by_id: dict[str, dict[str, Any]] = {u["id"]: u for u in manifest["units"]}
    figures_raw: list[dict[str, Any]] = manifest["figures"]
    if len(figures_raw) != 139:
        raise ValueError(f"Nombre de figures attendu = 139, trouvé {len(figures_raw)}")

    source_files_on_disk = {
        p.resolve()
        for p in schemas_dir.iterdir()
        if p.is_file() and p.name.startswith("SCH-") and p.suffix in {".svg", ".puml", ".mmd"}
    }
    render_files_on_disk = {
        p.resolve()
        for p in rendus_dir.iterdir()
        if p.is_file() and p.name.startswith("SCH-") and p.suffix in {".svg", ".png"}
    }

    matched_sources: set[Path] = set()
    matched_renders: set[Path] = set()
    unit_lines_cache: dict[str, list[str]] = {}
    items: list[dict[str, Any]] = []
    by_engine: Counter[str] = Counter()
    by_part: Counter[str] = Counter()

    for fig in figures_raw:
        sid = fig["id"]
        uid = fig["unit"]
        engine = fig["engine"]
        if engine not in ENGINE_TO_RENDER_EXT:
            raise ValueError(f"Moteur de schéma inconnu pour {sid} : {engine}")

        src_file = (schemas_dir / f"{sid}.{engine}").resolve()
        ren_ext = ENGINE_TO_RENDER_EXT[engine]
        ren_file = (rendus_dir / f"{sid}{ren_ext}").resolve()

        if not src_file.is_file():
            raise FileNotFoundError(f"Source manquante pour {sid} : {src_file}")
        if not ren_file.is_file():
            raise FileNotFoundError(f"Rendu manquant pour {sid} : {ren_file}")
        matched_sources.add(src_file)
        matched_renders.add(ren_file)

        unit_meta = units_by_id[uid]
        part_id, ch_num = _unit_part_and_chapter(unit_meta)
        domain_id = PART_TO_DOMAIN_ID.get(part_id, "D12")
        rel_man_path = f"Sources/Compendium/ouvrage/{unit_meta['file']}"
        man_abs = repo_root / rel_man_path
        if not man_abs.is_file():
            raise FileNotFoundError(f"Unité manuscrit introuvable pour {sid} : {man_abs}")

        if rel_man_path not in unit_lines_cache:
            unit_lines_cache[rel_man_path] = man_abs.read_text(encoding="utf-8").splitlines()
        man_lines = unit_lines_cache[rel_man_path]

        u_start, u_end = unit_spans.get(uid, (1, len(comp_lines)))
        comp_line = _locate_figure_line(comp_lines, sid, u_start, u_end)
        if comp_line is None:
            comp_line = _locate_figure_line(comp_lines, sid, 1, len(comp_lines))
        if comp_line is None:
            raise ValueError(f"Schéma {sid} introuvable dans Compendium/Compendium.md")

        src_line = _locate_figure_line(man_lines, sid, 1, len(man_lines))
        if src_line is None:
            raise ValueError(f"Schéma {sid} introuvable dans {rel_man_path}")

        pdf_page: int | None = None
        if pdf_index is not None:
            u_pdf_span = pdf_index.heading_pages_by_line.get(u_start)
            if u_pdf_span is None:
                p0 = pdf_index.resolve_line_page(u_start)
                p1 = max(p0, pdf_index.resolve_line_page(u_end))
                u_pdf_span = (p0, p1)
            pdf_page = pdf_index.resolve_figure_page(sid, u_pdf_span)

        by_engine[engine] += 1
        by_part[part_id] += 1

        items.append(
            {
                "schema_id": sid,
                "unit": uid,
                "part_id": part_id,
                "chapter_number": ch_num,
                "domain_id": domain_id,
                "engine": engine,
                "notation": fig["notation"],
                "title": fig["title"],
                "families_covered": list(fig.get("families_covered") or []),
                "themes_vulgarized": list(fig.get("themes_vulgarized") or []),
                "source_path": src_file.relative_to(repo_root).as_posix(),
                "rendered_path": ren_file.relative_to(repo_root).as_posix(),
                "source_bytes": src_file.stat().st_size,
                "rendered_bytes": ren_file.stat().st_size,
                "sha256_source": _sha256_file(src_file),
                "sha256_rendered": _sha256_file(ren_file),
                "compendium_md_file": "Compendium/Compendium.md",
                "compendium_md_line": comp_line,
                "pdf_page": pdf_page,
                "source_file": rel_man_path,
                "source_file_line": src_line,
            }
        )

    if matched_sources != source_files_on_disk:
        raise ValueError(f"Écart sources SCH-* sur disque : {source_files_on_disk ^ matched_sources}")
    if matched_renders != render_files_on_disk:
        raise ValueError(f"Écart rendus SCH-* sur disque : {render_files_on_disk ^ matched_renders}")

    return {
        "schema_version": "1.0.0",
        "lang": "fr-CA",
        "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "generator": "Sources/Cartographie/outils/inventorier_schemas_compendium.py",
        "manifest_source": "Sources/Compendium/ouvrage/specs/manifest.json",
        "compendium_md_source": "Compendium/Compendium.md",
        "totals": {
            "figures_count": len(items),
            "verified_sources_on_disk": len(matched_sources),
            "verified_renders_on_disk": len(matched_renders),
            "verified_compendium_lines": sum(1 for it in items if it["compendium_md_line"] >= 1),
            "verified_source_file_lines": sum(1 for it in items if it["source_file_line"] >= 1),
            "verified_pdf_pages": sum(1 for it in items if isinstance(it.get("pdf_page"), int) and it["pdf_page"] >= 1),
            "by_engine": dict(sorted(by_engine.items())),
            "by_part": {k: by_part[k] for k in sorted(by_part)},
        },
        "figures": items,
    }


def main() -> int:
    """Point d'entrée CLI générant ``Sources/Cartographie/donnees/inventaire-139-schemas-compendium.json``."""
    parser = argparse.ArgumentParser(description="Inventorie les 139 schémas compilés du Compendium.")
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path(__file__).resolve().parents[3],
        help="Racine du dépôt Agentique.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Chemin de sortie JSON.",
    )
    args = parser.parse_args()

    repo_root = args.repo_root.resolve()
    out_path = args.output or (repo_root / "Sources" / "Cartographie" / "donnees" / "inventaire-139-schemas-compendium.json")
    payload = build_compendium_schemas_inventory(repo_root)
    serialized = json.dumps(payload, indent=2, ensure_ascii=False) + "\n"
    out_path.write_text(serialized, encoding="utf-8", newline="\n")
    t = payload["totals"]
    print(
        f"Inventaire Compendium -> {out_path} : {t['figures_count']}/139 figures, "
        f"{t['verified_sources_on_disk']}/139 sources, {t['verified_renders_on_disk']}/139 rendus, "
        f"moteurs={t['by_engine']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
