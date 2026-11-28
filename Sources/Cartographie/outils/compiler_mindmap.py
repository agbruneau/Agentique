#!/usr/bin/env python3
"""Compilateur du bundle de données et de la MindMap HTML autonome du Compendium Agentique.

Fusionne :
- ``Sources/Cartographie/donnees/schema-cartographie.json``
- ``Sources/Cartographie/donnees/structure-integrale.json``
- ``Sources/Cartographie/donnees/pivots-concordance.json``
- ``Sources/Cartographie/donnees/synthese-transversale.json``
- ``Sources/Cartographie/outils/template_mindmap.html``

Produit :
- ``Sources/Cartographie/donnees/corpus-mindmap-data.json``
- ``Sources/Cartographie/MindMap - Cartographie thématique du Compendium.html``
"""

from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timezone
import json
from pathlib import Path
import re
import sys
from typing import Any, Callable

TOOLS_DIR = Path(__file__).resolve().parent
if str(TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(TOOLS_DIR))

PAGE_TITLE = "MindMap — Interopérabilité et automatisation agentique des systèmes d'entreprise (Compendium)"
TOME_ORDER: dict[str, int] = {
    "R": 0, "LIM": 1, "P01": 2, "P02": 3, "P03": 4, "P04": 5, "P05": 6,
    "P06": 7, "P07": 8, "P08": 9, "P09": 10, "P10": 11, "P11": 12, "P12": 13, "ANN": 14,
    "T1": 21, "T2": 22, "T3": 23, "T4": 24, "T5": 25, "T6": 26, "T7": 27, "T8": 28,
}

TOME_RANK: dict[str, int] = dict(TOME_ORDER)

# Correspondance entre les 6 repères généraux README et les clés canoniques L+
README_TO_CANONICAL_KEYS: dict[str, list[str]] = {
    "Depuis sept. 2023": ["2026-LOI25-ART12-1"],
    "Depuis août 2026": ["2026-08-02-EU-AI-ACT-ART50"],
    "Mars 2027 → Mars 2029": ["2027-03-15-TLS-100J", "2029-03-15-TLS-47J"],
    "1er mai 2027": ["2027-05-01-BSIF-E23-AMF"],
    "2027–2028": ["2027-12-02-EU-AI-ACT-ANNEXE-III", "2028-08-02-EU-AI-ACT-ANNEXE-I"],
    "2030–2035": ["2030-2035-G7-PQC-FINANCE"],
}


def map_outside_inline_code(text: str, transform: Callable[[str], str]) -> str:
    """Applique ``transform`` uniquement hors spans CommonMark `` `...` ``."""
    out: list[str] = []
    n = len(text)
    i = 0
    plain_start = 0
    while i < n:
        if text[i] == "`":
            run_end = i
            while run_end < n and text[run_end] == "`":
                run_end += 1
            tick_len = run_end - i
            close_pos = run_end
            matched_end = -1
            while close_pos < n:
                if text[close_pos] == "`":
                    c_end = close_pos
                    while c_end < n and text[c_end] == "`":
                        c_end += 1
                    if c_end - close_pos == tick_len:
                        matched_end = c_end
                        break
                    close_pos = c_end
                else:
                    close_pos += 1
            if matched_end != -1:
                if i > plain_start:
                    out.append(transform(text[plain_start:i]))
                out.append(text[i:matched_end])
                i = matched_end
                plain_start = i
                continue
            i = run_end
        else:
            i += 1
    if plain_start < n:
        out.append(transform(text[plain_start:]))
    return "".join(out)


def clean_dapp_label(raw: str) -> str:
    """Aplatit les libellés DAPP à parenthèses imbriquées (``A (B (C))`` -> ``A — B (C)``)."""
    txt = str(raw or "").strip()
    m = re.match(r"^([^()]+?)\s*\(([^()]+?)\s*\(([^()]+)\)\s*\)\s*$", txt)
    if m:
        outer, mid, inner = m.group(1).strip(), m.group(2).strip(), m.group(3).strip()
        return f"{outer} — {mid} ({inner.replace(' — ', ' : ')})"
    return txt


def clean_prose_typography(text: str) -> str:
    """Normalise les flèches ASCII, plages ``Lxxx–Lyyy``, ``\\$`` et accents hors code."""
    raw = str(text or "").replace(r"\$", "$")

    def _fix_plain(seg: str) -> str:
        seg = seg.replace("<->", "↔").replace("->", "→")
        seg = re.sub(r"\bL(\d+)-L?(\d+)\b", r"L\1–L\2", seg)
        seg = seg.replace("(reglementation)", "(réglementation)").replace("(marche)", "(marché)")
        return seg

    return map_outside_inline_code(raw, _fix_plain)


