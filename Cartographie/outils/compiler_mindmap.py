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
import sys
from typing import Any

PAGE_TITLE = "MindMap — Cartographie thématique du Corpus Agentique (Tomes 1 à 8)"


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
            "title": raw_div02.get("objet", "Fermeture de DIV-02"),
            "statut": raw_div02.get("statut", "Fermée"),
            "resolution": raw_div02.get("source", ""),
            "rectifications": raw_div02.get("trois_rectifications", []),
            "coquilles": raw_div02.get("quatre_coquilles_cad26_v1_1_rectifiees", []),
            "bilan_chiffre": raw_div02.get("bilan_chiffre", {}),
            "file": "Corpus/Tome 5 - Synthèse exécutive et concordance architecturale.md",
            "line_start": 19,
        }

    reconciliations: list[dict[str, Any]] = []
    cinq_disc = disc_block.get("cinq_discordances_tome_8") or {}
    for entry in cinq_disc.get("entries", []):
        reconciliations.append(
            {
                "id": entry.get("discordance_id", ""),
                "title": entry.get("topic", ""),
                "section": f"Tome 8 §{entry.get('liminaire_section', '0.2')}",
                "resolution": entry.get("canonical_vol8_choice", ""),
                "rationale": entry.get("rationale", ""),
                "variants": entry.get("volume_variants", []),
                "file": "Corpus/Tome 8 - Ingénierie exécutable et homologation vérifiable.md",
                "line_start": 34,
            }
        )

    raw_tl = raw_pivots.get("chronologie_2023_2035") or {}
    timeline: list[dict[str, Any]] = []
    for rep in raw_tl.get("six_reperes_readme", []):
        timeline.append(
            {
                "date": rep.get("echeance", ""),
                "cadre": rep.get("cadre", ""),
                "impact": rep.get("resume", ""),
                "tomes": ["R", "T4", "T7"],
                "file": "Corpus/README.md",
                "line_start": 24,
                "source_group": "Repères clés",
            }
        )
    for pal in raw_tl.get("rampe_et_paliers_dapp_t5", []):
        timeline.append(
            {
                "date": f"{pal.get('horizon', '')} ({pal.get('phase', '')})",
                "cadre": f"DAPP · {pal.get('stade', '')}",
                "impact": pal.get("jalons", ""),
                "tomes": ["T4", "T5"],
                "file": "Corpus/Tome 5 - Synthèse exécutive et concordance architecturale.md",
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
                "file": "Corpus/Tome 7 - Gouverner l'industrialisation cognitive.md",
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
                "file": "Corpus/Tome 8 - Ingénierie exécutable et homologation vérifiable.md",
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
                "file": "Corpus/Tome 4 - Prospective stratégique et trajectoire 2028-2035.md",
                "line_start": 5175,
                "source_group": "Tome 4 Annexe A",
            }
        )

    raw_mat = raw_pivots.get("matrices") or {}
    traceability_matrix: list[dict[str, Any]] = []
    t8_exec = raw_mat.get("tome8_executable") or {}
    for row in t8_exec.get("matrice_exig_prr_c40_95", []):
        traceability_matrix.append(
            {
                "id": row.get("id", ""),
                "family": f"{row.get('family', '')} ({row.get('criticality', '')})",
                "title": row.get("pytest_nodeid") or row.get("rego_rule") or "",
                "module": f"{row.get('trousse_module', '')}.{row.get('implementation_symbol', '')}",
                "anchor": row.get("corpus_anchor", ""),
            }
        )
    for sbb in t8_exec.get("cinq_sbb_tableau_12", []):
        traceability_matrix.append(
            {
                "id": sbb.get("sbb_id", ""),
                "family": f"5 SBB ({sbb.get('plan', '')})",
                "title": sbb.get("slot", ""),
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
                "title": item.get("point_controle", ""),
                "module": item.get("artefact_preuve", ""),
                "anchor": f"Grille {item.get('grid', '')}",
            }
        )
    for cap in raw_mat.get("cap_52", []):
        exigs = ", ".join(cap.get("exigences_cad26", [])[:6])
        traceability_matrix.append(
            {
                "id": cap.get("cap_id", ""),
                "family": f"CAP ({cap.get('statut', '')} · {cap.get('palier', '')})",
                "title": cap.get("nom") or cap.get("intitule_condense", ""),
                "module": exigs or cap.get("type_rattachement_cad26", ""),
                "anchor": cap.get("emplacement", ""),
            }
        )
    for pex in raw_mat.get("pex_24", []):
        traceability_matrix.append(
            {
                "id": pex.get("pex_id", ""),
                "family": f"PEX ({pex.get('sous_secteur', '')})",
                "title": pex.get("titre", ""),
                "module": ", ".join(pex.get("exigences_cad26", [])[:5]),
                "anchor": pex.get("chapitre_t4", ""),
            }
        )
    exig_meta = raw_mat.get("exig_cre_ia_2026_v1_2") or {}
    for fam in exig_meta.get("familles", []):
        if isinstance(fam, dict):
            traceability_matrix.append(
                {
                    "id": fam.get("prefixe") or fam.get("code", ""),
                    "family": "CRE-IA-2026-01 (Famille EXIG)",
                    "title": fam.get("titre") or fam.get("domaine") or "",
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
    donnees_dir = repo_root / "Cartographie" / "donnees"
    outils_dir = repo_root / "Cartographie" / "outils"

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
    )

    minified_json = json.dumps(bundle, ensure_ascii=False, separators=(",", ":"))
    safe_json = escape_json_for_script(minified_json)

    if template_html.count("__CORPUS_DATA_JSON__") != 1:
        raise ValueError("Marqueur __CORPUS_DATA_JSON__ doit apparaître exactement une fois dans template_mindmap.html")

    compiled_html = template_html.replace("__PAGE_TITLE__", PAGE_TITLE).replace(
        "__CORPUS_DATA_JSON__", safe_json, 1
    )

    html_out = repo_root / "Cartographie" / "MindMap - Cartographie thématique du Corpus.html"
    html_out.write_text(compiled_html, encoding="utf-8")

    return data_out, html_out, bundle


def main() -> int:
    """Point d'entrée CLI pour la compilation MindMap."""
    parser = argparse.ArgumentParser(
        description="Compile corpus-mindmap-data.json et la MindMap HTML autonome."
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path(__file__).resolve().parents[2],
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
