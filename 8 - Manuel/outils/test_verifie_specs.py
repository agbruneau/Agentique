# SPDX-License-Identifier: MIT
"""Tests unitaires de `verifie_specs.py` pour le Volume 8 (`8 - Manuel`)."""

from __future__ import annotations

import json
import shutil
from pathlib import Path

from verifie_specs import validate_specs

REAL_BOOK_DIR = Path(__file__).resolve().parent.parent


def _clone_specs_book(tmp_path: Path, with_trousse: bool = True) -> Path:
    clone = tmp_path / "8 - Manuel"
    clone.mkdir(parents=True)
    shutil.copy2(REAL_BOOK_DIR / "README.md", clone / "README.md")
    shutil.copy2(REAL_BOOK_DIR / ".gitignore", clone / ".gitignore")
    shutil.copytree(REAL_BOOK_DIR / "sources-locales", clone / "sources-locales")
    shutil.copytree(REAL_BOOK_DIR / "specs", clone / "specs")
    if with_trousse:
        (clone / "trousse").mkdir(exist_ok=True)
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


def test_detects_missing_trousse_and_word_budget_drift(tmp_path: Path) -> None:
    clone = _clone_specs_book(tmp_path, with_trousse=False)
    manifest_path = clone / "specs" / "manifest.json"
    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    data["internal_corpus_paths"] = []
    data["stylistic_benchmarks_for_gauntlet"] = []
    data["stylistic_benchmark_sections"] = {}
    data["units"][1]["target_words"] += 500
    manifest_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    errors = validate_specs(clone)
    assert any("trousse" in e.lower() for e in errors)
    assert any("Somme des unites" in e for e in errors)


def test_detects_duplicate_owned_concepts_and_metadata_only_violation(tmp_path: Path) -> None:
    clone = _clone_specs_book(tmp_path)
    manifest_path = clone / "specs" / "manifest.json"
    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    data["internal_corpus_paths"] = []
    data["stylistic_benchmarks_for_gauntlet"] = []
    data["stylistic_benchmark_sections"] = {}
    data["units"][2]["owned_concepts"].append(data["units"][1]["owned_concepts"][0])
    manifest_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    mlr_path = clone / "specs" / "protocole-mlr-2027.json"
    mlr = json.loads(mlr_path.read_text(encoding="utf-8"))
    mlr["strict_access_policy"]["max_metadata_only_pct_in_included_corpus"] = 5.0
    mlr_path.write_text(json.dumps(mlr, ensure_ascii=False, indent=2), encoding="utf-8")

    errors = validate_specs(clone)
    assert any("Collision dans owned_concepts" in e for e in errors)
    assert any("METADATA_ONLY" in e for e in errors)


def test_liminaire_contract_and_ao_ca_g0_coverage(tmp_path: Path) -> None:
    clone = _clone_specs_book(tmp_path)
    _clear_corpus_paths(clone)

    toc_path = clone / "specs" / "toc.md"
    toc_path.write_text(toc_path.read_text(encoding="utf-8").replace("**0.6**", "0-6"), encoding="utf-8")

    prd_path = clone / "specs" / "prd.md"
    prd_path.write_text(prd_path.read_text(encoding="utf-8").replace("AO-08", "AO-XX").replace("CA-20", "CA-XX"), encoding="utf-8")

    aq_path = clone / "specs" / "contrat-aq.md"
    aq_path.write_text(aq_path.read_text(encoding="utf-8").replace("G0", "GX"), encoding="utf-8")

    errors = validate_specs(clone)
    assert any("Sous-section du Liminaire **0.6**" in e for e in errors)
    assert any("AO-08" in e for e in errors)
    assert any("CA-20" in e for e in errors)
    assert any("G0" in e for e in errors)


