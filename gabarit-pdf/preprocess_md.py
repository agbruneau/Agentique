# SPDX-License-Identifier: MIT
"""Pre-traitement Markdown partage pour adapter les 8 tomes du depot au gabarit Typst."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

_FENCE_OPEN_RE = re.compile(r"^[ \t]*(`{3,}|~{3,})")


def extract_yaml_frontmatter(md_text: str) -> tuple[str, dict[str, str]]:
    """Retire un bloc YAML liminaire (`--- ... ---`) et extrait les champs scalaires simples."""
    lines = md_text.splitlines(keepends=True)
    if not lines or lines[0].strip() != "---":
        return md_text, {}
    end_idx = -1
    for i in range(1, len(lines)):
        if lines[i].strip() in ("---", "..."):
            end_idx = i
            break
    if end_idx == -1:
        return md_text, {}

    meta: dict[str, str] = {}
    for ln in lines[1:end_idx]:
        m = re.match(r"^([A-Za-z0-9_-]+)\s*:\s*(.*)$", ln.strip())
        if m:
            key = m.group(1).strip()
            val = m.group(2).strip()
            if len(val) >= 2 and val[0] == val[-1] and val[0] in ('"', "'"):
                val = val[1:-1]
            meta[key] = val

    body = "".join(lines[end_idx + 1 :]).lstrip("\r\n")
    return body, meta


def _iter_lines_with_fence_state(lines: list[str]):
    """Genere (index, line, in_fence) en respectant les blocs de code clotures."""
    fence_char: str | None = None
    fence_len = 0
    for idx, line in enumerate(lines):
        raw = line.rstrip("\r\n")
        if fence_char is None:
            m = _FENCE_OPEN_RE.match(raw)
            if m:
                fence_char = m.group(1)[0]
                fence_len = len(m.group(1))
                yield idx, line, True
                continue
            yield idx, line, False
        else:
            yield idx, line, True
            st = raw.strip()
            if st.startswith(fence_char * fence_len) and st == fence_char * len(st):
                fence_char = None
                fence_len = 0


def strip_legacy_preamble(md_text: str, keep_from_heading: str | None = None, wrap_orphan_intro: str | None = None) -> str:
    """Supprime le preambule de couverture aplati en tete des tomes 1-6.

    Si `keep_from_heading` est fourni (regex sur ligne H1), coupe avant ce titre.
    Si `wrap_orphan_intro` est fourni (ex. presentation des 5 livres du Tome 1 entre
    le tableau de metadonnees et `# Table des matières`), conserve ce bloc sous un H1 dedie.
    """
    lines = md_text.splitlines(keepends=True)

    if wrap_orphan_intro:
        # Cas specifique Tome 1 : apres la ligne `Actualisation | ...`, avant `# Table des matières`
        start_intro = -1
        for idx, line, in_fence in _iter_lines_with_fence_state(lines):
            if in_fence:
                continue
            if line.startswith("**Livre I"):
                start_intro = idx
                break
        if start_intro != -1:
            return f"# {wrap_orphan_intro}\n\n" + "".join(lines[start_intro:])

    if keep_from_heading:
        pat = re.compile(keep_from_heading)
        for idx, line, in_fence in _iter_lines_with_fence_state(lines):
            if not in_fence and pat.match(line.rstrip("\r\n")):
                return "".join(lines[idx:])
        return md_text

    # Repli generique : conserver a partir du 2e H1 (le 1er etant le titre de couverture),
    # ou du 1er H1 s'il est suivi de contenu normal (sans tableau de metadonnees `Cle | Valeur`).
    h1_indices = [
        idx
        for idx, line, in_fence in _iter_lines_with_fence_state(lines)
        if not in_fence and line.startswith("# ")
    ]
    if len(h1_indices) >= 2:
        first_h1 = lines[h1_indices[0]].strip()
        if not first_h1.startswith(("# Liminaire", "# Partie ", "# Livre ", "# Table des matières")):
            return "".join(lines[h1_indices[1] :])
    return md_text


def strip_static_sections(md_text: str, heading_titles: tuple[str, ...] = ("Table des matières",)) -> str:
    """Supprime les sections H1 statiques (ex. Table des matieres manuelle) jusqu'au prochain H1."""
    if not heading_titles:
        return md_text
    targets = {t.strip().lower() for t in heading_titles}
    lines = md_text.splitlines(keepends=True)
    out: list[str] = []
    skipping = False
    for _, line, in_fence in _iter_lines_with_fence_state(lines):
        if not in_fence and line.startswith("# "):
            title = line[2:].strip().lower()
            if title in targets:
                skipping = True
                continue
            if skipping:
                skipping = False
        if not skipping:
            out.append(line)
    return "".join(out)


def _format_markdown_image_target(rel: str, title_suffix: str = "") -> str:
    """Formate une cible d'image Markdown en l'entourant de `<...>` si elle contient des parentheses."""
    if "(" in rel or ")" in rel:
        return f"<{rel}>{title_suffix}"
    return f"{rel}{title_suffix}"


