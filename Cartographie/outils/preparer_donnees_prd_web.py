#!/usr/bin/env python3
"""Extracteur et préparateur des données web unifiées du PRD maître.

Produit ``Cartographie/donnees/prd-web-data.json`` à partir :
- des 7 shards dans ``Cartographie/donnees/prd_shards/``
- du bundle ``Cartographie/donnees/corpus-mindmap-data.json`` (ou d'un ``bundle`` en mémoire)
- des matrices brutes de ``Cartographie/donnees/pivots-concordance.json``
- des statistiques réelles de ``prd.md`` (si présent sur disque)

Expose ``build_prd_web_payload(repo_root: Path, bundle: dict | None = None) -> dict``
réutilisable par ``compiler_mindmap.py`` et ``compiler_prd_web.py``.
"""

from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path
import re
import sys
from typing import Any

TOOLS_DIR = Path(__file__).resolve().parent
if str(TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(TOOLS_DIR))

import compiler_prd as cp  # noqa: E402
import extraire_structure as es  # noqa: E402


def _parse_markdown_section_body(body_md: str) -> tuple[list[str], dict[str, Any] | None]:
    """Sépare les paragraphes de texte et l'éventuelle table GFM d'une sous-section."""
    lines = body_md.splitlines()
    paragraphs: list[str] = []
    cur_para: list[str] = []
    table_lines: list[str] = []
    in_table = False

    def flush_para() -> None:
        if cur_para:
            paragraphs.append(" ".join(x.strip() for x in cur_para if x.strip()))
            cur_para.clear()

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("|") and stripped.endswith("|"):
            flush_para()
            in_table = True
            table_lines.append(stripped)
            continue
        if in_table and stripped == "":
            in_table = False
            continue
        if stripped == "":
            flush_para()
        else:
            cur_para.append(stripped)
    flush_para()

    kpi_table: dict[str, Any] | None = None
    if len(table_lines) >= 3:
        split_row = lambda r: [c.strip() for c in r.strip("|").split("|")]
        headers = split_row(table_lines[0])
        rows = [
            split_row(r)
            for r in table_lines[2:]
            if not re.fullmatch(r"[\s|:-]+", r)
        ]
        kpi_table = {"headers": headers, "rows": rows}

    return paragraphs, kpi_table


def _load_and_validate_shards(
    repo_root: Path,
    bundle: dict[str, Any],
) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    """Charge et valide les 7 shards PRD face aux nœuds du ``bundle`` fourni."""
    shards_dir = repo_root / "Cartographie" / "donnees" / "prd_shards"
    missing = [fn for fn in cp.SHARD_FILENAMES if not (shards_dir / fn).is_file()]
    if missing:
        raise FileNotFoundError(f"Shards PRD manquants dans {shards_dir} : {missing}")

    global_shard = json.loads((shards_dir / "prd-global-et-annexes.json").read_text(encoding="utf-8"))
    domain_shards = [
        json.loads((shards_dir / fn).read_text(encoding="utf-8"))
        for fn in cp.SHARD_FILENAMES[1:]
    ]

    cp._assert_non_empty(global_shard.get("prd_title"), "prd_title")
    cp._assert_non_empty(global_shard.get("prd_subtitle"), "prd_subtitle")
    cp._assert_non_empty(global_shard.get("toc_representative_title"), "toc_representative_title")

    nodes = bundle["nodes"]
    expected_subs = {n["node_id"]: n for n in nodes if n["node_kind"] == "subdomain"}
    expected_fams = {n["node_id"]: n for n in nodes if n["node_kind"] == "family"}
    expected_themes = {n["node_id"]: n for n in nodes if n["node_kind"] == "theme"}

    all_chapters: list[dict[str, Any]] = []
    seen_ch_nums: set[int] = set()
    seen_subs: set[str] = set()
    seen_fams: set[str] = set()
    seen_themes: set[str] = set()

    for shard in domain_shards:
        for ch in shard.get("chapters", []):
            ch_num = int(ch["chapter_number"])
            dom_id = ch["domain_id"]
            sub_id = ch["subdomain_node_id"]
            if sub_id not in expected_subs:
                raise ValueError(f"Sous-domaine inconnu : {sub_id}")
            exp_num = cp.expected_chapter_number(dom_id, sub_id)
            if ch_num != exp_num:
                raise ValueError(f"Numéro de chapitre incohérent pour {sub_id}: {ch_num} != {exp_num}")
            seen_ch_nums.add(ch_num)
            seen_subs.add(sub_id)

            tc = ch.get("targeted_content") or {}
            for fam in tc.get("families_and_themes", []):
                fid = fam["family_node_id"]
                if fid not in expected_fams:
                    raise ValueError(f"Famille inconnue : {fid}")
                seen_fams.add(fid)
                for th in fam.get("themes_targeted", []):
                    tid = th["theme_node_id"]
                    if tid not in expected_themes:
                        raise ValueError(f"Thème inconnu : {tid}")
                    if expected_themes[tid]["canonical_slug"] != th["canonical_slug"]:
                        raise ValueError(f"Slug discordant pour {tid}")
                    seen_themes.add(tid)
            all_chapters.append(ch)

    if seen_ch_nums != set(range(1, 37)):
        raise ValueError(f"Chapitres manquants : {sorted(set(range(1, 37)) - seen_ch_nums)}")
    if seen_subs != set(expected_subs):
        raise ValueError(f"Sous-domaines manquants : {sorted(set(expected_subs) - seen_subs)}")
    if seen_fams != set(expected_fams):
        raise ValueError(f"Familles manquantes : {sorted(set(expected_fams) - seen_fams)}")
    if seen_themes != set(expected_themes):
        raise ValueError(f"Thèmes manquants : {sorted(set(expected_themes) - seen_themes)}")

    all_chapters.sort(key=lambda c: int(c["chapter_number"]))
    return global_shard, all_chapters


