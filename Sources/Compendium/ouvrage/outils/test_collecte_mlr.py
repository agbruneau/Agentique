# SPDX-License-Identifier: MIT
"""Tests TDD de la collecte scientifique ouverte L+ et du socle SSOT du Compendium (AO-01, AO-02, SHA-256)."""

from __future__ import annotations

import hashlib
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

import pytest

_TOOLS_DIR = Path(__file__).resolve().parent
_BOOK_DIR = _TOOLS_DIR.parent
if str(_TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(_TOOLS_DIR))

from collecte_mlr_ouverte import (  # noqa: E402
    build_manifest_payload,
    compute_sha256_file,
    extract_text_from_bytes,
    fetch_open_source,
    fetch_pinned_git_spec,
    verify_compendium_evidence,
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
    entry = fetch_open_source("https://genai.owasp.org/restricted.pdf", client=client)
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


def test_pinned_git_spec_accepts_exact_sha256_and_rejects_drift_or_403() -> None:
    spec_bytes = b"export interface McpTool {\n  name: string;\n  description?: string;\n}\n"
    expected_sha = hashlib.sha256(spec_bytes).hexdigest()

    ok_client = CountingClient(
        FakeResponse(
            status_code=200,
            content=spec_bytes,
            headers={"Content-Type": "text/plain; charset=utf-8"},
            url="https://raw.githubusercontent.com/modelcontextprotocol/specification/2026-07-28/schema/2026-07-28/schema.ts",
        )
    )
    ok = fetch_pinned_git_spec(
        "https://github.com/modelcontextprotocol/specification",
        "2026-07-28",
        "schema/2026-07-28/schema.ts",
        expected_sha,
        client=ok_client,
    )
    assert ok["status"] == "L+"
    assert ok["included_in_evidence"] is True
    assert ok["sha256"] == expected_sha
    assert len(ok_client.calls) == 1

    tampered_client = CountingClient(
        FakeResponse(status_code=200, content=b"export interface McpTool { name: number; }\n")
    )
    drift = fetch_pinned_git_spec(
        "https://github.com/modelcontextprotocol/specification",
        "2026-07-28",
        "schema/2026-07-28/schema.ts",
        expected_sha,
        client=tampered_client,
    )
    assert drift["status"] == "F"
    assert drift["included_in_evidence"] is False
    assert "SHA256_MISMATCH" in drift["block_reason"]

    with pytest.raises(ValueError, match="epinglee"):
        fetch_pinned_git_spec(
            "https://github.com/modelcontextprotocol/specification",
            "main",
            "schema/2026-07-28/schema.ts",
            expected_sha,
            client=ok_client,
        )


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
    assert payload["freeze_date"] == "2026-12-02"

    with pytest.raises(ValueError, match="METADATA_ONLY"):
        build_manifest_payload([dict(src_entry, metadata_only=True)])
    with pytest.raises(ValueError, match="statut F|L\\+"):
        build_manifest_payload([dict(src_entry, status="F")])
    with pytest.raises(ValueError, match="2026-12-02"):
        build_manifest_payload([dict(src_entry, publication_date="2026-12-15")])


def _build_minimal_compendium_tree(root: Path) -> dict:
    (root / "specs").mkdir(parents=True, exist_ok=True)
    (root / "recherche" / "corpus_l_plus").mkdir(parents=True, exist_ok=True)
    (root / "registre").mkdir(parents=True, exist_ok=True)
    (root / "sources").mkdir(parents=True, exist_ok=True)

    (root / "specs" / "protocole-mlr-compendium.json").write_text(
        json.dumps(
            {
                "protocol_id": "MLR-PRISMA-SCR-COMPENDIUM-2027-V1.0",
                "freeze_date": "2026-12-02",
                "research_questions_and_queries": [{"id": "RQ1", "min_included_studies": 1}],
            }
        ),
        encoding="utf-8",
    )
    meta = write_corpus_source(root / "recherche" / "corpus_l_plus", "SRC-001", "Texte L+ complet vérifié " * 15)
    manifest = build_manifest_payload(
        [
            {
                "source_id": "SRC-001",
                "category": "preprint",
                "peer_reviewed": False,
                "title": "Étude ouverte",
                "authors": "A. Chercheur",
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
        ],
        protocol_id="MLR-PRISMA-SCR-COMPENDIUM-2027-V1.0",
    )
    (root / "recherche" / "manifeste-sources-sha256.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    (root / "recherche" / "registre-statut-f.json").write_text(
        json.dumps(
            {
                "protocol_id": "MLR-PRISMA-SCR-COMPENDIUM-2027-V1.0",
                "freeze_date": "2026-12-02",
                "blocked": [
                    {
                        "source_hint": "OWASP portal",
                        "url": "https://genai.owasp.org/restricted",
                        "status": "F",
                        "included_in_evidence": False,
                        "http_status": 403,
                        "block_reason": "HTTP_403",
                    }
                ],
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    (root / "registre" / "mindmap-complet.json").write_text(
        json.dumps({"domains": [{}] * 12, "families": [{}] * 71, "themes": [{}] * 260, "relations": [{}] * 616}),
        encoding="utf-8",
    )
    (root / "registre" / "specifications-lplus.json").write_text(
        json.dumps({"specs": [{"spec_id": "SPEC-1", "statut_preuve": "l_plus", "source_l_plus_id": "SRC-001"}]}),
        encoding="utf-8",
    )
    (root / "registre" / "matrice-exig-prr-c40.json").write_text(
        json.dumps({"mappings": [{"id": "S-01"}], "exig_total": 305, "prr_total": 75}),
        encoding="utf-8",
    )
    (root / "registre" / "concordance-taxonomies.json").write_text(
        json.dumps({"div_02": {"divergence_id": "DIV-02"}, "concordances": [{"discordance_id": f"DISC-0{i}"} for i in range(1, 6)]}),
        encoding="utf-8",
    )
    (root / "registre" / "ancres-chronologiques.json").write_text(
        json.dumps({"anchors": [{"key": "ANC-1", "statut_preuve": "l_plus", "source_l_plus_id": "SRC-001"}]}),
        encoding="utf-8",
    )
    (root / "registre" / "faits-empiriques.json").write_text(
        json.dumps({"facts": [{"id": "FACT-1", "statut_preuve": "l_plus", "source_l_plus_id": "SRC-001"}]}),
        encoding="utf-8",
    )
    (root / "registre" / "glossaire-termes.json").write_text(
        json.dumps({"terms": [{"fr": "Systèmes d'agentivité", "statut_preuve": "l_plus", "source_l_plus_id": "SRC-001"}]}),
        encoding="utf-8",
    )

    for idx in range(37):
        content = (
            f"# Base documentaire fermée — ch{idx:02d}\n\n"
            "**Date de gel :** 2 décembre 2026 (`2026-12-02`)\n\n"
            "### [1] SRC-001 — Étude ouverte\n"
            "- **Synthèse factuelle vérifiée :** Fait vérifié sur texte complet L+.\n"
        )
        (root / "sources" / f"ch{idx:02d}-sources.md").write_bytes(content.encode("utf-8"))

    return manifest


def test_ao02_forbids_unanchored_facts_and_checks_37_sources(tmp_path: Path) -> None:
    _build_minimal_compendium_tree(tmp_path)
    assert verify_compendium_evidence(tmp_path) == []

    # 1. Injecter un fait non reancre (AO-02)
    (tmp_path / "registre" / "faits-empiriques.json").write_text(
        json.dumps({"facts": [{"id": "FACT-BAD", "statut_preuve": "a_reancrer", "source_l_plus_id": "Tome 1"}]}),
        encoding="utf-8",
    )
    errs = verify_compendium_evidence(tmp_path)
    assert any("AO-02" in e or "CA-10" in e for e in errs)

    # 2. Restaurer le fait valide puis supprimer ch36-sources.md
    (tmp_path / "registre" / "faits-empiriques.json").write_text(
        json.dumps({"facts": [{"id": "FACT-1", "statut_preuve": "l_plus", "source_l_plus_id": "SRC-001"}]}),
        encoding="utf-8",
    )
    (tmp_path / "sources" / "ch36-sources.md").unlink()
    errs_missing = verify_compendium_evidence(tmp_path)
    assert any("ch36-sources.md" in e for e in errs_missing)

    # 3. Reconstruire ch36 avec une reference SRC-999 absente du manifeste L+
    (tmp_path / "sources" / "ch36-sources.md").write_bytes(
        (
            "# Base — ch36\n\n**Date de gel :** 2 décembre 2026 (`2026-12-02`)\n\n"
            "### [1] SRC-999 — Source fantôme\n"
        ).encode("utf-8")
    )
    errs_orphan = verify_compendium_evidence(tmp_path)
    assert any("SRC-999" in e for e in errs_orphan)


def test_extract_xhtml_utf8_preserves_unicode_and_strips_xml_declaration() -> None:
    xhtml_bytes = (
        '<?xml version="1.0" encoding="utf-8"?>'
        '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">'
        '<html xmlns="http://www.w3.org/1999/xhtml"><body>'
        "<script>var secret = 1;</script>"
        "<article><h1>Loi sur les banques — article 67</h1>"
        "<p>Cessation d\u2019effet : 30 juin 2033 \u00e0 Montr\u00e9al.</p>"
        "</article></body></html>"
    ).encode("utf-8")

    extracted = extract_text_from_bytes(xhtml_bytes, content_type="application/xhtml+xml; charset=utf-8")
    assert "Loi sur les banques — article 67" in extracted
    assert "Montréal" in extracted
    assert "var secret" not in extracted


def test_compendium_production_socle_registries_and_37_sources() -> None:
    """Verifie le socle reel Sources/Compendium/ouvrage : L+ SHA-256, 7 registres SSOT et 37 bases sources/."""
    assert (_BOOK_DIR / "recherche" / "manifeste-sources-sha256.json").is_file()
    assert (_BOOK_DIR / "recherche" / "registre-statut-f.json").is_file()

    # Integrite L+ et statut F
    errors = verify_compendium_evidence(_BOOK_DIR)
    assert errors == [], f"Erreurs socle Compendium : {errors}"

    manifeste = json.loads((_BOOK_DIR / "recherche" / "manifeste-sources-sha256.json").read_text(encoding="utf-8"))
    assert manifeste["freeze_date"] == "2026-12-02"
    assert manifeste["metadata_only_pct"] == 0.0
    assert len(manifeste["sources"]) >= 114

    statut_f = json.loads((_BOOK_DIR / "recherche" / "registre-statut-f.json").read_text(encoding="utf-8"))
    blocked = statut_f.get("blocked", [])
    assert len(blocked) >= 24
    assert all(b.get("status") == "F" and b.get("included_in_evidence") is False for b in blocked)

    # Verification des 7 registres JSON SSOT
    reg_dir = _BOOK_DIR / "registre"
    mindmap = json.loads((reg_dir / "mindmap-complet.json").read_text(encoding="utf-8"))
    assert len(mindmap["domains"]) == 12
    assert len(mindmap["subdomains"]) == 36
    assert len(mindmap["families"]) == 71
    assert len(mindmap["themes"]) == 260
    assert len(mindmap["relations"]) == 616

    matrice = json.loads((reg_dir / "matrice-exig-prr-c40.json").read_text(encoding="utf-8"))
    assert matrice["exig_cre_ia_v1_2"]["total"] == 305
    assert matrice["exig_cre_ia_v1_2"]["repartition_force"] == {"DOIT": 255, "NE_DOIT_PAS": 34, "DEVRAIT": 16}
    assert len(matrice["cap_52"]) == 52
    assert len(matrice["pex_24"]) == 24
    assert matrice["prr_75"]["total"] == 75
    assert matrice["prr_75"]["blocking_count"] == 24
    assert len(matrice["c01_c40_blueprints"]) == 3
    assert len(matrice["cinq_sbb"]) == 5
    assert len(matrice["mappings"]) >= 95

    concordance = json.loads((reg_dir / "concordance-taxonomies.json").read_text(encoding="utf-8"))
    assert concordance["div_02"].get("id") == "DIV-02" or concordance["div_02"].get("divergence_id") == "DIV-02"
    assert [c["discordance_id"] for c in concordance["concordances"]] == [
        "DISC-01",
        "DISC-02",
        "DISC-03",
        "DISC-04",
        "DISC-05",
    ]

    ancres = json.loads((reg_dir / "ancres-chronologiques.json").read_text(encoding="utf-8"))
    assert len(ancres["anchors"]) == 77

    # Verification des 37 bases documentaires ch00..ch36-sources.md
    src_head_re = re.compile(r"^(?:#{1,4}|[-*+])?\s*\[(\d+)\](?:\s+(SRC-\d+))?", re.MULTILINE)
    valid_ids = {s["source_id"] for s in manifeste["sources"]}
    for idx in range(37):
        spath = _BOOK_DIR / "sources" / f"ch{idx:02d}-sources.md"
        assert spath.is_file(), f"Base manquante : {spath}"
        raw = spath.read_bytes()
        assert not raw.startswith(b"\xef\xbb\xbf"), f"BOM interdit dans {spath.name}"
        assert b"\r" not in raw, f"CRLF interdit dans {spath.name}"
        txt = raw.decode("utf-8")
        assert "2 décembre 2026" in txt
        heads = src_head_re.findall(txt)
        assert heads, f"Aucun en-tete [n] SRC-XXX dans {spath.name}"
        for _, sid in heads:
            assert sid in valid_ids, f"{sid} absent du manifeste L+ dans {spath.name}"
