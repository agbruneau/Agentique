# SPDX-License-Identifier: MIT
"""Tests unitaires et d'integration pour `compile_figures.py` du Volume 8 (CA-08)."""

from __future__ import annotations

import json
import os
import re
import shutil
import struct
import subprocess
import sys
import zlib
from pathlib import Path

from compile_figures import (
    compile_figures,
    count_figure_elements,
    extract_mmd_elements,
    extract_puml_elements,
    validate_render,
    validate_sources,
)

REAL_BOOK_DIR = Path(__file__).resolve().parent.parent
COMPILE_SCRIPT = Path(__file__).resolve().parent / "compile_figures.py"


def _make_valid_png_bytes(width: int = 240, height: int = 180) -> bytes:
    def _chunk(tag: bytes, data: bytes) -> bytes:
        return struct.pack("!I", len(data)) + tag + data + struct.pack("!I", zlib.crc32(tag + data) & 0xFFFFFFFF)

    ihdr = struct.pack("!IIBBBBB", width, height, 8, 6, 0, 0, 0)
    raw_scanlines = b"".join(b"\x00" + (b"\x1b\x36\x5d\xff" * width) for _ in range(height))
    idat = zlib.compress(raw_scanlines)
    return b"\x89PNG\r\n\x1a\n" + _chunk(b"IHDR", ihdr) + _chunk(b"IDAT", idat) + _chunk(b"IEND", b"")


def _make_vol8_fig_book(tmp_path: Path) -> Path:
    book = tmp_path / "8 - Manuel"
    shutil.copytree(REAL_BOOK_DIR / "specs", book / "specs")
    manifest = json.loads((book / "specs" / "manifest.json").read_text(encoding="utf-8"))
    diag_dir = book / "diagrammes"
    rendus_dir = diag_dir / "rendus"
    rendus_dir.mkdir(parents=True)

    puml_nodes = "\n".join(f'rectangle "Bloc {i}" as N{i} #1E4E79' for i in range(1, 10))
    puml_tail = 'rectangle "Modele" as N10 #B45309\nN1 --> N10'
    mmd_edges = "\n".join(f'  N{i}["Noeud {i}"] --> N{i + 1}["Noeud {i + 1}"]' for i in range(1, 10))
    mmd_styles = "\n  classDef det stroke:#1E4E79\n  classDef prob stroke:#B45309\n"

    for fig in manifest["figures"]:
        fid = fig["id"]
        if fig["engine"] == "puml":
            (diag_dir / f"{fid}.puml").write_text(
                f"@startuml\n{puml_nodes}\n{puml_tail}\n@enduml\n",
                encoding="utf-8",
            )
            (rendus_dir / f"{fid}.svg").write_text(
                '<svg xmlns="http://www.w3.org/2000/svg" width="320" height="200"><rect width="10" height="10"/></svg>',
                encoding="utf-8",
            )
        else:
            (diag_dir / f"{fid}.mmd").write_text(
                f"flowchart TD\n{mmd_edges}{mmd_styles}",
                encoding="utf-8",
            )
            (rendus_dir / f"{fid}.png").write_bytes(_make_valid_png_bytes())

    return book


def test_puml_counter_ignores_style_legend_notes_and_counts_all_element_kinds() -> None:
    puml = """@startuml
<style>
.det { BackgroundColor #EBF2F7; }
.prob { BackgroundColor #FFF5E0; }
</style>
skinparam rectangle {
  RoundCorner 8
}
legend bottom
  rectangle factice dans la legende
end legend
note right
  state factice dans une note
end note
package "Zone deterministe" {
  rectangle "Bloc un" as R1 <<det>>
  database "Journal" as R2 <<det>>
  [Composant trois] as R3
}
state "Etat quatre" as S4
participant "Acteur cinq" as P5
R1 --> R2
R2 --> R3
R3 --> S4
S4 --> P5
P5 -> Implicite6 : message
@enduml
"""
    elems = extract_puml_elements(puml)
    assert elems == ["R1", "R2", "R3", "S4", "P5", "Implicite6"]