def timeline_sort_key(date_str: str) -> tuple[int, int, int, int, str]:
    """Clé de tri chronologique croissante (``2018``..``2035``)."""
    s = str(date_str or "").strip()
    m_iso = re.match(r"^(\d{4})-(\d{2})(?:-(\d{2}))?$", s)
    if m_iso:
        return (int(m_iso.group(1)), int(m_iso.group(2)), int(m_iso.group(3) or 2), 0, s)
    if s.startswith("Immédiat"):
        return (2026, 12, 3, 1, s)
    if "9 mois" in s:
        return (2027, 9, 2, 1, s)
    if s.startswith("Fin 2027"):
        return (2027, 12, 31, 1, s)
    if s == "2027–2028":
        return (2027, 12, 31, 2, s)
    if s.startswith("Fin 2028"):
        return (2028, 12, 31, 1, s)
    if s.startswith("2028–2029"):
        return (2028, 12, 31, 2, s)
    if s.startswith("Mars 2027"):
        return (2027, 3, 15, 1, s)
    if s.startswith("2030–2032"):
        return (2030, 12, 31, 1, s)
    if s == "2030–2035":
        return (2030, 12, 31, 2, s)
    if s.startswith("2033–2035"):
        return (2033, 12, 31, 1, s)
    m_yr = re.search(r"(\d{4})", s)
    if m_yr:
        return (int(m_yr.group(1)), 12, 31, 3, s)
    return (9999, 12, 31, 9, s)


def _norm_timeline_date(raw_date: str) -> str:
    d = clean_dapp_label(clean_prose_typography(raw_date)).strip()
    aliases = {
        "Depuis sept. 2023": "2023-09-22",
        "Depuis août 2026": "2026-08",
        "1er mai 2027": "2027-05-01",
    }
    return aliases.get(d, d)


def _merge_unique_phrases(parts: list[str]) -> str:
    cleaned: list[str] = []
    seen_norm: set[str] = set()
    for p in parts:
        val = p.strip().rstrip(".")
        if not val:
            continue
        norm = re.sub(r"\s+", " ", val.lower())
        if norm in seen_norm:
            continue
        # Évite de dupliquer un libellé court déjà inclus à l'identique dans un autre
        if any(norm == other or (len(norm) > 25 and norm in other) for other in seen_norm):
            continue
        seen_norm.add(norm)
        cleaned.append(val)
    if not cleaned:
        return ""
    joined = " ; ".join(cleaned)
    return joined if joined.endswith(".") else f"{joined}."


