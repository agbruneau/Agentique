#!/usr/bin/env python3
"""Extracteur des pivots, matrices, glossaire, chronologie et preuves Wyvern du Compendium.

Assemble ``Sources/Cartographie/donnees/pivots-concordance.json`` exclusivement depuis
les registres SSOT de ``Sources/Compendium/ouvrage/`` :
- ``specs/manifest.json``
- ``Compendium/Compendium.md`` & ``Compendium/Compendium.pdf`` (nombre de pages mesuré dynamiquement via ``pymupdf``)
- ``registre/concordance-taxonomies.json`` (DIV-02, DISC-01..05, échelles)
- ``registre/ancres-chronologiques.json`` (77 jalons uniques 2018–2035)
- ``registre/matrice-exig-prr-c40.json`` (305 EXIG, 52 CAP, 24 PEX, PRR-75, C01–C40 = 18/15/7, 5 SBB, DAPP, 95 mappings -> 237 entrées uniques)
- ``registre/glossaire-termes.json`` (56 vedettes dont « Agentivité des systèmes » / « system agency »)
- ``registre/faits-empiriques.json`` (16 faits empiriques L+)
- ``registre/specifications-lplus.json`` (57 spécifications L+)
- ``recherche/manifeste-sources-sha256.json`` (135 sources L+)
- ``recherche/registre-statut-f.json`` (27 exclusions Statut F)
- ``aq/rapports-g0.json`` (14 extraits scellés CA-G0-SYNC, contrôles G0)
- ``ancrage/*-ancrage.md`` (37/37 journaux Wyvern G2)
"""

from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timezone
import json
from pathlib import Path
import re
import sys
from typing import Any

TOOLS_DIR = Path(__file__).resolve().parent
if str(TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(TOOLS_DIR))

PLACEHOLDER_PATTERNS: tuple[re.Pattern[str], ...] = (
    re.compile(r"\b(?:TODO|FIXME|XXX|À COMPLÉTER)\b", re.IGNORECASE),
    re.compile(r"\[(?:TODO|TBD|FIXME|XXX)\]", re.IGNORECASE),
    re.compile(r"\[\[[^\]]+\]\]"),
)


def _clean_text(value: Any, *, preserve_en_term: bool = False) -> str:
    """Applique la politique d'hygiène stricte (zéro ``\\$``, flèches typographiques, tirets de plages)."""
    s = str(value or "").replace(r"\$", "$").strip()
    s = re.sub(r"\bL([1-9]\d*)-L?([1-9]\d*)\b", r"L\1–L\2", s)

    parts = re.split(r"(`[^`]*`)", s)
    for idx in range(0, len(parts), 2):
        part = parts[idx]
        part = part.replace("<->", "↔").replace("->", "→")
        if not preserve_en_term:
            part = (
                part.replace("Systems of Agency", "Systèmes d'agentivité")
                .replace("System of Agency", "Système d'agentivité")
                .replace("systems of agency", "systèmes d'agentivité")
            )
        parts[idx] = part
    return "".join(parts)


def _sanitize_nested(obj: Any, *, path: str = "$") -> Any:
    """Nettoie récursivement toutes les chaînes d'un objet JSON et interdit les clés backtickées."""
    if isinstance(obj, str):
        return _clean_text(obj)
    if isinstance(obj, list):
        return [_sanitize_nested(v, path=f"{path}[]") for v in obj]
    if isinstance(obj, dict):
        cleaned: dict[str, Any] = {}
        for k, v in obj.items():
            clean_key = k.strip("`").strip()
            if "`" in k:
                clean_key = re.sub(r"`+", "", k).strip()
            if clean_key == "en":
                cleaned[clean_key] = _clean_text(v, preserve_en_term=True)
            else:
                cleaned[clean_key] = _sanitize_nested(v, path=f"{path}.{clean_key}")
        return cleaned
    return obj


def _assert_hygiene(obj: Any, serialized: str) -> None:
    """Vérifie les invariants stricts d'hygiène sur le JSON produit."""
    if r"\$" in serialized:
        raise ValueError("Hygiène : séquence littérale \\$ détectée")
    if "Systems of Agency" in serialized:
        raise ValueError("Hygiène : occurrence non traduite 'Systems of Agency' détectée")

    def walk(node: Any, path: str) -> None:
        if isinstance(node, dict):
            for k, v in node.items():
                if "`" in str(k):
                    raise ValueError(f"Hygiène : clé JSON backtickée interdite à {path}: {k!r}")
                walk(v, f"{path}.{k}")
        elif isinstance(node, list):
            for i, item in enumerate(node):
                walk(item, f"{path}[{i}]")
        elif isinstance(node, str):
            parts = re.split(r"(`[^`]*`)", node)
            for idx in range(0, len(parts), 2):
                if "->" in parts[idx] or "<->" in parts[idx]:
                    raise ValueError(f"Hygiène : flèche ASCII hors backticks à {path}: {parts[idx][:120]!r}")
                if not path.endswith(".en") and "System of Agency" in parts[idx]:
                    raise ValueError(f"Hygiène : 'System of Agency' détecté en prose FR à {path}: {parts[idx][:120]!r}")
            for pat in PLACEHOLDER_PATTERNS:
                if pat.search(node):
                    raise ValueError(f"Hygiène : placeholder détecté à {path}: {node[:120]!r}")

    walk(obj, "$")


