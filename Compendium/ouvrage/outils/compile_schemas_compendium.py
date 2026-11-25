#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Validation et compilation stricte des 115 schémas du Compendium (CA-08 / CA-22)."""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import struct
import subprocess
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

EXPECTED_TOTAL_SCHEMAS = 115
EXPECTED_PUML_COUNT = 52
EXPECTED_MMD_COUNT = 23
EXPECTED_SVG_COUNT = 40
EXPECTED_FAMILIES_COUNT = 71

MIN_NODES_PER_SCHEMA = 4
MAX_NODES_PER_SCHEMA = 14

NOTATION_PUML = "PlantUML"
NOTATION_MMD = "Mermaid"
NOTATION_SVG = "Infographie SVG bilingue métier-tech"

_PUML_CONTAINERS = {"package", "frame", "namespace", "box", "together"}
_PUML_IGNORE_PREFIXES = (
    "@start",
    "@end",
    "!",
    "skinparam",
    "title",
    "caption",
    "header",
    "footer",
    "hide",
    "show",
    "autonumber",
    "top to bottom",
    "left to right",
    "scale",
    "==",
    "...",
    "|||",
    "}",
    "else",
    "end ",
    "activate",
    "deactivate",
    "destroy",
    "return",
    "newpage",
    "allowmixing",
    "allow_mixing",
    "note ",
    "hnote ",
    "rnote ",
    "ref ",
    "alt ",
    "opt ",
    "loop ",
    "par ",
    "break ",
    "critical ",
    "group ",
)
_PUML_DECL_KEYWORDS = (
    "actor",
    "participant",
    "boundary",
    "control",
    "entity",
    "database",
    "collections",
    "queue",
    "component",
    "rectangle",
    "node",
    "agent",
    "artifact",
    "card",
    "cloud",
    "file",
    "folder",
    "hexagon",
    "interface",
    "label",
    "person",
    "stack",
    "storage",
    "usecase",
    "circle",
    "diamond",
    "class",
    "enum",
    "object",
    "struct",
    "state",
)
_PUML_DECL_RE = re.compile(
    r"^(" + "|".join(_PUML_DECL_KEYWORDS) + r")\b(.*)$",
    re.IGNORECASE,
)
_PUML_BRACKET_ONLY_RE = re.compile(
    r"^\[([^\]]+)\](?:\s+as\s+([A-Za-z0-9_.-]+))?(?:\s*<<[^>]+>>)*(?:\s*#[A-Za-z0-9_]+)?\s*$"
)
_PUML_ARROW_RE = re.compile(
    r"(?:<\|?|\*|o|\+)?"
    r"(?:"
    r"(?:-+(?:\[[^\]]*\])?(?:left|right|up|down|l|r|u|d)?-+)|"
    r"(?:\.+(?:\[[^\]]*\])?(?:left|right|up|down|l|r|u|d)?\.+)|"
    r"(?:=+(?:\[[^\]]*\])?(?:left|right|up|down|l|r|u|d)?=+)|"
    r"(?:->|<-|\.\.|--)"
    r")"
    r"(?:\|?>|\*|o|\+)?"
)

_MMD_SKIP_PREFIXES = (
    "flowchart",
    "graph",
    "direction",
    "subgraph",
    "end",
    "classdef",
    "class ",
    "style ",
    "linkstyle",
    "click ",
    "acctitle",
    "accdescr",
    "title ",
)
_MMD_ARROW_RE = re.compile(
    r"(?:"
    r"--[^-\n>]*-->|"
    r"-\.[^.\n>]*\.->|"
    r"==[^=\n>]*==>|"
    r"<-->|o--o|x--x|"
    r"-->|---|-\.->|-\.-|==>|===|~~~"
    r")(?:\s*\|[^|]*\|)?"
)

_SVG_ERROR_MARKERS = (
    "Syntax Error",
    "Some diagram description contains errors",
    "No diagram found",
    "Dot executable",
    "Cannot find Graphviz",
)

_SVG_SHAPE_TAGS = {"rect", "circle", "ellipse", "polygon"}
_SVG_NON_NODE_PREFIXES = (
    "zone",
    "legend",
    "leg",
    "bg",
    "background",
    "header",
    "footer",
    "takeaway",
    "key-takeaway",
    "arrow",
    "flow",
    "title",
    "canvas",
)

