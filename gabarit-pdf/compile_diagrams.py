#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Compilateur reutilisable des diagrammes PlantUML (.puml -> .svg) et Mermaid (.mmd -> .png).

Destine aux tomes du catalogue `gabarit-pdf/volumes.json` (notamment tomes 1 a 6) ou a tout
repertoire arbitraire (`--input-dir`). Prend en charge :
  - l'execution parallele (`-nbthread` pour PlantUML, `ThreadPoolExecutor` pour Mermaid CLI) ;
  - le cache incremental fonde sur la fraicheur (mtime) et la validite structurelle des rendus ;
  - la reconstruction integrale via `--force` et la verification seule via `--check-only` ;
  - la production d'un rapport console et/ou JSON (`--json`, `--json-report`).
"""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import json
import os
from pathlib import Path
import re
import shutil
import struct
import subprocess
import sys
import tempfile
import time
from typing import Any
import xml.etree.ElementTree as ET

GABARIT_DIR = Path(__file__).resolve().parent
REPO_ROOT = GABARIT_DIR.parent
if str(GABARIT_DIR) not in sys.path:
    sys.path.insert(0, str(GABARIT_DIR))

from compile_pdf import CATALOG_PATH, get_volume_config, load_catalog  # noqa: E402

DEFAULT_LEGACY_VOLUME_IDS = ("1", "2", "3", "4", "5", "6")
DEFAULT_MERMAID_SCALE = 3
DEFAULT_MERMAID_BACKGROUND = "white"
DEFAULT_PUML_BATCH_SIZE = 25

_SVG_ERROR_MARKERS = (
    "Syntax Error",
    "Some diagram description contains errors",
    "No diagram found",
    "Dot executable",
    "Cannot find Graphviz",
    "PlantUML has crashed",
    "You should send a mail to plantuml@gmail.com",
)


def _find_java_executable(hint_cmd_path: Path | None = None) -> str | None:
    """Localise `java.exe` / `java` en privilegiant la cible declaree dans `plantuml.cmd` si presente."""
    if hint_cmd_path and hint_cmd_path.is_file() and hint_cmd_path.suffix.lower() in {".cmd", ".bat"}:
        try:
            content = hint_cmd_path.read_text(encoding="utf-8", errors="replace")
            m = re.search(r'"([^"]*java(?:\.exe)?)"', content, re.IGNORECASE)
            if m:
                expanded = os.path.expandvars(m.group(1))
                if Path(expanded).is_file():
                    return expanded
        except OSError:
            pass
    found = shutil.which("java")
    if found:
        return found
    return None


def _find_plantuml_cmd() -> list[str] | None:
    """Resout la commande PlantUML.

    Sous Windows, si `plantuml.jar` et `java` sont disponibles, invoque `java -jar plantuml.jar`
    directement afin d'eviter la limite de 8191 caracteres et le transcodage OEM de `cmd.exe`
    sur les noms de fichiers accentues.
    """
    cmd_path: Path | None = None
    for candidate in ("plantuml", "plantuml.cmd", "plantuml.bat"):
        found = shutil.which(candidate)
        if found:
            cmd_path = Path(found)
            break
    if cmd_path is None:
        local_app = os.environ.get("LOCALAPPDATA")
        if local_app:
            fallback = Path(local_app) / "Programs" / "PlantUML" / "plantuml.cmd"
            if fallback.is_file():
                cmd_path = fallback

    jar_candidates: list[Path] = []
    if cmd_path is not None:
        jar_candidates.append(cmd_path.parent / "plantuml.jar")
    local_app = os.environ.get("LOCALAPPDATA")
    if local_app:
        jar_candidates.append(Path(local_app) / "Programs" / "PlantUML" / "plantuml.jar")

    for jar_path in jar_candidates:
        if jar_path.is_file():
            java_exe = _find_java_executable(cmd_path)
            if java_exe:
                return [
                    java_exe,
                    "-Djava.awt.headless=true",
                    "-Dfile.encoding=UTF-8",
                    "-jar",
                    str(jar_path),
                ]

    if cmd_path is not None:
        return [str(cmd_path)]
    return None


def _find_mmdc_cmd() -> list[str] | None:
    """Resout la commande Mermaid CLI (`mmdc`), en contournant `cmd.exe` sous Windows si possible."""
    cmd_path: Path | None = None
    for candidate in ("mmdc", "mmdc.cmd"):
        found = shutil.which(candidate)
        if found:
            cmd_path = Path(found)
            break
    if cmd_path is None:
        app_data = os.environ.get("APPDATA")
        if app_data:
            fallback = Path(app_data) / "npm" / "mmdc.cmd"
            if fallback.is_file():
                cmd_path = fallback

    if cmd_path is None:
        return None

    # Sous Windows, invoquer node + cli.js directement preserve les chemins Unicode sans cmd.exe
    if cmd_path.suffix.lower() in {".cmd", ".bat"} or os.name == "nt":
        cli_js = cmd_path.parent / "node_modules" / "@mermaid-js" / "mermaid-cli" / "src" / "cli.js"
        if cli_js.is_file():
            node_local = cmd_path.parent / "node.exe"
            node_exe = str(node_local) if node_local.is_file() else shutil.which("node")
            if node_exe:
                return [node_exe, str(cli_js)]

    return [str(cmd_path)]


def _find_puppeteer_executable() -> str | None:
    """Localise un navigateur Chromium/Edge compatible avec Puppeteer pour `mmdc`."""
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


def validate_render(
    render_path: Path,
    engine: str,
    source_path: Path | None = None,
    *,
    check_mtime: bool = True,
) -> list[str]:
    """Verifie qu'un rendu SVG ou PNG existe, est non vide, bien forme, sans erreur et a jour."""
    errors: list[str] = []
    if not render_path.is_file():
        return [f"Rendu manquant : {render_path}"]
    size = render_path.stat().st_size
    if size == 0:
        return [f"Rendu vide (0 octet) : {render_path}"]
    if check_mtime and source_path is not None and source_path.is_file():
        if source_path.stat().st_mtime > render_path.stat().st_mtime + 1e-3:
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
        if width < 80 or height < 40:
            errors.append(f"Resolution PNG insuffisante ({width}x{height}) : {render_path}")
    else:
        errors.append(f"Moteur inconnu pour validation de rendu : {engine}")
    return errors


