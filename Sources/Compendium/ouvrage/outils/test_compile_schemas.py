# SPDX-License-Identifier: MIT
"""Tests TDD unitaires et d'intégration pour `compile_schemas_compendium.py` (Task 3 / CA-08 / CA-22)."""

from __future__ import annotations

import json
import os
import struct
import subprocess
import sys
import zlib
from pathlib import Path

import pytest

TOOLS_DIR = Path(__file__).resolve().parent
BOOK_DIR = TOOLS_DIR.parent
REPO_ROOT = BOOK_DIR.parents[2]
CATALOG_PATH = REPO_ROOT / "Sources" / "Cartographie" / "donnees" / "catalogue-schemas-prd.json"
COMPILE_SCRIPT = TOOLS_DIR / "compile_schemas_compendium.py"

if str(TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(TOOLS_DIR))

from compile_schemas_compendium import (  # noqa: E402
    EXPECTED_SVG_COUNT,
    EXPECTED_MMD_COUNT,
    EXPECTED_PUML_COUNT,
    EXPECTED_TOTAL_SCHEMAS,
    MAX_NODES_PER_SCHEMA,
    MIN_NODES_PER_SCHEMA,
    compile_schemas,
    count_schema_elements,
    extract_mmd_elements,
    extract_puml_elements,
    extract_svg_elements,
    load_catalog,
    validate_render,
    validate_sources,
)


def _make_valid_png_bytes(width: int = 300, height: int = 200) -> bytes:
    def _chunk(tag: bytes, data: bytes) -> bytes:
        return struct.pack("!I", len(data)) + tag + data + struct.pack("!I", zlib.crc32(tag + data) & 0xFFFFFFFF)

    ihdr = struct.pack("!IIBBBBB", width, height, 8, 6, 0, 0, 0)
    raw_scanlines = b"".join(b"\x00" + (b"\x1b\x4f\x72\xff" * width) for _ in range(height))
    idat = zlib.compress(raw_scanlines)
    return b"\x89PNG\r\n\x1a\n" + _chunk(b"IHDR", ihdr) + _chunk(b"IDAT", idat) + _chunk(b"IEND", b"")


def _make_valid_svg_infographic(node_count: int = 6, extra_text: str = "") -> str:
    nodes = "\n".join(
        f'  <g id="node-{i}" class="node" data-node="true">'
        f'<rect x="{20 + (i - 1) * 120}" y="80" width="100" height="50" rx="6" fill="#EBF2F7" stroke="#1B4F72"/>'
        f'<text x="{70 + (i - 1) * 120}" y="110" text-anchor="middle">Bloc {i}</text>'
        f"</g>"
        for i in range(1, node_count + 1)
    )
    tail = f'<text x="20" y="180">{extra_text}</text>' if extra_text else ""
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 500" width="1000" height="500">\n'
        '  <title>Infographie de test Systèmes d\'agentivité</title>\n'
        f"{nodes}\n"
        f"{tail}\n"
        "</svg>\n"
    )


def _make_valid_puml(node_count: int = 6, extra_line: str = "") -> str:
    nodes = "\n".join(f'rectangle "Bloc {i}" as N{i} #EBF2F7;line:1B4F72' for i in range(1, node_count + 1))
    extra = f"\n{extra_line}" if extra_line else ""
    return f"@startuml\n{nodes}{extra}\nN1 --> N{node_count}\n@enduml\n"


def _make_valid_mmd(node_count: int = 6, extra_line: str = "") -> str:
    edges = "\n".join(f'  N{i}["Bloc {i}"] --> N{i + 1}["Bloc {i + 1}"]' for i in range(1, node_count))
    extra = f"\n  {extra_line}" if extra_line else ""
    return f"flowchart TD\n{edges}{extra}\n"