FORBIDDEN_PROSE_REGEXES: tuple[str, ...] = (
    r"\bSystems? of Agency\b",
    r"\bTODO\b",
    r"\bTBD\b",
    r"\blorem ipsum\b",
    r"\bplaceholder\b",
    r"\bà compléter\b",
    r"Dans un monde en constante évolution",
    r"À l'ère du numérique",
    r"Il convient de souligner que",
    r"Force est de constater que",
    r"changement de paradigme révolutionnaire",
    r"synergie holistique",
    r"En conclusion, nous avons vu que",
)

FORBIDDEN_RAW_MARKERS_REGEXES: tuple[str, ...] = (
    r"\[S\]",
    r"\[D\]",
    r"\[A\]",
    r"\[M\]",
    r"\[N\]",
    r"\[L\+\]",
)

FORBIDDEN_ORIGINAL_VENDOR_REGEXES: tuple[str, ...] = (
    r"\bOpenAI\b",
    r"\bChatGPT\b",
    r"\bAnthropic\b",
    r"\bClaude\b",
    r"\bGemini\b",
    r"\bCopilot\b",
    r"\bSalesforce\b",
    r"\bServiceNow\b",
    r"\bWorkday\b",
    r"\bDatabricks\b",
    r"\bSnowflake\b",
    r"\bBedrock\b",
    r"\bEntra\b",
    r"\bAzure\b",
    r"\bAWS\b",
    r"\bGCP\b",
    r"\bVertex\s+AI\b",
    r"\bLangChain\b",
    r"\bLangGraph\b",
    r"\bCrewAI\b",
    r"\bAutoGen\b",
    r"\bAutoGPT\b",
)


def _default_book_dir() -> Path:
    return Path(__file__).resolve().parent.parent


def _default_catalog_path() -> Path:
    repo_root = Path(__file__).resolve().parents[3]
    return repo_root / "Tomes" / "Cartographie" / "donnees" / "catalogue-schemas-prd.json"


def _normalize_quotes_spaces(text: str) -> str:
    return (
        text.replace("’", "'")
        .replace("‘", "'")
        .replace("\u00a0", " ")
        .replace("\u202f", " ")
    )


def _strip_backticks(text: str) -> str:
    return re.sub(r"`[^`]*`", "", text)


def _local_tag(tag: str) -> str:
    return tag.rsplit("}", 1)[-1] if "}" in tag else tag


def _replace_quoted_strings(text: str) -> tuple[str, dict[str, str]]:
    mapping: dict[str, str] = {}

    def _repl(match: re.Match[str]) -> str:
        key = f"__Q{len(mapping)}__"
        mapping[key] = match.group(1)
        return key

    cleaned = re.sub(r'"((?:[^"\\]|\\.)*)"', _repl, text)
    return cleaned, mapping


def _resolve_token(token: str, quoted: dict[str, str], display_to_id: dict[str, str]) -> str | None:
    tok = token.strip()
    if not tok or tok == "[*]":
        return None
    if tok.startswith("[") and tok.endswith("]"):
        tok = tok[1:-1].strip()
    if tok in quoted:
        tok = quoted[tok]
    tok = re.sub(r"<<[^>]+>>", "", tok).strip()
    tok = re.sub(r"#[A-Za-z0-9_]+$", "", tok).strip()
    if not tok or tok == "[*]":
        return None
    if tok in display_to_id:
        return display_to_id[tok]
    base = tok.split(".", 1)[0]
    if base in display_to_id:
        return display_to_id[base]
    return tok