def is_render_cached(src: Path, dst: Path, engine: str) -> bool:
    """Retourne True si le rendu existe, est a jour par rapport a `src` et passe la validation."""
    if not dst.is_file():
        return False
    return len(validate_render(dst, engine, source_path=src, check_mtime=True)) == 0


def resolve_volume_diagram_dirs(
    volume_ref: str,
    *,
    repo_root: Path = REPO_ROOT,
    catalog_path: Path = CATALOG_PATH,
) -> tuple[dict[str, Any], Path, Path]:
    """Resout `(config, source_dir, rendered_dir)` pour un volume du catalogue."""
    cfg = get_volume_config(volume_ref, catalog_path=catalog_path)
    rendered_rel = cfg.get("rendered_diagrams_dir")
    if not rendered_rel:
        raise ValueError(f"Le volume {cfg['id']} ({cfg['slug']}) ne declare pas `rendered_diagrams_dir`.")
    rendered_dir = Path(rendered_rel)
    if not rendered_dir.is_absolute():
        rendered_dir = repo_root / rendered_dir

    source_rel = cfg.get("diagrams_dir")
    if source_rel:
        source_dir = Path(source_rel)
        if not source_dir.is_absolute():
            source_dir = repo_root / source_dir
    else:
        source_dir = rendered_dir.parent

    return cfg, source_dir, rendered_dir


def discover_diagrams(source_dir: Path) -> list[tuple[Path, str]]:
    """Recense les sources `.puml` et `.mmd` directement presentes dans `source_dir`."""
    if not source_dir.is_dir():
        return []
    items: list[tuple[Path, str]] = []
    for fp in sorted(source_dir.iterdir(), key=lambda p: p.name.lower()):
        if not fp.is_file():
            continue
        ext = fp.suffix.lower()
        if ext == ".puml":
            items.append((fp, "puml"))
        elif ext == ".mmd":
            items.append((fp, "mmd"))
    return items


_CANONICAL_NAME_RE = re.compile(r"^(Figure|Fig)[\.-](\d+(?:\.\d+)?)\b", re.IGNORECASE)


