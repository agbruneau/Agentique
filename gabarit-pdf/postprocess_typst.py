# SPDX-License-Identifier: MIT
"""Post-traitement typographique Typst partage pour toute la collection Agentique.

Extrait et generalise a partir du pipeline de reference de 8 - Manuel afin d'assurer
un rendu fr-CA uniforme (tableaux reequilibres, virgules decimales en math, legendes
centrees, cesure d'URLs et de code inline, espaces insecables) pour les 8 volumes.
"""

from __future__ import annotations

import re
from typing import Callable

# Largeur utile Typst : page 6.14in - marges (0.90in + 0.78in) = 4.46in * 72 pt/in = 321.12 pt
USABLE_PAGE_WIDTH_PT = (6.14 - 0.90 - 0.78) * 72.0

_FENCE_OPEN_RE = re.compile(r"^[ \t]*(`{3,}|~{3,})")


def escape_typst_content(text: str) -> str:
    """Echappe une chaine pour injection dans un bloc de contenu Typst `[...]`."""
    return (
        text.replace("\\", "\\\\")
        .replace("#", "\\#")
        .replace("$", "\\$")
        .replace("[", "\\[")
        .replace("]", "\\]")
    )


def escape_typst_string(text: str) -> str:
    """Echappe une chaine pour injection dans une litterale Typst `"..."`."""
    return text.replace("\\", "\\\\").replace('"', '\\"')


def _count_backtick_run(text: str, idx: int) -> int:
    n = len(text)
    end = idx
    while end < n and text[end] == "`":
        end += 1
    return end - idx


def _transform_inline_backticks(
    text: str,
    transform: Callable[[str], str],
    respect_escapes: bool = True,
) -> str:
    """Applique `transform` au contenu des spans inline `...` hors blocs clotures."""
    out_lines: list[str] = []
    fence_char: str | None = None
    fence_len = 0
    for ln in text.splitlines(keepends=True):
        raw_ln = ln.rstrip("\r\n")
        if fence_char is None:
            m_fence = _FENCE_OPEN_RE.match(raw_ln)
            if m_fence:
                fence_char = m_fence.group(1)[0]
                fence_len = len(m_fence.group(1))
                out_lines.append(ln)
                continue
            ending = ln[len(raw_ln) :]
            buf: list[str] = []
            i = 0
            n = len(raw_ln)
            while i < n:
                if respect_escapes and raw_ln[i] == "\\" and i + 1 < n:
                    buf.append(raw_ln[i : i + 2])
                    i += 2
                    continue
                if raw_ln[i] == "`":
                    run = _count_backtick_run(raw_ln, i)
                    ticks = "`" * run
                    j = i + run
                    found = -1
                    while j < n:
                        if raw_ln[j] == "`":
                            close_run = _count_backtick_run(raw_ln, j)
                            if close_run == run:
                                found = j
                                break
                            j += close_run
                            continue
                        j += 1
                    if found != -1:
                        inner = raw_ln[i + run : found]
                        buf.append(ticks + transform(inner) + ticks)
                        i = found + run
                        continue
                    buf.append(ticks)
                    i += run
                    continue
                buf.append(raw_ln[i])
                i += 1
            out_lines.append("".join(buf) + ending)
        else:
            out_lines.append(ln)
            stripped = raw_ln.strip()
            if stripped.startswith(fence_char * fence_len) and stripped == fence_char * len(stripped):
                fence_char = None
                fence_len = 0
    return "".join(out_lines)


def _strip_typst_markup(cell: str) -> str:
    s = re.sub(r"#(?:strong|emph|link\([^)]*\)|text\([^)]*\))\[", "", cell)
    s = s.replace("[", "").replace("]", "").replace("`", "")
    s = re.sub(r"\\([\[\]$#_])", r"\1", s)
    return " ".join(s.split())