def extract_puml_elements(text: str) -> list[str]:
    """Extrait les identifiants uniques de nœuds, participants et états PlantUML."""
    cleaned = re.sub(r"/'[\s\S]*?'/", "", text)
    cleaned = re.sub(r"<style\b[^>]*>[\s\S]*?</style>", "", cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(
        r"^\s*legend\b[\s\S]*?^\s*end\s+legend\b",
        "",
        cleaned,
        flags=re.IGNORECASE | re.MULTILINE,
    )
    cleaned = re.sub(
        r"^\s*(?:[hr]?note)\b(?![^\n]*:)[\s\S]*?^\s*end\s+[hr]?note\b",
        "",
        cleaned,
        flags=re.IGNORECASE | re.MULTILINE,
    )
    cleaned = re.sub(
        r"^\s*skinparam\b[^{}\n]*\{[^}]*\}",
        "",
        cleaned,
        flags=re.IGNORECASE | re.MULTILINE,
    )

    elements: list[str] = []
    seen: set[str] = set()
    display_to_id: dict[str, str] = {}
    containers: set[str] = set()

    def _add(elem_id: str | None) -> None:
        if elem_id and elem_id not in containers and elem_id not in seen:
            seen.add(elem_id)
            elements.append(elem_id)

    for raw_line in cleaned.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("'"):
            continue
        lower = line.lower()
        if lower == "end" or any(lower.startswith(pref) for pref in _PUML_IGNORE_PREFIXES):
            continue

        line_q, quoted = _replace_quoted_strings(line)
        first_word = lower.split(None, 1)[0].rstrip("{")
        if first_word in _PUML_CONTAINERS:
            m_cont = re.search(r"\bas\s+([A-Za-z0-9_.-]+)", line_q)
            if m_cont:
                containers.add(m_cont.group(1))
            continue

        m_decl = _PUML_DECL_RE.match(line_q)
        if m_decl and not _PUML_ARROW_RE.search(line_q.split(":", 1)[0]):
            rest = m_decl.group(2).strip().rstrip("{").strip()
            rest = re.sub(r"<<[^>]+>>", "", rest).strip()
            rest = re.sub(r"\s+#[A-Za-z0-9_]+(?:\s*;[^\s]+)*$", "", rest).strip()

            m_as = re.search(r"^(.*?)\s+as\s+([^\s]+)\s*$", rest)
            if m_as:
                left = m_as.group(1).strip()
                right = m_as.group(2).strip()
                if right in quoted and left not in quoted and re.fullmatch(r"[A-Za-z0-9_.-]+", left):
                    alias = left
                    disp = _resolve_token(right, quoted, {})
                else:
                    alias = right
                    disp = _resolve_token(left, quoted, {})
                if disp:
                    display_to_id[disp] = alias
                display_to_id[alias] = alias
                _add(alias)
            else:
                head = rest.split(":", 1)[0].strip()
                if head.startswith("[") and head.endswith("]"):
                    head = head[1:-1].strip()
                elem_id = _resolve_token(head, quoted, {})
                if elem_id:
                    display_to_id[elem_id] = elem_id
                    _add(elem_id)
            continue

        m_br = _PUML_BRACKET_ONLY_RE.match(line_q)
        if m_br:
            disp = m_br.group(1).strip()
            alias = (m_br.group(2) or disp).strip()
            display_to_id[disp] = alias
            display_to_id[alias] = alias
            _add(alias)
            continue

        head_no_label = line_q.split(":", 1)[0]
        m_arr = _PUML_ARROW_RE.search(head_no_label)
        if m_arr:
            lhs = head_no_label[: m_arr.start()].strip()
            rhs = head_no_label[m_arr.end() :].strip()
            if lhs and rhs:
                _add(_resolve_token(lhs, quoted, display_to_id))
                _add(_resolve_token(rhs, quoted, display_to_id))

    return elements


def extract_mmd_elements(text: str) -> list[str]:
    """Extrait les identifiants uniques de nœuds dans un diagramme Mermaid."""
    cleaned = re.sub(r"%%\{[\s\S]*?\}%%", "", text)
    cleaned = re.sub(r"%%[^\n]*", "", cleaned)

    elements: list[str] = []
    seen: set[str] = set()
    skip_words = {"end", "subgraph", "direction", "flowchart", "graph", "class", "style", "click"}

    def _add_node_expr(expr: str) -> None:
        chunk = expr.strip()
        if not chunk:
            return
        chunk = re.sub(r":::[A-Za-z0-9_-]+", "", chunk).strip()
        m_id = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*)", chunk)
        if not m_id:
            return
        node_id = m_id.group(1)
        if node_id.lower() in skip_words:
            return
        if node_id not in seen:
            seen.add(node_id)
            elements.append(node_id)

    for raw_line in cleaned.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        line_q, _ = _replace_quoted_strings(line)
        for stmt in line_q.split(";"):
            stmt = stmt.strip()
            if not stmt:
                continue
            lower = stmt.lower()
            if lower == "end" or any(lower.startswith(pref) for pref in _MMD_SKIP_PREFIXES):
                continue

            parts = _MMD_ARROW_RE.split(stmt)
            for part in parts:
                for sub in part.split("&"):
                    _add_node_expr(sub)

    return elements


