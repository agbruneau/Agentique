#!/usr/bin/env python3
"""Parseur dynamique de ``Compendium/plan.md`` et sonde de ``Compendium/ouvrage/``.

Produit la charge JSON consommée par le tableau de bord web local de suivi de
progression du Compendium, sans aucune dépendance externe à la bibliothèque
standard Python.
"""

from __future__ import annotations

import csv
from datetime import datetime, timezone
import io
import json
import math
from pathlib import Path
import re
import subprocess
from typing import Any

STEP_LINE_RE = re.compile(r"^(\s*-\s+\[)([ xX])(\]\s+)(.*)$")
TASK_HEADING_RE = re.compile(r"^###\s+Task\s+(\d+)\s*:\s*(.+)$")
PARTIE_HEADING_RE = re.compile(r"^###\s+Partie\s+([IVX]+)\s+—\s+(D\d{2})\s*:\s*(.+)$")
FICHE_HEADING_RE = re.compile(r"^####\s+Fiche\s+(CH-\d{2})\s+—\s+Chapitre\s+(\d{2})\s*:\s*(.+)$")
ANNEXE_HEADING_RE = re.compile(r"^###\s+4\.(\d+)\s+Annexe\s+([A-E])\s+—\s+(.+)$")
MD_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
SCHEMA_ID_RE = re.compile(r"\bSCH-\d{2}-\d{2}\b")
FAM_ID_RE = re.compile(r"\bFAM_D\d{2}_\d{2}_\d{2}\b")
THM_ID_RE = re.compile(r"\bTHM_([a-z0-9-]+)\b")
EXIG_ID_RE = re.compile(r"\b(?:EXIG-[A-Z0-9-]+|CAP-\d{3}|PEX-\d{3}|PRR-\d+|C\d{2}|SBB-[A-Z0-9-]+)\b")

OUVRAGE_SUBDIRS: tuple[tuple[str, str], ...] = (
    ("specs", "Spécifications (manifest.json, protocole MLR)"),
    ("outils", "Outillage déterministe Python (G0/G1/G3/annexes)"),
    ("registre", "7 registres JSON SSOT"),
    ("recherche", "Corpus primaire ouvert L+ haché SHA-256"),
    ("sources", "37 bases fermées ch00..ch36-sources.md"),
    ("schemas", "115 schémas de vulgarisation + rendus/"),
    ("manuscrit", "42 unités rédigées (180 000 mots ± 8 %)"),
    ("ancrage", "37 journaux Wyvern G2 ch00..ch36-ancrage.md"),
    ("aq", "Rapports G0, G3 (2 passes), G4 et visuel G5"),
    ("livrables", "Éditions finales Compendium.{md,html,pdf}"),
)

EXPECTED_REGISTRES: tuple[str, ...] = (
    "mindmap-complet.json",
    "specifications-lplus.json",
    "matrice-exig-prr-c40.json",
    "concordance-taxonomies.json",
    "ancres-chronologiques.json",
    "faits-empiriques.json",
    "glossaire-termes.json",
)

EXPECTED_OUTILS: tuple[str, ...] = (
    "_communs.py",
    "verifie_specs.py",
    "verifie_manuscrit.py",
    "echantillon_aq.py",
    "genere_annexes.py",
    "execute_g0.py",
    "collecte_mlr_ouverte.py",
    "compile_schemas_compendium.py",
    "assemble_livre.py",
)

EXPECTED_DELIVERABLES: tuple[tuple[str, str], ...] = (
    ("Compendium.md", "Markdown consolidé intégral"),
    ("Compendium.html", "HTML autonome hors ligne (--embed-resources)"),
    ("Compendium.pdf", "PDF Typst imprimable (6,14 × 9,21 po)"),
)

EXPECTED_REVISION_REPORTS: tuple[tuple[str, str], ...] = (
    ("audit-references-viabilite.md", "Audit viabilité & fiabilité des références (REV-02)"),
    ("audit-prd-lot1.md", "Audit PRD — Lot 1 (Liminaire + Parties I–III)"),
    ("audit-prd-lot2.md", "Audit PRD — Lot 2 (Parties IV–VI)"),
    ("audit-prd-lot3.md", "Audit PRD — Lot 3 (Parties VII–IX)"),
    ("audit-prd-lot4.md", "Audit PRD — Lot 4 (Parties X–XII + Annexes + Schémas)"),
    ("rapport-audit-revision-prd.md", "Rapport consolidé d'audit & révision PRD (REV-06)"),
)


def parse_int_fr(text: str) -> int:
    """Convertit un entier formaté en français (espaces fines/insécables, backticks)."""
    digits = re.sub(r"[^\d]", "", str(text or ""))
    return int(digits) if digits else 0


def strip_md_inline(text: str) -> str:
    """Retire les marqueurs Markdown légers pour l'affichage tabulaire sans altérer ``*`` dans les motifs ``SCH-*``."""
    cleaned = MD_LINK_RE.sub(r"\1", str(text or ""))
    cleaned = cleaned.replace("`", "")
    cleaned = re.sub(r"\*\*([^*]+)\*\*", r"\1", cleaned)
    cleaned = re.sub(r"(?<![\w-])\*([^*\n]+)\*(?!\w)", r"\1", cleaned)
    return cleaned.strip()


def count_prose_words(markdown_text: str) -> int:
    """Compte les mots de prose hors front matter YAML, blocs de code, commentaires, marqueurs `#` et URLs."""
    text = markdown_text.replace("\r\n", "\n")
    if text.startswith("---\n"):
        end_fm = text.find("\n---\n", 4)
        if end_fm != -1:
            text = text[end_fm + 5 :]
    text = re.sub(r"<!--\s*BIBLIOGRAPHIE_BRUTE_DEBUT\s*-->[\s\S]*?<!--\s*BIBLIOGRAPHIE_BRUTE_FIN\s*-->", " ", text)
    text = re.sub(r"<!--[\s\S]*?-->", " ", text)
    lines = text.splitlines()
    kept: list[str] = []
    in_fence = False
    fence_char = ""
    for line in lines:
        stripped = line.lstrip()
        if not in_fence and (stripped.startswith("```") or stripped.startswith("~~~")):
            in_fence = True
            fence_char = stripped[:3]
            continue
        if in_fence:
            if stripped.startswith(fence_char):
                in_fence = False
            continue
        no_heading_hashes = re.sub(r"^\s*#{1,6}\s+", "", line)
        no_links = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", no_heading_hashes)
        no_urls = re.sub(r"https?://\S+", " ", no_links)
        kept.append(no_urls)
    return len(" ".join(kept).split())


def _split_md_table_row(line: str) -> list[str]:
    stripped = line.strip()
    if stripped.startswith("|"):
        stripped = stripped[1:]
    if stripped.endswith("|") and not stripped.endswith("\\|"):
        stripped = stripped[:-1]
    return [cell.replace("\\|", "|").strip() for cell in re.split(r"(?<!\\)\|", stripped)]