def deduplicate_and_sort_timeline(entries: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Fusionne les doublons de date, supprime ``\\$``/doubles parenthèses et trie ``2018→2035``."""
    grouped: dict[str, dict[str, Any]] = {}
    for ev in entries:
        ndate = _norm_timeline_date(ev.get("date", ""))
        cadre = clean_dapp_label(clean_prose_typography(ev.get("cadre", ""))).strip()
        impact = clean_prose_typography(ev.get("impact", "")).strip()
        tomes = [str(t) for t in (ev.get("tomes") or []) if t]
        if ndate not in grouped:
            grouped[ndate] = {
                "date": ndate,
                "cadres": [],
                "impacts": [],
                "tomes": set(),
                "file": ev.get("file", ""),
                "line_start": ev.get("line_start", 1),
                "source_groups": [],
            }
        bucket = grouped[ndate]
        if cadre and cadre not in bucket["cadres"]:
            bucket["cadres"].append(cadre)
        if impact and impact not in bucket["impacts"]:
            bucket["impacts"].append(impact)
        bucket["tomes"].update(tomes)
        sg = ev.get("source_group", "")
        if sg and sg not in bucket["source_groups"]:
            bucket["source_groups"].append(sg)
        if not bucket["file"] and ev.get("file"):
            bucket["file"] = ev.get("file", "")
            bucket["line_start"] = ev.get("line_start", 1)

    result: list[dict[str, Any]] = []
    for ndate in sorted(grouped.keys(), key=timeline_sort_key):
        b = grouped[ndate]
        cadre_str = " ; ".join(b["cadres"]) if len(b["cadres"]) <= 1 else " ; ".join(
            c for i, c in enumerate(b["cadres"])
            if not any(c.lower() in other.lower() for j, other in enumerate(b["cadres"]) if i != j and len(other) > len(c))
        )
        if not cadre_str and b["cadres"]:
            cadre_str = b["cadres"][0]
        result.append(
            {
                "date": ndate,
                "cadre": cadre_str,
                "impact": _merge_unique_phrases(b["impacts"]),
                "tomes": sorted(b["tomes"], key=lambda t: (TOME_ORDER.get(t, 99), t)),
                "file": b["file"],
                "line_start": b["line_start"],
                "source_group": ", ".join(b["source_groups"]),
            }
        )
    return result


def escape_json_for_script(json_str: str) -> str:
    """Échappe une chaîne JSON pour injection sûre dans un bloc ``<script>`` HTML.

    - ``</`` -> ``<\\/`` (évite toute fermeture prématurée de ``</script>``)
    - ``<!--`` -> ``\\u003c!--`` (évite l'ouverture de commentaire HTML)
    - U+2028 / U+2029 -> ``\\u2028`` / ``\\u2029`` (séparateurs de ligne JS)
    """
    return (
        json_str.replace("</", "<\\/")
        .replace("<!--", "\\u003c!--")
        .replace("\u2028", "\\u2028")
        .replace("\u2029", "\\u2029")
    )


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

    return map_outside_inline_code(s, _clean_outside_code)


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
                "pdf_page": anc.get("pdf_page"),
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
            if not entry.get("pdf_page") and anc.get("pdf_page"):
                entry["pdf_page"] = anc.get("pdf_page")
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
            "pdf_page": anc.get("pdf_page"),
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
                "pdf_page": 17,
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
                "pdf_page": item.get("pdf_page"),
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
                "pdf_page": pal.get("pdf_page"),
                "source_group": "Trajectoire DAPP (Ch. 31 / Annexe C)",
                "_tier": 1,
            }
        )

    events.sort(key=lambda e: _timeline_sort_key(e["date"], e.pop("_tier"), e["cadre"]))
    return events


def _flatten_struct_for_lookup(structure: dict[str, Any] | None) -> list[dict[str, Any]]:
    """Aplatit les nœuds structurels de ``Compendium/Compendium.md`` pour le raccordement ligne -> unité."""
    if not structure:
        return []
    out: list[dict[str, Any]] = []

    def walk(node: dict[str, Any]) -> None:
        out.append(node)
        for ch in node.get("children") or []:
            walk(ch)

    for f in structure.get("files") or []:
        if f.get("tome_id") == "R":
            continue
        for root in f.get("tree") or []:
            walk(root)
    return out


def _enrich_matrix_compendium_anchors(
    unified: list[dict[str, Any]],
    comp_lines: list[str] | None,
    structure: dict[str, Any] | None,
    pdf_index: Any | None,
) -> None:
    """Enrichit les 237 entrées de la matrice unifiée avec leur ancrage exact dans le Compendium."""
    if not comp_lines:
        return
    from extraire_pivots_compendium import _compute_compendium_unit_spans, _find_line_in_compendium  # noqa: E402

    unit_spans = _compute_compendium_unit_spans(comp_lines)
    struct_flat = _flatten_struct_for_lookup(structure)

    priority_by_prefix: tuple[tuple[str, list[str]], ...] = (
        ("5 SBB", ["ch35", "annexe-d", "ch06"]),
        ("PRR-75", ["ch34", "annexe-d", "ch35"]),
        ("C40", ["ch29", "ch35", "annexe-d"]),
        ("CAP", ["ch06", "annexe-d", "ch32"]),
        ("PEX", ["ch28", "annexe-d"]),
        ("EXIG", ["ch34", "annexe-d", "ch35"]),
        ("ADR_TEMPLATE", ["ch35", "ch34", "annexe-d"]),
        ("CRE-IA", ["ch34", "annexe-d"]),
    )

    body_start = unit_spans.get("00-liminaire", (74, len(comp_lines)))[0]
    body_span = (body_start, len(comp_lines))

    for entry in unified:
        eid = str(entry.get("id") or "")
        fam = str(entry.get("family") or "")
        pref_units = ["annexe-d", "ch34", "ch35"]
        for fam_pref, ulist in priority_by_prefix:
            if fam.startswith(fam_pref):
                pref_units = ulist
                break
        pref_spans = [unit_spans[u] for u in pref_units if u in unit_spans]
        pref_spans.append(body_span)

        clean_eid = eid.rstrip("-")
        needles = [eid] if eid == clean_eid else [eid, clean_eid]
        if fam.startswith("5 SBB") and entry.get("module"):
            needles.append(str(entry["module"]).split()[0])
        line_no = _find_line_in_compendium(comp_lines, needles, pref_spans)

        # Résolution de l'unité structurelle la plus profonde contenant line_no
        best_struct = None
        for sn in struct_flat:
            if int(sn.get("line_start", 0)) <= line_no <= int(sn.get("line_end", 0)):
                if best_struct is None or int(sn.get("level", 0)) >= int(best_struct.get("level", 0)):
                    best_struct = sn

        cid = best_struct.get("compendium_unit_id") if best_struct else None
        if not cid:
            for u_name, (u_lo, u_hi) in unit_spans.items():
                if u_lo <= line_no <= u_hi:
                    cid = u_name
                    break

        entry["compendium_unit_id"] = cid or "annexe-d"
        entry["struct_unit_id"] = best_struct.get("unit_id") if best_struct else None
        entry["compendium_line_start"] = line_no
        entry["pdf_page"] = pdf_index.resolve_line_page(line_no, needles) if pdf_index is not None else None


def _build_unified_matrix(
    raw_pivots: dict[str, Any],
    *,
    comp_lines: list[str] | None = None,
    structure: dict[str, Any] | None = None,
    pdf_index: Any | None = None,
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

    _enrich_matrix_compendium_anchors(unified, comp_lines, structure, pdf_index)

    summary_counts = {
        "unique_entries": len(unified),
        "tome8_executable_tests": len(m95),
        "shared_ids_merged": len(m95) + 5 + len(prr.get("items") or []) + len(raw_mat.get("cap_52") or []) + len(raw_mat.get("pex_24") or []) + len(exig_meta.get("familles") or []) - len(unified),
    }
    return unified, matrix_distribution, summary_counts


def normalize_pivots(
    raw_pivots: dict[str, Any],
    *,
    comp_lines: list[str] | None = None,
    structure: dict[str, Any] | None = None,
    pdf_index: Any | None = None,
) -> dict[str, Any]:
    """Normalise les pivots de concordance pour les sous-onglets de la Vue 4."""
    disc_block = raw_pivots.get("discordances_resolues") or {}
    raw_div02 = disc_block.get("div_02_tome_5") or {}
    div_02 = None
    if raw_div02:
        div_02 = {
            "id": raw_div02.get("id", "DIV-02"),
            "title": clean_prose_typography(raw_div02.get("objet", "Fermeture de DIV-02")),
            "statut": raw_div02.get("statut", "Fermée"),
            "resolution": clean_prose_typography(raw_div02.get("source", "")),
            "rectifications": [clean_prose_typography(r) for r in raw_div02.get("trois_rectifications", [])],
            "coquilles": [clean_prose_typography(c) for c in raw_div02.get("quatre_coquilles_cad26_v1_1_rectifiees", [])],
            "bilan_chiffre": raw_div02.get("bilan_chiffre", {}),
            "file": raw_div02.get("compendium_file") or "Compendium/Compendium.md",
            "line_start": int(raw_div02.get("compendium_line_start") or 108),
            "pdf_page": raw_div02.get("compendium_pdf_page"),
            "annexe_c_line": raw_div02.get("compendium_annexe_c_line"),
            "annexe_c_pdf_page": raw_div02.get("compendium_annexe_c_pdf_page"),
        }

    reconciliations: list[dict[str, Any]] = []
    cinq_disc = disc_block.get("cinq_discordances_tome_8") or {}
    for entry in cinq_disc.get("entries", []):
        variants_clean = [
            {k: clean_prose_typography(v) if isinstance(v, str) else v for k, v in var.items()}
            if isinstance(var, dict)
            else var
            for var in entry.get("volume_variants", [])
        ]
        c_line = int(entry.get("compendium_line_start") or 116)
        reconciliations.append(
            {
                "id": entry.get("discordance_id", ""),
                "title": clean_prose_typography(entry.get("topic", "")),
                "section": f"Compendium §{entry.get('liminaire_section', '0.2')} / Annexe C · L{c_line}",
                "resolution": clean_prose_typography(entry.get("canonical_vol8_choice", "")),
                "rationale": clean_prose_typography(entry.get("rationale", "")),
                "variants": variants_clean,
                "file": entry.get("compendium_file") or "Compendium/Compendium.md",
                "line_start": c_line,
                "pdf_page": entry.get("compendium_pdf_page"),
                "annexe_c_line": entry.get("compendium_annexe_c_line"),
                "annexe_c_pdf_page": entry.get("compendium_annexe_c_pdf_page"),
            }
        )

    raw_tl = raw_pivots.get("chronologie_2023_2035") or {}
    raw_mat = raw_pivots.get("matrices") or {}

    if raw_tl and raw_mat:
        tl_unified = _build_consolidated_timeline(raw_pivots, {"timeline": []})
        timeline = [
            {
                **ev,
                "date": clean_prose_typography(ev.get("date", "")),
                "cadre": clean_prose_typography(ev.get("cadre", "")),
                "impact": clean_prose_typography(ev.get("impact", "")),
            }
            for ev in tl_unified
        ]
        mat_unified, matrix_distribution, matrix_totals = _build_unified_matrix(
            raw_pivots, comp_lines=comp_lines, structure=structure, pdf_index=pdf_index
        )
        traceability_matrix = [
            {
                **item,
                "family": clean_prose_typography(item.get("family", "")),
                "title": clean_prose_typography(item.get("title", "")),
                "module": clean_prose_typography(item.get("module", "")),
                "anchor": clean_prose_typography(item.get("anchor", "")),
            }
            for item in mat_unified
        ]
        return {
            "div_02": div_02,
            "reconciliations": reconciliations,
            "timeline": timeline,
            "traceability_matrix": traceability_matrix,
            "matrix_distribution": matrix_distribution,
            "matrix_totals": matrix_totals,
            "collection_metrics": raw_pivots.get("collection_metrics", {}),
            "concordance_8_tomes": raw_pivots.get("concordance_8_tomes", {}),
            "bilans_aq": raw_pivots.get("bilans_aq_wyvern_et_statut_f", {}),
            "glossaire_pivot": raw_pivots.get("glossaire_pivot", {}),
            "faits_empiriques_16": raw_pivots.get("faits_empiriques_16", []),
            "specifications_lplus_57": raw_pivots.get("specifications_lplus_57", []),
            "statut_f_exclus_27": raw_pivots.get("statut_f_exclus_27", []),
        }

    timeline: list[dict[str, Any]] = []
    for rep in raw_tl.get("six_reperes_readme", []):
        timeline.append(
            {
                "date": rep.get("echeance", ""),
                "cadre": rep.get("cadre", ""),
                "impact": rep.get("resume", ""),
                "tomes": ["R", "T4", "T7"],
                "file": "Tomes/README.md",
                "line_start": 24,
                "source_group": "Repères clés",
            }
        )
    for pal in raw_tl.get("rampe_et_paliers_dapp_t5", []):
        horizon_clean = clean_dapp_label(f"{pal.get('horizon', '')} ({pal.get('phase', '')})")
        timeline.append(
            {
                "date": horizon_clean,
                "cadre": f"DAPP · {pal.get('stade', '')}",
                "impact": clean_prose_typography(pal.get("jalons", "")),
                "tomes": ["T4", "T5"],
                "file": "Tomes/Tome 5 - Synthèse exécutive et concordance architecturale.md",
                "line_start": 1544,
                "source_group": "Trajectoire DAPP",
            }
        )
    for anc in raw_tl.get("ancres_t7_l_plus", []):
        timeline.append(
            {
                "date": anc.get("date", ""),
                "cadre": f"{anc.get('label', '')} ({anc.get('jurisdiction', '')})",
                "impact": anc.get("commentaire_annexe") or anc.get("nature", ""),
                "tomes": ["T7"],
                "file": "Tomes/Tome 7 - Gouverner l'industrialisation cognitive.md",
                "line_start": 2053,
                "source_group": "Tome 7 Annexe B",
            }
        )
    for anc in raw_tl.get("ancres_t8_l_plus", []):
        timeline.append(
            {
                "date": anc.get("date", ""),
                "cadre": f"{anc.get('label', '')} ({anc.get('jurisdiction', '')})",
                "impact": anc.get("commentaire_annexe") or anc.get("nature", ""),
                "tomes": ["T8"],
                "file": "Tomes/Tome 8 - Ingénierie exécutable et homologation vérifiable.md",
                "line_start": 1483,
                "source_group": "Tome 8 L+",
            }
        )
    for anc in raw_tl.get("ancres_t4_67", []):
        timeline.append(
            {
                "date": anc.get("echeance", ""),
                "cadre": f"{anc.get('id', '')} · {anc.get('juridiction', '')} ({anc.get('axe', '')})",
                "impact": anc.get("enonce", ""),
                "tomes": ["T4"],
                "file": "Tomes/Tome 4 - Prospective stratégique et trajectoire 2028-2035.md",
                "line_start": 5175,
                "source_group": "Tome 4 Annexe A",
            }
        )

    timeline = deduplicate_and_sort_timeline(timeline)

    raw_mat = raw_pivots.get("matrices") or {}
    traceability_matrix: list[dict[str, Any]] = []
    t8_exec = raw_mat.get("tome8_executable") or {}
    for row in t8_exec.get("matrice_exig_prr_c40_95", []):
        traceability_matrix.append(
            {
                "id": row.get("id", ""),
                "family": f"{row.get('family', '')} ({row.get('criticality', '')})",
                "layer": "Test exécutable Tome 8",
                "title": clean_prose_typography(row.get("pytest_nodeid") or row.get("rego_rule") or ""),
                "module": f"{row.get('trousse_module', '')}.{row.get('implementation_symbol', '')}",
                "anchor": clean_prose_typography(row.get("corpus_anchor", "")),
            }
        )
    for sbb in t8_exec.get("cinq_sbb_tableau_12", []):
        traceability_matrix.append(
            {
                "id": sbb.get("sbb_id", ""),
                "family": f"5 SBB ({sbb.get('plan', '')})",
                "layer": "Architecture 5 SBB",
                "title": clean_prose_typography(sbb.get("slot", "")),
                "module": sbb.get("module_t8", ""),
                "anchor": "T2 Tableau 12 / T8 Annexe B",
            }
        )
    prr = raw_mat.get("prr_75") or {}
    for item in prr.get("items", []):
        traceability_matrix.append(
            {
                "id": item.get("prr_id", ""),
                "family": f"PRR-75 ({item.get('criticite', '')})",
                "layer": "Grille opérationnelle PRR-75",
                "title": clean_prose_typography(item.get("point_controle", "")),
                "module": clean_prose_typography(item.get("artefact_preuve", "")),
                "anchor": f"Grille {item.get('grid', '')}",
            }
        )
    for cap in raw_mat.get("cap_52", []):
        exigs = ", ".join(cap.get("exigences_cad26", []))
        traceability_matrix.append(
            {
                "id": cap.get("cap_id", ""),
                "family": f"CAP ({cap.get('statut', '')} · {cap.get('palier', '')})",
                "layer": "Portefeuille CAP-001..052",
                "title": clean_prose_typography(cap.get("nom") or cap.get("intitule_condense", "")),
                "module": exigs or cap.get("type_rattachement_cad26", ""),
                "anchor": clean_prose_typography(cap.get("emplacement", "")),
            }
        )
    for pex in raw_mat.get("pex_24", []):
        traceability_matrix.append(
            {
                "id": pex.get("pex_id", ""),
                "family": f"PEX ({pex.get('sous_secteur', '')})",
                "layer": "Profils sectoriels PEX-001..044",
                "title": clean_prose_typography(pex.get("titre", "")),
                "module": ", ".join(pex.get("exigences_cad26", [])),
                "anchor": clean_prose_typography(pex.get("chapitre_t4", "")),
            }
        )
    exig_meta = raw_mat.get("exig_cre_ia_2026_v1_2") or {}
    for fam in exig_meta.get("familles", []):
        if isinstance(fam, dict):
            traceability_matrix.append(
                {
                    "id": fam.get("prefixe") or fam.get("code", ""),
                    "family": "CRE-IA-2026-01 (Famille EXIG)",
                    "layer": "Familles normatives CRE-IA-2026-01",
                    "title": clean_prose_typography(fam.get("titre") or fam.get("domaine") or ""),
                    "module": f"{fam.get('nombre', fam.get('count', ''))} exigences",
                    "anchor": "T2 Annexe D / T5 Annexe A",
                }
            )

    return {
        "div_02": div_02,
        "reconciliations": reconciliations,
        "timeline": timeline,
        "traceability_matrix": traceability_matrix,
        "collection_metrics": raw_pivots.get("collection_metrics", {}),
        "concordance_8_tomes": raw_pivots.get("concordance_8_tomes", {}),
        "bilans_aq": raw_pivots.get("bilans_aq_wyvern_et_statut_f", {}),
        "glossaire_pivot": raw_pivots.get("glossaire_pivot", {}),
    }


def _build_schemas_catalog(
    comp_inv: dict[str, Any] | None,
    cat_schemas: dict[str, Any] | None,
) -> list[dict[str, Any]]:
    """Fusionne l'inventaire vérifié des 139 schémas et les métadonnées pédagogiques."""
    if not comp_inv:
        return []
    cat_by_id: dict[str, dict[str, Any]] = {}
    if cat_schemas:
        for grp in ("global_schemas", "chapter_schemas", "annex_schemas"):
            for item in cat_schemas.get(grp) or []:
                sid = item.get("schema_id")
                if sid:
                    cat_by_id[sid] = item

    out: list[dict[str, Any]] = []
    for fig in comp_inv.get("figures") or []:
        sid = fig["schema_id"]
        meta = cat_by_id.get(sid) or {}
        out.append(
            {
                "schema_id": sid,
                "unit": fig["unit"],
                "part_id": fig["part_id"],
                "chapter_number": int(fig.get("chapter_number", 0)),
                "domain_id": fig.get("domain_id", "GLOBAL"),
                "engine": fig["engine"],
                "notation": _clean_text(fig.get("notation", "")),
                "title": _clean_text(fig.get("title", "")),
                "rendered_path": fig["rendered_path"],
                "compendium_md_file": fig.get("compendium_md_file", "Compendium/Compendium.md"),
                "compendium_md_line": int(fig.get("compendium_md_line", 1)),
                "pdf_page": fig.get("pdf_page"),
                "pedagogical_objective": _clean_text(meta.get("pedagogical_objective", "")),
                "vulgarization_angle": _clean_text(meta.get("vulgarization_angle", "")),
                "target_audiences": [str(a) for a in (meta.get("target_audiences") or [])],
                "visual_archetype": _clean_text(meta.get("visual_archetype", "")),
                "families_covered": list(fig.get("families_covered") or meta.get("families_covered") or []),
                "themes_vulgarized": list(fig.get("themes_vulgarized") or meta.get("themes_vulgarized") or []),
            }
        )
    return out


def _build_reading_paths(
    chapters: list[dict[str, Any]],
    nodes: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """Construit 5 parcours guidés vérifiés dans le Compendium."""
    chapters_by_cid = {c["compendium_unit_id"]: c for c in chapters if c.get("compendium_unit_id")}
    sub_by_ch = {n.get("chapter_id"): n for n in nodes if n.get("node_kind") == "subdomain" and n.get("chapter_id")}
    node_by_slug = {n.get("canonical_slug"): n for n in nodes if n.get("canonical_slug")}

    specs = [
        {
            "path_id": "essentiel",
            "title": "Parcours Essentiel — Interopérabilité, 80/20 & Systèmes d'entreprise",
            "audience": "Direction · Décideurs · Tous publics",
            "description": "Saisir le continuum d'automatisation L0–L4, la loi de Lusser, la partition hybride 80/20, l'interopérabilité MCP, la sobriété OO1–OO4 et le panorama des systèmes d'entreprise.",
            "units": ["00-liminaire", "ch01", "ch02", "ch04", "ch07", "ch13", "annexe-e"],
        },
        {
            "path_id": "ae-strategie",
            "title": "Architecte d'Entreprise (AE) — Systèmes d'entreprise, Anti-verrouillage & Portefeuille",
            "audience": "Architecte d'entreprise (AE) · Direction TI",
            "description": "Gouverner l'économie de l'interopérabilité, le noyau possédé (42 CAP sur 52), les passerelles PEP, la sémantique canonique, la matrice sectorielle et la trajectoire DAPP 2028–2035.",
            "units": ["00-liminaire", "ch03", "ch06", "ch09", "ch10", "ch27", "ch28", "ch30", "ch31"],
        },
        {
            "path_id": "as-ingenierie",
            "title": "Architecte de Solutions (AS) — Interopérabilité MCP/A2A, Patrimoine & Automatisation Saga",
            "audience": "Architecte de solutions (AS) · Ingénierie",
            "description": "Concevoir les harnais 80/20, façades MCP et délégations A2A, passerelles PEP, contrats ODCS, mémoire CoALA, encapsulation ERP/ACL/OT, sobriété OO1–OO4, Event Mesh, Sagas et blueprints C01–C40.",
            "units": ["ch04", "ch07", "ch08", "ch09", "ch10", "ch11", "ch12", "ch13", "ch14", "ch15", "ch29"],
        },
        {
            "path_id": "rssi-securite",
            "title": "RSSI & Sécurité — Identité NHI, Passerelles PEP & Sûreté des systèmes d'entreprise",
            "audience": "RSSI · Cybersécurité · SRE",
            "description": "Verrouiller les passerelles PEP à neuf contrôles, fédérer les identités NHI/OBO/CIBA, automatiser la PKI 47 jours et le post-quantique, appliquer OPA/Cedar et la Règle de deux, confiner vers L0 et sceller l'audit.",
            "units": ["ch09", "ch16", "ch17", "ch18", "ch19", "ch20", "ch21", "ch22", "ch24"],
        },
        {
            "path_id": "juridique-2035",
            "title": "Juridique, Conformité & Homologation vérifiable des systèmes d'entreprise",
            "audience": "Juridique · Conformité · Audit",
            "description": "Articuler supervision anti-complaisance, Loi 25 (art. 12.1 et 27), étalon BSIF E-23/AMF, EU AI Act/DORA/Data Act, maintien du repli humain L0, référentiel CRE-IA/PRR-75 et homologation exécutable G0–G5.",
            "units": ["ch05", "ch25", "ch26", "ch33", "ch34", "ch35", "ch36", "annexe-c", "annexe-d"],
        },
    ]

    paths: list[dict[str, Any]] = []
    for sp in specs:
        steps: list[dict[str, Any]] = []
        total_min = 0
        total_pages = 0
        for uid in sp["units"]:
            ch = chapters_by_cid.get(uid)
            if not ch:
                continue
            sub_node = sub_by_ch.get(uid)
            rep_node_id = sub_node["node_id"] if sub_node else None
            if not rep_node_id:
                for sl in ch.get("themes_addressed") or []:
                    tn = node_by_slug.get(sl)
                    if tn:
                        rep_node_id = tn["node_id"]
                        break
            if not rep_node_id:
                rep_node_id = "NODE_ROOT"

            p0 = ch.get("pdf_page_start")
            p1 = ch.get("pdf_page_end")
            rmin = int(ch.get("reading_minutes") or max(1, round(int(ch.get("word_count", 0)) / 220)))
            total_min += rmin
            if p0 is not None and p1 is not None and p1 >= p0:
                total_pages += p1 - p0 + 1
            steps.append(
                {
                    "compendium_unit_id": uid,
                    "struct_unit_id": ch.get("unit_id"),
                    "representative_node_id": rep_node_id,
                    "part_id": ch.get("part_id"),
                    "title": _clean_text(ch.get("chapter_title") or uid),
                    "objective": _clean_text(ch.get("guiding_question") or ch.get("summary") or ""),
                    "line_start": int(ch.get("line_start") or 1),
                    "pdf_page_start": p0,
                    "pdf_page_end": p1,
                    "reading_minutes": rmin,
                }
            )
        paths.append(
            {
                "path_id": sp["path_id"],
                "title": sp["title"],
                "audience": sp["audience"],
                "description": sp["description"],
                "steps_count": len(steps),
                "total_minutes": total_min,
                "total_pages": total_pages,
                "steps": steps,
            }
        )
    return paths


def build_mindmap_bundle(
    schema: dict[str, Any],
    structure: dict[str, Any],
    pivots: dict[str, Any],
    synthese: dict[str, Any],
    comp_inv: dict[str, Any] | None = None,
    cat_schemas: dict[str, Any] | None = None,
    comp_lines: list[str] | None = None,
    pdf_index: Any | None = None,
) -> dict[str, Any]:
    """Assemble et valide le bundle unifié ``corpus-mindmap-data.json``."""
    nodes = synthese.get("nodes") or synthese.get("thematic_nodes") or []
    relations = synthese.get("relations") or synthese.get("edges") or []
    chapters = synthese.get("chapters") or synthese.get("chapters_mapped") or []
    concordance_matrix = synthese.get("concordance_matrix") or synthese.get("matrix") or []

    node_ids = {n["node_id"] for n in nodes if "node_id" in n}
    valid_rel_types = {rt["type_id"] for rt in schema.get("relation_types", [])}

    for rel in relations:
        src = rel.get("source")
        tgt = rel.get("target")
        rtype = rel.get("type")
        if src not in node_ids or tgt not in node_ids:
            raise ValueError(f"Arête cassée dans synthese-transversale.json : {rel}")
        if src == tgt:
            raise ValueError(f"Auto-boucle interdite détectée : {rel}")
        if valid_rel_types and rtype not in valid_rel_types:
            raise ValueError(f"Type de relation inconnu '{rtype}' dans {rel}")
        if not str(rel.get("justification", "")).strip():
            raise ValueError(f"Justification vide sur la relation {rel.get('relation_id')}")

    normalized_pivots = normalize_pivots(
        pivots, comp_lines=comp_lines, structure=structure, pdf_index=pdf_index
    )
    schemas_catalog = _build_schemas_catalog(comp_inv, cat_schemas)
    reading_paths = _build_reading_paths(chapters, nodes)

    return {
        "schema_version": "1.0.0",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "lang": "fr-CA",
        "schema": schema,
        "domains": schema.get("domains", []),
        "relation_types": schema.get("relation_types", []),
        "totals": {
            "files": structure.get("totals", {}).get("files", 9),
            "lines": structure.get("totals", {}).get("lines", 0),
            "words": structure.get("totals", {}).get("words", 0),
            "headings": structure.get("totals", {}).get("headings", 0),
            "nodes": len(nodes),
            "theme_nodes": sum(1 for n in nodes if n.get("node_kind") == "theme"),
            "relations": len(relations),
            "chapters": len(chapters),
            "schemas": len(schemas_catalog),
            "reading_paths": len(reading_paths),
        },
        "nodes": nodes,
        "relations": relations,
        "chapters": chapters,
        "concordance_matrix": concordance_matrix,
        "schemas": schemas_catalog,
        "reading_paths": reading_paths,
        "pivots": normalized_pivots,
        "structure": structure,
    }


def compile_mindmap(repo_root: Path) -> tuple[Path, Path, dict[str, Any]]:
    """Compile ``corpus-mindmap-data.json`` et l'application HTML autonome."""
    donnees_dir = repo_root / "Sources" / "Cartographie" / "donnees"
    outils_dir = repo_root / "Sources" / "Cartographie" / "outils"

    schema = json.loads((donnees_dir / "schema-cartographie.json").read_text(encoding="utf-8"))
    structure = json.loads((donnees_dir / "structure-integrale.json").read_text(encoding="utf-8"))
    pivots = json.loads((donnees_dir / "pivots-concordance.json").read_text(encoding="utf-8"))
    synthese = json.loads((donnees_dir / "synthese-transversale.json").read_text(encoding="utf-8"))
    comp_inv_path = donnees_dir / "inventaire-139-schemas-compendium.json"
    cat_schemas_path = donnees_dir / "catalogue-schemas-prd.json"
    comp_inv = json.loads(comp_inv_path.read_text(encoding="utf-8")) if comp_inv_path.is_file() else None
    cat_schemas = json.loads(cat_schemas_path.read_text(encoding="utf-8")) if cat_schemas_path.is_file() else None

    comp_md_path = repo_root / "Compendium" / "Compendium.md"
    comp_lines = comp_md_path.read_text(encoding="utf-8").splitlines() if comp_md_path.is_file() else None
    from index_pdf_compendium import CompendiumPdfIndex  # noqa: E402

    pdf_index = (
        CompendiumPdfIndex.from_repo(repo_root)
        if (repo_root / "Compendium" / "Compendium.pdf").is_file() and comp_md_path.is_file()
        else None
    )

    template_html = (outils_dir / "template_mindmap.html").read_text(encoding="utf-8")

    bundle = build_mindmap_bundle(
        schema,
        structure,
        pivots,
        synthese,
        comp_inv=comp_inv,
        cat_schemas=cat_schemas,
        comp_lines=comp_lines,
        pdf_index=pdf_index,
    )

    data_out = donnees_dir / "corpus-mindmap-data.json"
    data_out.write_text(
        json.dumps(bundle, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )

    minified_json = json.dumps(bundle, ensure_ascii=False, separators=(",", ":"))
    safe_json = escape_json_for_script(minified_json)
    for forbidden in ("</", "<!--", "\u2028", "\u2029"):
        if forbidden in safe_json:
            raise ValueError(f"Séquence dangereuse résiduelle dans le JSON injecté : {forbidden!r}")

    if template_html.count("__CORPUS_DATA_JSON__") != 1:
        raise ValueError("Marqueur __CORPUS_DATA_JSON__ doit apparaître exactement une fois dans template_mindmap.html")

    compiled_html = template_html.replace("__PAGE_TITLE__", PAGE_TITLE).replace(
        "__CORPUS_DATA_JSON__", safe_json, 1
    )
    json_match = re.search(
        r'<script[^>]*id="corpus-mindmap-data"[^>]*>([\s\S]*?)</script>',
        compiled_html,
    )
    if json_match is None:
        raise ValueError("Balise <script id='corpus-mindmap-data'> introuvable dans le HTML compilé")
    html_outside_json = compiled_html[: json_match.start(1)] + compiled_html[json_match.end(1) :]
    if re.search(r"https?://", html_outside_json, re.IGNORECASE):
        raise ValueError("URL http(s):// externe détectée hors bloc JSON dans MindMap HTML")
    if re.search(r"<script[^>]+src\s*=|<link[^>]+href\s*=\s*['\"]?(?:https?:)?//|@import\s+url\(|\bfetch\s*\(", html_outside_json, re.IGNORECASE):
        raise ValueError("Référence réseau/CDN détectée hors bloc JSON dans MindMap HTML")

    html_out = repo_root / "Sources" / "Cartographie" / "MindMap - Cartographie thématique du Compendium.html"
    html_out.write_text(compiled_html, encoding="utf-8", newline="\n")
    old_html = repo_root / "Sources" / "Cartographie" / "MindMap - Cartographie thématique du Corpus.html"
    if old_html.is_file():
        old_html.unlink()

    return data_out, html_out, bundle


def main() -> int:
    """Point d'entrée CLI pour la compilation MindMap."""
    parser = argparse.ArgumentParser(
        description="Compile corpus-mindmap-data.json et la MindMap HTML autonome."
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path(__file__).resolve().parents[3],
        help="Racine du dépôt Agentique.",
    )
    args = parser.parse_args()

    data_out, html_out, bundle = compile_mindmap(args.repo_root.resolve())
    t = bundle["totals"]
    print(
        f"Compilation réussie : {t['theme_nodes']} thèmes ({t['nodes']} nœuds), "
        f"{t['relations']} interrelations, {t['headings']} titres H1–H6, "
        f"{len(bundle['pivots']['reconciliations'])} discordances, "
        f"{len(bundle['pivots']['timeline'])} jalons, "
        f"{len(bundle['pivots']['traceability_matrix'])} entrées traçabilité -> "
        f"{data_out} & {html_out} ({html_out.stat().st_size} octets)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