def canonical_render_stem(src: Path) -> str:
    """Derive un nom de sortie canonique court (`Figure-01.0`, `Fig-01`) si reconnu, sinon `src.stem`."""
    m = _CANONICAL_NAME_RE.match(src.stem)
    if not m:
        return src.stem
    prefix = "Figure" if m.group(1).lower() == "figure" else "Fig"
    return f"{prefix}-{m.group(2)}"


def _build_render_targets(
    discovered: list[tuple[Path, str]],
    rendered_dir: Path,
    *,
    canonical_names: bool = True,
) -> list[tuple[Path, str, Path]]:
    """Associe chaque source a sa cible `.svg`/`.png` sans collision."""
    if not canonical_names:
        return [
            (src, engine, rendered_dir / f"{src.stem}{'.svg' if engine == 'puml' else '.png'}")
            for src, engine in discovered
        ]

    counts: dict[str, int] = {}
    proposed: list[tuple[Path, str, str]] = []
    for src, engine in discovered:
        suffix = ".svg" if engine == "puml" else ".png"
        cand = f"{canonical_render_stem(src)}{suffix}"
        counts[cand.lower()] = counts.get(cand.lower(), 0) + 1
        proposed.append((src, engine, cand))

    targets: list[tuple[Path, str, Path]] = []
    for src, engine, cand in proposed:
        suffix = ".svg" if engine == "puml" else ".png"
        final_name = cand if counts[cand.lower()] == 1 else f"{src.stem}{suffix}"
        targets.append((src, engine, rendered_dir / final_name))
    return targets


def _diagnose_single_puml(src: Path, puml_cmd: list[str], timeout: int = 120) -> str:
    """Execute `plantuml -checkonly` sur un fichier unique pour obtenir le diagnostic exact."""
    cmd = [*puml_cmd, "-checkonly", "-charset", "UTF-8", str(src.resolve())]
    try:
        proc = subprocess.run(
            cmd,
            shell=False,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=timeout,
        )
        detail = (proc.stderr or proc.stdout or "").strip()
        if detail:
            return detail
        return f"Code de retour PlantUML {proc.returncode}"
    except subprocess.TimeoutExpired:
        return f"Depassement de delai ({timeout}s) lors du diagnostic PlantUML"


def _compile_puml_items(
    items: list[tuple[Path, Path]],
    rendered_dir: Path,
    *,
    puml_cmd: list[str] | None,
    workers: int = 4,
    batch_size: int = DEFAULT_PUML_BATCH_SIZE,
    timeout: int = 300,
    volume_id: str | None = None,
) -> list[dict[str, Any]]:
    """Compile un lot de fichiers `.puml` en `.svg` via PlantUML (multi-thread JVM)."""
    if not items:
        return []
    results: list[dict[str, Any]] = []
    if not puml_cmd:
        for src, dst in items:
            results.append(
                {
                    "volume": volume_id,
                    "source": str(src),
                    "output": str(dst),
                    "engine": "puml",
                    "status": "failed",
                    "duration_s": 0.0,
                    "errors": ["Outil `plantuml` introuvable dans le PATH"],
                }
            )
        return results

    rendered_dir.mkdir(parents=True, exist_ok=True)
    nbthread = max(1, workers)
    step = max(1, batch_size)

    for idx in range(0, len(items), step):
        chunk = items[idx : idx + step]
        t0 = time.perf_counter()
        batch_error: str | None = None
        with tempfile.TemporaryDirectory(prefix="puml_stage_") as stage_str:
            stage_dir = Path(stage_str)
            cmd = [
                *puml_cmd,
                "-tsvg",
                "-charset",
                "UTF-8",
                "-nbthread",
                str(nbthread),
                "-o",
                str(stage_dir.resolve()),
                *[str(src.resolve()) for src, _ in chunk],
            ]
            try:
                proc = subprocess.run(
                    cmd,
                    shell=False,
                    capture_output=True,
                    text=True,
                    encoding="utf-8",
                    errors="replace",
                    timeout=timeout,
                )
                if proc.returncode != 0:
                    detail = (proc.stderr or proc.stdout or "").strip()
                    batch_error = f"PlantUML code {proc.returncode}" + (f" : {detail}" if detail else "")
            except subprocess.TimeoutExpired:
                batch_error = f"Depassement de delai ({timeout}s) lors de la compilation PlantUML"

            elapsed = round((time.perf_counter() - t0) / max(1, len(chunk)), 3)

            for src, dst in chunk:
                staged_svg = stage_dir / f"{src.stem}.svg"
                errs = validate_render(staged_svg, "puml", source_path=src, check_mtime=False)
                if errs:
                    if dst.is_file():
                        dst.unlink(missing_ok=True)
                    diag = _diagnose_single_puml(src, puml_cmd)
                    if diag and diag not in errs:
                        errs.append(diag)
                    elif batch_error and batch_error not in errs:
                        errs.append(batch_error)
                    results.append(
                        {
                            "volume": volume_id,
                            "source": str(src),
                            "output": str(dst),
                            "engine": "puml",
                            "status": "failed",
                            "duration_s": elapsed,
                            "errors": errs,
                        }
                    )
                else:
                    shutil.move(str(staged_svg), str(dst))
                    results.append(
                        {
                            "volume": volume_id,
                            "source": str(src),
                            "output": str(dst),
                            "engine": "puml",
                            "status": "compiled",
                            "duration_s": elapsed,
                            "errors": [],
                        }
                    )
    return results