def _populate_synthetic_compendium(tmp_path: Path) -> Path:
    book = tmp_path / "Sources" / "Compendium" / "ouvrage"
    schemas_dir = book / "schemas"
    rendus_dir = schemas_dir / "rendus"
    rendus_dir.mkdir(parents=True)

    all_schemas = load_catalog(CATALOG_PATH)
    puml_txt = _make_valid_puml(6)
    mmd_txt = _make_valid_mmd(6)
    svg_txt = _make_valid_svg_infographic(6)
    rendered_svg = '<svg xmlns="http://www.w3.org/2000/svg" width="800" height="400"><rect width="10" height="10"/></svg>\n'
    png_bytes = _make_valid_png_bytes()

    for sc in all_schemas:
        sid = sc["schema_id"]
        notation = sc["recommended_notation"]
        if notation == "PlantUML":
            (schemas_dir / f"{sid}.puml").write_text(puml_txt, encoding="utf-8", newline="\n")
            (rendus_dir / f"{sid}.svg").write_text(rendered_svg, encoding="utf-8", newline="\n")
        elif notation == "Mermaid":
            (schemas_dir / f"{sid}.mmd").write_text(mmd_txt, encoding="utf-8", newline="\n")
            (rendus_dir / f"{sid}.png").write_bytes(png_bytes)
        else:
            (schemas_dir / f"{sid}.svg").write_text(svg_txt, encoding="utf-8", newline="\n")
            (rendus_dir / f"{sid}.svg").write_text(svg_txt, encoding="utf-8", newline="\n")

    return book


def test_catalog_quotas_and_100pct_family_coverage() -> None:
    all_schemas = load_catalog(CATALOG_PATH)
    assert EXPECTED_TOTAL_SCHEMAS == 139
    assert EXPECTED_PUML_COUNT == 58
    assert EXPECTED_MMD_COUNT == 23
    assert EXPECTED_SVG_COUNT == 58
    assert MIN_NODES_PER_SCHEMA == 4
    assert MAX_NODES_PER_SCHEMA == 14

    assert len(all_schemas) == 139
    assert sum(1 for s in all_schemas if s["recommended_notation"] == "PlantUML") == 58
    assert sum(1 for s in all_schemas if s["recommended_notation"] == "Mermaid") == 23
    assert sum(1 for s in all_schemas if s["recommended_notation"] == "Infographie SVG bilingue métier-tech") == 58

    covered_fams = {fid for s in all_schemas for fid in s.get("families_covered", [])}
    assert len(covered_fams) == 71


def test_node_extractors_for_puml_mmd_and_svg() -> None:
    puml = """@startuml
legend bottom
  rectangle "Factice" as F1
end legend
package "Zone Z1" {
  rectangle "Composant A" as A
  database "Journal B" as B
}
actor "Humain C" as C
[Passerelle D] as D
A --> B
B --> C
C --> D
@enduml
"""
    assert extract_puml_elements(puml) == ["A", "B", "C", "D"]

    mmd = """flowchart TD
  subgraph Z1["Zone 1"]
    A["Noeud 1"] --> B{"Choix 2"}
    B -->|Oui| C["Action 3"]
    B -->|Non| D["Repli 4"]
  end
  classDef det stroke:#1B4F72
"""
    assert extract_mmd_elements(mmd) == ["A", "B", "C", "D"]

    svg = _make_valid_svg_infographic(5)
    assert len(extract_svg_elements(svg)) == 5


def test_synthetic_139_schemas_pass_strict_check_only(tmp_path: Path) -> None:
    book = _populate_synthetic_compendium(tmp_path)
    errors = compile_schemas(book, catalog_path=CATALOG_PATH, strict=True, check_only=True)
    assert errors == []


def test_schema_factory_enforces_139_quota_and_14_nodes(tmp_path: Path) -> None:
    book = _populate_synthetic_compendium(tmp_path)

    # 1. Suppression d'une source -> quota 139 non atteint
    (book / "schemas" / "SCH-00-01.svg").unlink()
    errors_missing = compile_schemas(book, catalog_path=CATALOG_PATH, strict=True, check_only=True)
    assert any("SCH-00-01" in e and ("manquant" in e.lower() or "139" in e) for e in errors_missing)

    # 2. Restauration puis depassement de densite (> 14 noeuds) sur PUML, MMD et SVG
    (book / "schemas" / "SCH-00-01.svg").write_text(_make_valid_svg_infographic(15), encoding="utf-8", newline="\n")
    (book / "schemas" / "rendus" / "SCH-00-01.svg").write_text(_make_valid_svg_infographic(15), encoding="utf-8", newline="\n")
    (book / "schemas" / "SCH-00-02.puml").write_text(_make_valid_puml(15), encoding="utf-8", newline="\n")
    (book / "schemas" / "SCH-00-04.mmd").write_text(_make_valid_mmd(15), encoding="utf-8", newline="\n")

    errors_dense = compile_schemas(book, catalog_path=CATALOG_PATH, strict=True, check_only=True)
    assert any("SCH-00-01.svg" in e and "15" in e for e in errors_dense)
    assert any("SCH-00-02.puml" in e and "15" in e for e in errors_dense)
    assert any("SCH-00-04.mmd" in e and "15" in e for e in errors_dense)


