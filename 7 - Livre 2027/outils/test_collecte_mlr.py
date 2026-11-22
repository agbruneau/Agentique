"""Tests TDD de la collecte scientifique ouverte L+ (AO-01, SHA-256, 0 % METADATA_ONLY)."""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from pathlib import Path

import pytest

from collecte_mlr_ouverte import (
    build_manifest_payload,
    compute_sha256_file,
    extract_text_from_bytes,
    fetch_open_source,
    verify_manifest_integrity,
    write_corpus_source,
)


@dataclass
class FakeResponse:
    status_code: int
    content: bytes = b""
    text: str = ""
    headers: dict[str, str] | None = None
    url: str = "https://example.org/resource"

    def __post_init__(self) -> None:
        if self.headers is None:
            self.headers = {"Content-Type": "text/html; charset=utf-8"}
        if not self.text and self.content:
            self.text = self.content.decode("utf-8", errors="replace")


class CountingClient:
    """Client HTTP simule comptant strictement chaque requete sortante."""

    def __init__(self, response: FakeResponse) -> None:
        self.response = response
        self.calls: list[str] = []

    def get(self, url: str, **kwargs: object) -> FakeResponse:
        self.calls.append(url)
        return self.response


def test_http_403_returns_status_f_immediately_without_retry() -> None:
    client = CountingClient(FakeResponse(status_code=403, text="Forbidden by Cloudflare"))
    entry = fetch_open_source("https://example.org/restricted.pdf", client=client)
    assert entry["status"] == "F"
    assert entry["included_in_evidence"] is False
    assert len(client.calls) == 1


def test_http_429_returns_status_f_immediately_without_retry() -> None:
    client = CountingClient(FakeResponse(status_code=429, text="Too Many Requests"))
    entry = fetch_open_source("https://example.org/rate-limited", client=client)
    assert entry["status"] == "F"
    assert entry["included_in_evidence"] is False
    assert len(client.calls) == 1


@pytest.mark.parametrize(
    ("status_code", "body"),
    [
        (202, "<html><title>Making sure you're not a bot - Anubis</title><div>Proof-of-work challenge</div></html>"),
        (200, "<html><body><div class='cf-turnstile'>Verify you are human</div></body></html>"),
        (200, "<html><body>Enable JavaScript and cookies to continue - Attention Required! Cloudflare</body></html>"),
        (200, "<html><body>Subscribe to continue reading this paywall article. Sign in required.</body></html>"),
        (401, "Unauthorized"),
        (451, "Unavailable For Legal Reasons"),
    ],
)
def test_challenge_waf_or_paywall_returns_status_f_without_retry(status_code: int, body: str) -> None:
    client = CountingClient(FakeResponse(status_code=status_code, text=body, content=body.encode("utf-8")))
    entry = fetch_open_source("https://example.org/gated-page", client=client)
    assert entry["status"] == "F"
    assert entry["included_in_evidence"] is False
    assert len(client.calls) == 1


def test_sha256_matches_utf8_file_byte_for_byte(tmp_path: Path) -> None:
    corpus_dir = tmp_path / "recherche" / "corpus_l_plus"
    sample_text = (
        "Ligne 1 : Évaluation empirique à Montréal.\n"
        "Ligne 2 : Coût estimé à 15,5 G\\$ US et signature ML-DSA-65 (3 309 octets).\n"
    )
    meta = write_corpus_source(corpus_dir, "SRC-001", sample_text)
    written_path = corpus_dir / "SRC-001.txt"

    assert written_path.is_file()
    raw_bytes = written_path.read_bytes()
    expected_sha = hashlib.sha256(raw_bytes).hexdigest()

    assert meta["sha256"] == expected_sha
    assert compute_sha256_file(written_path) == expected_sha
    assert meta["byte_length"] == len(raw_bytes)
    assert raw_bytes == sample_text.encode("utf-8")