def _compile_single_mmd(
    src: Path,
    dst: Path,
    *,
    mmdc_cmd: list[str],
    env: dict[str, str],
    scale: int = DEFAULT_MERMAID_SCALE,
    background: str = DEFAULT_MERMAID_BACKGROUND,
    timeout: int = 120,
    volume_id: str | None = None,
) -> dict[str, Any]:
    """Compile un fichier `.mmd` unique en PNG haute resolution via `mmdc`."""
    t0 = time.perf_counter()
    cmd = [
        *mmdc_cmd,
        "-i",
        str(src.resolve()),
        "-o",
        str(dst.resolve()),
        "-s",
        str(scale),
        "-b",
        background,
    ]
    errors: list[str] = []
    try:
        proc = subprocess.run(
            cmd,
            shell=False,
            env=env,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=timeout,
        )
        if proc.returncode != 0:
            detail = (proc.stderr or proc.stdout or "").strip()
            errors.append(
                f"Echec compilation Mermaid pour {src.name} (code {proc.returncode})"
                + (f" : {detail}" if detail else "")
            )
    except subprocess.TimeoutExpired:
        errors.append(f"Depassement de delai ({timeout}s) lors de la compilation Mermaid pour {src.name}")

    if not errors:
        errors.extend(validate_render(dst, "mmd", source_path=src, check_mtime=False))

    elapsed = round(time.perf_counter() - t0, 3)
    if errors:
        if dst.is_file():
            dst.unlink(missing_ok=True)
        return {
            "volume": volume_id,
            "source": str(src),
            "output": str(dst),
            "engine": "mmd",
            "status": "failed",
            "duration_s": elapsed,
            "errors": errors,
        }
    return {
        "volume": volume_id,
        "source": str(src),
        "output": str(dst),
        "engine": "mmd",
        "status": "compiled",
        "duration_s": elapsed,
        "errors": [],
    }


def _compile_mmd_items(
    items: list[tuple[Path, Path]],
    rendered_dir: Path,
    *,
    mmdc_cmd: list[str] | None,
    workers: int = 4,
    scale: int = DEFAULT_MERMAID_SCALE,
    background: str = DEFAULT_MERMAID_BACKGROUND,
    timeout: int = 120,
    volume_id: str | None = None,
) -> list[dict[str, Any]]:
    """Compile en parallele un ensemble de fichiers `.mmd` via `ThreadPoolExecutor`."""
    if not items:
        return []
    if not mmdc_cmd:
        return [
            {
                "volume": volume_id,
                "source": str(src),
                "output": str(dst),
                "engine": "mmd",
                "status": "failed",
                "duration_s": 0.0,
                "errors": ["Outil `mmdc` (Mermaid CLI) introuvable dans le PATH"],
            }
            for src, dst in items
        ]

    rendered_dir.mkdir(parents=True, exist_ok=True)
    env = os.environ.copy()
    pupp_exe = _find_puppeteer_executable()
    if pupp_exe:
        env["PUPPETEER_EXECUTABLE_PATH"] = pupp_exe

    max_workers = max(1, min(workers, len(items)))
    results_by_src: dict[Path, dict[str, Any]] = {}
    with ThreadPoolExecutor(max_workers=max_workers) as pool:
        fut_map = {
            pool.submit(
                _compile_single_mmd,
                src,
                dst,
                mmdc_cmd=mmdc_cmd,
                env=env,
                scale=scale,
                background=background,
                timeout=timeout,
                volume_id=volume_id,
            ): src
            for src, dst in items
        }
        for fut in as_completed(fut_map):
            src = fut_map[fut]
            results_by_src[src] = fut.result()

    return [results_by_src[src] for src, _ in items]