def test_strict_enforces_min_4_nodes(tmp_path: Path) -> None:
    book = _populate_synthetic_compendium(tmp_path)
    (book / "schemas" / "SCH-00-01.svg").write_text(_make_valid_svg_infographic(3), encoding="utf-8", newline="\n")
    (book / "schemas" / "rendus" / "SCH-00-01.svg").write_text(_make_valid_svg_infographic(3), encoding="utf-8", newline="\n")

    _, errors = validate_sources(book, catalog_path=CATALOG_PATH, strict=True)
    assert any("SCH-00-01.svg" in e and "3" in e for e in errors)


def test_forbidden_vendor_names_and_markers_rejected_in_originals(tmp_path: Path) -> None:
    book = _populate_synthetic_compendium(tmp_path)
    # SCH-01-02 est une creation originale (Infographie SVG)
    (book / "schemas" / "SCH-01-02.svg").write_text(
        _make_valid_svg_infographic(5, extra_text="Plateforme OpenAI ChatGPT et marqueur [S]"),
        encoding="utf-8",
        newline="\n",
    )
    # SCH-06-03 est une creation originale (Mermaid)
    (book / "schemas" / "SCH-06-03.mmd").write_text(
        _make_valid_mmd(5, extra_line='N6["Systems of Agency avec Salesforce"]'),
        encoding="utf-8",
        newline="\n",
    )

    _, errors = validate_sources(book, catalog_path=CATALOG_PATH, strict=True)
    assert any("SCH-01-02" in e and ("OpenAI" in e or "ChatGPT" in e or "produit" in e.lower()) for e in errors)
    assert any("SCH-01-02" in e and "[S]" in e for e in errors)
    assert any("SCH-06-03" in e and "Systems of Agency" in e for e in errors)
    assert any("SCH-06-03" in e and "Salesforce" in e for e in errors)


def test_svg_infographic_deterministic_copy_and_render_validation(tmp_path: Path) -> None:
    book = _populate_synthetic_compendium(tmp_path)
    src_svg = book / "schemas" / "SCH-00-01.svg"
    dst_svg = book / "schemas" / "rendus" / "SCH-00-01.svg"
    dst_svg.unlink()

    # check_only=False sur le seul SCH-00-01 doit copier deterministement vers rendus/
    errors = compile_schemas(
        book,
        catalog_path=CATALOG_PATH,
        strict=False,
        check_only=False,
        schema_ids=["SCH-00-01"],
    )
    assert errors == []
    assert dst_svg.is_file()
    assert dst_svg.read_bytes() == src_svg.read_bytes()

    # Validation d'un PNG corrompu et d'un SVG Syntax Error
    bad_svg = book / "schemas" / "rendus" / "SCH-00-02.svg"
    bad_svg.write_text("<svg><text>Syntax Error</text></svg>", encoding="utf-8")
    bad_png = book / "schemas" / "rendus" / "SCH-00-04.png"
    bad_png.write_bytes(b"corrupt")

    assert any("Syntax Error" in e for e in validate_render(bad_svg, "PlantUML"))
    assert any("Signature PNG invalide" in e for e in validate_render(bad_png, "Mermaid"))


def test_crlf_and_bom_rejected_and_cli_check_only_fails_on_empty_dir(tmp_path: Path) -> None:
    book = _populate_synthetic_compendium(tmp_path)
    p = book / "schemas" / "SCH-00-02.puml"
    p.write_bytes(b"\xef\xbb\xbf" + _make_valid_puml(5).replace("\n", "\r\n").encode("utf-8"))

    _, errors = validate_sources(book, catalog_path=CATALOG_PATH, strict=True)
    assert any("SCH-00-02.puml" in e and ("BOM" in e or "CRLF" in e) for e in errors)

    empty_book = tmp_path / "empty_book"
    empty_book.mkdir()
    proc = subprocess.run(
        [
            sys.executable,
            "-B",
            str(COMPILE_SCRIPT),
            "--root",
            str(empty_book),
            "--catalog",
            str(CATALOG_PATH),
            "--strict",
            "--check-only",
        ],
        capture_output=True,
        text=True,
    )
    assert proc.returncode != 0