def test_manifest_enforces_zero_metadata_only_and_freeze_date(tmp_path: Path) -> None:
    corpus_dir = tmp_path / "recherche" / "corpus_l_plus"
    meta = write_corpus_source(corpus_dir, "SRC-001", "Texte intégral vérifié " * 20)
    src_entry = {
        "source_id": "SRC-001",
        "category": "peer_reviewed",
        "peer_reviewed": True,
        "title": "Étude test",
        "authors": "A. Auteur",
        "year": 2026,
        "publication_date": "2026-10-15",
        "venue_or_issuer": "Conférence Test",
        "identifier": "arXiv:2601.00001",
        "url": "https://arxiv.org/abs/2601.00001",
        "status": "L+",
        "metadata_only": False,
        "aacods_score": 11.0,
        "research_axes": ["RQ1"],
        "local_txt_path": "recherche/corpus_l_plus/SRC-001.txt",
        "sha256": meta["sha256"],
        "byte_length": meta["byte_length"],
        "word_count": meta["word_count"],
    }
    payload = build_manifest_payload([src_entry])
    assert payload["metadata_only_pct"] == 0.0
    assert payload["freeze_date"] == "2026-12-31"
    assert len(payload["sources"]) == 1

    bad_metadata = dict(src_entry, metadata_only=True)
    with pytest.raises(ValueError, match="METADATA_ONLY"):
        build_manifest_payload([bad_metadata])

    bad_status_f = dict(src_entry, status="F")
    with pytest.raises(ValueError, match="statut F|L\\+"):
        build_manifest_payload([bad_status_f])

    bad_date = dict(src_entry, publication_date="2027-01-15")
    with pytest.raises(ValueError, match="2026-12-31"):
        build_manifest_payload([bad_date])


def test_verify_manifest_integrity_detects_tampered_file(tmp_path: Path) -> None:
    book_dir = tmp_path
    (book_dir / "specs").mkdir(parents=True)
    (book_dir / "recherche" / "corpus_l_plus").mkdir(parents=True)
    (book_dir / "specs" / "protocole-mlr-2027.json").write_text(
        json.dumps(
            {
                "protocol_id": "MLR-PRISMA-SCR-LIVRE-2027-V1.2",
                "research_questions_and_queries": [
                    {"id": "RQ1", "min_included_studies": 1},
                ],
            }
        ),
        encoding="utf-8",
    )
    meta = write_corpus_source(book_dir / "recherche" / "corpus_l_plus", "SRC-001", "Contenu complet L+ valide.")
    manifest = build_manifest_payload(
        [
            {
                "source_id": "SRC-001",
                "category": "preprint",
                "peer_reviewed": False,
                "title": "Test",
                "authors": "Test",
                "year": 2026,
                "publication_date": "2026-06-01",
                "venue_or_issuer": "arXiv",
                "identifier": "arXiv:2606.00001",
                "url": "https://arxiv.org/abs/2606.00001",
                "status": "L+",
                "metadata_only": False,
                "aacods_score": 10.5,
                "research_axes": ["RQ1"],
                "local_txt_path": "recherche/corpus_l_plus/SRC-001.txt",
                "sha256": meta["sha256"],
                "byte_length": meta["byte_length"],
                "word_count": meta["word_count"],
            }
        ]
    )
    manifest_path = book_dir / "recherche" / "manifeste-sources-sha256.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")

    assert verify_manifest_integrity(book_dir) == []

    # Alterer le fichier .txt sur disque doit echouer le controle SHA-256
    (book_dir / "recherche" / "corpus_l_plus" / "SRC-001.txt").write_bytes(b"Contenu altere")
    errors = verify_manifest_integrity(book_dir)
    assert any("SHA-256" in err for err in errors)


def test_extract_xhtml_utf8_preserves_unicode_and_strips_xml_declaration() -> None:
    xhtml_bytes = (
        '<?xml version="1.0" encoding="utf-8"?>'
        '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">'
        '<html xmlns="http://www.w3.org/1999/xhtml"><body>'
        '<script>var secret = 1;</script>'
        '<article><h1>Loi sur les banques — article 67</h1>'
        '<p>Cessation d\u2019effet : 30 juin 2033 \u00e0 Montr\u00e9al.</p>'
        '</article></body></html>'
    ).encode("utf-8")

    extracted = extract_text_from_bytes(xhtml_bytes, content_type="application/xhtml+xml; charset=utf-8")
    assert "Loi sur les banques — article 67" in extracted
    assert "Montréal" in extracted
    assert "var secret" not in extracted
