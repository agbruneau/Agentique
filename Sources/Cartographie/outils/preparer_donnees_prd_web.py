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
import consolider_catalogue_schemas as ccs  # noqa: E402
import extraire_structure as es  # noqa: E402

TOME_RANK: dict[str, int] = {
    "R": 0,
    "LIM": 1,
    "P01": 2,
    "P02": 3,
    "P03": 4,
    "P04": 5,
    "P05": 6,
    "P06": 7,
    "P07": 8,
    "P08": 9,
    "P09": 10,
    "P10": 11,
    "P11": 12,
    "P12": 13,
    "ANN": 14,
    "T1": 21,
    "T2": 22,
    "T3": 23,
    "T4": 24,
    "T5": 25,
    "T6": 26,
    "T7": 27,
    "T8": 28,
}

# Correspondance entre les 6 repères généraux README et les clés canoniques L+
README_TO_CANONICAL_KEYS: dict[str, list[str]] = {
    "Depuis sept. 2023": ["2026-LOI25-ART12-1"],
    "Depuis août 2026": ["2026-08-02-EU-AI-ACT-ART50"],
    "Mars 2027 → Mars 2029": ["2027-03-15-TLS-100J", "2029-03-15-TLS-47J"],
    "1er mai 2027": ["2027-05-01-BSIF-E23-AMF"],
    "2027–2028": ["2027-12-02-EU-AI-ACT-ANNEXE-III", "2028-08-02-EU-AI-ACT-ANNEXE-I"],
    "2030–2035": ["2030-2035-G7-PQC-FINANCE"],
}


def _check(condition: bool, message: str) -> None:
    """Lève ValueError de façon inconditionnelle (indépendant de ``python -O``)."""
    if not condition:
        raise ValueError(message)


def _clean_text(value: Any) -> str:
    """Supprime ``\\$``, normalise plages ``Lxxx–Lyyy``, flèches, comparateurs et « Systèmes d'agentivité » hors code."""
    s = str(value or "").replace(r"\$", "$").strip()
    s = re.sub(r"\bL([1-9]\d*)-L?([1-9]\d*)\b", r"L\1–L\2", s)

    def _clean_outside_code(seg: str) -> str:
        chunks = re.split(r"(<code\b[^>]*>.*?</code>)", seg, flags=re.IGNORECASE | re.DOTALL)
        for idx in range(0, len(chunks), 2):
            part = chunks[idx]
            part = part.replace("<->", "↔").replace("->", "→")
            part = (
                part.replace("Systems of Agency", "Systèmes d'agentivité")
                .replace("System of Agency", "Système d'agentivité")
                .replace("systems of agency", "systèmes d'agentivité")
            )
            part = re.sub(r"(?<![<>=])<=(?!=)", "≤", part)
            part = re.sub(r"(?<![<>=])>=(?!=)", "≥", part)
            chunks[idx] = part
        return "".join(chunks)

    return cp.cm.map_outside_inline_code(s, _clean_outside_code)


def _clean_nested_strings(obj: Any, skip_keys: set[str] | None = None) -> Any:
    """Applique ``_clean_text`` récursivement sur les chaînes d'une structure JSON."""
    skip = skip_keys or {
        "file", "canonical_slug", "node_id", "unit_id", "id", "discordance_id",
        "pytest_nodeid", "implementation_symbol", "rego_rule", "type", "type_id",
        "domain_id", "tome_id", "part_id", "section_id", "schema_id", "subdomain_node_id",
        "families_covered", "themes_vulgarized", "source_path", "rendered_path",
        "source_section_file", "fig_id", "diagram_uid", "chapter_code", "reuse_status",
        "linked_schema_ids", "source_file", "compendium_md_file", "compendium_rendered_path",
        "compendium_source_path", "en",
    }
    if isinstance(obj, str):
        return _clean_text(obj)
    if isinstance(obj, list):
        return [_clean_nested_strings(v, skip) for v in obj]
    if isinstance(obj, dict):
        return {k: (v if k in skip else _clean_nested_strings(v, skip)) for k, v in obj.items()}
    return obj


def _clean_schema_entry(raw_item: dict[str, Any]) -> dict[str, Any]:
    """Nettoie les chaînes éditoriales d'un schéma ``SCH-*`` et expose les liens Compendium compilés."""
    cleaned = dict(_clean_nested_strings(raw_item))
    cfig = raw_item.get("compendium_figure")
    if isinstance(cfig, dict):
        cleaned["compendium_rendered_path"] = cfig.get("rendered_path", "")
        cleaned["compendium_source_path"] = cfig.get("source_path", "")
        cleaned["compendium_md_file"] = cfig.get("compendium_md_file", "Compendium/Compendium.md")
        cleaned["compendium_md_line"] = cfig.get("compendium_md_line")
        cleaned["compendium_unit"] = cfig.get("unit", "")
        cleaned["compendium_part_id"] = cfig.get("part_id", "")
        cleaned["compendium_engine"] = cfig.get("engine", "")
        cleaned["compendium_source_file"] = cfig.get("source_file", "")
        cleaned["compendium_source_file_line"] = cfig.get("source_file_line")
    return cleaned


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
    shards_dir = repo_root / "Sources" / "Cartographie" / "donnees" / "prd_shards"
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
    exec_panorama_anchor = cp.gfm_anchor(
        "Panorama visuel directeur — Schémas de vulgarisation transversaux",
        seen,
    )

    part_anchors: dict[str, str] = {}
    chapter_anchors: dict[int, str] = {}
    family_anchors: dict[str, str] = {}
    schema_section_anchors: dict[int, str] = {}

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
            schema_section_anchors[ch_num] = cp.gfm_anchor(
                f"{ch_num:02d}.3 Schémas de vulgarisation à intégrer",
                seen,
            )

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

    return {
        "exec_anchor": exec_anchor,
        "exec_section_anchors": exec_section_anchors,
        "exec_panorama_anchor": exec_panorama_anchor,
        "part_anchors": part_anchors,
        "chapter_anchors": chapter_anchors,
        "family_anchors": family_anchors,
        "schema_section_anchors": schema_section_anchors,
        "annexe_anchors": annexe_anchors,
    }


def _extract_anchor_line(reference: str) -> int | None:
    m = re.search(r"\bL(\d+)\s*[–-]\s*L?\d+", reference) or re.search(r"\bL([1-9]\d*)\b", reference)
    return int(m.group(1)) if m else None


def _timeline_sort_key(date_str: str, tier: int, cadre: str) -> tuple[int, int, str]:
    """Clé de tri chronologique déterministe 2018 → 2035 pour la chronologie maîtresse."""
    s = date_str.strip()
    if s.startswith("Immédiat"):
        return (20261124, tier, cadre)
    if s.startswith("2027 —"):
        return (20270900, tier, cadre)
    if s.startswith("Fin 2027"):
        return (20271230, tier, cadre)
    if s.startswith("Fin 2028"):
        return (20281231, tier, cadre)
    if s.startswith("2028–2029"):
        return (20280100, tier, cadre)
    if s.startswith("2030–2032"):
        return (20300100, tier, cadre)
    if s.startswith("2030–2035"):
        return (20300101, tier, cadre)
    if s.startswith("2033–2035"):
        return (20330100, tier, cadre)
    m_full = re.search(r"(\d{4})-(\d{2})-(\d{2})", s)
    if m_full:
        return (int(m_full.group(1)) * 10000 + int(m_full.group(2)) * 100 + int(m_full.group(3)), tier, cadre)
    m_ym = re.search(r"(\d{4})-(\d{2})", s)
    if m_ym:
        return (int(m_ym.group(1)) * 10000 + int(m_ym.group(2)) * 100 + 2, tier, cadre)
    m_y = re.search(r"(\d{4})", s)
    if m_y:
        return (int(m_y.group(1)) * 10000 + 101, tier, cadre)
    return (99999999, tier, cadre)