def compile_directory(
    source_dir: Path,
    rendered_dir: Path,
    *,
    volume_id: str | None = None,
    volume_slug: str | None = None,
    force: bool = False,
    check_only: bool = False,
    workers: int = 4,
    scale: int = DEFAULT_MERMAID_SCALE,
    background: str = DEFAULT_MERMAID_BACKGROUND,
    puml_batch_size: int = DEFAULT_PUML_BATCH_SIZE,
    puml_cmd: list[str] | None = None,
    mmdc_cmd: list[str] | None = None,
) -> dict[str, Any]:
    """Compile ou verifie tous les diagrammes `.puml` et `.mmd` d'un repertoire vers `rendered_dir`."""
    t0 = time.perf_counter()
    discovered = discover_diagrams(source_dir)
    results: list[dict[str, Any]] = []
    puml_todo: list[tuple[Path, Path]] = []
    mmd_todo: list[tuple[Path, Path]] = []

    if not source_dir.is_dir():
        err_msg = f"Repertoire de diagrammes introuvable : {source_dir}"
        return {
            "volume": volume_id,
            "slug": volume_slug,
            "source_dir": str(source_dir),
            "rendered_dir": str(rendered_dir),
            "summary": {
                "total": 0,
                "puml": 0,
                "mmd": 0,
                "compiled": 0,
                "skipped_cached": 0,
                "ok": 0,
                "failed": 1,
                "duration_s": round(time.perf_counter() - t0, 3),
            },
            "results": [],
            "errors": [{"volume": volume_id, "source": str(source_dir), "errors": [err_msg]}],
        }

    for src, engine, dst in _build_render_targets(discovered, rendered_dir, canonical_names=True):
        if check_only:
            errs = validate_render(dst, engine, source_path=src, check_mtime=True)
            results.append(
                {
                    "volume": volume_id,
                    "source": str(src),
                    "output": str(dst),
                    "engine": engine,
                    "status": "ok" if not errs else "failed",
                    "duration_s": 0.0,
                    "errors": errs,
                }
            )
            continue

        if not force and is_render_cached(src, dst, engine):
            results.append(
                {
                    "volume": volume_id,
                    "source": str(src),
                    "output": str(dst),
                    "engine": engine,
                    "status": "cached",
                    "duration_s": 0.0,
                    "errors": [],
                }
            )
            continue

        if engine == "puml":
            puml_todo.append((src, dst))
        else:
            mmd_todo.append((src, dst))

    if not check_only:
        if puml_todo:
            resolved_puml = puml_cmd if puml_cmd is not None else _find_plantuml_cmd()
            results.extend(
                _compile_puml_items(
                    puml_todo,
                    rendered_dir,
                    puml_cmd=resolved_puml,
                    workers=workers,
                    batch_size=puml_batch_size,
                    volume_id=volume_id,
                )
            )
        if mmd_todo:
            resolved_mmd = mmdc_cmd if mmdc_cmd is not None else _find_mmdc_cmd()
            results.extend(
                _compile_mmd_items(
                    mmd_todo,
                    rendered_dir,
                    mmdc_cmd=resolved_mmd,
                    workers=workers,
                    scale=scale,
                    background=background,
                    volume_id=volume_id,
                )
            )

    results.sort(key=lambda r: Path(r["source"]).name.lower())
    n_puml = sum(1 for _, eng in discovered if eng == "puml")
    n_mmd = sum(1 for _, eng in discovered if eng == "mmd")
    n_compiled = sum(1 for r in results if r["status"] == "compiled")
    n_cached = sum(1 for r in results if r["status"] == "cached")
    n_ok = sum(1 for r in results if r["status"] == "ok")
    n_failed = sum(1 for r in results if r["status"] == "failed")
    error_entries = [
        {"volume": r["volume"], "source": r["source"], "output": r["output"], "errors": r["errors"]}
        for r in results
        if r["errors"]
    ]

    return {
        "volume": volume_id,
        "slug": volume_slug,
        "source_dir": str(source_dir),
        "rendered_dir": str(rendered_dir),
        "summary": {
            "total": len(discovered),
            "puml": n_puml,
            "mmd": n_mmd,
            "compiled": n_compiled,
            "skipped_cached": n_cached,
            "ok": n_ok,
            "failed": n_failed,
            "duration_s": round(time.perf_counter() - t0, 3),
        },
        "results": results,
        "errors": error_entries,
    }


