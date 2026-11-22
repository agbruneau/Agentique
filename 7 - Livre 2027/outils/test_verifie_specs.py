"""Tests unitaires de `verifie_specs.py` (cas nominal et cas limites)."""

from __future__ import annotations

import json
import shutil
from pathlib import Path

from verifie_specs import validate_specs

REAL_BOOK_DIR = Path(__file__).resolve().parent.parent


def test_real_specs_are_valid() -> None:
    assert validate_specs(REAL_BOOK_DIR) == []


def test_detects_word_budget_drift(tmp_path: Path) -> None:
    clone = tmp_path / "7 - Livre 2027"
    shutil.copytree(REAL_BOOK_DIR, clone)
    manifest_path = clone / "specs" / "manifest.json"
    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    # Create fake relative files so internal_corpus_paths still pass in tmp_path
    data["internal_corpus_paths"] = []
    data["stylistic_benchmarks_for_gauntlet"] = []
    data["units"][1]["target_words"] += 500
    manifest_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    errors = validate_specs(clone)
    assert any("Somme des unites" in e for e in errors)


def test_detects_duplicate_owned_concepts_and_metadata_only_violation(tmp_path: Path) -> None:
    clone = tmp_path / "7 - Livre 2027"
    shutil.copytree(REAL_BOOK_DIR, clone)
    manifest_path = clone / "specs" / "manifest.json"
    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    data["internal_corpus_paths"] = []
    data["stylistic_benchmarks_for_gauntlet"] = []
    data["units"][2]["owned_concepts"].append(data["units"][1]["owned_concepts"][0])
    manifest_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    mlr_path = clone / "specs" / "protocole-mlr-2027.json"
    mlr = json.loads(mlr_path.read_text(encoding="utf-8"))
    mlr["strict_access_policy"]["max_metadata_only_pct_in_included_corpus"] = 5.0
    mlr_path.write_text(json.dumps(mlr, ensure_ascii=False, indent=2), encoding="utf-8")

    errors = validate_specs(clone)
    assert any("Collision dans owned_concepts" in e for e in errors)
    assert any("METADATA_ONLY" in e for e in errors)