def _format_dapp_date(horizon: str, phase: str) -> str:
    """Formate une phase DAPP sans parenthèses doubles imbriquées."""
    h = _clean_text(horizon)
    p = _clean_text(phase)
    # Normalise "Palier 1 : P1" -> "Palier 1 (P1)" ou "90 jours — J1 : Fondations" -> "90 jours (J1 : Fondations)"
    if " : " in p:
        left, right = p.split(" : ", 1)
        left_clean = left.replace(" — ", " · ").strip()
        p_fmt = f"{left_clean} ({right.strip()})"
    else:
        p_fmt = p.replace("(", "").replace(")", "").strip()
    return f"{h} — {p_fmt}" if h else p_fmt


def _build_consolidated_timeline(raw_pivots: dict[str, Any], pivots: dict[str, Any]) -> list[dict[str, Any]]:
    """Construit la chronologie maîtresse dédupliquée et triée chronologiquement (2018 → 2035)."""
    chrono = raw_pivots.get("chronologie_2023_2035") or {}
    if not chrono:
        # Fallback défensif sur la chronologie pré-normalisée du bundle
        tl = list(pivots.get("timeline") or [])
        return sorted(tl, key=lambda e: _timeline_sort_key(e.get("date", ""), 1, e.get("cadre", "")))

    merged_by_key: dict[str, dict[str, Any]] = {}
    alias_to_entry: dict[str, dict[str, Any]] = {}

    def register_aliases(anc: dict[str, Any], primary_key: str, entry: dict[str, Any]) -> None:
        alias_to_entry[primary_key] = entry
        for al in anc.get("aliases") or []:
            if al:
                alias_to_entry.setdefault(str(al), entry)

    def upsert_l_plus(anc: dict[str, Any], origin_tag: str) -> None:
        key = anc["key"]
        date_val = "2026-08-02" if anc.get("date") == "2026-08" else _clean_text(anc.get("date", ""))
        cadre = f"{_clean_text(anc.get('label', ''))} ({_clean_text(anc.get('jurisdiction', ''))})"
        impact = _clean_text(anc.get("commentaire_annexe") or anc.get("nature", ""))
        file_path = anc.get("compendium_file") or "Compendium/Compendium.md"
        line_start = int(anc.get("compendium_line_start") or 7434)
        chaps = list(anc.get("chapters") or [])
        part_tags = [origin_tag] if not chaps else chaps[:4]
        if key not in merged_by_key:
            merged_by_key[key] = {
                "date": date_val,
                "cadre": cadre,
                "impact_parts": [impact] if impact else [],
                "tomes": list(dict.fromkeys(part_tags)),
                "file": file_path,
                "line_start": line_start,
                "source_group": f"Compendium Annexe C ({origin_tag})",
                "_tier": 0,
            }
        else:
            entry = merged_by_key[key]
            for pt in part_tags:
                if pt not in entry["tomes"]:
                    entry["tomes"].append(pt)
            if impact and impact not in entry["impact_parts"]:
                entry["impact_parts"].append(impact)
        register_aliases(anc, key, merged_by_key[key])

    for anc in chrono.get("ancres_t7_l_plus", []):
        upsert_l_plus(anc, "L+ T7/Compendium")
    for anc in chrono.get("ancres_t8_l_plus", []):
        upsert_l_plus(anc, "L+ T8/Compendium")

    t4_items: list[dict[str, Any]] = []
    for anc in chrono.get("ancres_t4_67", []):
        ch_list = anc.get("chapters") or ["ch25"]
        impact = _clean_text(anc.get("enonce", ""))
        t4_entry = {
            "date": _clean_text(anc.get("echeance", "")),
            "cadre": f"{anc.get('id', '')} · {_clean_text(anc.get('juridiction', ''))} ({_clean_text(anc.get('axe', ''))})",
            "impact_parts": [impact] if impact else [],
            "tomes": list(dict.fromkeys(ch_list[:4])),
            "file": anc.get("compendium_file") or "Compendium/Compendium.md",
            "line_start": int(anc.get("compendium_line_start") or 7434),
            "source_group": "Compendium Annexe C (Ch. 25–26, 31)",
            "_tier": 2,
        }
        t4_items.append(t4_entry)
        register_aliases(anc, str(anc.get("id", "")), t4_entry)

    for rep in chrono.get("six_reperes_readme", []):
        ech = _clean_text(rep.get("echeance", ""))
        target_keys = README_TO_CANONICAL_KEYS.get(ech, [])
        rep_resume = _clean_text(rep.get("resume", ""))
        matched = False
        for tk in target_keys:
            target_entry = alias_to_entry.get(tk)
            if target_entry is not None:
                matched = True
                if "LIM" not in target_entry["tomes"]:
                    target_entry["tomes"].append("LIM")
                if rep_resume and rep_resume[:45] not in " ".join(target_entry["impact_parts"]):
                    target_entry["impact_parts"].append(rep_resume)
        if not matched:
            merged_by_key[f"README-{ech}"] = {
                "date": ech,
                "cadre": _clean_text(rep.get("cadre", "")),
                "impact_parts": [rep_resume] if rep_resume else [],
                "tomes": ["LIM", "ANN"],
                "file": "Compendium/Compendium.md",
                "line_start": 165,
                "source_group": "Repères clés (§ 0.5 / Annexe C)",
                "_tier": 0,
            }

    events: list[dict[str, Any]] = []
    for item in [*merged_by_key.values(), *t4_items]:
        tomes_sorted = sorted(item["tomes"], key=lambda t: (TOME_RANK.get(t, 99), str(t)))
        impact_str = " · ".join(item["impact_parts"][:2])
        events.append(
            {
                "date": item["date"],
                "cadre": item["cadre"],
                "impact": impact_str,
                "tomes": tomes_sorted,
                "file": item["file"],
                "line_start": item["line_start"],
                "source_group": item["source_group"],
                "_tier": item["_tier"],
            }
        )

    for pal in chrono.get("rampe_et_paliers_dapp_t5", []):
        events.append(
            {
                "date": _format_dapp_date(pal.get("horizon", ""), pal.get("phase", "")),
                "cadre": f"DAPP · {_clean_text(pal.get('stade', ''))}",
                "impact": _clean_text(pal.get("jalons", "")),
                "tomes": ["ch31", "ch32"],
                "file": pal.get("compendium_file") or "Compendium/Compendium.md",
                "line_start": int(pal.get("compendium_line_start") or 5091),
                "source_group": "Trajectoire DAPP (Ch. 31 / Annexe C)",
                "_tier": 1,
            }
        )

    events.sort(key=lambda e: _timeline_sort_key(e["date"], e.pop("_tier"), e["cadre"]))
    return events


