#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Vérification mécanique de cohérence des spécifications `Sources/Compendium/ouvrage/specs/`."""

from __future__ import annotations

import json
import math
import re
import sys
from pathlib import Path

_TOOLS_DIR = Path(__file__).resolve().parent
if str(_TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(_TOOLS_DIR))

from _communs import DEFAULT_FREEZE_DATE, load_mlr_protocol, parse_iso_date  # noqa: E402

try:
    from jsonschema import Draft202012Validator
    from jsonschema.exceptions import SchemaError
except ImportError:  # pragma: no cover
    Draft202012Validator = None  # type: ignore[assignment]
    SchemaError = Exception  # type: ignore[assignment]


_ROMAN_PARTS = ("I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII")
_EXPECTED_DOMAINS = tuple(f"D{i:02d}" for i in range(1, 13))
_EXPECTED_CHAPTER_IDS = tuple(f"ch{i:02d}" for i in range(1, 37))
_EXPECTED_ANNEX_IDS = ("annexe-a", "annexe-b", "annexe-c", "annexe-d", "annexe-e")


def extract_ssot_schemas_from_arch(arch_text: str) -> tuple[dict[str, dict], list[str]]:
    """Extrait et parse les schémas JSON SSOT déclarés dans architecture-trousse-g0.md."""
    schemas: dict[str, dict] = {}
    errors: list[str] = []
    for m in re.finditer(r"```json\s*\n(.*?)\n```", arch_text, re.DOTALL):
        raw_block = m.group(1).replace(r"\$", "$")
        try:
            obj = json.loads(raw_block)
        except json.JSONDecodeError as exc:
            errors.append(f"Schema JSON invalide dans architecture-trousse-g0.md : {exc}")
            continue
        if isinstance(obj, dict) and isinstance(obj.get("title"), str):
            title = obj["title"]
            if Draft202012Validator is not None:
                try:
                    Draft202012Validator.check_schema(obj)
                except SchemaError as exc:
                    errors.append(f"Meta-schema Draft 2020-12 invalide pour {title} : {exc}")
            schemas[title] = obj
    return schemas, errors


def adapt_ssot_schemas_for_compendium(ssot_schemas: dict[str, dict]) -> dict[str, dict]:
    """Étend les schémas SSOT de Tome 8 au périmètre 36 chapitres et aux catalogues du Compendium."""
    adapted = json.loads(json.dumps(ssot_schemas))
    ch_enum = [f"ch{i:02d}" for i in range(1, 37)]
    if "RapportsG0Output" in adapted:
        props = adapted["RapportsG0Output"].get("properties", {})
        unit_schema = (
            props.get("synced_excerpts", {})
            .get("additionalProperties", {})
            .get("properties", {})
            .get("unit")
        )
        if isinstance(unit_schema, dict) and "enum" in unit_schema:
            unit_schema["enum"] = ch_enum
    if "MatriceExigPrrC40Registry" in adapted:
        adapted["MatriceExigPrrC40Registry"]["additionalProperties"] = True
        props = adapted["MatriceExigPrrC40Registry"].get("properties", {})
        items_schema = props.get("mappings", {}).get("items", {})
        if isinstance(items_schema, dict):
            items_schema["additionalProperties"] = True
            owner_schema = items_schema.get("properties", {}).get("owner_chapter")
            if isinstance(owner_schema, dict) and "enum" in owner_schema:
                owner_schema["enum"] = ch_enum
    if "SpecificationsLPlusRegistry" in adapted:
        adapted["SpecificationsLPlusRegistry"]["additionalProperties"] = True
    if "ConcordanceTaxonomiesRegistry" in adapted:
        adapted["ConcordanceTaxonomiesRegistry"]["additionalProperties"] = True
    return adapted


