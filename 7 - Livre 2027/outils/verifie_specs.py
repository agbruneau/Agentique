#!/usr/bin/env python3
"""Verification mecanique de coherence du dossier amont `7 - Livre 2027/specs/`."""

from __future__ import annotations

import json
import math
import re
import sys
from pathlib import Path


def validate_specs(book_dir: Path) -> list[str]:
    errors: list[str] = []
    specs_dir = book_dir / "specs"
    reg_dir = book_dir / "registre"

    required_files = [
        book_dir / "README.md",
        book_dir / "sources-locales" / "README.md",
        specs_dir / "prd.md",
        specs_dir / "toc.md",
        specs_dir / "charte-editoriale.md",
        specs_dir / "manifest.json",
        specs_dir / "protocole-mlr-2027.json",
        specs_dir / "contrat-aq.md",
        specs_dir / "plan-production-aq.md",
        reg_dir / "ancres-chronologiques.json",
        reg_dir / "faits-empiriques.json",
        reg_dir / "glossaire-termes.json",
    ]
    for path in required_files:
        if not path.is_file():
            errors.append(f"Fichier requis manquant : {path}")
    if errors:
        return errors

    try:
        manifest = json.loads((specs_dir / "manifest.json").read_text(encoding="utf-8"))
        mlr = json.loads((specs_dir / "protocole-mlr-2027.json").read_text(encoding="utf-8"))
        ancres = json.loads((reg_dir / "ancres-chronologiques.json").read_text(encoding="utf-8"))
        faits = json.loads((reg_dir / "faits-empiriques.json").read_text(encoding="utf-8"))
        glossaire = json.loads((reg_dir / "glossaire-termes.json").read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return [f"JSON invalide : {exc}"]

    # 1. Validation des budgets de mots et des bornes +-8 %
    wb = manifest["word_budget"]
    tol = wb["tolerance_pct"] / 100.0
    units = manifest["units"]
    unit_ids = [u["id"] for u in units]
    if len(unit_ids) != len(set(unit_ids)):
        errors.append("Identifiants d'unites dupliques dans manifest.json")

    sum_total = sum(u["target_words"] for u in units)
    sum_narrative = sum(u["target_words"] for u in units if u["kind"] in {"frontmatter", "chapter"})
    sum_annexes = sum(u["target_words"] for u in units if u["kind"] == "annex")

    if sum_total != wb["total_target"]:
        errors.append(f"Somme des unites ({sum_total}) != total_target ({wb['total_target']})")
    if sum_narrative != wb["narrative_target"]:
        errors.append(f"Somme narrative ({sum_narrative}) != narrative_target ({wb['narrative_target']})")
    if sum_annexes != wb["annexes_target"]:
        errors.append(f"Somme annexes ({sum_annexes}) != annexes_target ({wb['annexes_target']})")

    exp_tot_min = math.ceil(wb["total_target"] * (1.0 - tol))
    exp_tot_max = math.floor(wb["total_target"] * (1.0 + tol))
    if wb["total_min"] != exp_tot_min or wb["total_max"] != exp_tot_max:
        errors.append(
            f"Bornes globales invalides : ({wb['total_min']}, {wb['total_max']}) "
            f"attendu ({exp_tot_min}, {exp_tot_max})"
        )

    for u in units:
        exp_min = math.ceil(u["target_words"] * (1.0 - tol))
        exp_max = math.floor(u["target_words"] * (1.0 + tol))
        if u["min_words"] != exp_min or u["max_words"] != exp_max:
            errors.append(
                f"Bornes invalides pour {u['id']} : ({u['min_words']}, {u['max_words']}) "
                f"attendu ({exp_min}, {exp_max})"
            )

    # 2. Validation des unites narratives (liminaire + 12 chapitres), concepts possedes et figures
    chapters = [u for u in units if u["kind"] == "chapter"]
    narrative_units = [u for u in units if u["kind"] in {"frontmatter", "chapter"}]
    if len(chapters) != 12:
        errors.append(f"Nombre de chapitres attendu = 12, trouve = {len(chapters)}")
    if len(narrative_units) != 13:
        errors.append(f"Nombre d'unites narratives attendu = 13, trouve = {len(narrative_units)}")

    owned_all: list[str] = []
    for nu in narrative_units:
        owned = nu.get("owned_concepts", [])
        if not owned:
            errors.append(f"Unite narrative {nu['id']} sans owned_concepts")
        owned_all.extend(owned)
    if len(owned_all) != len(set(owned_all)):
        errors.append("Collision dans owned_concepts entre plusieurs unites narratives")

    declared_figs = {f["id"]: f for f in manifest["figures"]}
    if len(declared_figs) != 23:
        errors.append(f"Nombre de figures attendu = 23 (Fig-00..Fig-22), trouve = {len(declared_figs)}")

    assigned_figs = [fid for u in units for fid in u.get("figures", [])]
    if sorted(assigned_figs) != sorted(declared_figs.keys()):
        errors.append("Desaccord entre les figures assignees aux unites et la table figures de manifest.json")
    for fid, fmeta in declared_figs.items():
        unit_obj = next((u for u in units if u["id"] == fmeta["unit"]), None)
        if unit_obj is None or fid not in unit_obj.get("figures", []):
            errors.append(f"Figure {fid} mal rattachee a l'unite {fmeta['unit']}")

    # 3. Validation des regex interdites et de l'existence du corpus interne
    for pattern in manifest["forbidden_prose_regexes"]:
        try:
            re.compile(pattern)
        except re.error as exc:
            errors.append(f"Regex interdite invalide `{pattern}` : {exc}")

    for rel_path in manifest["internal_corpus_paths"] + manifest["stylistic_benchmarks_for_gauntlet"]:
        resolved = (book_dir / rel_path).resolve()
        if not resolved.is_file():
            errors.append(f"Chemin de corpus interne introuvable : {rel_path} -> {resolved}")

    for rel_path in manifest.get("stylistic_benchmark_sections", {}):
        if rel_path not in manifest["stylistic_benchmarks_for_gauntlet"]:
            errors.append(f"Section etalon hors des etalons declares : {rel_path}")

    # 4. Validation du protocole MLR et des axes RQ1..RQ6
    rq_ids = {rq["id"] for rq in mlr["research_questions_and_queries"]}
    if rq_ids != {"RQ1", "RQ2", "RQ3", "RQ4", "RQ5", "RQ6"}:
        errors.append(f"Axes RQ attendus RQ1..RQ6, trouves : {sorted(rq_ids)}")
    if mlr["strict_access_policy"]["max_metadata_only_pct_in_included_corpus"] != 0.0:
        errors.append("Le plafond METADATA_ONLY du protocole MLR doit etre strictement 0.0 %")

    for nu in narrative_units:
        if not nu.get("research_axes"):
            errors.append(f"Unite narrative {nu['id']} sans research_axes")
        for rq in nu.get("research_axes", []):
            if rq not in rq_ids:
                errors.append(f"Axe inconnu {rq} dans {nu['id']}")

    # 5. Validation des registres initiaux, du contrat du Liminaire et des criteres CA-01..CA-18
    chapter_id_set = {ch["id"] for ch in chapters}
    for anchor in ancres["anchors"]:
        for ch_ref in anchor["chapters"]:
            if ch_ref not in chapter_id_set:
                errors.append(f"Ancre {anchor['key']} pointe vers un chapitre inconnu : {ch_ref}")
    for fact in faits["facts"]:
        if fact["owner_chapter"] not in chapter_id_set:
            errors.append(f"Fait {fact['id']} pointe vers un chapitre inconnu : {fact['owner_chapter']}")
    for entry in [*faits["facts"], *ancres["anchors"]]:
        if entry.get("statut_preuve") not in {"a_reancrer", "l_plus"}:
            errors.append(f"Entree de registre sans statut_preuve valide : {entry.get('id', entry.get('key'))}")
    if len(glossaire["terms"]) < 12:
        errors.append("Glossaire initial trop court (< 12 termes)")

    prd_text = (specs_dir / "prd.md").read_text(encoding="utf-8")
    aq_text = (specs_dir / "contrat-aq.md").read_text(encoding="utf-8")
    toc_text = (specs_dir / "toc.md").read_text(encoding="utf-8")

    for sub in ("**0.1**", "**0.2**", "**0.3**", "**0.4**", "**0.5**", "**0.6**"):
        if sub not in toc_text:
            errors.append(f"Sous-section du Liminaire {sub} absente de toc.md")

    # Concordance des intitules manifest.json <-> toc.md (partie apres le premier tiret cadratin)
    for u in units:
        short_title = u["title"].split(" — ", 1)[-1]
        if short_title not in toc_text:
            errors.append(f"Intitule de {u['id']} absent de toc.md : {short_title}")

    # Les intitules de toc.md sont recopies dans le manuscrit : aucun `$` non echappe (CA-06)
    for lineno, line in enumerate(toc_text.splitlines(), start=1):
        if re.search(r"(?<!\\)\$", line):
            errors.append(f"Symbole $ non echappe dans toc.md (ligne {lineno})")

    for idx in range(1, 8):
        ao_id = f"AO-{idx:02d}"
        if ao_id not in prd_text:
            errors.append(f"Anti-objectif {ao_id} absent de prd.md")

    for idx in range(1, 19):
        ca_id = f"CA-{idx:02d}"
        if ca_id not in prd_text:
            errors.append(f"Critere {ca_id} absent de prd.md")
    for idx in range(0, 23):
        fig_id = f"Fig-{idx:02d}"
        if fig_id not in toc_text:
            errors.append(f"Figure {fig_id} absente de toc.md")
    for gate in ("G1", "G2", "G3", "G4", "G5"):
        if gate not in aq_text:
            errors.append(f"Barriere {gate} absente de contrat-aq.md")

    return errors


def main() -> int:
    book_dir = Path(__file__).resolve().parent.parent
    errors = validate_specs(book_dir)
    if errors:
        print("ECHEC de verification des specifications amont :", file=sys.stderr)
        for err in errors:
            print(f"  - {err}", file=sys.stderr)
        return 1
    print(
        "OK : Specifications amont valides (v1.1 : 16 unites = 74 000 mots, Liminaire 0.1-0.6 + 12 chapitres, "
        "23 figures Fig-00..Fig-22, RQ1-RQ6, AO-01..AO-07, CA-01..CA-18, intitules concordants, "
        "registres avec statut de preuve et chemins internes verifies)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