def _build_unified_matrix(
    raw_pivots: dict[str, Any],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], dict[str, int]]:
    """Construit la matrice unifiée dédupliquée (237 entrées uniques, 0 ID en double)."""
    raw_mat = raw_pivots.get("matrices") or {}
    t8_exec = raw_mat.get("tome8_executable") or {}
    m95 = t8_exec.get("matrice_exig_prr_c40_95") or []
    t8_by_id: dict[str, dict[str, Any]] = {row["id"]: row for row in m95 if row.get("id")}

    unified: list[dict[str, Any]] = []
    seen_ids: set[str] = set()

    def add_entry(entry: dict[str, Any]) -> None:
        eid = entry["id"]
        if eid in seen_ids:
            raise ValueError(f"Identifiant dupliqué dans la matrice unifiée : {eid}")
        seen_ids.add(eid)
        unified.append(entry)

    # 1. 5 SBB du Tableau 12 enrichis de leur test Tome 8
    for sbb in t8_exec.get("cinq_sbb_tableau_12") or []:
        sid = sbb.get("sbb_id", "")
        t8_row = t8_by_id.get(sid)
        t8_ref = f" · `{t8_row['pytest_nodeid']}`" if t8_row and t8_row.get("pytest_nodeid") else ""
        add_entry(
            {
                "id": sid,
                "family": f"5 SBB ({sbb.get('plan', '')})",
                "title": f"{_clean_text(sbb.get('slot', ''))}{t8_ref}",
                "module": _clean_text(sbb.get("module_t8", "")),
                "anchor": t8_row.get("corpus_anchor", "T2 Tableau 12 / T8 Annexe B") if t8_row else "T2 Tableau 12 / T8 Annexe B",
            }
        )

    # 2. Grille unifiée PRR-75 (75 points uniques ; les 24 bloquants incluent leur test pytest/Rego Tome 8)
    prr = raw_mat.get("prr_75") or {}
    for item in prr.get("items") or []:
        pid = item.get("prr_id", "")
        t8_row = t8_by_id.get(pid)
        proof = _clean_text(item.get("artefact_preuve", ""))
        anchor = f"Grille {item.get('grid', '')}"
        if t8_row:
            test_sym = t8_row.get("pytest_nodeid") or t8_row.get("rego_rule") or ""
            mod = f"{t8_row.get('trousse_module', '')}.{t8_row.get('implementation_symbol', '')}".strip(".")
            proof = f"{proof} · Test Tome 8 : `{test_sym}` (`{mod}`)" if test_sym else proof
            if t8_row.get("corpus_anchor"):
                anchor = f"{anchor} · {_clean_text(t8_row['corpus_anchor'])}"
        add_entry(
            {
                "id": pid,
                "family": f"PRR-75 ({_clean_text(item.get('criticite', ''))})",
                "title": _clean_text(item.get("point_controle", "")),
                "module": proof,
                "anchor": anchor,
            }
        )

    # 3. 40 critères C01–C40 des 3 blueprints
    for row in m95:
        if row.get("family") == "C40":
            add_entry(
                {
                    "id": row["id"],
                    "family": f"C40 ({row.get('criticality', '')})",
                    "title": _clean_text(row.get("pytest_nodeid") or row.get("rego_rule") or ""),
                    "module": f"{row.get('trousse_module', '')}.{row.get('implementation_symbol', '')}".strip("."),
                    "anchor": _clean_text(row.get("corpus_anchor", "")),
                }
            )

    # 4. 52 capacités CAP-001..CAP-052 (CAP-046 enrichi de son test pytest Tome 8)
    for cap in raw_mat.get("cap_52") or []:
        cid = cap.get("cap_id", "")
        exigs = ", ".join(cap.get("exigences_cad26", [])[:6])
        mod = exigs or _clean_text(cap.get("type_rattachement_cad26", ""))
        t8_row = t8_by_id.get(cid)
        anchor = _clean_text(cap.get("emplacement", ""))
        if t8_row:
            mod = f"{mod} · Test Tome 8 : `{t8_row.get('pytest_nodeid', '')}`"
            anchor = f"{anchor} · {_clean_text(t8_row.get('corpus_anchor', ''))}"
        add_entry(
            {
                "id": cid,
                "family": f"CAP ({_clean_text(cap.get('statut', ''))} · {_clean_text(cap.get('palier', ''))})",
                "title": _clean_text(cap.get("nom") or cap.get("intitule_condense", "")),
                "module": mod,
                "anchor": anchor,
            }
        )

    # 5. 24 extensions sectorielles PEX
    for pex in raw_mat.get("pex_24") or []:
        add_entry(
            {
                "id": pex.get("pex_id", ""),
                "family": f"PEX ({_clean_text(pex.get('sous_secteur', ''))})",
                "title": _clean_text(pex.get("titre", "")),
                "module": ", ".join(pex.get("exigences_cad26", [])[:5]),
                "anchor": _clean_text(pex.get("chapitre_t4", "")),
            }
        )

    # 6. 24 exigences EXIG-* vérifiées par tests exécutables Tome 8 + fiche 2027-B001
    for row in m95:
        if row.get("family") in ("EXIG", "ADR_TEMPLATE"):
            add_entry(
                {
                    "id": row["id"],
                    "family": f"{row['family']} ({row.get('criticality', '')})",
                    "title": _clean_text(row.get("pytest_nodeid") or row.get("rego_rule") or ""),
                    "module": f"{row.get('trousse_module', '')}.{row.get('implementation_symbol', '')}".strip("."),
                    "anchor": _clean_text(row.get("corpus_anchor", "")),
                }
            )

    # 7. 16 familles normatives CRE-IA-2026-01
    exig_meta = raw_mat.get("exig_cre_ia_2026_v1_2") or {}
    for fam in exig_meta.get("familles") or []:
        if isinstance(fam, dict):
            add_entry(
                {
                    "id": fam.get("prefixe") or fam.get("code", ""),
                    "family": "CRE-IA-2026-01 (Famille EXIG)",
                    "title": _clean_text(fam.get("titre") or fam.get("domaine") or ""),
                    "module": f"{fam.get('nombre', fam.get('count', ''))} exigences",
                    "anchor": "T2 Annexe D / T5 Annexe A",
                }
            )

    fam_buckets: dict[str, list[dict[str, Any]]] = {}
    subfam_counts: Counter[str] = Counter()
    for item in unified:
        fam_full = str(item.get("family") or "Autre")
        fam_top = fam_full.split(" (")[0].strip()
        fam_buckets.setdefault(fam_top, []).append(item)
        subfam_counts[fam_full] += 1

    matrix_distribution = [
        {
            "family": fam_top,
            "count": len(fam_buckets[fam_top]),
            "subfamilies": [
                {"name": sf, "count": cnt}
                for sf, cnt in sorted(subfam_counts.items())
                if sf.split(" (")[0].strip() == fam_top
            ],
        }
        for fam_top in sorted(fam_buckets, key=lambda k: (-len(fam_buckets[k]), k))
    ]

    summary_counts = {
        "unique_entries": len(unified),
        "tome8_executable_tests": len(m95),
        "shared_ids_merged": len(m95) + 5 + len(prr.get("items") or []) + len(raw_mat.get("cap_52") or []) + len(raw_mat.get("pex_24") or []) + len(exig_meta.get("familles") or []) - len(unified),
    }
    return unified, matrix_distribution, summary_counts


