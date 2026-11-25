#!/usr/bin/env python3
"""Consolide et valide les 7 shards de schémas de vulgarisation du PRD maître.

Charge ``Cartographie/donnees/prd_schemas_shards/schemas-*.json``, valide chaque
shard contre ``schema-prd-vulgarisation.json``, vérifie la couverture intégrale des
36 chapitres, 71 familles et des figures liées de ``inventaire-319-diagrammes.json``,
puis génère ``Cartographie/donnees/catalogue-schemas-prd.json`` en LF strict.
"""

from __future__ import annotations

import argparse
from collections import Counter
import datetime as dt
import json
from pathlib import Path
import re
import sys
from typing import Any

import jsonschema

TOOLS_DIR = Path(__file__).resolve().parent
if str(TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(TOOLS_DIR))

import compiler_prd as cp  # noqa: E402

SCHEMA_SHARD_FILENAMES: tuple[str, ...] = (
    "schemas-global-et-annexe-e.json",
    "schemas-d01-d02.json",
    "schemas-d03-d04.json",
    "schemas-d05-d06.json",
    "schemas-d07-d08.json",
    "schemas-d09-d10.json",
    "schemas-d11-d12.json",
)

PLACEHOLDER_PATTERNS: tuple[re.Pattern[str], ...] = (
    re.compile(r"\bTODO\b", re.IGNORECASE),
    re.compile(r"\bTBD\b", re.IGNORECASE),
    re.compile(r"\blorem ipsum\b", re.IGNORECASE),
    re.compile(r"\bplaceholder\b", re.IGNORECASE),
    re.compile(r"\bà compléter\b", re.IGNORECASE),
)

TOME_IDS: tuple[str, ...] = ("T1", "T2", "T3", "T4", "T5", "T6", "T7", "T8")


def _check_string_hygiene(obj: Any, source_label: str, path: str = "") -> None:
    """Vérifie l'absence de `\\$`, flèches ASCII hors backticks, clés backtickées et placeholders."""
    if isinstance(obj, dict):
        for k, v in obj.items():
            if "`" in k:
                raise ValueError(f"{source_label}: clé JSON avec backtick à {path}.{k}")
            _check_string_hygiene(v, source_label, f"{path}.{k}")
    elif isinstance(obj, list):
        for idx, item in enumerate(obj):
            _check_string_hygiene(item, source_label, f"{path}[{idx}]")
    elif isinstance(obj, str):
        if r"\$" in obj:
            raise ValueError(f"{source_label}: séquence littérale \\$ à {path} : {obj[:120]}")
        parts = re.split(r"`[^`]*`", obj)
        for idx, part in enumerate(parts):
            if idx % 2 == 0 and ("->" in part or "<->" in part):
                raise ValueError(f"{source_label}: flèche ASCII hors backticks à {path} : {part[:120]}")
        for pat in PLACEHOLDER_PATTERNS:
            if pat.search(obj):
                raise ValueError(f"{source_label}: placeholder détecté ({pat.pattern}) à {path}")