def _apply_cell_prose_nbsp(text: str) -> str:
    text = re.sub(r"(?i)\b([cdjlmnst]['’])(?=[A-Za-zÀ-ÖØ-öø-ÿ]{9,})", lambda m: m.group(1) + "\u200b", text)
    text = re.sub(r"(\d)\s+%", lambda m: m.group(1) + "\u00a0%", text)
    text = re.sub(r"(\d)\s+\\\$", lambda m: m.group(1) + "\u00a0\\$", text)
    text = re.sub(r"(\\\$)\s+(CA|US)\b", lambda m: m.group(1) + "\u00a0" + m.group(2), text)
    text = re.sub(r"(?<=\d) (?=\d{3}\b)", "\u00a0", text)
    text = re.sub(r"(\d)\s+(s|ms|min|h|o|Kio|Mio|po|pt)\b", lambda m: m.group(1) + "\u00a0" + m.group(2), text)
    text = re.sub(r"(?<!-) -> (?!-)", " → ", text)
    return text


def _wrap_url_display(url: str) -> str:
    if "://" in url:
        scheme, rest = url.split("://", 1)
        rest = rest.replace("/", "/\u200b").replace("-", "-\u200b")
        rest = re.sub(r"(?<!\.)\.(?=[A-Za-z0-9])", ".\u200b", rest)
        return scheme + "://" + rest
    res = url.replace("/", "/\u200b").replace("-", "-\u200b")
    return re.sub(r"(?<!\.)\.(?=[A-Za-z0-9])", ".\u200b", res)


def _format_typst_link_safe(m: re.Match[str]) -> str:
    url = m.group(1)
    label = m.group(2)
    if label is None:
        disp = _wrap_url_display(url)
    elif label.startswith(("http://", "https://")):
        disp = _wrap_url_display(label.replace("\u200b", ""))
    else:
        return f'#link("{url}")[{label}]'
    escaped = escape_typst_string(disp)
    return f'#link("{url}")[#text(hyphenate: false)[#("{escaped}")]]'


def _break_long_tokens_in_cell(cell: str) -> str:
    def _wrap_raw_inner(inner: str) -> str:
        inner = inner.replace(r"\$", "$")
        inner = re.sub(r"(\d)\s+%", lambda x: x.group(1) + "\u00a0%", inner)
        inner = inner.replace("->", "-\u2060>")
        inner = inner.replace("-*", "-\u2060*")
        inner = re.sub(
            r"(?<![A-Za-z0-9])(--?)(?=[A-Za-z0-9*])",
            lambda x: "".join(c + "\u2060" for c in x.group(1)),
            inner,
        )
        if "://" in inner:
            return f"`{_wrap_url_display(inner)}`"

        def _chunk_cell(m2: re.Match[str]) -> str:
            tok = m2.group(0)
            return "\u200b".join(tok[k : k + 12] for k in range(0, len(tok), 12))

        def _wrap_part(part: str) -> str:
            if "\u200b" in part:
                return part
            part = re.sub(
                r"(::|[_/:,=(]|(?<!\d)\.|(?<=\d)\.(?=[A-Za-z_]))(?=[A-Za-z0-9_{\"'])",
                lambda x: x.group(1) + "\u200b",
                part,
            )
            if len(part) >= 12:
                part = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", "\u200b", part)
            return re.sub(r"[A-Za-zÀ-ÖØ-öø-ÿ0-9]{16,}", _chunk_cell, part)

        wrapped = re.sub(r"\S+", lambda mm: _wrap_part(mm.group(0)), inner)
        return f"`{wrapped}`"

    protected_re = re.compile(r'((?<!`)`[^`\n]+`(?!`)|#link\("[^"]+"\)(?:\[[^\]]*\])?)')
    parts: list[str] = []
    pos = 0
    for m in protected_re.finditer(cell):
        if m.start() > pos:
            parts.append(_apply_cell_prose_nbsp(cell[pos : m.start()]))
        tok = m.group(0)
        if tok.startswith("`"):
            parts.append(_wrap_raw_inner(tok[1:-1]))
        else:
            parts.append(tok)
        pos = m.end()
    if pos < len(cell):
        parts.append(_apply_cell_prose_nbsp(cell[pos:]))
    return "".join(parts)


