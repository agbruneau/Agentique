#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Collecte scientifique et technique ouverte L+ (protocole MLR Compendium) et verification SHA-256."""

from __future__ import annotations

import argparse
import hashlib
import io
import json
import re
import ssl
import sys
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
import zipfile
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

import lxml.html
import pymupdf

_TOOLS_DIR = Path(__file__).resolve().parent
if str(_TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(_TOOLS_DIR))

try:
    from _communs import DEFAULT_FREEZE_DATE, compute_lf_sha256_bytes, get_freeze_date, parse_iso_date
except ImportError:
    DEFAULT_FREEZE_DATE = "2026-12-02"

    def compute_lf_sha256_bytes(data: bytes) -> str:
        """Calcule le SHA-256 hexadecimale apres normalisation CRLF -> LF."""
        return hashlib.sha256(data.replace(b"\r\n", b"\n")).hexdigest()

    def parse_iso_date(date_str: str) -> tuple[int, int, int] | None:
        """Analyse une date YYYY-MM-DD valide ou retourne None."""
        m = re.match(r"^(\d{4})-(\d{2})-(\d{2})$", (date_str or "").strip())
        if not m:
            return None
        try:
            parsed = date.fromisoformat(m.group(0))
        except ValueError:
            return None
        return parsed.year, parsed.month, parsed.day

    def get_freeze_date(book_dir: Path | None = None, mlr_data: dict | None = None) -> str:
        """Lit dynamiquement freeze_date depuis specs/protocole-mlr-compendium.json."""
        data = mlr_data
        if data is None and book_dir is not None:
            for fname in ("protocole-mlr-compendium.json", "protocole-mlr-2027.json"):
                mlr_path = Path(book_dir) / "specs" / fname
                if mlr_path.is_file():
                    try:
                        loaded = json.loads(mlr_path.read_text(encoding="utf-8"))
                        if isinstance(loaded, dict):
                            data = loaded
                            break
                    except (OSError, ValueError):
                        data = None
        if isinstance(data, dict):
            raw = data.get("freeze_date")
            if isinstance(raw, str) and parse_iso_date(raw) is not None:
                return raw.strip()
        return DEFAULT_FREEZE_DATE


USER_AGENT = "Compendium2027-MLR-Collector/1.0 (Open-Access Engineering Research; https://github.com/agbruneau/Agentique)"
SEC_USER_AGENT = "Compendium2027Research research@agentique-compendium2027.invalid"

DEFAULT_PROTOCOL_ID = "MLR-PRISMA-SCR-COMPENDIUM-2027-V1.0"

BLOCKED_HTTP_CODES = {401, 403, 429, 451}
_UNPINNED_GIT_REFS = {"", "head", "main", "master", "latest", "default"}
_SHA256_HEX_RE = re.compile(r"^[0-9a-f]{64}$")
_SRC_ENTRY_HEAD_RE = re.compile(r"^(?:#{1,4}|[-*+])?\s*\[(\d+)\](?:\s+(SRC-\d+))?", re.MULTILINE)

WAF_CHALLENGE_PATTERNS = (
    "cf-turnstile",
    "challenges.cloudflare.com",
    "attention required! | cloudflare",
    "enable javascript and cookies to continue",
    "just a moment...",
    "making sure you're not a bot",
    "anubis",
    "proof-of-work",
    "cf-mitigated",
    "g-recaptcha",
    "hcaptcha.com",
    "bot detection",
    "access denied",
)

SHORT_PAGE_PAYWALL_PATTERNS = (
    "subscribe to continue reading",
    "sign in to read",
    "purchase this article",
    "institutional login",
    "verify you are human",
    "this content is for subscribers",
    "buy this article",
    "create a free account to continue",
    "already a subscriber",
)


@dataclass
class HttpResponse:
    """Reponse HTTP normalisee compatible avec les clients simulables en tests."""

    status_code: int
    content: bytes
    text: str
    headers: dict[str, str]
    url: str


class StdlibHttpClient:
    """Client HTTP base sur urllib.request (sans contournement ni reessai sur blocage)."""

    def __init__(self) -> None:
        self._ssl_ctx = ssl.create_default_context()

    def get(self, url: str, headers: dict[str, str] | None = None, timeout: int = 30) -> HttpResponse:
        req = urllib.request.Request(url, headers=headers or {}, method="GET")
        try:
            with urllib.request.urlopen(req, context=self._ssl_ctx, timeout=timeout) as resp:
                raw = resp.read()
                hdrs = {k: v for k, v in resp.headers.items()}
                charset = resp.headers.get_content_charset() or "utf-8"
                return HttpResponse(
                    status_code=int(resp.status),
                    content=raw,
                    text=raw.decode(charset, errors="replace"),
                    headers=hdrs,
                    url=resp.geturl(),
                )
        except urllib.error.HTTPError as err:
            raw = b""
            try:
                raw = err.read()
            except Exception:
                pass
            hdrs = {k: v for k, v in (err.headers.items() if err.headers else [])}
            return HttpResponse(
                status_code=int(err.code),
                content=raw,
                text=raw.decode("utf-8", errors="replace"),
                headers=hdrs,
                url=err.geturl() or url,
            )


def compute_sha256_bytes(data: bytes) -> str:
    """Calcule l'empreinte SHA-256 hexadecimale exacte d'un tampon binaire."""
    return hashlib.sha256(data).hexdigest()


def compute_sha256_file(path: Path) -> str:
    """Calcule l'empreinte SHA-256 hexadecimale exacte d'un fichier sur disque."""
    return compute_sha256_bytes(path.read_bytes())


def normalize_text(text: str) -> str:
    """Normalise les fins de lignes et espaces superflus en UTF-8 sans BOM."""
    text = text.lstrip("\ufeff").replace("\r\n", "\n").replace("\r", "\n").replace("\x00", "")
    lines = [re.sub(r"[ \t]+", " ", line).strip() for line in text.split("\n")]
    cleaned = "\n".join(lines)
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned).strip()
    return f"{cleaned}\n" if cleaned else ""