def _build_annexes_payload(
    global_shard: dict[str, Any],
    bundle: dict[str, Any],
    raw_pivots: dict[str, Any],
    chapters_out: list[dict[str, Any]],
    anchors: dict[str, Any],
    theme_to_chapter: dict[str, int],
    schemas_catalogue: dict[str, Any],
) -> list[dict[str, Any]]:
    """Construit les 5 annexes A–E avec leurs tables analytiques exactes sans troncature."""
    nodes = bundle["nodes"]
    relations = bundle["relations"]
    rel_types = {rt["type_id"]: rt for rt in bundle["relation_types"]}
    pivots = bundle.get("pivots") or {}
    node_by_id = {n["node_id"]: n for n in nodes}
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
            "representative_title": f"Annexe {acode} — {_clean_text(clean_atitle)}",
            "slug": ann_anchors[acode],
            "executive_summary": _clean_text(ann["executive_summary"]),
            "targeted_content_description": _clean_text(ann["targeted_content_description"]),
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
                    ids_set.update(th.get("identifiers_and_norms") or [])
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
                        "parts_present": ch["parts_present"],
                        "tomes_present": ch["tomes_present"],
                        "key_identifiers": sorted(ids_set),
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
                    "label": _clean_text(rt["label"]),
                    "count": counts.get(rt_id, 0),
                    "directionality": _clean_text(rt.get("directionality", "")),
                    "semantic_rule": _clean_text(rt.get("semantic_rule", "")),
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
                    "title": _clean_text(tn["title"]),
                    "domain_id": tn["domain_id"],
                    "chapter_number": theme_to_chapter.get(tn["node_id"]),
                    "chapter_slug": chap_anchors.get(theme_to_chapter.get(tn["node_id"], 0), ""),
                    "relation_degree": int(tn.get("relation_degree", 0)),
                    "occurrence_count": int(tn.get("occurrence_count", 0)),
                    "parts_present": tn.get("parts_present") or [],
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
                    "source_title": _clean_text(node_by_id.get(tr["source"], {}).get("title", "")),
                    "source_chapter_number": theme_to_chapter.get(tr["source"]),
                    "target_node_id": tr["target"],
                    "target_slug": node_by_id.get(tr["target"], {}).get("canonical_slug", tr["target"]),
                    "target_title": _clean_text(node_by_id.get(tr["target"], {}).get("title", "")),
                    "target_chapter_number": theme_to_chapter.get(tr["target"]),
                    "label": _clean_text(tr.get("label", "")),
                    "justification": _clean_text(tr.get("justification", "")),
                    "parts": tr.get("parts") or [],
                    "tomes": tr.get("tomes") or [],
                }
                for tr in tensions_raw
            ]

        elif acode == "C":
            entry["div_02"] = _clean_nested_strings(pivots.get("div_02") or {})
            entry["reconciliations"] = _clean_nested_strings(pivots.get("reconciliations") or [])
            entry["timeline"] = _build_consolidated_timeline(raw_pivots, pivots)

        elif acode == "D":
            unified_mat, matrix_distribution, matrix_totals = _build_unified_matrix(raw_pivots)
            raw_mat = raw_pivots.get("matrices") or {}
            exig_cre = raw_mat.get("exig_cre_ia_2026_v1_2") or {}
            t8_exec = raw_mat.get("tome8_executable") or {}
            prr_raw = raw_mat.get("prr_75") or {}
            prr_items = prr_raw.get("items") or []
            prr_blocking_by_grid = dict(Counter(x["grid"] for x in prr_items if x.get("is_blocking")))

            c40_counts = Counter(str(item.get("family", "")) for item in unified_mat if str(item.get("family", "")).startswith("C40"))
            c40_breakdown = {
                "total": sum(c40_counts.values()),
                "BLOQUANT": c40_counts.get("C40 (BLOQUANT)", 0),
                "OBLIGATOIRE": c40_counts.get("C40 (OBLIGATOIRE)", 0),
                "RECOMMANDE": c40_counts.get("C40 (RECOMMANDE)", 0),
            }

            entry["bilans_aq"] = pivots.get("bilans_aq") or {}
            entry["collection_metrics"] = pivots.get("collection_metrics") or {}
            entry["matrix_totals"] = matrix_totals
            entry["matrix_distribution"] = matrix_distribution
            entry["matrix_all"] = unified_mat
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

        elif acode == "E":
            ann_e_spec = schemas_catalogue.get("annexe_e") or {}
            s_stats = schemas_catalogue["summary_stats"]
            tc_cov = schemas_catalogue["tome_figures_coverage"]
            ch_out_by_num = {int(c["chapter_number"]): c for c in chapters_out}
            schema_anchors = anchors["schema_section_anchors"]
            exec_title_clean = _clean_text(
                global_shard["executive_summary"].get("title", "Sommaire exécutif global")
            )

            all_raw_schemas = list(schemas_catalogue["global_schemas"]) + list(schemas_catalogue["chapter_schemas"])
            catalogue_all: list[dict[str, Any]] = []
            for s_raw in all_raw_schemas:
                s_clean = _clean_schema_entry(s_raw)
                cnum = int(s_clean["chapter_number"])
                if cnum == 0:
                    s_clean["chapter_code"] = "GLOBAL"
                    s_clean["chapter_title"] = exec_title_clean
                    s_clean["chapter_slug"] = anchors["exec_anchor"]
                    s_clean["schemas_anchor"] = anchors["exec_panorama_anchor"]
                else:
                    ch_info = ch_out_by_num[cnum]
                    s_clean["chapter_code"] = ch_info["chapter_code"]
                    s_clean["chapter_title"] = ch_info["representative_title"]
                    s_clean["chapter_slug"] = ch_info["slug"]
                    s_clean["schemas_anchor"] = schema_anchors[cnum]
                catalogue_all.append(s_clean)

            domain_chapter_distribution: list[dict[str, Any]] = [
                {
                    "domain_id": "GLOBAL",
                    "domain_title": "Sommaire exécutif global",
                    "chapters": [0],
                    "families_count": 0,
                    "themes_count": len(
                        {
                            sl
                            for s in schemas_catalogue["global_schemas"]
                            for sl in s["themes_vulgarized"]
                        }
                    ),
                    "schemas_count": s_stats["by_domain"]["GLOBAL"]["schemas_count"],
                    "schema_ids": s_stats["by_domain"]["GLOBAL"]["schema_ids"],
                }
            ]
            for dom in sorted(bundle["domains"], key=lambda d: d["domain_id"]):
                did = dom["domain_id"]
                d_chs = [c for c in chapters_out if c["domain_id"] == did]
                d_fams = sum(len(c["targeted_content"]["families_and_themes"]) for c in d_chs)
                d_thms = sum(
                    len(f["themes_targeted"])
                    for c in d_chs
                    for f in c["targeted_content"]["families_and_themes"]
                )
                d_stat = s_stats["by_domain"][did]
                domain_chapter_distribution.append(
                    {
                        "domain_id": did,
                        "domain_title": _clean_text(dom["title"]),
                        "chapters": [int(c["chapter_number"]) for c in d_chs],
                        "families_count": d_fams,
                        "themes_count": d_thms,
                        "schemas_count": d_stat["schemas_count"],
                        "schema_ids": d_stat["schema_ids"],
                    }
                )

            entry["summary_stats"] = _clean_nested_strings(s_stats)
            entry["tome_figures_coverage"] = _clean_nested_strings(
                {k: v for k, v in tc_cov.items() if k != "figures_catalogue"}
            )
            entry["domain_chapter_distribution"] = domain_chapter_distribution
            entry["editorial_guidelines"] = [
                _clean_text(g) for g in (ann_e_spec.get("editorial_guidelines") or [])
            ]
            entry["catalogue_columns"] = [
                _clean_text(col) for col in (ann_e_spec.get("catalogue_columns") or [])
            ]
            entry["catalogue_all"] = catalogue_all
            entry["tome_inventory_summary"] = {
                "total_inventory_figures": tc_cov["total_inventory_figures"],
                "plantuml_svg_count": tc_cov["inventory_plantuml_svg"],
                "mermaid_png_count": tc_cov["inventory_mermaid_png"],
                "unique_linked_figures_count": tc_cov["unique_linked_figures_count"],
                "by_tome": _clean_nested_strings(tc_cov["by_tome"]),
                "figures": _clean_nested_strings(tc_cov["figures_catalogue"]),
            }

        annexes_out.append(entry)

    return annexes_out