def extract_svg_elements(text: str) -> list[str]:
    """Extrait les identifiants de nœuds d'une infographie SVG bilingue métier-tech."""
    try:
        root = ET.fromstring(text)
    except ET.ParseError:
        return []

    # 1. Marquage explicite data-node="true" (prioritaire)
    explicit_data_nodes: list[str] = []
    for idx, elem in enumerate(root.iter(), 1):
        dn = elem.attrib.get("data-node")
        if dn is not None and dn.strip().lower() not in {"false", "0", "no"}:
            explicit_data_nodes.append(elem.attrib.get("id") or f"data-node-{idx}")
    if explicit_data_nodes:
        return explicit_data_nodes

    # 2. Marquage par classe `node` / `schema-node` ou id `node-*`
    class_or_id_nodes: list[str] = []
    for idx, elem in enumerate(root.iter(), 1):
        classes = set(elem.attrib.get("class", "").split())
        eid = elem.attrib.get("id", "")
        if "node" in classes or "schema-node" in classes or eid.startswith(("node-", "node_")):
            class_or_id_nodes.append(eid or f"svg-node-{idx}")
    if class_or_id_nodes:
        return class_or_id_nodes

    # 3. Repli structurel : groupes <g> feuilles contenant une forme et un texte
    def _is_non_node_container(elem: ET.Element) -> bool:
        eid = elem.attrib.get("id", "").lower()
        classes = elem.attrib.get("class", "").lower()
        return any(eid.startswith(p) or p in classes for p in _SVG_NON_NODE_PREFIXES)

    fallback_nodes: list[str] = []
    for idx, elem in enumerate(root.iter(), 1):
        if _local_tag(elem.tag) != "g" or _is_non_node_container(elem):
            continue
        has_shape = any(_local_tag(c.tag) in _SVG_SHAPE_TAGS for c in elem)
        has_text = any(_local_tag(c.tag) == "text" for c in elem.iter())
        has_child_group = any(_local_tag(c.tag) == "g" for c in elem)
        if has_shape and has_text and not has_child_group:
            fallback_nodes.append(elem.attrib.get("id") or f"group-node-{idx}")
    return fallback_nodes


def count_schema_elements(source_path: Path, notation: str) -> int:
    """Compte les nœuds, participants ou états d'un schéma source selon sa notation."""
    text = source_path.read_text(encoding="utf-8")
    if notation == NOTATION_PUML:
        return len(extract_puml_elements(text))
    if notation == NOTATION_MMD:
        return len(extract_mmd_elements(text))
    if notation == NOTATION_SVG:
        return len(extract_svg_elements(text))
    raise ValueError(f"Notation de schéma inconnue : {notation}")


def load_catalog(catalog_path: Path | None = None) -> list[dict]:
    """Charge la liste ordonnée des 115 schémas depuis `catalogue-schemas-prd.json`."""
    path = catalog_path or _default_catalog_path()
    data = json.loads(path.read_text(encoding="utf-8"))
    return list(data.get("global_schemas", [])) + list(data.get("chapter_schemas", []))


def _notation_source_ext(notation: str) -> str:
    if notation == NOTATION_PUML:
        return "puml"
    if notation == NOTATION_MMD:
        return "mmd"
    if notation == NOTATION_SVG:
        return "svg"
    raise ValueError(f"Notation non supportée : {notation}")


def _notation_render_ext(notation: str) -> str:
    if notation == NOTATION_MMD:
        return "png"
    if notation in (NOTATION_PUML, NOTATION_SVG):
        return "svg"
    raise ValueError(f"Notation non supportée : {notation}")


def _find_plantuml_cmd() -> list[str] | None:
    for candidate in ("plantuml", "plantuml.cmd", "plantuml.bat"):
        found = shutil.which(candidate)
        if found:
            return [found]
    local_app = os.environ.get("LOCALAPPDATA")
    if local_app:
        fallback = Path(local_app) / "Programs" / "PlantUML" / "plantuml.cmd"
        if fallback.is_file():
            return [str(fallback)]
    return None


def _find_mmdc_cmd() -> list[str] | None:
    for candidate in ("mmdc", "mmdc.cmd"):
        found = shutil.which(candidate)
        if found:
            return [found]
    app_data = os.environ.get("APPDATA")
    if app_data:
        fallback = Path(app_data) / "npm" / "mmdc.cmd"
        if fallback.is_file():
            return [str(fallback)]
    return None