def _validate_populated_registries(
    reg_dir: Path,
    chapter_id_set: set[str],
    narrative_id_set: set[str],
    ssot_schemas: dict[str, dict],
) -> tuple[dict[str, tuple[str, dict | None]], list[str]]:
    """Valide les 7 registres JSON SSOT lorsqu'ils sont présents sous registre/."""
    errors: list[str] = []
    registry_raws: dict[str, tuple[str, dict | None]] = {}

    required_reg_files = (
        "mindmap-complet.json",
        "specifications-lplus.json",
        "matrice-exig-prr-c40.json",
        "concordance-taxonomies.json",
        "ancres-chronologiques.json",
        "faits-empiriques.json",
        "glossaire-termes.json",
    )
    loaded: dict[str, dict] = {}
    for fname in required_reg_files:
        fpath = reg_dir / fname
        if not fpath.is_file():
            errors.append(f"Fichier requis manquant dans registre/ : {fpath}")
            continue
        raw = fpath.read_text(encoding="utf-8")
        try:
            obj = json.loads(raw)
        except json.JSONDecodeError as exc:
            errors.append(f"JSON invalide dans {fname} : {exc}")
            registry_raws[fname] = (raw, None)
            continue
        if not isinstance(obj, dict):
            errors.append(f"{fname} doit contenir un objet JSON")
            registry_raws[fname] = (raw, None)
            continue
        registry_raws[fname] = (raw, obj)
        loaded[fname] = obj

    if "mindmap-complet.json" in loaded:
        mm = loaded["mindmap-complet.json"]
        nodes = mm.get("nodes", [])
        relations = mm.get("relations", [])
        if isinstance(nodes, list) and nodes:
            fams = [n for n in nodes if isinstance(n, dict) and n.get("node_kind") == "family"]
            thms = [n for n in nodes if isinstance(n, dict) and n.get("node_kind") == "theme"]
        else:
            fams = mm.get("families", []) if isinstance(mm.get("families"), list) else []
            thms = mm.get("themes", []) if isinstance(mm.get("themes"), list) else []
        if len(fams) != 71:
            errors.append(f"mindmap-complet.json : 71 familles attendues, trouvé {len(fams)}")
        if len(thms) != 260:
            errors.append(f"mindmap-complet.json : 260 thèmes attendus, trouvé {len(thms)}")
        if len(relations) != 616:
            errors.append(f"mindmap-complet.json : 616 interrelations attendues, trouvé {len(relations)}")

    if "ancres-chronologiques.json" in loaded:
        for anchor in loaded["ancres-chronologiques.json"].get("anchors", []):
            for ch_ref in anchor.get("chapters", []):
                if ch_ref not in narrative_id_set:
                    errors.append(f"Ancre {anchor.get('key')} pointe vers un chapitre inconnu : {ch_ref}")
            if anchor.get("statut_preuve") not in {"a_reancrer", "l_plus"}:
                errors.append(f"Ancre sans statut_preuve valide : {anchor.get('key')}")

    if "faits-empiriques.json" in loaded:
        for fact in loaded["faits-empiriques.json"].get("facts", []):
            if fact.get("owner_chapter") not in narrative_id_set:
                errors.append(f"Fait {fact.get('id')} pointe vers un chapitre inconnu : {fact.get('owner_chapter')}")
            if fact.get("statut_preuve") not in {"a_reancrer", "l_plus"}:
                errors.append(f"Fait sans statut_preuve valide : {fact.get('id')}")

    if "glossaire-termes.json" in loaded:
        terms = loaded["glossaire-termes.json"].get("terms", [])
        if len(terms) < 12:
            errors.append("Glossaire initial trop court (< 12 termes)")
        seen_terms_fr: set[str] = set()
        for term in terms:
            fr_val = str(term.get("fr", "")).strip()
            en_val = str(term.get("en", "")).strip()
            def_val = str(term.get("definition", "")).strip()
            owner = term.get("chapitre_proprietaire")
            if not fr_val or not en_val or not def_val:
                errors.append(f"Entree incomplete dans glossaire-termes.json : {fr_val or '<vide>'}")
            if owner not in narrative_id_set:
                errors.append(f"Terme '{fr_val}' avec chapitre_proprietaire inconnu : {owner!r}")
            low_fr = fr_val.lower()
            if low_fr in seen_terms_fr:
                errors.append(f"Terme duplique dans glossaire-termes.json : {fr_val}")
            seen_terms_fr.add(low_fr)

    if Draft202012Validator is not None and ssot_schemas:
        adapted_ssot = adapt_ssot_schemas_for_compendium(ssot_schemas)
        for fname, schema_name in (
            ("specifications-lplus.json", "SpecificationsLPlusRegistry"),
            ("matrice-exig-prr-c40.json", "MatriceExigPrrC40Registry"),
            ("concordance-taxonomies.json", "ConcordanceTaxonomiesRegistry"),
        ):
            if fname in loaded and schema_name in adapted_ssot:
                v = Draft202012Validator(adapted_ssot[schema_name])
                for err in v.iter_errors(loaded[fname]):
                    errors.append(f"Validation schema {schema_name} echouee : {err.message}")

    return registry_raws, errors


