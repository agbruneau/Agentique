#!/usr/bin/env python3
"""Barriere deterministe G1 du Livre 2027 (verifie_manuscrit.py).

Controle CA-01..CA-11, CA-17 et la presence/coherence des livrables G2..G5.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import unicodedata
from dataclasses import dataclass
from pathlib import Path

_YAML_FM_RE = re.compile(r"\A\ufeff?---\r?\n.*?\r?\n(?:---|\.\.\.)(?:\r?\n|\Z)", re.DOTALL)
_BIBLIO_BLOCK_RE = re.compile(
    r"<!--\s*BIBLIOGRAPHIE_BRUTE_DEBUT\s*-->.*?<!--\s*BIBLIOGRAPHIE_BRUTE_FIN\s*-->",
    re.DOTALL,
)
_HTML_COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)
_FENCE_OPEN_RE = re.compile(r"^\s*(`{3,}|~{3,})")
_INLINE_CODE_RE = re.compile(r"`[^`\n]+`")
_MD_IMAGE_RE = re.compile(r"!\[([^\]]*)\]\([^)]*\)")
_MD_LINK_RE = re.compile(r"\[([^\]]*)\]\([^)]*\)")
_AUTOLINK_RE = re.compile(r"<(?:https?://|mailto:|ftp://)[^>]+>")
_BARE_URL_RE = re.compile(r"(?:https?://|ftp://|www\.)[^\s)\]>]+")
_HAS_ALNUM_RE = re.compile(r"[0-9A-Za-zÀ-ÖØ-öø-ÿŒœÆæ]")
_NGRAM_TOKEN_RE = re.compile(r"[a-z0-9àâäéèêëîïôöùûüçœæ]+(?:'[a-z0-9àâäéèêëîïôöùûüçœæ]+)*")
_QUOTED_CITED_RE = re.compile(r"«([^»]+)»\s*(?:\[\d+(?:\s*,\s*\d+)*\])+")
_TABLE_SEP_RE = re.compile(r"^\s*\|?\s*:?-{3,}:?\s*(?:\|\s*:?-{3,}:?\s*)+\|?\s*$")
_BULLET_LINE_RE = re.compile(r"^\s*[-*+]\s+")
_CITATION_REF_RE = re.compile(r"(?<!\\)\[(\d+(?:\s*,\s*\d+)*)\]")
_UNESCAPED_DOLLAR_RE = re.compile(r"(?<!\\)(?:\\\\)*\$")
_SRC_ENTRY_HEAD_RE = re.compile(r"^(?:#{1,4}|[-*+])?\s*\[(\d+)\](?:\s+(SRC-\d+))?", re.MULTILINE)

_FRENCH_MONTHS = {
    "janvier": 1,
    "février": 2,
    "fevrier": 2,
    "mars": 3,
    "avril": 4,
    "mai": 5,
    "juin": 6,
    "juillet": 7,
    "août": 8,
    "aout": 8,
    "septembre": 9,
    "octobre": 10,
    "novembre": 11,
    "décembre": 12,
    "decembre": 12,
}
_FRENCH_DATE_RE = re.compile(
    r"\b(\d{1,2})(?:er)?\s+(janvier|f[eé]vrier|mars|avril|mai|juin|juillet|ao[uû]t|septembre|octobre|novembre|d[eé]cembre)\s+(\d{4})\b",
    re.IGNORECASE,
)
_ISO_DATE_RE = re.compile(r"\b(\d{4})-(\d{2})-(\d{2})\b")
_NUMBER_RE = re.compile(r"\b\d+(?:[ \u00a0\u202f]\d{3})*(?:[.,]\d+)?\b")


def _strip_yaml_and_preserve_lines(text: str) -> tuple[str, int]:
    """Supprime le front matter YAML et retourne (texte, offset_lignes)."""
    norm = text.replace("\r\n", "\n").replace("\r", "\n")
    m = _YAML_FM_RE.match(norm)
    if not m:
        return norm, 0
    removed_lines = m.group(0).count("\n")
    return norm[m.end() :], removed_lines


def _mask_fenced_code_preserving_lines(text: str) -> str:
    """Remplace les blocs de code clotures par des lignes vides pour conserver les numeros de ligne."""
    out: list[str] = []
    fence_char: str | None = None
    fence_len = 0
    for line in text.split("\n"):
        if fence_char is None:
            m = _FENCE_OPEN_RE.match(line)
            if m:
                fence_char = m.group(1)[0]
                fence_len = len(m.group(1))
                out.append("")
                continue
            out.append(line)
        else:
            stripped = line.lstrip()
            if stripped.startswith(fence_char * fence_len) and stripped.strip() == fence_char * len(stripped.strip()):
                fence_char = None
                fence_len = 0
            out.append("")
    return "\n".join(out)


def _mask_comments_and_biblio(text: str) -> str:
    """Remplace les blocs de bibliographie brute et commentaires HTML en gardant le nombre de lignes."""

    def _keep_newlines(match: re.Match[str]) -> str:
        return "\n" * match.group(0).count("\n")

    cleaned = _BIBLIO_BLOCK_RE.sub(_keep_newlines, text)
    return _HTML_COMMENT_RE.sub(_keep_newlines, cleaned)


def count_prose_words(text: str) -> int:
    """Compte les mots de prose en excluant YAML, biblio brute, blocs de code et URLs."""
    body, _ = _strip_yaml_and_preserve_lines(text)
    body = _mask_comments_and_biblio(body)
    body = _mask_fenced_code_preserving_lines(body)
    body = _MD_IMAGE_RE.sub(r"\1", body)
    body = _MD_LINK_RE.sub(r"\1", body)
    body = _AUTOLINK_RE.sub(" ", body)
    body = _BARE_URL_RE.sub(" ", body)
    body = body.replace("|", " ")
    return sum(1 for tok in body.split() if _HAS_ALNUM_RE.search(tok))


def _tokenize_ngram_words(text: str) -> list[str]:
    norm = unicodedata.normalize("NFKC", text).lower().replace("’", "'").replace("`", "")
    return _NGRAM_TOKEN_RE.findall(norm)


def _unit_sources_filename(unit_id: str) -> str:
    return "ch00-sources.md" if unit_id == "00-liminaire" else f"{unit_id}-sources.md"


def _load_json(path: Path) -> dict | list:
    return json.loads(path.read_text(encoding="utf-8"))


def _parse_sources_md(path: Path) -> dict[int, str | None]:
    """Extrait {numero_renvoi: source_id_ou_None} depuis sources/chNN-sources.md."""
    text = path.read_text(encoding="utf-8")
    refs: dict[int, str | None] = {}
    for m in _SRC_ENTRY_HEAD_RE.finditer(text):
        num = int(m.group(1))
        sid = m.group(2)
        if num not in refs:
            refs[num] = sid
    return refs


def _valid_date_not_after_freeze(date_str: str, freeze_date: str = "2026-12-31") -> bool:
    s = str(date_str).strip()
    if not re.match(r"^\d{4}(?:-\d{2}(?:-\d{2})?)?$", s):
        return False
    padded = s
    if len(s) == 4:
        padded = f"{s}-01-01"
    elif len(s) == 7:
        padded = f"{s}-01"
    return padded <= freeze_date


def _check_sources_and_registries(root: Path, manifest: dict, mlr: dict) -> list[str]:
    """Controle --sources-only : CA-09, CA-10 (bases et registres), CA-11."""
    errors: list[str] = []
    reg_dir = root / "registre"
    ancres_path = reg_dir / "ancres-chronologiques.json"
    faits_path = reg_dir / "faits-empiriques.json"
    manifeste_path = root / "recherche" / "manifeste-sources-sha256.json"
    statut_f_path = root / "recherche" / "registre-statut-f.json"

    if not manifeste_path.is_file():
        return [f"[CA-09] Manifeste L+ manquant : {manifeste_path}"]

    try:
        manifeste = _load_json(manifeste_path)
    except json.JSONDecodeError as exc:
        return [f"[CA-09] JSON invalide dans manifeste-sources-sha256.json : {exc}"]

    if not isinstance(manifeste, dict):
        return ["[CA-09] manifeste-sources-sha256.json doit contenir un objet JSON"]

    freeze_date = str(manifeste.get("freeze_date", ""))
    if not freeze_date or freeze_date > "2026-12-31":
        errors.append(f"[CA-10] Date de gel invalide dans manifeste-sources-sha256.json : {freeze_date!r}")

    if manifeste.get("metadata_only_pct") != 0.0:
        errors.append(
            f"[CA-10] METADATA_ONLY interdit : metadata_only_pct={manifeste.get('metadata_only_pct')!r} (attendu 0.0)"
        )

    sources_list = manifeste.get("sources", [])
    if not isinstance(sources_list, list) or not sources_list:
        errors.append("[CA-09] Aucune source L+ recensee dans manifeste-sources-sha256.json")
        return errors

    valid_l_plus_ids: set[str] = set()
    blocked_urls: set[str] = set()
    if statut_f_path.is_file():
        try:
            sf_data = _load_json(statut_f_path)
            entries_f = sf_data.get("blocked", sf_data.get("sources", [])) if isinstance(sf_data, dict) else sf_data
            if isinstance(entries_f, list):
                for item in entries_f:
                    if isinstance(item, dict):
                        if item.get("included_in_evidence") is True:
                            errors.append(f"[CA-10] Source en statut F marquee included_in_evidence=True : {item.get('url')}")
                        if item.get("url"):
                            blocked_urls.add(str(item["url"]))
        except json.JSONDecodeError as exc:
            errors.append(f"[CA-10] JSON invalide dans registre-statut-f.json : {exc}")

    rq_counts: dict[str, set[str]] = {rq["id"]: set() for rq in mlr["research_questions_and_queries"]}

    for idx, src in enumerate(sources_list):
        sid = str(src.get("source_id", f"index-{idx}"))
        if src.get("status") != "L+":
            errors.append(f"[CA-10] Source {sid} en statut F ou non-L+ incluse dans manifeste : status={src.get('status')!r}")
        if src.get("metadata_only") is not False:
            errors.append(f"[CA-10] Source {sid} marquee METADATA_ONLY (metadata_only={src.get('metadata_only')!r})")

        pub_date = str(src.get("publication_date", ""))
        if not _valid_date_not_after_freeze(pub_date, "2026-12-31"):
            errors.append(f"[CA-10] Source {sid} posterieure au gel 2026-12-31 ou date invalide : {pub_date!r}")

        if src.get("url") and str(src["url"]) in blocked_urls:
            errors.append(f"[CA-10] URL en statut F incluse dans le manifeste L+ : {src['url']}")

        rel_txt = src.get("local_txt_path", "")
        txt_path = (root / rel_txt) if rel_txt else None
        if txt_path is None or not txt_path.is_file() or txt_path.stat().st_size == 0:
            errors.append(f"[CA-09] Fichier texte integral manquant ou vide pour {sid} : {rel_txt!r}")
        else:
            raw_bytes = txt_path.read_bytes()
            try:
                raw_bytes.decode("utf-8")
            except UnicodeDecodeError:
                errors.append(f"[CA-09] Fichier non UTF-8 pour {sid} : {rel_txt}")
            digest = hashlib.sha256(raw_bytes).hexdigest()
            if digest != src.get("sha256"):
                errors.append(
                    f"[CA-09] Empreinte sha256 invalide pour {sid} : attendu {src.get('sha256')}, calcule {digest}"
                )

        if src.get("status") == "L+" and src.get("metadata_only") is False:
            valid_l_plus_ids.add(sid)
            for rq in src.get("research_axes", []):
                if rq in rq_counts:
                    rq_counts[rq].add(sid)

    for rq_meta in mlr["research_questions_and_queries"]:
        rq_id = rq_meta["id"]
        min_req = int(rq_meta["min_included_studies"])
        got = len(rq_counts.get(rq_id, set()))
        if got < min_req:
            errors.append(f"[CA-11] Couverture insuffisante pour {rq_id} : {got} < {min_req} etudes L+")

    # Verification des registres
    for reg_path, key_name in ((ancres_path, "anchors"), (faits_path, "facts")):
        if not reg_path.is_file():
            errors.append(f"[CA-07] Registre manquant : {reg_path}")
            continue
        reg_data = _load_json(reg_path)
        for entry in reg_data.get(key_name, []):
            eid = entry.get("id", entry.get("key", "?"))
            if entry.get("statut_preuve") != "l_plus":
                errors.append(f"[CA-10] Entree de registre {eid} non reancree (statut_preuve={entry.get('statut_preuve')!r})")
            lplus_ref = entry.get("source_l_plus_id")
            if not lplus_ref:
                errors.append(f"[CA-10] Entree de registre {eid} sans source_l_plus_id")
            else:
                ref_ids = re.findall(r"SRC-\d+", str(lplus_ref)) or [str(lplus_ref)]
                missing = [r for r in ref_ids if r not in valid_l_plus_ids]
                if missing:
                    errors.append(f"[CA-10] Entree de registre {eid} pointe vers source_l_plus_id invalide : {missing}")

    # Verification des 13 bases fermees sources/ch00..ch12-sources.md
    narrative_units = [u for u in manifest["units"] if u["kind"] in {"frontmatter", "chapter"}]
    for u in narrative_units:
        sname = _unit_sources_filename(u["id"])
        spath = root / "sources" / sname
        if not spath.is_file():
            errors.append(f"[CA-10] Base fermee manquante : sources/{sname}")
            continue
        stext = spath.read_text(encoding="utf-8")
        if not re.search(r"31\s+d[eé]cembre\s+2026", stext, re.IGNORECASE):
            errors.append(f"[CA-10] Date de gel '31 décembre 2026' absente de sources/{sname}")
        parsed = _parse_sources_md(spath)
        if not parsed:
            errors.append(f"[CA-10] Aucune entree numerotee [n] dans sources/{sname}")
        for ref_num, sid in parsed.items():
            if sid and sid not in valid_l_plus_ids:
                errors.append(f"[CA-10] Reference [{ref_num}] dans sources/{sname} cite une source absente ou non-L+ : {sid}")

    return errors


@dataclass
class _CorpusIndex:
    """Index glissant de 12-grammes sur le corpus interne."""

    base: int
    mod_mask: int
    vocab: dict[str, int]
    buckets: dict[int, tuple[str, int, tuple[int, ...]]]

    @classmethod
    def build(cls, root: Path, rel_paths: list[str]) -> _CorpusIndex:
        base = 1_000_003
        mod_mask = (1 << 64) - 1
        pow_base = pow(base, 11, 1 << 64)
        vocab: dict[str, int] = {}
        buckets: dict[int, tuple[str, int, tuple[int, ...]]] = {}

        for rel in rel_paths:
            fpath = (root / rel).resolve()
            if not fpath.is_file():
                continue
            raw = fpath.read_text(encoding="utf-8")
            body, offset = _strip_yaml_and_preserve_lines(raw)
            body = _mask_fenced_code_preserving_lines(body)
            body = _MD_IMAGE_RE.sub(r"\1", body)
            body = _MD_LINK_RE.sub(r"\1", body)
            body = _BARE_URL_RE.sub(" ", body)

            tok_ids: list[int] = []
            tok_lines: list[int] = []
            for lineno, line in enumerate(body.split("\n"), start=offset + 1):
                for w in _tokenize_ngram_words(line):
                    tid = vocab.get(w)
                    if tid is None:
                        tid = len(vocab) + 1
                        vocab[w] = tid
                    tok_ids.append(tid)
                    tok_lines.append(lineno)

            if len(tok_ids) < 12:
                continue

            h = 0
            for j in range(12):
                h = (h * base + tok_ids[j]) & mod_mask
            buckets.setdefault(h, (rel, tok_lines[0], tuple(tok_ids[:12])))

            for i in range(12, len(tok_ids)):
                h = ((h - tok_ids[i - 12] * pow_base) * base + tok_ids[i]) & mod_mask
                if h not in buckets:
                    start = i - 11
                    buckets[h] = (rel, tok_lines[start], tuple(tok_ids[start : i + 1]))

        return cls(base=base, mod_mask=mod_mask, vocab=vocab, buckets=buckets)

    def find_collisions(self, text: str, unit_file: str) -> list[str]:
        if not self.buckets:
            return []
        body, offset = _strip_yaml_and_preserve_lines(text)
        body = _mask_comments_and_biblio(body)
        body = _mask_fenced_code_preserving_lines(body)
        body = _MD_IMAGE_RE.sub(r"\1", body)
        body = _MD_LINK_RE.sub(r"\1", body)
        body = _BARE_URL_RE.sub(" ", body)

        # Exclure exclusivement les segments entre guillemets francais <= 40 mots suivis de [n]
        def _replace_valid_quote(match: re.Match[str]) -> str:
            inner = match.group(1)
            if "\n\n" in inner:
                return match.group(0)
            inner_words = _tokenize_ngram_words(inner)
            if 1 <= len(inner_words) <= 40:
                return " §QUOTE_BREAK§ " + ("\n" * match.group(0).count("\n"))
            return match.group(0)

        filtered = _QUOTED_CITED_RE.sub(_replace_valid_quote, body)

        # Decouper par frontieres de citation exclue
        collisions: list[str] = []
        reported_lines: set[int] = set()
        pow_base = pow(self.base, 11, 1 << 64)

        # Parcours ligne par ligne avec reinitialisation sur §QUOTE_BREAK§
        tok_ids: list[int] = []
        tok_words: list[str] = []
        tok_lines: list[int] = []
        segments: list[tuple[list[int], list[str], list[int]]] = []

        for lineno, line in enumerate(filtered.split("\n"), start=offset + 1):
            parts = line.split("§QUOTE_BREAK§")
            for p_idx, part in enumerate(parts):
                if p_idx > 0:
                    if tok_ids:
                        segments.append((tok_ids, tok_words, tok_lines))
                    tok_ids, tok_words, tok_lines = [], [], []
                for w in _tokenize_ngram_words(part):
                    tid = self.vocab.get(w, 0)
                    tok_ids.append(tid)
                    tok_words.append(w)
                    tok_lines.append(lineno)
        if tok_ids:
            segments.append((tok_ids, tok_words, tok_lines))

        for seg_ids, seg_words, seg_lines in segments:
            if len(seg_ids) < 12:
                continue
            h = 0
            zeros = sum(1 for x in seg_ids[:12] if x == 0)
            for j in range(12):
                h = (h * self.base + seg_ids[j]) & self.mod_mask
            if zeros == 0 and h in self.buckets:
                rel, clino, ctuple = self.buckets[h]
                if tuple(seg_ids[:12]) == ctuple and seg_lines[0] not in reported_lines:
                    reported_lines.add(seg_lines[0])
                    snippet = " ".join(seg_words[:12])
                    collisions.append(
                        f"[CA-03] Collision 12-gramme dans {unit_file} (ligne {seg_lines[0]}) "
                        f"avec {rel} (ligne {clino}) : « {snippet} »"
                    )
            for i in range(12, len(seg_ids)):
                out_id = seg_ids[i - 12]
                in_id = seg_ids[i]
                if out_id == 0:
                    zeros -= 1
                if in_id == 0:
                    zeros += 1
                h = ((h - out_id * pow_base) * self.base + in_id) & self.mod_mask
                if zeros == 0 and h in self.buckets:
                    rel, clino, ctuple = self.buckets[h]
                    start = i - 11
                    if tuple(seg_ids[start : i + 1]) == ctuple and seg_lines[start] not in reported_lines:
                        reported_lines.add(seg_lines[start])
                        snippet = " ".join(seg_words[start : i + 1])
                        collisions.append(
                            f"[CA-03] Collision 12-gramme dans {unit_file} (ligne {seg_lines[start]}) "
                            f"avec {rel} (ligne {clino}) : « {snippet} »"
                        )
        return collisions


def _compile_forbidden_patterns(raw_patterns: list[str]) -> list[tuple[str, re.Pattern[str]]]:
    compiled: list[tuple[str, re.Pattern[str]]] = []
    for pat in raw_patterns:
        is_prose_phrase = " " in pat and "\\" not in pat and "[" not in pat
        flags = re.IGNORECASE if is_prose_phrase else 0
        compiled.append((pat, re.compile(pat, flags)))
    return compiled


def _check_ca02_unit(text: str, unit_file: str, compiled_patterns: list[tuple[str, re.Pattern[str]]]) -> list[str]:
    body, offset = _strip_yaml_and_preserve_lines(text)
    body = _mask_comments_and_biblio(body)
    body = _mask_fenced_code_preserving_lines(body)
    body = _QUOTED_CITED_RE.sub(lambda m: "\n" * m.group(0).count("\n"), body)

    errors: list[str] = []
    for lineno, line in enumerate(body.split("\n"), start=offset + 1):
        for pat_str, regex in compiled_patterns:
            m = regex.search(line)
            if m:
                errors.append(
                    f"[CA-02] Motif banni `{pat_str}` detecte dans {unit_file} (ligne {lineno}) : `{m.group(0)}`"
                )
    return errors


def _check_ca04_unit(text: str, unit_meta: dict) -> list[str]:
    uid = unit_meta["id"]
    ufile = unit_meta["file"]
    body, _ = _strip_yaml_and_preserve_lines(text)
    body = _mask_fenced_code_preserving_lines(body)
    errors: list[str] = []

    if not re.search(r"\*Question directrice\s*:", body):
        errors.append(f"[CA-04] Exergue `*Question directrice :*` manquant dans {ufile}")

    if uid == "00-liminaire":
        for sub in range(1, 7):
            if not re.search(rf"^#{{2,4}}\s+(?:\*\*)?0\.{sub}\b", body, re.MULTILINE):
                errors.append(f"[CA-04] Sous-section 0.{sub} manquante dans {ufile}")
        if not re.search(r"^>\s*\*\*Cinq critères permanents", body, re.MULTILINE):
            errors.append(f"[CA-04] Encadre `> **Cinq critères permanents...` manquant dans {ufile}")
    else:
        num = int(uid[2:])
        for sub in range(1, 5):
            if not re.search(rf"^#{{2,4}}\s+(?:\*\*)?{num}\.{sub}\b", body, re.MULTILINE):
                errors.append(f"[CA-04] Sous-section {num}.{sub} manquante dans {ufile}")
        if not re.search(r"^>\s*\*\*Trois arbitrages sans regret", body, re.MULTILINE):
            errors.append(f"[CA-04] Encadre `> **Trois arbitrages sans regret...` manquant dans {ufile}")

    for fid in unit_meta.get("figures", []):
        if not re.search(rf"\b{re.escape(fid)}\b", body):
            errors.append(f"[CA-04] Figure assignee {fid} non referencee dans {ufile}")

    return errors


def _check_ca05_unit(text: str, unit_meta: dict, wb: dict) -> list[str]:
    uid = unit_meta["id"]
    ufile = unit_meta["file"]
    body, _ = _strip_yaml_and_preserve_lines(text)
    body = _mask_comments_and_biblio(body)
    body = _mask_fenced_code_preserving_lines(body)
    lines = body.split("\n")

    table_count = sum(1 for line in lines if _TABLE_SEP_RE.match(line))
    errors: list[str] = []
    if uid == "00-liminaire":
        if table_count != 1:
            errors.append(f"[CA-05] Le liminaire doit contenir exactement 1 tableau (trouve : {table_count})")
    else:
        max_tables = int(wb.get("max_tables_per_chapter", 2))
        if table_count > max_tables:
            errors.append(f"[CA-05] Trop de tableaux dans {ufile} : {table_count} > {max_tables}")

    non_empty = [line for line in lines if line.strip()]
    if non_empty:
        bullet_count = sum(1 for line in non_empty if _BULLET_LINE_RE.match(line))
        ratio = bullet_count / len(non_empty)
        max_ratio = float(wb.get("max_bullet_line_ratio", 0.18))
        if ratio > max_ratio:
            errors.append(
                f"[CA-05] Ratio de lignes en puces excessif dans {ufile} : {ratio:.1%} > {max_ratio:.0%}"
            )
    return errors


def _check_ca06_unit(text: str, unit_file: str) -> list[str]:
    body, offset = _strip_yaml_and_preserve_lines(text)
    body = _mask_comments_and_biblio(body)
    body = _mask_fenced_code_preserving_lines(body)
    errors: list[str] = []

    no_inline_lines: list[str] = []
    for lineno, line in enumerate(body.split("\n"), start=offset + 1):
        clean_line = _INLINE_CODE_RE.sub("", line)
        no_inline_lines.append(clean_line)
        if _UNESCAPED_DOLLAR_RE.search(clean_line):
            errors.append(
                f"[CA-06] Symbole $ non echappe dans {unit_file} (ligne {lineno}) : {line.strip()}"
            )

    full_clean = "\n".join(no_inline_lines)
    if full_clean.count(r"\(") != full_clean.count(r"\)"):
        errors.append(f"[CA-06] Delimiteurs mathematiques \\(...\\) desequilibres dans {unit_file}")
    if full_clean.count(r"\[") != full_clean.count(r"\]"):
        errors.append(f"[CA-06] Delimiteurs mathematiques \\[...\\] desequilibres dans {unit_file}")
    return errors


def _check_ca10_unit(text: str, unit_meta: dict, root: Path) -> list[str]:
    uid = unit_meta["id"]
    ufile = unit_meta["file"]
    sname = _unit_sources_filename(uid)
    spath = root / "sources" / sname
    if not spath.is_file():
        return [f"[CA-10] Base fermee manquante pour {uid} : sources/{sname}"]

    valid_refs = set(_parse_sources_md(spath).keys())
    body, offset = _strip_yaml_and_preserve_lines(text)
    body = _mask_comments_and_biblio(body)
    body = _mask_fenced_code_preserving_lines(body)
    body = _INLINE_CODE_RE.sub("", body)
    body = _MD_IMAGE_RE.sub("", body)
    body = _MD_LINK_RE.sub(r"\1", body)

    errors: list[str] = []
    found_any = False
    for lineno, line in enumerate(body.split("\n"), start=offset + 1):
        for m in _CITATION_REF_RE.finditer(line):
            for part in m.group(1).split(","):
                ref_num = int(part.strip())
                found_any = True
                if ref_num not in valid_refs:
                    errors.append(
                        f"[CA-10] Renvoi orphelin [{ref_num}] dans {ufile} (ligne {lineno}) absent de sources/{sname}"
                    )
    if not found_any:
        errors.append(f"[CA-10] Aucun renvoi source [n] dans {ufile}")
    return errors


def _extract_iso_dates_from_text(text: str) -> set[str]:
    """Extrait les dates ISO YYYY-MM-DD des formulations francaises ou ISO."""
    dates: set[str] = set()
    for m in _ISO_DATE_RE.finditer(text):
        dates.add(f"{m.group(1)}-{m.group(2)}-{m.group(3)}")
    for m in _FRENCH_DATE_RE.finditer(text):
        day = int(m.group(1))
        month = _FRENCH_MONTHS.get(m.group(2).lower())
        year = int(m.group(3))
        if month:
            dates.add(f"{year:04d}-{month:02d}-{day:02d}")
    return dates


def _extract_numbers(text: str) -> set[float]:
    nums: set[float] = set()
    for m in _NUMBER_RE.finditer(text):
        raw = m.group(0).replace(" ", "").replace("\u00a0", "").replace("\u202f", "").replace(",", ".")
        try:
            nums.add(float(raw))
        except ValueError:
            continue
    return nums


def _anchor_matches_sentence(anchor_key: str, sent_lower: str) -> bool:
    if anchor_key == "2026-08-02-EU-AI-ACT-ART50":
        return "ai act" in sent_lower and ("article 50" in sent_lower or "art. 50" in sent_lower)
    if anchor_key == "2026-LOI25-ART12-1":
        return "loi 25" in sent_lower and ("12.1" in sent_lower or "automatis" in sent_lower)
    if anchor_key == "2027-03-15-TLS-100J":
        return ("tls" in sent_lower or "certificat" in sent_lower) and "100 jours" in sent_lower
    if anchor_key == "2027-05-01-BSIF-E23-AMF":
        return "e-23" in sent_lower or ("amf" in sent_lower and "ligne directrice" in sent_lower)
    if anchor_key == "2027-12-02-EU-AI-ACT-ANNEXE-III":
        return "ai act" in sent_lower and "annexe iii" in sent_lower
    if anchor_key == "2028-08-02-EU-AI-ACT-ANNEXE-I":
        return "ai act" in sent_lower and bool(re.search(r"\bannexe i\b", sent_lower))
    if anchor_key == "2028-10-01-GESTION-PATRIMOINE-RETROFACTURATION":
        return "rétrofacturation" in sent_lower or "retrofacturation" in sent_lower
    if anchor_key == "2028-12-31-BSIF-B15-PORTEE3":
        return "b-15" in sent_lower and "portée 3" in sent_lower
    if anchor_key == "2029-03-15-TLS-47J":
        return ("tls" in sent_lower or "certificat" in sent_lower) and "47 jours" in sent_lower
    if anchor_key == "2030-2035-G7-PQC-FINANCE":
        return ("g7" in sent_lower and "post-quantique" in sent_lower) or "ir 8547" in sent_lower
    if anchor_key == "2033-06-30-LOIS-FINANCIERES-CANADA":
        return ("lois fédérales" in sent_lower or "lois financières" in sent_lower) and "révision" in sent_lower
    return False


def _fact_matches_sentence(fact_id: str, sent_lower: str) -> tuple[bool, bool]:
    """Retourne (correspond_au_fait, requiert_verification_stricte_chiffres)."""
    if fact_id == "FACT-COMPUTE-10X":
        return ("genewein" in sent_lower and "calcul" in sent_lower and "×" in sent_lower), True
    if fact_id == "FACT-LUSSER-10-STEPS":
        return ("lusser" in sent_lower and "94" in sent_lower and "%" in sent_lower), True
    if fact_id == "FACT-GARTNER-ABANDON-2027":
        return ("abandon" in sent_lower and "2027" in sent_lower and "%" in sent_lower), True
    if fact_id == "FACT-HYPERSCALER-CAPEX-2026":
        has_hyp = any(k in sent_lower for k in ("alphabet", "amazon", "meta", "microsoft", "hyperscaler", "quatre grands fournisseurs"))
        return (has_hyp and "2026" in sent_lower and ("g$" in sent_lower or "g\\$" in sent_lower)), True
    if fact_id == "FACT-MARKET-ENVELOPE-2027-2030":
        return ("médiane" in sent_lower and ("2027" in sent_lower or "2030" in sent_lower) and ("g$" in sent_lower or "g\\$" in sent_lower)), True
    if fact_id == "FACT-MAP-STUDY":
        return (("étude map" in sent_lower or "pan et al" in sent_lower) and "%" in sent_lower), True
    if fact_id == "FACT-MAST-FAILURES":
        return ("mast" in sent_lower and "%" in sent_lower), True
    if fact_id == "FACT-CAMEL-AGENTDOJO":
        return ("camel" in sent_lower and "agentdojo" in sent_lower and "%" in sent_lower), True
    if fact_id == "FACT-JUNIOR-DEV-CONTRACTION":
        return ("stanford hai" in sent_lower and ("22" in sent_lower or "développeur" in sent_lower) and "%" in sent_lower), True
    if fact_id == "FACT-PQC-SIGNATURE-SIZE":
        return (("ml-dsa-65" in sent_lower or "ml-dsa-87" in sent_lower) and "octet" in sent_lower), True
    return False, False


def _check_ca07_registries(root: Path, unit_texts: dict[str, str], check_global_presence: bool) -> list[str]:
    """Controle la concordance exacte avec ancres-chronologiques.json et faits-empiriques.json."""
    errors: list[str] = []
    ancres = _load_json(root / "registre" / "ancres-chronologiques.json").get("anchors", [])
    faits = _load_json(root / "registre" / "faits-empiriques.json").get("facts", [])

    # 1. Presence globale des ancres et faits dans leurs chapitres proprietaires
    if check_global_presence:
        for anchor in ancres:
            akey = anchor["key"]
            adate = str(anchor["date"])
            joined = "\n".join(unit_texts.get(ch, "") for ch in anchor["chapters"])
            if re.match(r"^\d{4}-\d{2}-\d{2}$", adate):
                found_dates = _extract_iso_dates_from_text(joined)
                if adate not in found_dates:
                    errors.append(
                        f"[CA-07] Date de l'ancre {akey} ({adate}) absente de ses chapitres {anchor['chapters']}"
                    )
            else:
                years = re.findall(r"\d{4}", adate)
                if years and not all(y in joined for y in years):
                    errors.append(
                        f"[CA-07] Repere temporel de l'ancre {akey} ({adate}) absent de ses chapitres {anchor['chapters']}"
                    )

        for fact in faits:
            owner = fact["owner_chapter"]
            owner_text = unit_texts.get(owner, "")
            expected_nums = _extract_numbers(fact["value"])
            owner_nums = _extract_numbers(owner_text)
            if expected_nums and not (expected_nums & owner_nums):
                errors.append(
                    f"[CA-07] Valeurs du fait {fact['id']} ({fact['value']}) absentes du chapitre proprietaire {owner}"
                )

    # 2. Contradictions locales phrase par phrase
    exact_anchors = {a["key"]: a for a in ancres if re.match(r"^\d{4}-\d{2}-\d{2}$", str(a["date"]))}
    for uid, raw_text in unit_texts.items():
        body, _ = _strip_yaml_and_preserve_lines(raw_text)
        body = _mask_comments_and_biblio(body)
        body = _mask_fenced_code_preserving_lines(body)
        sentences = [s.strip() for s in re.split(r"(?<=[.!?])\s+|\n+", body) if s.strip()]

        for sent in sentences:
            sent_lower = sent.lower()
            sent_dates = _extract_iso_dates_from_text(sent)
            if sent_dates:
                matched_anchors = [a for a in ancres if _anchor_matches_sentence(a["key"], sent_lower)]
                expected_in_sent = {str(a["date"]) for a in matched_anchors if a["key"] in exact_anchors}
                for a in matched_anchors:
                    if a["key"] in exact_anchors and str(a["date"]) not in sent_dates:
                        # Verifier si la date presente appartient a une autre ancre mentionnee dans la meme phrase
                        other_expected = expected_in_sent - {str(a["date"])}
                        if not (sent_dates <= other_expected):
                            errors.append(
                                f"[CA-07] Divergence de date pour l'ancre {a['key']} dans {uid} : "
                                f"trouve {sorted(sent_dates)}, attendu {a['date']}"
                            )

            for fact in faits:
                matched, strict_num = _fact_matches_sentence(fact["id"], sent_lower)
                if not matched or not strict_num:
                    continue
                val_str = fact["value"]
                val_pcts = {
                    float(m.replace(",", "."))
                    for m in re.findall(r"(\d+(?:[.,]\d+)?)\s*%", val_str)
                }
                sent_pcts = {
                    float(m.replace(",", "."))
                    for m in re.findall(r"(\d+(?:[.,]\d+)?)\s*%", sent)
                }
                val_nums = _extract_numbers(val_str)
                sent_nums = _extract_numbers(sent)
                if val_pcts and sent_pcts:
                    if not (val_pcts & sent_pcts):
                        errors.append(
                            f"[CA-07] Divergence de pourcentage pour {fact['id']} dans {uid} : "
                            f"attendu {sorted(val_pcts)} %, trouve {sorted(sent_pcts)} % (extrait : {sent[:120]})"
                        )
                elif fact["id"] == "FACT-PQC-SIGNATURE-SIZE":
                    large_expected = {n for n in val_nums if n >= 100}
                    if "ml-dsa-65" in sent_lower and (3309.0 in val_nums) and 3309.0 not in sent_nums:
                        errors.append(f"[CA-07] Divergence ML-DSA-65 dans {uid} : attendu 3 309 octets")
                    elif "ml-dsa-87" in sent_lower and (4627.0 in val_nums) and 4627.0 not in sent_nums:
                        errors.append(f"[CA-07] Divergence ML-DSA-87 dans {uid} : attendu 4 627 octets")
                    elif large_expected and not (large_expected & sent_nums):
                        errors.append(f"[CA-07] Divergence taille PQC dans {uid} : attendu {sorted(large_expected)}")
                elif val_nums and not (val_nums & sent_nums):
                    errors.append(
                        f"[CA-07] Divergence chiffree pour {fact['id']} dans {uid} : "
                        f"attendu {val_str} (extrait : {sent[:120]})"
                    )

    return errors


def _check_ca08_figures(root: Path, manifest: dict) -> list[str]:
    errors: list[str] = []
    rendus_dir = root / "diagrammes" / "rendus"
    for fmeta in manifest.get("figures", []):
        fid = fmeta["id"]
        engine = fmeta["engine"]
        ext = "svg" if engine == "puml" else "png"
        out_path = rendus_dir / f"{fid}.{ext}"
        if not out_path.is_file() or out_path.stat().st_size == 0:
            errors.append(f"[CA-08] Rendu de figure manquant ou vide : {out_path}")
            continue
        if ext == "svg":
            svg_txt = out_path.read_text(encoding="utf-8", errors="replace")
            if "<svg" not in svg_txt or "Syntax Error" in svg_txt:
                errors.append(f"[CA-08] SVG invalide ou erreur de syntaxe dans {out_path}")
        else:
            if not out_path.read_bytes().startswith(b"\x89PNG\r\n\x1a\n"):
                errors.append(f"[CA-08] Signature PNG invalide dans {out_path}")
    return errors


def _check_ca17_annexes(root: Path) -> list[str]:
    from genere_annexes import build_annexes  # lazy import pour eviter cycle

    errors: list[str] = []
    expected_map = build_annexes(root, dry_run=True)
    for annex_path, expected_content in expected_map.items():
        if not annex_path.is_file():
            errors.append(f"[CA-17] Annexe generee manquante : {annex_path}")
            continue
        actual = annex_path.read_text(encoding="utf-8").replace("\r\n", "\n").rstrip()
        expected = expected_content.replace("\r\n", "\n").rstrip()
        if actual != expected:
            errors.append(
                f"[CA-17] Annexe {annex_path.name} desynchronisee par rapport a genere_annexes.py"
            )
    return errors


def _check_deliverables(root: Path, manifest: dict) -> list[str]:
    errors: list[str] = []
    narrative_units = [u for u in manifest["units"] if u["kind"] in {"frontmatter", "chapter"}]

    # CA-12 : ancrage/ch00..ch12-ancrage.md (100 % supportes, 0 non supporte)
    for u in narrative_units:
        aname = "ch00-ancrage.md" if u["id"] == "00-liminaire" else f"{u['id']}-ancrage.md"
        apath = root / "ancrage" / aname
        if not apath.is_file() or apath.stat().st_size == 0:
            errors.append(f"[CA-12] Journal d'ancrage manquant ou vide : ancrage/{aname}")
            continue
        atext = apath.read_text(encoding="utf-8")
        if "supporté" not in atext.lower():
            errors.append(f"[CA-12] Verdict 'supporté' absent de ancrage/{aname}")
        if re.search(r"(?i)(?:verdict|statut)\s*[:=]\s*non supporté", atext) or re.search(
            r"(?i)non supportés?\s*:\s*[1-9]\d*", atext
        ):
            errors.append(f"[CA-12] Affirmation non supportee restante dans ancrage/{aname}")

    # CA-13 & CA-14 : recollations G3
    s1_locs: set[str] = set()
    s1_paras: set[str] = set()
    for seed, code, required in (("202701", "CA-13", True), ("202702", "CA-14", True), ("202703", "CA-14", False)):
        jpath = root / "aq" / f"recollation-seed-{seed}.json"
        mpath = root / "aq" / f"recollation-seed-{seed}.md"
        if not jpath.is_file() or not mpath.is_file():
            if required:
                errors.append(f"[{code}] Livrable de recollation manquant pour seed={seed}")
            continue
        try:
            data = _load_json(jpath)
        except json.JSONDecodeError as exc:
            errors.append(f"[{code}] JSON invalide dans {jpath.name} : {exc}")
            continue
        items = data.get("items", data.get("sample", [])) if isinstance(data, dict) else data
        if not isinstance(items, list) or len(items) != 60:
            errors.append(f"[{code}] {jpath.name} doit contenir 60 items (trouve : {len(items) if isinstance(items, list) else 'invalide'})")
            continue
        locs = {str(it.get("claim_loc", "")) for it in items}
        paras = {str(it.get("paragraph_loc", "")) for it in items}
        if seed == "202701":
            s1_locs, s1_paras = locs, paras
        elif seed == "202702":
            if not locs.isdisjoint(s1_locs) or not paras.isdisjoint(s1_paras):
                errors.append("[CA-14] Chevauchement detecte entre recollation 202701 et 202702")
        md_txt = mpath.read_text(encoding="utf-8")
        if "60/60" not in md_txt and "60 / 60" not in md_txt:
            errors.append(f"[{code}] Score final 60/60 absent de {mpath.name}")

    # CA-15 & CA-16/18 : gauntlet et lissage/visuel
    glog = root / "aq" / "gauntlet-log.md"
    if not glog.is_file() or glog.stat().st_size == 0:
        errors.append("[CA-15] Journal aq/gauntlet-log.md manquant ou vide")
    rvis = root / "aq" / "rapport-lissage-et-visuel.md"
    if not rvis.is_file() or rvis.stat().st_size == 0:
        errors.append("[CA-16] Rapport aq/rapport-lissage-et-visuel.md manquant ou vide")

    # Livrables assembles
    liv_dir = root / "livrables"
    md_out = liv_dir / "7 - Livre 2027.md"
    html_out = liv_dir / "7 - Livre 2027.html"
    pdf_out = liv_dir / "7 - Livre 2027.pdf"
    if not md_out.is_file() or md_out.stat().st_size == 0:
        errors.append("[CA-18] Livrable Markdown manquant : livrables/7 - Livre 2027.md")
    if not html_out.is_file() or "<html" not in html_out.read_text(encoding="utf-8", errors="replace"):
        errors.append("[CA-18] Livrable HTML autonome manquant ou invalide : livrables/7 - Livre 2027.html")
    if not pdf_out.is_file() or not pdf_out.read_bytes().startswith(b"%PDF-"):
        errors.append("[CA-18] Livrable PDF manquant ou invalide : livrables/7 - Livre 2027.pdf")

    return errors


def check_manuscrit(
    root: Path,
    strict: bool = True,
    sources_only: bool = False,
    unit_id: str | None = None,
    check_deliverables: bool = False,
) -> list[str]:
    """Execute les verifications deterministes du manuscrit selon le mode demande."""
    root = Path(root)
    manifest = _load_json(root / "specs" / "manifest.json")
    mlr = _load_json(root / "specs" / "protocole-mlr-2027.json")

    if sources_only:
        return _check_sources_and_registries(root, manifest, mlr)

    errors: list[str] = []
    wb = manifest["word_budget"]
    units = manifest["units"]
    compiled_forbidden = _compile_forbidden_patterns(manifest["forbidden_prose_regexes"])

    if unit_id is not None:
        target_units = [u for u in units if u["id"] == unit_id]
        if not target_units:
            return [f"Unite inconnue dans manifest.json : {unit_id}"]
    else:
        target_units = units
        errors.extend(_check_sources_and_registries(root, manifest, mlr))

    corpus_index = _CorpusIndex.build(root, manifest["internal_corpus_paths"])
    unit_texts: dict[str, str] = {}
    total_words = 0

    for u in target_units:
        uid = u["id"]
        ufile = u["file"]
        upath = root / ufile
        if not upath.is_file():
            errors.append(f"[CA-01] Fichier d'unite manquant : {ufile}")
            continue

        text = upath.read_text(encoding="utf-8")
        unit_texts[uid] = text
        wc = count_prose_words(text)
        total_words += wc

        if wc < u["min_words"] or wc > u["max_words"]:
            errors.append(
                f"[CA-01] Volume hors plage pour {uid} ({ufile}) : {wc} mots (attendu [{u['min_words']}, {u['max_words']}])"
            )

        errors.extend(_check_ca06_unit(text, ufile))

        if u["kind"] in {"frontmatter", "chapter"}:
            errors.extend(_check_ca02_unit(text, ufile, compiled_forbidden))
            errors.extend(corpus_index.find_collisions(text, ufile))
            errors.extend(_check_ca04_unit(text, u))
            errors.extend(_check_ca05_unit(text, u, wb))
            errors.extend(_check_ca10_unit(text, u, root))

    if unit_id is None:
        if strict:
            if total_words < wb["total_min"] or total_words > wb["total_max"]:
                errors.append(
                    f"[CA-01] Volume total hors plage : {total_words} mots (attendu [{wb['total_min']}, {wb['total_max']}])"
                )
            errors.extend(_check_ca08_figures(root, manifest))
            errors.extend(_check_ca17_annexes(root))
        errors.extend(_check_ca07_registries(root, unit_texts, check_global_presence=strict))
    elif strict:
        errors.extend(_check_ca07_registries(root, unit_texts, check_global_presence=False))

    if check_deliverables:
        errors.extend(_check_deliverables(root, manifest))

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Verificateur deterministe G1 du Livre 2027.")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent, help="Racine du livre")
    parser.add_argument("--strict", action="store_true", help="Verification complete stricte (defaut)")
    parser.add_argument("--sources-only", action="store_true", help="Verifier uniquement corpus L+, SHA-256 et bases sources")
    parser.add_argument("--unit", type=str, default=None, help="Verifier une unite specifique (ex. ch01, 00-liminaire)")
    parser.add_argument("--check-deliverables", action="store_true", help="Verifier aussi ancrage/, aq/ et livrables/")
    args = parser.parse_args()

    strict_mode = True if not args.unit else args.strict
    if args.strict:
        strict_mode = True

    errors = check_manuscrit(
        root=args.root,
        strict=strict_mode,
        sources_only=args.sources_only,
        unit_id=args.unit,
        check_deliverables=args.check_deliverables,
    )
    if errors:
        print(f"ECHEC G1 ({len(errors)} erreur(s)) :", file=sys.stderr)
        for err in errors:
            print(f"  - {err}", file=sys.stderr)
        return 1
    print("OK : Barriere deterministe G1 passee avec 0 erreur.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