def compile_volumes(
    volume_refs: list[str],
    *,
    repo_root: Path = REPO_ROOT,
    catalog_path: Path = CATALOG_PATH,
    force: bool = False,
    check_only: bool = False,
    workers: int = 4,
    scale: int = DEFAULT_MERMAID_SCALE,
    background: str = DEFAULT_MERMAID_BACKGROUND,
    puml_batch_size: int = DEFAULT_PUML_BATCH_SIZE,
) -> dict[str, Any]:
    """Compile ou verifie les diagrammes d'une liste de volumes du catalogue."""
    t0 = time.perf_counter()
    volume_reports: list[dict[str, Any]] = []
    all_errors: list[dict[str, Any]] = []

    puml_cmd = None if check_only else _find_plantuml_cmd()
    mmdc_cmd = None if check_only else _find_mmdc_cmd()

    for ref in volume_refs:
        cfg, src_dir, rendus_dir = resolve_volume_diagram_dirs(
            ref, repo_root=repo_root, catalog_path=catalog_path
        )
        rep = compile_directory(
            src_dir,
            rendus_dir,
            volume_id=cfg["id"],
            volume_slug=cfg["slug"],
            force=force,
            check_only=check_only,
            workers=workers,
            scale=scale,
            background=background,
            puml_batch_size=puml_batch_size,
            puml_cmd=puml_cmd,
            mmdc_cmd=mmdc_cmd,
        )
        volume_reports.append(rep)
        all_errors.extend(rep["errors"])

    summary = {
        "volumes": len(volume_reports),
        "total": sum(r["summary"]["total"] for r in volume_reports),
        "puml": sum(r["summary"]["puml"] for r in volume_reports),
        "mmd": sum(r["summary"]["mmd"] for r in volume_reports),
        "compiled": sum(r["summary"]["compiled"] for r in volume_reports),
        "skipped_cached": sum(r["summary"]["skipped_cached"] for r in volume_reports),
        "ok": sum(r["summary"]["ok"] for r in volume_reports),
        "failed": sum(r["summary"]["failed"] for r in volume_reports),
        "duration_s": round(time.perf_counter() - t0, 3),
    }
    return {
        "mode": "check-only" if check_only else ("force" if force else "incremental"),
        "summary": summary,
        "volumes": volume_reports,
        "errors": all_errors,
    }


def _parse_volume_args(raw_volumes: list[str]) -> list[str]:
    refs: list[str] = []
    for item in raw_volumes:
        for part in item.split(","):
            tok = part.strip()
            if tok and tok not in refs:
                refs.append(tok)
    return refs


def _print_console_report(report: dict[str, Any]) -> None:
    if "volumes" in report:
        for vrep in report["volumes"]:
            s = vrep["summary"]
            label = f"[{vrep['volume']}] {vrep['slug']}" if vrep.get("volume") else vrep["source_dir"]
            status_tag = "OK" if s["failed"] == 0 else "ECHEC"
            print(
                f"{status_tag} {label} : {s['total']} diagrammes "
                f"({s['puml']} .puml, {s['mmd']} .mmd) — "
                f"compiles={s['compiled']}, cache={s['skipped_cached']}, "
                f"ok={s['ok']}, echecs={s['failed']} ({s['duration_s']:.2f}s)"
            )
        tot = report["summary"]
        print(
            f"TOTAL ({report['mode']}) : {tot['total']} diagrammes — "
            f"compiles={tot['compiled']}, cache={tot['skipped_cached']}, "
            f"ok={tot['ok']}, echecs={tot['failed']} ({tot['duration_s']:.2f}s)"
        )
    else:
        s = report["summary"]
        status_tag = "OK" if s["failed"] == 0 else "ECHEC"
        print(
            f"{status_tag} {report['source_dir']} -> {report['rendered_dir']} : "
            f"{s['total']} diagrammes ({s['puml']} .puml, {s['mmd']} .mmd) — "
            f"compiles={s['compiled']}, cache={s['skipped_cached']}, "
            f"ok={s['ok']}, echecs={s['failed']} ({s['duration_s']:.2f}s)"
        )

    errors = report.get("errors") or []
    if errors:
        print("\nErreurs detectees :", file=sys.stderr)
        for entry in errors:
            src_name = Path(entry["source"]).name
            prefix = f"[Vol {entry['volume']}] " if entry.get("volume") else ""
            for msg in entry.get("errors", []):
                print(f"  - {prefix}{src_name} : {msg}", file=sys.stderr)