def test_mmd_counter_ignores_subgraph_classdef_and_counts_unique_nodes() -> None:
    mmd = """%% Commentaire ignoré
%%{init: {'theme': 'base'}}%%
flowchart TD
  subgraph Zone["Conteneur ignoré"]
    A{"Decision ?"} -->|Oui| B["Action 1"]:::det
    A -->|Non| C(["Action 2"]):::prob
  end
  B & C --> D["Validation - flux"]
  D -. "si echec" .-> E["Repli"]
  classDef det fill:#EBF2F7,stroke:#1E4E79
  classDef prob fill:#FFF5E0,stroke:#B45309
"""
    elems = extract_mmd_elements(mmd)
    assert elems == ["A", "B", "C", "D", "E"]


def test_all_9_declared_figures_comply_with_vol8_manifest_and_charte(tmp_path: Path) -> None:
    manifest = json.loads((REAL_BOOK_DIR / "specs" / "manifest.json").read_text(encoding="utf-8"))
    figures = manifest["figures"]
    assert len(figures) == 9
    assert [f["id"] for f in figures] == [f"Fig-{i:02d}" for i in range(9)]
    assert [f["id"] for f in figures if f["engine"] == "puml"] == [
        "Fig-00",
        "Fig-01",
        "Fig-02",
        "Fig-03",
        "Fig-05",
        "Fig-06",
        "Fig-07",
    ]
    assert [f["id"] for f in figures if f["engine"] == "mmd"] == ["Fig-04", "Fig-08"]

    # Valider le jeu synthetique complet (et le reel s'il est deja genere en Tache 4)
    target_book = REAL_BOOK_DIR if (REAL_BOOK_DIR / "diagrammes").is_dir() else _make_vol8_fig_book(tmp_path)
    forbidden = [re.compile(p) for p in manifest["forbidden_prose_regexes"]]
    diag_dir = target_book / "diagrammes"
    rendus_dir = diag_dir / "rendus"

    for fig in figures:
        fid = fig["id"]
        engine = fig["engine"]
        ext = "puml" if engine == "puml" else "mmd"
        render_ext = "svg" if engine == "puml" else "png"

        src = diag_dir / f"{fid}.{ext}"
        rnd = rendus_dir / f"{fid}.{render_ext}"
        assert src.is_file(), f"Source manquante : {src}"
        assert rnd.is_file(), f"Rendu manquant : {rnd}"

        text = src.read_text(encoding="utf-8")
        for pat in forbidden:
            assert not pat.search(text), f"Code ou formule bannie ({pat.pattern}) dans {src}"

        count = count_figure_elements(src, engine)
        assert 10 <= count <= 14, f"{fid} doit contenir 10 a 14 noeuds/etats/participants (trouve {count})"
        assert "#1E4E79" in text and "#B45309" in text, f"Palette deterministe/probabiliste manquante dans {fid}"
        assert validate_render(rnd, engine) == []

    assert compile_figures(target_book, strict=True, check_only=True) == []


def test_strict_fails_when_puml_exceeds_14_nodes(tmp_path: Path) -> None:
    clone = _make_vol8_fig_book(tmp_path)
    puml_path = clone / "diagrammes" / "Fig-00.puml"
    nodes = "\n".join(f'rectangle "Noeud {i}" as N{i}' for i in range(1, 16))
    puml_path.write_text(f"@startuml\n{nodes}\nN1 --> N15\n@enduml\n", encoding="utf-8")

    proc = subprocess.run(
        [sys.executable, "-B", str(COMPILE_SCRIPT), "--root", str(clone), "--strict", "--check-only"],
        capture_output=True,
        text=True,
    )
    assert proc.returncode != 0
    assert "Depassement de densite" in proc.stderr or "15 elements" in proc.stderr


def test_strict_fails_when_puml_sequence_or_state_exceeds_14_elements(tmp_path: Path) -> None:
    clone = _make_vol8_fig_book(tmp_path)
    seq_path = clone / "diagrammes" / "Fig-03.puml"
    parts = "\n".join(f'participant "P{i}" as P{i}' for i in range(1, 16))
    seq_path.write_text(f"@startuml\n{parts}\nP1 -> P15 : msg\n@enduml\n", encoding="utf-8")

    state_path = clone / "diagrammes" / "Fig-06.puml"
    states = "\n".join(f'state "Etat {i}" as S{i}' for i in range(1, 16))
    state_path.write_text(f"@startuml\n{states}\nS1 --> S15\n@enduml\n", encoding="utf-8")

    _, errors = validate_sources(clone, strict=True)
    assert any("Fig-03.puml" in e and "15 elements" in e for e in errors)
    assert any("Fig-06.puml" in e and "15 elements" in e for e in errors)


