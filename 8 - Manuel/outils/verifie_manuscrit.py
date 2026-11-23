#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Barriere deterministe G1 du Volume 8 (verifie_manuscrit.py).

Controle CA-01..CA-11, CA-17, CA-20 (CA-G0-SYNC) et les livrables G0..G5.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import unicodedata
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path

import pymupdf

_TOOLS_DIR = Path(__file__).resolve().parent
if str(_TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(_TOOLS_DIR))

from _communs import (  # noqa: E402
    DEFAULT_FREEZE_DATE,
    compile_forbidden_patterns,
    compute_excerpt_sha256,
    compute_lf_sha256_bytes,
    format_french_date,
    french_date_regex,
    get_freeze_date,
    is_markdown_table_block,
    normalize_lf_text,
    normalize_quotes_spaces,
    parse_iso_date,
    split_sentences,
)

_YAML_FM_RE = re.compile(r"\A\ufeff?---\r?\n.*?\r?\n(?:---|\.\.\.)(?:\r?\n|\Z)", re.DOTALL)
_BIBLIO_BLOCK_RE = re.compile(
    r"<!--\s*BIBLIOGRAPHIE_BRUTE_DEBUT\s*-->.*?<!--\s*BIBLIOGRAPHIE_BRUTE_FIN\s*-->",
    re.DOTALL,
)
_HTML_COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)
_CA_G0_SYNC_RE = re.compile(
    r'<!--\s*CA-G0-SYNC\s+([^>]*?)-->'
)
_CA_G0_ATTR_RE = re.compile(r'(\w+)="([^"]*)"')
_FENCE_OPEN_RE = re.compile(r"^\s*(`{3,}|~{3,})")
_INLINE_CODE_RE = re.compile(r"(?<!`)(`+)(?!`)(?:(?!(?<!`)\1(?!`)).)+?\1(?!`)")
_MD_IMAGE_RE = re.compile(r"!\[([^\]]*)\]\([^)]*\)")
_MD_LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)]*)\)")
_AUTOLINK_RE = re.compile(r"<(?:https?://|mailto:|ftp://)[^>]+>")
_BARE_URL_RE = re.compile(r"(?:https?://|ftp://|www\.)[^\s)\]>]+")
_HAS_ALNUM_RE = re.compile(r"[0-9A-Za-zÀ-ÖØ-öø-ÿŒœÆæ]")
_NGRAM_TOKEN_RE = re.compile(r"[a-z0-9àâäéèêëîïôöùûüçœæ]+(?:'[a-z0-9àâäéèêëîïôöùûüçœæ]+)*")
_QUOTED_CITED_RE = re.compile(r"«([^»]+)»\s*(?:\[\d+(?:\s*,\s*\d+)*\])+")
_TABLE_SEP_RE = re.compile(r"^\s*\|?\s*:?-{3,}:?\s*(?:\|\s*:?-{3,}:?\s*)+\|?\s*$")
_LIST_LINE_RE = re.compile(r"^\s*(?:[-*+]|\d+\.)\s+")
_CITATION_REF_RE = re.compile(r"(?<!\\)\[(\d+(?:\s*,\s*\d+)*)\]")
_UNESCAPED_DOLLAR_RE = re.compile(r"(?<!\\)(?:\\\\)*\$")
_SRC_ENTRY_HEAD_RE = re.compile(r"^(?:#{1,4}|[-*+])?\s*\[(\d+)\](?:\s+(SRC-\d+))?", re.MULTILINE)
_HTML_ENTITY_RE = re.compile(r"&(?:#\d+|#x[0-9a-fA-F]+|[A-Za-z][A-Za-z0-9]+);")
_INLINE_MATH_RE = re.compile(r"\\\(.*?\\\)|\\\[.*?\\\]", re.DOTALL)
_DECIMAL_DOT_RE = re.compile(r"(?<=\d)\.(?=\d)")
_SECTION_REF_RE = re.compile(r"§\s*\d+(?:\.\d+)*")
_CAPTION_FIG_RE = re.compile(r"^\*Figure\s+(\d+)\s*[—–-]")
_CAPTION_TAB_DOT_RE = re.compile(r"^\*Tableau\s+(\d+)\.(\d+)\s*[—–-]")
_CAPTION_TAB_BARE_RE = re.compile(r"^\*Tableau\s+(\d+)\s*[—–-]")
_FORBIDDEN_PROSE_BACKTICK_RE = re.compile(
    r"^(?:"
    r"draft-[a-z0-9-]+|RFC\s*\d+|FIPS\s*\d+|ISO(?:/IEC)?\s*\d+|Loi\s+\d+|(?:EU\s+)?AI\s+Act|"
    r"SHA-\d+|MD5|HMAC|TLS(?:\s*1\.[23])?|PKI|HTTPS?|REST|gRPC|GraphQL|"
    r"JSON|YAML|XML|HTML|PDF|SVG|PNG|CSV|SQL|API|SDK|LLM|RAG|AGI|ASI|"
    r"ERP|CRM|ITSM|MCP|A2A|OPA|Rego|BSIF|OSFI|AMF|OCRI|ACVM|NIST|IETF|WIMSE|"
    r"SPIFFE|SPIRE|DORA|RGPD|WORM|FinOps|FOCUS|OTel|DAPP|STAMP|STPA|EvalOps|"
    r"ML-DSA(?:-\d+)?|SLH-DSA|CapEx|NHI|OBO|CIBA|DPoP|FIDO2|JCS|JWS|I-JSON|SCITT|"
    r"MAST|MAP|CaMeL|CoALA|Zero-Trust|PRR|SBB|L[0-4]|L\+"
    r")$",
    re.IGNORECASE,
)

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
_FRENCH_MONTH_YEAR_RE = re.compile(
    r"\b(janvier|f[eé]vrier|mars|avril|mai|juin|juillet|ao[uû]t|septembre|octobre|novembre|d[eé]cembre)\s+(\d{4})\b",
    re.IGNORECASE,
)
_ISO_DATE_RE = re.compile(r"\b(\d{4})-(\d{2})-(\d{2})\b")
_ISO_MONTH_RE = re.compile(r"\b(\d{4})-(\d{2})(?!-\d)\b")
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
    no_refs = _CITATION_REF_RE.sub(" ", text)
    norm = unicodedata.normalize("NFKC", no_refs).lower().replace("’", "'").replace("‘", "'").replace("`", "")
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


def _valid_date_not_after_freeze(date_str: str, freeze_date: str = DEFAULT_FREEZE_DATE) -> bool:
    s = str(date_str).strip()
    if not re.match(r"^\d{4}(?:-\d{2}(?:-\d{2})?)?$", s):
        return False
    padded = s
    if len(s) == 4:
        padded = f"{s}-01-01"
    elif len(s) == 7:
        padded = f"{s}-01"
    if parse_iso_date(padded) is None:
        return False
    return padded <= freeze_date


def _extract_fenced_blocks(body: str) -> list[tuple[int, int, list[str]]]:
    """Extrait (ligne_ouverture_0idx, ligne_fermeture_0idx, lignes_internes) de chaque bloc cloture."""
    lines = body.split("\n")
    blocks: list[tuple[int, int, list[str]]] = []
    fence_char: str | None = None
    fence_len = 0
    open_idx = -1
    inner: list[str] = []

    for idx, line in enumerate(lines):
        if fence_char is None:
            m = _FENCE_OPEN_RE.match(line)
            if m:
                fence_char = m.group(1)[0]
                fence_len = len(m.group(1))
                open_idx = idx
                inner = []
        else:
            stripped = line.lstrip()
            if stripped.startswith(fence_char * fence_len) and stripped.strip() == fence_char * len(stripped.strip()):
                blocks.append((open_idx, idx, inner))
                fence_char = None
                fence_len = 0
                open_idx = -1
                inner = []
            else:
                inner.append(line)

    if fence_char is not None and open_idx >= 0:
        blocks.append((open_idx, len(lines) - 1, inner))
    return blocks