def _find_puppeteer_executable() -> str | None:
    env_exe = os.environ.get("PUPPETEER_EXECUTABLE_PATH")
    if env_exe and Path(env_exe).is_file():
        return env_exe

    home = Path.home()
    cache_roots = [
        home / ".cache" / "puppeteer" / "chrome-headless-shell",
        home / ".cache" / "puppeteer" / "chrome",
    ]
    for root in cache_roots:
        if root.is_dir():
            for sub in sorted(root.iterdir(), reverse=True):
                if not sub.is_dir():
                    continue
                for exe_name in ("chrome-headless-shell.exe", "chrome-headless-shell", "chrome.exe", "chrome"):
                    matches = list(sub.rglob(exe_name))
                    if matches and matches[0].is_file():
                        return str(matches[0])

    system_candidates = [
        Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe"),
        Path(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"),
        Path(r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"),
    ]
    for cand in system_candidates:
        if cand.is_file():
            return str(cand)
    return None


def _parse_svg_dimensions(root: ET.Element) -> tuple[float | None, float | None]:
    def _num(val: str | None) -> float | None:
        if not val:
            return None
        m = re.match(r"^\s*([0-9]+(?:\.[0-9]+)?)", val)
        return float(m.group(1)) if m else None

    w = _num(root.attrib.get("width"))
    h = _num(root.attrib.get("height"))
    if w is not None and h is not None:
        return w, h
    vb = root.attrib.get("viewBox", "")
    parts = re.split(r"[\s,]+", vb.strip())
    if len(parts) == 4:
        try:
            return float(parts[2]), float(parts[3])
        except ValueError:
            return None, None
    return None, None


def validate_svg_content(content: str, label: Path, check_dimensions: bool = False) -> list[str]:
    """Vérifie qu'un SVG est bien formé XML, sans marqueur d'erreur et aux dimensions valides."""
    errors: list[str] = []
    if "<svg" not in content or "</svg>" not in content:
        return [f"SVG invalide (balise <svg> manquante) : {label}"]
    for marker in _SVG_ERROR_MARKERS:
        if marker in content:
            errors.append(f"Erreur de rendu SVG ({marker}) dans {label}")
    try:
        root = ET.fromstring(content)
        if _local_tag(root.tag) != "svg":
            errors.append(f"Racine XML inattendue dans {label} : {root.tag}")
        elif check_dimensions:
            w, h = _parse_svg_dimensions(root)
            if w is None or h is None or w < 200 or h < 150:
                errors.append(f"Dimensions SVG insuffisantes ou absentes ({w}x{h}) dans {label}")
    except ET.ParseError as exc:
        errors.append(f"SVG XML mal formé dans {label} : {exc}")
    return errors


def validate_render(
    render_path: Path,
    notation: str,
    source_path: Path | None = None,
) -> list[str]:
    """Vérifie qu'un rendu SVG ou PNG existe, est à jour, bien formé et sans erreur."""
    errors: list[str] = []
    if not render_path.is_file():
        return [f"Rendu manquant : {render_path}"]
    if render_path.stat().st_size == 0:
        return [f"Rendu vide (0 octet) : {render_path}"]
    if source_path is not None and source_path.is_file():
        if source_path.stat().st_mtime > render_path.stat().st_mtime:
            errors.append(
                f"Rendu obsolète ({source_path.name} modifié après {render_path.name}) : {render_path}"
            )

    if notation in (NOTATION_PUML, NOTATION_SVG):
        content = render_path.read_text(encoding="utf-8", errors="replace")
        errors.extend(validate_svg_content(content, render_path, check_dimensions=(notation == NOTATION_SVG)))
        if notation == NOTATION_SVG and source_path is not None and source_path.is_file():
            if render_path.read_bytes() != source_path.read_bytes():
                errors.append(f"Copie non déterministe (octets divergents) : {render_path}")
    elif notation == NOTATION_MMD:
        data = render_path.read_bytes()
        if len(data) < 24 or data[:8] != b"\x89PNG\r\n\x1a\n":
            errors.append(f"Signature PNG invalide : {render_path}")
            return errors
        width, height = struct.unpack(">II", data[16:24])
        if width < 200 or height < 150:
            errors.append(f"Résolution PNG insuffisante ({width}x{height}) : {render_path}")
    else:
        errors.append(f"Notation inconnue pour validation de rendu : {notation}")
    return errors


def _validate_catalog_quotas(all_schemas: list[dict]) -> list[str]:
    errors: list[str] = []
    if len(all_schemas) != EXPECTED_TOTAL_SCHEMAS:
        errors.append(f"Quota catalogue attendu = {EXPECTED_TOTAL_SCHEMAS} schémas, trouvé {len(all_schemas)}")
    n_puml = sum(1 for s in all_schemas if s.get("recommended_notation") == NOTATION_PUML)
    n_mmd = sum(1 for s in all_schemas if s.get("recommended_notation") == NOTATION_MMD)
    n_svg = sum(1 for s in all_schemas if s.get("recommended_notation") == NOTATION_SVG)
    if n_puml != EXPECTED_PUML_COUNT:
        errors.append(f"Quota PlantUML attendu = {EXPECTED_PUML_COUNT}, trouvé {n_puml}")
    if n_mmd != EXPECTED_MMD_COUNT:
        errors.append(f"Quota Mermaid attendu = {EXPECTED_MMD_COUNT}, trouvé {n_mmd}")
    if n_svg != EXPECTED_SVG_COUNT:
        errors.append(f"Quota Infographies SVG attendu = {EXPECTED_SVG_COUNT}, trouvé {n_svg}")
    fams = {fid for s in all_schemas for fid in s.get("families_covered", [])}
    if len(fams) != EXPECTED_FAMILIES_COUNT:
        errors.append(f"Couverture familles FAM_* attendue = {EXPECTED_FAMILIES_COUNT}, trouvée {len(fams)}")
    return errors


def validate_sources(
    book_dir: Path,
    catalog_path: Path | None = None,
    strict: bool = True,
    schema_ids: list[str] | None = None,
) -> tuple[list[dict], list[str]]:
    """Valide les sources de schémas selon le catalogue PRD et la charte fr-CA."""
    cat_path = catalog_path or _default_catalog_path()
    if not cat_path.is_file():
        return [], [f"Catalogue introuvable : {cat_path}"]

    all_schemas = load_catalog(cat_path)
    errors: list[str] = _validate_catalog_quotas(all_schemas)

    if schema_ids is not None:
        wanted = set(schema_ids)
        selected = [s for s in all_schemas if s["schema_id"] in wanted]
        missing_ids = sorted(wanted - {s["schema_id"] for s in selected})
        if missing_ids:
            errors.append(f"Identifiants de schémas inconnus dans le catalogue : {missing_ids}")
    elif not strict:
        schemas_dir = book_dir / "schemas"
        selected = [
            s
            for s in all_schemas
            if (schemas_dir / f"{s['schema_id']}.{_notation_source_ext(s['recommended_notation'])}").is_file()
        ]
        if not selected:
            errors.append(f"Aucune source de schéma trouvée dans {schemas_dir}")
    else:
        selected = all_schemas

    prose_pats = [(p, re.compile(_normalize_quotes_spaces(p), re.IGNORECASE)) for p in FORBIDDEN_PROSE_REGEXES]
    marker_pats = [(p, re.compile(p)) for p in FORBIDDEN_RAW_MARKERS_REGEXES]
    vendor_pats = [(p, re.compile(p, re.IGNORECASE)) for p in FORBIDDEN_ORIGINAL_VENDOR_REGEXES]

    schemas_dir = book_dir / "schemas"
    for sc in selected:
        sid = sc["schema_id"]
        notation = sc["recommended_notation"]
        ext = _notation_source_ext(notation)
        src = schemas_dir / f"{sid}.{ext}"
        if not src.is_file():
            errors.append(f"Source de schéma manquante : {src}")
            continue

        raw_bytes = src.read_bytes()
        if raw_bytes.startswith(b"\xef\xbb\xbf"):
            errors.append(f"BOM UTF-8 interdit dans {src}")
        if b"\r\n" in raw_bytes:
            errors.append(f"Fins de ligne CRLF interdites dans {src}")
        try:
            text = raw_bytes.decode("utf-8")
        except UnicodeDecodeError as exc:
            errors.append(f"Encodage UTF-8 invalide dans {src} : {exc}")
            continue
        if "\ufffd" in text:
            errors.append(f"Caractère de remplacement U+FFFD détecté dans {src}")

        norm_text = _normalize_quotes_spaces(_strip_backticks(text))
        for pat_str, pat_re in prose_pats:
            m = pat_re.search(norm_text)
            if m:
                errors.append(f"Formule ou terme interdit ({pat_str} -> '{m.group(0)}') dans {src}")

        if int(sc.get("chapter_number", -1)) != 36:
            for pat_str, pat_re in marker_pats:
                m = pat_re.search(text)
                if m:
                    errors.append(f"Marqueur épistémique brut interdit hors CH-36 ({m.group(0)}) dans {src}")

        if sc.get("reuse_status") == "creation_originale":
            for pat_str, pat_re in vendor_pats:
                m = pat_re.search(text)
                if m:
                    errors.append(
                        f"Nom de produit ou fournisseur interdit dans la création originale {src} : '{m.group(0)}'"
                    )

        if notation == NOTATION_SVG:
            errors.extend(validate_svg_content(text, src, check_dimensions=True))

        elem_count = count_schema_elements(src, notation)
        if elem_count == 0:
            errors.append(f"Aucun nœud détecté dans {src}")
        elif elem_count < MIN_NODES_PER_SCHEMA:
            errors.append(
                f"Densité insuffisante dans {src} : {elem_count} nœuds (min {MIN_NODES_PER_SCHEMA}, max {MAX_NODES_PER_SCHEMA})"
            )
        elif elem_count > MAX_NODES_PER_SCHEMA:
            errors.append(
                f"Dépassement de densité dans {src} : {elem_count} nœuds (max {MAX_NODES_PER_SCHEMA})"
            )

    return selected, errors


def compile_schemas(
    book_dir: Path,
    catalog_path: Path | None = None,
    strict: bool = True,
    check_only: bool = False,
    schema_ids: list[str] | None = None,
    incremental: bool = False,
) -> list[str]:
    """Valide les sources, compile les schémas et contrôle chaque rendu."""
    selected, errors = validate_sources(
        book_dir,
        catalog_path=catalog_path,
        strict=strict,
        schema_ids=schema_ids,
    )
    if errors and strict and not check_only:
        return errors

    schemas_dir = book_dir / "schemas"
    rendus_dir = schemas_dir / "rendus"
    rendus_dir.mkdir(parents=True, exist_ok=True)

    puml_items: list[tuple[dict, Path, Path]] = []
    mmd_items: list[tuple[dict, Path, Path]] = []
    svg_items: list[tuple[dict, Path, Path]] = []

    for sc in selected:
        sid = sc["schema_id"]
        notation = sc["recommended_notation"]
        if notation == NOTATION_PUML:
            puml_items.append((sc, schemas_dir / f"{sid}.puml", rendus_dir / f"{sid}.svg"))
        elif notation == NOTATION_MMD:
            mmd_items.append((sc, schemas_dir / f"{sid}.mmd", rendus_dir / f"{sid}.png"))
        elif notation == NOTATION_SVG:
            svg_items.append((sc, schemas_dir / f"{sid}.svg", rendus_dir / f"{sid}.svg"))

    if not check_only:
        to_compile_puml = [
            src
            for _, src, dst in puml_items
            if src.is_file()
            and not (incremental and dst.is_file() and src.stat().st_mtime <= dst.stat().st_mtime and not validate_render(dst, NOTATION_PUML, src))
        ]
        if to_compile_puml:
            puml_cmd = _find_plantuml_cmd()
            if not puml_cmd:
                errors.append("Outil `plantuml` introuvable dans le PATH")
            else:
                cmd = [
                    *puml_cmd,
                    "-tsvg",
                    "-failfast2",
                    "-charset",
                    "UTF-8",
                    "-o",
                    str(rendus_dir.resolve()),
                    *[str(p.resolve()) for p in to_compile_puml],
                ]
                proc = subprocess.run(
                    cmd,
                    shell=False,
                    capture_output=True,
                    text=True,
                    encoding="utf-8",
                    errors="replace",
                )
                if proc.returncode != 0:
                    detail = (proc.stderr or proc.stdout).strip()
                    errors.append(f"Échec compilation PlantUML (code {proc.returncode}) : {detail}")

        to_compile_mmd = [
            (sc, src, dst)
            for sc, src, dst in mmd_items
            if src.is_file()
            and not (incremental and dst.is_file() and src.stat().st_mtime <= dst.stat().st_mtime and not validate_render(dst, NOTATION_MMD, src))
        ]
        if to_compile_mmd:
            mmdc_cmd = _find_mmdc_cmd()
            if not mmdc_cmd:
                errors.append("Outil `mmdc` (Mermaid CLI) introuvable dans le PATH")
            else:
                env = os.environ.copy()
                pupp_exe = _find_puppeteer_executable()
                if pupp_exe:
                    env["PUPPETEER_EXECUTABLE_PATH"] = pupp_exe
                for sc, src, dst in to_compile_mmd:
                    cmd = [
                        *mmdc_cmd,
                        "-i",
                        str(src.resolve()),
                        "-o",
                        str(dst.resolve()),
                        "-s",
                        "3",
                        "-b",
                        "white",
                    ]
                    proc = subprocess.run(
                        cmd,
                        shell=False,
                        env=env,
                        capture_output=True,
                        text=True,
                        encoding="utf-8",
                        errors="replace",
                    )
                    if proc.returncode != 0:
                        detail = (proc.stderr or proc.stdout).strip()
                        errors.append(
                            f"Échec compilation Mermaid pour {sc['schema_id']} (code {proc.returncode}) : {detail}"
                        )

        for _, src, dst in svg_items:
            if src.is_file():
                src_bytes = src.read_bytes()
                if (
                    not dst.is_file()
                    or dst.read_bytes() != src_bytes
                    or src.stat().st_mtime > dst.stat().st_mtime
                ):
                    dst.write_bytes(src_bytes)

    for sc, src, dst in [*puml_items, *mmd_items, *svg_items]:
        errors.extend(validate_render(dst, sc["recommended_notation"], source_path=src))

    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Valide et compile les 115 schémas du Compendium (52 PlantUML .svg, "
            "23 Mermaid .png 300 DPI et 40 infographies SVG bilingues métier-tech)."
        )
    )
    parser.add_argument(
        "--root",
        "--book-dir",
        dest="root",
        type=Path,
        default=_default_book_dir(),
        help="Racine du dossier `Compendium/ouvrage`",
    )
    parser.add_argument(
        "--catalog",
        type=Path,
        default=_default_catalog_path(),
        help="Chemin vers `catalogue-schemas-prd.json`",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        default=True,
        help="Active la validation stricte (115/115 schémas, 4..14 nœuds, 71/71 familles, rendus propres)",
    )
    parser.add_argument(
        "--no-strict",
        dest="strict",
        action="store_false",
        help="Valide et compile uniquement les schémas présents sur disque",
    )
    parser.add_argument(
        "--ids",
        nargs="+",
        default=None,
        help="Liste explicite d'identifiants `SCH-XX-YY` à traiter",
    )
    parser.add_argument(
        "--check-only",
        action="store_true",
        help="Vérifie sources et rendus existants sans relancer plantuml/mmdc/copie",
    )
    parser.add_argument(
        "--incremental",
        action="store_true",
        help="Évite de recompiler les rendus déjà valides et plus récents que leur source",
    )
    args = parser.parse_args(argv)

    root = args.root.resolve()
    cat_path = args.catalog.resolve()
    errors = compile_schemas(
        root,
        catalog_path=cat_path,
        strict=args.strict,
        check_only=args.check_only,
        schema_ids=args.ids,
        incremental=args.incremental,
    )
    if errors:
        print("ECHEC de validation/compilation des schémas :", file=sys.stderr)
        for err in errors:
            print(f"  - {err}", file=sys.stderr)
        return 1

    all_schemas = load_catalog(cat_path)
    if args.ids:
        wanted = set(args.ids)
        shown = [s for s in all_schemas if s["schema_id"] in wanted]
    elif not args.strict:
        schemas_dir = root / "schemas"
        shown = [
            s
            for s in all_schemas
            if (schemas_dir / f"{s['schema_id']}.{_notation_source_ext(s['recommended_notation'])}").is_file()
        ]
    else:
        shown = all_schemas

    n_tot = len(shown)
    n_puml = sum(1 for s in shown if s.get("recommended_notation") == NOTATION_PUML)
    n_mmd = sum(1 for s in shown if s.get("recommended_notation") == NOTATION_MMD)
    n_svg = sum(1 for s in shown if s.get("recommended_notation") == NOTATION_SVG)
    mode = "--strict" if args.strict else "--no-strict"
    print(
        f"OK : {n_tot}/{len(all_schemas)} schémas valides ({n_puml} PlantUML .svg, "
        f"{n_mmd} Mermaid .png 300 DPI, {n_svg} infographies .svg, {mode}, 4..14 nœuds)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