def _parse_markdown_table(lines: list[str], start_idx: int) -> tuple[list[dict[str, str]], int]:
    """Parse un tableau GFM à partir de la ligne d'en-tête ``start_idx`` (0-based)."""
    if start_idx + 1 >= len(lines):
        return [], start_idx
    headers = [strip_md_inline(h) for h in _split_md_table_row(lines[start_idx])]
    rows: list[dict[str, str]] = []
    idx = start_idx + 2
    while idx < len(lines) and lines[idx].strip().startswith("|"):
        cells = _split_md_table_row(lines[idx])
        if len(cells) == len(headers):
            rows.append(dict(zip(headers, cells)))
        idx += 1
    return rows, idx


def _find_table_after(lines: list[str], heading_prefix: str, header_contains: str) -> list[dict[str, str]]:
    """Trouve le premier tableau GFM contenant ``header_contains`` après ``heading_prefix``."""
    in_section = not heading_prefix
    for i, line in enumerate(lines):
        if heading_prefix and line.startswith(heading_prefix):
            in_section = True
            continue
        if in_section and line.strip().startswith("|") and header_contains in line:
            if i + 1 < len(lines) and re.match(r"^\s*\|?[\s:-]+(?:\|[\s:-]+)+\|?\s*$", lines[i + 1]):
                rows, _ = _parse_markdown_table(lines, i)
                return rows
    return []


def _extract_meta_field(text: str, label: str, default: str = "") -> str:
    m = re.search(rf"\*\*{re.escape(label)}\*\*\s*:\s*`?([^·\n`]+)`?", text)
    return m.group(1).strip() if m else default


def _extract_blockquote_bullet(text: str, label: str) -> str:
    m = re.search(rf"^>\s*-\s*\*\*{re.escape(label)}\*\*\s*:\s*(.+)$", text, flags=re.MULTILINE)
    return strip_md_inline(m.group(1)) if m else ""


def _parse_units_table(lines: list[str]) -> list[dict[str, Any]]:
    rows = _find_table_after(lines, "### 1.4", "Unité")
    units: list[dict[str, Any]] = []
    for row in rows:
        raw_unit = row.get("Unité", "")
        if "Total" in raw_unit:
            continue
        link_m = MD_LINK_RE.search(raw_unit)
        unit_label = strip_md_inline(link_m.group(1) if link_m else raw_unit)
        prd_link = link_m.group(2) if link_m else ""
        prd_anchor = prd_link.partition("#")[2] if "#" in prd_link else ""

        dom_cell = row.get("Domaine / Sous-domaine", "")
        dom_parts = [strip_md_inline(p) for p in dom_cell.split("/", 1)]
        domain_id = dom_parts[0] if dom_parts else ""
        subdomain_id = dom_parts[1] if len(dom_parts) > 1 else ""

        if unit_label.startswith("00"):
            unit_type = "liminaire"
            unit_code = "CH-00"
            order_idx = 0
        elif unit_label.startswith("CH-"):
            unit_type = "chapitre"
            unit_code = unit_label
            order_idx = int(unit_label.split("-")[1])
        else:
            unit_type = "annexe"
            letter = unit_label.replace("Annexe", "").strip()
            unit_code = f"ANN-{letter}"
            order_idx = 100 + (ord(letter[0]) - ord("A")) if letter else 100

        sch_cell = row.get("Schémas SCH-*", "")
        schema_ids = SCHEMA_ID_RE.findall(sch_cell)
        if unit_type == "liminaire" and len(schema_ids) == 2 and schema_ids[0] == "SCH-00-01" and schema_ids[1] == "SCH-00-04":
            schema_ids = ["SCH-00-01", "SCH-00-02", "SCH-00-03", "SCH-00-04"]

        target_words = parse_int_fr(row.get("Cible (mots)", "0"))
        range_cell = row.get("Plage [min, max]", "")
        range_nums = re.findall(r"\d[\d\s\u00a0\u202f]*", range_cell)
        min_words = parse_int_fr(range_nums[0]) if len(range_nums) >= 1 else math.ceil(0.92 * target_words)
        max_words = parse_int_fr(range_nums[1]) if len(range_nums) >= 2 else math.floor(1.08 * target_words)

        units.append({
            "order": order_idx,
            "unit_id": unit_label,
            "unit_code": unit_code,
            "unit_type": unit_type,
            "title": unit_label,
            "domain_id": domain_id,
            "subdomain_id": subdomain_id,
            "prd_anchor": prd_anchor,
            "families_count": parse_int_fr(row.get("Familles", "0")),
            "themes_count": parse_int_fr(row.get("Thèmes", "0")),
            "schema_ids": schema_ids,
            "target_words": target_words,
            "min_words": min_words,
            "max_words": max_words,
            "part_roman": "",
            "part_title": "",
            "families": [],
            "themes": [],
            "requirements": [],
            "deliverables_summary": "",
        })
    return units


def _parse_tasks(lines: list[str]) -> list[dict[str, Any]]:
    tasks: list[dict[str, Any]] = []
    task_starts: list[tuple[int, int, str]] = []
    sec3_idx = len(lines)
    for idx, line in enumerate(lines):
        if line.startswith("## 3. "):
            sec3_idx = idx
            break
        m = TASK_HEADING_RE.match(line)
        if m:
            task_starts.append((idx, int(m.group(1)), strip_md_inline(m.group(2))))

    for pos, (start_idx, task_num, task_title) in enumerate(task_starts):
        end_idx = task_starts[pos + 1][0] if pos + 1 < len(task_starts) else sec3_idx
        block_lines = lines[start_idx:end_idx]

        files: list[str] = []
        consumes: list[str] = []
        produces: list[str] = []
        mode = ""
        steps: list[dict[str, Any]] = []

        for offset, raw in enumerate(block_lines):
            abs_line = start_idx + offset + 1
            stripped = raw.strip()
            if stripped == "**Files:**":
                mode = "files"
                continue
            if stripped == "**Interfaces:**":
                mode = "interfaces"
                continue
            step_m = STEP_LINE_RE.match(raw)
            if step_m:
                mode = "step"
                checked = step_m.group(2).lower() == "x"
                label = strip_md_inline(step_m.group(4))
                steps.append({
                    "id": f"T{task_num}-S{len(steps) + 1}",
                    "task_number": task_num,
                    "step_number": len(steps) + 1,
                    "line_no": abs_line,
                    "label": label,
                    "checked": checked,
                    "command": "",
                    "expected": "",
                })
                continue

            if mode == "files" and stripped.startswith("- "):
                files.append(strip_md_inline(stripped[2:]))
            elif mode == "interfaces":
                if stripped.startswith("- Consumes:"):
                    consumes.append(strip_md_inline(stripped.split(":", 1)[1]))
                elif stripped.startswith("- Produces:"):
                    val = stripped.split(":", 1)[1].strip()
                    if val:
                        produces.append(strip_md_inline(val))
                elif stripped.startswith("- ") and produces is not None:
                    produces.append(strip_md_inline(stripped[2:]))
            elif mode == "step" and steps:
                if stripped.startswith("Run:"):
                    steps[-1]["command"] = stripped.split(":", 1)[1].strip().strip("`")
                elif stripped.startswith("Expected:"):
                    steps[-1]["expected"] = strip_md_inline(stripped.split(":", 1)[1])

        done_cnt = sum(1 for s in steps if s["checked"])
        total_cnt = len(steps)
        tasks.append({
            "task_number": task_num,
            "task_id": f"Task {task_num}",
            "title": task_title,
            "start_line": start_idx + 1,
            "end_line": end_idx,
            "files": files,
            "consumes": consumes,
            "produces": produces,
            "steps": steps,
            "steps_done": done_cnt,
            "steps_total": total_cnt,
            "pct": round((done_cnt / total_cnt) * 100.0, 1) if total_cnt else 0.0,
            "status": "terminee" if total_cnt and done_cnt == total_cnt else ("en_cours" if done_cnt > 0 else "a_faire"),
        })
    return tasks


