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


def test_liminaire_interoperabilite_contract_enforced(tmp_path: Path) -> None:
    clone = tmp_path / "7 - Livre 2027"
    shutil.copytree(REAL_BOOK_DIR, clone)
    manifest_path = clone / "specs" / "manifest.json"
    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    data["internal_corpus_paths"] = []
    data["stylistic_benchmarks_for_gauntlet"] = []
    # Simuler collision d'un concept du Liminaire avec le Chapitre 05
    data["units"][5]["owned_concepts"].append(data["units"][0]["owned_concepts"][1])
    manifest_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    toc_path = clone / "specs" / "toc.md"
    toc_path.write_text(toc_path.read_text(encoding="utf-8").replace("**0.6**", "0-6"), encoding="utf-8")

    errors = validate_specs(clone)
    assert any("Collision dans owned_concepts" in e for e in errors)
    assert any("Sous-section du Liminaire **0.6**" in e for e in errors)



def test_title_drift_and_unescaped_dollar_in_toc_detected(tmp_path: Path) -> None:
    clone = tmp_path / "7 - Livre 2027"
    shutil.copytree(REAL_BOOK_DIR, clone)
    manifest_path = clone / "specs" / "manifest.json"
    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    data["internal_corpus_paths"] = []
    data["stylistic_benchmarks_for_gauntlet"] = []
    data["stylistic_benchmark_sections"] = {}
    data["units"][8]["title"] = "Chapitre 08 — Intitule divergent"
    manifest_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    toc_path = clone / "specs" / "toc.md"
    toc_path.write_text(toc_path.read_text(encoding="utf-8") + "\n- **9.9** Formule $x$\n", encoding="utf-8")

    errors = validate_specs(clone)
    assert any("Intitule de ch08 absent de toc.md" in e for e in errors)
    assert any("Symbole $ non echappe dans toc.md" in e for e in errors)


def test_registry_entry_without_evidence_status_detected(tmp_path: Path) -> None:
    clone = tmp_path / "7 - Livre 2027"
    shutil.copytree(REAL_BOOK_DIR, clone)
    manifest_path = clone / "specs" / "manifest.json"
    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    data["internal_corpus_paths"] = []
    data["stylistic_benchmarks_for_gauntlet"] = []
    data["stylistic_benchmark_sections"] = {}
    manifest_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    faits_path = clone / "registre" / "faits-empiriques.json"
    faits = json.loads(faits_path.read_text(encoding="utf-8"))
    del faits["facts"][0]["statut_preuve"]
    faits_path.write_text(json.dumps(faits, ensure_ascii=False, indent=2), encoding="utf-8")

    errors = validate_specs(clone)
    assert any("statut_preuve" in e for e in errors)


def test_freeze_window_and_local_sources_exclusion_enforced(tmp_path: Path) -> None:
    clone = tmp_path / "7 - Livre 2027"
    shutil.copytree(REAL_BOOK_DIR, clone, ignore=shutil.ignore_patterns("*.pdf"))
    mlr_path = clone / "specs" / "protocole-mlr-2027.json"
    mlr = json.loads(mlr_path.read_text(encoding="utf-8"))
    mlr["time_window"]["primary"] = "2023-01-01/2027-06-30"
    mlr_path.write_text(json.dumps(mlr, ensure_ascii=False, indent=2), encoding="utf-8")
    (clone / ".gitignore").write_text("__pycache__/\n", encoding="utf-8")

    errors = validate_specs(clone)
    assert any("Fenetre MLR posterieure" in e for e in errors)
    assert any("sources-locales/*" in e for e in errors)


def test_detects_figure_order_swap_and_toc_subsection_drift(tmp_path: Path) -> None:
    clone = tmp_path / "7 - Livre 2027"
    shutil.copytree(REAL_BOOK_DIR, clone, ignore=shutil.ignore_patterns("*.pdf"))
    manifest_path = clone / "specs" / "manifest.json"
    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    data["internal_corpus_paths"] = []
    data["stylistic_benchmarks_for_gauntlet"] = []
    data["stylistic_benchmark_sections"] = {}
    ch04 = next(u for u in data["units"] if u["id"] == "ch04")
    ch04["figures"] = list(reversed(ch04["figures"]))
    manifest_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    toc_path = clone / "specs" / "toc.md"
    toc_txt = toc_path.read_text(encoding="utf-8")
    # Retirer une Question directrice dans toc.md
    toc_txt = toc_txt.replace("- **Question directrice** :", "- **Note** :", 1)
    toc_path.write_text(toc_txt, encoding="utf-8")

    errors = validate_specs(clone)
    assert any("Ordre des figures" in e or "Fig-08" in e for e in errors)
    assert any("Question directrice" in e for e in errors)


def test_detects_stale_freeze_date_and_invalid_glossary_owner(tmp_path: Path) -> None:
    clone = tmp_path / "7 - Livre 2027"
    shutil.copytree(REAL_BOOK_DIR, clone, ignore=shutil.ignore_patterns("*.pdf"))
    manifest_path = clone / "specs" / "manifest.json"
    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    data["internal_corpus_paths"] = []
    data["stylistic_benchmarks_for_gauntlet"] = []
    data["stylistic_benchmark_sections"] = {}
    manifest_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    mlr_path = clone / "specs" / "protocole-mlr-2027.json"
    mlr = json.loads(mlr_path.read_text(encoding="utf-8"))
    mlr["freeze_date"] = "2026-12-31"
    mlr_path.write_text(json.dumps(mlr, ensure_ascii=False, indent=2), encoding="utf-8")

    gloss_path = clone / "registre" / "glossaire-termes.json"
    gloss = json.loads(gloss_path.read_text(encoding="utf-8"))
    gloss["terms"][0]["chapitre_proprietaire"] = "ch99"
    gloss_path.write_text(json.dumps(gloss, ensure_ascii=False, indent=2), encoding="utf-8")

    errors = validate_specs(clone)
    assert any("2026-12-02" in e and "freeze_date" in e for e in errors)
    assert any("ch99" in e for e in errors)