def _compute_gfm_anchors(
    global_shard: dict[str, Any],
    chapters_by_num: dict[int, dict[str, Any]],
) -> dict[str, Any]:
    """Calcule les ancres GFM exactes dans l'ordre exact d'apparition dans ``prd.md``."""
    seen: dict[str, int] = {}
    cp.gfm_anchor(global_shard["prd_title"].strip(), seen)
    cp.gfm_anchor(global_shard["toc_representative_title"].strip(), seen)

    exec_sum = global_shard["executive_summary"]
    exec_anchor = cp.gfm_anchor(exec_sum.get("title", "Sommaire exécutif global").strip(), seen)
    exec_section_anchors: list[str] = [
        cp.gfm_anchor(sec["heading"].strip(), seen)
        for sec in exec_sum["sections"]
    ]

    part_anchors: dict[str, str] = {}
    chapter_anchors: dict[int, str] = {}
    family_anchors: dict[str, str] = {}

    for p in global_shard["parties"]:
        dom_id = p["domain_id"]
        roman = p.get("part_roman") or cp.ROMAN_NUMERALS[int(dom_id[1:])]
        clean_ptitle = re.sub(
            rf"^Partie\s+{re.escape(roman)}\s*[—–:-]?\s*",
            "",
            p["representative_part_title"].strip(),
            flags=re.IGNORECASE,
        ).strip() or p["representative_part_title"].strip()
        p_head = f"Partie {roman} — {dom_id} : {clean_ptitle}"
        part_anchors[dom_id] = cp.gfm_anchor(p_head, seen)

        for ch_num in p["chapter_numbers"]:
            ch_num = int(ch_num)
            ch = chapters_by_num[ch_num]
            clean_chtitle = re.sub(
                rf"^Chapitre\s+0?{ch_num}\s*[—–:-]?\s*",
                "",
                ch["representative_title"].strip(),
                flags=re.IGNORECASE,
            ).strip() or ch["representative_title"].strip()
            ch_head = f"Chapitre {ch_num:02d} — {clean_chtitle}"
            chapter_anchors[ch_num] = cp.gfm_anchor(ch_head, seen)
            cp.gfm_anchor(f"{ch_num:02d}.1 Résumé", seen)
            cp.gfm_anchor(f"{ch_num:02d}.2 Descriptif du contenu ciblé", seen)
            for k, fam in enumerate(ch["targeted_content"]["families_and_themes"], 1):
                f_head = f"{ch_num:02d}.2.{k} {fam['family_title'].strip()}"
                family_anchors[fam["family_node_id"]] = cp.gfm_anchor(f_head, seen)

    annexe_anchors: dict[str, str] = {}
    for ann in global_shard["annexes"]:
        acode = ann["annexe_code"]
        clean_atitle = re.sub(
            rf"^Annexe\s+{re.escape(acode)}\s*[—–:-]?\s*",
            "",
            ann["representative_title"].strip(),
            flags=re.IGNORECASE,
        ).strip() or ann["representative_title"].strip()
        a_head = f"Annexe {acode} — {clean_atitle}"
        annexe_anchors[acode] = cp.gfm_anchor(a_head, seen)
        cp.gfm_anchor(f"Annexe {acode}.1 Résumé", seen)
        cp.gfm_anchor(f"Annexe {acode}.2 Descriptif du contenu ciblé", seen)
        if acode == "A":
            cp.gfm_anchor("Table maîtresse de traçabilité MindMap (12 Domaines / 36 Sous-domaines / 71 Familles / 260 Thèmes) → PRD", seen)
        elif acode == "B":
            cp.gfm_anchor("Répartition des 616 interrelations par type canonique", seen)
            cp.gfm_anchor("Top 20 des nœuds carrefours par degré d'interrelations", seen)
            cp.gfm_anchor("Tensions d'arbitrage structurantes (62 relations `tension_arbitrage`)", seen)
        elif acode == "C":
            cp.gfm_anchor("Fermeture de la divergence architecturale `DIV-02` (Tome 5)", seen)
            cp.gfm_anchor("Résolution des cinq discordances inter-volumes (`DISC-01` à `DISC-05`, Tome 8 §0.2)", seen)
            cp.gfm_anchor("Jalons chronologiques consolidés 2023–2035 (extrait structurant sur 100 jalons)", seen)
        elif acode == "D":
            cp.gfm_anchor("Synthèse d'homologation vérifiable `G0–G5`, licences et clause `non-avis`", seen)
            cp.gfm_anchor("Distribution des 267 entrées de la matrice de traçabilité par famille", seen)
            cp.gfm_anchor("Extrait stratifié multi-familles de la matrice de traçabilité `EXIG / CAP / PRR-75 / C01–C40 / 5 SBB / PEX` (60 entrées représentatives sur 267 au bundle)", seen)
            cp.gfm_anchor("Répartition des 16 familles normatives `CRE-IA-2026-01` (305 `EXIG-*` : `DOIT` 255, `NE_DOIT_PAS` 34, `DEVRAIT` 16)", seen)
            cp.gfm_anchor("Cinq blocs normalisés (`5 SBB`) et trois blueprints (`C01–C40`)", seen)

    return {
        "exec_anchor": exec_anchor,
        "exec_section_anchors": exec_section_anchors,
        "part_anchors": part_anchors,
        "chapter_anchors": chapter_anchors,
        "family_anchors": family_anchors,
        "annexe_anchors": annexe_anchors,
    }


