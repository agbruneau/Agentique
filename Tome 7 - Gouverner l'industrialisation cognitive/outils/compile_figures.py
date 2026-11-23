#!/usr/bin/env python3
"""Validation et compilation stricte des 23 figures du Tome 7 (Tome 7 - Gouverner l'industrialisation cognitive : 20 schémas vectoriels PlantUML et 3 organigrammes Mermaid haute résolution)."""

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

_TOOLS_DIR = Path(__file__).resolve().parent
if str(_TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(_TOOLS_DIR))

from _communs import compile_forbidden_patterns, match_forbidden_patterns

MIN_NODES_PER_FIGURE = 10
MAX_NODES_PER_FIGURE = 14
EXPECTED_FIGURE_COUNT = 23

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
    # Remove port/field suffix like Node.port if Node is already known
    base = tok.split(".", 1)[0]
    if base in display_to_id:
        return display_to_id[base]
    return tok


def extract_puml_elements(text: str) -> list[str]:
    """Extrait les identifiants uniques de noeuds, participants et etats PlantUML."""
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

        # 1. Explicit element declaration (rectangle, participant, state, actor, ...)
        m_decl = _PUML_DECL_RE.match(line_q)
        if m_decl and not _PUML_ARROW_RE.search(line_q.split(":", 1)[0]):
            rest = m_decl.group(2).strip().rstrip("{").strip()
            rest = re.sub(r"<<[^>]+>>", "", rest).strip()
            rest = re.sub(r"\s+#[A-Za-z0-9_]+$", "", rest).strip()

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
                # Could be `state Foo : description` or `participant __Q0__` or `state S1`
                head = rest.split(":", 1)[0].strip()
                if head.startswith("[") and head.endswith("]"):
                    head = head[1:-1].strip()
                elem_id = _resolve_token(head, quoted, {})
                if elem_id:
                    display_to_id[elem_id] = elem_id
                    _add(elem_id)
            continue

        # 2. Bracketed component declaration `[Nom] as Alias`
        m_br = _PUML_BRACKET_ONLY_RE.match(line_q)
        if m_br:
            disp = m_br.group(1).strip()
            alias = (m_br.group(2) or disp).strip()
            display_to_id[disp] = alias
            display_to_id[alias] = alias
            _add(alias)
            continue

        # 3. Arrow / relation lines (catch implicit sequence participants or bracketed nodes)
        head_no_label = line_q.split(":", 1)[0]
        m_arr = _PUML_ARROW_RE.search(head_no_label)
        if m_arr:
            lhs = head_no_label[: m_arr.start()].strip()
            rhs = head_no_label[m_arr.end() :].strip()
            # Filter out single-token false hits where arrow wasn't actually a connector
            if lhs and rhs:
                _add(_resolve_token(lhs, quoted, display_to_id))
                _add(_resolve_token(rhs, quoted, display_to_id))

    return elements


def extract_mmd_elements(text: str) -> list[str]:
    """Extrait les identifiants uniques de noeuds dans un diagramme Mermaid."""
    cleaned = re.sub(r"%%\{[\s\S]*?\}%%", "", text)
    cleaned = re.sub(r"%%[^\n]*", "", cleaned)

    elements: list[str] = []
    seen: set[str] = set()
    skip_words = {"end", "subgraph", "direction", "flowchart", "graph", "class", "style", "click"}

    def _add_node_expr(expr: str) -> None:
        chunk = expr.strip()
        if not chunk:
            return
        # Remove trailing :::className
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


def count_figure_elements(source_path: Path, engine: str) -> int:
    """Compte le nombre de noeuds, participants ou etats d'un diagramme source."""
    text = source_path.read_text(encoding="utf-8")
    if engine == "puml":
        return len(extract_puml_elements(text))
    if engine == "mmd":
        return len(extract_mmd_elements(text))
    raise ValueError(f"Moteur de figure inconnu : {engine}")


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
            # Prefer newest cached version directory first
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


def validate_render(
    render_path: Path,
    engine: str,
    source_path: Path | None = None,
) -> list[str]:
    """Verifie qu'un rendu SVG ou PNG existe, est a jour, est bien forme et sans erreur."""
    errors: list[str] = []
    if not render_path.is_file():
        return [f"Rendu manquant : {render_path}"]
    size = render_path.stat().st_size
    if size == 0:
        return [f"Rendu vide (0 octet) : {render_path}"]
    if source_path is not None and source_path.is_file():
        if source_path.stat().st_mtime > render_path.stat().st_mtime:
            errors.append(
                f"Rendu obsolete ({source_path.name} modifie apres {render_path.name}) : {render_path}"
            )

    if engine == "puml":
        content = render_path.read_text(encoding="utf-8", errors="replace")
        if "<svg" not in content or "</svg>" not in content:
            errors.append(f"SVG invalide (balise <svg> manquante) : {render_path}")
            return errors
        for marker in _SVG_ERROR_MARKERS:
            if marker in content:
                errors.append(f"Erreur de rendu PlantUML ({marker}) dans {render_path}")
        try:
            root = ET.fromstring(content)
            if not root.tag.endswith("svg"):
                errors.append(f"Racine XML inattendue dans {render_path} : {root.tag}")
        except ET.ParseError as exc:
            errors.append(f"SVG XML mal forme dans {render_path} : {exc}")
    elif engine == "mmd":
        data = render_path.read_bytes()
        if len(data) < 24 or data[:8] != b"\x89PNG\r\n\x1a\n":
            errors.append(f"Signature PNG invalide : {render_path}")
            return errors
        width, height = struct.unpack(">II", data[16:24])
        if width < 200 or height < 150:
            errors.append(f"Resolution PNG insuffisante ({width}x{height}) : {render_path}")
    else:
        errors.append(f"Moteur inconnu pour validation de rendu : {engine}")
    return errors