def _check_ca_g0_sync(
    root: Path,
    text: str,
    unit_meta: dict,
    g0_report: dict | None,
) -> list[str]:
    """Controle CA-20 (CA-G0-SYNC) en levant le masquage des blocs de code clotures."""
    uid = unit_meta["id"]
    ufile = unit_meta["file"]
    body, offset = _strip_yaml_and_preserve_lines(text)
    body_no_bib = _BIBLIO_BLOCK_RE.sub(lambda m: "\n" * m.group(0).count("\n"), body)
    lines = body_no_bib.split("\n")
    fenced_blocks = _extract_fenced_blocks(body_no_bib)

    if not fenced_blocks:
        return []

    errors: list[str] = []
    if unit_meta.get("kind") != "chapter":
        for open_idx, _, _ in fenced_blocks:
            errors.append(
                f"[CA-G0-SYNC] [CA-20] Bloc de code interdit hors Chapitres 01..04 dans {ufile} (ligne {offset + open_idx + 1})"
            )
        return errors

    trousse_root = (root / "trousse").resolve()
    synced_map = (g0_report or {}).get("synced_excerpts", {}) if isinstance(g0_report, dict) else {}

    for open_idx, _, block_lines in fenced_blocks:
        lineno = offset + open_idx + 1
        if len(block_lines) == 0:
            errors.append(f"[CA-G0-SYNC] [CA-20] Bloc de code vide dans {ufile} (ligne {lineno})")
            continue
        if len(block_lines) > 40:
            errors.append(
                f"[CA-G0-SYNC] [CA-20] Extrait de code depasse 40 lignes ({len(block_lines)} L) dans {ufile} (ligne {lineno})"
            )

        # Chercher la balise <!-- CA-G0-SYNC ... --> sur la ligne precedente non vide
        anchor_attrs: dict[str, str] | None = None
        for probe in range(open_idx - 1, max(-1, open_idx - 4), -1):
            cand = lines[probe].strip()
            if not cand:
                continue
            m_tag = _CA_G0_SYNC_RE.fullmatch(cand)
            if m_tag:
                anchor_attrs = {k: v for k, v in _CA_G0_ATTR_RE.findall(m_tag.group(1))}
            break

        if not anchor_attrs or not {"id", "path", "lines", "sha256"} <= set(anchor_attrs.keys()):
            errors.append(
                f"[CA-G0-SYNC] [CA-20] Bloc de code sans balise `<!-- CA-G0-SYNC id=... path=... lines=... sha256=... -->` valide dans {ufile} (ligne {lineno})"
            )
            continue

        anchor_id = anchor_attrs["id"].strip()
        rel_path_raw = anchor_attrs["path"].strip()
        lines_spec = anchor_attrs["lines"].strip()
        declared_sha = anchor_attrs["sha256"].strip().lower()

        if not rel_path_raw.startswith("8 - Manuel/trousse/"):
            errors.append(
                f"[CA-G0-SYNC] [CA-20] Chemin CA-G0-SYNC invalide pour {anchor_id} (doit debuter par '8 - Manuel/trousse/') : {rel_path_raw!r}"
            )
            continue

        rel_inside = rel_path_raw[len("8 - Manuel/trousse/") :]
        src_path = (trousse_root / rel_inside).resolve()
        if not src_path.is_relative_to(trousse_root) or not src_path.is_file():
            errors.append(
                f"[CA-G0-SYNC] [CA-20] Fichier source introuvable pour {anchor_id} : {rel_path_raw}"
            )
            continue

        m_rng = re.fullmatch(r"(\d+)-(\d+)", lines_spec)
        if not m_rng:
            errors.append(
                f"[CA-G0-SYNC] [CA-20] Plage de lignes invalide pour {anchor_id} : {lines_spec!r}"
            )
            continue
        start_ln, end_ln = int(m_rng.group(1)), int(m_rng.group(2))
        src_norm_lines = normalize_lf_text(src_path.read_text(encoding="utf-8")).split("\n")
        if src_norm_lines and src_norm_lines[-1] == "":
            src_norm_lines = src_norm_lines[:-1]

        if start_ln < 1 or end_ln < start_ln or end_ln > len(src_norm_lines):
            errors.append(
                f"[CA-G0-SYNC] [CA-20] Bornes de lignes hors fichier pour {anchor_id} ({lines_spec}, fichier={len(src_norm_lines)} L)"
            )
            continue

        expected_slice = src_norm_lines[start_ln - 1 : end_ln]
        if len(expected_slice) > 40:
            errors.append(
                f"[CA-G0-SYNC] [CA-20] Tranche source > 40 lignes pour {anchor_id} ({len(expected_slice)} L)"
            )

        actual_sha = compute_excerpt_sha256(block_lines)
        expected_sha = compute_excerpt_sha256(expected_slice)
        if block_lines != expected_slice or actual_sha != expected_sha or declared_sha != expected_sha:
            errors.append(
                f"[CA-G0-SYNC] [CA-20] Divergence octet ou SHA-256 pour {anchor_id} dans {ufile} (ligne {lineno}) : "
                f"extrait={actual_sha[:12]}, source={expected_sha[:12]}, balise={declared_sha[:12]}"
            )

        if g0_report is None:
            errors.append(
                f"[CA-G0-SYNC] [CA-19] Rapport aq/rapports-g0.json manquant pour valider {anchor_id} dans {ufile}"
            )
        else:
            if g0_report.get("overall_status") != "PASS" or g0_report.get("exit_code") != 0:
                errors.append(
                    f"[CA-G0-SYNC] [CA-19] aq/rapports-g0.json n'est pas au statut PASS/exit 0 pour {anchor_id}"
                )
            entry = synced_map.get(anchor_id)
            if not isinstance(entry, dict):
                errors.append(
                    f"[CA-G0-SYNC] [CA-20] Ancre {anchor_id} absente de aq/rapports-g0.json[synced_excerpts]"
                )
            else:
                if entry.get("unit") != uid:
                    errors.append(
                        f"[CA-G0-SYNC] [CA-20] Unite de {anchor_id} divergente dans rapports-g0.json : {entry.get('unit')!r} != {uid!r}"
                    )
                if entry.get("source_path") != rel_path_raw or entry.get("lines") != lines_spec or entry.get("sha256") != expected_sha:
                    errors.append(
                        f"[CA-G0-SYNC] [CA-20] Desynchronisation entre {ufile} et aq/rapports-g0.json pour {anchor_id}"
                    )

    return errors