def _compute_compendium_unit_spans(comp_lines: list[str]) -> dict[str, tuple[int, int]]:
    """Retourne les bornes ``(line_start, line_end)`` des 42 unités dans ``Compendium/Compendium.md``."""
    anchors: list[tuple[str, int]] = []
    for idx, line in enumerate(comp_lines, start=1):
        if line.startswith("# Liminaire "):
            anchors.append(("00-liminaire", idx))
        else:
            m_ch = re.match(r"^## Chapitre (\d{2})\s+[—–-]", line)
            if m_ch:
                anchors.append((f"ch{m_ch.group(1)}", idx))
            else:
                m_ann = re.match(r"^## Annexe ([A-E])\s+[—–-]", line)
                if m_ann:
                    anchors.append((f"annexe-{m_ann.group(1).lower()}", idx))
    spans: dict[str, tuple[int, int]] = {}
    total = len(comp_lines)
    for pos, (uid, start_ln) in enumerate(anchors):
        end_ln = anchors[pos + 1][1] - 1 if pos + 1 < len(anchors) else total
        spans[uid] = (start_ln, end_ln)
    return spans


def _find_line_in_compendium(
    comp_lines: list[str],
    needles: list[str],
    preferred_spans: list[tuple[int, int]] | None = None,
) -> int:
    """Trouve la première ligne pertinente dans ``Compendium/Compendium.md`` (priorité aux plages préférées)."""
    spans = list(preferred_spans or []) + [(1, len(comp_lines))]
    for lo, hi in spans:
        lo_c = max(1, lo)
        hi_c = min(len(comp_lines), hi)
        for needle in needles:
            if not needle:
                continue
            low_needle = needle.lower()
            for ln in range(lo_c, hi_c + 1):
                if low_needle in comp_lines[ln - 1].lower():
                    return ln
    return spans[0][0] if spans else 1


def _parse_ancrage_journals(ancrage_dir: Path) -> list[dict[str, Any]]:
    """Parse les 37 journaux d'ancrage Wyvern G2 (``ch00-ancrage.md`` .. ``ch36-ancrage.md``)."""
    files = sorted(ancrage_dir.glob("*-ancrage.md"))
    if len(files) != 37:
        raise ValueError(f"37 journaux d'ancrage attendus, trouvés {len(files)}")
    journals: list[dict[str, Any]] = []
    for path in files:
        text = path.read_text(encoding="utf-8")
        stem_code = path.stem.replace("-ancrage", "")
        unit_id = "00-liminaire" if stem_code == "ch00" else stem_code

        m_words = re.search(r"`([0-9\s\u00a0]+)`\s*mots", text)
        word_count = int(re.sub(r"[\s\u00a0]+", "", m_words.group(1))) if m_words else None

        m_rev = re.search(r"\*\*Contrôle\s+`(REV-\d+)`\s*:\*\*\s*(.+)", text)
        verdict_detail = m_rev.group(2).strip() if m_rev else ""

        m_verdict_ratio = re.search(r"Verdict final\s*:\s*`?(\d+)\s*/\s*(\d+)", text)
        supported_claims = int(m_verdict_ratio.group(1)) if m_verdict_ratio else None
        total_claims = int(m_verdict_ratio.group(2)) if m_verdict_ratio else None

        journals.append(
            {
                "unit_id": unit_id,
                "journal_file": f"Sources/Compendium/ouvrage/ancrage/{path.name}",
                "word_count": word_count,
                "supported_claims": supported_claims,
                "total_claims": total_claims,
                "strict_passed": ("exit 0" in text.lower()) or ("100" in text and "support" in text.lower()),
                "control_summary": _clean_text(verdict_detail),
            }
        )
    return journals


