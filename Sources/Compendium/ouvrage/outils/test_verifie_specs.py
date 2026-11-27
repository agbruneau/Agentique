# SPDX-License-Identifier: MIT
"""Tests unitaires de `verifie_specs.py` pour le Compendium (`Sources/Compendium/ouvrage/`)."""

from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

TOOLS_DIR = Path(__file__).resolve().parent
REAL_BOOK_DIR = TOOLS_DIR.parent
if str(TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(TOOLS_DIR))

from verifie_specs import validate_specs  # noqa: E402


def _clone_specs_book(tmp_path: Path) -> Path:
    clone = tmp_path / "ouvrage"
    clone.mkdir(parents=True)
    shutil.copytree(REAL_BOOK_DIR / "specs", clone / "specs")
    return clone


def _clear_corpus_paths(clone: Path) -> None:
    manifest_path = clone / "specs" / "manifest.json"
    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    data["internal_corpus_paths"] = []
    data["stylistic_benchmarks_for_gauntlet"] = []
    data["stylistic_benchmark_sections"] = {}
    manifest_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def test_real_specs_are_valid() -> None:
    assert validate_specs(REAL_BOOK_DIR) == []


def test_manifest_exposes_42_units_180k_71_fam_260_thm_139_schemas() -> None:
    manifest = json.loads((REAL_BOOK_DIR / "specs" / "manifest.json").read_text(encoding="utf-8"))
    assert len(manifest["units"]) == 42
    assert manifest["word_budget"]["total_target"] == 180000
    assert manifest["g3_seeds"] == {"pass1": 20270901, "pass2": 20270902}
    assert manifest["deliverables"]["md"] == "../../../Compendium/Compendium.md"
    assert "html" not in manifest["deliverables"]
    assert manifest["deliverables"]["pdf"] == "../../../Compendium/Compendium.pdf"

    chapters = [u for u in manifest["units"] if u["kind"] == "chapter"]
    assert len(chapters) == 36
    assert sum(len(u.get("families", [])) for u in chapters) == 71
    assert sum(len(u.get("themes", [])) for u in chapters) == 260
    assert len(manifest["figures"]) == 139
    assert sum(1 for f in manifest["figures"] if f["engine"] == "puml") == 58
    assert sum(1 for f in manifest["figures"] if f["engine"] == "mmd") == 23
    assert sum(1 for f in manifest["figures"] if f["engine"] == "svg") == 58


def test_detects_word_budget_drift_and_missing_unit(tmp_path: Path) -> None:
    clone = _clone_specs_book(tmp_path)
    _clear_corpus_paths(clone)
    manifest_path = clone / "specs" / "manifest.json"
    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    data["units"][1]["target_words"] += 500
    manifest_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    errors = validate_specs(clone)
    assert any("Somme des unites" in e or "Bornes invalides" in e for e in errors)

    data["units"].pop()
    manifest_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    errors2 = validate_specs(clone)
    assert any("42" in e for e in errors2)


def test_detects_duplicate_owned_concepts_and_family_theme_drift(tmp_path: Path) -> None:
    clone = _clone_specs_book(tmp_path)
    _clear_corpus_paths(clone)
    manifest_path = clone / "specs" / "manifest.json"
    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    data["units"][2]["owned_concepts"].append(data["units"][1]["owned_concepts"][0])
    data["units"][2]["families"].append(data["units"][1]["families"][0])
    manifest_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    mlr_path = clone / "specs" / "protocole-mlr-compendium.json"
    mlr = json.loads(mlr_path.read_text(encoding="utf-8"))
    mlr["strict_access_policy"]["max_metadata_only_pct_in_included_corpus"] = 5.0
    mlr_path.write_text(json.dumps(mlr, ensure_ascii=False, indent=2), encoding="utf-8")

    errors = validate_specs(clone)
    assert any("owned_concepts" in e for e in errors)
    assert any("famille" in e.lower() or "71" in e for e in errors)
    assert any("METADATA_ONLY" in e for e in errors)


def test_detects_stale_freeze_date_and_forbidden_compendium_ids(tmp_path: Path) -> None:
    clone = _clone_specs_book(tmp_path)
    _clear_corpus_paths(clone)

    mlr_path = clone / "specs" / "protocole-mlr-compendium.json"
    mlr = json.loads(mlr_path.read_text(encoding="utf-8"))
    mlr["freeze_date"] = "2026-12-31"
    mlr_path.write_text(json.dumps(mlr, ensure_ascii=False, indent=2), encoding="utf-8")

    manifest_path = clone / "specs" / "manifest.json"
    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    data["forbidden_prose_regexes"].extend([
        r"\bEXIG-[A-Z]+-\d{2}\b",
        r"\bINI-\d{3}\b",
        r"\bSIG-\d{3}\b",
        r"\bDIV-02\b",
        r"\bDISC-01\b",
    ])
    manifest_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    errors = validate_specs(clone)
    assert any("2026-12-02" in e and "freeze_date" in e for e in errors)
    assert any("EXIG-SEC-06" in e for e in errors)
    assert any("INI-043" in e for e in errors)
    assert any("SIG-001" in e for e in errors)
    assert any("DIV-02" in e for e in errors)
    assert any("DISC-01" in e for e in errors)


def test_detects_missing_schema_or_invalid_deliverables(tmp_path: Path) -> None:
    clone = _clone_specs_book(tmp_path)
    _clear_corpus_paths(clone)
    manifest_path = clone / "specs" / "manifest.json"
    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    data["figures"].pop()
    data["deliverables"]["pdf"] = "autre/chemin.pdf"
    manifest_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    errors = validate_specs(clone)
    assert any("139" in e for e in errors)
    assert any("deliverables" in e for e in errors)


def test_populated_registries_validated_when_present(tmp_path: Path) -> None:
    clone = _clone_specs_book(tmp_path)
    _clear_corpus_paths(clone)
    reg_dir = clone / "registre"
    reg_dir.mkdir()
    (reg_dir / "ancres-chronologiques.json").write_text(
        json.dumps({"registry_version": "1.0", "freeze_date": "2026-12-02", "anchors": []}),
        encoding="utf-8",
    )
    (reg_dir / "faits-empiriques.json").write_text(
        json.dumps({
            "registry_version": "1.0",
            "freeze_date": "2026-12-02",
            "facts": [{"id": "F1", "owner_chapter": "ch01"}],
        }),
        encoding="utf-8",
    )
    (reg_dir / "glossaire-termes.json").write_text(
        json.dumps({
            "registry_version": "1.0",
            "freeze_date": "2026-12-02",
            "terms": [
                {
                    "fr": f"terme {i}",
                    "en": f"term {i}",
                    "definition": "Définition valide.",
                    "chapitre_proprietaire": "ch99" if i == 0 else "ch01",
                }
                for i in range(12)
            ],
        }),
        encoding="utf-8",
    )
    (reg_dir / "specifications-lplus.json").write_text(
        json.dumps({"registry_version": "1.0", "freeze_date": "2026-12-02", "specs": []}),
        encoding="utf-8",
    )

    errors = validate_specs(clone)
    assert any("statut_preuve" in e for e in errors)
    assert any("ch99" in e for e in errors)
    assert any("mindmap-complet.json" in e for e in errors)
    assert any("matrice-exig-prr-c40.json" in e for e in errors)
    assert any("concordance-taxonomies.json" in e for e in errors)