def _extract_anchor_line(reference: str) -> int | None:
    m = re.search(r"\bL(\d+)\s*[–-]\s*L?\d+", reference) or re.search(r"\bL([1-9]\d*)\b", reference)
    return int(m.group(1)) if m else None


def _build_annexes_payload(
    global_shard: dict[str, Any],
    bundle: dict[str, Any],
    raw_pivots: dict[str, Any],
    chapters_out: list[dict[str, Any]],
    anchors: dict[str, Any],
    theme_to_chapter: dict[str, int],
) -> list[dict[str, Any]]:
    """Construit les 4 annexes A–D avec leurs tables analytiques exactes."""
    nodes = bundle["nodes"]
    relations = bundle["relations"]
    rel_types = {rt["type_id"]: rt for rt in bundle["relation_types"]}
    pivots = bundle.get("pivots") or {}
    node_by_id = {n["node_id"]: n for n in nodes}
    chapters_by_num = {c["chapter_number"]: c for c in chapters_out}
    chap_anchors = anchors["chapter_anchors"]
    ann_anchors = anchors["annexe_anchors"]

    annexes_out: list[dict[str, Any]] = []
    for ann in global_shard["annexes"]:
        acode = ann["annexe_code"]
        clean_atitle = re.sub(
            rf"^Annexe\s+{re.escape(acode)}\s*[—–:-]?\s*",
            "",
            ann["representative_title"].strip(),
            flags=re.IGNORECASE,
        ).strip() or ann["representative_title"].strip()

        entry: dict[str, Any] = {
            "annexe_code": acode,
            "representative_title": f"Annexe {acode} — {clean_atitle}",
            "slug": ann_anchors[acode],
            "executive_summary": ann["executive_summary"].strip(),
            "targeted_content_description": ann["targeted_content_description"].strip(),
        }

        if acode == "A":
            rows_a = []
            for ch in chapters_out:
                cnum = ch["chapter_number"]
                fams = ch["targeted_content"]["families_and_themes"]
                thm_list = [th for f in fams for th in f["themes_targeted"]]
                occ_sum = sum(int(node_by_id[th["theme_node_id"]].get("occurrence_count", 0)) for th in thm_list)
                ids_set: set[str] = set()
                for th in thm_list:
                    ids_set.update(node_by_id[th["theme_node_id"]].get("identifiers") or [])
                rows_a.append(
                    {
                        "chapter_number": cnum,
                        "chapter_code": ch["chapter_code"],
                        "chapter_slug": ch["slug"],
                        "domain_id": ch["domain_id"],
                        "subdomain_node_id": ch["subdomain_node_id"],
                        "subdomain_title": ch["subdomain_title"],
                        "representative_title": ch["representative_title"],
                        "families_count": len(fams),
                        "themes_count": len(thm_list),
                        "occurrence_count": occ_sum,
                        "tomes_present": ch["tomes_present"],
                        "key_identifiers": sorted(ids_set)[:6],
                    }
                )
            entry["traceability_table"] = rows_a
            entry["totals"] = {
                "domains": 12,
                "chapters": len(rows_a),
                "families": sum(r["families_count"] for r in rows_a),
                "themes": sum(r["themes_count"] for r in rows_a),
            }

        elif acode == "B":
            counts = Counter(r["type"] for r in relations)
            entry["relation_types_stats"] = [
                {
                    "type_id": rt_id,
                    "label": rt["label"],
                    "count": counts.get(rt_id, 0),
                    "directionality": rt.get("directionality", ""),
                    "semantic_rule": rt.get("semantic_rule", ""),
                }
                for rt_id, rt in rel_types.items()
            ]
            themes = [n for n in nodes if n["node_kind"] == "theme"]
            deg_sorted = sorted(themes, key=lambda n: (-int(n.get("relation_degree", 0)), n["title"]))[:20]
            entry["top_hubs"] = [
                {
                    "rank": idx,
                    "node_id": tn["node_id"],
                    "canonical_slug": tn["canonical_slug"],
                    "title": tn["title"],
                    "domain_id": tn["domain_id"],
                    "chapter_number": theme_to_chapter.get(tn["node_id"]),
                    "chapter_slug": chap_anchors.get(theme_to_chapter.get(tn["node_id"], 0), ""),
                    "relation_degree": int(tn.get("relation_degree", 0)),
                    "occurrence_count": int(tn.get("occurrence_count", 0)),
                    "tomes_present": tn.get("tomes_present") or [],
                }
                for idx, tn in enumerate(deg_sorted, 1)
            ]
            tensions_raw = [r for r in relations if r["type"] == "tension_arbitrage"]
            entry["tensions"] = [
                {
                    "relation_id": tr.get("relation_id", ""),
                    "source_node_id": tr["source"],
                    "source_slug": node_by_id.get(tr["source"], {}).get("canonical_slug", tr["source"]),
                    "source_title": node_by_id.get(tr["source"], {}).get("title", ""),
                    "source_chapter_number": theme_to_chapter.get(tr["source"]),
                    "target_node_id": tr["target"],
                    "target_slug": node_by_id.get(tr["target"], {}).get("canonical_slug", tr["target"]),
                    "target_title": node_by_id.get(tr["target"], {}).get("title", ""),
                    "target_chapter_number": theme_to_chapter.get(tr["target"]),
                    "label": tr.get("label", ""),
                    "justification": tr.get("justification", ""),
                    "tomes": tr.get("tomes") or [],
                }
                for tr in tensions_raw
            ]

        elif acode == "C":
            entry["div_02"] = pivots.get("div_02") or {}
            entry["reconciliations"] = pivots.get("reconciliations") or []
            entry["timeline"] = pivots.get("timeline") or []

        elif acode == "D":
            mat = pivots.get("traceability_matrix") or []
            fam_buckets: dict[str, list[dict[str, Any]]] = {}
            subfam_counts: Counter[str] = Counter()
            for item in mat:
                fam_full = str(item.get("family") or "Autre")
                fam_top = fam_full.split(" (")[0].strip()
                fam_buckets.setdefault(fam_top, []).append(item)
                subfam_counts[fam_full] += 1

            matrix_distribution = []
            for fam_top in sorted(fam_buckets, key=lambda k: (-len(fam_buckets[k]), k)):
                subfams = [
                    {"name": sf, "count": cnt}
                    for sf, cnt in sorted(subfam_counts.items())
                    if sf.split(" (")[0].strip() == fam_top
                ]
                matrix_distribution.append(
                    {"family": fam_top, "count": len(fam_buckets[fam_top]), "subfamilies": subfams}
                )

            stratified_mat: list[dict[str, Any]] = []
            bucket_order = sorted(fam_buckets.keys())
            for r_idx in range(6):
                for fam_top in bucket_order:
                    b = fam_buckets[fam_top]
                    if r_idx < len(b):
                        stratified_mat.append(b[r_idx])

            raw_mat = raw_pivots.get("matrices") or {}
            exig_cre = raw_mat.get("exig_cre_ia_2026_v1_2") or {}
            t8_exec = raw_mat.get("tome8_executable") or {}
            prr_raw = raw_mat.get("prr_75") or {}
            prr_items = prr_raw.get("items") or []
            prr_blocking_by_grid = dict(Counter(x["grid"] for x in prr_items if x.get("is_blocking")))

            c40_counts = Counter(str(item.get("family", "")) for item in mat if str(item.get("family", "")).startswith("C40"))
            c40_breakdown = {
                "total": sum(c40_counts.values()),
                "BLOQUANT": c40_counts.get("C40 (BLOQUANT)", 0),
                "OBLIGATOIRE": c40_counts.get("C40 (OBLIGATOIRE)", 0),
                "RECOMMANDE": c40_counts.get("C40 (RECOMMANDE)", 0),
            }

            entry["bilans_aq"] = pivots.get("bilans_aq") or {}
            entry["collection_metrics"] = pivots.get("collection_metrics") or {}
            entry["matrix_distribution"] = matrix_distribution
            entry["matrix_sample"] = stratified_mat
            entry["matrix_all"] = mat
            entry["exig_cre_ia"] = {
                "code_norme": exig_cre.get("code_norme", "CRE-IA-2026-01"),
                "total": exig_cre.get("total", 305),
                "repartition_force": exig_cre.get("repartition_force") or {},
                "familles": exig_cre.get("familles") or [],
            }
            entry["prr_summary"] = {
                "total": prr_raw.get("total", 75),
                "blocking_count": prr_raw.get("blocking_count", 24),
                "conditional_count": prr_raw.get("conditional_count", 26),
                "elevated_medium_count": prr_raw.get("elevated_medium_count", 25),
                "blocking_by_grid": prr_blocking_by_grid,
            }
            entry["five_sbb"] = t8_exec.get("cinq_sbb_tableau_12") or []
            entry["blueprints_c40"] = {
                "blueprints": t8_exec.get("c01_a_c40_blueprints") or [],
                "c40_breakdown": c40_breakdown,
            }

        annexes_out.append(entry)

    return annexes_out