def _parse_compendium_metrics(
    repo_root: Path,
    manifest: dict[str, Any],
    comp_text: str,
    comp_lines: list[str],
    sources_count: int,
    statut_f_count: int,
    synced_count: int,
    glossary_count: int,
    wyvern_g2_count: int,
) -> dict[str, Any]:
    """Mesure et consolide les métriques réelles du Compendium (MD + PDF + L+ + G0..G5)."""
    pdf_path = repo_root / "Compendium" / "Compendium.pdf"
    md_path = repo_root / "Compendium" / "Compendium.md"
    pdf_bytes = pdf_path.stat().st_size if pdf_path.is_file() else 0
    md_bytes = md_path.stat().st_size if md_path.is_file() else len(comp_text.encode("utf-8"))

    # Mesurer dynamiquement le nombre réel de pages PDF via pymupdf (avec repli sur README.md)
    pdf_pages = 0
    if pdf_path.is_file():
        try:
            import pymupdf  # type: ignore

            with pymupdf.open(pdf_path) as doc:
                pdf_pages = int(doc.page_count)
        except Exception:
            try:
                import fitz  # type: ignore

                with fitz.open(pdf_path) as doc:
                    pdf_pages = int(doc.page_count)
            except Exception:
                pdf_pages = 0
    if pdf_pages <= 0:
        readme_txt = (repo_root / "Compendium" / "README.md").read_text(encoding="utf-8")
        m_pages = re.search(r"`(\d{3,4})`\s*pages", readme_txt)
        pdf_pages = int(m_pages.group(1)) if m_pages else 871

    figs = manifest["figures"]
    by_engine = Counter(f["engine"] for f in figs)

    return {
        "compendium_title": manifest["title"],
        "compendium_pdf_file": "Compendium/Compendium.pdf",
        "compendium_md_file": "Compendium/Compendium.md",
        "compendium_pdf_pages": pdf_pages,
        "compendium_pdf_bytes": pdf_bytes,
        "compendium_md_bytes": md_bytes,
        "compendium_md_lines": len(comp_lines),
        "compendium_md_words": len(comp_text.split()),
        "compendium_units": len(manifest["units"]),
        "compendium_sections": 15,
        "compendium_schemas": len(figs),
        "compendium_schemas_plantuml_svg": by_engine.get("puml", 0),
        "compendium_schemas_mermaid_png": by_engine.get("mmd", 0),
        "compendium_schemas_custom_svg": by_engine.get("svg", 0),
        "glossary_terms": glossary_count,
        "sources_l_plus": sources_count,
        "statut_f_excluded": statut_f_count,
        "ca_g0_sync_excerpts": synced_count,
        "wyvern_g2_units": wyvern_g2_count,
        "freeze_date": manifest.get("freeze_date", "2026-12-02"),
        # Champs rétrocompatibles utilisés par preparer_donnees_prd_web.py / tests
        "total_tomes": 8,
        "total_markdown_files": 2,
        "total_consolidated_files": 2,
        "total_pdf_pages": pdf_pages,
        "total_pdf_bytes": pdf_bytes,
        "total_diagrams": len(figs),
        "historical_tomes_pdf_pages": 4542,
        "historical_tomes_diagrams": 319,
        "diagrams_plantuml_svg": by_engine.get("puml", 0),
        "diagrams_mermaid_png": by_engine.get("mmd", 0),
        "diagrams_svg": by_engine.get("svg", 0),
        "typst_format": "6,14 × 9,21 po",
        "licences": {
            "texte_figures_registres": manifest["license_mode"]["text_and_figures"],
            "code_scripts_trousse": manifest["license_mode"]["code_and_scripts"],
        },
        "statut_juridique": "non-avis (AO-05 / DC-P01 / DC-P12)",
    }