def _normalize_typst_math_commas(typst_src: str) -> str:
    """Convertit les virgules decimales (, ou \\,) en ',' typographique dans les blocs $...$."""
    out: list[str] = []
    pos = 0
    n = len(typst_src)
    raw_ticks = 0
    in_math = False
    in_math_str = False
    math_start = 0

    def _fix_math_inner(inner: str) -> str:
        parts: list[str] = []
        p = 0
        for sm in re.finditer(r'"(?:[^"\\]|\\.)*"', inner):
            parts.append(re.sub(r"(\d)(?:\\,|,)(?=\d)", r'\1","', inner[p : sm.start()]))
            parts.append(sm.group(0))
            p = sm.end()
        parts.append(re.sub(r"(\d)(?:\\,|,)(?=\d)", r'\1","', inner[p:]))
        return "".join(parts)

    while pos < n:
        ch = typst_src[pos]
        if raw_ticks > 0:
            if ch == "`":
                run = _count_backtick_run(typst_src, pos)
                out.append("`" * run)
                if run == raw_ticks:
                    raw_ticks = 0
                pos += run
            else:
                out.append(ch)
                pos += 1
            continue

        if in_math:
            if in_math_str:
                if ch == "\\" and pos + 1 < n:
                    pos += 2
                    continue
                if ch == '"':
                    in_math_str = False
                pos += 1
                continue
            if ch == "\\" and pos + 1 < n:
                pos += 2
                continue
            if ch == '"':
                in_math_str = True
                pos += 1
                continue
            if ch == "$":
                inner = typst_src[math_start:pos]
                out.append("$" + _fix_math_inner(inner) + "$")
                in_math = False
                pos += 1
                continue
            pos += 1
            continue

        if ch == "\\" and pos + 1 < n:
            out.append(typst_src[pos : pos + 2])
            pos += 2
            continue
        if ch == "`":
            run = _count_backtick_run(typst_src, pos)
            out.append("`" * run)
            raw_ticks = run
            pos += run
            continue
        if ch == "$":
            in_math = True
            in_math_str = False
            math_start = pos + 1
            pos += 1
            continue
        out.append(ch)
        pos += 1

    if in_math:
        out.append("$" + typst_src[math_start:])
    return "".join(out)


def _split_top_level_args(body: str) -> list[str]:
    args: list[str] = []
    cur: list[str] = []
    paren_stack = [0]
    in_str = False
    raw_ticks = 0
    i = 0
    n = len(body)
    while i < n:
        ch = body[i]
        if in_str:
            cur.append(ch)
            if ch == "\\" and i + 1 < n:
                cur.append(body[i + 1])
                i += 2
                continue
            if ch == '"':
                in_str = False
            i += 1
            continue
        if raw_ticks > 0:
            if ch == "`":
                run = _count_backtick_run(body, i)
                cur.append("`" * run)
                if run == raw_ticks:
                    raw_ticks = 0
                i += run
            else:
                cur.append(ch)
                i += 1
            continue
        if ch == "\\":
            cur.append(ch)
            if i + 1 < n:
                cur.append(body[i + 1])
                i += 2
                continue
        elif ch == '"':
            in_str = True
        elif ch == "`":
            run = _count_backtick_run(body, i)
            cur.append("`" * run)
            raw_ticks = run
            i += run
            continue
        elif ch == "[":
            paren_stack.append(0)
        elif ch == "]":
            if len(paren_stack) > 1:
                paren_stack.pop()
        elif ch == "(":
            paren_stack[-1] += 1
        elif ch == ")":
            paren_stack[-1] = max(0, paren_stack[-1] - 1)
        elif ch == "," and len(paren_stack) == 1 and paren_stack[0] == 0:
            args.append("".join(cur))
            cur = []
            i += 1
            continue
        cur.append(ch)
        i += 1
    if "".join(cur).strip():
        args.append("".join(cur))
    return args