def _extract_html_text(content: bytes | str) -> str:
    """Extrait le texte lisible d'un document HTML/XHTML en preservant les sauts de bloc."""
    if isinstance(content, bytes):
        decoded = content.decode("utf-8", errors="replace")
    else:
        decoded = content
    clean_str = re.sub(r"^\s*<\?xml[^>]*\?>", "", decoded, count=1)
    doc = lxml.html.fromstring(clean_str)
    for bad in doc.xpath("//script|//style|//noscript|//svg|//iframe|//template"):
        bad.drop_tree()

    root = doc
    mains = doc.xpath("//main") or doc.xpath("//article") or doc.xpath("//body")
    if mains:
        candidate = mains[0]
        if len(candidate.text_content().split()) >= 40:
            root = candidate
        else:
            bodies = doc.xpath("//body")
            if bodies:
                root = bodies[0]

    block_tags = {
        "p",
        "div",
        "section",
        "article",
        "li",
        "tr",
        "h1",
        "h2",
        "h3",
        "h4",
        "h5",
        "h6",
        "blockquote",
        "pre",
        "br",
        "hr",
        "dt",
        "dd",
    }
    chunks: list[str] = []

    def walk(node: lxml.html.HtmlElement) -> None:
        tag = node.tag.lower() if isinstance(node.tag, str) else ""
        if tag in block_tags:
            chunks.append("\n")
        if node.text:
            chunks.append(node.text)
        for child in node:
            walk(child)
            if child.tail:
                chunks.append(child.tail)
        if tag in block_tags:
            chunks.append("\n")
        elif tag in {"td", "th", "span", "a", "strong", "em", "code"}:
            chunks.append(" ")

    walk(root)
    return normalize_text("".join(chunks))


def extract_text_from_bytes(content: bytes, content_type: str = "", url: str = "") -> str:
    """Extrait le texte integral UTF-8 depuis PDF, HTML, XHTML, ZIP (CSV), XML ou texte brut."""
    ct_low = (content_type or "").lower()
    url_low = (url or "").lower()

    is_pdf = "application/pdf" in ct_low or content.lstrip().startswith(b"%PDF-") or url_low.endswith(".pdf")
    if is_pdf:
        doc = pymupdf.open(stream=content, filetype="pdf")
        try:
            pages = [page.get_text("text") for page in doc]
        finally:
            doc.close()
        return normalize_text("\n\n".join(pages))

    is_zip = "application/zip" in ct_low or content[:4] == b"PK\x03\x04" or url_low.endswith(".zip")
    if is_zip:
        parts: list[str] = []
        with zipfile.ZipFile(io.BytesIO(content)) as zf:
            for name in sorted(zf.namelist()):
                if name.lower().endswith((".csv", ".txt", ".md")):
                    raw_member = zf.read(name).decode("utf-8-sig", errors="replace")
                    parts.append(f"=== {name} ===\n{raw_member}")
        return normalize_text("\n\n".join(parts))

    decoded = content.decode("utf-8", errors="replace")
    head_low = decoded[:4096].lower()
    is_html = (
        "html" in ct_low
        or "<html" in head_low
        or "<!doctype html" in head_low
        or "<ix:header" in head_low
    )
    if is_html:
        return _extract_html_text(content)

    if "xml" in ct_low and not url_low.endswith(".txt"):
        root = ET.fromstring(decoded)
        return normalize_text("\n".join(t for t in root.itertext() if t and t.strip()))

    return normalize_text(decoded)


_UNMISTAKABLE_WAF_MARKERS = (
    "cf-turnstile",
    "challenges.cloudflare.com",
    "attention required! | cloudflare",
    "enable javascript and cookies to continue",
    "making sure you're not a bot",
    "just a moment...",
    "g-recaptcha",
    "hcaptcha.com",
    "cf-mitigated",
)


def _visible_html_word_count(html_text: str) -> int:
    cleaned = re.sub(
        r"<(?:script|style|noscript)\b[^>]*>[\s\S]*?</(?:script|style|noscript)>",
        " ",
        html_text,
        flags=re.IGNORECASE,
    )
    cleaned = re.sub(r"<[^>]+>", " ", cleaned)
    return len(re.findall(r"[A-Za-zÀ-ÿ0-9]{2,}", cleaned))


def _detect_block_reason(status_code: int, headers: dict[str, Any], content: bytes, text_preview: str) -> str | None:
    """Detecte tout blocage HTTP, WAF, CAPTCHA, PoW Anubis ou mur payant (AO-01)."""
    if status_code in BLOCKED_HTTP_CODES:
        return f"HTTP_{status_code}"
    if status_code == 202:
        low_preview = text_preview.lower()
        if any(tok in low_preview for tok in ("anubis", "proof-of-work", "bot", "challenge", "wait")):
            return "HTTP_202_POW_CHALLENGE"
        return "HTTP_202_NON_FINAL"
    if status_code >= 400 or status_code == 0:
        return f"HTTP_{status_code}"

    headers_low = {str(k).lower(): str(v).lower() for k, v in (headers or {}).items()}
    if "challenge" in headers_low.get("cf-mitigated", ""):
        return "CLOUDFLARE_CHALLENGE_HEADER"

    if content.lstrip().startswith(b"%PDF-"):
        return None

    head_low = text_preview[:8192].lower()
    low_html = text_preview.lower()
    visible_words: int | None = None

    def _is_sparse_shell() -> bool:
        nonlocal visible_words
        if visible_words is None:
            visible_words = _visible_html_word_count(text_preview)
        return visible_words < 400

    for pat in WAF_CHALLENGE_PATTERNS:
        if pat in _UNMISTAKABLE_WAF_MARKERS and pat in low_html:
            return f"WAF_OR_CHALLENGE:{pat}"
        if pat in head_low and _is_sparse_shell():
            return f"WAF_OR_CHALLENGE:{pat}"
        if pat in low_html and _is_sparse_shell():
            return f"WAF_OR_CHALLENGE:{pat}"

    if _is_sparse_shell():
        for pat in SHORT_PAGE_PAYWALL_PATTERNS:
            if pat in low_html:
                return f"PAYWALL_OR_AUTH:{pat}"

    return None