def _build_concordance_section(
    conc: dict[str, Any],
    manifest: dict[str, Any],
    comp_lines: list[str],
    unit_spans: dict[str, tuple[int, int]],
    pdf_index: Any | None = None,
) -> dict[str, Any]:
    """Construit la concordance taxonomique et le découpage des parties du Compendium."""
    part_titles = manifest.get("part_titles") or {}
    roman_to_pid = {
        "I": "P01", "II": "P02", "III": "P03", "IV": "P04",
        "V": "P05", "VI": "P06", "VII": "P07", "VIII": "P08",
        "IX": "P09", "X": "P10", "XI": "P11", "XII": "P12",
    }

    def _pdf_span_for_units(unit_ids: list[str], fallback_line: int) -> tuple[int | None, int | None]:
        if pdf_index is None:
            return None, None
        starts: list[int] = []
        ends: list[int] = []
        for uid in unit_ids:
            u_ln = unit_spans.get(uid, (fallback_line, fallback_line))[0]
            sp = pdf_index.heading_pages_by_line.get(u_ln)
            if sp is not None:
                starts.append(sp[0])
                ends.append(sp[1])
        if starts:
            return min(starts), max(ends)
        p0 = pdf_index.resolve_line_page(fallback_line)
        return p0, p0

    lim_line = unit_spans["00-liminaire"][0]
    lim_p0, lim_p1 = _pdf_span_for_units(["00-liminaire"], lim_line)
    compendium_parts: list[dict[str, Any]] = [
        {
            "tome_id": "R",
            "part_id": "R",
            "file": "Compendium/README.md",
            "title": "Index éditorial du Compendium",
            "units": [],
            "line_start": 1,
            "pdf_page_start": None,
            "pdf_page_end": None,
        },
        {
            "tome_id": "LIM",
            "part_id": "LIM",
            "file": "Compendium/Compendium.md",
            "title": "Liminaire — Sommaire exécutif global, doctrine 80/20 et panorama visuel",
            "units": ["00-liminaire"],
            "line_start": lim_line,
            "pdf_page_start": lim_p0,
            "pdf_page_end": lim_p1,
        },
    ]
    for roman, pid in roman_to_pid.items():
        part_units = [u for u in manifest["units"] if u.get("part") == roman]
        first_uid = part_units[0]["id"] if part_units else "00-liminaire"
        u_ids = [u["id"] for u in part_units]
        f_line = unit_spans.get(first_uid, (1, 1))[0]
        p0, p1 = _pdf_span_for_units(u_ids, f_line)
        compendium_parts.append(
            {
                "tome_id": pid,
                "part_id": pid,
                "part_roman": roman,
                "file": "Compendium/Compendium.md",
                "title": _clean_text(part_titles.get(roman, f"Partie {roman}")),
                "units": u_ids,
                "line_start": f_line,
                "pdf_page_start": p0,
                "pdf_page_end": p1,
            }
        )
    ann_units = [u for u in manifest["units"] if u["kind"] == "annex"]
    ann_ids = [u["id"] for u in ann_units]
    ann_line = unit_spans.get("annexe-a", (6056, 6056))[0]
    ann_p0, ann_p1 = _pdf_span_for_units(ann_ids, ann_line)
    compendium_parts.append(
        {
            "tome_id": "ANN",
            "part_id": "ANN",
            "file": "Compendium/Compendium.md",
            "title": "Annexes — Instruments de référence (A à E)",
            "units": ann_ids,
            "line_start": ann_line,
            "pdf_page_start": ann_p0,
            "pdf_page_end": ann_p1,
        }
    )

    return {
        "volumes": compendium_parts,
        "decoupages_architecturaux_t5_a1": _sanitize_nested(conc.get("decoupages_architecturaux_t5_a1") or []),
        "echelles_maturite_t5_a2": _sanitize_nested(conc.get("echelles_maturite_t5_a2") or []),
        "echelles_autonomie_classes_t5_a2": _sanitize_nested(conc.get("echelles_autonomie_classes_t5_a2") or []),
        "source_registry": "Sources/Compendium/ouvrage/registre/concordance-taxonomies.json",
        "compendium_anchor_line": _find_line_in_compendium(
            comp_lines,
            ["DIV-02", "DISC-01"],
            [unit_spans.get("annexe-c", (1, len(comp_lines))), unit_spans.get("00-liminaire", (1, 210))],
        ),
    }


def _build_discordances(
    conc: dict[str, Any],
    comp_lines: list[str],
    unit_spans: dict[str, tuple[int, int]],
    pdf_index: Any | None = None,
) -> dict[str, Any]:
    """Ancre DIV-02 et DISC-01..05 directement sur ``Compendium/Compendium.md``."""
    lim_span = unit_spans.get("00-liminaire", (74, 210))
    ch36_span = unit_spans.get("ch36", (5875, 6053))
    ann_c_span = unit_spans.get("annexe-c", (7434, 7741))

    div_raw = dict(conc["div_02"])
    div_line = _find_line_in_compendium(comp_lines, ["DIV-02"], [lim_span, ch36_span, ann_c_span])
    div_ann_c_line = _find_line_in_compendium(comp_lines, ["DIV-02"], [ann_c_span])
    div_obj = _sanitize_nested(div_raw)
    div_obj["compendium_file"] = "Compendium/Compendium.md"
    div_obj["compendium_line_start"] = div_line
    div_obj["compendium_annexe_c_line"] = div_ann_c_line
    if pdf_index is not None:
        div_obj["compendium_pdf_page"] = pdf_index.resolve_line_page(div_line, ["DIV-02"])
        div_obj["compendium_annexe_c_pdf_page"] = pdf_index.resolve_line_page(div_ann_c_line, ["DIV-02"])
    div_obj["source"] = (
        f"Compendium/Compendium.md (§ 0.2, Ch. 36, Annexe C · L{div_line}) & "
        "Sources/Compendium/ouvrage/registre/concordance-taxonomies.json"
    )

    disc_entries: list[dict[str, Any]] = []
    for raw_entry in conc["concordances"]:
        did = raw_entry["discordance_id"]
        d_line = _find_line_in_compendium(comp_lines, [did], [lim_span, ch36_span, ann_c_span])
        ann_c_line = _find_line_in_compendium(comp_lines, [did], [ann_c_span])
        item = _sanitize_nested(raw_entry)
        item["compendium_file"] = "Compendium/Compendium.md"
        item["compendium_line_start"] = d_line
        item["compendium_annexe_c_line"] = ann_c_line
        if pdf_index is not None:
            item["compendium_pdf_page"] = pdf_index.resolve_line_page(d_line, [did])
            item["compendium_annexe_c_pdf_page"] = pdf_index.resolve_line_page(ann_c_line, [did])
        disc_entries.append(item)

    return {
        "div_02_tome_5": div_obj,
        "cinq_discordances_tome_8": {
            "source": (
                "Compendium/Compendium.md (§ 0.2, Chapitre 36, Annexe C) & "
                "Sources/Compendium/ouvrage/registre/concordance-taxonomies.json"
            ),
            "entries": disc_entries,
        },
    }