def normalize_image_paths_for_typst(md_text: str, repo_root: Path, md_source_path: Path | None = None) -> str:
    """Normalise les chemins d'images Markdown en chemins absolus Typst (`/rel/to/repo_root`)."""
    base_dir = md_source_path.parent if md_source_path is not None else repo_root
    img_re = re.compile(
        r"!\[([^\]]*)\]\((<[^>\n]+>(?:\s+(?:\"[^\"]*\"|'[^']*'))?|(?:[^()\n]|\([^()\n]*\))+)\)"
    )

    def _repl(m: re.Match[str]) -> str:
        alt, raw_spec = m.group(1), m.group(2).strip()
        # Gerer une cible entouree de <...> et un eventuel titre optionnel "..."
        title_suffix = ""
        if raw_spec.startswith("<"):
            end_gt = raw_spec.find(">")
            if end_gt != -1:
                raw_target = raw_spec[1:end_gt]
                title_suffix = raw_spec[end_gt + 1 :]
            else:
                raw_target = raw_spec
        else:
            m_title = re.match(r'^(.+?)\s+("[^"]*"|\'[^\']*\')\s*$', raw_spec)
            if m_title:
                raw_target = m_title.group(1).strip()
                title_suffix = " " + m_title.group(2)
            else:
                raw_target = raw_spec

        if raw_target.startswith(("http://", "https://", "data:", "/")):
            return m.group(0)
        resolved = (base_dir / raw_target).resolve()
        try:
            rel = "/" + resolved.relative_to(repo_root.resolve()).as_posix()
            return f"![{alt}]({_format_markdown_image_target(rel, title_suffix)})"
        except ValueError:
            return m.group(0)

    out: list[str] = []
    for _, line, in_fence in _iter_lines_with_fence_state(md_text.splitlines(keepends=True)):
        out.append(line if in_fence else img_re.sub(_repl, line))
    return "".join(out)


def _strip_preceding_figure_placeholder_blockquote(out: list[str]) -> bool:
    """Retire un bloc de citation `> **[Figure]**` contigu en fin de `out` (hors lignes vides finales)."""
    end = len(out)
    while end > 0 and not out[end - 1].strip():
        end -= 1
    if end == 0 or not out[end - 1].lstrip().startswith(">"):
        return False
    start = end
    while start > 0 and out[start - 1].lstrip().startswith(">"):
        start -= 1
    first_line = out[start].lstrip()
    if re.match(r"^>\s*\*\*\[Figure\]\*\*", first_line, re.IGNORECASE):
        del out[start:]
        return True
    return False


def inject_rendered_diagrams(
    md_text: str,
    rendered_dir: Path,
    repo_root: Path,
) -> tuple[str, int]:
    """Injecte les diagrammes rendus (.svg/.png) au-dessus des legendes correspondantes s'ils existent.

    Utile pour les tomes 1-6 une fois leurs sources PlantUML/Mermaid compilees dans `Tomes/<Tome>/Diagrammes/rendus/`.
    Remplace un eventuel encadre de texte aplati `> **[Figure]**` precedant immediatement la legende,
    et ne duplique jamais une image deja presente avant la legende.
    """
    if not rendered_dir.is_dir():
        return md_text, 0

    # Indexer par cle normalisee : ("1.0" ou "1" ou "01") -> Path
    index: dict[str, Path] = {}
    for ext in (".svg", ".png"):
        for fp in sorted(rendered_dir.glob(f"*{ext}")):
            m = re.match(r"^(?:Figure|Fig)[\.-](\d+(?:\.\d+)?)\b", fp.stem, re.IGNORECASE)
            if not m:
                continue
            raw_num = m.group(1)
            norm_num = ".".join(str(int(part)) for part in raw_num.split("."))
            index.setdefault(norm_num, fp)

    if not index:
        return md_text, 0

    cap_re = re.compile(
        r"^\*(?:\*\*)?(?:Figure|Fig\.)\s*(\d+(?:\.\d+)?)\.?(?:\*\*)?(?:\s*\([^)\n]+\))?\s*[—–-]"
    )
    lines = md_text.splitlines(keepends=True)
    out: list[str] = []
    injected = 0
    for idx, line, in_fence in _iter_lines_with_fence_state(lines):
        if not in_fence:
            m = cap_re.match(line.strip())
            if m:
                norm_num = ".".join(str(int(part)) for part in m.group(1).split("."))
                asset = index.get(norm_num)
                if asset is not None:
                    _strip_preceding_figure_placeholder_blockquote(out)
                    prev_nonempty = ""
                    for prev in reversed(out):
                        if prev.strip():
                            prev_nonempty = prev.strip()
                            break
                    if not prev_nonempty.startswith("!["):
                        try:
                            rel = "/" + asset.resolve().relative_to(repo_root.resolve()).as_posix()
                        except ValueError:
                            rel = asset.as_posix()
                        if out and out[-1].strip():
                            out.append("\n")
                        target = _format_markdown_image_target(rel)
                        out.append(f"![Figure {norm_num}]({target})\n\n")
                        injected += 1
        out.append(line)
    return "".join(out), injected


def preprocess_markdown(
    md_text: str,
    repo_root: Path,
    md_source_path: Path | None = None,
    options: dict[str, Any] | None = None,
) -> tuple[str, dict[str, str]]:
    """Pipeline complet de preparation Markdown avant conversion Pandoc -> Typst."""
    opts = options or {}
    body, yaml_meta = extract_yaml_frontmatter(md_text)

    if opts.get("strip_preamble", False):
        body = strip_legacy_preamble(
            body,
            keep_from_heading=opts.get("keep_from_heading"),
            wrap_orphan_intro=opts.get("wrap_orphan_intro"),
        )

    static_to_strip: list[str] = []
    if opts.get("strip_manual_toc", False):
        static_to_strip.append("Table des matières")
    if opts.get("strip_static_lists", False):
        static_to_strip.extend(["Liste des tableaux", "Liste des figures"])
    if static_to_strip:
        body = strip_static_sections(body, tuple(static_to_strip))

    if opts.get("inject_diagrams") and opts.get("rendered_diagrams_dir"):
        rdir = Path(opts["rendered_diagrams_dir"])
        if not rdir.is_absolute():
            rdir = repo_root / rdir
        body, _ = inject_rendered_diagrams(body, rdir, repo_root)

    body = normalize_image_paths_for_typst(body, repo_root, md_source_path=md_source_path)
    return body.strip() + "\n", yaml_meta