def test_strict_fails_when_mmd_exceeds_14_nodes(tmp_path: Path) -> None:
    clone = _make_vol8_fig_book(tmp_path)
    mmd_path = clone / "diagrammes" / "Fig-04.mmd"
    edges = "\n".join(f'N{i}["Noeud {i}"] --> N{i + 1}["Noeud {i + 1}"]' for i in range(1, 15))
    mmd_path.write_text(f"flowchart TD\n{edges}\n", encoding="utf-8")

    proc = subprocess.run(
        [sys.executable, "-B", str(COMPILE_SCRIPT), "--root", str(clone), "--strict", "--check-only"],
        capture_output=True,
        text=True,
    )
    assert proc.returncode != 0
    assert "Fig-04.mmd" in proc.stderr and "15 elements" in proc.stderr


def test_strict_allows_tech_ids_and_rejects_banned_markers(tmp_path: Path) -> None:
    clone = _make_vol8_fig_book(tmp_path)
    puml_path = clone / "diagrammes" / "Fig-01.puml"
    nodes = "\n".join(f'rectangle "Bloc {i}" as N{i}' for i in range(1, 10))
    puml_path.write_text(
        f'@startuml\n{nodes}\nrectangle "EXIG-SEC-06 PRR-75 et [L+] Classe 1" as N10\nN1 --> N10\n@enduml\n',
        encoding="utf-8",
    )

    _, errors = validate_sources(clone, strict=True)
    assert not any("EXIG-" in e or "PRR" in e for e in errors)
    assert any("[L+]" in e for e in errors)
    assert any("Classe" in e for e in errors)


def test_strict_fails_when_render_missing_or_corrupt(tmp_path: Path) -> None:
    clone = _make_vol8_fig_book(tmp_path)
    svg_path = clone / "diagrammes" / "rendus" / "Fig-00.svg"
    png_path = clone / "diagrammes" / "rendus" / "Fig-08.png"
    svg_path.unlink(missing_ok=True)
    png_path.unlink(missing_ok=True)

    proc = subprocess.run(
        [sys.executable, "-B", str(COMPILE_SCRIPT), "--root", str(clone), "--strict", "--check-only"],
        capture_output=True,
        text=True,
    )
    assert proc.returncode != 0
    assert "Rendu manquant" in proc.stderr

    svg_path.parent.mkdir(parents=True, exist_ok=True)
    svg_path.write_text("<svg><text>Syntax Error</text></svg>", encoding="utf-8")
    png_path.write_bytes(b"not-a-png")
    errors = compile_figures(clone, strict=True, check_only=True)
    assert any("Syntax Error" in e for e in errors)
    assert any("Signature PNG invalide" in e for e in errors)


def test_puml_counter_handles_alias_as_quoted_label() -> None:
    puml = """@startuml
rectangle R1 as "Premier bloc"
state S2 as "Deuxieme etat"
R1 --> S2
@enduml
"""
    elems = extract_puml_elements(puml)
    assert elems == ["R1", "S2"]


def test_strict_fails_when_fewer_than_10_elements_or_stale_mtime_or_case_insensitive_forbidden(
    tmp_path: Path,
) -> None:
    clone = _make_vol8_fig_book(tmp_path)
    p0 = clone / "diagrammes" / "Fig-00.puml"
    r0 = clone / "diagrammes" / "rendus" / "Fig-00.svg"
    p0.write_text(
        "@startuml\nrectangle A as \"Noeud A\"\nrectangle B as \"Noeud B\"\nA --> B\n@enduml\n",
        encoding="utf-8",
    )
    os.utime(r0, (1_700_000_000, 1_700_000_000))
    os.utime(p0, (1_700_000_500, 1_700_000_500))

    p1 = clone / "diagrammes" / "Fig-01.puml"
    nodes = "\n".join(f'rectangle "Bloc {i}" as N{i}' for i in range(1, 11))
    p1.write_text(
        f"@startuml\n{nodes}\nrectangle \"à l’ère du numérique\" as X\nN1 --> X\n@enduml\n",
        encoding="utf-8",
    )

    errors = compile_figures(clone, strict=True, check_only=True)
    assert any("Densite insuffisante" in e and "Fig-00.puml" in e for e in errors)
    assert any("Rendu obsolete" in e and "Fig-00.svg" in e for e in errors)
    assert any("À l'ère du numérique" in e and "Fig-01.puml" in e for e in errors)