def fetch_open_source(
    url: str,
    client: Any = None,
    timeout: int = 30,
    headers: dict[str, str] | None = None,
) -> dict[str, Any]:
    """Effectue exactement UNE requete HTTP GET conforme a AO-01 (zero contournement)."""
    req_headers = {"User-Agent": SEC_USER_AGENT if "sec.gov" in url.lower() else USER_AGENT}
    if headers:
        req_headers.update(headers)

    http_client = client if client is not None else StdlibHttpClient()

    try:
        resp = http_client.get(url, headers=req_headers, timeout=timeout)
    except Exception as exc:
        return {
            "url": url,
            "status": "F",
            "included_in_evidence": False,
            "http_status": None,
            "block_reason": f"NETWORK_ERROR:{type(exc).__name__}",
            "checked_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        }

    status_code = int(getattr(resp, "status_code", 0))
    resp_headers = dict(getattr(resp, "headers", {}) or {})
    raw_content = getattr(resp, "content", b"")
    if not raw_content and getattr(resp, "text", ""):
        raw_content = str(resp.text).encode("utf-8")

    preview = raw_content[:262144].decode("utf-8", errors="replace") if raw_content else str(getattr(resp, "text", ""))
    block_reason = _detect_block_reason(status_code, resp_headers, raw_content, preview)
    if block_reason is not None:
        return {
            "url": url,
            "final_url": str(getattr(resp, "url", url)),
            "status": "F",
            "included_in_evidence": False,
            "http_status": status_code,
            "block_reason": block_reason,
            "checked_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        }

    content_type = resp_headers.get("Content-Type", resp_headers.get("content-type", ""))
    try:
        extracted = extract_text_from_bytes(raw_content, content_type=content_type, url=str(getattr(resp, "url", url)))
    except Exception as exc:
        return {
            "url": url,
            "final_url": str(getattr(resp, "url", url)),
            "status": "F",
            "included_in_evidence": False,
            "http_status": status_code,
            "block_reason": f"EXTRACTION_ERROR:{type(exc).__name__}",
            "checked_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        }

    if len(extracted.split()) < 30:
        return {
            "url": url,
            "final_url": str(getattr(resp, "url", url)),
            "status": "F",
            "included_in_evidence": False,
            "http_status": status_code,
            "block_reason": "INSUFFICIENT_OR_EMPTY_TEXT",
            "checked_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        }

    encoded = extracted.encode("utf-8")
    return {
        "url": url,
        "final_url": str(getattr(resp, "url", url)),
        "status": "L+",
        "included_in_evidence": True,
        "metadata_only": False,
        "http_status": status_code,
        "content_type": content_type,
        "text": extracted,
        "sha256": compute_sha256_bytes(encoded),
        "byte_length": len(encoded),
        "word_count": len(extracted.split()),
        "checked_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }


def _build_pinned_git_raw_url(repo_url: str, ref_or_commit: str, rel_path: str) -> str:
    """Construit l'URL brute d'un fichier dans un depot Git epingle par tag ou commit."""
    clean_repo = repo_url.strip().rstrip("/")
    if clean_repo.endswith(".git"):
        clean_repo = clean_repo[:-4]
    parsed = urllib.parse.urlparse(clean_repo)
    clean_rel = rel_path.strip().lstrip("/")
    if not clean_rel or ".." in Path(clean_rel).parts:
        raise ValueError(f"Chemin relatif de specification Git invalide : {rel_path!r}")

    host = parsed.netloc.lower()
    path_parts = [p for p in parsed.path.split("/") if p]
    if host in {"github.com", "raw.githubusercontent.com"} and len(path_parts) >= 2:
        owner, repo = path_parts[0], path_parts[1]
        return f"https://raw.githubusercontent.com/{owner}/{repo}/{ref_or_commit}/{clean_rel}"
    if "gitlab" in host and len(path_parts) >= 2:
        return f"{parsed.scheme}://{parsed.netloc}/{'/'.join(path_parts)}/-/raw/{ref_or_commit}/{clean_rel}"
    return f"{clean_repo}/{ref_or_commit}/{clean_rel}"


def fetch_pinned_git_spec(
    repo_url: str,
    ref_or_commit: str,
    rel_path: str,
    expected_sha256: str,
    client: Any = None,
    timeout: int = 30,
) -> dict[str, Any]:
    """Moissonne une specification Git epinglee sous garde AO-01 (1 requete) et verifie son SHA-256."""
    ref = (ref_or_commit or "").strip()
    if ref.lower() in _UNPINNED_GIT_REFS:
        raise ValueError(f"Reference Git non epinglee interdite : {ref_or_commit!r}")

    exp_hash = (expected_sha256 or "").strip().lower()
    if not _SHA256_HEX_RE.fullmatch(exp_hash):
        raise ValueError(f"Empreinte expected_sha256 invalide (64 hex attendus) : {expected_sha256!r}")

    raw_url = _build_pinned_git_raw_url(repo_url, ref, rel_path)
    http_client = client if client is not None else StdlibHttpClient()
    req_headers = {"User-Agent": USER_AGENT}
    checked_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    try:
        resp = http_client.get(raw_url, headers=req_headers, timeout=timeout)
    except Exception as exc:
        return {
            "url": raw_url,
            "repo_url": repo_url,
            "ref_or_commit": ref,
            "rel_path": rel_path.lstrip("/"),
            "status": "F",
            "included_in_evidence": False,
            "http_status": None,
            "block_reason": f"NETWORK_ERROR:{type(exc).__name__}",
            "checked_at": checked_at,
        }

    status_code = int(getattr(resp, "status_code", 0))
    resp_headers = dict(getattr(resp, "headers", {}) or {})
    raw_content = getattr(resp, "content", b"")
    if not raw_content and getattr(resp, "text", ""):
        raw_content = str(resp.text).encode("utf-8")

    preview = raw_content[:65536].decode("utf-8", errors="replace") if raw_content else str(getattr(resp, "text", ""))
    block_reason = _detect_block_reason(status_code, resp_headers, raw_content, preview)
    if block_reason is not None:
        return {
            "url": raw_url,
            "final_url": str(getattr(resp, "url", raw_url)),
            "repo_url": repo_url,
            "ref_or_commit": ref,
            "rel_path": rel_path.lstrip("/"),
            "status": "F",
            "included_in_evidence": False,
            "http_status": status_code,
            "block_reason": block_reason,
            "checked_at": checked_at,
        }

    if not raw_content:
        return {
            "url": raw_url,
            "final_url": str(getattr(resp, "url", raw_url)),
            "repo_url": repo_url,
            "ref_or_commit": ref,
            "rel_path": rel_path.lstrip("/"),
            "status": "F",
            "included_in_evidence": False,
            "http_status": status_code,
            "block_reason": "EMPTY_GIT_SPEC",
            "checked_at": checked_at,
        }

    raw_sha = compute_sha256_bytes(raw_content)
    lf_sha = compute_lf_sha256_bytes(raw_content)
    if raw_sha == exp_hash:
        verified_sha = raw_sha
    elif lf_sha == exp_hash:
        verified_sha = lf_sha
    else:
        return {
            "url": raw_url,
            "final_url": str(getattr(resp, "url", raw_url)),
            "repo_url": repo_url,
            "ref_or_commit": ref,
            "rel_path": rel_path.lstrip("/"),
            "status": "F",
            "included_in_evidence": False,
            "http_status": status_code,
            "block_reason": f"SHA256_MISMATCH:expected={exp_hash},actual={raw_sha}",
            "expected_sha256": exp_hash,
            "actual_sha256": raw_sha,
            "checked_at": checked_at,
        }

    text = raw_content.decode("utf-8", errors="replace").replace("\r\n", "\n").replace("\r", "\n")
    return {
        "url": raw_url,
        "final_url": str(getattr(resp, "url", raw_url)),
        "repo_url": repo_url,
        "ref_or_commit": ref,
        "rel_path": rel_path.lstrip("/"),
        "status": "L+",
        "included_in_evidence": True,
        "metadata_only": False,
        "http_status": status_code,
        "text": text,
        "sha256": verified_sha,
        "byte_length": len(raw_content),
        "word_count": len(text.split()),
        "checked_at": checked_at,
    }


def write_corpus_source(corpus_dir: Path, source_id: str, text: str) -> dict[str, Any]:
    """Ecrit le texte integral UTF-8 sans BOM (LF) sur disque et retourne ses empreintes."""
    corpus_dir.mkdir(parents=True, exist_ok=True)
    out_path = corpus_dir / f"{source_id}.txt"
    norm_text = text.lstrip("\ufeff").replace("\r\n", "\n").replace("\r", "\n")
    payload = norm_text.encode("utf-8")
    out_path.write_bytes(payload)
    return {
        "source_id": source_id,
        "path": out_path,
        "sha256": compute_sha256_bytes(payload),
        "byte_length": len(payload),
        "word_count": len(norm_text.split()),
    }


def _validate_publication_date(pub_date: str, freeze_date: str, source_id: str) -> None:
    """Valide une date YYYY-MM-DD, YYYY-MM ou YYYY et verifie qu'elle <= freeze_date."""
    cleaned = pub_date.strip()
    if not re.fullmatch(r"\d{4}(?:-\d{2}(?:-\d{2})?)?", cleaned):
        raise ValueError(f"Format de publication_date invalide pour {source_id} : {pub_date}")
    padded = f"{cleaned}-01-01" if len(cleaned) == 4 else (f"{cleaned}-01" if len(cleaned) == 7 else cleaned)
    if parse_iso_date(padded) is None:
        raise ValueError(f"Date de publication invalide pour {source_id} : {pub_date}")
    if padded > freeze_date:
        raise ValueError(f"Source {source_id} posterieure a la date de gel {freeze_date} : {pub_date}")


def build_manifest_payload(
    sources: list[dict[str, Any]],
    protocol_id: str = DEFAULT_PROTOCOL_ID,
    freeze_date: str = DEFAULT_FREEZE_DATE,
) -> dict[str, Any]:
    """Construit le manifeste probatoire SHA-256 en imposant 0 % METADATA_ONLY et gel des faits."""
    required_keys = {
        "source_id",
        "category",
        "peer_reviewed",
        "title",
        "authors",
        "year",
        "publication_date",
        "venue_or_issuer",
        "identifier",
        "url",
        "status",
        "metadata_only",
        "aacods_score",
        "research_axes",
        "local_txt_path",
        "sha256",
        "byte_length",
        "word_count",
    }
    validated: list[dict[str, Any]] = []
    seen_ids: set[str] = set()
    for src in sources:
        missing = required_keys - set(src.keys())
        if missing:
            raise ValueError(f"Champs manquants dans {src.get('source_id', '?')} : {sorted(missing)}")
        sid = str(src["source_id"])
        if sid in seen_ids:
            raise ValueError(f"source_id duplique : {sid}")
        seen_ids.add(sid)

        if src["status"] != "L+":
            raise ValueError(f"Source {sid} exclue : statut {src['status']} interdit (seul L+ permis)")
        if src["metadata_only"] is not False:
            raise ValueError(f"Source {sid} viole 0 % METADATA_ONLY")
        _validate_publication_date(str(src["publication_date"]), freeze_date, sid)
        validated.append(src)

    metadata_only_count = sum(1 for s in validated if s["metadata_only"])
    pct = 0.0 if not validated else round((metadata_only_count / len(validated)) * 100.0, 4)

    return {
        "protocol_id": protocol_id,
        "freeze_date": freeze_date,
        "metadata_only_pct": pct,
        "sources": validated,
    }


def _resolve_protocol_path(book_dir: Path) -> Path | None:
    for fname in ("protocole-mlr-compendium.json", "protocole-mlr-2027.json"):
        cand = book_dir / "specs" / fname
        if cand.is_file():
            return cand
    return None


def verify_manifest_integrity(book_dir: Path) -> list[str]:
    """Verifie integralement le manifeste SHA-256, les fichiers .txt et les seuils D01..D12 / RQ."""
    errors: list[str] = []
    manifest_path = book_dir / "recherche" / "manifeste-sources-sha256.json"
    proto_path = _resolve_protocol_path(book_dir)

    if not manifest_path.is_file():
        return [f"Manifeste introuvable : {manifest_path}"]
    if proto_path is None:
        return [f"Protocole MLR introuvable dans {book_dir / 'specs'}"]

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    proto = json.loads(proto_path.read_text(encoding="utf-8"))

    expected_freeze = get_freeze_date(book_dir, proto)
    freeze_date = manifest.get("freeze_date", expected_freeze)
    if freeze_date > expected_freeze:
        errors.append(f"Date de gel invalide dans manifeste : {freeze_date}")
    if manifest.get("metadata_only_pct") != 0.0:
        errors.append(f"metadata_only_pct doit valoir 0.0, trouve : {manifest.get('metadata_only_pct')}")

    rq_counts: dict[str, int] = {rq["id"]: 0 for rq in proto.get("research_questions_and_queries", [])}
    seen_ids: set[str] = set()
    seen_sha: dict[str, str] = {}

    for src in manifest.get("sources", []):
        sid = src.get("source_id", "?")
        if sid in seen_ids:
            errors.append(f"source_id duplique dans manifeste : {sid}")
        seen_ids.add(sid)

        if src.get("status") != "L+":
            errors.append(f"Source {sid} non L+ dans le manifeste : {src.get('status')}")
        if src.get("metadata_only") is not False:
            errors.append(f"Source {sid} marquee metadata_only=True")
        pub_date = str(src.get("publication_date", ""))
        try:
            _validate_publication_date(pub_date, freeze_date, sid)
        except ValueError as exc:
            errors.append(str(exc))

        rel_txt = src.get("local_txt_path", "")
        txt_path = book_dir / rel_txt
        if not txt_path.is_file():
            errors.append(f"Fichier texte manquant pour {sid} : {txt_path}")
        else:
            raw = txt_path.read_bytes()
            if raw.startswith(b"\xef\xbb\xbf"):
                errors.append(f"BOM UTF-8 interdit pour {sid} : {txt_path}")
            if b"\r" in raw:
                errors.append(f"Fin de ligne CR/CRLF interdite pour {sid} : {txt_path}")
            actual_sha = compute_lf_sha256_bytes(raw)
            raw_sha = compute_sha256_bytes(raw)
            if src.get("sha256") not in {actual_sha, raw_sha}:
                errors.append(f"Empreinte SHA-256 divergente pour {sid} : attendu {src.get('sha256')}, lu {actual_sha}")
            if actual_sha in seen_sha and seen_sha[actual_sha] != sid:
                errors.append(f"Doublon SHA-256 entre {seen_sha[actual_sha]} et {sid}")
            seen_sha[actual_sha] = sid
            norm_len = len(raw.replace(b"\r\n", b"\n"))
            if src.get("byte_length") not in {len(raw), norm_len}:
                errors.append(f"Taille en octets divergente pour {sid} : attendu {src.get('byte_length')}, lu {norm_len}")

        for rq in src.get("research_axes", []):
            if rq in rq_counts:
                rq_counts[rq] += 1

    for rq in proto.get("research_questions_and_queries", []):
        rq_id = rq["id"]
        min_req = int(rq["min_included_studies"])
        if rq_counts.get(rq_id, 0) < min_req:
            errors.append(f"Axe {rq_id} sous le seuil min_included_studies ({rq_counts.get(rq_id, 0)} < {min_req})")

    return errors


def verify_compendium_evidence(book_dir: Path) -> list[str]:
    """Controle complet AO-01, AO-02, 7 registres SSOT et 37 bases fermees sources/ch00..ch36-sources.md."""
    errors = verify_manifest_integrity(book_dir)

    manifest_path = book_dir / "recherche" / "manifeste-sources-sha256.json"
    statut_f_path = book_dir / "recherche" / "registre-statut-f.json"
    if not manifest_path.is_file():
        return errors

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    valid_ids = {
        str(s["source_id"])
        for s in manifest.get("sources", [])
        if s.get("status") == "L+" and s.get("metadata_only") is False
    }
    lplus_urls = {str(s.get("url", "")) for s in manifest.get("sources", []) if s.get("url")}

    if not statut_f_path.is_file():
        errors.append(f"[CA-10] Registre statut F manquant : {statut_f_path}")
    else:
        try:
            sf_data = json.loads(statut_f_path.read_text(encoding="utf-8"))
            for item in sf_data.get("blocked", []):
                if item.get("status") != "F" or item.get("included_in_evidence") is not False:
                    errors.append(f"[AO-01] Entree statut F invalide : {item.get('url')}")
                if item.get("url") and item["url"] in lplus_urls:
                    errors.append(f"[AO-01] URL bloquee incluse dans le manifeste L+ : {item['url']}")
        except json.JSONDecodeError as exc:
            errors.append(f"[CA-10] JSON invalide dans registre-statut-f.json : {exc}")

    reg_dir = book_dir / "registre"
    expected_regs = (
        "mindmap-complet.json",
        "specifications-lplus.json",
        "matrice-exig-prr-c40.json",
        "concordance-taxonomies.json",
        "ancres-chronologiques.json",
        "faits-empiriques.json",
        "glossaire-termes.json",
    )
    for rname in expected_regs:
        rpath = reg_dir / rname
        if not rpath.is_file():
            errors.append(f"[CA-07] Registre SSOT manquant : {rpath}")
            continue
        try:
            data = json.loads(rpath.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"[CA-07] JSON invalide dans {rname} : {exc}")
            continue

        if rname in {"ancres-chronologiques.json", "faits-empiriques.json", "specifications-lplus.json", "glossaire-termes.json"}:
            key = {"ancres-chronologiques.json": "anchors", "faits-empiriques.json": "facts", "specifications-lplus.json": "specs", "glossaire-termes.json": "terms"}[rname]
            for entry in data.get(key, []):
                eid = entry.get("id", entry.get("key", entry.get("spec_id", entry.get("fr", "?"))))
                if entry.get("statut_preuve") != "l_plus":
                    errors.append(f"[AO-02] [CA-10] Entree {eid} dans {rname} non reancree L+ : {entry.get('statut_preuve')!r}")
                lref = entry.get("source_l_plus_id")
                if not lref:
                    errors.append(f"[AO-02] [CA-10] Entree {eid} dans {rname} sans source_l_plus_id")
                else:
                    refs = re.findall(r"SRC-\d+", str(lref)) or [str(lref)]
                    missing = [r for r in refs if r not in valid_ids]
                    if missing:
                        errors.append(f"[AO-02] [CA-10] Entree {eid} dans {rname} pointe vers source absente : {missing}")

    sources_dir = book_dir / "sources"
    for idx in range(37):
        spath = sources_dir / f"ch{idx:02d}-sources.md"
        if not spath.is_file():
            errors.append(f"[CA-10] Base fermee manquante : sources/ch{idx:02d}-sources.md")
            continue
        raw = spath.read_bytes()
        if raw.startswith(b"\xef\xbb\xbf"):
            errors.append(f"[CA-22] BOM UTF-8 interdit dans sources/{spath.name}")
        if b"\r" in raw:
            errors.append(f"[CA-22] Fin de ligne CR/CRLF interdite dans sources/{spath.name}")
        stext = raw.decode("utf-8", errors="replace")
        if not re.search(r"\b2\s+d[ée]cembre\s+2026\b", stext, re.IGNORECASE):
            errors.append(f"[CA-10] Date de gel '2 décembre 2026' absente de sources/{spath.name}")
        heads = _SRC_ENTRY_HEAD_RE.findall(stext)
        if not heads:
            errors.append(f"[CA-10] Aucune entree [n] SRC-XXX dans sources/{spath.name}")
        for num, sid in heads:
            if not sid:
                errors.append(f"[CA-10] Entree [{num}] sans SRC-XXX dans sources/{spath.name}")
            elif sid not in valid_ids:
                errors.append(f"[CA-10] Reference [{num}] -> {sid} absente du manifeste L+ dans sources/{spath.name}")

    return errors


# --- Connecteurs d'API ouvertes ---


def _api_get_json(url: str, params: dict[str, Any] | None = None, timeout: int = 25) -> tuple[int, dict[str, Any] | None]:
    full_url = f"{url}?{urllib.parse.urlencode(params)}" if params else url
    client = StdlibHttpClient()
    resp = client.get(full_url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"}, timeout=timeout)
    if resp.status_code in BLOCKED_HTTP_CODES or resp.status_code >= 400:
        return resp.status_code, None
    try:
        return resp.status_code, json.loads(resp.text)
    except json.JSONDecodeError:
        return resp.status_code, None


def search_arxiv(query: str, max_results: int = 10, timeout: int = 25) -> tuple[int, list[dict[str, Any]]]:
    """Interroge l'API ouverte export.arxiv.org."""
    params = urllib.parse.urlencode(
        {"search_query": query, "start": 0, "max_results": max_results, "sortBy": "relevance"}
    )
    url = f"https://export.arxiv.org/api/query?{params}"
    resp = StdlibHttpClient().get(url, headers={"User-Agent": USER_AGENT}, timeout=timeout)
    if resp.status_code in BLOCKED_HTTP_CODES or resp.status_code >= 400:
        return resp.status_code, []
    try:
        root = ET.fromstring(resp.text)
    except ET.ParseError:
        return resp.status_code, []
    ns = {"atom": "http://www.w3.org/2005/Atom"}
    out: list[dict[str, Any]] = []
    for entry in root.findall("atom:entry", ns):
        id_text = (entry.findtext("atom:id", "", ns) or "").strip()
        arxiv_id = id_text.rsplit("/abs/", 1)[-1].split("v")[0]
        title = re.sub(r"\s+", " ", (entry.findtext("atom:title", "", ns) or "").strip())
        published = (entry.findtext("atom:published", "", ns) or "")[:10]
        authors = ", ".join((a.findtext("atom:name", "", ns) or "").strip() for a in entry.findall("atom:author", ns))
        out.append(
            {
                "identifier": f"arXiv:{arxiv_id}",
                "title": title,
                "authors": authors,
                "publication_date": published,
                "pdf_url": f"https://arxiv.org/pdf/{arxiv_id}",
                "abs_url": f"https://arxiv.org/abs/{arxiv_id}",
            }
        )
    return resp.status_code, out


def search_crossref_oa(
    query: str,
    rows: int = 10,
    timeout: int = 25,
    freeze_date: str = DEFAULT_FREEZE_DATE,
) -> tuple[int, list[dict[str, Any]]]:
    """Interroge l'API ouverte api.crossref.org pour reperer des liens OA."""
    code, data = _api_get_json(
        "https://api.crossref.org/works",
        {"query": query, "rows": rows, "filter": f"from-pub-date:2023-01-01,until-pub-date:{freeze_date}"},
        timeout=timeout,
    )
    if data is None:
        return code, []
    items = data.get("message", {}).get("items", [])
    results: list[dict[str, Any]] = []
    for it in items:
        links = [lnk.get("URL") for lnk in it.get("link", []) if lnk.get("URL")]
        title = (it.get("title") or [""])[0]
        doi = it.get("DOI", "")
        results.append({"doi": doi, "title": title, "links": links, "raw": it})
    return code, results


def search_hal(query: str, rows: int = 10, timeout: int = 25) -> tuple[int, list[dict[str, Any]]]:
    """Interroge l'API ouverte HAL (archives-ouvertes.fr)."""
    code, data = _api_get_json(
        "https://api.archives-ouvertes.fr/search/",
        {"q": query, "rows": rows, "wt": "json", "fl": "halId_s,title_s,authFullName_s,publicationDate_s,fileMain_s"},
        timeout=timeout,
    )
    if data is None:
        return code, []
    return code, data.get("response", {}).get("docs", [])


def search_europepmc(query: str, page_size: int = 10, timeout: int = 25) -> tuple[int, list[dict[str, Any]]]:
    """Interroge l'API ouverte Europe PMC (open access)."""
    code, data = _api_get_json(
        "https://www.ebi.ac.uk/europepmc/webservices/rest/search",
        {"query": f"({query}) AND OPEN_ACCESS:Y", "format": "json", "pageSize": page_size, "resultType": "core"},
        timeout=timeout,
    )
    if data is None:
        return code, []
    return code, data.get("resultList", {}).get("result", [])


def search_doaj(query: str, page_size: int = 10, timeout: int = 25) -> tuple[int, list[dict[str, Any]]]:
    """Interroge l'API ouverte DOAJ."""
    code, data = _api_get_json(
        f"https://doaj.org/api/search/articles/{urllib.parse.quote(query)}",
        {"pageSize": page_size},
        timeout=timeout,
    )
    if data is None:
        return code, []
    return code, data.get("results", [])


def search_ietf_datatracker(query: str, limit: int = 10, timeout: int = 25) -> tuple[int, list[dict[str, Any]]]:
    """Interroge l'API ouverte datatracker.ietf.org."""
    code, data = _api_get_json(
        "https://datatracker.ietf.org/api/v1/doc/document/",
        {"name__icontains": query, "limit": limit, "format": "json"},
        timeout=timeout,
    )
    if data is None:
        return code, []
    return code, data.get("objects", [])


def search_nist_csrc(query: str, timeout: int = 25) -> tuple[int, str]:
    """Interroge le portail ouvert CSRC/nvlpubs du NIST."""
    url = f"https://csrc.nist.gov/publications/search?keywords-lg={urllib.parse.quote(query)}"
    res = fetch_open_source(url, timeout=timeout)
    return int(res.get("http_status") or 0), res.get("text", "") if res.get("status") == "L+" else ""


_DOMAIN_LOCKS: dict[str, threading.Lock] = {}
_DOMAIN_LOCK_GUARD = threading.Lock()


def _fetch_respectful(url: str, timeout: int = 35) -> dict[str, Any]:
    """Serialise les requetes par hote avec courtoisie (0 contournement AO-01)."""
    host = urllib.parse.urlparse(url).netloc.lower()
    with _DOMAIN_LOCK_GUARD:
        lock = _DOMAIN_LOCKS.setdefault(host, threading.Lock())
    with lock:
        res = fetch_open_source(url, timeout=timeout)
        if any(k in host for k in ("arxiv.org", "sec.gov", "nist.gov", "europa.eu", "osfi-bsif.gc.ca", "github.com", "githubusercontent.com")):
            time.sleep(0.25)
        return res


def _run_api_discovery(probes: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Interroge les API ouvertes du protocole MLR et journalise leurs reponses."""
    logs: list[dict[str, Any]] = []
    for probe in probes:
        api = probe.get("api", "")
        query = probe.get("query", "")
        axis = probe.get("axis", "")
        t0 = time.time()
        code = 0
        count = 0
        sample: list[str] = []
        try:
            if api == "arxiv":
                code, items = search_arxiv(query, max_results=5)
                count = len(items)
                sample = [it.get("identifier", "") for it in items[:3]]
            elif api == "crossref":
                code, items = search_crossref_oa(query, rows=5)
                count = len(items)
                sample = [it.get("doi", "") for it in items[:3]]
            elif api == "hal":
                code, items = search_hal(query, rows=5)
                count = len(items)
                sample = [it.get("halId_s", "") for it in items[:3]]
            elif api == "europepmc":
                code, items = search_europepmc(query, page_size=5)
                count = len(items)
                sample = [it.get("pmcid", it.get("pmid", "")) for it in items[:3]]
            elif api == "doaj":
                code, items = search_doaj(query, page_size=5)
                count = len(items)
                sample = [it.get("id", "") for it in items[:3]]
            elif api == "ietf_datatracker":
                code, items = search_ietf_datatracker(query, limit=5)
                count = len(items)
                sample = [it.get("name", "") for it in items[:3]]
            elif api == "nist_csrc":
                code, txt = search_nist_csrc(query)
                count = 1 if txt else 0
                sample = ["nist_csrc_ok" if txt else "empty"]
        except Exception as exc:
            sample = [f"error:{type(exc).__name__}"]
        logs.append(
            {
                "api": api,
                "axis": axis,
                "query": query,
                "http_status": code,
                "hits": count,
                "sample_ids": sample,
                "elapsed_s": round(time.time() - t0, 2),
            }
        )
    return logs


def run_mlr_harvest(book_dir: Path, skip_api_discovery: bool = False) -> int:
    """Execute la collecte ouverte L+, consigne les statuts F (AO-01) et produit le manifeste SHA-256."""
    recherche_dir = book_dir / "recherche"
    corpus_dir = recherche_dir / "corpus_l_plus"
    catalog_path = recherche_dir / "catalogue_mlr_2027.json"
    if not catalog_path.is_file():
        print(f"ERREUR : catalogue introuvable : {catalog_path}", file=sys.stderr)
        return 1

    catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
    protocol_id = catalog.get("protocol_id", DEFAULT_PROTOCOL_ID)
    freeze_date = catalog.get("freeze_date") or get_freeze_date(book_dir)

    api_logs: list[dict[str, Any]] = []
    if not skip_api_discovery:
        api_logs = _run_api_discovery(catalog.get("api_discovery_probes", []))

    blocked_records: list[dict[str, Any]] = []
    with ThreadPoolExecutor(max_workers=6) as pool:
        f_futures = {
            pool.submit(_fetch_respectful, cand["url"], 15): cand
            for cand in catalog.get("blocked_candidates_status_f", [])
        }
        for fut in as_completed(f_futures):
            cand = f_futures[fut]
            res = fut.result()
            reason = res.get("block_reason", "BLOCKED") if res.get("status") == "F" else "EXCLUDED_UNVERIFIED_NON_CATALOG"
            blocked_records.append(
                {
                    "source_hint": cand.get("source_hint", ""),
                    "url": cand["url"],
                    "status": "F",
                    "included_in_evidence": False,
                    "http_status": res.get("http_status"),
                    "block_reason": reason,
                    "reason": reason,
                    "note": cand.get("note", ""),
                    "checked_at": res.get("checked_at"),
                }
            )
    blocked_records.sort(key=lambda x: x["url"])

    l_plus_sources: list[dict[str, Any]] = []
    unexpected_blocks: list[dict[str, Any]] = []
    entries = catalog.get("l_plus_catalog", [])

    def _collect_entry(entry: dict[str, Any]) -> dict[str, Any]:
        if entry.get("pinned_git"):
            pg = entry["pinned_git"]
            return fetch_pinned_git_spec(
                pg["repo_url"],
                pg["ref_or_commit"],
                pg["rel_path"],
                pg["expected_sha256"],
            )
        return _fetch_respectful(entry["url"], 35)

    with ThreadPoolExecutor(max_workers=6) as pool:
        l_futures = {pool.submit(_collect_entry, entry): entry for entry in entries}
        results_by_id: dict[str, tuple[dict[str, Any], dict[str, Any]]] = {}
        for fut in as_completed(l_futures):
            entry = l_futures[fut]
            res = fut.result()
            results_by_id[entry["source_id"]] = (entry, res)

    for entry in entries:
        sid = entry["source_id"]
        _, res = results_by_id[sid]
        if res.get("status") != "L+":
            reason = res.get("block_reason", "UNEXPECTED_BLOCK")
            block_rec = {
                "source_hint": entry.get("title", sid),
                "url": res.get("url", entry.get("url", "")),
                "status": "F",
                "included_in_evidence": False,
                "http_status": res.get("http_status"),
                "block_reason": reason,
                "reason": reason,
                "note": f"Bloque lors de la collecte {sid}; exclu conformement a AO-01.",
                "checked_at": res.get("checked_at"),
            }
            blocked_records.append(block_rec)
            unexpected_blocks.append(block_rec)
            continue

        written = write_corpus_source(corpus_dir, sid, res["text"])
        l_plus_sources.append(
            {
                "source_id": sid,
                "seed_id": entry.get("seed_id"),
                "category": entry["category"],
                "peer_reviewed": bool(entry["peer_reviewed"]),
                "title": entry["title"],
                "authors": entry["authors"],
                "year": int(entry["year"]),
                "publication_date": entry["publication_date"],
                "venue_or_issuer": entry["venue_or_issuer"],
                "identifier": entry["identifier"],
                "url": res.get("url", entry["url"]),
                "status": "L+",
                "metadata_only": False,
                "aacods_score": float(entry["aacods_score"]),
                "research_axes": list(entry["research_axes"]),
                "chapters": list(entry.get("chapters", [])),
                "local_txt_path": f"recherche/corpus_l_plus/{sid}.txt",
                "sha256": written["sha256"],
                "byte_length": written["byte_length"],
                "word_count": written["word_count"],
            }
        )

    statut_f_payload = {
        "protocol_id": protocol_id,
        "freeze_date": freeze_date,
        "ao_01_policy": "ZERO contournement. Toute URL retournee avec HTTP 401/403/429/451, 202 PoW, WAF, CAPTCHA ou mur payant est arretee apres 1 requete et exclue de l'evidence.",
        "blocked": blocked_records,
    }
    (recherche_dir / "registre-statut-f.json").write_bytes(
        (json.dumps(statut_f_payload, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    )

    manifest_payload = build_manifest_payload(
        l_plus_sources, protocol_id=protocol_id, freeze_date=freeze_date
    )
    (recherche_dir / "manifeste-sources-sha256.json").write_bytes(
        (json.dumps(manifest_payload, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    )

    journal_payload = {
        "protocol_id": protocol_id,
        "freeze_date": freeze_date,
        "executed_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "l_plus_count": len(l_plus_sources),
        "status_f_count": len(blocked_records),
        "unexpected_blocks": unexpected_blocks,
        "metadata_only_pct": manifest_payload["metadata_only_pct"],
        "api_discovery_probes": api_logs,
    }
    (recherche_dir / "journal-collecte-mlr.json").write_bytes(
        (json.dumps(journal_payload, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    )

    errors = verify_manifest_integrity(book_dir)
    if errors or unexpected_blocks:
        for blk in unexpected_blocks:
            print(f"BLOQUE (AO-01 F) : {blk['source_hint']} ({blk['url']}) -> {blk['block_reason']}", file=sys.stderr)
        for err in errors:
            print(f"ERREUR INTEGRITE : {err}", file=sys.stderr)
        return 1

    print(
        f"OK : {len(l_plus_sources)} sources L+ ecrites et hachees SHA-256 "
        f"(0 % METADATA_ONLY), {len(blocked_records)} URLs consignees en statut F."
    )
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Collecte MLR ouverte L+ et verification SHA-256 (Compendium)")
    parser.add_argument("--verify", action="store_true", help="Verifie l'integrite du manifeste, des registres et des 37 bases")
    parser.add_argument("--harvest", action="store_true", help="Execute la collecte MLR ouverte L+ selon catalogue_mlr_2027.json")
    parser.add_argument("--skip-api-discovery", action="store_true", help="Saute les requetes de decouverte API lors du --harvest")
    parser.add_argument("--book-dir", type=Path, default=Path(__file__).resolve().parent.parent)
    args = parser.parse_args(argv)

    if args.harvest:
        return run_mlr_harvest(args.book_dir, skip_api_discovery=args.skip_api_discovery)

    if args.verify:
        errors = verify_compendium_evidence(args.book_dir)
        if errors:
            for err in errors:
                print(f"ERREUR : {err}", file=sys.stderr)
            return 1
        print("OK : Manifeste SHA-256, 7 registres SSOT et 37 bases sources integres (0 % METADATA_ONLY).")
        return 0

    parser.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