def _check_sources_and_registries(root: Path, manifest: dict, mlr: dict) -> list[str]:
    """Controle --sources-only : CA-09, CA-10 (bases et registres), CA-11."""
    errors: list[str] = []
    reg_dir = root / "registre"
    ancres_path = reg_dir / "ancres-chronologiques.json"
    faits_path = reg_dir / "faits-empiriques.json"
    specs_lplus_path = reg_dir / "specifications-lplus.json"
    matrice_path = reg_dir / "matrice-exig-prr-c40.json"
    concordance_path = reg_dir / "concordance-taxonomies.json"
    manifeste_path = root / "recherche" / "manifeste-sources-sha256.json"
    statut_f_path = root / "recherche" / "registre-statut-f.json"

    expected_freeze = get_freeze_date(root, mlr)
    expected_freeze_fr = format_french_date(expected_freeze)
    expected_freeze_re = french_date_regex(expected_freeze)

    if not manifeste_path.is_file():
        return [f"[CA-09] Manifeste L+ manquant : {manifeste_path}"]

    try:
        manifeste = _load_json(manifeste_path)
    except json.JSONDecodeError as exc:
        return [f"[CA-09] JSON invalide dans manifeste-sources-sha256.json : {exc}"]

    if not isinstance(manifeste, dict):
        return ["[CA-09] manifeste-sources-sha256.json doit contenir un objet JSON"]

    freeze_date = str(manifeste.get("freeze_date", ""))
    if not freeze_date or parse_iso_date(freeze_date) is None or freeze_date > expected_freeze:
        errors.append(
            f"[CA-10] Date de gel invalide dans manifeste-sources-sha256.json : {freeze_date!r} (attendu <= {expected_freeze})"
        )

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
        if not _valid_date_not_after_freeze(pub_date, expected_freeze):
            errors.append(f"[CA-10] Source {sid} posterieure au gel {expected_freeze} ou date invalide : {pub_date!r}")

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
            lf_digest = compute_lf_sha256_bytes(raw_bytes)
            raw_digest = hashlib.sha256(raw_bytes).hexdigest()
            if src.get("sha256") not in {lf_digest, raw_digest}:
                errors.append(
                    f"[CA-09] Empreinte sha256 invalide pour {sid} : attendu {src.get('sha256')}, calcule {lf_digest}"
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

    # Verification des registres herites
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

    # Verification des nouveaux registres SSOT Volume 8 lorsqu'ils existent
    if specs_lplus_path.is_file():
        slp = _load_json(specs_lplus_path)
        for sp in slp.get("specs", []):
            if sp.get("statut_preuve") != "l_plus":
                errors.append(f"[CA-10] Spec L+ {sp.get('spec_id')} avec statut_preuve invalide : {sp.get('statut_preuve')!r}")
            sid_ref = str(sp.get("source_l_plus_id", ""))
            if sid_ref not in valid_l_plus_ids:
                errors.append(f"[CA-10] Spec L+ {sp.get('spec_id')} pointe vers source_l_plus_id absente : {sid_ref!r}")
    if matrice_path.is_file():
        mat = _load_json(matrice_path)
        if not mat.get("mappings"):
            errors.append("[CA-07] matrice-exig-prr-c40.json ne contient aucune entree dans mappings")
    if concordance_path.is_file():
        conc = _load_json(concordance_path)
        if len(conc.get("concordances", [])) < 5:
            errors.append("[CA-07] concordance-taxonomies.json doit contenir au moins 5 discordances DISC-01..DISC-05")

    # Verification des 5 bases fermees sources/ch00..ch04-sources.md
    narrative_units = [u for u in manifest["units"] if u["kind"] in {"frontmatter", "chapter"}]
    for u in narrative_units:
        sname = _unit_sources_filename(u["id"])
        spath = root / "sources" / sname
        if not spath.is_file():
            errors.append(f"[CA-10] Base fermee manquante : sources/{sname}")
            continue
        stext = spath.read_text(encoding="utf-8")
        if not expected_freeze_re.search(stext):
            errors.append(f"[CA-10] Date de gel '{expected_freeze_fr}' absente de sources/{sname}")
        parsed = _parse_sources_md(spath)
        if not parsed:
            errors.append(f"[CA-10] Aucune entree numerotee [n] dans sources/{sname}")
        for ref_num, sid in parsed.items():
            if not sid:
                errors.append(f"[CA-10] Entree [{ref_num}] dans sources/{sname} sans identifiant SRC-NNN")
            elif sid not in valid_l_plus_ids:
                errors.append(f"[CA-10] Reference [{ref_num}] dans sources/{sname} cite une source absente ou non-L+ : {sid}")

    return errors


def _preprocess_markdown_for_ngrams(raw: str) -> tuple[str, int]:
    """Normalise un fichier Markdown en preservant les numeros de ligne pour le comptage n-grammes."""
    body, offset = _strip_yaml_and_preserve_lines(raw)
    body = _mask_comments_and_biblio(body)
    body = _mask_fenced_code_preserving_lines(body)
    body = _MD_IMAGE_RE.sub(r"\1", body)
    body = _MD_LINK_RE.sub(r"\1", body)
    body = _AUTOLINK_RE.sub(" ", body)
    body = _BARE_URL_RE.sub(" ", body)
    return body, offset


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
            body, offset = _preprocess_markdown_for_ngrams(raw)

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
        body, offset = _preprocess_markdown_for_ngrams(text)

        def _replace_valid_quote(match: re.Match[str]) -> str:
            inner = match.group(1)
            if "\n\n" in inner:
                return match.group(0)
            inner_words = _tokenize_ngram_words(inner)
            if 1 <= len(inner_words) <= 40:
                return " §QUOTE_BREAK§ " + ("\n" * match.group(0).count("\n"))
            return match.group(0)

        filtered = _QUOTED_CITED_RE.sub(_replace_valid_quote, body)

        collisions: list[str] = []
        pow_base = pow(self.base, 11, 1 << 64)

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
            next_allowed_offset = 0
            h = 0
            zeros = sum(1 for x in seg_ids[:12] if x == 0)
            for j in range(12):
                h = (h * self.base + seg_ids[j]) & self.mod_mask
            if zeros == 0 and h in self.buckets:
                rel, clino, ctuple = self.buckets[h]
                if tuple(seg_ids[:12]) == ctuple:
                    next_allowed_offset = 12
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
                start = i - 11
                if zeros == 0 and start >= next_allowed_offset and h in self.buckets:
                    rel, clino, ctuple = self.buckets[h]
                    if tuple(seg_ids[start : i + 1]) == ctuple:
                        next_allowed_offset = start + 12
                        snippet = " ".join(seg_words[start : i + 1])
                        collisions.append(
                            f"[CA-03] Collision 12-gramme dans {unit_file} (ligne {seg_lines[start]}) "
                            f"avec {rel} (ligne {clino}) : « {snippet} »"
                        )
        return collisions


def _compile_forbidden_patterns(raw_patterns: list[str]) -> list[tuple[str, re.Pattern[str]]]:
    return compile_forbidden_patterns(raw_patterns)


def _check_ca02_unit(text: str, unit_file: str, compiled_patterns: list[tuple[str, re.Pattern[str]]]) -> list[str]:
    body, offset = _strip_yaml_and_preserve_lines(text)
    body = _mask_comments_and_biblio(body)
    body = _mask_fenced_code_preserving_lines(body)
    errors: list[str] = []

    def _check_and_mask_quote(match: re.Match[str]) -> str:
        inner = match.group(1)
        if "\n\n" in inner:
            return match.group(0)
        wc = len(_tokenize_ngram_words(inner))
        if wc > 40:
            lineno = offset + body[: match.start()].count("\n") + 1
            errors.append(
                f"[CA-02] Citation « ... » [n] depasse 40 mots ({wc} mots) dans {unit_file} (ligne {lineno})"
            )
            return match.group(0)
        return "\n" * match.group(0).count("\n")

    body = _QUOTED_CITED_RE.sub(_check_and_mask_quote, body)

    for lineno, line in enumerate(body.split("\n"), start=offset + 1):
        norm_line = normalize_quotes_spaces(line)
        for pat_str, regex in compiled_patterns:
            m = regex.search(norm_line)
            if m:
                errors.append(
                    f"[CA-02] Motif banni `{pat_str}` detecte dans {unit_file} (ligne {lineno}) : `{m.group(0)}`"
                )
    return errors


def _norm_toc_title(text: str) -> str:
    """Normalisation typographique prudente sans tronquer au ':'."""
    cleaned = normalize_quotes_spaces(text)
    cleaned = cleaned.replace("`", "").replace("**", "").replace("*", "")
    cleaned = re.sub(r"\bpass\^k\b", "passᵏ", cleaned)
    return re.sub(r"\s+", " ", cleaned).strip()


def _parse_toc_expectations(root: Path) -> dict[str, dict[str, object]]:
    """Extrait par unite les questions directrices et titres de sous-sections de specs/toc.md."""
    toc_path = root / "specs" / "toc.md"
    if not toc_path.is_file():
        return {}
    toc_text = toc_path.read_text(encoding="utf-8")
    unit_heading_re = re.compile(
        r"^(?:###\s+`00`\s+—|####\s+Chapitre\s+(\d{2})\s+—).*$",
        re.MULTILINE,
    )
    matches = list(unit_heading_re.finditer(toc_text))
    expectations: dict[str, dict[str, object]] = {}
    for idx, m in enumerate(matches):
        ch_num = m.group(1)
        uid = "00-liminaire" if ch_num is None else f"ch{ch_num}"
        start = m.end()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(toc_text)
        block = toc_text[start:end]
        m_qd = re.search(r"(?m)^-\s+\*\*Question directrice\*\*\s*:\s*(.+)$", block)
        qd = m_qd.group(1).strip() if m_qd else None
        subs = {
            sub_id: title.strip()
            for sub_id, title in re.findall(r"(?m)^-\s+\*\*(\d+\.\d+)\*\*\s+(.+)$", block)
        }
        expectations[uid] = {"qd": qd, "subs": subs}
    return expectations


def _extract_unit_qd(body: str) -> str | None:
    """Extrait le texte de l'exergue Question directrice dans le manuscrit."""
    for line in body.splitlines():
        stripped = line.strip()
        if "Question directrice" not in stripped:
            continue
        m1 = re.match(r"^\*Question directrice\s*:\s*(.+?)\*$", stripped)
        if m1 and m1.group(1).strip():
            return m1.group(1).strip()
        m2 = re.match(r"^(?:\*\*|\*)Question directrice\s*:\s*(?:\*\*|\*)\s*(.+?)\*?$", stripped)
        if m2 and m2.group(1).strip():
            return m2.group(1).strip()
    return None


def _check_ca04_unit(
    text: str,
    unit_meta: dict,
    toc_expectations: dict[str, dict[str, object]] | None = None,
) -> list[str]:
    uid = unit_meta["id"]
    ufile = unit_meta["file"]
    body, offset = _strip_yaml_and_preserve_lines(text)
    body = _mask_fenced_code_preserving_lines(body)
    lines = body.split("\n")
    errors: list[str] = []

    if not re.search(r"\*Question directrice\s*:", body):
        errors.append(f"[CA-04] Exergue `*Question directrice :*` manquant dans {ufile}")

    unit_toc = (toc_expectations or {}).get(uid, {})
    expected_qd = unit_toc.get("qd") if isinstance(unit_toc, dict) else None
    if isinstance(expected_qd, str) and expected_qd:
        found_qd = _extract_unit_qd(body)
        if found_qd is None or _norm_toc_title(found_qd) != _norm_toc_title(expected_qd):
            errors.append(f"[CA-04] Question directrice divergente de toc.md dans {ufile}")

    expected_subs = unit_toc.get("subs", {}) if isinstance(unit_toc, dict) else {}
    found_headings = {
        m.group(1): m.group(2).strip()
        for m in re.finditer(r"(?m)^#{2,4}\s+(?:\*\*)?(\d+\.\d+)(?:\*\*)?\s+(.+)$", body)
    }

    if uid == "00-liminaire":
        for sub in range(1, 7):
            sub_id = f"0.{sub}"
            if sub_id not in found_headings:
                errors.append(f"[CA-04] Sous-section {sub_id} manquante dans {ufile}")
            elif isinstance(expected_subs, dict) and sub_id in expected_subs:
                if _norm_toc_title(found_headings[sub_id]) != _norm_toc_title(expected_subs[sub_id]):
                    errors.append(
                        f"[CA-04] Sous-section {sub_id} divergente de toc.md dans {ufile} : '{found_headings[sub_id]}'"
                    )
        if not re.search(r"^>\s*\*\*Cinq critères permanents d'évaluation et de preuve exécutable\*\*", body, re.MULTILINE):
            if not re.search(r"^>\s*\*\*Cinq critères permanents", body, re.MULTILINE):
                errors.append(f"[CA-04] Encadre `> **Cinq critères permanents d'évaluation et de preuve exécutable**` manquant dans {ufile}")
    else:
        num = int(uid[2:])
        for sub in range(1, 5):
            sub_id = f"{num}.{sub}"
            if sub_id not in found_headings:
                errors.append(f"[CA-04] Sous-section {sub_id} manquante dans {ufile}")
            elif isinstance(expected_subs, dict) and sub_id in expected_subs:
                if _norm_toc_title(found_headings[sub_id]) != _norm_toc_title(expected_subs[sub_id]):
                    errors.append(
                        f"[CA-04] Sous-section {sub_id} divergente de toc.md dans {ufile} : '{found_headings[sub_id]}'"
                    )
        if not re.search(r"^>\s*\*\*Trois invariants exécutables", body, re.MULTILINE):
            errors.append(f"[CA-04] Encadre `> **Trois invariants exécutables — Chapitre {num}**` manquant dans {ufile}")

    expected_figs: list[str] = list(unit_meta.get("figures", []))
    included_figs: list[str] = []
    for lidx, line in enumerate(lines):
        for m_img in re.finditer(r"!\[([^\]]*)\]\(([^)]+)\)", line):
            m_fid = re.search(r"(Fig-\d{2})\.(?:svg|png)", m_img.group(2))
            if not m_fid:
                continue
            fid = m_fid.group(1)
            fig_num = int(fid[4:])
            included_figs.append(fid)
            caption_found = False
            checked = 0
            for j in range(lidx + 1, min(len(lines), lidx + 6)):
                nxt = lines[j].strip()
                if not nxt:
                    continue
                checked += 1
                m_cap = _CAPTION_FIG_RE.match(nxt)
                if m_cap and int(m_cap.group(1)) == fig_num:
                    caption_found = True
                    break
                if checked >= 2:
                    break
            if not caption_found:
                errors.append(
                    f"[CA-04] Legende `*Figure {fig_num} — ...*` manquante apres l'inclusion de {fid} dans {ufile} (ligne {offset + lidx + 1})"
                )

    for fid in expected_figs:
        if fid not in included_figs and not re.search(rf"\b{re.escape(fid)}\b", body):
            errors.append(f"[CA-04] Figure assignee {fid} non referencee dans {ufile}")
        elif fid not in included_figs:
            errors.append(f"[CA-04] Figure assignee {fid} sans inclusion Markdown `![...](...{fid}.svg/.png)` dans {ufile}")
    if expected_figs and included_figs != expected_figs:
        errors.append(
            f"[CA-04] Ordre ou liste d'inclusion des figures incorrect dans {ufile} : {included_figs} != {expected_figs}"
        )

    chapter_prefix = 0 if uid == "00-liminaire" else int(uid[2:])
    sep_indices = [i for i, ln in enumerate(lines) if _TABLE_SEP_RE.match(ln)]
    expected_tab_seq = 1
    for sep_idx in sep_indices:
        top = sep_idx
        while top > 0 and lines[top - 1].lstrip().startswith("|"):
            top -= 1
        bot = sep_idx
        while bot + 1 < len(lines) and lines[bot + 1].lstrip().startswith("|"):
            bot += 1

        candidate_indices = [
            j
            for j in (*range(max(0, top - 3), top), *range(bot + 1, min(len(lines), bot + 4)))
            if lines[j].strip()
        ]
        matched_tab_caption = False
        for cidx in candidate_indices:
            cand = lines[cidx].strip()
            m_bare = _CAPTION_TAB_BARE_RE.match(cand)
            if m_bare:
                errors.append(
                    f"[CA-04] Numerotation de tableau sans prefixe de chapitre dans {ufile} (ligne {offset + cidx + 1}) : Tableau {m_bare.group(1)} (attendu Tableau {chapter_prefix}.{expected_tab_seq})"
                )
                matched_tab_caption = True
                break
            m_dot = _CAPTION_TAB_DOT_RE.match(cand)
            if m_dot:
                pref, seq = int(m_dot.group(1)), int(m_dot.group(2))
                if pref != chapter_prefix or seq != expected_tab_seq:
                    errors.append(
                        f"[CA-04] Numerotation de legende Tableau {pref}.{seq} incoherente dans {ufile} (ligne {offset + cidx + 1}) : attendu Tableau {chapter_prefix}.{expected_tab_seq}"
                    )
                matched_tab_caption = True
                break
        if not matched_tab_caption:
            errors.append(
                f"[CA-04] Tableau sans legende `*Tableau {chapter_prefix}.{expected_tab_seq} — ...*` dans {ufile} (ligne {offset + sep_idx + 1})"
            )
        expected_tab_seq += 1

    return errors


def _strip_markup_for_semicolon(line: str) -> str:
    """Nettoie une ligne hors code/URLs/entites/math pour detecter un ';' sans espace devant."""
    s = _INLINE_CODE_RE.sub(" ", line)
    s = _INLINE_MATH_RE.sub(" ", s)
    s = _MD_IMAGE_RE.sub(r"\1", s)
    s = _MD_LINK_RE.sub(r"\1", s)
    s = _AUTOLINK_RE.sub(" ", s)
    s = _BARE_URL_RE.sub(" ", s)
    s = _HTML_ENTITY_RE.sub(" ", s)
    return s


def _check_ca05_unit(text: str, unit_meta: dict, wb: dict, strict: bool = True) -> list[str]:
    uid = unit_meta["id"]
    ufile = unit_meta["file"]
    body, offset = _strip_yaml_and_preserve_lines(text)
    body = _mask_comments_and_biblio(body)
    body = _mask_fenced_code_preserving_lines(body)
    lines = body.split("\n")

    table_count = sum(1 for line in lines if _TABLE_SEP_RE.match(line))
    errors: list[str] = []
    if uid == "00-liminaire":
        if table_count != 1:
            errors.append(f"[CA-05] Le liminaire doit contenir exactement 1 tableau (trouve : {table_count})")
    else:
        max_tables = int(wb.get("max_tables_per_chapter", 3))
        if table_count > max_tables:
            errors.append(f"[CA-05] Trop de tableaux dans {ufile} : {table_count} > {max_tables}")

    non_empty = [line for line in lines if line.strip()]
    if non_empty:
        list_count = sum(
            1
            for line in non_empty
            if not line.lstrip().startswith((">", "|")) and _LIST_LINE_RE.match(line)
        )
        ratio = list_count / len(non_empty)
        max_ratio = float(wb.get("max_bullet_line_ratio", 0.25))
        if ratio > max_ratio:
            errors.append(
                f"[CA-05] Ratio de lignes en puces/listes excessif dans {ufile} : {ratio:.1%} > {max_ratio:.0%}"
            )

    if strict:
        for lineno, line in enumerate(lines, start=offset + 1):
            stripped = line.lstrip()
            if not stripped or stripped.startswith("|") or _TABLE_SEP_RE.match(line):
                continue
            cleaned_line = _strip_markup_for_semicolon(line)
            m_semi = re.search(r"\S;", cleaned_line)
            if m_semi:
                errors.append(
                    f"[CA-05] Espace manquant avant ';' dans {ufile} (ligne {lineno}) : `{cleaned_line.strip()[:100]}`"
                )

        for block in re.split(r"\n\s*\n", body):
            stripped = block.strip()
            if not stripped:
                continue
            if stripped.startswith("#") or is_markdown_table_block(stripped):
                continue
            if stripped.startswith("![") and stripped.endswith(")"):
                continue
            if _CAPTION_FIG_RE.match(stripped) or _CAPTION_TAB_DOT_RE.match(stripped) or _CAPTION_TAB_BARE_RE.match(stripped):
                continue

            block_lines = [ln.strip() for ln in stripped.splitlines() if ln.strip()]
            is_list_or_callout_block = all(ln.startswith(">") or bool(_LIST_LINE_RE.match(ln)) for ln in block_lines)
            if not is_list_or_callout_block:
                para_wc = count_prose_words(stripped)
                if para_wc > 180:
                    errors.append(
                        f"[CA-05] Paragraphe trop long dans {ufile} : {para_wc} mots > 180 mots ({stripped[:80]}...)"
                    )

            sent_chunks: list[str] = []
            cur_para: list[str] = []
            for ln in block_lines:
                if ln.startswith("|"):
                    continue
                clean_ln = re.sub(r"^>\s*", "", ln)
                if _LIST_LINE_RE.match(clean_ln):
                    if cur_para:
                        sent_chunks.append(" ".join(cur_para))
                        cur_para = []
                    sent_chunks.append(_LIST_LINE_RE.sub("", clean_ln, count=1))
                else:
                    cur_para.append(clean_ln)
            if cur_para:
                sent_chunks.append(" ".join(cur_para))

            for chunk in sent_chunks:
                prose_for_sent = _DECIMAL_DOT_RE.sub("\u2024", chunk)
                for sent in split_sentences(prose_for_sent):
                    restored = sent.replace("\u2024", ".")
                    sent_wc = count_prose_words(restored)
                    if sent_wc > 70:
                        errors.append(
                            f"[CA-05] Phrase trop longue dans {ufile} : {sent_wc} mots > 70 mots ({restored[:90]}...)"
                        )

    return errors


def _check_sequential_delimiters(text: str, open_tok: str, close_tok: str, unit_file: str, label: str) -> list[str]:
    """Verifie l'appariement sequentiel (ordre, non-imbrication, fermeture) de delimiteurs."""
    errors: list[str] = []
    pat = re.compile(re.escape(open_tok) + "|" + re.escape(close_tok))
    depth = 0
    open_line = 0
    for m in pat.finditer(text):
        tok = m.group(0)
        lineno = text[: m.start()].count("\n") + 1
        if tok == open_tok:
            if depth > 0:
                errors.append(
                    f"[CA-06] Delimiteur {label} imbrique dans {unit_file} (ligne {lineno}, deja ouvert ligne {open_line})"
                )
            else:
                depth = 1
                open_line = lineno
        else:
            if depth == 0:
                errors.append(f"[CA-06] Fermeture {close_tok} inattendue sans {open_tok} dans {unit_file} (ligne {lineno})")
            else:
                depth = 0
    if depth > 0:
        errors.append(f"[CA-06] Delimiteur {label} non ferme dans {unit_file} (ouvert ligne {open_line})")
    return errors


def _is_forbidden_prose_backtick(inner: str) -> bool:
    s = inner.strip()
    if _FORBIDDEN_PROSE_BACKTICK_RE.match(s):
        return True
    words = s.split()
    if len(words) >= 4 and not re.search(r'[{}=()<>/":._]', s):
        return True
    return False


def _check_ca06_unit(text: str, unit_file: str, check_narrative_style: bool = True) -> list[str]:
    body, offset = _strip_yaml_and_preserve_lines(text)
    body = _mask_comments_and_biblio(body)
    body = _mask_fenced_code_preserving_lines(body)
    errors: list[str] = []

    no_inline_lines: list[str] = []
    for lineno, line in enumerate(body.split("\n"), start=offset + 1):
        if _UNESCAPED_DOLLAR_RE.search(line):
            errors.append(
                f"[CA-06] Symbole $ non echappe dans {unit_file} (ligne {lineno}) : {line.strip()}"
            )

        if check_narrative_style:
            for m_bt in _INLINE_CODE_RE.finditer(line):
                inner = m_bt.group(0).strip("`")
                if _is_forbidden_prose_backtick(inner):
                    errors.append(
                        f"[CA-06] Backticks interdits sur sigle ou prose courante `{inner}` dans {unit_file} (ligne {lineno})"
                    )

        clean_line = _INLINE_CODE_RE.sub("", line)
        no_inline_lines.append(clean_line)

        if check_narrative_style:
            if _BARE_URL_RE.search(clean_line) or re.search(r"\]\(\s*(?:https?|ftp)://", clean_line):
                errors.append(
                    f"[CA-06] Lien externe brut non autorise dans le corps narratif de {unit_file} (ligne {lineno})"
                )

    full_clean = "\n" * offset + "\n".join(no_inline_lines)
    errors.extend(_check_sequential_delimiters(full_clean, r"\(", r"\)", unit_file, r"\(...\)"))
    errors.extend(_check_sequential_delimiters(full_clean, r"\[", r"\]", unit_file, r"\[...\]"))
    return errors


def _check_ca10_unit(text: str, unit_meta: dict, root: Path) -> list[str]:
    uid = unit_meta["id"]
    ufile = unit_meta["file"]
    sname = _unit_sources_filename(uid)
    spath = root / "sources" / sname
    if not spath.is_file():
        return [f"[CA-10] Base fermee manquante pour {uid} : sources/{sname}"]

    src_map = _parse_sources_md(spath)
    valid_refs = set(src_map.keys())
    body, offset = _strip_yaml_and_preserve_lines(text)
    body = _mask_comments_and_biblio(body)
    body = _mask_fenced_code_preserving_lines(body)
    body = _INLINE_CODE_RE.sub("", body)
    body = _MD_IMAGE_RE.sub("", body)
    body = _MD_LINK_RE.sub(r"\1", body)

    errors: list[str] = []
    for ref_num, sid in sorted(src_map.items()):
        if sid is None:
            errors.append(
                f"[CA-10] Entree [{ref_num}] dans sources/{sname} sans identifiant SRC-NNN"
            )

    cited_refs: set[int] = set()
    for lineno, line in enumerate(body.split("\n"), start=offset + 1):
        for m in _CITATION_REF_RE.finditer(line):
            for part in m.group(1).split(","):
                ref_num = int(part.strip())
                cited_refs.add(ref_num)
                if ref_num not in valid_refs:
                    errors.append(
                        f"[CA-10] Renvoi orphelin [{ref_num}] dans {ufile} (ligne {lineno}) absent de sources/{sname}"
                    )
    if not cited_refs:
        errors.append(f"[CA-10] Aucun renvoi source [n] dans {ufile}")

    unused = sorted(valid_refs - cited_refs)
    if unused:
        errors.append(
            f"[CA-10] Sources declarees dans sources/{sname} jamais citees dans {ufile} : {unused}"
        )
    return errors


def _extract_dates_from_text(text: str) -> tuple[set[str], set[str]]:
    """Extrait (dates exactes YYYY-MM-DD, mois-annee YYYY-MM) des formulations francaises ou ISO."""
    exact: set[str] = set()
    ym: set[str] = set()
    for m in _ISO_DATE_RE.finditer(text):
        iso = f"{m.group(1)}-{m.group(2)}-{m.group(3)}"
        exact.add(iso)
        ym.add(iso[:7])
    for m in _ISO_MONTH_RE.finditer(text):
        ym.add(f"{m.group(1)}-{m.group(2)}")
    for m in _FRENCH_DATE_RE.finditer(text):
        day = int(m.group(1))
        month = _FRENCH_MONTHS.get(m.group(2).lower())
        year = int(m.group(3))
        if month:
            iso = f"{year:04d}-{month:02d}-{day:02d}"
            exact.add(iso)
            ym.add(iso[:7])
    for m in _FRENCH_MONTH_YEAR_RE.finditer(text):
        month = _FRENCH_MONTHS.get(m.group(1).lower())
        year = int(m.group(2))
        if month:
            ym.add(f"{year:04d}-{month:02d}")
    return exact, ym


def _extract_iso_dates_from_text(text: str) -> set[str]:
    return _extract_dates_from_text(text)[0]


def _extract_numbers(text: str) -> set[float]:
    cleaned = _SECTION_REF_RE.sub(" ", text).replace("{,}", ",")
    cleaned = re.sub(r"\b(?:Fig|SRC|CA|AO|RQ|DISC|EXIG|CAP|ADR|POR)-\d+\b", " ", cleaned)
    nums: set[float] = set()
    for m in _NUMBER_RE.finditer(cleaned):
        raw = m.group(0).replace(" ", "").replace("\u00a0", "").replace("\u202f", "").replace(",", ".")
        try:
            nums.add(float(raw))
        except ValueError:
            continue
    return nums


def _extract_pcts(text: str) -> set[float]:
    cleaned = text.replace("{,}", ",")
    return {
        float(m.replace(" ", "").replace("\u00a0", "").replace("\u202f", "").replace(",", "."))
        for m in re.findall(r"(\d+(?:[ \u00a0\u202f]?\d{3})*(?:[.,]\d+)?)\s*%", cleaned)
    }


def _split_top_level_value(text: str) -> str:
    return re.sub(r"\([^)]*\)", " ", text)


def _anchor_matches_sentence(anchor_key: str, sent_lower: str) -> bool:
    if anchor_key == "2026-08-02-EU-AI-ACT-ART50":
        return "ai act" in sent_lower and ("article 50" in sent_lower or "art. 50" in sent_lower)
    if anchor_key == "2026-LOI25-ART12-1":
        return "loi 25" in sent_lower and ("12.1" in sent_lower or "automatis" in sent_lower)
    if anchor_key == "2027-03-15-TLS-100J":
        return ("tls" in sent_lower or "certificat" in sent_lower) and "100 jours" in sent_lower
    if anchor_key == "2027-03-30-MCP-SEP-3398":
        return "sep-3398" in sent_lower and ("mcp" in sent_lower or "révision" in sent_lower)
    if anchor_key == "2027-05-01-BSIF-E23-AMF":
        return "e-23" in sent_lower or ("amf" in sent_lower and "ligne directrice" in sent_lower)
    if anchor_key == "2027-07-28-MCP-MIGRATION":
        return "2026-07-28" in sent_lower and "migration" in sent_lower
    if anchor_key == "2027-12-02-EU-AI-ACT-ANNEXE-III":
        return "ai act" in sent_lower and "annexe iii" in sent_lower
    if anchor_key == "2028-08-02-EU-AI-ACT-ANNEXE-I":
        return "ai act" in sent_lower and bool(re.search(r"\bannexe i\b", sent_lower))
    if anchor_key == "2029-03-15-TLS-47J":
        return ("tls" in sent_lower or "certificat" in sent_lower) and "47 jours" in sent_lower
    if anchor_key == "2030-2035-G7-PQC-FINANCE":
        return ("g7" in sent_lower and "post-quantique" in sent_lower) or "ir 8547" in sent_lower
    return False


def _fact_matches_sentence(fact_id: str, sent_lower: str) -> tuple[bool, bool]:
    """Retourne (correspond_au_fait, requiert_verification_stricte_chiffres)."""
    if fact_id == "FACT-MCP-DRIFT-4058":
        return (("8 900" in sent_lower or "mcp" in sent_lower) and "dérive silencieuse" in sent_lower and "%" in sent_lower), True
    if fact_id == "FACT-MAP-STUDY":
        return (("étude map" in sent_lower or "pan et al" in sent_lower) and "%" in sent_lower), True
    if fact_id == "FACT-MAST-FAILURES":
        return ("mast" in sent_lower and "%" in sent_lower), True
    if fact_id in {"FACT-CAMEL-AGENTDOJO", "FACT-CAMEL-RESIDUAL"}:
        return (
            "camel" in sent_lower
            and (bool(re.search(r"\bagentdojo\b", sent_lower)) or "trifecta" in sent_lower)
            and "%" in sent_lower
        ), True
    if fact_id == "FACT-PQC-SIGNATURE-SIZE":
        return (("ml-dsa-65" in sent_lower or "ml-dsa-87" in sent_lower) and "octet" in sent_lower), True
    if fact_id == "FACT-WILSON-3P":
        return ("wilson" in sent_lower and "3/p" in sent_lower and "%" in sent_lower), True
    return False, False


def _critical_fact_requirements(fact: dict) -> list[tuple[float, ...]]:
    val_str = str(fact.get("value", ""))
    metric_str = str(fact.get("metric", ""))
    val_pcts = _extract_pcts(val_str)
    top_nums = _extract_numbers(_split_top_level_value(val_str))

    groups: list[tuple[float, ...]] = []
    seen: set[float] = set()
    for p in sorted(val_pcts):
        groups.append((p,))
        seen.add(p)
    for n in sorted(top_nums):
        if n not in seen:
            groups.append((n,))
            seen.add(n)
    if not groups:
        for n in sorted(_extract_numbers(val_str + " " + metric_str)):
            groups.append((n,))
    return groups


def _missing_fact_groups(
    req_groups: list[tuple[float, ...]],
    target_nums: set[float],
    target_pcts: set[float] | None = None,
    pct_values: set[float] | None = None,
) -> list[str]:
    missing: list[str] = []
    pct_set = pct_values or set()
    for aliases in req_groups:
        pool = target_pcts if (target_pcts is not None and any(a in pct_set for a in aliases)) else target_nums
        ok = any(a in pool for a in aliases)
        if not ok:
            missing.append("/".join(str(int(a) if a.is_integer() else a) for a in aliases))
    return missing


def _check_ca07_registries(root: Path, unit_texts: dict[str, str], check_global_presence: bool) -> list[str]:
    """Controle la concordance exacte avec registre/*.json (herites + SSOT Vol. 8)."""
    errors: list[str] = []
    ancres = _load_json(root / "registre" / "ancres-chronologiques.json").get("anchors", [])
    faits = _load_json(root / "registre" / "faits-empiriques.json").get("facts", [])
    glossaire_path = root / "registre" / "glossaire-termes.json"
    glossaire_terms = _load_json(glossaire_path).get("terms", []) if glossaire_path.is_file() else []

    if check_global_presence:
        for anchor in ancres:
            akey = anchor["key"]
            adate = str(anchor["date"])
            joined = "\n".join(unit_texts.get(ch, "") for ch in anchor["chapters"])
            found_exact, found_ym = _extract_dates_from_text(joined)
            if re.match(r"^\d{4}-\d{2}-\d{2}$", adate):
                if adate not in found_exact:
                    errors.append(
                        f"[CA-07] Date de l'ancre {akey} ({adate}) absente de ses chapitres {anchor['chapters']}"
                    )
            elif re.match(r"^\d{4}-\d{2}$", adate):
                if adate not in found_ym:
                    errors.append(
                        f"[CA-07] Mois/annee de l'ancre {akey} ({adate}) absent de ses chapitres {anchor['chapters']}"
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
            owner_nums = _extract_numbers(owner_text)
            owner_pcts = _extract_pcts(owner_text)
            req_groups = _critical_fact_requirements(fact)
            val_pcts = _extract_pcts(str(fact.get("value", "")))
            missing = _missing_fact_groups(
                req_groups, owner_nums, target_pcts=owner_pcts, pct_values=val_pcts
            )
            if missing:
                errors.append(
                    f"[CA-07] Valeurs critiques du fait {fact['id']} ({missing}) absentes du chapitre proprietaire {owner}"
                )

    norm_unit_texts = {uid: _norm_toc_title(raw).lower() for uid, raw in unit_texts.items()}
    for term in glossaire_terms:
        owner = term.get("chapitre_proprietaire")
        fr_head = str(term.get("fr", "")).strip()
        if owner in norm_unit_texts and fr_head:
            if _norm_toc_title(fr_head).lower() not in norm_unit_texts[owner]:
                errors.append(
                    f"[CA-07] Vedette du glossaire '{fr_head}' absente de son chapitre proprietaire {owner}"
                )

    exact_anchors = {a["key"]: a for a in ancres if re.match(r"^\d{4}-\d{2}-\d{2}$", str(a["date"]))}
    month_anchors = {a["key"]: a for a in ancres if re.match(r"^\d{4}-\d{2}$", str(a["date"]))}
    for uid, raw_text in unit_texts.items():
        body, _ = _strip_yaml_and_preserve_lines(raw_text)
        body = _mask_comments_and_biblio(body)
        body = _mask_fenced_code_preserving_lines(body)
        sentences: list[str] = []
        for raw_line in body.split("\n"):
            if not raw_line.strip():
                continue
            protected_line = _DECIMAL_DOT_RE.sub("\u2024", raw_line)
            for s in split_sentences(protected_line):
                restored = s.replace("\u2024", ".").strip()
                if restored:
                    sentences.append(restored)

        for sent in sentences:
            sent_lower = sent.lower()
            sent_exact, sent_ym = _extract_dates_from_text(sent)
            if sent_exact or sent_ym:
                matched_anchors = [a for a in ancres if _anchor_matches_sentence(a["key"], sent_lower)]
                expected_exact_in_sent = {str(a["date"]) for a in matched_anchors if a["key"] in exact_anchors}
                expected_ym_in_sent = {
                    str(a["date"])[:7] for a in matched_anchors if a["key"] in exact_anchors or a["key"] in month_anchors
                }
                is_publication_ref = any(
                    k in sent_lower for k in ("publié", "bulletin", "avis ", "rapport ", "modifié le", "modifiant")
                )
                is_effective_claim = any(
                    k in sent_lower
                    for k in ("vigueur", "appliqu", "applicab", "échéance", "à compter", "effecti", "attendue")
                )
                for a in matched_anchors:
                    ak = a["key"]
                    adate = str(a["date"])
                    if ak in exact_anchors:
                        if sent_exact and adate not in sent_exact:
                            other_exact = expected_exact_in_sent - {adate}
                            if not (sent_exact <= other_exact):
                                errors.append(
                                    f"[CA-07] Divergence de date pour l'ancre {ak} dans {uid} : "
                                    f"trouve {sorted(sent_exact)}, attendu {adate}"
                                )
                        elif not sent_exact and sent_ym and is_effective_claim and not is_publication_ref and adate[:7] not in sent_ym:
                            other_ym = expected_ym_in_sent - {adate[:7]}
                            if not (sent_ym <= other_ym):
                                errors.append(
                                    f"[CA-07] Divergence mois/annee pour l'ancre {ak} dans {uid} : "
                                    f"trouve {sorted(sent_ym)}, attendu {adate[:7]}"
                                )
                    elif ak in month_anchors and sent_ym and (is_effective_claim or not is_publication_ref) and adate not in sent_ym:
                        other_ym = expected_ym_in_sent - {adate}
                        if not (sent_ym <= other_ym):
                            errors.append(
                                f"[CA-07] Divergence mois/annee pour l'ancre {ak} dans {uid} : "
                                f"trouve {sorted(sent_ym)}, attendu {adate}"
                            )

            for fact in faits:
                matched, strict_num = _fact_matches_sentence(fact["id"], sent_lower)
                if not matched or not strict_num:
                    continue
                val_str = fact["value"]
                fid = fact["id"]
                val_pcts = _extract_pcts(val_str)
                sent_pcts = _extract_pcts(sent)
                val_nums = _extract_numbers(val_str)
                sent_nums = _extract_numbers(sent)

                if fid in {"FACT-CAMEL-AGENTDOJO", "FACT-CAMEL-RESIDUAL"}:
                    if 77.0 not in sent_pcts or ("sans défense" in sent_lower and 84.0 not in sent_pcts):
                        errors.append(
                            f"[CA-07] Divergence de pourcentage pour {fid} dans {uid} : attendu 77 % et 84 %, trouve {sorted(sent_pcts)} %"
                        )
                elif fid == "FACT-MCP-DRIFT-4058":
                    if 40.58 not in sent_pcts:
                        errors.append(
                            f"[CA-07] Divergence derive MCP ({fid}) dans {uid} : attendu 40,58 %, trouve {sorted(sent_pcts)} %"
                        )
                elif fid == "FACT-MAST-FAILURES":
                    if "41" in sent_lower and (41.0 not in sent_pcts or 86.7 not in sent_pcts):
                        errors.append(
                            f"[CA-07] Divergence fourchette MAST ({fid}) dans {uid} : attendu 41 % a 86,7 %, trouve {sorted(sent_pcts)} %"
                        )
                    elif not (val_pcts & sent_pcts):
                        errors.append(
                            f"[CA-07] Divergence de pourcentage pour {fid} dans {uid} : attendu {sorted(val_pcts)} %, trouve {sorted(sent_pcts)} %"
                        )
                elif fid == "FACT-PQC-SIGNATURE-SIZE":
                    if "ml-dsa-65" in sent_lower and 3309.0 not in sent_nums:
                        errors.append(f"[CA-07] Divergence ML-DSA-65 dans {uid} : attendu 3 309 octets")
                    elif "ml-dsa-87" in sent_lower and 4627.0 not in sent_nums:
                        errors.append(f"[CA-07] Divergence ML-DSA-87 dans {uid} : attendu 4 627 octets")
                elif val_pcts and sent_pcts:
                    if not (val_pcts & sent_pcts):
                        errors.append(
                            f"[CA-07] Divergence de pourcentage pour {fid} dans {uid} : "
                            f"attendu {sorted(val_pcts)} %, trouve {sorted(sent_pcts)} % (extrait : {sent[:120]})"
                        )
                else:
                    top_expected = _extract_numbers(_split_top_level_value(val_str)) or val_nums
                    if top_expected and not (top_expected <= sent_nums):
                        errors.append(
                            f"[CA-07] Divergence chiffree pour {fid} dans {uid} : "
                            f"attendu {val_str} (extrait : {sent[:120]})"
                        )

    return errors


def _check_ca08_figures(root: Path, manifest: dict, strict: bool = True) -> list[str]:
    from compile_figures import validate_render, validate_sources

    figures, errors = validate_sources(root, strict=strict)
    diag_dir = root / "diagrammes"
    rendus_dir = diag_dir / "rendus"
    for fmeta in figures:
        fid = fmeta["id"]
        engine = fmeta["engine"]
        src_ext = "puml" if engine == "puml" else "mmd"
        rnd_ext = "svg" if engine == "puml" else "png"
        src_path = diag_dir / f"{fid}.{src_ext}"
        out_path = rendus_dir / f"{fid}.{rnd_ext}"
        for err in validate_render(out_path, engine, source_path=src_path):
            errors.append(err if err.startswith("[CA-") else f"[CA-08] {err}")
    return [err if err.startswith("[CA-") else f"[CA-08] {err}" for err in errors]


def _check_ca17_annexes(root: Path) -> list[str]:
    from genere_annexes import build_annexes

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


def _has_valid_pdf(candidates: tuple[Path, ...]) -> bool:
    for path in candidates:
        if path.is_file():
            with path.open("rb") as fh:
                if fh.read(5) == b"%PDF-":
                    return True
    return False


class _DeliverableHtmlParser(HTMLParser):
    """Analyse structurelle du livrable HTML autonome (Annexe A / Bibliographie)."""

    def __init__(self) -> None:
        super().__init__()
        self.img_srcs: list[str] = []
        self.figcaption_count = 0
        self.external_deps: list[str] = []
        self.annexe_bib_links: list[str] = []
        self._in_heading = False
        self._heading_buf: list[str] = []
        self._in_annexe_bib = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr_map = {k.lower(): (v or "") for k, v in attrs}
        t = tag.lower()
        el_id = attr_map.get("id", "").lower()
        if t in {"h1", "h2", "h3"}:
            self._in_heading = True
            self._heading_buf = []
            if el_id.startswith(("annexe-a", "bibliographie-class")):
                self._in_annexe_bib = True
            elif el_id.startswith("annexe-b"):
                self._in_annexe_bib = False
        if t == "figcaption":
            self.figcaption_count += 1
        elif t == "img":
            src = attr_map.get("src", "")
            self.img_srcs.append(src)
            if src.startswith(("http://", "https://")):
                self.external_deps.append(f"<img src={src}>")
        elif t == "script":
            src = attr_map.get("src", "")
            if src.startswith(("http://", "https://")):
                self.external_deps.append(f"<script src={src}>")
        elif t == "link":
            href = attr_map.get("href", "")
            if href.startswith(("http://", "https://")):
                self.external_deps.append(f"<link href={href}>")
        elif t == "a" and self._in_annexe_bib:
            href = attr_map.get("href", "")
            if href.startswith(("http://", "https://")):
                self.annexe_bib_links.append(href)

    def handle_data(self, data: str) -> None:
        if self._in_heading:
            self._heading_buf.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() in {"h1", "h2", "h3"} and self._in_heading:
            self._in_heading = False
            heading = re.sub(r"\s+", " ", "".join(self._heading_buf)).strip()
            if "Annexe A" in heading or "Bibliographie classée" in heading:
                self._in_annexe_bib = True
            elif "Annexe B" in heading:
                self._in_annexe_bib = False


def _check_g0_report(root: Path) -> list[str]:
    errors: list[str] = []
    g0_path = root / "aq" / "rapports-g0.json"
    if not g0_path.is_file():
        return [f"[CA-19] Rapport G0 manquant : {g0_path}"]
    try:
        g0 = _load_json(g0_path)
    except json.JSONDecodeError as exc:
        return [f"[CA-19] aq/rapports-g0.json invalide : {exc}"]
    if not isinstance(g0, dict):
        return ["[CA-19] aq/rapports-g0.json doit contenir un objet JSON"]

    if g0.get("overall_status") != "PASS" or g0.get("exit_code") != 0:
        errors.append(
            f"[CA-19] Barriere G0 non validee dans aq/rapports-g0.json : status={g0.get('overall_status')!r}, exit_code={g0.get('exit_code')!r}"
        )
    if not g0.get("spdx_check", {}).get("passed"):
        errors.append("[CA-19] Controle SPDX MIT en echec dans aq/rapports-g0.json")
    if not g0.get("lockfile_check", {}).get("passed"):
        errors.append("[CA-19] Controle requirements.lock en echec dans aq/rapports-g0.json")
    if not g0.get("schema_validation", {}).get("passed"):
        errors.append("[CA-19] Validation JSON Schema 2020-12 en echec dans aq/rapports-g0.json")

    opa = g0.get("opa_check", {})
    if opa.get("coverage_pct") != 100.0 or opa.get("tests_failed", 1) != 0 or opa.get("missing_default_deny"):
        errors.append(f"[CA-19] Controle OPA / Rego insuffisant dans aq/rapports-g0.json : {opa}")

    pyt = g0.get("pytest_check", {})
    if pyt.get("failed", 1) != 0 or pyt.get("skipped", 1) != 0 or pyt.get("passed", 0) < 1:
        errors.append(f"[CA-19] Controle pytest G0 invalide dans aq/rapports-g0.json : {pyt}")

    vecs = g0.get("third_party_vectors", {})
    for suite in ("rfc8785", "nist_acvp", "a2a_tck", "owasp_src055"):
        if not vecs.get(suite, {}).get("passed"):
            errors.append(f"[CA-19] Suite vecteurs tiers '{suite}' non validee dans aq/rapports-g0.json")

    return errors


def _check_deliverables(root: Path, manifest: dict) -> list[str]:
    from assemble_livre import _resolve_deliverable_paths, build_consolidated_markdown

    errors: list[str] = []
    narrative_units = [u for u in manifest["units"] if u["kind"] in {"frontmatter", "chapter"}]
    fig_count = len(manifest.get("figures", []))

    # CA-19 : aq/rapports-g0.json
    errors.extend(_check_g0_report(root))

    # CA-12 : ancrage/ch00..ch04-ancrage.md (100 % supportes, 0 non supporte)
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

    # CA-13 & CA-14 : recollations G3 (graines depuis manifest.json : 20270801 / 20270802)
    seeds_cfg = manifest.get("g3_seeds", {"pass1": 20270801, "pass2": 20270802})
    seed1 = str(seeds_cfg.get("pass1", 20270801))
    seed2 = str(seeds_cfg.get("pass2", 20270802))
    seed3 = str(int(seed2) + 1)

    s1_locs: set[str] = set()
    s1_paras: set[str] = set()
    for seed, code, required in ((seed1, "CA-13", True), (seed2, "CA-14", True), (seed3, "CA-14", False)):
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
            errors.append(
                f"[{code}] {jpath.name} doit contenir 60 items (trouve : {len(items) if isinstance(items, list) else 'invalide'})"
            )
            continue
        locs = {str(it.get("claim_loc", "")) for it in items}
        paras = {str(it.get("paragraph_loc", "")) for it in items}
        if seed == seed1:
            s1_locs, s1_paras = locs, paras
        elif seed == seed2:
            if not locs.isdisjoint(s1_locs) or not paras.isdisjoint(s1_paras):
                errors.append(f"[CA-14] Chevauchement detecte entre recollation {seed1} et {seed2}")
        md_txt = mpath.read_text(encoding="utf-8")
        if "60/60" not in md_txt and "60 / 60" not in md_txt:
            errors.append(f"[{code}] Score final 60/60 absent de {mpath.name}")

    # CA-15 & CA-16 : gauntlet et lissage/visuel
    glog = root / "aq" / "gauntlet-log.md"
    if not glog.is_file() or glog.stat().st_size == 0:
        errors.append("[CA-15] Journal aq/gauntlet-log.md manquant ou vide")
    rvis = root / "aq" / "rapport-lissage-et-visuel.md"
    if not rvis.is_file() or rvis.stat().st_size == 0:
        errors.append("[CA-16] Rapport aq/rapport-lissage-et-visuel.md manquant ou vide")

    # CA-18 : Livrables consolides et HTML autonome
    root = Path(root) if Path(root).is_absolute() and Path(root).name else Path(root).resolve()
    consolidated_md, consolidated_pdf, html_out, expected_prefix = _resolve_deliverable_paths(root, manifest)
    html_name = html_out.name
    md_name = consolidated_md.name
    pdf_name = consolidated_pdf.name
    liv_dir = html_out.parent

    if liv_dir.is_dir():
        unexpected_files = sorted(p.name for p in liv_dir.iterdir() if p.name != html_name)
        if unexpected_files:
            errors.append(
                f"[CA-18] livrables/ ne doit contenir que {html_name} ; fichiers interdits/residuels detectes : {unexpected_files}"
            )

    manifeste_path = root / "recherche" / "manifeste-sources-sha256.json"
    has_open_sources = False
    if manifeste_path.is_file():
        try:
            mdata = _load_json(manifeste_path)
            has_open_sources = bool(isinstance(mdata, dict) and mdata.get("sources"))
        except json.JSONDecodeError:
            has_open_sources = False

    if not consolidated_md.is_file() or consolidated_md.stat().st_size == 0:
        errors.append(f"[CA-18] Livrable Markdown consolide manquant : ../0 - PDF-MD/{md_name}")
    else:
        md_actual = consolidated_md.read_text(encoding="utf-8").replace("\r\n", "\n")
        try:
            md_expected, _, _ = build_consolidated_markdown(root, image_prefix=expected_prefix)
            if md_actual.rstrip() != md_expected.replace("\r\n", "\n").rstrip():
                errors.append(
                    f"[CA-18] ../0 - PDF-MD/{md_name} desynchronise de l'assemblage du manuscrit"
                )
        except Exception as exc:
            errors.append(f"[CA-18] Impossible de comparer {md_name} a l'assemblage : {exc}")

        fig_matches = re.findall(r"!\[[^\]]*\]\(([^)]+)\)", md_actual)
        expected_figs = [f["id"] for f in manifest.get("figures", [])]
        expected_ext = {f["id"]: ("svg" if f["engine"] == "puml" else "png") for f in manifest.get("figures", [])}
        if len(fig_matches) != fig_count:
            errors.append(f"[CA-18] {md_name} doit referencer {fig_count} images (trouve : {len(fig_matches)})")
        else:
            seen_fids: list[str] = []
            for raw_img in fig_matches:
                m_fid = re.search(r"(Fig-\d{2})\.(svg|png)$", raw_img.strip())
                if not m_fid or not raw_img.strip().startswith(f"{expected_prefix.rstrip('/')}/"):
                    errors.append(f"[CA-18] Chemin d'image invalide dans {md_name} : {raw_img}")
                    continue
                fid, ext = m_fid.group(1), m_fid.group(2)
                seen_fids.append(fid)
                if expected_ext.get(fid) != ext:
                    errors.append(f"[CA-18] Extension inattendue pour {fid} dans {md_name} : .{ext}")
                resolved_img = (consolidated_md.parent / raw_img.strip()).resolve()
                if not resolved_img.is_file():
                    errors.append(f"[CA-18] Image introuvable depuis {md_name} : {raw_img} -> {resolved_img}")
            if seen_fids != expected_figs:
                errors.append(f"[CA-18] Ordre des {fig_count} figures dans {md_name} divergent : {seen_fids}")

    if not html_out.is_file():
        errors.append(f"[CA-18] Livrable HTML autonome manquant : livrables/{html_name}")
    else:
        html_txt = html_out.read_text(encoding="utf-8", errors="replace")
        if "<html" not in html_txt:
            errors.append(f"[CA-18] Livrable HTML invalide (balise <html> absente) : livrables/{html_name}")
        else:
            parser = _DeliverableHtmlParser()
            parser.feed(html_txt)
            base64_imgs = [s for s in parser.img_srcs if s.startswith("data:image/") and "base64," in s]
            if len(parser.img_srcs) != fig_count or len(base64_imgs) != fig_count:
                errors.append(
                    f"[CA-18] HTML doit contenir {fig_count} <img> base64 (trouve {len(parser.img_srcs)} img, {len(base64_imgs)} base64)"
                )
            if parser.figcaption_count != 0:
                errors.append(
                    f"[CA-18] HTML contient {parser.figcaption_count} balise(s) <figcaption> dupliquee(s) (attendu 0)"
                )
            if parser.external_deps:
                errors.append(
                    f"[CA-18] HTML non autonome (dependances HTTP externes) : {parser.external_deps[:5]}"
                )
            if has_open_sources and not parser.annexe_bib_links:
                errors.append("[CA-18] Aucun hyperlien cliquable (<a href=...>) en Annexe A du HTML")

    if not _has_valid_pdf((consolidated_pdf,)):
        errors.append(f"[CA-18] Livrable PDF consolide manquant ou invalide : ../0 - PDF-MD/{pdf_name}")
    else:
        try:
            with pymupdf.open(consolidated_pdf) as doc:
                if doc.page_count <= 20:
                    errors.append(f"[CA-18] PDF trop court ({doc.page_count} pages <= 20) : {consolidated_pdf}")
                annexe_uris: list[str] = []
                in_annexe_bib = False
                for pno in range(doc.page_count):
                    page = doc[pno]
                    ptext = page.get_text("text")
                    if "Annexe A" in ptext or "Bibliographie classée" in ptext:
                        in_annexe_bib = True
                    if in_annexe_bib:
                        for lnk in page.get_links():
                            uri = str(lnk.get("uri", ""))
                            if uri.startswith(("http://", "https://")):
                                annexe_uris.append(uri)
                    m_bad = re.search(r"\\\$|\$[0-9][^\n$]{0,20}\$|\\\(|\\\)|Syntax Error", ptext)
                    if m_bad:
                        errors.append(
                            f"[CA-18] Artifice LaTeX/Typst ou erreur dans PDF p.{pno + 1} : {m_bad.group(0)!r}"
                        )
                if has_open_sources and not annexe_uris:
                    errors.append("[CA-18] Aucun lien /URI cliquable detecte en Annexe A du PDF")
        except Exception as exc:
            errors.append(f"[CA-18] Echec lecture PDF via pymupdf ({consolidated_pdf}) : {exc}")

    return errors


def check_manuscrit(
    root: Path,
    strict: bool = True,
    sources_only: bool = False,
    unit_id: str | None = None,
    check_deliverables: bool = False,
) -> list[str]:
    """Execute les verifications deterministes du manuscrit selon le mode demande."""
    root = Path(root) if Path(root).is_absolute() and Path(root).name else Path(root).resolve()
    manifest = _load_json(root / "specs" / "manifest.json")
    mlr = _load_json(root / "specs" / "protocole-mlr-2027.json")

    if sources_only:
        return _check_sources_and_registries(root, manifest, mlr)

    errors: list[str] = []
    wb = manifest["word_budget"]
    units = manifest["units"]
    compiled_forbidden = _compile_forbidden_patterns(manifest["forbidden_prose_regexes"])
    toc_expectations = _parse_toc_expectations(root)

    g0_path = root / "aq" / "rapports-g0.json"
    g0_report: dict | None = None
    if g0_path.is_file():
        try:
            loaded_g0 = _load_json(g0_path)
            if isinstance(loaded_g0, dict):
                g0_report = loaded_g0
        except json.JSONDecodeError:
            g0_report = None

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

        is_narrative = u["kind"] in {"frontmatter", "chapter"}
        errors.extend(_check_ca06_unit(text, ufile, check_narrative_style=is_narrative))
        errors.extend(_check_ca_g0_sync(root, text, u, g0_report))

        if is_narrative:
            errors.extend(_check_ca02_unit(text, ufile, compiled_forbidden))
            errors.extend(corpus_index.find_collisions(text, ufile))
            errors.extend(_check_ca04_unit(text, u, toc_expectations=toc_expectations))
            errors.extend(_check_ca05_unit(text, u, wb, strict=strict))
            errors.extend(_check_ca10_unit(text, u, root))

    if unit_id is None:
        if strict:
            if total_words < wb["total_min"] or total_words > wb["total_max"]:
                errors.append(
                    f"[CA-01] Volume total hors plage : {total_words} mots (attendu [{wb['total_min']}, {wb['total_max']}])"
                )
            errors.extend(_check_ca08_figures(root, manifest, strict=strict))
            errors.extend(_check_ca17_annexes(root))
        errors.extend(_check_ca07_registries(root, unit_texts, check_global_presence=strict))
    else:
        errors.extend(_check_ca07_registries(root, unit_texts, check_global_presence=False))

    if check_deliverables:
        errors.extend(_check_deliverables(root, manifest))

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Verificateur deterministe G1 du Volume 8 (8 - Manuel).")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent, help="Racine du manuel")
    parser.add_argument("--strict", action="store_true", help="Verification complete stricte (defaut)")
    parser.add_argument("--sources-only", action="store_true", help="Verifier uniquement corpus L+, SHA-256 et bases sources")
    parser.add_argument("--unit", type=str, default=None, help="Verifier une unite specifique (ex. ch01, 00-liminaire)")
    parser.add_argument("--check-deliverables", action="store_true", help="Verifier aussi aq/rapports-g0.json, ancrage/, aq/ et livrables/")
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