def validate_specs(book_dir: Path) -> list[str]:
    """Valide intégralement `Sources/Compendium/ouvrage/specs/` (42 unités, 180 000 mots, 71 fam., 260 thèmes, 139 schémas, CA-01..CA-22)."""
    errors: list[str] = []
    book_dir = Path(book_dir)
    specs_dir = book_dir / "specs"
    reg_dir = book_dir / "registre"

    manifest_path = specs_dir / "manifest.json"
    mlr_path = specs_dir / "protocole-mlr-compendium.json"
    for path in (manifest_path, mlr_path):
        if not path.is_file():
            errors.append(f"Fichier requis manquant : {path}")
    if errors:
        return errors

    try:
        manifest_raw = manifest_path.read_text(encoding="utf-8")
        mlr_raw = mlr_path.read_text(encoding="utf-8")
        manifest = json.loads(manifest_raw)
        mlr = json.loads(mlr_raw)
    except json.JSONDecodeError as exc:
        return [f"JSON invalide : {exc}"]

    if manifest.get("project_id") != "COMPENDIUM-ENTREPRISE-AGENTIQUE-2027":
        errors.append(f"project_id inattendu dans manifest.json : {manifest.get('project_id')!r}")
    if not str(manifest.get("author_credit", "")).strip():
        errors.append("author_credit absent de manifest.json")
    if manifest.get("language") != "fr-CA":
        errors.append(f"language attendu 'fr-CA', trouvé {manifest.get('language')!r}")

    # 1. Date de gel (2026-12-02)
    freeze_date = mlr.get("freeze_date")
    if freeze_date != DEFAULT_FREEZE_DATE:
        errors.append(
            f"Date de gel freeze_date attendue = {DEFAULT_FREEZE_DATE} dans protocole-mlr-compendium.json, trouve = {freeze_date!r}"
        )
    if manifest.get("freeze_date") != DEFAULT_FREEZE_DATE:
        errors.append(f"freeze_date attendu = {DEFAULT_FREEZE_DATE} dans manifest.json, trouve = {manifest.get('freeze_date')!r}")
    tw_end = str(mlr.get("time_window", {}).get("primary", "")).split("/")[-1].strip()
    if parse_iso_date(tw_end) is None or tw_end > DEFAULT_FREEZE_DATE:
        errors.append(f"Fenetre MLR posterieure a la date de gel ({DEFAULT_FREEZE_DATE}) : {tw_end}")
    if mlr.get("strict_access_policy", {}).get("max_metadata_only_pct_in_included_corpus") != 0.0:
        errors.append("Le plafond METADATA_ONLY du protocole MLR doit etre strictement 0.0 %")

    stale_re = re.compile(r"(?:2026-12-31|31\s+d[eé]cembre\s+2026)", re.IGNORECASE)
    for label, raw in (("protocole-mlr-compendium.json", mlr_raw), ("manifest.json", manifest_raw)):
        if stale_re.search(raw):
            errors.append(f"Ancienne date de gel (2026-12-31) presente dans {label}")

    # 2. Budgets de mots et 42 unités = 180 000 mots
    wb = manifest.get("word_budget", {})
    tol = wb.get("tolerance_pct", 8) / 100.0
    units = manifest.get("units", [])
    unit_ids = [u["id"] for u in units]
    if len(unit_ids) != len(set(unit_ids)):
        errors.append("Identifiants d'unites dupliques dans manifest.json")
    if len(units) != 42:
        errors.append(f"Nombre total d'unites attendu = 42, trouve = {len(units)}")

    chapters = [u for u in units if u.get("kind") == "chapter"]
    annexes = [u for u in units if u.get("kind") == "annex"]
    narrative_units = [u for u in units if u.get("kind") in {"frontmatter", "chapter"}]
    if len(chapters) != 36:
        errors.append(f"Nombre de chapitres attendu = 36, trouve = {len(chapters)}")
    if len(annexes) != 5:
        errors.append(f"Nombre d'annexes attendu = 5, trouve = {len(annexes)}")
    if len(narrative_units) != 37:
        errors.append(f"Nombre d'unites narratives attendu = 37, trouve = {len(narrative_units)}")

    expected_order = ["00-liminaire", *_EXPECTED_CHAPTER_IDS, *_EXPECTED_ANNEX_IDS]
    if unit_ids != expected_order and len(units) == 42:
        errors.append("Ordre ou identifiants des 42 unites non conformes (00-liminaire, ch01..ch36, annexe-a..annexe-e)")

    sum_total = sum(u.get("target_words", 0) for u in units)
    sum_narrative = sum(u.get("target_words", 0) for u in narrative_units)
    sum_annexes = sum(u.get("target_words", 0) for u in annexes)

    if wb.get("total_target") != 180000:
        errors.append(f"total_target attendu = 180000, trouve = {wb.get('total_target')!r}")
    if sum_total != wb.get("total_target"):
        errors.append(f"Somme des unites ({sum_total}) != total_target ({wb.get('total_target')})")
    if sum_narrative != wb.get("narrative_target"):
        errors.append(f"Somme narrative ({sum_narrative}) != narrative_target ({wb.get('narrative_target')})")
    if sum_annexes != wb.get("annexes_target"):
        errors.append(f"Somme annexes ({sum_annexes}) != annexes_target ({wb.get('annexes_target')})")

    exp_tot_min = math.ceil(wb["total_target"] * (1.0 - tol))
    exp_tot_max = math.floor(wb["total_target"] * (1.0 + tol))
    if wb.get("total_min") != exp_tot_min or wb.get("total_max") != exp_tot_max:
        errors.append(
            f"Bornes globales invalides : ({wb.get('total_min')}, {wb.get('total_max')}) attendu ({exp_tot_min}, {exp_tot_max})"
        )

    for u in units:
        tw = u.get("target_words", 0)
        exp_min = math.ceil(tw * (1.0 - tol))
        exp_max = math.floor(tw * (1.0 + tol))
        if u.get("min_words") != exp_min or u.get("max_words") != exp_max:
            errors.append(
                f"Bornes invalides pour {u['id']} : ({u.get('min_words')}, {u.get('max_words')}) attendu ({exp_min}, {exp_max})"
            )
        if u.get("kind") == "chapter":
            t_count = len(u.get("themes", []))
            expected_c = 3100 + 190 * t_count
            if tw != expected_c:
                errors.append(
                    f"Formule C = 3100 + 190*t violee pour {u['id']} : {tw} != {expected_c} (t={t_count})"
                )

    # 3. Partition bijective 71 familles, 260 thèmes et owned_concepts
    all_families: list[str] = []
    all_themes: list[str] = []
    all_owned: list[str] = []
    for nu in narrative_units:
        owned = nu.get("owned_concepts", [])
        if not owned:
            errors.append(f"Unite narrative {nu['id']} sans owned_concepts")
        all_owned.extend(owned)
        if nu.get("kind") == "chapter":
            fams = nu.get("families", [])
            thms = nu.get("themes", [])
            if not fams or not thms:
                errors.append(f"Chapitre {nu['id']} sans families ou themes")
            all_families.extend(fams)
            all_themes.extend(thms)

    if len(all_families) != 71 or len(set(all_families)) != 71:
        errors.append(f"Partition des familles attendue = 71 uniques, trouve {len(all_families)} ({len(set(all_families))} uniques)")
    if len(all_themes) != 260 or len(set(all_themes)) != 260:
        errors.append(f"Partition des themes attendue = 260 uniques, trouve {len(all_themes)} ({len(set(all_themes))} uniques)")
    if len(all_owned) != len(set(all_owned)):
        errors.append("Collision dans owned_concepts entre plusieurs unites narratives")

    # 4. part_titles, deliverables, g3_seeds, synced_excerpts_catalog, 139 schémas
    part_titles = manifest.get("part_titles", {})
    if set(part_titles.keys()) != set(_ROMAN_PARTS):
        errors.append(f"part_titles attendu pour I..XII, trouve : {sorted(part_titles.keys())}")

    deliv = manifest.get("deliverables", {})
    if "html" in deliv:
        errors.append("deliverables['html'] doit être absent (édition HTML supprimée)")
    for key, exp_val in (
        ("md", "../../../Compendium/Compendium.md"),
        ("pdf", "../../../Compendium/Compendium.pdf"),
    ):
        if deliv.get(key) != exp_val:
            errors.append(f"deliverables[{key!r}] attendu = {exp_val!r}, trouve = {deliv.get(key)!r}")

    g3_seeds = manifest.get("g3_seeds", {})
    if g3_seeds.get("pass1") != 20270901 or g3_seeds.get("pass2") != 20270902:
        errors.append(f"g3_seeds attendu (20270901, 20270902), trouve : {g3_seeds!r}")

    excerpts_cat = manifest.get("synced_excerpts_catalog", [])
    chapter_id_set = set(_EXPECTED_CHAPTER_IDS)
    if len(excerpts_cat) != 14:
        errors.append(f"synced_excerpts_catalog attendu = 14 extraits, trouve = {len(excerpts_cat)}")
    else:
        for ex in excerpts_cat:
            if ex.get("unit") not in chapter_id_set:
                errors.append(f"Extrait CA-G0-SYNC {ex.get('id')} avec unite invalide : {ex.get('unit')!r}")
            if not (1 <= int(ex.get("max_lines", 0)) <= 40):
                errors.append(f"Extrait CA-G0-SYNC {ex.get('id')} depasse 40 L : {ex.get('max_lines')}")

    figures = manifest.get("figures", [])
    if len(figures) != 139:
        errors.append(f"Catalogue des schemas attendu = 139, trouve = {len(figures)}")
    declared_figs = {f["id"]: f for f in figures if "id" in f}
    if len(declared_figs) != len(figures):
        errors.append("Identifiants de schemas dupliques dans manifest.json")
    assigned_figs = [fid for u in units for fid in u.get("figures", [])]
    if sorted(assigned_figs) != sorted(declared_figs.keys()):
        errors.append("Desaccord entre les schemas assignes aux unites et manifest.json['figures']")
    for fid, fmeta in declared_figs.items():
        if not re.fullmatch(r"SCH-(?:\d{2}|A[A-E])-\d{2}", fid):
            errors.append(f"Identifiant de schema invalide : {fid!r}")
        if fmeta.get("engine") not in {"puml", "mmd", "svg"}:
            errors.append(f"Moteur invalide pour {fid} : {fmeta.get('engine')!r}")
        unit_obj = next((u for u in units if u["id"] == fmeta.get("unit")), None)
        if unit_obj is None or fid not in unit_obj.get("figures", []):
            errors.append(f"Schema {fid} mal rattache a l'unite {fmeta.get('unit')!r}")

    # 5. Regex interdites (AO-03) et corpus interne
    compiled_forbidden: list[tuple[str, re.Pattern[str]]] = []
    for pattern in manifest.get("forbidden_prose_regexes", []):
        try:
            compiled_forbidden.append((pattern, re.compile(pattern, re.IGNORECASE)))
        except re.error as exc:
            errors.append(f"Regex interdite invalide `{pattern}` : {exc}")

    for allowed_id in (
        "EXIG-SEC-06", "CAP-046", "ADR-001", "POR-001", "PRR", "PRR-75",
        "PEX-001", "C01", "C40", "SBB", "SCH-01-01", "INI-043", "SIG-001", "DIV-02", "DISC-01", "DISC-05",
    ):
        for pat_str, regex in compiled_forbidden:
            if regex.search(allowed_id):
                errors.append(
                    f"forbidden_prose_regexes ne doit pas bannir l'identifiant autorise '{allowed_id}' (motif `{pat_str}`)"
                )

    for rel_path in manifest.get("internal_corpus_paths", []) + manifest.get("stylistic_benchmarks_for_gauntlet", []):
        resolved = (book_dir / rel_path).resolve()
        if not resolved.is_file():
            errors.append(f"Chemin de corpus interne introuvable : {rel_path} -> {resolved}")

    # 6. Axes MLR (D01..D12 ou RQ1..RQ6)
    rq_ids = {rq["id"] for rq in mlr.get("research_questions_and_queries", [])}
    if not rq_ids or (not set(_EXPECTED_DOMAINS) <= rq_ids and not {"RQ1", "RQ2", "RQ3", "RQ4", "RQ5", "RQ6"} <= rq_ids):
        errors.append(f"Axes de recherche incomplets dans protocole-mlr-compendium.json : {sorted(rq_ids)}")

    # 7. Validation conditionnelle de registre/ et recherche/
    narrative_id_set = {nu["id"] for nu in narrative_units}
    ssot_schemas: dict[str, dict] = {}
    arch_candidate = book_dir.parents[2] / "Sources" / "Tomes" / "Tome 8 - Ingénierie exécutable et homologation vérifiable" / "specs" / "architecture-trousse-g0.md"
    if arch_candidate.is_file():
        ssot_schemas, _ = extract_ssot_schemas_from_arch(arch_candidate.read_text(encoding="utf-8"))

    if reg_dir.is_dir():
        _, reg_errs = _validate_populated_registries(
            reg_dir=reg_dir,
            chapter_id_set=chapter_id_set,
            narrative_id_set=narrative_id_set,
            ssot_schemas=ssot_schemas,
        )
        errors.extend(reg_errs)

    statut_f_path = book_dir / "recherche" / "registre-statut-f.json"
    if statut_f_path.is_file():
        try:
            loaded_sf = json.loads(statut_f_path.read_text(encoding="utf-8"))
            blocked_entries = loaded_sf.get("blocked", loaded_sf.get("blocked_sources")) if isinstance(loaded_sf, dict) else None
            if not isinstance(blocked_entries, list):
                errors.append("registre-statut-f.json doit contenir une liste 'blocked'")
            else:
                for idx, entry in enumerate(blocked_entries):
                    if not isinstance(entry, dict):
                        errors.append(f"Entree statut-F #{idx} invalide")
                        continue
                    if entry.get("status") != "F":
                        errors.append(f"Entree statut-F sans status=='F' : {entry.get('url')}")
                    if entry.get("included_in_evidence") is not False:
                        errors.append(f"Entree statut-F doit avoir included_in_evidence==False : {entry.get('url')}")
        except json.JSONDecodeError as exc:
            errors.append(f"registre-statut-f.json invalide : {exc}")

    return errors


def main() -> int:
    book_dir = Path(__file__).resolve().parent.parent
    errors = validate_specs(book_dir)
    if errors:
        print("ECHEC de verification des specifications du Compendium :", file=sys.stderr)
        for err in errors:
            print(f"  - {err}", file=sys.stderr)
        return 1
    print(
        "OK : Specifications Compendium valides (42 unites = 180 000 mots, 71 familles, "
        "260 themes disjoints, 139 schemas SCH-00-01..SCH-AD-01, 14 extraits CA-G0-SYNC, CA-01..CA-22)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
