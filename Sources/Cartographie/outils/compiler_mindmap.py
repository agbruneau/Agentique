#!/usr/bin/env python3
"""Compilateur du bundle de données et de la MindMap HTML autonome du Corpus Agentique.

Fusionne :
- ``Cartographie/donnees/schema-cartographie.json``
- ``Cartographie/donnees/structure-integrale.json``
- ``Cartographie/donnees/pivots-concordance.json``
- ``Cartographie/donnees/synthese-transversale.json``
- ``Cartographie/outils/template_mindmap.html``

Produit :
- ``Cartographie/donnees/corpus-mindmap-data.json``
- ``Cartographie/MindMap - Cartographie thématique du Corpus.html``
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import re
import sys
from typing import Any, Callable

PAGE_TITLE = "MindMap — Cartographie thématique du Corpus Agentique (Tomes 1 à 8)"
TOME_ORDER: dict[str, int] = {"R": 0, "T1": 1, "T2": 2, "T3": 3, "T4": 4, "T5": 5, "T6": 6, "T7": 7, "T8": 8}


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


def normalize_pivots(raw_pivots: dict[str, Any]) -> dict[str, Any]:
    """Normalise les pivots de concordance pour les 4 sous-onglets de la Vue 4."""
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
            "file": "Tomes/Tome 5 - Synthèse exécutive et concordance architecturale.md",
            "line_start": 19,
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
        reconciliations.append(
            {
                "id": entry.get("discordance_id", ""),
                "title": clean_prose_typography(entry.get("topic", "")),
                "section": f"Tome 8 §{entry.get('liminaire_section', '0.2')}",
                "resolution": clean_prose_typography(entry.get("canonical_vol8_choice", "")),
                "rationale": clean_prose_typography(entry.get("rationale", "")),
                "variants": variants_clean,
                "file": "Tomes/Tome 8 - Ingénierie exécutable et homologation vérifiable.md",
                "line_start": 34,
            }
        )

    raw_tl = raw_pivots.get("chronologie_2023_2035") or {}
    raw_mat = raw_pivots.get("matrices") or {}

    if raw_tl and raw_mat:
        tools_str = str(Path(__file__).resolve().parent)
        if tools_str not in sys.path:
            sys.path.insert(0, tools_str)
        from preparer_donnees_prd_web import (  # noqa: E402
            _build_consolidated_timeline,
            _build_unified_matrix,
        )

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
        mat_unified, matrix_distribution, matrix_totals = _build_unified_matrix(raw_pivots)
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


def build_mindmap_bundle(
    schema: dict[str, Any],
    structure: dict[str, Any],
    pivots: dict[str, Any],
    synthese: dict[str, Any],
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

    normalized_pivots = normalize_pivots(pivots)

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
        },
        "nodes": nodes,
        "relations": relations,
        "chapters": chapters,
        "concordance_matrix": concordance_matrix,
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
    template_html = (outils_dir / "template_mindmap.html").read_text(encoding="utf-8")

    bundle = build_mindmap_bundle(schema, structure, pivots, synthese)

    outils_str = str(outils_dir)
    if outils_str not in sys.path:
        sys.path.insert(0, outils_str)
    from preparer_donnees_prd_web import build_prd_web_payload  # noqa: E402

    bundle["prd"] = build_prd_web_payload(repo_root, bundle=bundle)

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

    html_out = repo_root / "Sources" / "Cartographie" / "MindMap - Cartographie thématique du Corpus.html"
    html_out.write_text(compiled_html, encoding="utf-8", newline="\n")

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
    prd_c = len((bundle.get("prd") or {}).get("chapters") or [])
    print(
        f"Compilation réussie : {t['theme_nodes']} thèmes ({t['nodes']} nœuds), "
        f"{t['relations']} interrelations, {t['headings']} titres H1–H6, "
        f"{len(bundle['pivots']['reconciliations'])} discordances, "
        f"{len(bundle['pivots']['timeline'])} jalons, "
        f"{len(bundle['pivots']['traceability_matrix'])} entrées traçabilité, "
        f"{prd_c} chapitres PRD -> "
        f"{data_out} & {html_out} ({html_out.stat().st_size} octets)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
