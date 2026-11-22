"""Tests unitaires et d'integration pour `compile_figures.py` (CA-08)."""

from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
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


def _clone_book(tmp_path: Path) -> Path:
    clone = tmp_path / "7 - Livre 2027"
    shutil.copytree(
        REAL_BOOK_DIR,
        clone,
        ignore=shutil.ignore_patterns("*.pdf", "__pycache__", ".pytest_cache"),
    )
    return clone


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


def test_all_23_declared_figures_exist_and_comply_with_charte() -> None:
    manifest = json.loads((REAL_BOOK_DIR / "specs" / "manifest.json").read_text(encoding="utf-8"))
    figures = manifest["figures"]
    assert len(figures) == 23

    forbidden = [re.compile(p) for p in manifest["forbidden_prose_regexes"]]
    diag_dir = REAL_BOOK_DIR / "diagrammes"
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

        # Verifie la distinction visuelle deterministe vs probabiliste (charte § 4.3)
        assert "#1E4E79" in text and "#B45309" in text, f"Palette deterministe/probabiliste manquante dans {fid}"

        render_errors = validate_render(rnd, engine)
        assert render_errors == [], f"Rendu invalide pour {fid} : {render_errors}"


def test_strict_check_passes_on_real_book() -> None:
    errors = compile_figures(REAL_BOOK_DIR, strict=True, check_only=True)
    assert errors == []


def test_strict_fails_when_puml_exceeds_14_nodes(tmp_path: Path) -> None:
    clone = _clone_book(tmp_path)
    puml_path = clone / "diagrammes" / "Fig-00.puml"
    nodes = "\n".join(f'rectangle "Noeud {i}" as N{i}' for i in range(1, 16))
    puml_path.write_text(f"@startuml\n{nodes}\nN1 --> N15\n@enduml\n", encoding="utf-8")

    proc = subprocess.run(
        [sys.executable, str(COMPILE_SCRIPT), "--root", str(clone), "--strict", "--check-only"],
        capture_output=True,
        text=True,
    )
    assert proc.returncode != 0
    assert "Depassement de densite" in proc.stderr or "15 elements" in proc.stderr


def test_strict_fails_when_puml_sequence_or_state_exceeds_14_elements(tmp_path: Path) -> None:
    clone = _clone_book(tmp_path)
    seq_path = clone / "diagrammes" / "Fig-13.puml"
    parts = "\n".join(f'participant "P{i}" as P{i}' for i in range(1, 16))
    seq_path.write_text(f"@startuml\n{parts}\nP1 -> P15 : msg\n@enduml\n", encoding="utf-8")

    state_path = clone / "diagrammes" / "Fig-04.puml"
    states = "\n".join(f'state "Etat {i}" as S{i}' for i in range(1, 16))
    state_path.write_text(f"@startuml\n{states}\nS1 --> S15\n@enduml\n", encoding="utf-8")

    _, errors = validate_sources(clone, strict=True)
    assert any("Fig-13.puml" in e and "15 elements" in e for e in errors)
    assert any("Fig-04.puml" in e and "15 elements" in e for e in errors)


def test_strict_fails_when_mmd_exceeds_14_nodes(tmp_path: Path) -> None:
    clone = _clone_book(tmp_path)
    mmd_path = clone / "diagrammes" / "Fig-06.mmd"
    edges = "\n".join(f'N{i}["Noeud {i}"] --> N{i + 1}["Noeud {i + 1}"]' for i in range(1, 15))
    mmd_path.write_text(f"flowchart TD\n{edges}\n", encoding="utf-8")

    proc = subprocess.run(
        [sys.executable, str(COMPILE_SCRIPT), "--root", str(clone), "--strict", "--check-only"],
        capture_output=True,
        text=True,
    )
    assert proc.returncode != 0
    assert "Fig-06.mmd" in proc.stderr and "15 elements" in proc.stderr


def test_strict_fails_when_forbidden_code_present(tmp_path: Path) -> None:
    clone = _clone_book(tmp_path)
    puml_path = clone / "diagrammes" / "Fig-01.puml"
    puml_path.write_text(
        '@startuml\nrectangle "Exigence CAP-001 et Classe 1" as A\nrectangle "B" as B\nA --> B\n@enduml\n',
        encoding="utf-8",
    )

    _, errors = validate_sources(clone, strict=True)
    assert any("CAP-" in e for e in errors)
    assert any("Classe" in e for e in errors)


def test_strict_fails_when_render_missing_or_corrupt(tmp_path: Path) -> None:
    clone = _clone_book(tmp_path)
    svg_path = clone / "diagrammes" / "rendus" / "Fig-00.svg"
    png_path = clone / "diagrammes" / "rendus" / "Fig-06.png"
    svg_path.unlink(missing_ok=True)
    png_path.unlink(missing_ok=True)

    proc = subprocess.run(
        [sys.executable, str(COMPILE_SCRIPT), "--root", str(clone), "--strict", "--check-only"],
        capture_output=True,
        text=True,
    )
    assert proc.returncode != 0
    assert "Rendu manquant" in proc.stderr

    # Simule un rendu SVG en erreur PlantUML et un PNG corrompu
    svg_path.parent.mkdir(parents=True, exist_ok=True)
    svg_path.write_text("<svg><text>Syntax Error</text></svg>", encoding="utf-8")
    png_path.write_bytes(b"not-a-png")
    errors = compile_figures(clone, strict=True, check_only=True)
    assert any("Syntax Error" in e for e in errors)
    assert any("Signature PNG invalide" in e for e in errors)