def build_prd_web_payload(
    repo_root: Path,
    bundle: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Assemble le payload complet du PRD pour ``prd-web-data.json`` et la Vue 5 MindMap."""
    donnees_dir = repo_root / "Cartographie" / "donnees"
    if bundle is None:
        bundle_path = donnees_dir / "corpus-mindmap-data.json"
        if not bundle_path.is_file():
            raise FileNotFoundError(f"Bundle MindMap introuvable : {bundle_path}")
        bundle = json.loads(bundle_path.read_text(encoding="utf-8"))

    pivots_path = donnees_dir / "pivots-concordance.json"
    raw_pivots = json.loads(pivots_path.read_text(encoding="utf-8")) if pivots_path.is_file() else {}

    global_shard, chapters_raw = _load_and_validate_shards(repo_root, bundle)
    chapters_by_num = {int(c["chapter_number"]): c for c in chapters_raw}
    anchors = _compute_gfm_anchors(global_shard, chapters_by_num)

    nodes = bundle["nodes"]
    relations = bundle["relations"]
    domains_by_id = {d["domain_id"]: d for d in bundle["domains"]}
    rel_types = {rt["type_id"]: rt for rt in bundle["relation_types"]}
    node_by_id = {n["node_id"]: n for n in nodes}
    node_by_slug = {n["canonical_slug"]: n for n in nodes if n.get("canonical_slug")}

    theme_to_chapter: dict[str, int] = {}
    theme_to_family: dict[str, str] = {}
    slug_to_chapter: dict[str, int] = {}
    for ch in chapters_raw:
        cnum = int(ch["chapter_number"])
        for fam in ch["targeted_content"]["families_and_themes"]:
            fid = fam["family_node_id"]
            for th in fam["themes_targeted"]:
                theme_to_chapter[th["theme_node_id"]] = cnum
                theme_to_family[th["theme_node_id"]] = fid
                slug_to_chapter[th["canonical_slug"]] = cnum

    # Statistiques live de prd.md si présent
    prd_md_path = repo_root / "prd.md"
    line_count, word_count, heading_count = 0, 0, 0
    if prd_md_path.is_file():
        prd_text = prd_md_path.read_text(encoding="utf-8")
        prd_lines = prd_text.splitlines()
        headings, _, _ = es.parse_markdown_lines(prd_lines)
        line_count = len(prd_lines)
        word_count = len(prd_text.split())
        heading_count = len(headings)

    gmeta = global_shard.get("metadata") or {}
    meta = {
        "prd_title": global_shard["prd_title"].strip(),
        "prd_subtitle": global_shard["prd_subtitle"].strip(),
        "toc_representative_title": global_shard["toc_representative_title"].strip(),
        "toc_intro_note": global_shard.get("toc_intro_note", "").strip(),
        "version": gmeta.get("version", "1.0.0"),
        "date": gmeta.get("date", "2026-11-24"),
        "status": gmeta.get("status", "Référentiel d'exigences produit et architecture (non-avis)"),
        "source_md": "../prd.md",
        "line_count": line_count,
        "word_count": word_count,
        "heading_count": heading_count,
        "domains_count": 12,
        "chapters_count": len(chapters_raw),
        "families_count": sum(len(c["targeted_content"]["families_and_themes"]) for c in chapters_raw),
        "themes_count": len(theme_to_chapter),
        "relations_count": len(relations),
        "annexes_count": len(global_shard["annexes"]),
    }

    exec_raw = global_shard["executive_summary"]
    exec_sections = []
    for idx, sec in enumerate(exec_raw["sections"], 1):
        paragraphs, kpi_table = _parse_markdown_section_body(sec["body"].strip())
        exec_sections.append(
            {
                "id": f"exec-{idx:02d}",
                "slug": anchors["exec_section_anchors"][idx - 1],
                "heading": sec["heading"].strip(),
                "body_md": sec["body"].strip(),
                "paragraphs": paragraphs,
                "kpi_table": kpi_table,
            }
        )
    executive_summary = {
        "title": exec_raw.get("title", "Sommaire exécutif global").strip(),
        "slug": anchors["exec_anchor"],
        "lead": exec_raw["lead"].strip(),
        "sections": exec_sections,
    }

    parties_out: list[dict[str, Any]] = []
    domain_to_part: dict[str, int] = {}
    for p in global_shard["parties"]:
        dom_id = p["domain_id"]
        p_num = int(p["part_number"])
        domain_to_part[dom_id] = p_num
        dom_meta = domains_by_id[dom_id]
        roman = p.get("part_roman") or cp.ROMAN_NUMERALS[int(dom_id[1:])]
        clean_ptitle = re.sub(
            rf"^Partie\s+{re.escape(roman)}\s*[—–:-]?\s*",
            "",
            p["representative_part_title"].strip(),
            flags=re.IGNORECASE,
        ).strip() or p["representative_part_title"].strip()
        parties_out.append(
            {
                "part_number": p_num,
                "part_roman": roman,
                "domain_id": dom_id,
                "domain_node_id": dom_meta.get("node_id") or f"DOM_{dom_id}",
                "domain_title": dom_meta["title"],
                "key_identifiers": dom_meta.get("key_identifiers") or [],
                "representative_part_title": clean_ptitle,
                "part_summary": p["part_summary"].strip(),
                "chapter_numbers": [int(c) for c in p["chapter_numbers"]],
                "slug": anchors["part_anchors"][dom_id],
            }
        )

    # Index rapide des relations MindMap par paire (source_id, target_id) pour enrichir les relations de shards
    rels_by_pair: dict[tuple[str, str], list[dict[str, Any]]] = {}
    for mrel in relations:
        rels_by_pair.setdefault((mrel["source"], mrel["target"]), []).append(mrel)

    chapters_out: list[dict[str, Any]] = []
    for ch in chapters_raw:
        cnum = int(ch["chapter_number"])
        dom_id = ch["domain_id"]
        sub_node = node_by_id[ch["subdomain_node_id"]]
        tc = ch["targeted_content"]

        fams_out: list[dict[str, Any]] = []
        ch_theme_ids: set[str] = set()
        for k, fam in enumerate(tc["families_and_themes"], 1):
            themes_out: list[dict[str, Any]] = []
            for th in fam["themes_targeted"]:
                tid = th["theme_node_id"]
                ch_theme_ids.add(tid)
                mm_node = node_by_id[tid]
                ids_merged = sorted(
                    set(th.get("identifiers_and_norms") or []) | set(mm_node.get("identifiers") or [])
                )
                direct_anchors = [
                    {
                        "tome_id": occ["tome_id"],
                        "file": occ["file"],
                        "line_start": int(occ["line_start"]),
                        "line_end": int(occ["line_end"]),
                        "label": f"{occ['tome_id']} L{occ['line_start']}–L{occ['line_end']}",
                    }
                    for occ in (mm_node.get("occurrences") or [])
                ]
                themes_out.append(
                    {
                        "theme_node_id": tid,
                        "canonical_slug": th["canonical_slug"],
                        "theme_title": th["theme_title"].strip(),
                        "content_specification": th["content_specification"].strip(),
                        "autonomy_levels": mm_node.get("autonomy_levels") or [],
                        "roles": mm_node.get("roles") or [],
                        "horizon": mm_node.get("horizon") or "",
                        "horizons": mm_node.get("horizons") or [],
                        "tomes_present": mm_node.get("tomes_present") or [],
                        "identifiers_and_norms": ids_merged,
                        "occurrence_count": int(mm_node.get("occurrence_count", 0)),
                        "relation_degree": int(mm_node.get("relation_degree", 0)),
                        "direct_anchors": direct_anchors,
                    }
                )
            fams_out.append(
                {
                    "family_node_id": fam["family_node_id"],
                    "family_code": f"{cnum:02d}.2.{k}",
                    "family_title": fam["family_title"].strip(),
                    "slug": anchors["family_anchors"][fam["family_node_id"]],
                    "family_overview": fam["family_overview"].strip(),
                    "themes_targeted": themes_out,
                }
            )

        # Interrelations de shard + complétion intégrale depuis les 616 relations du MindMap
        inter_out: list[dict[str, Any]] = []
        seen_rel_keys: set[tuple[int, str]] = set()
        for rel in tc.get("cross_chapter_interrelations", []):
            t_num = int(rel["target_chapter_number"])
            t_slug = rel.get("target_slug", "")
            seen_rel_keys.add((t_num, t_slug))
            direction = rel.get("direction", "sortante")
            rtype = rel.get("relation_type", "")
            tgt_node = node_by_slug.get(t_slug) or {}
            tgt_nid = tgt_node.get("node_id", "")

            local_slug = ""
            rel_label = rel_types.get(rtype, {}).get("label", rtype)
            if tgt_nid:
                for local_tid in sorted(ch_theme_ids):
                    pair = (local_tid, tgt_nid) if direction == "sortante" else (tgt_nid, local_tid)
                    matched = [r for r in rels_by_pair.get(pair, []) if r["type"] == rtype] or rels_by_pair.get(pair, [])
                    if matched:
                        local_slug = node_by_id[local_tid]["canonical_slug"]
                        rel_label = matched[0]["label"]
                        break

            inter_out.append(
                {
                    "direction": direction,
                    "relation_type": rtype,
                    "target_chapter_number": t_num,
                    "target_chapter_title": chapters_by_num[t_num]["representative_title"].strip(),
                    "target_slug": t_slug,
                    "target_node_id": tgt_nid,
                    "local_slug": local_slug,
                    "label": rel_label,
                    "synthesis": rel.get("synthesis", "").strip(),
                }
            )

        for mrel in relations:
            src, tgt = mrel["source"], mrel["target"]
            if src in ch_theme_ids and tgt not in ch_theme_ids:
                o_ch = theme_to_chapter.get(tgt)
                o_node = node_by_id.get(tgt)
                if o_ch and o_node and (o_ch, o_node["canonical_slug"]) not in seen_rel_keys:
                    seen_rel_keys.add((o_ch, o_node["canonical_slug"]))
                    inter_out.append(
                        {
                            "direction": "sortante",
                            "relation_type": mrel["type"],
                            "target_chapter_number": o_ch,
                            "target_chapter_title": chapters_by_num[o_ch]["representative_title"].strip(),
                            "target_slug": o_node["canonical_slug"],
                            "target_node_id": tgt,
                            "local_slug": node_by_id[src]["canonical_slug"],
                            "label": mrel["label"],
                            "synthesis": f"{mrel['label']} — {mrel['justification']}",
                        }
                    )
            elif tgt in ch_theme_ids and src not in ch_theme_ids:
                o_ch = theme_to_chapter.get(src)
                o_node = node_by_id.get(src)
                if o_ch and o_node and (o_ch, o_node["canonical_slug"]) not in seen_rel_keys:
                    seen_rel_keys.add((o_ch, o_node["canonical_slug"]))
                    inter_out.append(
                        {
                            "direction": "entrante",
                            "relation_type": mrel["type"],
                            "target_chapter_number": o_ch,
                            "target_chapter_title": chapters_by_num[o_ch]["representative_title"].strip(),
                            "target_slug": o_node["canonical_slug"],
                            "target_node_id": src,
                            "local_slug": node_by_id[tgt]["canonical_slug"],
                            "label": mrel["label"],
                            "synthesis": f"{mrel['label']} — {mrel['justification']}",
                        }
                    )

        corpus_anchors_out = [
            {
                "tome_id": anc["tome_id"],
                "file": anc["file"],
                "line_start": _extract_anchor_line(str(anc.get("reference", ""))),
                "reference": str(anc.get("reference", "")).strip(),
            }
            for anc in tc.get("corpus_anchors", [])
        ]

        clean_chtitle = re.sub(
            rf"^Chapitre\s+0?{cnum}\s*[—–:-]?\s*",
            "",
            ch["representative_title"].strip(),
            flags=re.IGNORECASE,
        ).strip() or ch["representative_title"].strip()

        chapters_out.append(
            {
                "chapter_number": cnum,
                "chapter_code": ch["chapter_code"],
                "part_number": domain_to_part[dom_id],
                "domain_id": dom_id,
                "subdomain_node_id": ch["subdomain_node_id"],
                "subdomain_title": sub_node["title"],
                "representative_title": clean_chtitle,
                "slug": anchors["chapter_anchors"][cnum],
                "executive_summary": ch["executive_summary"].strip(),
                "tomes_present": sub_node.get("tomes_present") or [],
                "autonomy_levels": sub_node.get("autonomy_levels") or [],
                "roles": sub_node.get("roles") or [],
                "horizons": sub_node.get("horizons") or [],
                "targeted_content": {
                    "scope_and_objectives": tc["scope_and_objectives"].strip(),
                    "key_requirements_and_objectives": [x.strip() for x in tc["key_requirements_and_objectives"]],
                    "families_and_themes": fams_out,
                    "deliverables_and_verification": [x.strip() for x in tc["deliverables_and_verification"]],
                    "cross_chapter_interrelations": inter_out,
                    "corpus_anchors": corpus_anchors_out,
                },
            }
        )

    annexes_out = _build_annexes_payload(
        global_shard,
        bundle,
        raw_pivots,
        chapters_out,
        anchors,
        theme_to_chapter,
    )

    # Lookup couvrant 100 % des 379 nœuds non-racine du MindMap + chapitres structurels
    node_id_to_prd: dict[str, dict[str, Any]] = {}
    for n in nodes:
        nkind = n.get("node_kind")
        nid = n["node_id"]
        if nkind == "root":
            continue
        dom_id = n["domain_id"]
        if nkind == "domain":
            pnum = domain_to_part[dom_id]
            node_id_to_prd[nid] = {
                "kind": "domain",
                "domain_id": dom_id,
                "chapter_number": None,
                "family_node_id": None,
                "theme_node_id": None,
                "section_id": f"part-{pnum:02d}",
                "slug": anchors["part_anchors"][dom_id],
            }
        elif nkind == "subdomain":
            cnum = cp.expected_chapter_number(dom_id, nid)
            node_id_to_prd[nid] = {
                "kind": "subdomain",
                "domain_id": dom_id,
                "chapter_number": cnum,
                "family_node_id": None,
                "theme_node_id": None,
                "section_id": f"ch-{cnum:02d}",
                "slug": anchors["chapter_anchors"][cnum],
            }
        elif nkind == "family":
            sub_id = n["parent_id"]
            cnum = cp.expected_chapter_number(dom_id, sub_id)
            node_id_to_prd[nid] = {
                "kind": "family",
                "domain_id": dom_id,
                "chapter_number": cnum,
                "family_node_id": nid,
                "theme_node_id": None,
                "section_id": f"fam-{nid}",
                "slug": anchors["family_anchors"][nid],
            }
        elif nkind == "theme":
            cnum = theme_to_chapter[nid]
            fid = theme_to_family[nid]
            node_id_to_prd[nid] = {
                "kind": "theme",
                "domain_id": dom_id,
                "chapter_number": cnum,
                "family_node_id": fid,
                "theme_node_id": nid,
                "section_id": f"thm-{n['canonical_slug']}",
                "slug": anchors["family_anchors"][fid],
            }

    unit_id_to_chapter: dict[str, int] = {}
    for struct_ch in bundle.get("chapters") or []:
        uid = struct_ch.get("unit_id")
        if not uid:
            continue
        for tslug in struct_ch.get("themes_addressed") or []:
            if tslug in slug_to_chapter:
                unit_id_to_chapter[uid] = slug_to_chapter[tslug]
                break

    payload = {
        "schema_version": "1.0.0",
        "lang": "fr-CA",
        "generator": "Cartographie/outils/preparer_donnees_prd_web.py",
        "meta": meta,
        "executive_summary": executive_summary,
        "parties": parties_out,
        "chapters": chapters_out,
        "annexes": annexes_out,
        "lookup": {
            "node_id_to_prd": node_id_to_prd,
            "slug_to_chapter": slug_to_chapter,
            "domain_to_part": domain_to_part,
            "unit_id_to_chapter": unit_id_to_chapter,
        },
    }

    # Assertions internes de parité stricte (12 / 36 / 71 / 260 / 616 / 62 / 4 / 379)
    assert len(parties_out) == 12, f"parties={len(parties_out)}"
    assert len(chapters_out) == 36, f"chapters={len(chapters_out)}"
    assert meta["families_count"] == 71, f"families={meta['families_count']}"
    assert meta["themes_count"] == 260, f"themes={meta['themes_count']}"
    assert len(annexes_out) == 4, f"annexes={len(annexes_out)}"
    assert len(executive_summary["sections"]) == 5
    assert executive_summary["sections"][3]["kpi_table"] is not None
    assert len(executive_summary["sections"][3]["kpi_table"]["rows"]) == 8
    ann_b = next(a for a in annexes_out if a["annexe_code"] == "B")
    assert sum(rt["count"] for rt in ann_b["relation_types_stats"]) == 616
    assert len(ann_b["tensions"]) == 62
    assert len(ann_b["top_hubs"]) == 20
    ann_c = next(a for a in annexes_out if a["annexe_code"] == "C")
    assert len(ann_c["reconciliations"]) == 5
    assert len(ann_c["timeline"]) == 100
    ann_d = next(a for a in annexes_out if a["annexe_code"] == "D")
    assert sum(d["count"] for d in ann_d["matrix_distribution"]) == 267
    assert ann_d["blueprints_c40"]["c40_breakdown"] == {"total": 40, "BLOQUANT": 18, "OBLIGATOIRE": 15, "RECOMMANDE": 7}
    assert len(node_id_to_prd) == 379, f"lookup nodes={len(node_id_to_prd)} != 379"

    return payload


def main() -> int:
    """Point d'entrée CLI générant ``Cartographie/donnees/prd-web-data.json``."""
    parser = argparse.ArgumentParser(description="Prépare prd-web-data.json depuis le MindMap et les shards PRD.")
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path(__file__).resolve().parents[2],
        help="Racine du dépôt Agentique.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Chemin de sortie JSON (défaut : Cartographie/donnees/prd-web-data.json).",
    )
    args = parser.parse_args()

    repo_root = args.repo_root.resolve()
    payload = build_prd_web_payload(repo_root)
    out_path = args.output or (repo_root / "Cartographie" / "donnees" / "prd-web-data.json")
    out_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    m = payload["meta"]
    print(
        f"Données web PRD générées -> {out_path} : {m['domains_count']} domaines, "
        f"{m['chapters_count']} chapitres, {m['families_count']} familles, {m['themes_count']} thèmes, "
        f"{m['relations_count']} relations, {m['annexes_count']} annexes, "
        f"{len(payload['lookup']['node_id_to_prd'])} nœuds indexés"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