def test_title_drift_and_unescaped_dollar_across_specs_detected(tmp_path: Path) -> None:
    clone = _clone_specs_book(tmp_path)
    manifest_path = clone / "specs" / "manifest.json"
    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    data["internal_corpus_paths"] = []
    data["stylistic_benchmarks_for_gauntlet"] = []
    data["stylistic_benchmark_sections"] = {}
    data["units"][3]["title"] = "Chapitre 03 — Intitule divergent"
    manifest_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    toc_path = clone / "specs" / "toc.md"
    toc_path.write_text(toc_path.read_text(encoding="utf-8") + "\n- **9.9** Formule $x$\n", encoding="utf-8")
    prd_path = clone / "specs" / "prd.md"
    prd_path.write_text(prd_path.read_text(encoding="utf-8") + "\nBudget 100 $.\n", encoding="utf-8")

    errors = validate_specs(clone)
    assert any("Intitule de ch03 absent de toc.md" in e for e in errors)
    assert any("toc.md" in e and "Symbole $ non echappe" in e for e in errors)
    assert any("prd.md" in e and "Symbole $ non echappe" in e for e in errors)


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
        json.dumps(
            {
                "registry_version": "1.0",
                "freeze_date": "2026-12-02",
                "facts": [{"id": "F1", "owner_chapter": "ch01"}],
            }
        ),
        encoding="utf-8",
    )
    (reg_dir / "glossaire-termes.json").write_text(
        json.dumps(
            {
                "registry_version": "1.0",
                "freeze_date": "2026-12-02",
                "terms": [
                    {
                        "fr": f"terme {i}",
                        "en": f"term {i}",
                        "definition": "Definition valide.",
                        "chapitre_proprietaire": "ch99" if i == 0 else "ch01",
                    }
                    for i in range(12)
                ],
            }
        ),
        encoding="utf-8",
    )
    (reg_dir / "specifications-lplus.json").write_text(
        json.dumps({"registry_version": "1.0", "freeze_date": "2026-12-02", "specs": []}),
        encoding="utf-8",
    )

    errors = validate_specs(clone)
    assert any("statut_preuve" in e for e in errors)
    assert any("ch99" in e for e in errors)
    assert any("matrice-exig-prr-c40.json" in e for e in errors)
    assert any("concordance-taxonomies.json" in e for e in errors)


def test_freeze_window_and_local_sources_exclusion_enforced(tmp_path: Path) -> None:
    clone = _clone_specs_book(tmp_path)
    _clear_corpus_paths(clone)
    mlr_path = clone / "specs" / "protocole-mlr-2027.json"
    mlr = json.loads(mlr_path.read_text(encoding="utf-8"))
    mlr["time_window"]["primary"] = "2023-01-01/2027-06-30"
    mlr_path.write_text(json.dumps(mlr, ensure_ascii=False, indent=2), encoding="utf-8")
    (clone / ".gitignore").write_text("__pycache__/\n", encoding="utf-8")

    errors = validate_specs(clone)
    assert any("Fenetre MLR posterieure" in e for e in errors)
    assert any("sources-locales/*" in e for e in errors)


def test_detects_figure_order_swap_and_toc_subsection_drift(tmp_path: Path) -> None:
    clone = _clone_specs_book(tmp_path)
    _clear_corpus_paths(clone)
    manifest_path = clone / "specs" / "manifest.json"
    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    ch04 = next(u for u in data["units"] if u["id"] == "ch04")
    ch04["figures"] = list(reversed(ch04["figures"]))
    manifest_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    toc_path = clone / "specs" / "toc.md"
    toc_txt = toc_path.read_text(encoding="utf-8")
    toc_txt = toc_txt.replace("- **Question directrice** :", "- **Note** :", 1)
    toc_path.write_text(toc_txt, encoding="utf-8")

    errors = validate_specs(clone)
    assert any("Ordre des figures" in e or "Fig-08" in e for e in errors)
    assert any("Question directrice" in e for e in errors)


def test_detects_stale_freeze_date_and_forbidden_tech_id_ban(tmp_path: Path) -> None:
    clone = _clone_specs_book(tmp_path)
    _clear_corpus_paths(clone)

    mlr_path = clone / "specs" / "protocole-mlr-2027.json"
    mlr = json.loads(mlr_path.read_text(encoding="utf-8"))
    mlr["freeze_date"] = "2026-12-31"
    mlr_path.write_text(json.dumps(mlr, ensure_ascii=False, indent=2), encoding="utf-8")

    manifest_path = clone / "specs" / "manifest.json"
    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    data["forbidden_prose_regexes"].append("\\bEXIG-[A-Z]+-\\d{2}\\b")
    manifest_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    errors = validate_specs(clone)
    assert any("2026-12-02" in e and "freeze_date" in e for e in errors)
    assert any("EXIG-SEC-06" in e for e in errors)