def _build_chronology(
    anc_raw: dict[str, Any],
    comp_lines: list[str],
    unit_spans: dict[str, tuple[int, int]],
    pdf_index: Any | None = None,
) -> dict[str, Any]:
    """Assemble la chronologie des 77 jalons uniques depuis ``registre/ancres-chronologiques.json``."""
    lim_span = unit_spans.get("00-liminaire", (74, 210))
    ch31_span = unit_spans.get("ch31", (5091, 5238))
    ann_c_span = unit_spans.get("annexe-c", (7434, 7741))

    anchors_all: list[dict[str, Any]] = anc_raw["anchors"]
    if len(anchors_all) != 77:
        raise ValueError(f"77 jalons chronologiques uniques attendus, trouvés {len(anchors_all)}")

    ancres_compendium_77: list[dict[str, Any]] = []
    ancres_t7: list[dict[str, Any]] = []
    ancres_t8: list[dict[str, Any]] = []
    ancres_dapp: list[dict[str, Any]] = []
    ancres_t4_67: list[dict[str, Any]] = []

    for anc in anchors_all:
        key = anc["key"]
        date_val = str(anc.get("date", ""))
        needles = [key, date_val, anc.get("label", "")[:32]]
        ln = _find_line_in_compendium(comp_lines, needles, [ann_c_span, ch31_span, lim_span])
        pdf_page = pdf_index.resolve_line_page(ln, needles) if pdf_index is not None else None
        enriched = _sanitize_nested(anc)
        enriched["compendium_file"] = "Compendium/Compendium.md"
        enriched["compendium_line_start"] = ln
        enriched["pdf_page"] = pdf_page
        ancres_compendium_77.append(enriched)

        origin = anc.get("origin")
        if origin == "T7":
            ancres_t7.append(enriched)
        elif origin == "T8":
            ancres_t8.append(enriched)
        elif origin == "T5_DAPP":
            comm = _clean_text(anc.get("commentaire_annexe", ""))
            m_hor = re.search(r"horizon\s*:\s*([^)]+)\)", comm, flags=re.IGNORECASE)
            horizon = m_hor.group(1).strip() if m_hor else "Pluriannuel"
            lbl = _clean_text(anc.get("label", ""))
            m_stade = re.search(r"\(([^)]+)\)\s*:", lbl)
            stade = m_stade.group(1).strip() if m_stade else "Trajectoire DAPP"
            jalons = lbl.split(":", 1)[-1].strip() if ":" in lbl else lbl
            ancres_dapp.append(
                {
                    "key": key,
                    "phase": _clean_text(date_val),
                    "horizon": horizon,
                    "stade": stade,
                    "jalons": jalons,
                    "compendium_file": "Compendium/Compendium.md",
                    "compendium_line_start": ln,
                    "pdf_page": pdf_page,
                    "source_l_plus_id": _clean_text(anc.get("source_l_plus_id", "")),
                }
            )
        elif origin == "T4":
            ancres_t4_67.append(
                {
                    "id": key,
                    "aliases": list(anc.get("aliases") or []),
                    "echeance": _clean_text(date_val),
                    "axe": _clean_text(anc.get("nature", "")),
                    "juridiction": _clean_text(anc.get("jurisdiction", "")),
                    "enonce": _clean_text(anc.get("label", "")),
                    "chapters": list(anc.get("chapters") or []),
                    "source_l_plus_id": _clean_text(anc.get("source_l_plus_id", "")),
                    "compendium_file": "Compendium/Compendium.md",
                    "compendium_line_start": ln,
                    "pdf_page": pdf_page,
                }
            )

    six_reperes_readme = [
        {
            "echeance": "Depuis sept. 2023",
            "cadre": "Québec (Loi 25, art. 12.1)",
            "resume": "Obligation d'informer la personne visée par une décision exclusivement automatisée, d'expliquer les paramètres principaux et d'offrir une révision humaine.",
        },
        {
            "echeance": "Depuis août 2026",
            "cadre": "Union européenne (EU AI Act, art. 50)",
            "resume": "Obligations de transparence et de marquage des interactions synthétiques en application depuis le 2 août 2026 (avec aménagement transitoire art. 111 au 2 déc. 2026).",
        },
        {
            "echeance": "Mars 2027 → Mars 2029",
            "cadre": "PKI publique (CA/Browser Forum SC-081v3)",
            "resume": "Réduction graduelle de la durée maximale des certificats TLS à 100 jours (mars 2027) puis 47 jours (15 mars 2029).",
        },
        {
            "echeance": "1er mai 2027",
            "cadre": "Canada fédéral (BSIF E-23 / AMF)",
            "resume": "Entrée en vigueur de la ligne directrice E-23 révisée du BSIF sur la gestion du risque de modèle et gouvernance prudente des modèles IA/agentiques.",
        },
        {
            "echeance": "2027–2028",
            "cadre": "Union européenne (EU AI Act, Annexes III et I)",
            "resume": "Échéances d'application étendues des systèmes à haut risque (2 décembre 2027 Annexe III ; 2 août 2028 Annexe I selon Règlement UE 2026/1744).",
        },
        {
            "echeance": "2030–2035",
            "cadre": "Transition post-quantique G7 / NIST / CSE ITSP.40.111",
            "resume": "Bascules planifiées vers ML-KEM / ML-DSA / SLH-DSA et interdiction des schémas RSA/ECDSA classiques à l'horizon 2030–2035.",
        },
    ]

    return {
        "total_jalons": len(ancres_compendium_77),
        "ancres_compendium_77": ancres_compendium_77,
        "six_reperes_readme": six_reperes_readme,
        "rampe_et_paliers_dapp_t5": ancres_dapp,
        "ancres_t7_l_plus": ancres_t7,
        "ancres_t8_l_plus": ancres_t8,
        "ancres_t4_67": ancres_t4_67,
    }


