#!/usr/bin/env python3
"""Utilitaires partagés (stdlib uniquement) pour l'outillage du Livre 2027."""

from __future__ import annotations

from datetime import date
import json
import re
from pathlib import Path

DEFAULT_FREEZE_DATE = "2026-12-02"

FRENCH_MONTHS: tuple[str, ...] = (
    "janvier",
    "février",
    "mars",
    "avril",
    "mai",
    "juin",
    "juillet",
    "août",
    "septembre",
    "octobre",
    "novembre",
    "décembre",
)

_FRENCH_MONTH_REGEX_PARTS: tuple[str, ...] = (
    "janvier",
    r"f[eé]vrier",
    "mars",
    "avril",
    "mai",
    "juin",
    "juillet",
    r"ao[uû]t",
    "septembre",
    "octobre",
    "novembre",
    r"d[eé]cembre",
)

_ISO_DATE_RE = re.compile(r"^(\d{4})-(\d{2})-(\d{2})$")

# Abréviations françaises courantes terminées par un point à protéger avant découpage en phrases.
ABBREV_DOT_RE = re.compile(
    r"\b(?:et\s+al|art|al|par|chap|ch|fig|vol|no|p\.\s*ex|c\.-à-d|M\.Sc|dr|prof|env|cf|"
    r"janv|févr|avr|juill|sept|oct|nov|déc|ibid|coll|dir|éd|pp|p|M|c)\.",
    re.IGNORECASE,
)

# Séparateur de ligne de tableau Markdown (ligne d'alignement : | --- | :---: |)
TABLE_SEP_RE = re.compile(r"^\|[\s:|\-]+\|$")

_CODE_SEGMENT_RE = re.compile(
    r"(```[\s\S]*?```|~~~[\s\S]*?~~~|(?<!`)(`+)(?!`)(?:(?!(?<!`)\2(?!`)).)+?\2(?!`))",
    re.DOTALL,
)
_UNESCAPED_DOLLAR_RE = re.compile(r"(?<!\\)((?:\\\\)*)\$")


def parse_iso_date(date_str: str) -> tuple[int, int, int] | None:
    """Analyse une date YYYY-MM-DD valide (calendrier réel) ou retourne None."""
    m = _ISO_DATE_RE.match((date_str or "").strip())
    if not m:
        return None
    try:
        parsed = date.fromisoformat(m.group(0))
    except ValueError:
        return None
    return parsed.year, parsed.month, parsed.day


def format_french_date(iso_date: str) -> str:
    """Convertit une date ISO YYYY-MM-DD en libellé français (ex. '2 décembre 2026')."""
    parsed = parse_iso_date(iso_date)
    if parsed is None:
        return iso_date
    year, month, day = parsed
    day_str = "1er" if day == 1 else str(day)
    return f"{day_str} {FRENCH_MONTHS[month - 1]} {year}"


def french_date_regex(iso_date: str) -> re.Pattern[str]:
    """Construit une regex tolérant accents/espaces pour la forme française de iso_date."""
    parsed = parse_iso_date(iso_date)
    if parsed is None:
        return re.compile(re.escape(iso_date), re.IGNORECASE)
    year, month, day = parsed
    day_pat = r"1(?:er)?" if day == 1 else str(day)
    month_pat = _FRENCH_MONTH_REGEX_PARTS[month - 1]
    return re.compile(rf"\b{day_pat}\s+{month_pat}\s+{year}\b", re.IGNORECASE)


def get_freeze_date(
    book_dir: Path | None = None,
    mlr_data: dict | None = None,
) -> str:
    """Lit dynamiquement freeze_date depuis specs/protocole-mlr-2027.json (avec repli sûr)."""
    data = mlr_data
    if data is None and book_dir is not None:
        mlr_path = Path(book_dir) / "specs" / "protocole-mlr-2027.json"
        if mlr_path.exists():
            try:
                loaded = json.loads(mlr_path.read_text(encoding="utf-8"))
                if isinstance(loaded, dict):
                    data = loaded
            except (OSError, ValueError):
                data = None

    if isinstance(data, dict):
        raw = data.get("freeze_date")
        if isinstance(raw, str) and parse_iso_date(raw) is not None:
            return raw.strip()
        tw = data.get("time_window")
        if isinstance(tw, dict):
            primary = str(tw.get("primary", ""))
            tail = primary.split("/")[-1].strip()
            if parse_iso_date(tail) is not None:
                return tail

    return DEFAULT_FREEZE_DATE


def normalize_quotes_spaces(text: str) -> str:
    """Normalise apostrophes typographiques et espaces insécables pour la détection."""
    return (
        text.replace("’", "'")
        .replace("‘", "'")
        .replace("\u00a0", " ")
        .replace("\u202f", " ")
    )


def compile_forbidden_patterns(
    raw_patterns: list[str] | tuple[str, ...],
) -> list[tuple[str, re.Pattern[str]]]:
    """Compile les motifs interdits avec normalisation apostrophes/espaces et IGNORECASE."""
    compiled: list[tuple[str, re.Pattern[str]]] = []
    for raw in raw_patterns:
        norm = normalize_quotes_spaces(raw)
        compiled.append((raw, re.compile(norm, re.IGNORECASE)))
    return compiled


def match_forbidden_patterns(
    text: str,
    compiled_patterns: list[tuple[str, re.Pattern[str]]],
) -> list[str]:
    """Retourne les motifs d'origine correspondant au texte normalisé."""
    norm_text = normalize_quotes_spaces(text)
    return [raw for raw, pat in compiled_patterns if pat.search(norm_text)]


def escape_dollars(text: str) -> str:
    """Échappe tout symbole $ nu en \\$ hors blocs/spans de code inline sans casser \\\\$."""
    out: list[str] = []
    pos = 0
    for m in _CODE_SEGMENT_RE.finditer(text):
        if m.start() > pos:
            chunk = text[pos : m.start()]
            out.append(_UNESCAPED_DOLLAR_RE.sub(lambda dm: dm.group(1) + r"\$", chunk))
        out.append(m.group(0))
        pos = m.end()
    if pos < len(text):
        chunk = text[pos:]
        out.append(_UNESCAPED_DOLLAR_RE.sub(lambda dm: dm.group(1) + r"\$", chunk))
    return "".join(out)


def split_sentences(text: str) -> list[str]:
    """Découpe un texte français en phrases en protégeant abréviations courantes et cotes."""
    protected = ABBREV_DOT_RE.sub(lambda m: m.group(0).replace(".", "\u2024"), text)
    # Protège également les abréviations 'n°' / 'Dr' suivies sans point éventuel ou 'p. ex.'
    raw_parts = re.split(
        r"(?<=[.!?])\s+(?=[A-ZÀÂÄÉÈÊËÎÏÔÖÙÛÜÇ«\"“\(0-9*`])",
        protected,
    )
    return [part.replace("\u2024", ".").strip() for part in raw_parts if part.strip()]


def is_markdown_table_block(block: str) -> bool:
    """Indique si un bloc Markdown correspond à un tableau (ou contient un séparateur de tableau)."""
    lines = [ln.strip() for ln in block.splitlines() if ln.strip()]
    if len(lines) < 2:
        return False
    # Vérifie en priorité la ligne séparatrice sur la 2e ligne non vide, ou toute ligne séparatrice
    if TABLE_SEP_RE.match(lines[1]):
        return True
    return any(TABLE_SEP_RE.match(ln) for ln in lines)