def _build_dedup_interrelations(
    ch: dict[str, Any],
    ch_theme_ids: set[str],
    relations: list[dict[str, Any]],
    rel_types: dict[str, dict[str, Any]],
    rels_by_pair: dict[tuple[str, str], list[dict[str, Any]]],
    node_by_id: dict[str, dict[str, Any]],
    node_by_slug: dict[str, dict[str, Any]],
    theme_to_chapter: dict[str, int],
    chapters_by_num: dict[int, dict[str, Any]],
) -> list[dict[str, Any]]:
    """Fusionne et déduplique les interrelations par ``(direction, relation_type, target_chapter_number)``."""
    tc = ch["targeted_content"]
    raw_items: list[dict[str, Any]] = []

    for rel in tc.get("cross_chapter_interrelations", []):
        t_num = int(rel["target_chapter_number"])
        t_slug = rel.get("target_slug", "")
        direction = rel.get("direction", "sortante")
        rtype = rel.get("relation_type", "")
        tgt_node = node_by_slug.get(t_slug) or {}
        tgt_nid = tgt_node.get("node_id", "")

        local_slug = ""
        if tgt_nid:
            for local_tid in sorted(ch_theme_ids):
                pair = (local_tid, tgt_nid) if direction == "sortante" else (tgt_nid, local_tid)
                matched = [r for r in rels_by_pair.get(pair, []) if r["type"] == rtype] or rels_by_pair.get(pair, [])
                if matched:
                    local_slug = node_by_id[local_tid]["canonical_slug"]
                    break

        syn_txt = _clean_text(rel.get("synthesis", ""))
        # Nettoyer tout préfixe hétérogène ("Thème local `slug` — / :" ou "[slug]" / "[src → tgt]")
        m_tl = re.match(r"^Thème local\s+`?([^:—–\n]+?)`?\s*[:—–]\s*(.*)$", syn_txt)
        if m_tl:
            if not local_slug:
                cand = m_tl.group(1).strip()
                if cand in node_by_slug:
                    local_slug = cand
            syn_txt = m_tl.group(2).strip()
        m_br = re.match(r"^\[([a-z0-9-]+)(?:\s*[→↔-]\s*([a-z0-9-]+))?\]\s*(.*)$", syn_txt)
        if m_br:
            if not local_slug:
                c1, c2 = m_br.group(1), m_br.group(2)
                cand = c1 if direction == "sortante" or not c2 else c2
                if cand in node_by_slug:
                    local_slug = cand
            syn_txt = m_br.group(3).strip()
        if syn_txt and syn_txt[0].islower():
            syn_txt = syn_txt[0].upper() + syn_txt[1:]
        raw_items.append(
            {
                "direction": direction,
                "relation_type": rtype,
                "target_chapter_number": t_num,
                "target_slug": t_slug,
                "target_node_id": tgt_nid,
                "local_slug": local_slug,
                "synthesis": syn_txt,
            }
        )

    for mrel in relations:
        src, tgt = mrel["source"], mrel["target"]
        if src in ch_theme_ids and tgt not in ch_theme_ids:
            o_ch = theme_to_chapter.get(tgt)
            o_node = node_by_id.get(tgt)
            if o_ch and o_node:
                syn_m = _clean_text(f"{mrel['label']} — {mrel['justification']}")
                if syn_m and syn_m[0].islower():
                    syn_m = syn_m[0].upper() + syn_m[1:]
                raw_items.append(
                    {
                        "direction": "sortante",
                        "relation_type": mrel["type"],
                        "target_chapter_number": o_ch,
                        "target_slug": o_node["canonical_slug"],
                        "target_node_id": tgt,
                        "local_slug": node_by_id[src]["canonical_slug"],
                        "synthesis": syn_m,
                    }
                )
        elif tgt in ch_theme_ids and src not in ch_theme_ids:
            o_ch = theme_to_chapter.get(src)
            o_node = node_by_id.get(src)
            if o_ch and o_node:
                syn_m = _clean_text(f"{mrel['label']} — {mrel['justification']}")
                if syn_m and syn_m[0].islower():
                    syn_m = syn_m[0].upper() + syn_m[1:]
                raw_items.append(
                    {
                        "direction": "entrante",
                        "relation_type": mrel["type"],
                        "target_chapter_number": o_ch,
                        "target_slug": o_node["canonical_slug"],
                        "target_node_id": src,
                        "local_slug": node_by_id[tgt]["canonical_slug"],
                        "synthesis": syn_m,
                    }
                )

    grouped: dict[tuple[str, str, int], dict[str, Any]] = {}
    for item in raw_items:
        key = (item["direction"], item["relation_type"], item["target_chapter_number"])
        if key not in grouped:
            grouped[key] = {
                "direction": item["direction"],
                "relation_type": item["relation_type"],
                "target_chapter_number": item["target_chapter_number"],
                "target_slugs": [],
                "target_node_ids": [],
                "local_slugs": [],
                "syntheses": [],
                "_seen_prefixes": set(),
            }
        grp = grouped[key]
        if item["target_slug"] and item["target_slug"] not in grp["target_slugs"]:
            grp["target_slugs"].append(item["target_slug"])
        if item["target_node_id"] and item["target_node_id"] not in grp["target_node_ids"]:
            grp["target_node_ids"].append(item["target_node_id"])
        if item["local_slug"] and item["local_slug"] not in grp["local_slugs"]:
            grp["local_slugs"].append(item["local_slug"])
        syn = item["synthesis"]
        pref = re.sub(r"[^a-z0-9àâäéèêëîïôöùûüç]+", " ", syn.lower()).strip()[:32]
        body_part = re.split(r"\s*[:—]\s*", syn, maxsplit=1)[-1]
        body_key = re.sub(r"[^a-z0-9àâäéèêëîïôöùûüç]+", " ", body_part.lower()).strip()[:45]
        if syn and pref not in grp["_seen_prefixes"] and body_key not in grp["_seen_prefixes"]:
            grp["_seen_prefixes"].add(pref)
            if body_key:
                grp["_seen_prefixes"].add(body_key)
            grp["syntheses"].append(syn)

    inter_out: list[dict[str, Any]] = []
    for key in sorted(grouped, key=lambda k: (0 if k[0] == "sortante" else 1, k[2], k[1])):
        grp = grouped[key]
        direction, rtype, t_num = key
        fr_label = _clean_text(rel_types.get(rtype, {}).get("label", rtype))
        combined_syn = " ; ".join(grp["syntheses"][:2])
        inter_out.append(
            {
                "direction": direction,
                "relation_type": rtype,
                "target_chapter_number": t_num,
                "target_chapter_title": _clean_text(chapters_by_num[t_num]["representative_title"]),
                "target_slug": grp["target_slugs"][0] if grp["target_slugs"] else "",
                "target_slugs": grp["target_slugs"],
                "target_node_id": grp["target_node_ids"][0] if grp["target_node_ids"] else "",
                "local_slug": grp["local_slugs"][0] if grp["local_slugs"] else "",
                "local_slugs": grp["local_slugs"],
                "label": fr_label,
                "synthesis": combined_syn,
            }
        )

    return inter_out