def _load_manifest(book_dir: Path) -> tuple[dict | None, list[str]]:
    manifest_path = book_dir / "specs" / "manifest.json"
    if not manifest_path.is_file():
        return None, [f"Manifeste introuvable : {manifest_path}"]
    try:
        return json.loads(manifest_path.read_text(encoding="utf-8")), []
    except json.JSONDecodeError as exc:
        return None, [f"Manifeste JSON invalide : {exc}"]


def validate_sources(book_dir: Path, strict: bool = True) -> tuple[list[dict], list[str]]:
    """Valide toutes les sources declarees dans manifest.json."""
    manifest, errors = _load_manifest(book_dir)
    if manifest is None:
        return [], errors

    figures = manifest.get("figures", [])
    if strict and len(figures) != EXPECTED_FIGURE_COUNT:
        errors.append(
            f"Nombre de figures declarees attendu = {EXPECTED_FIGURE_COUNT}, trouve = {len(figures)}"
        )

    compiled_regexes = compile_forbidden_patterns(manifest.get("forbidden_prose_regexes", []))

    diag_dir = book_dir / "diagrammes"
    for fig in figures:
        fid = fig["id"]
        engine = fig["engine"]
        ext = "puml" if engine == "puml" else "mmd" if engine == "mmd" else None
        if ext is None:
            errors.append(f"Moteur non supporte pour {fid} : {engine}")
            continue

        src = diag_dir / f"{fid}.{ext}"
        if not src.is_file():
            errors.append(f"Source de figure manquante : {src}")
            continue

        text = src.read_text(encoding="utf-8")
        for pat_str in match_forbidden_patterns(text, compiled_regexes):
            errors.append(f"Code ou formule bannie ({pat_str}) detecte dans {src}")

        elem_count = count_figure_elements(src, engine)
        if elem_count == 0:
            errors.append(f"Aucun element detecte dans {src}")
        elif elem_count < MIN_NODES_PER_FIGURE:
            errors.append(
                f"Densite insuffisante dans {src} : {elem_count} elements (min {MIN_NODES_PER_FIGURE}, cible 10..14)"
            )
        elif elem_count > MAX_NODES_PER_FIGURE:
            errors.append(
                f"Depassement de densite dans {src} : {elem_count} elements (max {MAX_NODES_PER_FIGURE})"
            )

    return figures, errors


def compile_figures(
    book_dir: Path,
    strict: bool = True,
    check_only: bool = False,
) -> list[str]:
    """Valide les sources, compile les 23 figures et controle chaque rendu."""
    figures, errors = validate_sources(book_dir, strict=strict)
    if errors and strict and not check_only:
        return errors

    diag_dir = book_dir / "diagrammes"
    rendus_dir = diag_dir / "rendus"
    rendus_dir.mkdir(parents=True, exist_ok=True)

    puml_items: list[tuple[dict, Path, Path]] = []
    mmd_items: list[tuple[dict, Path, Path]] = []
    for fig in figures:
        fid = fig["id"]
        engine = fig["engine"]
        if engine == "puml":
            puml_items.append((fig, diag_dir / f"{fid}.puml", rendus_dir / f"{fid}.svg"))
        elif engine == "mmd":
            mmd_items.append((fig, diag_dir / f"{fid}.mmd", rendus_dir / f"{fid}.png"))

    if not check_only:
        existing_puml = [src for _, src, _ in puml_items if src.is_file()]
        if existing_puml:
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
                    *[str(p.resolve()) for p in existing_puml],
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
                    errors.append(f"Echec compilation PlantUML (code {proc.returncode}) : {detail}")

        existing_mmd = [(fig, src, dst) for fig, src, dst in mmd_items if src.is_file()]
        if existing_mmd:
            mmdc_cmd = _find_mmdc_cmd()
            if not mmdc_cmd:
                errors.append("Outil `mmdc` (Mermaid CLI) introuvable dans le PATH")
            else:
                env = os.environ.copy()
                pupp_exe = _find_puppeteer_executable()
                if pupp_exe:
                    env["PUPPETEER_EXECUTABLE_PATH"] = pupp_exe
                for fig, src, dst in existing_mmd:
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
                            f"Echec compilation Mermaid pour {fig['id']} (code {proc.returncode}) : {detail}"
                        )

    for fig, src, dst in [*puml_items, *mmd_items]:
        errors.extend(validate_render(dst, fig["engine"], source_path=src))

    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Valide et compile les 23 figures du Tome 7 (Tome 7 - Gouverner l'industrialisation cognitive : "
            "20 schémas vectoriels PlantUML et 3 organigrammes Mermaid haute résolution)."
        )
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parent.parent,
        help="Racine du dossier `Tome 7 - Gouverner l'industrialisation cognitive`",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        default=True,
        help="Active la validation stricte (10..14 noeuds, 0 code banni, 23 rendus propres et a jour)",
    )
    parser.add_argument(
        "--no-strict",
        dest="strict",
        action="store_false",
        help="Desactive le controle strict du nombre de figures",
    )
    parser.add_argument(
        "--check-only",
        action="store_true",
        help="Verifie sources et rendus existants sans relancer plantuml/mmdc",
    )
    args = parser.parse_args(argv)

    errors = compile_figures(args.root.resolve(), strict=args.strict, check_only=args.check_only)
    if errors:
        print("ECHEC de validation/compilation des figures :", file=sys.stderr)
        for err in errors:
            print(f"  - {err}", file=sys.stderr)
        return 1

    print(
        "OK : 23/23 figures (20 schémas vectoriels PlantUML et 3 organigrammes Mermaid haute résolution) "
        "valides (--strict, 10..14 noeuds, 0 code banni)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