def _parse_parties_and_fiches(lines: list[str], units_by_id: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    parties: list[dict[str, Any]] = []
    current_party: dict[str, Any] | None = None
    sec4_idx = len(lines)
    fiche_starts: list[tuple[int, str, str, dict[str, Any] | None]] = []

    for idx, line in enumerate(lines):
        if line.startswith("## 4. "):
            sec4_idx = idx
            break
        pm = PARTIE_HEADING_RE.match(line)
        if pm:
            current_party = {
                "part_roman": pm.group(1),
                "domain_id": pm.group(2),
                "title": strip_md_inline(pm.group(3)),
                "line_no": idx + 1,
                "chapter_ids": [],
            }
            parties.append(current_party)
            continue
        fm = FICHE_HEADING_RE.match(line)
        if fm:
            ch_id = fm.group(1)
            ch_title = strip_md_inline(fm.group(3))
            if current_party is not None:
                current_party["chapter_ids"].append(ch_id)
            fiche_starts.append((idx, ch_id, ch_title, current_party))

    for pos, (start_idx, ch_id, ch_title, party) in enumerate(fiche_starts):
        end_idx = fiche_starts[pos + 1][0] if pos + 1 < len(fiche_starts) else sec4_idx
        block = "\n".join(lines[start_idx:end_idx])
        unit = units_by_id.get(ch_id)
        if unit is None:
            continue
        unit["title"] = ch_title
        unit["plan_line"] = start_idx + 1
        if party is not None:
            unit["part_roman"] = party["part_roman"]
            unit["part_title"] = party["title"]
        unit["families"] = list(dict.fromkeys(FAM_ID_RE.findall(block)))
        unit["themes"] = list(dict.fromkeys(THM_ID_RE.findall(block)))
        unit["requirements"] = list(dict.fromkeys(EXIG_ID_RE.findall(block)))[:24]
        sub5_m = re.search(
            r"\*\*5\.\s+Livrables du chapitre[^\n]*\*\*\s*\n+([\s\S]*?)(?:\n---|\Z)",
            block,
        )
        if sub5_m:
            unit["deliverables_summary"] = strip_md_inline(" ".join(sub5_m.group(1).splitlines()))[:420]

    # Enrichir les titres des annexes depuis ## 4.
    for idx, line in enumerate(lines):
        am = ANNEXE_HEADING_RE.match(line)
        if am:
            letter = am.group(2)
            ann_unit = units_by_id.get(f"Annexe {letter}")
            if ann_unit is not None:
                ann_unit["title"] = strip_md_inline(am.group(3))
                ann_unit["plan_line"] = idx + 1
    if "00 - Liminaire" in units_by_id:
        units_by_id["00 - Liminaire"]["title"] = "Liminaire — Doctrine 80/20, concordance DIV-02/DISC-01..05 et Panorama SCH-00"
    return parties


def _load_schemas_catalogue(repo_root: Path, units: list[dict[str, Any]]) -> list[dict[str, Any]]:
    cat_path = repo_root / "Tomes" / "Cartographie" / "donnees" / "catalogue-schemas-prd.json"
    schemas: list[dict[str, Any]] = []
    if cat_path.is_file():
        cat = json.loads(cat_path.read_text(encoding="utf-8"))
        raw_list = list(cat.get("global_schemas") or []) + list(cat.get("chapter_schemas") or [])
        for sc in raw_list:
            ch_num = int(sc.get("chapter_number", 0))
            scope = "00 - Liminaire" if ch_num == 0 else f"CH-{ch_num:02d}"
            schemas.append({
                "schema_id": sc["schema_id"],
                "scope": scope,
                "chapter_number": ch_num,
                "domain_id": sc.get("domain_id", "GLOBAL" if ch_num == 0 else ""),
                "title": sc.get("title", sc["schema_id"]),
                "reuse_status": sc.get("reuse_status", "adaptation_vulgarisee"),
                "recommended_notation": sc.get("recommended_notation", "PlantUML"),
                "visual_archetype": sc.get("visual_archetype", ""),
                "insertion_point": sc.get("insertion_point", ""),
                "linked_figures_count": len(sc.get("linked_tome_figures") or []),
            })
        return schemas

    # Repli depuis la table des unités si le JSON de cartographie est absent
    for u in units:
        for sid in u["schema_ids"]:
            schemas.append({
                "schema_id": sid,
                "scope": u["unit_id"],
                "chapter_number": u["order"] if u["unit_type"] != "annexe" else 0,
                "domain_id": u["domain_id"],
                "title": f"Schéma {sid}",
                "reuse_status": "adaptation_vulgarisee",
                "recommended_notation": "PlantUML",
                "visual_archetype": "",
                "insertion_point": u["unit_id"],
                "linked_figures_count": 0,
            })
    return schemas


def _parse_waves(lines: list[str]) -> list[dict[str, Any]]:
    waves: list[dict[str, Any]] = []
    in_sec6 = False
    for line in lines:
        if line.startswith("## 6. "):
            in_sec6 = True
            continue
        if in_sec6 and line.startswith("### "):
            break
        if in_sec6:
            m = re.match(r"^\d+\.\s+\*\*(Vague\s+(\d+)\s+—\s+[^*]+)\*\*\s*:\s*(.+)$", line)
            if m:
                waves.append({
                    "wave_id": f"V{m.group(2)}",
                    "title": strip_md_inline(m.group(1)),
                    "description": strip_md_inline(m.group(3)),
                })
    return waves


def parse_plan_markdown(plan_path: Path, repo_root: Path | None = None) -> dict[str, Any]:
    """Parse intégralement ``Compendium/plan.md`` en dictionnaire structuré."""
    resolved_plan = plan_path.resolve()
    root = repo_root.resolve() if repo_root else resolved_plan.parents[1]
    raw_bytes = resolved_plan.read_bytes()
    text = raw_bytes.decode("utf-8")
    lines = text.splitlines()
    stat = resolved_plan.stat()

    meta = {
        "title": lines[0].lstrip("# ").strip() if lines else "Plan directeur du Compendium",
        "plan_path": str(resolved_plan),
        "version": _extract_meta_field(text[:2500], "Version", "1.0.0"),
        "freeze_date": _extract_meta_field(text[:2500], "Gel des faits", "2026-12-02"),
        "target_release": _extract_meta_field(text[:2500], "Parution cible", "janvier 2027"),
        "author": _extract_meta_field(text[:2500], "Auteur", "André-Guy Bruneau, M.Sc IT"),
        "status": _extract_meta_field(text[:2500], "Statut", "Plan d'ingénierie éditoriale (non-avis)"),
        "goal": _extract_blockquote_bullet(text[:3500], "Goal"),
        "architecture": _extract_blockquote_bullet(text[:3500], "Architecture"),
        "tech_stack": _extract_blockquote_bullet(text[:3500], "Tech Stack"),
        "line_count": len(lines),
        "word_count": len(text.split()),
        "byte_size": len(raw_bytes),
        "crlf_free": b"\r\n" not in raw_bytes,
        "mtime_iso": datetime.fromtimestamp(stat.st_mtime, tz=timezone.utc).isoformat(),
    }

    units = _parse_units_table(lines)
    units_by_id = {u["unit_id"]: u for u in units}
    tasks = _parse_tasks(lines)
    parties = _parse_parties_and_fiches(lines, units_by_id)
    schemas = _load_schemas_catalogue(root, units)

    ao_rows = _find_table_after(lines, "### 1.2", "Code")
    constraints_ao = [
        {
            "code": strip_md_inline(r.get("Code", "")),
            "title": strip_md_inline(r.get("Intitulé", "")),
            "rule": strip_md_inline(r.get("Règle exécutable et seuil bloquant", "")),
        }
        for r in ao_rows
    ]

    ca_rows = _find_table_after(lines, "## 5.", "Critère")
    criteria_ca = [
        {
            "id": strip_md_inline(r.get("Critère", "")),
            "description": strip_md_inline(r.get("Objet du contrôle et seuil bloquant", "")),
            "gates": [g.strip() for g in strip_md_inline(r.get("Barrière(s)", "")).split(",") if g.strip()],
            "verifier": strip_md_inline(r.get("Outil ou agent vérificateur", "")),
        }
        for r in ca_rows
    ]

    gate_rows = _find_table_after(lines, "## 5.", "Exécuteur étanche")
    gates = [
        {
            "gate_id": strip_md_inline(r.get("Barrière", "")),
            "executor": strip_md_inline(r.get("Exécuteur étanche (AO-07)", "")),
            "inputs": strip_md_inline(r.get("Entrées inspectées", "")),
            "exit_condition": strip_md_inline(r.get("Condition de sortie bloquante", "")),
        }
        for r in gate_rows
    ]

    risk_rows = _find_table_after(lines, "### Registre synthétique", "Risque identifié")
    risks = [
        {
            "risk": strip_md_inline(r.get("Risque identifié", "")),
            "impact": strip_md_inline(r.get("Impact potentiel", "")),
            "mitigation": strip_md_inline(r.get("Parade exécutable et porte de rattrapage", "")),
        }
        for r in risk_rows
    ]

    waves = _parse_waves(lines)

    return {
        "meta": meta,
        "tasks": tasks,
        "units": units,
        "parties": parties,
        "schemas": schemas,
        "constraints_ao": constraints_ao,
        "criteria_ca": criteria_ca,
        "gates": gates,
        "waves": waves,
        "risks": risks,
    }


def _find_unit_manuscript(manuscrit_dir: Path, unit: dict[str, Any]) -> Path | None:
    if not manuscrit_dir.is_dir():
        return None
    md_files = sorted(manuscrit_dir.rglob("*.md"))
    utype = unit["unit_type"]
    if utype == "liminaire":
        for p in md_files:
            low = p.name.lower()
            if "liminaire" in low or low.startswith("00"):
                return p
    elif utype == "chapitre":
        ch_num = unit["unit_id"].split("-")[1]
        pat = re.compile(rf"(?:^|[^0-9])(?:ch(?:apitre)?[\s_-]*){ch_num}(?:[^0-9]|$)", re.IGNORECASE)
        for p in md_files:
            if pat.search(p.stem):
                return p
    elif utype == "annexe":
        letter = unit["unit_id"].replace("Annexe", "").strip()
        pat = re.compile(rf"annexe[\s_-]+{re.escape(letter)}(?:[^a-z0-9]|$)", re.IGNORECASE)
        for p in md_files:
            if pat.search(p.stem):
                return p
    return None


def _parse_ancrage_verdicts(ancrage_path: Path) -> dict[str, int]:
    text = ancrage_path.read_text(encoding="utf-8", errors="replace").lower()
    non_sup = len(re.findall(r"\bnon[\s_-]+support[ée]", text))
    imprecis = len(re.findall(r"\bimpr[ée]cis\b", text))
    sup_total = len(re.findall(r"\bsupport[ée]", text))
    supported = max(0, sup_total - non_sup)
    return {
        "supported": supported,
        "imprecis": imprecis,
        "non_supported": non_sup,
    }


def _read_git_head(repo_root: Path) -> dict[str, str]:
    try:
        sha = subprocess.check_output(
            ["git", "-C", str(repo_root), "rev-parse", "--short", "HEAD"],
            text=True,
            stderr=subprocess.DEVNULL,
            timeout=3,
        ).strip()
        subject = subprocess.check_output(
            ["git", "-C", str(repo_root), "log", "-1", "--pretty=%s"],
            text=True,
            stderr=subprocess.DEVNULL,
            timeout=3,
        ).strip()
        branch = subprocess.check_output(
            ["git", "-C", str(repo_root), "rev-parse", "--abbrev-ref", "HEAD"],
            text=True,
            stderr=subprocess.DEVNULL,
            timeout=3,
        ).strip()
        return {"branch": branch, "commit": sha, "subject": subject}
    except Exception:
        return {"branch": "inconnu", "commit": "n/a", "subject": ""}


def _normalize_finding_severity(raw: Any) -> str:
    val = str(raw or "").strip().upper()
    if val in ("BLOQUANT", "CRITIQUE", "CRITICAL", "BLOCKER", "HIGH"):
        return "BLOQUANT"
    if val in ("MAJEUR", "MAJOR", "MEDIUM"):
        return "MAJEUR"
    return "MINEUR"


def _normalize_finding_status(raw: Any) -> str:
    val = str(raw or "").strip().lower()
    val = val.replace("é", "e").replace("è", "e").replace("ê", "e")
    if val in ("corrige", "fixed", "resolved", "resolu"):
        return "corrige"
    if val in ("verifie", "verified", "valide", "validee", "ferme", "closed"):
        return "verifie"
    return "ouvert"


def _normalize_finding(raw: dict[str, Any], fallback_id: str) -> dict[str, Any]:
    fid = str(raw.get("id") or fallback_id).strip()
    severity = _normalize_finding_severity(raw.get("severity") or raw.get("severite"))
    status = _normalize_finding_status(raw.get("status") or raw.get("statut"))
    axis = str(raw.get("axis") or raw.get("axe") or "couverture_prd").strip()
    unit = str(raw.get("unit") or raw.get("unite") or raw.get("target") or raw.get("cible") or "").strip()
    title = str(raw.get("title") or raw.get("titre") or raw.get("summary") or fid).strip()
    detail = str(raw.get("detail") or raw.get("description") or raw.get("evidence") or "").strip()
    return {
        **raw,
        "id": fid,
        "severity": severity,
        "status": status,
        "axis": axis,
        "unit": unit,
        "title": title,
        "detail": detail,
    }


def _probe_revision(ouvrage_dir: Path) -> dict[str, Any]:
    """Sonde ``Compendium/ouvrage/aq/suivi-revision-prd.json`` et les fichiers ``findings-*.json``."""
    aq_dir = ouvrage_dir / "aq"
    suivi_path = aq_dir / "suivi-revision-prd.json"

    reports: list[dict[str, Any]] = []
    seen_reports: set[str] = set()
    for fn, label in EXPECTED_REVISION_REPORTS:
        p = aq_dir / fn
        exists = p.is_file()
        reports.append({
            "filename": fn,
            "label": label,
            "path": f"Compendium/ouvrage/aq/{fn}",
            "exists": exists,
            "byte_size": p.stat().st_size if exists else 0,
            "mtime_iso": datetime.fromtimestamp(p.stat().st_mtime, tz=timezone.utc).isoformat() if exists else "",
        })
        seen_reports.add(fn)
    if aq_dir.is_dir():
        for extra in sorted(aq_dir.glob("audit-*.md")):
            if extra.name not in seen_reports:
                reports.append({
                    "filename": extra.name,
                    "label": f"Rapport complémentaire ({extra.stem})",
                    "path": f"Compendium/ouvrage/aq/{extra.name}",
                    "exists": True,
                    "byte_size": extra.stat().st_size,
                    "mtime_iso": datetime.fromtimestamp(extra.stat().st_mtime, tz=timezone.utc).isoformat(),
                })
                seen_reports.add(extra.name)

    reports_done = sum(1 for r in reports if r["exists"])
    default_summary = {
        "milestones_done": 0,
        "milestones_total": 0,
        "revision_pct": 0.0,
        "findings_total": 0,
        "open_count": 0,
        "by_severity": {"BLOQUANT": 0, "MAJEUR": 0, "MINEUR": 0},
        "by_status": {"ouvert": 0, "corrige": 0, "verifie": 0},
        "open_blocking": 0,
        "open_major": 0,
        "open_minor": 0,
        "reports_done": reports_done,
        "reports_total": len(reports),
    }

    if not suivi_path.is_file():
        return {
            "active": False,
            "campaign_id": "",
            "title": "",
            "updated_at": "",
            "milestones": [],
            "reference_metrics": {},
            "prd_coverage": {},
            "findings": [],
            "findings_files": [],
            "reports": reports,
            "summary": default_summary,
        }

    try:
        base_data = json.loads(suivi_path.read_text(encoding="utf-8"))
        if not isinstance(base_data, dict):
            base_data = {}
    except Exception:
        return {
            "active": False,
            "campaign_id": "",
            "title": "",
            "updated_at": "",
            "milestones": [],
            "reference_metrics": {},
            "prd_coverage": {},
            "findings": [],
            "findings_files": [],
            "reports": reports,
            "summary": default_summary,
        }

    milestones = [m for m in (base_data.get("milestones") or []) if isinstance(m, dict)]
    ref_metrics: dict[str, Any] = dict(base_data.get("reference_metrics") or {})
    prd_cov: dict[str, Any] = {
        "lots_completed": 0,
        "lots_total": 4,
        "units_audited": 0,
        "units_total": 42,
        **(base_data.get("prd_coverage") or {}),
    }

    findings_by_id: dict[str, dict[str, Any]] = {}
    findings_files: list[str] = []
    lots_done_ids: set[str] = set()
    units_audited_sum = 0
    units_audited_set: set[str] = set()

    if aq_dir.is_dir():
        for fpath in sorted(aq_dir.glob("findings-*.json")):
            try:
                raw_obj = json.loads(fpath.read_text(encoding="utf-8"))
            except Exception:
                continue
            findings_files.append(fpath.name)
            items: list[Any] = []
            if isinstance(raw_obj, list):
                items = raw_obj
            elif isinstance(raw_obj, dict):
                items = list(raw_obj.get("findings") or [])
                f_ref = raw_obj.get("reference_metrics")
                if isinstance(f_ref, dict):
                    for k, v in f_ref.items():
                        if v is None:
                            continue
                        if k == "audit_completed" and ref_metrics.get("audit_completed") is True and v is False:
                            continue
                        ref_metrics[k] = v
                ld = raw_obj.get("lot_done")
                if ld is True:
                    lots_done_ids.add(str(raw_obj.get("lot_id") or raw_obj.get("lot") or fpath.stem))
                elif isinstance(ld, (int, str)) and ld:
                    lots_done_ids.add(str(ld))
                elif isinstance(ld, dict):
                    lots_done_ids.add(str(ld.get("lot_id") or ld.get("id") or fpath.stem))
                    if isinstance(ld.get("units_audited"), int):
                        units_audited_sum += ld["units_audited"]
                    elif isinstance(ld.get("units_audited"), list):
                        units_audited_set.update(str(u) for u in ld["units_audited"])
                ua = raw_obj.get("units_audited")
                if isinstance(ua, int):
                    units_audited_sum += ua
                elif isinstance(ua, list):
                    units_audited_set.update(str(u) for u in ua)
                f_cov = raw_obj.get("prd_coverage")
                if isinstance(f_cov, dict):
                    if isinstance(f_cov.get("lots_completed"), int):
                        prd_cov["lots_completed"] = max(int(prd_cov.get("lots_completed") or 0), f_cov["lots_completed"])
                    if isinstance(f_cov.get("units_audited"), int):
                        prd_cov["units_audited"] = max(int(prd_cov.get("units_audited") or 0), f_cov["units_audited"])

            for idx, item in enumerate(items, start=1):
                if not isinstance(item, dict):
                    continue
                norm = _normalize_finding(item, f"{fpath.stem}-{idx}")
                fid = norm["id"]
                if fid in findings_by_id:
                    findings_by_id[fid] = {**findings_by_id[fid], **norm}
                else:
                    findings_by_id[fid] = norm

    # Les constats inscrits dans suivi-revision-prd.json ont préséance (consolidations / mises à jour de statut)
    for idx, item in enumerate(base_data.get("findings") or [], start=1):
        if not isinstance(item, dict):
            continue
        norm = _normalize_finding(item, f"suivi-{idx}")
        fid = norm["id"]
        if fid in findings_by_id:
            findings_by_id[fid] = {**findings_by_id[fid], **norm}
        else:
            findings_by_id[fid] = norm

    prd_cov["lots_completed"] = max(int(prd_cov.get("lots_completed") or 0), len(lots_done_ids))
    units_from_files = max(units_audited_sum, len(units_audited_set))
    prd_cov["units_audited"] = max(int(prd_cov.get("units_audited") or 0), units_from_files)

    findings = list(findings_by_id.values())

    milestones_total = len(milestones)
    milestones_done = sum(
        1
        for m in milestones
        if str(m.get("status") or "").strip().lower().replace("é", "e") in ("termine", "terminee", "valide", "validee", "done")
    )
    revision_pct = round((milestones_done / milestones_total) * 100.0, 1) if milestones_total else 0.0

    by_severity = {"BLOQUANT": 0, "MAJEUR": 0, "MINEUR": 0}
    by_status = {"ouvert": 0, "corrige": 0, "verifie": 0}
    open_blocking = 0
    open_major = 0
    open_minor = 0

    for f in findings:
        sev = f["severity"]
        st = f["status"]
        by_severity[sev] = by_severity.get(sev, 0) + 1
        by_status[st] = by_status.get(st, 0) + 1
        if st == "ouvert":
            if sev == "BLOQUANT":
                open_blocking += 1
            elif sev == "MAJEUR":
                open_major += 1
            else:
                open_minor += 1

    return {
        "active": True,
        "campaign_id": str(base_data.get("campaign_id") or ""),
        "title": str(base_data.get("title") or ""),
        "updated_at": str(base_data.get("updated_at") or ""),
        "milestones": milestones,
        "reference_metrics": ref_metrics,
        "prd_coverage": prd_cov,
        "findings": findings,
        "findings_files": findings_files,
        "reports": reports,
        "summary": {
            "milestones_done": milestones_done,
            "milestones_total": milestones_total,
            "revision_pct": revision_pct,
            "findings_total": len(findings),
            "open_count": by_status["ouvert"],
            "by_severity": by_severity,
            "by_status": by_status,
            "open_blocking": open_blocking,
            "open_major": open_major,
            "open_minor": open_minor,
            "reports_done": reports_done,
            "reports_total": len(reports),
        },
    }


def probe_ouvrage(repo_root: Path, parsed: dict[str, Any]) -> dict[str, Any]:
    """Sonde ``Compendium/ouvrage/`` et les fondations du dépôt pour calculer l'avancement réel."""
    root = repo_root.resolve()
    ouvrage_dir = root / "Compendium" / "ouvrage"
    ouvrage_exists = ouvrage_dir.is_dir()

    # 1. Sonde des 10 sous-dossiers de l'usine
    directories: list[dict[str, Any]] = []
    for sub_name, desc in OUVRAGE_SUBDIRS:
        sub_path = ouvrage_dir / sub_name
        exists = sub_path.is_dir()
        file_count = sum(1 for p in sub_path.rglob("*") if p.is_file()) if exists else 0
        directories.append({
            "name": sub_name,
            "path": f"Compendium/ouvrage/{sub_name}/",
            "description": desc,
            "exists": exists,
            "file_count": file_count,
        })

    # 2. Socle specs / outils / registres / recherche
    specs_ready = [
        (ouvrage_dir / "specs" / fn).is_file()
        for fn in ("manifest.json", "protocole-mlr-compendium.json")
    ]
    outils_ready = [(ouvrage_dir / "outils" / fn).is_file() for fn in EXPECTED_OUTILS]
    registres_ready = [(ouvrage_dir / "registre" / fn).is_file() for fn in EXPECTED_REGISTRES]
    corpus_lplus_dir = ouvrage_dir / "recherche" / "corpus_l_plus"
    corpus_lplus_count = sum(1 for p in corpus_lplus_dir.glob("*.txt")) if corpus_lplus_dir.is_dir() else 0
    manifeste_sha_ok = (ouvrage_dir / "recherche" / "manifeste-sources-sha256.json").is_file()
    statut_f_ok = (ouvrage_dir / "recherche" / "registre-statut-f.json").is_file()

    socle_items_done = sum(specs_ready) + sum(outils_ready) + sum(registres_ready) + int(manifeste_sha_ok) + int(statut_f_ok)
    socle_items_total = len(specs_ready) + len(outils_ready) + len(registres_ready) + 2

    # 3. Sonde des 115 schémas
    schemas_dir = ouvrage_dir / "schemas"
    rendus_dir = schemas_dir / "rendus"
    schemas_out: list[dict[str, Any]] = []
    schemas_by_unit: dict[str, list[dict[str, Any]]] = {}
    schemas_sources_done = 0
    schemas_rendered_done = 0

    for sc in parsed["schemas"]:
        sid = sc["schema_id"]
        src_found = ""
        for ext in (".puml", ".mmd", ".svg"):
            cand = schemas_dir / f"{sid}{ext}"
            if cand.is_file():
                src_found = f"Compendium/ouvrage/schemas/{cand.name}"
                break
        ren_found = ""
        for ext in (".svg", ".png"):
            cand = rendus_dir / f"{sid}{ext}"
            if cand.is_file():
                ren_found = f"Compendium/ouvrage/schemas/rendus/{cand.name}"
                break
        has_src = bool(src_found)
        has_ren = bool(ren_found)
        if has_src:
            schemas_sources_done += 1
        if has_ren:
            schemas_rendered_done += 1
        enriched = {
            **sc,
            "has_source": has_src,
            "has_rendered": has_ren,
            "source_file": src_found,
            "rendered_file": ren_found,
            "disk_status": "rendu" if has_ren else ("source" if has_src else "a_produire"),
        }
        schemas_out.append(enriched)
        schemas_by_unit.setdefault(sc["scope"], []).append(enriched)

    # 4. Sonde des 42 unités (manuscrit, sources, ancrage Wyvern G2)
    manuscrit_dir = ouvrage_dir / "manuscrit"
    sources_dir = ouvrage_dir / "sources"
    ancrage_dir = ouvrage_dir / "ancrage"

    units_out: list[dict[str, Any]] = []
    words_written_total = 0
    words_target_total = 0
    units_started = 0
    units_conforme = 0
    sources_done = 0
    ancrages_done = 0

    for u in parsed["units"]:
        words_target_total += u["target_words"]
        m_path = _find_unit_manuscript(manuscrit_dir, u)
        actual_words = count_prose_words(m_path.read_text(encoding="utf-8", errors="replace")) if m_path else 0
        words_written_total += actual_words

        if actual_words == 0:
            m_status = "non_demarre"
        elif actual_words < u["min_words"]:
            m_status = "sous_calibre"
            units_started += 1
        elif actual_words > u["max_words"]:
            m_status = "sur_calibre"
            units_started += 1
        else:
            m_status = "conforme"
            units_started += 1
            units_conforme += 1

        word_pct = round(min(200.0, (actual_words / u["target_words"]) * 100.0), 1) if u["target_words"] else 0.0

        is_narrative = u["unit_type"] in ("liminaire", "chapitre")
        has_sources: bool | None = None
        has_ancrage: bool | None = None
        ancrage_verdicts: dict[str, int] | None = None
        if is_narrative:
            ch_idx = 0 if u["unit_type"] == "liminaire" else int(u["unit_id"].split("-")[1])
            src_file = sources_dir / f"ch{ch_idx:02d}-sources.md"
            anc_file = ancrage_dir / f"ch{ch_idx:02d}-ancrage.md"
            has_sources = src_file.is_file()
            has_ancrage = anc_file.is_file()
            if has_sources:
                sources_done += 1
            if has_ancrage:
                ancrages_done += 1
                ancrage_verdicts = _parse_ancrage_verdicts(anc_file)

        u_schemas = schemas_by_unit.get(u["unit_id"], [])
        u_sch_rendered = sum(1 for sc in u_schemas if sc["has_rendered"])

        units_out.append({
            **u,
            "manuscript_file": str(m_path.relative_to(root)).replace("\\", "/") if m_path else "",
            "actual_words": actual_words,
            "word_pct": word_pct,
            "manuscript_status": m_status,
            "has_sources": has_sources,
            "has_ancrage": has_ancrage,
            "ancrage_verdicts": ancrage_verdicts,
            "schemas_rendered": u_sch_rendered,
            "schemas_total": len(u["schema_ids"]),
        })

    # 5. Barrières G0-G5 et livrables finaux
    aq_dir = ouvrage_dir / "aq"
    tome8_g0_path = root / "Tomes" / "Tome 8 - Ingénierie exécutable et homologation vérifiable" / "aq" / "rapports-g0.json"
    tome8_g0_summary: dict[str, Any] = {"available": tome8_g0_path.is_file(), "status": "absent"}
    if tome8_g0_path.is_file():
        try:
            g0_data = json.loads(tome8_g0_path.read_text(encoding="utf-8"))
            tome8_g0_summary = {
                "available": True,
                "status": g0_data.get("overall_status") or g0_data.get("status") or "PASS",
                "path": "Tomes/Tome 8 - Ingénierie exécutable et homologation vérifiable/aq/rapports-g0.json",
            }
        except Exception:
            tome8_g0_summary["status"] = "illisible"

    g0_comp_ok = (aq_dir / "rapports-g0.json").is_file()
    g1_ok = units_conforme == len(units_out) and len(units_out) > 0 and schemas_rendered_done == len(schemas_out)
    g2_ok = ancrages_done == 37
    g3_p1_ok = (aq_dir / "recollation-seed-20270901.md").is_file() or (aq_dir / "recollation-seed-20270901.json").is_file()
    g3_p2_ok = (aq_dir / "recollation-seed-20270902.md").is_file() or (aq_dir / "recollation-seed-20270902.json").is_file()
    g4_ok = (aq_dir / "gauntlet-log.md").is_file()
    g5_vis_ok = (aq_dir / "rapport-lissage-et-visuel.md").is_file()

    livrables_dir = ouvrage_dir / "livrables"
    deliverables_out: list[dict[str, Any]] = []
    deliverables_done = 0
    for fn, label in EXPECTED_DELIVERABLES:
        p = livrables_dir / fn
        exists = p.is_file()
        if exists:
            deliverables_done += 1
        deliverables_out.append({
            "filename": fn,
            "label": label,
            "path": f"Compendium/ouvrage/livrables/{fn}",
            "exists": exists,
            "byte_size": p.stat().st_size if exists else 0,
        })

    gate_states_map = {
        "G0": ("validee" if g0_comp_ok else ("en_cours" if tome8_g0_summary["available"] else "a_venir"),
               "rapports-g0.json Compendium présent" if g0_comp_ok else "Socle Tome 8 prêt ; sync Compendium en attente (Task 4)"),
        "G1": ("validee" if g1_ok else ("en_cours" if units_started > 0 else "a_venir"),
               f"{units_conforme}/42 unités conformes · {schemas_rendered_done}/115 schémas"),
        "G2": ("validee" if g2_ok else ("en_cours" if ancrages_done > 0 else "a_venir"),
               f"{ancrages_done}/37 journaux Wyvern présents"),
        "G3": ("validee" if (g3_p1_ok and g3_p2_ok) else ("en_cours" if g3_p1_ok else "a_venir"),
               "Passes 1 et 2 archivées" if (g3_p1_ok and g3_p2_ok) else ("Passe 1 archivée" if g3_p1_ok else "En attente (Tasks 7–8)")),
        "G4": ("validee" if g4_ok else "a_venir",
               "gauntlet-log.md archivé" if g4_ok else "En attente (Task 7)"),
        "G5": ("validee" if (g5_vis_ok and deliverables_done == 3) else ("en_cours" if (g5_vis_ok or deliverables_done > 0) else "a_venir"),
               f"{deliverables_done}/3 livrables · rapport visuel {'présent' if g5_vis_ok else 'absent'}"),
    }

    gates_out: list[dict[str, Any]] = []
    gates_validated = 0
    for g in parsed["gates"]:
        gid = g["gate_id"]
        st, detail = gate_states_map.get(gid, ("a_venir", ""))
        if st == "validee":
            gates_validated += 1
        gates_out.append({**g, "status": st, "detail": detail})

    # 6. Agrégation par domaine D01-D12
    domains_summary: list[dict[str, Any]] = []
    for p in parsed["parties"]:
        did = p["domain_id"]
        d_units = [u for u in units_out if u["domain_id"] == did]
        d_target = sum(u["target_words"] for u in d_units)
        d_actual = sum(u["actual_words"] for u in d_units)
        d_conforme = sum(1 for u in d_units if u["manuscript_status"] == "conforme")
        d_sources = sum(1 for u in d_units if u["has_sources"])
        d_ancrages = sum(1 for u in d_units if u["has_ancrage"])
        d_sch_total = sum(u["schemas_total"] for u in d_units)
        d_sch_done = sum(u["schemas_rendered"] for u in d_units)
        d_pct = round(
            (
                (d_sources / max(1, len(d_units))) * 20.0
                + (d_sch_done / max(1, d_sch_total)) * 20.0
                + (min(1.0, d_actual / max(1, d_target))) * 40.0
                + (d_ancrages / max(1, len(d_units))) * 20.0
            ),
            1,
        )
        domains_summary.append({
            "domain_id": did,
            "part_roman": p["part_roman"],
            "title": p["title"],
            "chapters_count": len(d_units),
            "themes_count": sum(u["themes_count"] for u in d_units),
            "target_words": d_target,
            "actual_words": d_actual,
            "units_conforme": d_conforme,
            "sources_done": d_sources,
            "ancrages_done": d_ancrages,
            "schemas_done": d_sch_done,
            "schemas_total": d_sch_total,
            "progress_pct": d_pct,
        })

    # 7. KPI globaux
    steps_done = sum(t["steps_done"] for t in parsed["tasks"])
    steps_total = sum(t["steps_total"] for t in parsed["tasks"])
    plan_steps_pct = round((steps_done / steps_total) * 100.0, 1) if steps_total else 0.0

    socle_ratio = socle_items_done / max(1, socle_items_total)
    sources_ratio = sources_done / 37.0
    schemas_ratio = schemas_rendered_done / max(1, len(schemas_out))
    words_ratio = min(1.0, words_written_total / max(1, words_target_total))
    ancrage_ratio = ancrages_done / 37.0
    gates_deliv_ratio = (gates_validated + deliverables_done) / 9.0
    ouvrage_pct = round(
        (socle_ratio * 10.0 + sources_ratio * 15.0 + schemas_ratio * 15.0 + words_ratio * 35.0 + ancrage_ratio * 15.0 + gates_deliv_ratio * 10.0),
        1,
    )

    foundations = [
        {"label": "PRD maître (Compendium/prd.md)", "ok": (root / "Compendium" / "prd.md").is_file()},
        {"label": "Plan directeur (Compendium/plan.md)", "ok": (root / "Compendium" / "plan.md").is_file()},
        {"label": "Cartographie & MindMap (Tomes/Cartographie/)", "ok": (root / "Tomes" / "Cartographie" / "donnees" / "corpus-mindmap-data.json").is_file()},
        {"label": "Trousse G0 de référence (Tome 8)", "ok": tome8_g0_summary["available"]},
        {"label": "Gabarit PDF Typst (gabarit-pdf/)", "ok": (root / "gabarit-pdf" / "gabarit-collection.typ").is_file()},
    ]

    revision = _probe_revision(ouvrage_dir)

    return {
        "ouvrage_exists": ouvrage_exists,
        "directories": directories,
        "socle": {
            "done": socle_items_done,
            "total": socle_items_total,
            "corpus_lplus_files": corpus_lplus_count,
            "manifeste_sha256": manifeste_sha_ok,
            "registre_statut_f": statut_f_ok,
        },
        "tome8_g0": tome8_g0_summary,
        "foundations": foundations,
        "units": units_out,
        "schemas": schemas_out,
        "gates": gates_out,
        "deliverables": deliverables_out,
        "domains": domains_summary,
        "revision": revision,
        "kpis": {
            "plan_steps_done": steps_done,
            "plan_steps_total": steps_total,
            "plan_steps_pct": plan_steps_pct,
            "tasks_done": sum(1 for t in parsed["tasks"] if t["status"] == "terminee"),
            "tasks_total": len(parsed["tasks"]),
            "ouvrage_pct": ouvrage_pct,
            "words_written": words_written_total,
            "words_target": words_target_total,
            "words_pct": round((words_written_total / max(1, words_target_total)) * 100.0, 1),
            "units_started": units_started,
            "units_conforme": units_conforme,
            "units_total": len(units_out),
            "sources_done": sources_done,
            "sources_total": 37,
            "ancrages_done": ancrages_done,
            "ancrages_total": 37,
            "schemas_sources_done": schemas_sources_done,
            "schemas_rendered_done": schemas_rendered_done,
            "schemas_total": len(schemas_out),
            "gates_validated": gates_validated,
            "gates_total": len(gates_out),
            "criteria_total": len(parsed["criteria_ca"]),
            "deliverables_done": deliverables_done,
            "deliverables_total": len(deliverables_out),
        },
    }


def build_dashboard_payload(repo_root: Path, plan_path: Path | None = None) -> dict[str, Any]:
    """Assemble la charge JSON complète du tableau de bord."""
    root = repo_root.resolve()
    target_plan = plan_path.resolve() if plan_path else (root / "Compendium" / "plan.md")
    parsed = parse_plan_markdown(target_plan, repo_root=root)
    probed = probe_ouvrage(root, parsed)
    return {
        "generated_at": datetime.now(tz=timezone.utc).isoformat(),
        "git": _read_git_head(root),
        "meta": parsed["meta"],
        "kpis": probed["kpis"],
        "foundations": probed["foundations"],
        "tome8_g0": probed["tome8_g0"],
        "ouvrage_exists": probed["ouvrage_exists"],
        "directories": probed["directories"],
        "socle": probed["socle"],
        "tasks": parsed["tasks"],
        "domains": probed["domains"],
        "units": probed["units"],
        "schemas": probed["schemas"],
        "constraints_ao": parsed["constraints_ao"],
        "criteria_ca": parsed["criteria_ca"],
        "gates": probed["gates"],
        "waves": parsed["waves"],
        "risks": parsed["risks"],
        "deliverables": probed["deliverables"],
        "revision": probed["revision"],
    }


def toggle_plan_step(plan_path: Path, line_no: int, checked: bool) -> dict[str, Any]:
    """Bascule de façon atomique et en LF strict une case ``- [ ]`` / ``- [x]`` de ``plan.md``."""
    resolved = plan_path.resolve()
    raw = resolved.read_bytes()
    text = raw.decode("utf-8")
    has_trailing_nl = text.endswith("\n")
    lines = text.splitlines()

    if not isinstance(line_no, int) or line_no < 1 or line_no > len(lines):
        raise ValueError(f"Numéro de ligne hors bornes : {line_no}")
    if not isinstance(checked, bool):
        raise ValueError("Le paramètre 'checked' doit être un booléen")

    target_line = lines[line_no - 1]
    m = STEP_LINE_RE.match(target_line)
    if not m:
        raise ValueError(f"La ligne {line_no} n'est pas une case à cocher d'étape valide")

    mark = "x" if checked else " "
    new_line = f"{m.group(1)}{mark}{m.group(3)}{m.group(4)}"
    lines[line_no - 1] = new_line

    output = "\n".join(lines) + ("\n" if has_trailing_nl else "")
    tmp_path = resolved.with_suffix(".md.tmp")
    tmp_path.write_bytes(output.encode("utf-8"))
    tmp_path.replace(resolved)

    return {
        "line_no": line_no,
        "checked": checked,
        "label": strip_md_inline(m.group(4)),
    }


def export_units_csv(payload: dict[str, Any]) -> str:
    """Génère un export CSV UTF-8 (séparateur ';') des 42 unités du Compendium."""
    buf = io.StringIO()
    writer = csv.writer(buf, delimiter=";", lineterminator="\n")
    writer.writerow([
        "Unité",
        "Type",
        "Domaine",
        "Sous-domaine",
        "Familles",
        "Thèmes",
        "Cible (mots)",
        "Min",
        "Max",
        "Mots réels",
        "Progression (%)",
        "Statut manuscrit",
        "Sources L+",
        "Schémas rendus",
        "Schémas totaux",
        "Wyvern G2",
    ])
    for u in payload["units"]:
        writer.writerow([
            u["unit_id"],
            u["unit_type"],
            u["domain_id"],
            u["subdomain_id"],
            u["families_count"],
            u["themes_count"],
            u["target_words"],
            u["min_words"],
            u["max_words"],
            u["actual_words"],
            str(u["word_pct"]).replace(".", ","),
            u["manuscript_status"],
            "n/a" if u["has_sources"] is None else ("Oui" if u["has_sources"] else "Non"),
            u["schemas_rendered"],
            u["schemas_total"],
            "n/a" if u["has_ancrage"] is None else ("Oui" if u["has_ancrage"] else "Non"),
        ])
    return "\ufeff" + buf.getvalue()