def main(argv: list[str] | None = None) -> int:
    default_workers = max(1, min(4, os.cpu_count() or 2))
    parser = argparse.ArgumentParser(
        description=(
            "Compilateur reutilisable des diagrammes PlantUML (.svg) et Mermaid (.png) "
            "de la collection Agentique."
        )
    )
    target = parser.add_mutually_exclusive_group(required=True)
    target.add_argument(
        "--volume",
        action="append",
        help="Identifiant (1..8), slug (ex. Tome 1 - ...), nom de tome (ex. Tome 5) ou liste séparée par des virgules (ex. --volume 1,2,3)",
    )
    target.add_argument(
        "--all",
        action="store_true",
        help="Compiler les diagrammes des tomes 1 à 6 du catalogue",
    )
    target.add_argument(
        "--all-volumes",
        action="store_true",
        help="Compiler les diagrammes de tous les tomes (1 à 8) du catalogue",
    )
    target.add_argument(
        "--input-dir",
        type=Path,
        help="Repertoire arbitraire contenant des sources .puml et/ou .mmd",
    )

    parser.add_argument(
        "--output-dir",
        type=Path,
        help="Repertoire de sortie (avec --input-dir ; defaut : <input-dir>/rendus)",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Reconstruire tous les rendus meme s'ils sont deja a jour en cache",
    )
    parser.add_argument(
        "--check-only",
        action="store_true",
        help="Verifier les rendus existants sans lancer plantuml ni mmdc",
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=default_workers,
        help=f"Nombre de travailleurs paralleles (defaut : {default_workers})",
    )
    parser.add_argument(
        "--scale",
        type=int,
        default=DEFAULT_MERMAID_SCALE,
        help=f"Facteur d'echelle PNG pour Mermaid CLI (defaut : {DEFAULT_MERMAID_SCALE})",
    )
    parser.add_argument(
        "--background",
        default=DEFAULT_MERMAID_BACKGROUND,
        help=f"Couleur de fond Mermaid PNG (defaut : {DEFAULT_MERMAID_BACKGROUND})",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Afficher le rapport complet en JSON sur stdout",
    )
    parser.add_argument(
        "--json-report",
        type=Path,
        help="Ecrire le rapport JSON detaille dans ce fichier",
    )
    args = parser.parse_args(argv)

    if args.input_dir is not None:
        src_dir = args.input_dir.resolve()
        out_dir = (args.output_dir or (src_dir / "rendus")).resolve()
        report: dict[str, Any] = compile_directory(
            src_dir,
            out_dir,
            force=args.force,
            check_only=args.check_only,
            workers=args.workers,
            scale=args.scale,
            background=args.background,
        )
    else:
        if args.all:
            refs = list(DEFAULT_LEGACY_VOLUME_IDS)
        elif args.all_volumes:
            catalog = load_catalog()
            refs = [v["id"] for v in catalog["volumes"]]
        else:
            refs = _parse_volume_args(args.volume)
        report = compile_volumes(
            refs,
            force=args.force,
            check_only=args.check_only,
            workers=args.workers,
            scale=args.scale,
            background=args.background,
        )

    if args.json_report is not None:
        args.json_report.parent.mkdir(parents=True, exist_ok=True)
        args.json_report.write_text(
            json.dumps(report, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
            newline="\n",
        )

    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        _print_console_report(report)

    return 0 if report["summary"]["failed"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