def build_catalogue_schemas_payload(
    repo_root: Path,
    bundle: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Consolide et valide les 7 shards de schémas de vulgarisation en un catalogue unique."""
    donnees_dir = repo_root / "Sources" / "Cartographie" / "donnees"
    shards_dir = donnees_dir / "prd_schemas_shards"
    schema_path = donnees_dir / "schema-prd-vulgarisation.json"
    inv_path = donnees_dir / "inventaire-319-diagrammes.json"

    if bundle is None:
        bundle_path = donnees_dir / "corpus-mindmap-data.json"
        bundle = json.loads(bundle_path.read_text(encoding="utf-8"))

    schema_vulg = json.loads(schema_path.read_text(encoding="utf-8"))
    jsonschema.Draft202012Validator.check_schema(schema_vulg)
    validator = jsonschema.Draft202012Validator(schema_vulg)

    inv_data = json.loads(inv_path.read_text(encoding="utf-8"))
    inv_figures: list[dict[str, Any]] = inv_data["figures"]
    if len(inv_figures) != 319:
        raise ValueError(f"Inventaire attendu à 319 figures, obtenu {len(inv_figures)}")
    inv_by_uid: dict[str, dict[str, Any]] = {f["diagram_uid"]: f for f in inv_figures}

    nodes = bundle["nodes"]
    subs_by_id = {n["node_id"]: n for n in nodes if n["node_kind"] == "subdomain"}
    fams_by_id = {n["node_id"]: n for n in nodes if n["node_kind"] == "family"}
    themes_by_slug = {n["canonical_slug"]: n for n in nodes if n["node_kind"] == "theme"}

    expected_fams_by_chapter: dict[int, set[str]] = {}
    sub_by_chapter: dict[int, dict[str, Any]] = {}
    for sub_id, sub_node in subs_by_id.items():
        cnum = cp.expected_chapter_number(sub_node["domain_id"], sub_id)
        expected_fams_by_chapter[cnum] = set(sub_node.get("children_ids") or [])
        sub_by_chapter[cnum] = sub_node

    all_global_schemas: list[dict[str, Any]] = []
    all_chapter_schemas: list[dict[str, Any]] = []
    annexe_e_block: dict[str, Any] = {}
    seen_schema_ids: set[str] = set()
    fams_covered_by_chapter: dict[int, set[str]] = {}
    all_covered_slugs: set[str] = set()
    linked_schemas_by_uid: dict[str, list[str]] = {}

    for fn in SCHEMA_SHARD_FILENAMES:
        sp = shards_dir / fn
        if not sp.is_file():
            raise FileNotFoundError(f"Shard de schémas manquant : {sp}")
        raw_bytes = sp.read_bytes()
        if bytes([13, 10]) in raw_bytes:
            raise ValueError(f"Fins de ligne CRLF détectées dans {sp}")
        raw_text = raw_bytes.decode("utf-8")
        if r"\$" in raw_text:
            raise ValueError(f"Séquence littérale \\$ détectée dans {sp}")
        shard_obj = json.loads(raw_text)
        _check_string_hygiene(shard_obj, fn)
        validator.validate(shard_obj)

        is_global = fn == "schemas-global-et-annexe-e.json"
        if is_global:
            annexe_e_block = shard_obj["annexe_e"]
            expected_domains_in_shard = {"GLOBAL"}
            expected_chapters_in_shard = {0}
        else:
            expected_domains_in_shard = set(shard_obj["domains_covered"])
            expected_chapters_in_shard = {int(c) for c in shard_obj["chapters_covered"]}

        seen_chapters_in_shard: set[int] = set()
        for item in shard_obj["schemas"]:
            sid = item["schema_id"]
            if sid in seen_schema_ids:
                raise ValueError(f"Identifiant schema_id dupliqué : {sid}")
            seen_schema_ids.add(sid)

            cnum = int(item["chapter_number"])
            dom_id = item["domain_id"]
            sub_id = item["subdomain_node_id"]
            if dom_id not in expected_domains_in_shard:
                raise ValueError(f"{fn}/{sid}: domain_id {dom_id} hors périmètre {expected_domains_in_shard}")
            if cnum not in expected_chapters_in_shard:
                raise ValueError(f"{fn}/{sid}: chapter_number {cnum} hors périmètre {expected_chapters_in_shard}")
            seen_chapters_in_shard.add(cnum)

            if cnum == 0:
                if not is_global or dom_id != "GLOBAL" or sub_id != "ROOT" or item["families_covered"] != []:
                    raise ValueError(f"{fn}/{sid}: métadonnées globales invalides")
                all_global_schemas.append(item)
            else:
                exp_num = cp.expected_chapter_number(dom_id, sub_id)
                if exp_num != cnum:
                    raise ValueError(f"{fn}/{sid}: incohérence {dom_id}/{sub_id} -> {exp_num} != {cnum}")
                fams = item["families_covered"]
                if not fams:
                    raise ValueError(f"{fn}/{sid}: families_covered vide pour chapitre {cnum}")
                for fid in fams:
                    if fid not in fams_by_id:
                        raise ValueError(f"{fn}/{sid}: famille inconnue {fid}")
                    if fid not in expected_fams_by_chapter[cnum]:
                        raise ValueError(f"{fn}/{sid}: famille {fid} n'appartient pas au chapitre {cnum}")
                fams_covered_by_chapter.setdefault(cnum, set()).update(fams)
                all_chapter_schemas.append(item)

            for slug in item["themes_vulgarized"]:
                if slug not in themes_by_slug:
                    raise ValueError(f"{fn}/{sid}: canonical_slug inconnu {slug}")
                all_covered_slugs.add(slug)

            for lf in item["linked_tome_figures"]:
                uid = f"{lf['tome_id']}:{lf['fig_id']}"
                if uid not in inv_by_uid:
                    raise ValueError(f"{fn}/{sid}: figure Tome introuvable dans l'inventaire : {uid}")
                inv_f = inv_by_uid[uid]
                for field in ("title", "source_path", "rendered_path"):
                    if lf[field] != inv_f[field]:
                        raise ValueError(
                            f"{fn}/{sid}: divergence sur {uid}.{field} : {lf[field]!r} != {inv_f[field]!r}"
                        )
                src_p = repo_root / lf["source_path"]
                ren_p = repo_root / lf["rendered_path"]
                if not src_p.is_file():
                    raise FileNotFoundError(f"{fn}/{sid}: source_path manquant sur disque : {src_p}")
                if not ren_p.is_file():
                    raise FileNotFoundError(f"{fn}/{sid}: rendered_path manquant sur disque : {ren_p}")
                linked_schemas_by_uid.setdefault(uid, []).append(sid)

        if seen_chapters_in_shard != expected_chapters_in_shard:
            raise ValueError(
                f"{fn}: chapitres incomplets : {sorted(seen_chapters_in_shard)} != {sorted(expected_chapters_in_shard)}"
            )

    if len(all_global_schemas) != 4:
        raise ValueError(f"Attendu 4 schémas globaux SCH-00-*, obtenu {len(all_global_schemas)}")
    if set(fams_covered_by_chapter.keys()) != set(range(1, 37)):
        missing_chs = sorted(set(range(1, 37)) - set(fams_covered_by_chapter.keys()))
        raise ValueError(f"Chapitres non couverts : {missing_chs}")

    total_covered_fams: set[str] = set()
    for cnum in range(1, 37):
        exp_fams = expected_fams_by_chapter[cnum]
        got_fams = fams_covered_by_chapter.get(cnum, set())
        if got_fams != exp_fams:
            raise ValueError(
                f"Chapitre {cnum:02d}: couverture FAM_* incomplète : manquantes={sorted(exp_fams - got_fams)}"
            )
        total_covered_fams.update(got_fams)

    if len(total_covered_fams) != 71:
        raise ValueError(f"Couverture totale FAM_* = {len(total_covered_fams)} != 71")

    all_global_schemas.sort(key=lambda s: s["schema_id"])
    all_chapter_schemas.sort(key=lambda s: (int(s["chapter_number"]), s["schema_id"]))
    all_schemas = all_global_schemas + all_chapter_schemas

    # Statistiques synthétiques
    reuse_order = schema_vulg["enums"]["reuse_status"]
    archetype_order = schema_vulg["enums"]["visual_archetype"]
    notation_order = schema_vulg["enums"]["recommended_notation"]
    audience_order = schema_vulg["enums"]["target_audiences"]

    reuse_counts = Counter(s["reuse_status"] for s in all_schemas)
    archetype_counts = Counter(s["visual_archetype"] for s in all_schemas)
    notation_counts = Counter(s["recommended_notation"] for s in all_schemas)
    audience_counts = Counter(aud for s in all_schemas for aud in s["target_audiences"])

    by_domain: dict[str, dict[str, Any]] = {}
    for dom_key in ["GLOBAL"] + [f"D{i:02d}" for i in range(1, 13)]:
        d_schemas = [s for s in all_schemas if s["domain_id"] == dom_key]
        d_fams = sorted({fid for s in d_schemas for fid in s["families_covered"]})
        d_chs = sorted({int(s["chapter_number"]) for s in d_schemas})
        by_domain[dom_key] = {
            "schemas_count": len(d_schemas),
            "chapters": d_chs,
            "families_covered_count": len(d_fams),
            "schema_ids": [s["schema_id"] for s in d_schemas],
        }

    by_chapter: list[dict[str, Any]] = []
    for cnum in range(0, 37):
        c_schemas = [s for s in all_schemas if int(s["chapter_number"]) == cnum]
        if cnum == 0:
            by_chapter.append(
                {
                    "chapter_number": 0,
                    "chapter_code": "GLOBAL",
                    "domain_id": "GLOBAL",
                    "subdomain_node_id": "ROOT",
                    "schemas_count": len(c_schemas),
                    "schema_ids": [s["schema_id"] for s in c_schemas],
                    "families_covered_count": 0,
                }
            )
        else:
            sub_node = sub_by_chapter[cnum]
            c_fams = sorted({fid for s in c_schemas for fid in s["families_covered"]})
            by_chapter.append(
                {
                    "chapter_number": cnum,
                    "chapter_code": f"CH-{cnum:02d}",
                    "domain_id": sub_node["domain_id"],
                    "subdomain_node_id": sub_node["node_id"],
                    "schemas_count": len(c_schemas),
                    "schema_ids": [s["schema_id"] for s in c_schemas],
                    "families_covered_count": len(c_fams),
                }
            )

    summary_stats = {
        "total_schemas": len(all_schemas),
        "global_schemas_count": len(all_global_schemas),
        "chapter_schemas_count": len(all_chapter_schemas),
        "chapters_covered_count": len(fams_covered_by_chapter),
        "families_covered_count": len(total_covered_fams),
        "families_total_count": len(fams_by_id),
        "unique_themes_vulgarized_count": len(all_covered_slugs),
        "total_themes_count": len(themes_by_slug),
        "by_reuse_status": {k: reuse_counts.get(k, 0) for k in reuse_order},
        "by_visual_archetype": {k: archetype_counts.get(k, 0) for k in archetype_order},
        "by_recommended_notation": {k: notation_counts.get(k, 0) for k in notation_order},
        "by_target_audience": {k: audience_counts.get(k, 0) for k in audience_order},
        "by_domain": by_domain,
        "by_chapter": by_chapter,
    }

    # Couverture complète sur les 319 figures des Tomes 1–8 (sans troncature)
    by_tome_cov: dict[str, dict[str, Any]] = {}
    figures_catalogue: list[dict[str, Any]] = []
    for f in inv_figures:
        uid = f["diagram_uid"]
        sids = sorted(set(linked_schemas_by_uid.get(uid, [])))
        figures_catalogue.append(
            {
                "diagram_uid": uid,
                "tome_id": f["tome_id"],
                "fig_id": f["fig_id"],
                "title": f["title"],
                "notation": f["notation"],
                "source_path": f["source_path"],
                "rendered_path": f["rendered_path"],
                "source_section": f["source_section"],
                "domain_hints": f["domain_hints"],
                "linked_schema_ids": sids,
                "linked_count": len(linked_schemas_by_uid.get(uid, [])),
            }
        )

    for tid in TOME_IDS:
        t_figs = [f for f in inv_figures if f["tome_id"] == tid]
        t_linked = [f for f in t_figs if f["diagram_uid"] in linked_schemas_by_uid]
        t_unlinked = [f for f in t_figs if f["diagram_uid"] not in linked_schemas_by_uid]
        inv_puml = sum(1 for f in t_figs if f["notation"] == "PlantUML")
        inv_mmd = sum(1 for f in t_figs if f["notation"] == "Mermaid")
        lnk_puml = sum(1 for f in t_linked if f["notation"] == "PlantUML")
        lnk_mmd = sum(1 for f in t_linked if f["notation"] == "Mermaid")
        total_refs = sum(len(linked_schemas_by_uid.get(f["diagram_uid"], [])) for f in t_figs)
        by_tome_cov[tid] = {
            "inventory_total": len(t_figs),
            "inventory_plantuml": inv_puml,
            "inventory_mermaid": inv_mmd,
            "unique_linked_count": len(t_linked),
            "unique_linked_plantuml": lnk_puml,
            "unique_linked_mermaid": lnk_mmd,
            "unlinked_count": len(t_unlinked),
            "total_links_count": total_refs,
            "coverage_percent": round((len(t_linked) / len(t_figs)) * 100, 2) if t_figs else 0.0,
            "linked_fig_ids": [f["fig_id"] for f in t_linked],
            "unlinked_fig_ids": [f["fig_id"] for f in t_unlinked],
        }

    unique_linked_uids = set(linked_schemas_by_uid.keys())
    linked_puml_total = sum(
        1 for f in inv_figures if f["diagram_uid"] in unique_linked_uids and f["notation"] == "PlantUML"
    )
    linked_mmd_total = sum(
        1 for f in inv_figures if f["diagram_uid"] in unique_linked_uids and f["notation"] == "Mermaid"
    )
    inv_puml_total = sum(1 for f in inv_figures if f["notation"] == "PlantUML")
    inv_mmd_total = sum(1 for f in inv_figures if f["notation"] == "Mermaid")

    tome_figures_coverage = {
        "total_inventory_figures": len(inv_figures),
        "inventory_plantuml_svg": inv_puml_total,
        "inventory_mermaid_png": inv_mmd_total,
        "unique_linked_figures_count": len(unique_linked_uids),
        "unlinked_figures_count": len(inv_figures) - len(unique_linked_uids),
        "total_figure_links_count": sum(len(v) for v in linked_schemas_by_uid.values()),
        "coverage_percent": round((len(unique_linked_uids) / len(inv_figures)) * 100, 2),
        "by_notation": {
            "PlantUML": {
                "inventory_total": inv_puml_total,
                "unique_linked_count": linked_puml_total,
                "unlinked_count": inv_puml_total - linked_puml_total,
                "coverage_percent": round((linked_puml_total / inv_puml_total) * 100, 2),
            },
            "Mermaid": {
                "inventory_total": inv_mmd_total,
                "unique_linked_count": linked_mmd_total,
                "unlinked_count": inv_mmd_total - linked_mmd_total,
                "coverage_percent": round((linked_mmd_total / inv_mmd_total) * 100, 2),
            },
        },
        "by_tome": by_tome_cov,
        "figures_catalogue": figures_catalogue,
    }

    payload = {
        "schema_version": "1.0.0",
        "lang": "fr-CA",
        "generated_at": dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "generator": "Sources/Cartographie/outils/consolider_catalogue_schemas.py",
        "source_shards": [f"Sources/Cartographie/donnees/prd_schemas_shards/{fn}" for fn in SCHEMA_SHARD_FILENAMES],
        "source_inventory": "Sources/Cartographie/donnees/inventaire-319-diagrammes.json",
        "global_schemas": all_global_schemas,
        "chapter_schemas": all_chapter_schemas,
        "annexe_e": annexe_e_block,
        "summary_stats": summary_stats,
        "tome_figures_coverage": tome_figures_coverage,
    }
    _check_string_hygiene(payload, "catalogue-schemas-prd.json")
    return payload


def main() -> int:
    """Point d'entrée CLI générant ``Cartographie/donnees/catalogue-schemas-prd.json``."""
    parser = argparse.ArgumentParser(description="Consolide les 7 shards de schémas de vulgarisation du PRD.")
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
        help="Chemin de sortie JSON (défaut : Sources/Cartographie/donnees/catalogue-schemas-prd.json).",
    )
    args = parser.parse_args()

    repo_root = args.repo_root.resolve()
    payload = build_catalogue_schemas_payload(repo_root)
    out_path = args.output or (repo_root / "Sources" / "Cartographie" / "donnees" / "catalogue-schemas-prd.json")
    serialized = json.dumps(payload, indent=2, ensure_ascii=False) + "\n"
    if r"\$" in serialized:
        raise ValueError(f"Séquence littérale \\$ dans le JSON sérialisé : {out_path}")
    with out_path.open("w", encoding="utf-8", newline="\n") as fh:
        fh.write(serialized)
    raw_bytes = out_path.read_bytes()
    assert bytes([13, 10]) not in raw_bytes, f"CRLF détecté dans {out_path}"

    st = payload["summary_stats"]
    tc = payload["tome_figures_coverage"]
    print(
        f"Catalogue consolidé -> {out_path} : {st['total_schemas']} schémas "
        f"({st['global_schemas_count']} SCH-00 + {st['chapter_schemas_count']} SCH-01..36), "
        f"{st['chapters_covered_count']}/36 chapitres, {st['families_covered_count']}/71 familles, "
        f"{tc['unique_linked_figures_count']}/{tc['total_inventory_figures']} figures uniques des Tomes "
        f"({tc['total_figure_links_count']} liens, {tc['coverage_percent']} %)."
    )
    print(f"  reuse_status: {st['by_reuse_status']}")
    print(f"  recommended_notation: {st['by_recommended_notation']}")
    for tid, tinfo in tc["by_tome"].items():
        print(
            f"  {tid}: {tinfo['unique_linked_count']}/{tinfo['inventory_total']} figures uniques "
            f"({tinfo['unique_linked_plantuml']}/{tinfo['inventory_plantuml']} PlantUML, "
            f"{tinfo['unique_linked_mermaid']}/{tinfo['inventory_mermaid']} Mermaid, "
            f"{tinfo['total_links_count']} références)"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