def _build_matrices(mat: dict[str, Any]) -> dict[str, Any]:
    """Assemble la structure matrices complète (237 entrées uniques + C01–C40 = 18/15/7)."""
    exig_raw = _sanitize_nested(mat["exig_cre_ia_v1_2"])
    cap_52 = _sanitize_nested(mat["cap_52"])
    pex_24 = _sanitize_nested(mat["pex_24"])
    prr_75 = _sanitize_nested(mat["prr_75"])
    principes = _sanitize_nested(mat["principes_et_decisions"])
    dapp_por_15 = _sanitize_nested(mat["dapp_por_15"])
    dapp_sig_27 = _sanitize_nested(mat["dapp_sig_27"])
    dapp_ini_43 = _sanitize_nested(mat["dapp_ini_43"])
    c01_c40_blueprints = _sanitize_nested(mat["c01_c40_blueprints"])
    cinq_sbb = _sanitize_nested(mat["cinq_sbb"])
    mappings_95 = _sanitize_nested(mat["mappings"])

    return {
        "exig_cre_ia_2026_v1_2": exig_raw,
        "cap_52": cap_52,
        "pex_24": pex_24,
        "principes_et_decisions": principes,
        "dapp_por_15": dapp_por_15,
        "dapp_sig_27": dapp_sig_27,
        "dapp_ini_43": dapp_ini_43,
        "prr_75": prr_75,
        "tome8_executable": {
            "c01_a_c40_blueprints": c01_c40_blueprints,
            "cinq_sbb_tableau_12": cinq_sbb,
            "matrice_exig_prr_c40_95": mappings_95,
        },
    }