def build_prd_web_payload(
    repo_root: Path,
    bundle: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Assemble le payload complet du PRD pour ``prd-web-data.json`` et la Vue 5 MindMap."""
    donnees_dir = repo_root / "Sources" / "Cartographie" / "donnees"
    if bundle is None:
        synthese_path = donnees_dir / "synthese-transversale.json"
        bundle_path = donnees_dir / "corpus-mindmap-data.json"
        chosen = synthese_path if synthese_path.is_file() else bundle_path
        if not chosen.is_file():
            raise FileNotFoundError(f"Graphe MindMap introuvable : {chosen}")
        bundle = dict(json.loads(chosen.read_text(encoding="utf-8")))
    else:
        bundle = dict(bundle)

    if not bundle.get("domains") or not bundle.get("relation_types"):
        schema_path = donnees_dir / "schema-cartographie.json"
        if schema_path.is_file():
            schema_cfg = json.loads(schema_path.read_text(encoding="utf-8"))
            if not bundle.get("domains"):
                bundle["domains"] = schema_cfg.get("domains", [])
            if not bundle.get("relation_types"):
                bundle["relation_types"] = schema_cfg.get("relation_types", [])

    pivots_path = donnees_dir / "pivots-concordance.json"
    raw_pivots = json.loads(pivots_path.read_text(encoding="utf-8")) if pivots_path.is_file() else {}
    if not bundle.get("pivots") and raw_pivots:
        import compiler_mindmap as _cm_mod  # noqa: E402
        bundle["pivots"] = _cm_mod.normalize_pivots(raw_pivots)

    cat_path = donnees_dir / "catalogue-schemas-prd.json"
    if cat_path.is_file():
        schemas_catalogue = json.loads(cat_path.read_text(encoding="utf-8"))
    else:
        schemas_catalogue = ccs.build_catalogue_schemas_payload(repo_root, bundle=bundle)

    chapter_schemas_by_num: dict[int, list[dict[str, Any]]] = {}
    for s_item in schemas_catalogue["chapter_schemas"]:
        chapter_schemas_by_num.setdefault(int(s_item["chapter_number"]), []).append(s_item)

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
    prd_md_path = repo_root / "Sources" / "Compendium" / "prd.md"
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
        "prd_title": _clean_text(global_shard["prd_title"]),
        "prd_subtitle": _clean_text(global_shard["prd_subtitle"]),
        "toc_representative_title": _clean_text(global_shard["toc_representative_title"]),
        "toc_intro_note": _clean_text(global_shard.get("toc_intro_note", "")),
        "version": gmeta.get("version", "1.0.0"),
        "date": gmeta.get("date", "2026-11-24"),
        "status": _clean_text(gmeta.get("status", "Référentiel d'exigences produit et architecture (non-avis)")),
        "source_md": "../../Sources/Compendium/prd.md",
        "line_count": line_count,
        "word_count": word_count,
        "heading_count": heading_count,
        "domains_count": 12,
        "chapters_count": len(chapters_raw),
        "families_count": sum(len(c["targeted_content"]["families_and_themes"]) for c in chapters_raw),
        "themes_count": len(theme_to_chapter),
        "relations_count": len(relations),
        "annexes_count": len(global_shard["annexes"]),
        "schemas_count": schemas_catalogue["summary_stats"]["total_schemas"],
        "tome_figures_count": schemas_catalogue["tome_figures_coverage"]["total_inventory_figures"],
    }

    exec_raw = global_shard["executive_summary"]
    exec_sections = []
    for idx, sec in enumerate(exec_raw["sections"], 1):
        body_clean = _clean_text(sec["body"])
        paragraphs, kpi_table = _parse_markdown_section_body(body_clean)
        exec_sections.append(
            {
                "id": f"exec-{idx:02d}",
                "slug": anchors["exec_section_anchors"][idx - 1],
                "heading": _clean_text(sec["heading"]),
                "body_md": body_clean,
                "paragraphs": paragraphs,
                "kpi_table": kpi_table,
            }
        )
    executive_summary = {
        "title": _clean_text(exec_raw.get("title", "Sommaire exécutif global")),
        "slug": anchors["exec_anchor"],
        "lead": _clean_text(exec_raw["lead"]),
        "sections": exec_sections,
        "panorama_anchor": anchors["exec_panorama_anchor"],
        "vulgarization_schemas": [
            _clean_schema_entry(s) for s in schemas_catalogue["global_schemas"]
        ],
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
                "domain_title": _clean_text(dom_meta["title"]),
                "key_identifiers": dom_meta.get("key_identifiers") or [],
                "representative_part_title": _clean_text(clean_ptitle),
                "part_summary": _clean_text(p["part_summary"]),
                "chapter_numbers": [int(c) for c in p["chapter_numbers"]],
                "slug": anchors["part_anchors"][dom_id],
            }
        )

    rels_by_pair: dict[tuple[str, str], list[dict[str, Any]]] = {}
    for mrel in relations:
        rels_by_pair.setdefault((mrel["source"], mrel["target"]), []).append(mrel)

    comp_spans = cp.build_compendium_heading_spans(repo_root)
    mod_line_counts: dict[str, int] = {}
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
                    {_clean_text(x) for x in ((th.get("identifiers_and_norms") or []) + (mm_node.get("identifiers") or [])) if str(x).strip()}
                )
                direct_anchors = [
                    {
                        "part_id": occ.get("part_id") or occ.get("tome_id", ""),
                        "tome_id": occ.get("part_id") or occ.get("tome_id", ""),
                        "compendium_unit_id": occ.get("compendium_unit_id") or "",
                        "file": occ["file"],
                        "source_file": occ.get("source_file") or "",
                        "line_start": int(occ["line_start"]),
                        "line_end": int(occ["line_end"]),
                        "label": (
                            f"{occ.get('part_id') or occ['tome_id']} · "
                            f"{occ.get('compendium_unit_id', '')} · L{occ['line_start']}–L{occ['line_end']}"
                        ).replace(" ·  · ", " · "),
                    }
                    for occ in sorted(
                        mm_node.get("occurrences") or [],
                        key=lambda o: (TOME_RANK.get(o.get("part_id") or o.get("tome_id", ""), 99), int(o["line_start"])),
                    )
                ]
                themes_out.append(
                    {
                        "theme_node_id": tid,
                        "canonical_slug": th["canonical_slug"],
                        "theme_title": _clean_text(th["theme_title"]),
                        "content_specification": _clean_text(th["content_specification"]),
                        "autonomy_levels": mm_node.get("autonomy_levels") or [],
                        "roles": mm_node.get("roles") or [],
                        "horizon": mm_node.get("horizon") or "",
                        "horizons": mm_node.get("horizons") or [],
                        "owner_chapter": mm_node.get("owner_chapter") or f"ch{cnum:02d}",
                        "parts_present": mm_node.get("parts_present") or [],
                        "units_present": mm_node.get("units_present") or [],
                        "tomes_present": mm_node.get("tomes_present") or [],
                        "compendium_schemas": mm_node.get("compendium_schemas") or [],
                        "glossary_terms": mm_node.get("glossary_terms") or [],
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
                    "family_title": _clean_text(fam["family_title"]),
                    "slug": anchors["family_anchors"][fam["family_node_id"]],
                    "family_overview": _clean_text(fam["family_overview"]),
                    "themes_targeted": themes_out,
                }
            )

        inter_out = _build_dedup_interrelations(
            ch,
            ch_theme_ids,
            relations,
            rel_types,
            rels_by_pair,
            node_by_id,
            node_by_slug,
            theme_to_chapter,
            chapters_by_num,
        )

        by_tome_line: dict[tuple[str, str, int], dict[str, Any]] = {}
        for anc in tc.get("corpus_anchors", []):
            ln, ref_txt = cp.resolve_corpus_anchor(anc, repo_root, comp_spans, mod_line_counts)
            pid = str(anc.get("part_id") or anc.get("section_id") or anc.get("tome_id") or "")
            uid_anc = str(anc.get("unit_id") or "")
            k = (pid, anc["file"], ln or 0)
            if k not in by_tome_line or len(ref_txt) > len(by_tome_line[k]["reference"]):
                by_tome_line[k] = {
                    "part_id": pid,
                    "tome_id": pid,
                    "unit_id": uid_anc,
                    "file": anc["file"],
                    "line_start": ln,
                    "reference": ref_txt,
                }
        corpus_anchors_out = sorted(
            by_tome_line.values(),
            key=lambda a: (TOME_RANK.get(a["part_id"], 99), a["line_start"] or 0, a["reference"]),
        )

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
                "subdomain_title": _clean_text(sub_node["title"]),
                "representative_title": _clean_text(clean_chtitle),
                "slug": anchors["chapter_anchors"][cnum],
                "executive_summary": _clean_text(ch["executive_summary"]),
                "owner_chapter": sub_node.get("owner_chapter") or f"ch{cnum:02d}",
                "parts_present": sub_node.get("parts_present") or [],
                "units_present": sub_node.get("units_present") or [],
                "tomes_present": sub_node.get("tomes_present") or [],
                "autonomy_levels": sub_node.get("autonomy_levels") or [],
                "roles": sub_node.get("roles") or [],
                "horizons": sub_node.get("horizons") or [],
                "schemas_anchor": anchors["schema_section_anchors"][cnum],
                "vulgarization_schemas": [
                    _clean_schema_entry(s) for s in chapter_schemas_by_num.get(cnum, [])
                ],
                "targeted_content": {
                    "scope_and_objectives": _clean_text(tc["scope_and_objectives"]),
                    "key_requirements_and_objectives": [_clean_text(x) for x in tc["key_requirements_and_objectives"]],
                    "families_and_themes": fams_out,
                    "deliverables_and_verification": [_clean_text(x) for x in tc["deliverables_and_verification"]],
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
        schemas_catalogue,
    )

    node_id_to_prd: dict[str, dict[str, Any]] = {}
    for n in nodes:
        nkind = n.get("node_kind")
        nid = n["node_id"]
        if nkind == "root":
            continue
        dom_id = n["domain_id"]
        if nkind == "domain":
            node_id_to_prd[nid] = {
                "kind": "domain",
                "domain_id": dom_id,
                "chapter_number": None,
                "family_node_id": None,
                "theme_node_id": None,
                "section_id": f"part-{dom_id}",
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
                "section_id": f"thm-{nid}",
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

    ann_e = next(a for a in annexes_out if a["annexe_code"] == "E")
    tc_cov = schemas_catalogue["tome_figures_coverage"]
    vulgarization_summary = {
        "summary_stats": _clean_nested_strings(schemas_catalogue["summary_stats"]),
        "tome_figures_totals": _clean_nested_strings(
            {k: v for k, v in tc_cov.items() if k not in ("by_tome", "figures_catalogue")}
        ),
        "tome_figures_coverage_by_tome": _clean_nested_strings(tc_cov["by_tome"]),
        "schemas_overview": [
            {
                "schema_id": item["schema_id"],
                "chapter_number": item["chapter_number"],
                "chapter_code": item["chapter_code"],
                "domain_id": item["domain_id"],
                "title": item["title"],
                "visual_archetype": item["visual_archetype"],
                "recommended_notation": item["recommended_notation"],
                "reuse_status": item["reuse_status"],
                "target_audiences": item["target_audiences"],
                "families_covered": item["families_covered"],
                "linked_tome_figures_count": len(item["linked_tome_figures"]),
                "compendium_rendered_path": item.get("compendium_rendered_path", ""),
                "compendium_source_path": item.get("compendium_source_path", ""),
                "compendium_md_line": item.get("compendium_md_line"),
                "compendium_unit": item.get("compendium_unit", ""),
                "chapter_slug": item["chapter_slug"],
                "schemas_anchor": item["schemas_anchor"],
            }
            for item in ann_e["catalogue_all"]
        ],
    }

    cm_meta = raw_pivots.get("collection_metrics") or {}
    comp_bilans = (raw_pivots.get("bilans_aq_wyvern_et_statut_f") or {}).get("compendium_g0_g5") or {}
    compendium_meta = {
        "title": _clean_text(cm_meta.get("compendium_title", "Compendium de l'entreprise agentique")),
        "pdf_file": "Compendium/Compendium.pdf",
        "md_file": "Compendium/Compendium.md",
        "pdf_pages": int(cm_meta.get("compendium_pdf_pages", 852)),
        "pdf_bytes": int(cm_meta.get("compendium_pdf_bytes", 0)),
        "words": int(cm_meta.get("compendium_md_words", 246518)),
        "lines": int(cm_meta.get("compendium_md_lines", 8532)),
        "editorial_units": int(cm_meta.get("compendium_units", 42)),
        "sections": int(cm_meta.get("compendium_sections", 15)),
        "compiled_schemas": int(cm_meta.get("compendium_schemas", 115)),
        "glossary_terms_count": int(cm_meta.get("glossary_terms", 56)),
        "lplus_sources_count": int(cm_meta.get("sources_l_plus", 135)),
        "statut_f_count": int(cm_meta.get("statut_f_excluded", 27)),
        "synced_excerpts_count": int(cm_meta.get("ca_g0_sync_excerpts", 14)),
        "wyvern_g2_units": int(cm_meta.get("wyvern_g2_units", 37)),
        "freeze_date": str(cm_meta.get("freeze_date", "2026-12-02")),
    }
    raw_gloss = (raw_pivots.get("glossaire_pivot") or {}).get("glossaire_compendium_56") or []
    glossary_out = _clean_nested_strings(raw_gloss)
    socle_probatoire = {
        "freeze_date": compendium_meta["freeze_date"],
        "sources_l_plus_count": compendium_meta["lplus_sources_count"],
        "metadata_only_pct": comp_bilans.get("metadata_only_pct", 0.0),
        "statut_f_count": compendium_meta["statut_f_count"],
        "ca_g0_sync_count": compendium_meta["synced_excerpts_count"],
        "wyvern_g2_units": compendium_meta["wyvern_g2_units"],
        "faits_empiriques": _clean_nested_strings(raw_pivots.get("faits_empiriques_16") or comp_bilans.get("faits_empiriques_16") or []),
        "specifications_lplus": _clean_nested_strings(raw_pivots.get("specifications_lplus_57") or comp_bilans.get("specifications_lplus_57") or []),
        "statut_f_excluded": _clean_nested_strings(raw_pivots.get("statut_f_exclus_27") or []),
        "ca_g0_sync_catalog": _clean_nested_strings(comp_bilans.get("ca_g0_sync_catalog") or []),
        "wyvern_g2_unites": _clean_nested_strings(comp_bilans.get("wyvern_g2_unites") or []),
        "rapports_g0": _clean_nested_strings(comp_bilans.get("rapports_g0") or {}),
    }

    payload = {
        "schema_version": "2.0.0",
        "lang": "fr-CA",
        "generator": "Sources/Cartographie/outils/preparer_donnees_prd_web.py",
        "meta": meta,
        "compendium_meta": compendium_meta,
        "glossary": glossary_out,
        "socle_probatoire": socle_probatoire,
        "executive_summary": executive_summary,
        "parties": parties_out,
        "chapters": chapters_out,
        "annexes": annexes_out,
        "vulgarization_summary": vulgarization_summary,
        "lookup": {
            "node_id_to_prd": node_id_to_prd,
            "slug_to_chapter": slug_to_chapter,
            "domain_to_part": domain_to_part,
            "unit_id_to_chapter": unit_id_to_chapter,
        },
    }

    # Contrôles inconditionnels de parité (actifs même sous python -O)
    _check(len(parties_out) == 12, f"Nombre de parties invalide : {len(parties_out)}")
    _check(len(chapters_out) == 36, f"Nombre de chapitres invalide : {len(chapters_out)}")
    _check(meta["families_count"] == 71, f"Nombre de familles invalide : {meta['families_count']}")
    _check(meta["themes_count"] == 260, f"Nombre de thèmes invalide : {meta['themes_count']}")
    _check(meta["annexes_count"] == 5, f"meta.annexes_count invalide : {meta['annexes_count']}")
    _check(meta["schemas_count"] == 115, f"meta.schemas_count invalide : {meta['schemas_count']}")
    _check(meta["tome_figures_count"] == 319, f"meta.tome_figures_count invalide : {meta['tome_figures_count']}")
    _check(len(annexes_out) == 5, f"Nombre d'annexes invalide : {len(annexes_out)}")
    _check([a["annexe_code"] for a in annexes_out] == ["A", "B", "C", "D", "E"], "Ordre annexes != A..E")
    _check(len(executive_summary["sections"]) == 5, "Sommaire exécutif != 5 sections")
    _check(bool(executive_summary.get("panorama_anchor")), "panorama_anchor manquant")
    _check(len(executive_summary["vulgarization_schemas"]) == 4, "Schémas globaux != 4")
    _check(executive_summary["sections"][3]["kpi_table"] is not None, "Tableau KPI/SLO manquant")
    _check(len(executive_summary["sections"][3]["kpi_table"]["rows"]) == 8, "Tableau KPI/SLO != 8 lignes")
    _check(
        all(bool(c.get("schemas_anchor")) and len(c.get("vulgarization_schemas") or []) >= 1 for c in chapters_out),
        "Au moins un chapitre n'a pas schemas_anchor ou vulgarization_schemas non vide",
    )
    _check(
        sum(len(c["vulgarization_schemas"]) for c in chapters_out) == 111,
        "Total schémas de chapitres != 111",
    )
    _check(len(ann_e["catalogue_all"]) == 115, f"Annexe E catalogue_all != 115 : {len(ann_e['catalogue_all'])}")
    _check(
        len(ann_e["tome_inventory_summary"]["figures"]) == 319,
        f"Annexe E tome_inventory_summary != 319 : {len(ann_e['tome_inventory_summary']['figures'])}",
    )
    _check(ann_e["summary_stats"]["chapters_covered_count"] == 36, "Annexe E chapters_covered != 36")
    _check(ann_e["summary_stats"]["families_covered_count"] == 71, "Annexe E families_covered != 71")

    ann_b = next(a for a in annexes_out if a["annexe_code"] == "B")
    expected_tensions = sum(1 for r in relations if r["type"] == "tension_arbitrage")
    _check(sum(rt["count"] for rt in ann_b["relation_types_stats"]) == len(relations), "Total relations Annexe B incohérent")
    _check(len(ann_b["tensions"]) == expected_tensions, f"Tensions d'arbitrage != {expected_tensions} : {len(ann_b['tensions'])}")
    _check(len(ann_b["top_hubs"]) == 20, "Top hubs != 20")

    ann_c = next(a for a in annexes_out if a["annexe_code"] == "C")
    _check(len(ann_c["reconciliations"]) == 5, "Réconciliations DISC != 5")
    _check(len(ann_c["timeline"]) >= 77, f"Chronologie consolidée insuffisante : {len(ann_c['timeline'])}")
    _check(
        all("((" not in ev["date"] and "))" not in ev["date"] for ev in ann_c["timeline"]),
        "Parenthèses doubles détectées dans la chronologie",
    )

    ann_d = next(a for a in annexes_out if a["annexe_code"] == "D")
    mat_ids = [x["id"] for x in ann_d["matrix_all"]]
    _check(len(mat_ids) == len(set(mat_ids)) == 237, f"Doublons ou cardinal matrice invalide : {len(mat_ids)} / {len(set(mat_ids))}")
    _check(sum(d["count"] for d in ann_d["matrix_distribution"]) == 237, "Distribution matrice != 237")
    _check(
        ann_d["blueprints_c40"]["c40_breakdown"] == {"total": 40, "BLOQUANT": 18, "OBLIGATOIRE": 15, "RECOMMANDE": 7},
        f"Ventilation C01–C40 inattendue : {ann_d['blueprints_c40']['c40_breakdown']}",
    )
    _check(len(node_id_to_prd) == 379, f"lookup node_id_to_prd={len(node_id_to_prd)} != 379")

    return payload


def main() -> int:
    """Point d'entrée CLI générant ``Cartographie/donnees/prd-web-data.json``."""
    parser = argparse.ArgumentParser(description="Prépare prd-web-data.json depuis le MindMap et les shards PRD.")
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
        help="Chemin de sortie JSON (défaut : Sources/Cartographie/donnees/prd-web-data.json).",
    )
    args = parser.parse_args()

    repo_root = args.repo_root.resolve()
    payload = build_prd_web_payload(repo_root)
    out_path = args.output or (repo_root / "Sources" / "Cartographie" / "donnees" / "prd-web-data.json")
    out_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")

    m = payload["meta"]
    ann_c = next(a for a in payload["annexes"] if a["annexe_code"] == "C")
    ann_d = next(a for a in payload["annexes"] if a["annexe_code"] == "D")
    print(
        f"Données web PRD générées -> {out_path} : {m['domains_count']} domaines, "
        f"{m['chapters_count']} chapitres, {m['families_count']} familles, {m['themes_count']} thèmes, "
        f"{m['relations_count']} relations, {m['annexes_count']} annexes, {m['schemas_count']} schémas "
        f"({m['tome_figures_count']} figures Tomes), {len(ann_c['timeline'])} jalons chronologiques, "
        f"{len(ann_d['matrix_all'])} entrées matrice uniques, {len(payload['lookup']['node_id_to_prd'])} nœuds indexés"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