def _rebalance_single_table(table_inner: str) -> str:
    args = _split_top_level_args(table_inner)
    col_idx = -1
    ncols = 0
    for idx, arg in enumerate(args):
        m = re.match(r"^\s*columns:\s*(?:\(([^)]+)\)|(\d+))\s*$", arg, re.DOTALL)
        if m:
            col_idx = idx
            if m.group(1) is not None:
                ncols = len([x for x in m.group(1).split(",") if x.strip()])
            else:
                ncols = int(m.group(2))
            break
    if col_idx < 0 or ncols <= 1:
        return table_inner

    cell_texts: list[str] = []
    new_args: list[str] = []
    for arg in args:
        st = arg.strip()
        if st.startswith("table.header(") and st.endswith(")"):
            h_inner = st[len("table.header(") : -1]
            h_args = _split_top_level_args(h_inner)
            fixed_h = []
            for h in h_args:
                hs = h.strip()
                if hs.startswith("[") and hs.endswith("]"):
                    hs = _break_long_tokens_in_cell(hs)
                    cell_texts.append(_strip_typst_markup(hs).replace("\u200b", " ").replace("\u2060", ""))
                fixed_h.append(hs)
            new_args.append("\n    table.header(" + ", ".join(fixed_h) + ",)")
        elif re.match(r"^align:\s*\(", st):
            new_args.append(re.sub(r"\bauto\b", "left", arg))
        elif st.startswith("[") and st.endswith("]"):
            broken = _break_long_tokens_in_cell(st)
            cell_texts.append(_strip_typst_markup(broken).replace("\u200b", " ").replace("\u2060", ""))
            new_args.append(arg.replace(st, broken, 1))
        else:
            new_args.append(arg)

    if len(cell_texts) < ncols:
        return table_inner

    col_scores: list[float] = []
    min_shares: list[float] = []
    for c in range(ncols):
        vals = [cell_texts[i] for i in range(c, len(cell_texts), ncols)]
        lens = sorted(len(v) for v in vals)
        med = lens[len(lens) // 2]
        p90 = lens[min(len(lens) - 1, int(0.9 * len(lens)))]
        hdr_len = len(vals[0]) if vals else 4
        max_word = max((max((len(w) for w in v.split()), default=0) for v in vals), default=0)
        hdr_max_word = max((len(w) for w in vals[0].split()), default=0) if vals else 0
        min_floor = max(0.045, 0.55 / ncols) if ncols >= 8 else 0.085
        if med < 15:
            eff_word = min(max(max_word, hdr_max_word), 12)
            req_floor = max(min_floor, (eff_word * 3.8 + 8.0) / USABLE_PAGE_WIDTH_PT)
        else:
            eff_word = min(max(max_word, hdr_max_word), 16)
            cap = max(24.0, 220.0 / ncols) if ncols >= 8 else (47.0 if ncols >= 6 else 72.0)
            req_floor = max(
                min_floor,
                min(cap / USABLE_PAGE_WIDTH_PT, (eff_word * 3.7 + 7.5) / USABLE_PAGE_WIDTH_PT),
            )
        min_shares.append(req_floor)
        score = max(
            float(hdr_len) * 1.15,
            0.55 * max(med, 5) + 0.45 * min(p90, 95),
            min(eff_word, 16) * 1.4,
        )
        col_scores.append(max(score, 8.0))

    floor_sum = sum(min_shares)
    max_floor_sum = 0.82 if ncols >= 8 else (0.94 if ncols >= 6 else 0.88)
    if floor_sum > max_floor_sum:
        scale_f = max_floor_sum / floor_sum
        min_shares = [s * scale_f for s in min_shares]
        floor_sum = sum(min_shares)

    remaining = max(0.0, 1.0 - floor_sum)
    total_score = sum(col_scores) or 1.0
    shares = [min_shares[c] + remaining * (col_scores[c] / total_score) for c in range(ncols)]
    sh_sum = sum(shares)
    pcts = [round(100.0 * s / sh_sum, 2) for s in shares]
    pcts[-1] = round(100.0 - sum(pcts[:-1]), 2)
    col_spec = ", ".join(f"{p:.2f}%" for p in pcts)

    if ncols >= 9:
        new_args[col_idx] = f"\n    columns: ({col_spec}),\n    inset: (x: 1.5pt, y: 2.5pt)"
    elif ncols == 8:
        new_args[col_idx] = f"\n    columns: ({col_spec}),\n    inset: (x: 2.0pt, y: 2.8pt)"
    else:
        new_args[col_idx] = f"\n    columns: ({col_spec})"
    return ",".join(new_args) + ("," if not table_inner.rstrip().endswith(",") else "")


def _wrap_inline_raw_tokens_typst(inner: str) -> str:
    """Deseschappe \\$ et ajoute des points de cesure discrets (\\u200b) dans le code inline hors tableaux."""
    fixed = inner.replace(r"\$", "$")
    fixed = re.sub(r"(\d)\s+%", lambda x: x.group(1) + "\u00a0%", fixed)
    fixed = re.sub(
        r"\b([1-8])\s+-\s+(Compendium|Cadre|Plan|Memoire|Mémoire|Livre|Manuel)\b",
        lambda m: f"{m.group(1)}\u00a0-\u00a0{m.group(2)}",
        fixed,
    )
    fixed = fixed.replace("->", "-\u2060>")
    fixed = fixed.replace("-*", "-\u2060*")
    fixed = re.sub(
        r"(?<![A-Za-z0-9])(--?)(?=[A-Za-z0-9*])",
        lambda x: "".join(c + "\u2060" for c in x.group(1)),
        fixed,
    )
    if "://" in fixed or "\u200b" in fixed:
        return fixed

    def _chunk_long_run(m: re.Match[str]) -> str:
        tok = m.group(0)
        if len(tok) < 32:
            return tok
        return "\u200b".join(tok[k : k + 16] for k in range(0, len(tok), 16))

    def _wrap_part(part: str) -> str:
        if len(part) < 16:
            return part
        part = re.sub(
            r"(::|[_/,=]|(?<!\d)\.|(?<=\d)\.(?=[A-Za-z_]))(?=[A-Za-z0-9_{\"'])",
            lambda x: x.group(1) + "\u200b",
            part,
        )
        if len(part) >= 26:
            part = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", "\u200b", part)
        return re.sub(r"[A-Za-zÀ-ÖØ-öø-ÿ0-9]{32,}", _chunk_long_run, part)

    return re.sub(r"\S+", lambda m: _wrap_part(m.group(0)), fixed)


def _wrap_long_tokens_in_fenced_raw(typst_src: str, max_token_len: int = 78, chunk_len: int = 64) -> str:
    """Insere des points de cesure discrets (\\u200b) dans les jetons continus longs des blocs ```."""
    out_lines: list[str] = []
    fence_char: str | None = None
    fence_len = 0

    def _break_token(m: re.Match[str]) -> str:
        tok = m.group(0)
        if len(tok) <= max_token_len or "\u200b" in tok:
            return tok
        # 1. Points de cesure naturels apres separateurs courants (URL, query string, JSON, chemins)
        broken = re.sub(r"([&=,;:/.?_-])(?=\S)", lambda x: x.group(1) + "\u200b", tok)
        # 2. Couper tout segment residuel sans separateur (ex. JWT base64, empreinte SHA-256)
        segments = broken.split("\u200b")
        final_segs: list[str] = []
        for seg in segments:
            if len(seg) > chunk_len:
                final_segs.extend(seg[k : k + chunk_len] for k in range(0, len(seg), chunk_len))
            else:
                final_segs.append(seg)
        return "\u200b".join(final_segs)

    for ln in typst_src.splitlines(keepends=True):
        raw_ln = ln.rstrip("\r\n")
        if fence_char is None:
            m_fence = _FENCE_OPEN_RE.match(raw_ln)
            if m_fence:
                fence_char = m_fence.group(1)[0]
                fence_len = len(m_fence.group(1))
            out_lines.append(ln)
        else:
            stripped = raw_ln.strip()
            if stripped.startswith(fence_char * fence_len) and stripped == fence_char * len(stripped):
                fence_char = None
                fence_len = 0
                out_lines.append(ln)
            else:
                ending = ln[len(raw_ln) :]
                out_lines.append(re.sub(r"\S+", _break_token, raw_ln) + ending)
    return "".join(out_lines)


def _postprocess_inline_raw_typst(typst_src: str) -> str:
    """Traite le code inline hors blocs clotures sans alterer les blocs ``` ni la prose."""
    return _transform_inline_backticks(typst_src, _wrap_inline_raw_tokens_typst, respect_escapes=True)


def _apply_prose_nbsp_segment(seg: str) -> str:
    seg = re.sub(r"(\d)\s+%", lambda m: m.group(1) + "\u00a0%", seg)
    seg = re.sub(r"(\d)\s+\\\$", lambda m: m.group(1) + "\u00a0\\$", seg)
    seg = re.sub(r"(\\\$)\s+(CA|US)\b", lambda m: m.group(1) + "\u00a0" + m.group(2), seg)
    seg = re.sub(r"(?<=\d) (?=\d{3}\b)", "\u00a0", seg)
    seg = re.sub(r"(\d)\s+(s|ms|min|h|o|Kio|Mio|po|pt)\b", lambda m: m.group(1) + "\u00a0" + m.group(2), seg)
    seg = re.sub(r"(§{1,2})\s+(?=\d)", lambda m: m.group(1) + "\u00a0", seg)
    seg = re.sub(r"([−–])\s+(?=\d)", lambda m: m.group(1) + "\u00a0", seg)
    seg = re.sub(
        r"\b([1-8])\s+-\s+(Compendium|Cadre|Plan|Memoire|Mémoire|Livre|Manuel)\b",
        lambda m: f"{m.group(1)}\u00a0-\u00a0{m.group(2)}",
        seg,
    )
    seg = re.sub(r"(?<!-) -> (?!-)", " → ", seg)
    return seg


def _protect_typst_prose_line(line: str) -> str:
    """Applique les espaces insecables et -> en prose hors spans `...`, math $...$ et appels #link/image/#(...)."""
    if line.lstrip().startswith(("#set ", "#show ", "#page", "#let ", "#import ", "#figure(", "#block(", "#align(")):
        return line
    protected_re = re.compile(
        r'(`[^`\n]+`|(?<!\\)\$(?:\\.|[^$\n\\])+\$|#?link\("[^"]+"\)|#?image\("[^"]+"|#\("(?:[^"\\]|\\.)*"\))'
    )
    parts: list[str] = []
    pos = 0
    for m in protected_re.finditer(line):
        if m.start() > pos:
            parts.append(_apply_prose_nbsp_segment(line[pos : m.start()]))
        parts.append(m.group(0))
        pos = m.end()
    if pos < len(line):
        parts.append(_apply_prose_nbsp_segment(line[pos:]))
    return "".join(parts)


def _bind_small_tables_to_captions(typst_src: str) -> str:
    """Enveloppe chaque petit tableau (<= 16 cellules) avec sa legende Tableau dans un bloc indivisible."""
    out: list[str] = []
    pos = 0
    n = len(typst_src)
    marker = "#figure("
    cap_re = re.compile(
        r"^\s*\n\s*\n(#align\(center\)\[#set par\(justify: false\); #set text\(size: 8\.6pt, fill: rgb\(\"#475569\"\)\); #emph\[(?:#strong\[)?Tableau\s+\d+(?:\.\d+)?(?:\])?\b[^\n]*\]\])"
    )
    while pos < n:
        hit = typst_src.find(marker, pos)
        if hit == -1:
            out.append(typst_src[pos:])
            break
        out.append(typst_src[pos:hit])
        i = hit + len(marker)
        paren_depth = 1
        in_str = False
        raw_ticks = 0
        while i < n and paren_depth > 0:
            ch = typst_src[i]
            if in_str:
                if ch == "\\" and i + 1 < n:
                    i += 2
                    continue
                if ch == '"':
                    in_str = False
            elif raw_ticks > 0:
                if ch == "`":
                    run = _count_backtick_run(typst_src, i)
                    if run == raw_ticks:
                        raw_ticks = 0
                    i += run
                    continue
            else:
                if ch == "\\":
                    i += 2
                    continue
                elif ch == '"':
                    in_str = True
                elif ch == "`":
                    run = _count_backtick_run(typst_src, i)
                    raw_ticks = run
                    i += run
                    continue
                elif ch == "(":
                    paren_depth += 1
                elif ch == ")":
                    paren_depth -= 1
            i += 1
        fig_block = typst_src[hit:i]
        is_small_table = ", kind: table" in fig_block and fig_block.count("\n    [") <= 16
        m_cap = cap_re.match(typst_src[i:]) if is_small_table else None
        if m_cap and (typst_src[hit : hit + 6] == "#figur"):
            end_cap = i + m_cap.end()
            out.append(
                "\n#block(width: 100%, breakable: false)[\n"
                + fig_block
                + "\n\n"
                + m_cap.group(1)
                + "\n]\n"
            )
            pos = end_cap
        else:
            out.append(fig_block)
            pos = i
    return "".join(out)


def _apply_outside_fences(typst_src: str, line_fn: Callable[[str], str]) -> str:
    out_lines: list[str] = []
    fence_char: str | None = None
    fence_len = 0
    for ln in typst_src.splitlines(keepends=True):
        raw_ln = ln.rstrip("\r\n")
        if fence_char is None:
            m_fence = _FENCE_OPEN_RE.match(raw_ln)
            if m_fence:
                fence_char = m_fence.group(1)[0]
                fence_len = len(m_fence.group(1))
                out_lines.append(ln)
            else:
                ending = ln[len(raw_ln) :]
                out_lines.append(line_fn(raw_ln) + ending)
        else:
            out_lines.append(ln)
            stripped = raw_ln.strip()
            if stripped.startswith(fence_char * fence_len) and stripped == fence_char * len(stripped):
                fence_char = None
                fence_len = 0
    return "".join(out_lines)


def _wrap_unjustified_section(typst_src: str, start_pattern: str, stop_pattern: str) -> str:
    m_start = re.search(start_pattern, typst_src, re.MULTILINE)
    if not m_start:
        return typst_src
    s_idx = m_start.end()
    after = typst_src[s_idx:]
    m_stop = re.search(stop_pattern, after, re.MULTILINE)
    if m_stop:
        body = after[: m_stop.start()]
        rest = "\n" + after[m_stop.start() :].lstrip("\n")
    else:
        body = after
        rest = ""
    return (
        typst_src[:s_idx]
        + "\n\n#block(width: 100%, breakable: true)[\n#set par(justify: false, leading: 0.56em, spacing: 0.45em)\n"
        + body.strip()
        + "\n]\n"
        + rest
    )


def postprocess_typst_body(typst_src: str) -> str:
    """Post-traite un corps Typst issu de Pandoc selon la charte fr-CA de la collection."""
    normalized = _normalize_typst_math_commas(typst_src)
    out: list[str] = []
    pos = 0
    marker = "#table("
    n = len(normalized)
    while pos < n:
        hit = normalized.find(marker, pos)
        if hit == -1:
            out.append(normalized[pos:])
            break
        out.append(normalized[pos:hit])
        i = hit + len(marker)
        paren_stack = [1]
        in_str = False
        raw_ticks = 0
        while i < n and paren_stack[0] > 0:
            ch = normalized[i]
            if in_str:
                if ch == "\\":
                    i += 2
                    continue
                if ch == '"':
                    in_str = False
            elif raw_ticks > 0:
                if ch == "`":
                    run = _count_backtick_run(normalized, i)
                    if run == raw_ticks:
                        raw_ticks = 0
                    i += run
                    continue
            else:
                if ch == "\\":
                    i += 2
                    continue
                elif ch == '"':
                    in_str = True
                elif ch == "`":
                    run = _count_backtick_run(normalized, i)
                    raw_ticks = run
                    i += run
                    continue
                elif ch == "[":
                    paren_stack.append(0)
                elif ch == "]":
                    if len(paren_stack) > 1:
                        paren_stack.pop()
                elif ch == "(":
                    paren_stack[-1] += 1
                elif ch == ")":
                    if len(paren_stack) > 1:
                        paren_stack[-1] = max(0, paren_stack[-1] - 1)
                    else:
                        paren_stack[0] -= 1
            i += 1
        if paren_stack[0] == 0:
            inner = normalized[hit + len(marker) : i - 1]
            out.append("#table(" + _rebalance_single_table(inner) + ")")
            pos = i
        else:
            out.append(marker)
            pos = hit + len(marker)

    res = "".join(out)

    # Retirer un separateur horizontal immediatement avant un titre
    res = re.sub(r"(?m)^#divider\(\)\s*\n+(?=={1,6}\s+)", "", res)

    # Centrer les legendes numerotees (Figure N / Figure N.M / (anc. Figure ...) / Fig. N. / Tableau X / Tableau X.Y)
    res = re.sub(
        r"(?ms)^(#emph\[(?:#strong\[)?(?:Figure\s+\d+(?:\.\d+)?|Fig\.\s*\d+(?:\.\d+)?\.?|Tableau\s+\d+(?:\.\d+)?)(?:\])?(?:\s*\([^)\n]+\))?\s*[—–-][^\n]+(?:\n(?!\s*\n)[^\n]+)*\])(?=\s*(?:\n\s*\n|\Z))",
        r'#align(center)[#set par(justify: false); #set text(size: 8.6pt, fill: rgb("#475569")); \1]',
        res,
    )

    # Lier chaque petit tableau (<= 16 cellules) a sa legende Tableau
    res = _bind_small_tables_to_captions(res)

    # Securiser tous les #link HTTP/HTTPS contre l'autolinker Typst et autoriser la cesure des URLs
    def _fix_line_urls(line: str) -> str:
        line = re.sub(r'#link\("(https?://[^"]+)"\)(?:\[([^\]]+)\])?', _format_typst_link_safe, line)
        return re.sub(r"`(https?://[^`\n]+)`", lambda m: "`" + _wrap_url_display(m.group(1)) + "`", line)

    res = _apply_outside_fences(res, _fix_line_urls)

    # Desactiver la justification excessive dans les sections bibliographiques, references et matrices denses
    stop_major = r"^={1,2}\s+(?:Annexe\s+|Annexes\b|Chapitre\s+|Partie\s+|Livre\s+|[A-Z]\s+[A-ZÀ-ÖØ-Þ])"
    for sec_pat in (
        r"^=+\s+(?:Annexe\s+[A-Z0-9]+\s*[—–-]\s*)?Bibliographie\b[^\n]*(?:\n<[^>\n]+>)?",
        r"^=+\s+(?:Annexe\s+[A-Z0-9]+\s*[—–-]\s*|[A-Z]\s+)Références\b[^\n]*(?:\n<[^>\n]+>)?",
        r"^=+\s+Matrice détaillée\b[^\n]*(?:\n<[^>\n]+>)?",
    ):
        res = _wrap_unjustified_section(res, sec_pat, stop_major)

    res = _apply_outside_fences(res, _protect_typst_prose_line)
    res = _wrap_long_tokens_in_fenced_raw(res)
    return _postprocess_inline_raw_typst(res)