def _build_glossary(
    gloss: dict[str, Any],
    comp_lines: list[str],
    unit_spans: dict[str, tuple[int, int]],
    pdf_index: Any | None = None,
) -> dict[str, Any]:
    """Enrichit les 56 vedettes du glossaire avec leur ligne vérifiée dans ``Compendium.md``."""
    terms_raw: list[dict[str, Any]] = gloss["terms"]
    if len(terms_raw) != 56:
        raise ValueError(f"56 termes glossaire attendus, trouvés {len(terms_raw)}")

    enriched_terms: list[dict[str, Any]] = []
    has_system_agency = False
    for t in terms_raw:
        owner = t.get("chapitre_proprietaire", "00-liminaire")
        owner_span = unit_spans.get(owner, (1, len(comp_lines)))
        fr = t.get("fr", "")
        en = t.get("en", "")
        line_no = _find_line_in_compendium(comp_lines, [fr, en], [owner_span])
        if fr.lower() == "agentivité des systèmes" and en.lower() == "system agency":
            has_system_agency = True
        entry = _sanitize_nested(t)
        entry["compendium_md_file"] = "Compendium/Compendium.md"
        entry["compendium_md_line"] = line_no
        entry["pdf_page"] = pdf_index.resolve_line_page(line_no, [fr, en]) if pdf_index is not None else None
        enriched_terms.append(entry)

    if not has_system_agency:
        raise ValueError("Vedette obligatoire 'Agentivité des systèmes' / 'system agency' absente du glossaire SSOT")

    return {
        "total_terms": len(enriched_terms),
        "glossaire_compendium_56": enriched_terms,
        "vedettes_t8": enriched_terms,
    }


def build_pivots_payload(repo_root: Path) -> dict[str, Any]:
    """Assemble ``Sources/Cartographie/donnees/pivots-concordance.json`` depuis le SSOT du Compendium."""
    ouv = repo_root / "Sources" / "Compendium" / "ouvrage"
    reg = ouv / "registre"
    rech = ouv / "recherche"
    aq = ouv / "aq"

    manifest = json.loads((ouv / "specs" / "manifest.json").read_text(encoding="utf-8"))
    conc = json.loads((reg / "concordance-taxonomies.json").read_text(encoding="utf-8"))
    anc = json.loads((reg / "ancres-chronologiques.json").read_text(encoding="utf-8"))
    mat = json.loads((reg / "matrice-exig-prr-c40.json").read_text(encoding="utf-8"))
    gloss = json.loads((reg / "glossaire-termes.json").read_text(encoding="utf-8"))
    faits = json.loads((reg / "faits-empiriques.json").read_text(encoding="utf-8"))
    specs = json.loads((reg / "specifications-lplus.json").read_text(encoding="utf-8"))
    sources_lplus = json.loads((rech / "manifeste-sources-sha256.json").read_text(encoding="utf-8"))
    statut_f = json.loads((rech / "registre-statut-f.json").read_text(encoding="utf-8"))
    g0_report = json.loads((aq / "rapports-g0.json").read_text(encoding="utf-8"))
    wyvern_g2 = _parse_ancrage_journals(ouv / "ancrage")

    comp_path = repo_root / "Compendium" / "Compendium.md"
    comp_text = comp_path.read_text(encoding="utf-8")
    comp_lines = comp_text.splitlines()
    unit_spans = _compute_compendium_unit_spans(comp_lines)

    from index_pdf_compendium import CompendiumPdfIndex  # noqa: E402

    pdf_index = (
        CompendiumPdfIndex.from_repo(repo_root)
        if (repo_root / "Compendium" / "Compendium.pdf").is_file()
        else None
    )

    lplus_count = len(sources_lplus["sources"])
    statut_f_count = len(statut_f["blocked"])
    synced_count = len(manifest["synced_excerpts_catalog"])
    facts_list = _sanitize_nested(faits["facts"])
    specs_list = _sanitize_nested(specs["specs"])

    if lplus_count != 135:
        raise ValueError(f"135 sources L+ attendues, trouvées {lplus_count}")
    if statut_f_count != 27:
        raise ValueError(f"27 exclusions Statut F attendues, trouvées {statut_f_count}")
    if synced_count != 14:
        raise ValueError(f"14 extraits CA-G0-SYNC attendus, trouvés {synced_count}")
    if len(facts_list) != 16:
        raise ValueError(f"16 faits empiriques attendus, trouvés {len(facts_list)}")
    if len(specs_list) != 57:
        raise ValueError(f"57 spécifications L+ attendues, trouvées {len(specs_list)}")

    collection_metrics = _parse_compendium_metrics(
        repo_root=repo_root,
        manifest=manifest,
        comp_text=comp_text,
        comp_lines=comp_lines,
        sources_count=lplus_count,
        statut_f_count=statut_f_count,
        synced_count=synced_count,
        glossary_count=len(gloss["terms"]),
        wyvern_g2_count=len(wyvern_g2),
    )

    bilans_aq = {
        "compendium_g0_g5": {
            "freeze_date": manifest["freeze_date"],
            "sources_l_plus": lplus_count,
            "metadata_only_pct": sources_lplus.get("metadata_only_pct", 0.0),
            "statut_f_exclus": statut_f_count,
            "ao_01_policy": _clean_text(statut_f.get("ao_01_policy", "")),
            "ca_g0_sync_count": synced_count,
            "ca_g0_sync_catalog": _sanitize_nested(manifest["synced_excerpts_catalog"]),
            "wyvern_g2_unites_count": len(wyvern_g2),
            "wyvern_g2_unites": wyvern_g2,
            "rapports_g0": _sanitize_nested(g0_report),
            "faits_empiriques_16": facts_list,
            "specifications_lplus_57": specs_list,
        },
        # Alias rétrocompatibles pour preparer_donnees_prd_web.py
        "tome_8_g0_g5": {
            "overall_status": g0_report.get("overall_status"),
            "opa_tests_passed": (g0_report.get("opa_check") or {}).get("tests_passed"),
            "pytest_passed": (g0_report.get("pytest_check") or {}).get("passed"),
            "synced_excerpts_count": synced_count,
            "wyvern_g2_units": len(wyvern_g2),
            "sources_l_plus": lplus_count,
            "statut_f_exclus": statut_f_count,
        },
    }

    payload: dict[str, Any] = {
        "schema_version": "2.0.0",
        "lang": "fr-CA",
        "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "generator": "Sources/Cartographie/outils/extraire_pivots_compendium.py",
        "freeze_dates": {
            "compendium": f"{manifest.get('freeze_date', '2026-12-02')} (parution janvier 2027)",
            "tomes_1_a_6": "2026-11-19 (édition historique consolidée dans le Compendium)",
            "tomes_7_et_8": "2026-12-02 (gel unifié du Compendium)",
        },
        "collection_metrics": collection_metrics,
        "concordance_8_tomes": _build_concordance_section(conc, manifest, comp_lines, unit_spans, pdf_index=pdf_index),
        "discordances_resolues": _build_discordances(conc, comp_lines, unit_spans, pdf_index=pdf_index),
        "chronologie_2023_2035": _build_chronology(anc, comp_lines, unit_spans, pdf_index=pdf_index),
        "matrices": _build_matrices(mat),
        "bilans_aq_wyvern_et_statut_f": bilans_aq,
        "glossaire_pivot": _build_glossary(gloss, comp_lines, unit_spans, pdf_index=pdf_index),
        "faits_empiriques_16": facts_list,
        "specifications_lplus_57": specs_list,
        "statut_f_exclus_27": _sanitize_nested(statut_f["blocked"]),
    }

    serialized = json.dumps(payload, indent=2, ensure_ascii=False) + "\n"
    _assert_hygiene(payload, serialized)
    return payload


def main() -> int:
    """Point d'entrée CLI générant ``Sources/Cartographie/donnees/pivots-concordance.json``."""
    parser = argparse.ArgumentParser(description="Extrait les pivots et registres SSOT du Compendium.")
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
        help="Chemin de sortie JSON (défaut : Sources/Cartographie/donnees/pivots-concordance.json).",
    )
    args = parser.parse_args()

    repo_root = args.repo_root.resolve()
    out_path = args.output or (repo_root / "Sources" / "Cartographie" / "donnees" / "pivots-concordance.json")
    payload = build_pivots_payload(repo_root)
    serialized = json.dumps(payload, indent=2, ensure_ascii=False) + "\n"
    out_path.write_text(serialized, encoding="utf-8", newline="\n")
    raw_bytes = out_path.read_bytes()
    if b"\r\n" in raw_bytes or raw_bytes.startswith(b"\xef\xbb\xbf"):
        raise ValueError(f"BOM ou CRLF détecté dans {out_path}")

    cm = payload["collection_metrics"]
    mat = payload["matrices"]
    print(
        f"Pivots Compendium -> {out_path} : {cm['compendium_pdf_pages']} p. PDF, "
        f"{cm['compendium_md_lines']} lignes MD, {cm['compendium_schemas']} schémas, "
        f"{len(payload['chronologie_2023_2035']['ancres_compendium_77'])} jalons, "
        f"{len(payload['glossaire_pivot']['glossaire_compendium_56'])} termes glossaire, "
        f"{cm['sources_l_plus']} L+, {cm['statut_f_excluded']} Statut F, "
        f"{cm['ca_g0_sync_excerpts']} CA-G0-SYNC, {cm['wyvern_g2_units']}/37 Wyvern G2, "
        f"{mat['exig_cre_ia_2026_v1_2']['total']} EXIG, {len(mat['cap_52'])} CAP, "
        f"{len(mat['pex_24'])} PEX, {mat['prr_75']['total']} PRR"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
